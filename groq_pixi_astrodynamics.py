#!/usr/bin/env python3
"""
Astrodynamics Pixi Environment Generator
Generates optimized pixi.toml configurations using Groq AI
"""

import os
import re
import json
import sys
from pathlib import Path
from typing import Optional, Dict, Any

try:
    from groq import Groq
except ImportError:
    print("Error: groq library not installed. Run: pip install groq")
    sys.exit(1)

# ============================================================================
# CONFIGURATION
# ============================================================================

SCRIPT_DIR = Path(__file__).parent
LIBS_FILE = SCRIPT_DIR / "space_astrodynamics_libs.json"
PRESETS_FILE = SCRIPT_DIR / "astrodynamics_presets.json"
FEATURES_FILE = SCRIPT_DIR / "astrodynamics_features.toml"
CHANNELS_FILE = SCRIPT_DIR / "channels_config.json"

PLATFORMS = '["linux-64", "osx-64", "osx-arm64", "win-64"]'

# ============================================================================
# DATA LOADERS
# ============================================================================

def load_libraries() -> Dict[str, Any]:
    if not LIBS_FILE.exists():
        print(f"❌ Error: {LIBS_FILE} not found"); sys.exit(1)
    with open(LIBS_FILE) as f:
        return json.load(f)

def load_presets() -> Dict[str, Any]:
    if not PRESETS_FILE.exists():
        print(f"❌ Error: {PRESETS_FILE} not found"); sys.exit(1)
    with open(PRESETS_FILE) as f:
        return json.load(f)

def load_features() -> str:
    if not FEATURES_FILE.exists():
        print(f"❌ Error: {FEATURES_FILE} not found"); sys.exit(1)
    return FEATURES_FILE.read_text()

def load_channels() -> Dict[str, Any]:
    if not CHANNELS_FILE.exists():
        print(f"❌ Error: {CHANNELS_FILE} not found"); sys.exit(1)
    with open(CHANNELS_FILE) as f:
        return json.load(f)

# ============================================================================
# POST-PROCESSOR  (safety net — fixes LLM drift even when prompt is clear)
# ============================================================================

def sanitize_toml(content: str) -> str:
    """
    Strip known pixi-invalid patterns from LLM output:
      1. Markdown fences
      2. description = "..." inside [feature.*] sections
      3. Duplicate [workspace] headers
      4. Wrong channel URL (bare 'conda-forge' → prefix.dev mirror)
    """
    # 1. Strip markdown fences
    content = re.sub(r"```(?:toml)?\n?", "", content).strip()

    lines = content.splitlines()
    cleaned: list[str] = []
    in_feature_section = False

    for line in lines:
        stripped = line.strip()

        # Track section context
        if re.match(r"^\[feature\.", stripped):
            in_feature_section = True
        elif stripped.startswith("[") and not stripped.startswith("[feature."):
            in_feature_section = False

        # Drop description inside [feature.*]
        if in_feature_section and re.match(r'^description\s*=', stripped):
            continue

        cleaned.append(line)

    content = "\n".join(cleaned)

    # 2. Drop any duplicate [workspace] block (keep first occurrence only)
    # Split on section headers, reassemble skipping extra [workspace] blocks
    section_pattern = re.compile(r"^(\[[^\[\]]+\])", re.MULTILINE)
    parts = section_pattern.split(content)
    # parts = [pre, header1, body1, header2, body2, ...]
    seen_workspace = False
    final_parts: list[str] = [parts[0]]  # text before first header
    i = 1
    while i < len(parts) - 1:
        header = parts[i]
        body   = parts[i + 1]
        if header == "[workspace]":
            if seen_workspace:
                i += 2
                continue   # skip the entire duplicate block
            seen_workspace = True
        final_parts.append(header)
        final_parts.append(body)
        i += 2

    content = "".join(final_parts)

    # 3. Ensure correct channel URL
    content = re.sub(
        r'channels\s*=\s*\["conda-forge"\]',
        'channels = ["https://prefix.dev/conda-forge"]',
        content,
    )

    # 4. Ensure platforms line exists in [workspace]
    if 'platforms = ' not in content:
        # insert after channels line
        content = re.sub(
            r'(channels\s*=\s*\[.*?\])',
            rf'\1\nplatforms = {PLATFORMS}',
            content,
        )

    return content.strip()

# ============================================================================
# GROQ INTEGRATION
# ============================================================================

PIXI_FORMAT_EXAMPLE = f"""\
[workspace]
name = "project-name"
version = "0.1.0"
description = "Project description"
channels = ["https://prefix.dev/conda-forge"]
platforms = {PLATFORMS}

[dependencies]
numpy = "*"
scipy = "*"

[feature.orbital-core]
platforms = {PLATFORMS}
dependencies = {{poliastro = "*", astropy = "*"}}

[feature.visualization]
platforms = {PLATFORMS}
dependencies = {{plotly = "*", jupyter = "*"}}

[environments]
design.features = ["orbital-core", "visualization"]
"""

def create_system_prompt(libs: Dict, presets: Dict, channels: Dict) -> str:
    library_list = "\n".join([
        f"- {lib['name']}: {lib['description']} ({lib['tier']})"
        for category in libs.values()
        if isinstance(category, list)
        for lib in category
    ])

    preset_list = "\n".join([
        f"- {p['name']} ({p['skill_level']}): {p['description']}"
        for p in presets['presets']
    ])

    return f"""You are an expert astrodynamics package manager. Generate valid pixi.toml files.

AVAILABLE LIBRARIES:
{library_list}

AVAILABLE PRESETS (use as starting point):
{preset_list}

STRICT PIXI.TOML RULES — VIOLATION CAUSES INSTALL FAILURE:
1. Only ONE [workspace] section — never repeat it
2. [feature.*] sections MUST NOT have a `description` field — it is not supported
3. [feature.*] sections MUST have a `dependencies` field
4. [feature.*] sections MUST have: platforms = {PLATFORMS}
5. channels must use: ["https://prefix.dev/conda-forge"]
6. platforms in [workspace] must be: {PLATFORMS}
7. Environments syntax: env-name.features = ["feature-name"]
8. Return ONLY raw TOML — no markdown fences, no explanations

CORRECT FORMAT (follow exactly):
{PIXI_FORMAT_EXAMPLE}

WRONG — never do this:
[feature.some-feature]
description = "anything"   # ← ILLEGAL, will break pixi
dependencies = {{...}}
"""


def generate_config(task_description: str, api_key: Optional[str] = None) -> str:
    if not api_key:
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            print("❌ Error: GROQ_API_KEY not set. Export it first.")
            sys.exit(1)

    print("📚 Loading configuration files...")
    libs = load_libraries()
    presets = load_presets()
    channels = load_channels()

    system_prompt = create_system_prompt(libs, presets, channels)

    print("🤖 Calling Groq AI...")
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": f"Task: {task_description}"},
        ],
        temperature=0.2,        # lower = less creative drift
        max_tokens=2000,
    )

    raw = response.choices[0].message.content
    return sanitize_toml(raw)


# ============================================================================
# VALIDATION
# ============================================================================

def validate_pixi_toml(content: str) -> bool:
    ok = True

    if content.count("[workspace]") > 1:
        print("❌ Multiple [workspace] sections"); ok = False

    if "[workspace]" not in content:
        print("❌ Missing [workspace]"); ok = False

    if "[dependencies]" not in content:
        print("❌ Missing [dependencies]"); ok = False

    # Check every feature section for banned description field
    for match in re.finditer(r"(\[feature\.[^\]]+\])(.*?)(?=\n\[|\Z)", content, re.DOTALL):
        section_header = match.group(1)
        section_body   = match.group(2)
        if re.search(r'^\s*description\s*=', section_body, re.MULTILINE):
            print(f"❌ {section_header} has illegal 'description' field"); ok = False
        if not re.search(r'^\s*dependencies\s*=', section_body, re.MULTILINE):
            print(f"⚠️  {section_header} missing 'dependencies' field"); ok = False

    if "https://prefix.dev/conda-forge" not in content:
        print("⚠️  Channel URL should be https://prefix.dev/conda-forge")

    return ok


# ============================================================================
# CLI
# ============================================================================

def save_config(content: str, filename: str = "pixi.toml") -> str:
    filepath = Path(filename)
    filepath.write_text(content)
    return str(filepath.absolute())


def main():
    print("=" * 70)
    print("🚀 Astrodynamics Pixi Environment Generator")
    print("=" * 70)
    print()
    print("Describe your astrodynamics task:")
    print("(e.g. 'Design lunar transfer orbit', 'Analyze satellite telemetry')")
    print()

    task = input("Task: ").strip()
    if not task:
        print("❌ Task cannot be empty"); sys.exit(1)

    try:
        config = generate_config(task)
    except Exception as e:
        print(f"❌ Groq API error: {e}"); sys.exit(1)

    print("\n🔍 Validating...")
    valid = validate_pixi_toml(config)
    print("✓ Validation passed" if valid else "⚠️  Validation issues (review before use)")

    print("\n" + "=" * 70)
    print("Generated pixi.toml:")
    print("=" * 70)
    print(config)
    print("=" * 70 + "\n")

    filepath = save_config(config)
    print(f"✓ Saved to: {filepath}\n")
    print("Next steps:")
    print("  1. pixi lock          # resolve deps")
    print("  2. pixi install       # install default env")
    print("  3. pixi install -e <env-name>   # install specific env")
    print()


if __name__ == "__main__":
    main()

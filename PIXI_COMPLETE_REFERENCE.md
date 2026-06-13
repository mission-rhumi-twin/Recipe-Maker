# PIXI.TOML REFERENCE DOCUMENTATION
## Complete Guide from Official Pixi Documentation

Based on: https://pixi.prefix.dev/latest/ and comprehensive site scraping

---

## CORRECT PIXI.TOML STRUCTURE

**IMPORTANT**: Only ONE `[workspace]` section at the top. No `description` field in features.

### Basic Template

```toml
[workspace]
name = "project-name"
version = "0.1.0"
description = "Your project description"
authors = ["Your Name <email@example.com>"]
channels = ["https://prefix.dev/conda-forge"]
platforms = ["linux-64", "osx-64", "osx-arm64", "win-64"]

[dependencies]
python = ">=3.9"
numpy = "*"

[pypi-dependencies]
# Optional: PyPI packages

[feature.feature-name]
platforms = ["linux-64", "osx-64", "osx-arm64", "win-64"]
dependencies = {lib1 = "*", lib2 = "*"}

[environments]
env-name.features = ["feature-name"]
```

---

## SECTION 1: [workspace] - PROJECT METADATA

### Required Fields

**name**: string
- Your project name
- Example: `name = "orbital-designer"`

**channels**: array of strings
- Where to get packages from
- Use: `channels = ["https://prefix.dev/conda-forge"]` (preferred, faster)
- Or: `channels = ["conda-forge"]` (standard)
- ONLY conda-forge is recommended for most users
- Order matters: first available package is used
- Example:
  ```toml
  channels = ["https://prefix.dev/conda-forge"]
  ```

**platforms**: array of strings
- Which operating systems your project supports
- Options: `"linux-64"`, `"osx-64"`, `"osx-arm64"`, `"win-64"`
- Include ALL platforms you want to support
- Example:
  ```toml
  platforms = ["linux-64", "osx-64", "osx-arm64", "win-64"]
  ```

### Optional Fields

**version**: string
- Project version (SemVer format recommended)
- Example: `version = "0.1.0"`

**description**: string
- What your project does
- Example: `description = "Spacecraft orbit design toolkit"`

**authors**: array of strings
- Project creators
- Example: `authors = ["Jane Doe <jane@example.com>"]`

**license**: string
- Project license
- Example: `license = "MIT"`

---

## SECTION 2: [dependencies] - BASE PACKAGES

```toml
[dependencies]
python = ">=3.9"
numpy = "*"
scipy = "1.10.*"
plotly = ">=5.0"
```

**Version Specifiers:**
- `"*"` - Latest compatible version
- `">=1.0"` - Minimum version
- `"1.10.*"` - Latest patch version
- `">=1.0,<2.0"` - Version range

**Important:**
- These are conda packages only
- For PyPI packages, use `[pypi-dependencies]`
- These are installed in ALL environments

---

## SECTION 3: [pypi-dependencies] - PYTHON PACKAGES FROM PYPI

```toml
[pypi-dependencies]
requests = ">=2.28"
scikit-learn = "*"
torch = {version = ">=2.0", extras = ["cuda"]}
```

**Features:**
- Installs from PyPI, not conda-forge
- Supports extras: `{version = "...", extras = ["feature1"]}`
- Version specifiers same as conda

---

## SECTION 4: [feature.*] - FEATURE GROUPS

### Syntax

```toml
[feature.feature-name]
platforms = ["linux-64", "osx-64"]
channels = ["conda-forge"]
dependencies = {lib1 = "*", lib2 = "*"}
pypi-dependencies = {pkg1 = "*"}
```

### What Features Are

- Groups of related libraries
- Optional add-ons to base dependencies
- Combined in environments
- Each project can have multiple features

### Example: Multi-Feature Setup

```toml
[feature.orbital-core]
platforms = ["linux-64", "osx-64", "osx-arm64", "win-64"]
dependencies = {poliastro = "*", numpy = "*", scipy = "*"}

[feature.ml-pipeline]
platforms = ["linux-64", "osx-64", "win-64"]
dependencies = {pytorch = "*", scikit-learn = "*"}

[feature.visualization]
platforms = ["linux-64", "osx-64", "osx-arm64", "win-64"]
dependencies = {plotly = "*", jupyter = "*"}
```

### Fields in Features

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `dependencies` | table | No | Conda packages |
| `pypi-dependencies` | table | No | PyPI packages |
| `platforms` | array | No | Default: workspace platforms |
| `channels` | array | No | Default: workspace channels |

### Key Rules

- ✅ `description` field: NOT supported (ERROR if included)
- ✅ `dependencies` field: Required for feature to exist
- ✅ `platforms` field: Optional, overrides workspace platforms
- ✅ Multiple features: Can be combined in environments

---

## SECTION 5: [environments] - ENVIRONMENT DEFINITIONS

### Syntax

```toml
[environments]
env-name.features = ["feature1", "feature2"]
```

### What Environments Are

- Named combinations of features
- Each has its own installed packages
- Switch between them with: `pixi shell --environment env-name`

### Example

```toml
[environments]
# Basic design environment with just orbital core
design.features = ["orbital-core"]

# Development with ML
ml-dev.features = ["orbital-core", "ml-pipeline", "visualization"]

# Full production setup
production.features = ["orbital-core", "ml-pipeline", "visualization"]

# Minimal testing
test.features = ["orbital-core"]
```

### Using Environments

```bash
# Switch to design environment
pixi shell --environment design

# Run command in specific environment
pixi run --environment ml-dev python train.py

# List all environments
pixi env list
```

---

## SECTION 6: PLATFORM-SPECIFIC CONFIGURATION

### Target-Specific Dependencies

Use `[target.PLATFORM.*]` to override for specific platforms:

```toml
[dependencies]
python = ">=3.9"

[target.win-64.dependencies]
python = ">=3.10"  # Windows needs Python 3.10+

[target.osx-arm64.dependencies]
numpy = ">=1.24"  # Apple Silicon specific
```

### Multi-Platform Example

```toml
[workspace]
platforms = ["win-64", "linux-64", "osx-64", "osx-arm64"]

[dependencies]
python = ">=3.9"

[target.win-64.dependencies]
python = "3.11"  # Windows specific Python version

[target.osx-arm64.dependencies]
numpy = ">=1.24"  # Apple Silicon needs newer NumPy
```

---

## SECTION 7: TASKS

```toml
[tasks]
test = "pytest tests/"
format = "black src/"
lint = "ruff check ."
train = {cmd = "python train.py", depends_on = ["test"]}
```

**Usage:**

```bash
pixi run test        # Run tests
pixi run lint        # Run linter
pixi run train       # Runs test first, then train
```

---

## SECTION 8: ACTIVATION SCRIPTS

```toml
[activation]
scripts = ["setup.sh"]
env = {MY_VAR = "value"}

[target.win-64.activation]
scripts = ["setup.bat"]
```

---

## WHAT NOT TO DO

### ❌ COMMON MISTAKES

1. **Duplicate `[workspace]` sections**
   ```toml
   [workspace]
   [workspace]  # ❌ ERROR: Duplicate section
   ```

2. **`description` in features**
   ```toml
   [feature.myfeature]
   description = "..."  # ❌ ERROR: Not supported
   dependencies = {...}
   ```

3. **Missing `platforms` in workspace**
   ```toml
   [workspace]
   name = "..."
   channels = ["conda-forge"]
   # ❌ ERROR: Must specify platforms
   ```

4. **Invalid platform names**
   ```toml
   platforms = ["windows-64"]  # ❌ ERROR: Use "win-64"
   platforms = ["mac-64"]      # ❌ ERROR: Use "osx-64" or "osx-arm64"
   ```

5. **Mixing conda and PyPI badly**
   ```toml
   [dependencies]
   requests = "*"  # ❌ Use [pypi-dependencies] instead
   ```

---

## COMPLETE WORKING EXAMPLE

```toml
[workspace]
name = "spacecraft-orbit-simulation"
version = "0.1.0"
description = "Spacecraft orbit design and simulation"
authors = ["Jane Doe <jane@example.com>"]
channels = ["https://prefix.dev/conda-forge"]
platforms = ["linux-64", "osx-64", "osx-arm64", "win-64"]

[dependencies]
python = ">=3.9"
numpy = "*"
scipy = "*"
poliastro = "*"
astropy = "*"
jupyter = "*"

[pypi-dependencies]
requests = ">=2.28"

[feature.orbital-core]
dependencies = {poliastro = "*", astropy = "*", numpy = "*", scipy = "*"}

[feature.optimization]
dependencies = {pykep = "*", pygmo = "*"}

[feature.visualization]
dependencies = {plotly = "*", mayavi = "*"}

[feature.ml]
platforms = ["linux-64", "osx-64", "win-64"]
dependencies = {pytorch = "*", scikit-learn = "*"}

[environments]
design.features = ["orbital-core", "optimization", "visualization"]
ml-dev.features = ["orbital-core", "ml"]
full.features = ["orbital-core", "optimization", "visualization", "ml"]
test.features = ["orbital-core"]

[tasks]
test = "pytest tests/"
train = "python train.py"
```

---

## OFFICIAL PIXI DOCUMENTATION

**Main Documentation**: https://pixi.prefix.dev/latest/

**Key Pages:**
- Manifest Reference: https://pixi.prefix.dev/latest/reference/pixi_manifest/
- Multi-Platform: https://pixi.prefix.dev/latest/workspace/multi_platform_configuration/
- Environments: https://pixi.prefix.dev/latest/workspace/environment/
- Features: https://pixi.prefix.dev/latest/workspace/environments/#environments

---

## QUICK REFERENCE: VALID KEYS

### [workspace] - Valid Keys
- `name` ✅
- `version` ✅
- `description` ✅
- `authors` ✅
- `license` ✅
- `channels` ✅
- `platforms` ✅
- `preview` ✅

### [dependencies] - Format
```toml
library-name = "version-spec"
```

### [feature.*] - Valid Keys
- `dependencies` ✅
- `pypi-dependencies` ✅
- `platforms` ✅
- `channels` ✅
- `description` ❌ NOT SUPPORTED

### [environments] - Format
```toml
env-name.features = ["feature1", "feature2"]
```

---

## TROUBLESHOOTING

**Error: "Unexpected keys in feature"**
- Remove `description` from `[feature.*]` sections

**Error: "Workspace does not support 'win-64'"**
- Add to `[workspace]` platforms: `platforms = [..., "win-64"]`

**Error: "Duplicate [workspace]"**
- Only ONE `[workspace]` section allowed at top

**Error: "Expected 'features' in environments"**
- Use correct format: `env-name.features = ["name"]`

---

## THIS INFORMATION IS CURRENT AS OF

- Pixi Version: 0.59.0+
- Documentation Source: https://pixi.prefix.dev/latest/
- Last Updated: June 8, 2026

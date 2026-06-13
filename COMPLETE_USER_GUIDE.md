# COMPLETE USER GUIDE
## Astrodynamics Pixi Environment Generator

**Version**: 1.0.0 | **Last Updated**: June 8, 2026

---

## TABLE OF CONTENTS

1. [Before You Start](#before-you-start)
2. [Installation](#installation)
3. [Basic Usage](#basic-usage)
4. [Advanced Usage](#advanced-usage)
5. [Understanding Your Generated Config](#understanding-your-generated-config)
6. [Examples](#examples)
7. [Troubleshooting](#troubleshooting)
8. [FAQ](#faq)

---

## BEFORE YOU START

### What This Tool Does

This tool generates a `pixi.toml` configuration file for your astrodynamics project. You provide a description of what you need to build. The tool:

1. ✅ Understands your requirements
2. ✅ Selects appropriate libraries from 70 space-tech options
3. ✅ Organizes them into logical groups (features)
4. ✅ Creates named environments
5. ✅ Generates a complete, tested configuration

You then run `pixi install` to create your development environment.

### What You'll Need

**Absolute Requirements:**
- Python 3.9 or higher
- Internet connection (for Groq AI and package downloads)
- 5-15 GB disk space (for dependencies)

**Optional but Highly Recommended:**
- Pixi package manager (instructions below)
- Git (to version control your config)

### Time Investment

- **First time setup**: 5-10 minutes
- **Generating a config**: < 30 seconds
- **Installing environment**: 1-5 minutes
- **Next time you use it**: < 1 minute

---

## INSTALLATION

### Step 1: Get Python 3.9+

**Check your Python version:**

```bash
python --version
```

You should see something like `Python 3.11.9` or higher.

**If you need Python:**
- macOS: `brew install python@3.11`
- Windows: Download from https://python.org
- Linux: `sudo apt install python3.11`

### Step 2: Install Groq Library

This is the only Python package you need to install:

```bash
pip install groq
```

**Verify it worked:**

```bash
python -c "import groq; print('✓ Groq installed')"
```

### Step 3: Get Your Groq API Key

**Free, takes 2 minutes:**

1. Go to https://console.groq.com
2. Click "Sign Up" (Google or email)
3. Create account and verify email
4. Click "API Keys" on left menu
5. Click "Create API Key"
6. Copy the key (looks like `gsk_...`)
7. Keep it safe (don't share or commit to Git)

### Step 4: Install Pixi (Recommended)

Pixi is the package manager that reads your generated config. This tool generates the config; Pixi uses it.

**macOS/Linux:**

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

**Windows:**

```bash
winget install prefix-dev.pixi
```

**Verify it worked:**

```bash
pixi --version
```

You should see a version number like `0.25.0` or higher.

### Step 5: Download This Tool

**Option A: Clone from GitHub (if available)**

```bash
git clone <repo-url>
cd astrodynamics-pixi-generator
```

**Option B: Download Files Manually**

Download these 5 files into a folder:
- `groq_pixi_astrodynamics.py`
- `space_astrodynamics_libs.json`
- `astrodynamics_presets.json`
- `astrodynamics_features.toml`
- `channels_config.json`

All files must be in the same folder.

### Step 6: Set Your API Key

This tells the tool where to find your Groq API key.

**Temporary (current session only):**

```bash
export GROQ_API_KEY="your-key-here"
```

Replace `your-key-here` with the actual key from Step 3.

**Permanent (all sessions, recommended):**

**On macOS/Linux:**

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export GROQ_API_KEY="your-key-here"
```

Then reload:

```bash
source ~/.bashrc
```

**On Windows:**

Set environment variable via System Properties or PowerShell:

```powershell
[Environment]::SetEnvironmentVariable("GROQ_API_KEY", "your-key-here", "User")
```

**Verify it worked:**

```bash
echo $GROQ_API_KEY  # macOS/Linux
echo %GROQ_API_KEY%  # Windows
```

You should see your key printed (if it shows nothing, try restarting terminal).

---

## BASIC USAGE

### The Simplest Way: 3 Steps

#### Step 1: Run the Tool

```bash
python groq_pixi_astrodynamics.py
```

You'll see:

```
======================================================================
🚀 Astrodynamics Pixi Environment Generator
======================================================================

Describe your astrodynamics task:
(Examples: 'Design lunar transfer orbit', 'Analyze satellite data')

Task: _
```

#### Step 2: Describe Your Task

Type what you want to build. Be specific. Examples:

```
Task: Design a lunar transfer orbit
```

Or:

```
Task: Build a satellite attitude control system with simulation
```

Or:

```
Task: Analyze spacecraft telemetry for anomalies using machine learning
```

Press Enter.

#### Step 3: Get Your Config

The tool will:
- Think for 10-15 seconds
- Show you a `pixi.toml` file with all dependencies
- Save it to `pixi.toml` in your current folder

Example output:

```
======================================================================
Generated pixi.toml:
======================================================================

[workspace]
name = "lunar-transfer-design"
version = "0.1.0"
description = "Design lunar transfer orbit"
channels = ["conda-forge"]

[dependencies]
poliastro = "*"
pykep = "*"
pygmo = "*"
numpy = "*"
scipy = "*"
plotly = "*"
jupyter = "*"
...more...

[feature.orbital-core]
dependencies = {poliastro = "*", astropy = "*", numpy = "*"}

[environments]
design.features = ["orbital-core"]

======================================================================
✓ Saved to: /your/path/pixi.toml

Next steps:
  1. Review: cat pixi.toml
  2. Test: pixi lock
  3. Install: pixi install
```

### Now Install It

```bash
pixi install
```

This creates your environment with all dependencies. It takes 1-5 minutes depending on your internet speed.

**Done!** Your environment is ready to use.

---

## ADVANCED USAGE

### Understanding the Generated Config

Your generated `pixi.toml` has four main sections:

#### Section 1: [workspace]

Metadata about your project:

```toml
[workspace]
name = "orbital-design"                    # Your project name
version = "0.1.0"                          # Version number
description = "Design lunar orbits"        # Description
channels = ["conda-forge"]                 # Where to get packages
```

You can edit the name and description. **Don't change channels.**

#### Section 2: [dependencies]

Base libraries that are always included:

```toml
[dependencies]
numpy = "*"          # Installed in all environments
scipy = "*"
poliastro = "*"
```

The `"*"` means "latest compatible version". You can change it to `"1.24.3"` to pin a specific version.

#### Section 3: [feature.*]

Groups of related libraries. Think of them as optional add-ons:

```toml
[feature.orbital-core]
description = "Core orbital mechanics"
dependencies = {poliastro = "*", astropy = "*"}

[feature.optimization]
description = "Trajectory optimization"
dependencies = {pykep = "*", pygmo = "*"}
```

You can add/remove features. Each feature can be included in multiple environments.

#### Section 4: [environments]

Named environments that combine features:

```toml
[environments]
design.features = ["orbital-core", "optimization"]
test.features = ["orbital-core"]
```

- `design` environment = orbital-core + optimization features
- `test` environment = just orbital-core features

### Using Different Environments

Once installed, activate a specific environment:

```bash
# Use the "design" environment
pixi shell --environment design

# Inside the environment, you can run Python
python my_orbit_script.py

# Exit with: exit
```

Or run a command directly without entering shell:

```bash
pixi run --environment design python my_script.py
```

### Editing Your Config

You can hand-edit `pixi.toml` after generation:

**Add a library:**

```toml
[dependencies]
numpy = "*"
scipy = "*"
my-new-lib = "*"  # Add this line
```

**Remove a library:**

Just delete the line.

**Change a version:**

```toml
numpy = "*"        # Any compatible version
numpy = "1.24.3"   # Specific version
numpy = ">=1.24,<2.0"  # Version range
```

**Create a new feature:**

```toml
[feature.my-feature]
description = "My custom feature"
dependencies = {lib1 = "*", lib2 = "*"}
```

**Create a new environment:**

```toml
[environments]
my-env.features = ["my-feature", "other-feature"]
```

After editing, regenerate the lock file:

```bash
pixi lock
```

### Advanced: Using with Jupyter

Jupyter is included by default. To start a Jupyter notebook:

```bash
pixi run jupyter notebook
```

Or with a specific environment:

```bash
pixi run --environment design jupyter lab
```

### Advanced: Using in Git

**Commit your config (recommended):**

```bash
git add pixi.toml pixi.lock
git commit -m "Add astrodynamics environment"
```

**When a colleague clones your repo:**

```bash
git clone <your-repo>
cd <your-repo>
pixi install
# Done! They have identical environment
```

### Advanced: Using in CI/CD

**In GitHub Actions:**

```yaml
name: Test

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: prefix-dev/setup-pixi@v0.4.1
      - run: pixi run pytest
```

**In GitLab CI:**

```yaml
test:
  image: ubuntu:latest
  script:
    - curl -fsSL https://pixi.sh/install.sh | bash
    - pixi install
    - pixi run pytest
```

---

## UNDERSTANDING YOUR GENERATED CONFIG

### What Are Features?

Features are groups of libraries that work together for a specific purpose:

- **orbital-core**: Fundamental orbit calculations (poliastro, astropy)
- **optimization-stack**: Trajectory optimization (pykep, pygmo)
- **bayesian-inference**: Statistical analysis (pymc, arviz)
- **ml-pipeline**: Machine learning (pytorch, scikit-learn)
- **visualization-3d**: 3D graphics (plotly, mayavi)

**Why separate them?** You might want orbital-core alone for a simple script, but orbital-core + optimization-stack + ml-pipeline for a complex mission simulator.

### What Are Environments?

Environments combine features into specific use cases:

- **design** environment: orbital-core + optimization (for trajectory design)
- **analysis** environment: bayesian-inference + data-processing (for statistics)
- **full** environment: all features (for comprehensive simulation)

**Why separate environments?** Different team members need different tools:
- Analyst needs data-processing + visualization
- Engineer needs dynamics + optimization
- Researcher needs symbolic-math + bayesian-inference

### The pixi.lock File

When you run `pixi lock`, a new file appears: `pixi.lock`

```
[generated with pixi]
inputs-hash = "..."
time = "2026-06-08T..."

[[linux-64.numpy]]
url = "https://..."
sha256 = "abcd1234..."
...
```

**What is this?** An exact specification of every package version your environment uses.

**Why does it matter?** If you commit pixi.lock to Git, anyone who runs `pixi install` gets 100% identical environment. This solves "works on my machine" forever.

---

## EXAMPLES

### Example 1: Beginner - Simple Orbit Visualization

**Task**: "I want to learn orbital mechanics and visualize some orbits"

**Expected Output:**

```toml
[workspace]
name = "orbit-learning"
channels = ["conda-forge"]

[dependencies]
poliastro = "*"
numpy = "*"
scipy = "*"
plotly = "*"
jupyter = "*"

[environments]
learn.features = ["orbital-core", "visualization-basic"]
```

**What you get:**
- poliastro for orbit calculations
- Jupyter for interactive learning
- Plotly for visualizations

**Next steps:**

```bash
pixi install
pixi shell
python
>>> from poliastro.bodies import Earth, Mars
>>> from poliastro.twobody import Orbit
>>> # Your learning code here
```

### Example 2: Intermediate - Satellite Analysis

**Task**: "Analyze satellite telemetry data for anomalies using machine learning"

**Expected Output:**

```toml
[dependencies]
pandas = "*"
polars = "*"
scikit-learn = "*"
xgboost = "*"
plotly = "*"
numpy = "*"
scipy = "*"

[feature.data-processing]
dependencies = {pandas = "*", polars = "*", numpy = "*"}

[feature.ml-basics]
dependencies = {scikit-learn = "*", xgboost = "*"}

[environments]
analysis.features = ["data-processing", "ml-basics", "visualization-basic"]
```

**What you get:**
- Efficient data handling (pandas, polars)
- ML algorithms (scikit-learn, xgboost)
- Data visualization (plotly)

**Next steps:**

```bash
pixi install
pixi run --environment analysis python telemetry_analysis.py
```

### Example 3: Advanced - Full Mission Simulation

**Task**: "Full end-to-end mission simulation with orbital mechanics, dynamics, ML, and visualization"

**Expected Output:**

```toml
[dependencies]
tudatpy = "*"
nyx-space = "*"
pykep = "*"
pygmo = "*"
pytorch = "*"
numpy = "*"
scipy = "*"
plotly = "*"
mayavi = "*"
prefect = "*"
pandas = "*"

[feature.dynamics-core]
dependencies = {tudatpy = "*", nyx-space = "*", numpy = "*"}

[feature.optimization-stack]
dependencies = {pykep = "*", pygmo = "*"}

[feature.ml-pipeline]
dependencies = {pytorch = "*", scikit-learn = "*"}

[feature.visualization-3d]
dependencies = {plotly = "*", mayavi = "*"}

[environments]
simulation.features = ["dynamics-core", "optimization-stack", "ml-pipeline", "visualization-3d", "workflow-automation"]
```

**What you get:**
- High-fidelity dynamics (tudatpy, nyx-space)
- Trajectory optimization (pykep, pygmo)
- Machine learning (pytorch)
- 3D visualization (plotly, mayavi)
- Workflow orchestration (prefect)

**Next steps:**

```bash
pixi install
pixi shell --environment simulation
python full_mission_sim.py
```

---

## TROUBLESHOOTING

### Problem 1: "GROQ_API_KEY not set"

**Error Message:**
```
❌ Error: GROQ_API_KEY environment variable not set
Set it with: export GROQ_API_KEY='your-key-here'
```

**Solution:**

```bash
export GROQ_API_KEY="your-actual-key"
python groq_pixi_astrodynamics.py
```

### Problem 2: "ModuleNotFoundError: groq"

**Error Message:**
```
ModuleNotFoundError: No module named 'groq'
```

**Solution:**

```bash
pip install groq
python groq_pixi_astrodynamics.py
```

### Problem 3: "pixi: command not found"

**Error Message:**
```
pixi: command not found
```

**Solution:**

Install Pixi:

```bash
# macOS/Linux
curl -fsSL https://pixi.sh/install.sh | bash

# Windows
winget install prefix-dev.pixi
```

Then restart your terminal and verify:

```bash
pixi --version
```

### Problem 4: "pixi lock" or "pixi install" fails

**Error Message:**
```
error: unexpected argument '-f' found
```

**Possible causes:**
- You're using old Pixi version
- You're using wrong pixi command syntax

**Solution:**

Update Pixi and use correct commands:

```bash
pixi install --help  # Check available options
pixi lock            # Create lock file
pixi install         # Install environment
```

### Problem 5: Generated config looks wrong

**Symptom**: Missing libraries, weird choices, invalid TOML

**Solution:**

1. Describe your task more specifically:
   - ❌ "Astrodynamics"
   - ✅ "Design lunar transfer orbit with multi-objective optimization"

2. Regenerate:
   ```bash
   rm pixi.toml
   python groq_pixi_astrodynamics.py
   ```

3. If still wrong, manually edit `pixi.toml`:
   ```bash
   nano pixi.toml  # or your editor
   ```

### Problem 6: Installation takes forever

**Symptom**: `pixi install` running for > 10 minutes

**Likely causes:**
- Slow internet
- Large dependency tree
- Many precompiled packages needed

**Solutions:**
- Wait (first install is slowest)
- Check internet speed
- Try again at different time
- Run with progress: `pixi install --verbose`

---

## FAQ

### Q: Do I need to pay for this?

**A:** No. Everything is free:
- This tool: Open source (MIT License)
- Groq API: Free tier (30 requests/min)
- Pixi: Free and open source
- Libraries: All free/open source

### Q: Can I use this for production?

**A:** Yes. The generated `pixi.toml` + `pixi.lock` are production-grade:
- Deterministic (pixi.lock ensures exact same versions)
- Reproducible (works on any machine with same OS/architecture)
- Version controlled (commit to Git)

### Q: Can I edit the generated config?

**A:** Yes. Edit `pixi.toml` to:
- Add/remove libraries
- Create custom features
- Define new environments
- Change versions

After editing:

```bash
pixi lock   # Update lock file
pixi install   # Reinstall
```

### Q: What if I need a library that's not in the list?

**A:** Add it manually to `pixi.toml`:

```toml
[dependencies]
your-new-lib = "*"
```

Then:

```bash
pixi lock
pixi install
```

If library is on conda-forge, it will work.

### Q: Can I use this for Python-only projects?

**A:** Yes. The tool supports any astrodynamics/space-tech work. Some libraries are Python-only, some are compiled (C++, Rust, Fortran).

### Q: What if I want to contribute new libraries or presets?

**A:** This is open source! You can:
- Fork the repo
- Edit `space_astrodynamics_libs.json` to add libraries
- Edit `astrodynamics_presets.json` to add task templates
- Submit a pull request

### Q: Is my API key secure?

**A:** Yes:
- Key never sent to tool code (only to Groq)
- Key read from environment variable
- Key not logged anywhere
- Tool is open source (you can audit it)

### Q: Can I use this offline?

**A:** Partially:
- Generating config requires internet (Groq API)
- Installing with `pixi install` requires internet (downloading packages)
- Once installed, everything works offline

### Q: How do I update my environment?

**A:** Option 1: Regenerate

```bash
rm pixi.toml pixi.lock
python groq_pixi_astrodynamics.py
pixi install
```

Option 2: Manual edit

```bash
nano pixi.toml
pixi lock
pixi install
```

### Q: Can I have multiple environments in one project?

**A:** Yes! Edit `[environments]` in your `pixi.toml`:

```toml
[environments]
dev.features = ["orbital-core", "optimization-stack"]
test.features = ["orbital-core"]
prod.features = ["orbital-core"]
```

Then use:

```bash
pixi shell --environment dev
pixi shell --environment test
pixi shell --environment prod
```

### Q: What if the AI generates something that doesn't work?

**A:** Options:
1. Try describing your task differently and regenerate
2. Manually edit the config
3. Report the issue (GitHub Issues)

We're always improving!

---

## GETTING HELP

### Documentation
- **PROJECT_README.md** - Quick overview
- **PROJECT_REPORT.md** - Technical deep dive
- **TEST_REPORT.md** - Testing & validation results

### Online Resources
- **Pixi Docs**: https://pixi.sh
- **Conda-forge**: https://conda-forge.org
- **Groq Console**: https://console.groq.com
- **Space Tech Libraries**: See links in PROJECT_README.md

### Community
- GitHub Issues: Report problems or request features
- Discord: Pixi community (https://discord.gg/EjwXZeB7Gr)

---

## NEXT STEPS

1. ✅ Follow the installation steps above
2. ✅ Run: `python groq_pixi_astrodynamics.py`
3. ✅ Describe your task
4. ✅ Review generated config
5. ✅ Run: `pixi install`
6. ✅ Start coding!

**Good luck with your space project! 🚀**

---

**User Guide Version**: 1.0  
**Last Updated**: June 8, 2026  
**For Questions**: See FAQ or GitHub Issues

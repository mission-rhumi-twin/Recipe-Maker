# Astrodynamics Pixi Environment Generator
## Complete Setup Manual

**Version**: 2.0  
**Last Updated**: June 12, 2026  
**Platform**: Windows PowerShell (with cross-platform notes)

---

## Table of Contents

1. [Getting the Code from GitHub](#getting-the-code-from-github)
2. [Understanding Python and UV](#understanding-python-and-uv)
3. [Installing Python or UV](#installing-python-or-uv)
4. [Installing Pixi](#installing-pixi)
5. [Setting Up Your Groq API Key](#setting-up-your-groq-api-key)
6. [Running the Application](#running-the-application)
7. [Understanding Pixi Commands](#understanding-pixi-commands)
8. [Finishing Touches](#finishing-touches)
9. [Troubleshooting](#troubleshooting)
10. [Conclusion](#conclusion)

---

## Getting the Code from GitHub

The safest and most professional way to get this project is directly from your company's official GitHub repository. Do not use pull requests or forks unless you know what you are doing.

### Step 1: Navigate to the Repository

Open your browser and go to your company's GitHub repository URL. Your administrator should have provided this to you. It will look something like:

```
https://github.com/your-company/astrodynamics-pixi-generator
```

### Step 2: Download the Code

On the repository page, look for a green button labeled "Code" (usually on the right side, near the top). Click it.

A dropdown menu will appear with several options. Look for "Download ZIP" at the bottom of the menu. Click it. Your browser will download a file called something like `astrodynamics-pixi-generator-main.zip`.

### Step 3: Extract the Files

Navigate to your Downloads folder (or wherever the file was saved). Right-click the ZIP file and select "Extract All..." (on Windows). Choose a location where you want to work. A good choice is your Documents folder or a dedicated Projects folder.

For example: `C:\Users\YourName\Projects\astrodynamics-pixi-generator`

### Step 4: Open the Folder

Once extracted, you should see these files:

- `groq_pixi_astrodynamics.py` (the main script)
- `space_astrodynamics_libs.json` (library database)
- `astrodynamics_presets.json` (preset task templates)
- `astrodynamics_features.toml` (feature definitions)
- `channels_config.json` (package manager configuration)
- `README.md` (project overview)

All of these files must stay in the same folder. Do not move them separately.

### Why Not Clone with Git?

If you are experienced with Git, you could also clone the repository using Git commands. However, if you are new to this, downloading the ZIP file is simpler and safer. It is harder to accidentally make unwanted changes to a ZIP download.

---

## Understanding Python and UV

Before you install anything, you need to understand what Python is and what UV is. You will choose one of them to run this project.

### What is Python?

Python is a programming language. The `groq_pixi_astrodynamics.py` file is written in Python. To run it, you need Python installed on your computer. When you run the script, Python reads the file and executes the instructions inside it.

Python is mature, widely used, and has been around for 30+ years. Most developers know how to use it.

**Pros of Python:**
- Industry standard. If you ever need help, many people know Python
- Works everywhere: Windows, macOS, Linux
- Easy to install and manage
- If you already have Python installed, you are done

**Cons of Python:**
- Can have version conflicts. Different projects might want different Python versions
- Package management (installing libraries) can get messy over time
- Slow to start up the first time you run a script
- If something breaks in your Python installation, the whole system feels broken

### What is UV?

UV is a newer tool created by Astral (the company behind Ruff, a Python code formatter). Think of UV as a modernized, faster, and cleaner version of Python's traditional package management system. It handles installing Python itself and manages your project's dependencies in an isolated, clean environment.

UV is much faster than traditional Python package managers. It is also more reliable because it keeps projects separate from each other.

**Pros of UV:**
- Extremely fast (10-100x faster than traditional tools)
- Keeps your projects isolated (one project's libraries do not interfere with another's)
- Modern and actively maintained
- Automatically manages Python version for you
- Great error messages if something goes wrong
- Recommended by many modern Python developers

**Cons of UV:**
- Newer tool, not as many people know about it yet
- If you find an obscure problem, fewer online solutions exist
- Overkill for simple, one-off scripts (but this project uses it well)

### Which Should You Choose?

**Choose Python if:**
- You already have Python 3.9 or higher installed
- You prefer simplicity and want the fastest setup
- You are new to development and want familiar tools
- You only plan to use this project once

**Choose UV if:**
- You plan to work on multiple Python projects in the future
- You want a modern, fast, and reliable setup
- You are willing to learn a new tool
- You want your projects to never interfere with each other

**Our Recommendation:**

If you are unsure, start with Python. It is simpler. If you find yourself installing multiple Python projects in the future, learn UV for your next project.

---

## Installing Python or UV

### Option A: Installing Python

#### Step 1: Check Your Current Python Version

Open PowerShell (search for "PowerShell" in the Windows search bar and click it). Type this command and press Enter:

```powershell
python --version
```

If this shows Python 3.9 or higher (like `Python 3.11.5`), you already have Python installed and can skip ahead to [Setting Up Your Groq API Key](#setting-up-your-groq-api-key).

If you see an error like "python is not recognized", continue with Step 2.

#### Step 2: Download Python

Go to https://www.python.org/downloads/

Click the large yellow button that says "Download Python 3.12" (or the latest version). A file will download. Run it.

#### Step 3: Install Python

When the installer opens, you will see a window. Important: At the bottom of the window, check the box that says "Add Python to PATH". This lets you use Python from PowerShell.

Then click "Install Now" and wait for installation to complete.

#### Step 4: Verify Installation

Open a new PowerShell window and type:

```powershell
python --version
```

You should see something like `Python 3.12.3`. If you see this, Python is installed correctly.

#### Step 5: Install the Groq Library

You need one Python library installed globally: the Groq library. In PowerShell, type:

```powershell
pip install groq
```

Wait for it to complete. You should see a message saying "Successfully installed groq".

**You are done with Python installation. Skip to [Setting Up Your Groq API Key](#setting-up-your-groq-api-key).**

---

### Option B: Installing UV

#### Step 1: Download and Install UV

Open PowerShell and copy this command exactly. Right-click in PowerShell and select "Paste" to paste it:

```powershell
powershell -ExecutionPolicy BypassCurrentUser -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Press Enter. Wait for the installation to complete. You will see text scrolling. When it stops, close PowerShell completely.

#### Step 2: Verify Installation

Open a new PowerShell window and type:

```powershell
uv --version
```

You should see something like `uv 0.1.24`. If you see this, UV is installed correctly.

#### Step 3: UV Installs Python Automatically

You do not need to install Python separately with UV. UV will automatically download and manage Python for you. You can verify this by typing:

```powershell
uv python list
```

This shows the Python versions UV has available. UV will use the appropriate version automatically.

**You are done with UV installation. Skip to [Setting Up Your Groq API Key](#setting-up-your-groq-api-key).**

---

## Installing Pixi

Pixi is a package manager, similar to pip or conda. It reads the `pixi.toml` file that this project generates and installs all the libraries you need for your astrodynamics work.

### What is Pixi?

Pixi is a tool created by the same people who maintain conda-forge (a huge repository of scientific software). It is faster and more reliable than conda, and it works with the `pixi.toml` file that this project creates.

Think of Pixi as a restaurant menu reader. You tell it what you want (the `pixi.toml` file), and it goes and gets all the ingredients (libraries) you need and sets them up properly.

### Installing Pixi

You have three options. Choose the one that feels most comfortable.

#### Option 1: Install via PowerShell (Recommended for Beginners)

Open PowerShell and copy this command:

```powershell
powershell -ExecutionPolicy BypassCurrentUser -c "irm https://pixi.sh/install.ps1 | iex"
```

Paste it into PowerShell and press Enter. Wait for installation to complete. When done, close PowerShell completely.

Open a new PowerShell window and verify:

```powershell
pixi --version
```

You should see something like `0.25.0`. If you see this, Pixi is installed.

#### Option 2: Direct Installer Download

If you prefer to download and run an installer file manually:

1. Go to https://pixi.sh
2. Look for "Download" or a similar button
3. Download the Windows installer for your system (usually `pixi-x86_64-pc-windows-msvc.msi`)
4. Run the installer file
5. Follow the on-screen instructions
6. When done, verify with `pixi --version` in PowerShell

#### Option 3: Web Download and Manual Setup

If the above two options do not work:

1. Visit https://github.com/prefix-dev/pixi/releases
2. Look for the latest release (highest version number)
3. Under "Assets", download the Windows `.exe` file that matches your system
4. Move the downloaded file to `C:\Program Files\pixi\` (create the folder if needed)
5. Add this folder to your Windows PATH (ask your IT administrator if unsure)
6. Open a new PowerShell and verify with `pixi --version`

### Verifying Pixi Installation

Regardless of which installation method you used, verify it works by opening PowerShell and typing:

```powershell
pixi --help
```

You should see a long list of commands. This means Pixi is ready to use.

---

## Setting Up Your Groq API Key

This project uses artificial intelligence to analyze your requirements and suggest the right libraries. We use Groq's API for this, which is fast and free.

### Note: You Can Use Any AI Provider

While this guide uses Groq as an example, the code supports any AI provider that works via API. If your company uses a different AI service (OpenAI, Anthropic, Azure, etc.), your administrator can modify the code to use that instead. Ask your administrator if you are unsure.

### Creating a Groq Account

#### Step 1: Sign Up

Go to https://console.groq.com in your browser.

Click "Sign Up" or "Create Account". You can sign up with:
- Google account (fastest)
- Email and password

If you use your company email, use that. If you use a personal email, that works too.

#### Step 2: Verify Your Email

If you signed up with email and password, check your email for a verification link. Click it. If you used Google, this step is automatic.

#### Step 3: Create an API Key

Once you are logged in to the Groq console, look on the left side of the screen. You should see a menu. Find and click "API Keys".

You will see a section that says "Create New API Key" or similar. Click it.

A long string of random characters will appear. This is your API key. It looks something like: `gsk_a1b2c3d4e5f6g7h8i9j0...`

Copy this entire string. Do not share it with anyone. Do not post it online.

#### Step 4: Save Your API Key Safely

You will need this key in the next step. For now, paste it somewhere safe and private. You could use:
- A password manager (Bitwarden, 1Password, LastPass)
- A private note file on your computer (not in your project folder)
- A secure shared drive only you can access

Do not save it in your project folder and do not commit it to Git. This is a security best practice.

---

## Running the Application

Now you have everything installed. Time to actually run the project.

### Step 1: Open PowerShell in Your Project Folder

Navigate to the folder where you extracted the project files. For example: `C:\Users\YourName\Projects\astrodynamics-pixi-generator`

Right-click in the empty space inside the folder and select "Open in Terminal" or "Open PowerShell window here". A PowerShell window will open in that folder.

Alternatively, you can open PowerShell manually, then navigate to the folder by typing:

```powershell
cd C:\Users\YourName\Projects\astrodynamics-pixi-generator
```

### Step 2: Create an Environment File

The environment file (called `.env`) stores your API key so the Python script can find it. This keeps your key out of the code itself.

In PowerShell, create this file by typing:

```powershell
New-Item -ItemType File -Name ".env" -Force
```

This creates an empty file named `.env` in your project folder.

### Step 3: Add Your API Key to the Environment File

Open the `.env` file with a text editor. You can use Notepad:

```powershell
notepad .env
```

Notepad will open. Type exactly this (replace the example key with your real key):

```
GROQ_API_KEY=gsk_your_actual_key_here
```

For example:
```
GROQ_API_KEY=gsk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

Save the file (Ctrl+S) and close Notepad.

**Important Security Note**: Do not share this `.env` file. Do not commit it to Git. Add it to `.gitignore` if you use version control. Your API key is private.

### Step 4: Set Up Your Python Environment

#### If You Chose Python:

In PowerShell, create a virtual environment:

```powershell
python -m venv venv
```

This creates a folder called `venv`. Wait for this to complete (it takes 10-20 seconds).

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Your PowerShell prompt should now show `(venv)` at the beginning, like this:

```
(venv) PS C:\Users\YourName\Projects\astrodynamics-pixi-generator>
```

Install dependencies for the project:

```powershell
pip install -r requirements.txt
```

If there is no `requirements.txt` file, install just Groq:

```powershell
pip install groq python-dotenv
```

#### If You Chose UV:

UV automatically manages environments, so you do not need to create a separate one. Just make sure you are in your project folder in PowerShell.

### Step 5: Run the Python Script

Now run the main script. In PowerShell, type:

```powershell
python groq_pixi_astrodynamics.py
```

You should see output like this:

```
======================================================================
Astrodynamics Pixi Environment Generator
======================================================================

Describe your astrodynamics task:
(Examples: 'Design lunar transfer orbit', 'Analyze satellite data')

Task: _
```

The cursor is waiting for you to type.

### Step 6: Describe Your Task

Think about what you want to build. Type a clear description. Examples:

```
Task: Design a lunar transfer orbit with trajectory optimization
```

Or:

```
Task: Analyze satellite telemetry data for anomalies using machine learning
```

Be specific. The more detail you give, the better the tool chooses libraries.

Press Enter.

### Step 7: Wait for the AI to Think

The script will take 10-30 seconds. You will see it thinking. When done, it will print a configuration like this:

```toml
[workspace]
name = "lunar-transfer-design"
version = "0.1.0"
description = "Design lunar transfer orbit with trajectory optimization"
channels = ["conda-forge"]

[dependencies]
poliastro = "*"
pykep = "*"
numpy = "*"
scipy = "*"
...more libraries...
```

The script saves this as `pixi.toml` in your project folder.

### Step 8: Verify Everything Works

Before installing all the libraries, make sure the generated configuration is valid. In PowerShell, type:

```powershell
pixi info
```

This shows information about your `pixi.toml` file. If you see error messages, something is wrong. Go to the [Troubleshooting](#troubleshooting) section.

If everything looks good, continue.

---

## Understanding Pixi Commands

Now that you have a `pixi.toml` file, you need to understand the main Pixi commands. These do the actual work of setting up your development environment.

### The Lock File: `pixi lock`

Before Pixi installs anything, it creates a lock file. This file records exactly which version of each library will be installed. This ensures that everyone working on the project gets the exact same versions.

**When to use it:** Before you run `pixi install` for the first time, and after any time you modify `pixi.toml`.

**How to run it:**

```powershell
pixi lock
```

**What to expect:** You will see text scrolling as Pixi resolves all the dependencies. This takes 30 seconds to 5 minutes depending on how many libraries you have. When done, you should see `pixi.lock` in your project folder.

### Installing Dependencies: `pixi install`

This command actually downloads and installs all the libraries listed in your `pixi.toml` and `pixi.lock` files.

**When to use it:** After running `pixi lock`, or if you modify the configuration.

**How to run it:**

```powershell
pixi install
```

**What to expect:** You will see progress bars and text as Pixi downloads and installs libraries. This can take anywhere from 2-20 minutes depending on how many libraries you need and your internet speed. Be patient. The first installation is always the slowest.

When done, you should see a message like "Installation complete" or similar.

### Activating Your Environment: `pixi shell`

Once installed, you need to enter the environment to use the libraries. Think of it as entering a special room where all your tools are available.

**How to run it:**

```powershell
pixi shell
```

**What to expect:** Your PowerShell prompt will change slightly to show you are in the Pixi environment.

**To exit the environment:** Type `exit` and press Enter.

### Running Commands in Your Environment

You can run a Python script without entering the shell:

```powershell
pixi run python your_script.py
```

This runs the script using the environment but does not put you in the shell. Useful for one-off tasks.

### Understanding Features and Presets

Your `pixi.toml` might contain sections called `[feature.something]`. These are groups of related libraries.

For example:

```toml
[feature.orbital-mechanics]
description = "Core orbital dynamics libraries"
dependencies = {poliastro = "*", astropy = "*", numpy = "*"}

[feature.data-analysis]
description = "Data manipulation and analysis"
dependencies = {pandas = "*", scipy = "*"}
```

**Why features exist:** They organize libraries into logical groups. One environment might use orbital-mechanics but not data-analysis. Another might use both.

You do not need to do anything special with features. Pixi handles them automatically when you run `pixi install`.

### Checking Your Environment

To see what is installed:

```powershell
pixi list
```

This shows all packages in your current environment with their versions.

### Removing and Reinstalling

If something breaks or you want a fresh start:

```powershell
pixi clean
pixi lock
pixi install
```

This removes everything and reinstalls from scratch.

---

## Finishing Touches

### Add .env to Git Ignore (If Using Version Control)

If you use Git to track your code, you must prevent your `.env` file from being uploaded to GitHub. This protects your API key.

Create or edit a file called `.gitignore` in your project folder. Add this line:

```
.env
```

This tells Git to never track or upload your `.env` file.

### Commit Your pixi.lock File

The opposite of `.env`: you should commit your `pixi.lock` file to Git. This ensures everyone on your team gets the exact same library versions.

### Create a README for Your Project

Document what you are building. A good README includes:

- What this project does
- How to set it up (refer to this manual)
- How to run it
- What libraries are used and why

### Organize Your Code

Once your environment is ready, create folders for your actual code:

```
your-project/
├── .env (private, not in Git)
├── .gitignore
├── pixi.toml
├── pixi.lock (in Git)
├── README.md
├── src/
│   └── your_code_here.py
├── data/
│   └── your_data_files.csv
└── notebooks/
    └── exploration.ipynb
```

This structure keeps everything organized.

---

## Troubleshooting

### PowerShell Says "cannot be loaded because running scripts is disabled"

**Error message:** Something like "cannot be loaded because running scripts is disabled on this system."

**What happened:** PowerShell has safety settings preventing script execution. This is common on corporate computers.

**Solution:** Use the bypass method. When running any installation command that starts with `powershell -ExecutionPolicy BypassCurrentUser`, that part handles the security temporarily for just that command.

If you still get errors, ask your IT administrator to allow PowerShell scripts for your user account.

### "Python is not recognized" in PowerShell

**What happened:** PowerShell cannot find Python.

**Solution Option 1:** Python was not added to PATH during installation. Reinstall Python. When the installer opens, make sure to check "Add Python to PATH" before clicking Install.

**Solution Option 2:** You installed Python but PowerShell has not restarted since. Close PowerShell completely and open a new window.

**Solution Option 3:** Python is installed somewhere but not in PATH. You can use the full path to run it:

```powershell
C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe --version
```

Replace the username and version numbers as needed.

### "UV is not recognized" or UV Installation Failed in VS Code Terminal

**What happened:** UV installed successfully, but VS Code's terminal does not see it. Or UV installed but PowerShell does not find it.

**Why this happens:** When you install UV while PowerShell is open, the new installation is not available until you close and reopen PowerShell. VS Code's integrated terminal sometimes has the same issue.

**Solution:**
1. Close VS Code completely
2. Close all PowerShell windows
3. Wait 10 seconds
4. Open PowerShell again (not from VS Code)
5. Type `uv --version`

If it works in regular PowerShell but not VS Code, restart VS Code entirely.

If it still does not work, open VS Code settings (Ctrl+,) and search for "terminal.integrated.inheritEnv". Make sure it is set to true.

### "pixi: command not found"

**What happened:** Pixi installed but PowerShell cannot find it.

**Solution:** Same as the UV solution above. Close everything, reopen PowerShell, and try again.

If that does not work, try the manual installer download method instead of the PowerShell installation.

### Python Runs But Script Fails with "ModuleNotFoundError"

**Error:** Something like "ModuleNotFoundError: No module named 'groq'"

**What happened:** The Groq library is not installed.

**Solution:**

If you are using Python:
```powershell
pip install groq python-dotenv
```

If you are using UV:
```powershell
uv pip install groq python-dotenv
```

Then try running the script again.

### "GROQ_API_KEY not set" Error

**What happened:** The script cannot find your API key.

**Possible causes:**
- Your `.env` file is not in the project folder
- Your `.env` file does not have the key (typo or missed it)
- PowerShell has not reloaded the environment

**Solution:**
1. Check that `.env` exists in your project folder: `ls .env` in PowerShell
2. Check the contents: `Get-Content .env` and make sure you see `GROQ_API_KEY=gsk_...`
3. Close PowerShell completely and open a new window
4. Navigate back to your project folder
5. Try running the script again

### Script Runs but Produces "Invalid TOML" or "Weird Dependencies"

**What happened:** The AI suggested libraries that do not work together, or the output is malformed.

**Solution:**
1. Describe your task more specifically. Instead of "Build an orbital simulator", try "Build an orbital simulator using poliastro with trajectory optimization using PyGMO"
2. Delete the bad `pixi.toml` file: `rm pixi.toml` in PowerShell
3. Run the script again: `python groq_pixi_astrodynamics.py`
4. Provide a more detailed description

If it still generates bad output, manually edit `pixi.toml` using a text editor (Notepad or VS Code) and fix the issues.

### "pixi lock" or "pixi install" Takes Forever (30+ minutes)

**What happened:** Installation is slow.

**Possible causes:**
- Your internet is slow
- You have a very large dependency tree
- Conda-forge is busy
- Your computer is slow

**Solution:**
- Be patient. First installations are always slow. Future installs of the same environment are faster
- Check your internet speed: try downloading something else
- Try at a different time of day
- If you have limited bandwidth, wait until you have better connectivity

You can see progress with:

```powershell
pixi install --verbose
```

### Pixi Says "conflicting dependencies" or "cannot resolve"

**What happened:** Libraries you requested have incompatible requirements.

**Solution:**
1. Try running the generator again with a simpler task description
2. Manually edit `pixi.toml` and remove one of the conflicting libraries
3. Run `pixi lock` to see if it resolves

Some libraries really cannot work together, especially if they need different versions of core dependencies like NumPy.

### Getting Stuck on a Windows Security or Firewall Warning

**What happened:** Windows Defender or a corporate firewall blocks installation.

**Solution:**
- Check if this is expected (corporate environment). Ask IT
- Temporarily disable firewall (if it is your own computer) for installation
- Use a different network if possible (not corporate WiFi, etc)

### Script Runs, Generates Config, But Cannot Run "pixi install"

**Symptoms:** `pixi install` gets stuck or fails with network errors

**Possible causes:**
- Your internet connection dropped
- Conda-forge is temporarily unreachable
- Firewall is blocking package downloads

**Solution:**
- Check internet connection
- Wait a few minutes and try again
- Run with verbose output to see where it gets stuck: `pixi install --verbose`
- If a specific package fails, manually edit `pixi.toml` and remove that library, then try again

### You Installed Everything But Do Not Know What to Do Next

**Solution:** Once your environment is installed, enter it:

```powershell
pixi shell
```

Then start a Python interactive session:

```powershell
python
```

Now you can test importing libraries:

```python
import poliastro
import numpy as np
print("Success!")
exit()
```

If imports work, your environment is ready for actual development work.

### Still Stuck?

If none of these solutions work:

1. Copy the exact error message
2. Search GitHub Issues for your company's project
3. Contact your project administrator or team lead
4. Provide:
   - The exact command you ran
   - The exact error message (copy and paste)
   - Your operating system and Python version (`python --version`)
   - Whether you are using Python or UV

This information helps others solve your problem faster.

---

## Conclusion

You have now completed the full setup for the Astrodynamics Pixi Environment Generator. Your development environment is isolated, reproducible, and ready for sophisticated space technology work.

### What You Have Accomplished

- Downloaded the project securely from GitHub
- Installed a modern Python environment (either with Python or UV)
- Installed Pixi, a fast and reliable package manager
- Set up API access to an AI service
- Generated a project configuration tailored to your needs
- Installed all required libraries
- Verified everything works

### Next Steps for Your Work

1. **Understand your environment**: List installed packages with `pixi list`
2. **Start coding**: Create your Python scripts in an organized folder structure
3. **Document as you go**: Write comments and README files explaining your work
4. **Test regularly**: Make sure your scripts work before committing to version control
5. **Version control**: Commit `pixi.lock` to Git so others get the same environment

### A Note on Maintenance

Your environment is fixed at specific library versions (in `pixi.lock`). This is good because it is reproducible. Over time, as new versions of libraries come out, you might want to update. To do this safely:

1. Create a backup: Copy your project folder
2. Run: `pixi update`
3. Test thoroughly
4. If something breaks, revert from your backup
5. Commit the new `pixi.lock` to Git if everything works

### Final Thought

This setup might seem complex the first time. It is thorough because space technology work is unforgiving. A reliable development environment is worth the investment. Every project you build from here forward will use this same pattern, and it will feel faster each time.

Good luck with your astrodynamics work.

---

**Manual Version**: 2.0  
**Created**: June 12, 2026  
**For updates or corrections**: Contact your project administrator

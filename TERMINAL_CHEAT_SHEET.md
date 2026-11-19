# Terminal & FastAPI — Quick Reference Guide

> You don't need to memorize 50 commands. You need to know the 15–20 you'll actually use every single day in backend engineering, plus a few lifesavers for when things get stuck.

---

## 1. How to Get Inside a Folder (Navigation)

The command is `cd` = **C**hange **D**irectory.

```bash
cd FASTAPI          # Enter the folder named FASTAPI in current location
cd ~/FASTAPI        # Enter FASTAPI located in your user home folder (~ means /Users/yourusername)
```

| Command | Short Use Case | Why / When to use it |
| :--- | :--- | :--- |
| `cd ..` | Go one folder back | When you are inside `Codes/` and need to get back to the project root `FASTAPI/`. |
| `cd ~` | Go to your Home directory | Instantly jump to your Mac user root from anywhere. |
| `cd /` | Go to system root | Takes you to the top-most level of your Mac's filesystem. |
| `cd -` | Return to previous directory | Quick toggle between your current folder and the one you just came from. |
| `pwd` | Print Working Directory | Answers: *"Where on my Mac am I right now?"* Prevents running commands in the wrong folder. |

---

## 2. How to Open a Folder / Editor

Useful shortcuts on macOS:

| Command | Short Use Case | Why / When to use it |
| :--- | :--- | :--- |
| `code .` | Open current folder in VS Code | Quickly open the active project workspace in VS Code. |
| `open .` | Open current folder in Finder | Visual inspection of files, images, or folder contents in macOS Finder. |
| `code ~/FASTAPI` | Open specific path in VS Code | Launch your project in VS Code from any terminal tab without `cd`-ing first. |
| `open ~/FASTAPI` | Open specific path in Finder | Launch Finder directly to your project from anywhere. |

> **Note:** If `code` says *command not found*, open VS Code, press `Cmd + Shift + P`, search for `Shell Command: Install 'code' command in PATH`, and run it.

---

## 3. Daily Terminal Commands

### A. Navigation & File Management

| Command | Short Use Case | Why / When to use it |
| :--- | :--- | :--- |
| `pwd` | Show current directory path | Check your absolute folder path before running setup commands. |
| `ls` | List visible files and folders | See what is inside the current directory. |
| `ls -la` | List all files, including hidden (`.`) ones | Check for hidden files like `.venv`, `.gitignore`, and `.env`. |
| `mkdir <foldername>` | Create a new folder | E.g., `mkdir Codes` or `mkdir tests`. |
| `touch <filename>` | Create an empty file | E.g., `touch main.py` or `touch .env`. |
| `cat <filename>` | Print file contents to terminal | Quickly inspect a file (like `cat requirements.txt`) without opening VS Code. |
| `mv <old> <new>` | Rename or move a file/folder | E.g., `mv old_file.py new_file.py` to rename, or `mv main.py Codes/` to move. |
| `cp <source> <dest>` | Copy a file | E.g., `cp .env.example .env` to duplicate a template configuration. |
| `rm <filename>` | Delete a single file | Permanently remove a file (careful: terminal deletes skip the Trash!). |
| `rm -rf <foldername>` | Delete a directory and contents | **Use with caution!** Handy for deleting corrupt `__pycache__` or recreating `.venv`. |
| `clear` | Clean the terminal screen | Clear away long logs and clutter so you can focus on the next output. |

---

### B. Python & Virtual Environment (`.venv`)

| Command | Short Use Case | Why / When to use it |
| :--- | :--- | :--- |
| `python3 --version` | Verify Python version | Make sure you are running a supported Python version (e.g., 3.10+). |
| `python3 -m venv .venv` | Create virtual environment | Isolates your project's libraries so they don't break other Python projects. |
| `source .venv/bin/activate` | Activate virtual environment | **Must run every new terminal session!** Your prompt will show `(.venv)`. |
| `which python` | Verify active Python interpreter | Confirms whether you are using the `.venv` Python or the Mac system Python. |
| `deactivate` | Exit the virtual environment | Leave the isolated environment when done working. |
| `pip install <package>` | Install package into active env | E.g., `pip install fastapi uvicorn pydantic`. |
| `pip install -r requirements.txt` | Install all dependencies listed in file | Use when cloning the repo on another machine or setting up a clean environment. |
| `pip freeze` | Display installed packages & versions | Check exact versions of all libraries in your environment. |
| `pip freeze > requirements.txt` | Save packages to file | Keep an accurate record of dependencies so others can reproduce your setup. |
| `pip show <package>` | Inspect an installed package | E.g., `pip show fastapi` to verify its version and location. |

---

### C. FastAPI & Server Execution (Uvicorn)

| Command | Short Use Case | Why / When to use it |
| :--- | :--- | :--- |
| `uvicorn Codes.main:app --reload` | Run FastAPI server with file in subfolder | When your file is inside `Codes/`, tell Uvicorn the module path `Folder.file:app`. |
| `uvicorn main:app --reload` | Run server (root file) | Starts local development server with auto-reload whenever you save a file. |
| `uvicorn Codes.main:app --reload --port 8080` | Run server on custom port | Useful if another service is already using the default port 8000. |
| `CTRL + C` | Stop the running Uvicorn server | Gracefully terminate your web server process. |

#### Browser URLs to Bookmark:
- **Interactive API Documentation (Swagger UI):** `http://127.0.0.1:8000/docs`
- **Alternative API Documentation (ReDoc):** `http://127.0.0.1:8000/redoc`

#### Quick API Testing from Terminal:
| Command | Short Use Case |
| :--- | :--- |
| `curl http://127.0.0.1:8000/` | Quick GET request directly from the terminal without opening a browser. |
| `curl -X POST http://127.0.0.1:8000/users -H "Content-Type: application/json" -d '{"name":"Neeraj","age":22}'` | Quick POST request to test endpoints accepting JSON payloads. |

---

### D. Process & Port Debugging (The "Port Already in Use" Fix)

Every backend developer faces `[Errno 48] Address already in use` when a background process doesn't close properly.

| Command | Short Use Case | Why / When to use it |
| :--- | :--- | :--- |
| `lsof -i :8000` | Find what process is using port 8000 | Shows the Process ID (`PID`) holding your port hostage. |
| `kill -9 <PID>` | Force stop the stuck process | Replace `<PID>` with the number from `lsof` (e.g. `kill -9 12345`) to free the port. |

---

### E. Git & GitHub (Version Control)

| Command | Short Use Case | Why / When to use it |
| :--- | :--- | :--- |
| `git init` | Initialize Git repo | Run once when starting a new project. |
| `git status` | Check working tree status | Shows modified, untracked, and staged files. Run this before and after committing! |
| `git diff` | Show exact line changes | See code additions (green `+`) and deletions (red `-`) before staging. |
| `git diff --staged` | Show changes in staged files | Verify what will be included in the upcoming commit. |
| `git add <filename>` | Stage specific file | Best practice: stage intentionally rather than blindly adding everything. |
| `git add .` | Stage all modified & new files | Fast staging for all project changes. |
| `git restore <filename>` | Discard unstaged changes in a file | Reset a file back to its last committed state if an experiment went wrong. |
| `git restore --staged <filename>` | Unstage a file | Removes file from staging area without losing your written code. |
| `git commit -m "feat: description"` | Save snapshot of staged changes | Records permanent version with a clear message explaining *what* and *why*. |
| `git branch` | List local branches | See all branches and the current one marked with `*`. |
| `git checkout -b <branch-name>` | Create and switch to new branch | E.g., `git checkout -b feature/user-auth` to build a feature safely. |
| `git switch <branch-name>` | Switch between existing branches | E.g., `git switch main` to switch back to your main branch. |
| `git stash` | Temporarily shelve uncommitted work | Cleans your working directory so you can switch branches without committing unfinished work. |
| `git stash pop` | Restore shelved work | Reapplies your shelved changes onto the current branch. |
| `git log --oneline` | View compact commit history | See commit hashes and titles in a clean, one-line format. |
| `git remote -v` | Inspect remote repository URLs | Verify your GitHub `origin` push and fetch links. |
| `git pull origin main` | Download & merge latest GitHub changes | Keep your local copy up-to-date with your remote repo. |
| `git push origin <branch-name>` | Upload local commits to GitHub | Share your code or back it up to GitHub. |

---

## 4. Daily FastAPI Workflow (Best Practice Rhythm)

### Step 1: Starting Your Day / Session
```bash
# 1. Navigate to your project root
cd ~/FASTAPI

# 2. Open VS Code (if not already open)
code .

# 3. Activate your virtual environment
source .venv/bin/activate

# 4. Verify you're in the right python environment (should point inside .venv)
which python

# 5. Start your FastAPI server (adjust path to where your app instance lives)
uvicorn Codes.main:app --reload
```

---

### Step 2: During Development
- Write code in VS Code.
- Watch the Uvicorn terminal output for syntax errors or reload confirmations.
- Test endpoints in your browser at `http://127.0.0.1:8000/docs`.

---

### Step 3: Saving & Committing Your Progress
```bash
# 1. Check what files you touched
git status

# 2. Review the exact code changes
git diff

# 3. Stage the files
git add Codes/crud_operations.py

# 4. Commit with a meaningful conventional message
git commit -m "feat: add user update endpoint with query parameter"

# 5. Push to GitHub
git push origin <branch-name>
```

---

### Step 4: Wrapping Up
```bash
# 1. Stop the server
CTRL + C

# 2. Deactivate the virtual environment
deactivate
```

---

## 5. Golden Rules for Beginners

1. **Always check for `(.venv)` in your prompt:**
   If you run `pip install` without activating `.venv`, packages install globally into macOS and can break system tools or cause "module not found" errors in VS Code.
2. **Never commit `.venv`:**
   Ensure `.venv` is in your `.gitignore` file. Dependencies are shared via `requirements.txt`, not raw virtual environment folders.
3. **Know where your file lives:**
   If your file is `/Codes/main.py`, the command is `uvicorn Codes.main:app --reload`, NOT `uvicorn main:app --reload`.

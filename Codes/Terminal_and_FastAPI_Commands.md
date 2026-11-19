# Terminal & FastAPI — Master Reference Guide

> A practical, day-to-day command reference for Python backend engineers learning FastAPI. Each command includes a clear, short use case and explanation.

---

## 1. Directory Navigation & Folder Access

The primary command for moving between directories is `cd` (**C**hange **D**irectory).

| Command | Short Use Case | Practical Explanation |
| :--- | :--- | :--- |
| `pwd` | Show current directory | Prints your working directory so you know exactly where you are in the filesystem. |
| `cd foldername` | Enter a subfolder | Moves down into a folder (e.g., `cd Codes` or `cd FASTAPI`). |
| `cd ..` | Go back one folder | Moves up to the parent directory (e.g., from `FASTAPI/Codes` back to `FASTAPI`). |
| `cd ~` | Go to Home directory | Instantly jump to `/Users/<username>` from anywhere. |
| `cd /` | Go to System Root | Moves to the top-most level of your operating system. |
| `cd -` | Return to previous directory | Quick toggle between your current directory and the last folder you were in. |

---

## 2. Opening Folders & Editors (macOS Shortcuts)

| Command | Short Use Case | Practical Explanation |
| :--- | :--- | :--- |
| `code .` | Open current folder in VS Code | Launches your current directory as an active project workspace. |
| `open .` | Open current folder in Finder | Opens the current directory in macOS Finder for visual file management. |
| `code ~/FASTAPI` | Open project in VS Code from anywhere | Open the project without needing to `cd` into it first. |
| `open ~/FASTAPI` | Open project in Finder from anywhere | Open the project in Finder from any terminal window. |

> **VS Code Tip:** If `code .` displays *command not found*, open VS Code, press `Cmd + Shift + P`, type `Shell Command: Install 'code' command in PATH`, and press Enter.

---

## 3. File Operations & Inspection

| Command | Short Use Case | Practical Explanation |
| :--- | :--- | :--- |
| `ls` | List visible files | See standard files and folders in your current directory. |
| `ls -la` | List all files with details | Displays permissions, sizes, and hidden files (such as `.venv`, `.gitignore`, `.env`). |
| `ls -lh` | List files with human-readable sizes | Shows file sizes in KB, MB, or GB instead of raw bytes. |
| `mkdir foldername` | Create a new folder | E.g., `mkdir routers` or `mkdir tests`. |
| `mkdir -p parent/child` | Create nested folders | Creates both the parent and child folders in a single command without erroring. |
| `touch filename.py` | Create an empty file | Quickly create files like `touch models.py` or `touch .env`. |
| `cat filename` | Print entire file in terminal | Read short files (like `requirements.txt`) directly in the terminal. |
| `head -n 10 filename` | View first 10 lines | Inspect the beginning/headers of large files or logs. |
| `tail -n 10 filename` | View last 10 lines | Inspect recent log entries or the end of a file. |
| `cp source.py backup.py` | Copy a file | Duplicate a file before experimenting or making risky changes. |
| `mv old.py new.py` | Rename or move a file | Rename a file or move it into another directory (`mv test.py Codes/`). |
| `rm filename` | Delete a file permanently | Removes a file. **Warning:** Terminal deletions bypass macOS Trash! |
| `rm -rf foldername` | Force delete folder and contents | Use with extreme caution. Useful for clearing corrupt `__pycache__` or `.venv`. |
| `find . -name "*.py"` | Search for Python files | Recursively finds all Python files in the current folder tree. |
| `clear` | Clear terminal screen | Resets cluttered output so you can focus on new logs. |
| `history` | View previous commands | Review previously typed commands if you forget a specific flag or sequence. |

---

## 4. Python & Virtual Environment Management (`.venv`)

Virtual environments isolate your project packages so they do not conflict with system tools or other Python versions.

| Command | Short Use Case | Practical Explanation |
| :--- | :--- | :--- |
| `python3 --version` | Verify Python version | Confirms that Python 3.10+ is installed and active. |
| `python3 -m venv .venv` | Create virtual environment | Sets up a private `.venv` directory for your project's dependencies (run once). |
| `source .venv/bin/activate` | Activate virtual environment | **Run this in every new terminal window.** Your prompt will prefix `(.venv)`. |
| `deactivate` | Exit virtual environment | Leaves the virtual environment when you are done working. |
| `which python` / `command -v python3` | Verify active interpreter path | Confirms whether the terminal is using `.venv/bin/python` or the system Python. |
| `python3 -m pip install --upgrade pip` | Upgrade pip | Ensures package installer has the latest security and wheel support. |
| `pip install package-name` | Install package into `.venv` | E.g., `pip install fastapi uvicorn pydantic`. |
| `pip install -r requirements.txt` | Install all dependencies | Recreates the exact environment from a shared dependency file. |
| `pip freeze` | List installed packages | Displays all packages and their exact versions. |
| `pip freeze > requirements.txt` | Export dependency snapshot | Saves dependencies so teammates or servers can reproduce your setup. |
| `pip show fastapi` | Inspect an installed package | Shows installed version, author, location, and dependencies. |
| `pip uninstall package-name` | Remove an unused package | Cleans up packages you no longer need. |
| `python3 filename.py` | Run a script directly | Executes a standalone Python file. |

---

## 5. FastAPI & Uvicorn Server Operations

| Command | Short Use Case | Practical Explanation |
| :--- | :--- | :--- |
| `uvicorn Codes.main:app --reload` | Run server with file inside subfolder | Use when `main.py` is inside `Codes/`. Format: `<folder>.<file>:<app_instance>`. |
| `uvicorn main:app --reload` | Run server with file in root | Starts the development server with live reload on code changes. |
| `uvicorn main:app --port 8080 --reload` | Run on a different port | Useful when port 8000 is occupied by another application. |
| `uvicorn main:app --host 0.0.0.0 --port 8000` | Expose to local network | Allows testing your API from a mobile phone or another device on your WiFi. |
| `CTRL + C` | Stop development server | Gracefully halts the Uvicorn server process. |

### Essential FastAPI Browser Endpoints:
- **Interactive Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc Documentation:** `http://127.0.0.1:8000/redoc`
- **OpenAPI Schema (JSON):** `http://127.0.0.1:8000/openapi.json`

### Testing Endpoints via Terminal (`curl`):
```bash
# 1. Quick GET request
curl http://127.0.0.1:8000/

# 2. Quick POST request with JSON payload
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Neeraj", "age": 22}'
```

---

## 6. Process & Port Troubleshooting

When you see: `ERROR: [Errno 48] Address already in use`, another process is holding port 8000.

| Command | Short Use Case | Practical Explanation |
| :--- | :--- | :--- |
| `lsof -i :8000` | Identify process using port 8000 | Lists the Process ID (`PID`) holding the port. |
| `kill -9 <PID>` | Force terminate stuck process | Replace `<PID>` with the numeric ID from `lsof` (e.g. `kill -9 54321`). |

---

## 7. Git & GitHub Workflow (Version Control)

| Command | Short Use Case | Practical Explanation |
| :--- | :--- | :--- |
| `git init` | Initialize Git repo | Starts version tracking in the current directory. |
| `git clone <url>` | Download remote repo | Clones an existing GitHub repository to your local machine. |
| `git status` | Check working tree | Shows modified, untracked, and staged files. **Run often!** |
| `git diff` | View unstaged changes | Shows exact line-by-line differences before staging. |
| `git diff --staged` | View staged changes | Reviews lines that are queued up for the next commit. |
| `git add filename` | Stage specific file | Best practice: stage intentionally rather than everything at once. |
| `git add .` | Stage all changes | Stages all new and modified files in the working directory. |
| `git add -p` | Interactively stage parts of a file | Allows staging specific chunks/lines while leaving others unstaged. |
| `git commit -m "feat: message"` | Commit staged changes | Records a permanent snapshot with a concise explanation. |
| `git commit -am "message"` | Stage & commit tracked files | Shortcut to stage modified tracked files and commit in one step. |
| `git restore filename` | Discard unstaged changes | Reverts a file to its last committed state if an edit broke things. |
| `git restore --staged filename` | Unstage a file | Removes file from staging area without losing any written code. |
| `git branch` | List local branches | Displays existing branches with an asterisk `*` on the active one. |
| `git switch -c feature-name` | Create & switch to new branch | Modern syntax to start a new feature or experiment branch safely. |
| `git switch branch-name` | Switch between branches | Switches active working directory to an existing branch. |
| `git stash` | Shelve uncommitted work | Temporarily hides uncommitted edits so you can cleanly switch branches. |
| `git stash pop` | Reapply shelved work | Restores your temporarily shelved changes onto your current branch. |
| `git fetch origin` | Download remote updates | Fetches changes from GitHub without merging them into local files. |
| `git pull origin main` | Pull & merge latest code | Downloads and merges the newest changes from GitHub. |
| `git push -u origin branch-name` | Push & set upstream tracking | Uploads a new branch to GitHub and configures default remote tracking. |
| `git log --oneline` | View compact commit history | Clean view of recent commit hashes and descriptions. |
| `git log --oneline --all --graph` | View visual branch tree | See branching and merging history across all branches. |

---

## 8. Daily FastAPI Developer Workflow

Follow this repeatable routine every time you code:

### Start of Session:
```bash
cd ~/FASTAPI
code .
source .venv/bin/activate
which python                  # Confirm you are inside .venv
uvicorn Codes.main:app --reload
```

### During Development:
- Write code in VS Code.
- Check terminal output for server reloads and error tracebacks.
- Test endpoints interactively at `http://127.0.0.1:8000/docs`.

### Saving Work:
```bash
git status                    # 1. See what changed
git diff                      # 2. Review the code changes
git add .                     # 3. Stage changes
git commit -m "feat: add user schema validation"
git push origin <branch-name> # 4. Sync with GitHub
```

### End of Session:
```bash
CTRL + C                      # Stop server
deactivate                    # Exit virtual environment
```

---

## 9. Critical Rules to Remember

1. **Virtual Environment Isolation:** Never run `pip install` without checking for `(.venv)` in your terminal prompt.
2. **Git Hygiene:** Never commit `.venv/`, `.env`, or `__pycache__/`. Keep them in `.gitignore`.
3. **Module Resolution:** If your code lives in a folder (e.g., `Codes/`), run `uvicorn Codes.<file>:app --reload`, not `uvicorn <file>:app --reload`.
4. **Destructive Commands:** Commands like `rm`, `rm -rf`, and `git restore` permanently delete or discard code. Verify paths before running them.

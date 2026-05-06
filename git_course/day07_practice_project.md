### &larr; [Day 6 — Workflows & Best Practices](day06_workflows_best_practices.md) | [Index](index.md) |

---

# Git Learning Curriculum
## Day 7 — Practice Project & Review

> **Goal:** Bring everything together. Build a complete project from scratch using professional Git practices, then review the full week and map your path forward.

---

## Table of Contents
1. [What You've Learned This Week](#1-what-youve-learned-this-week)
2. [The Graduation Project — Personal Portfolio CLI Tool](#2-the-graduation-project--personal-portfolio-cli-tool)
3. [Phase 1 — Repository Setup](#3-phase-1--repository-setup)
4. [Phase 2 — Feature Development with GitHub Flow](#4-phase-2--feature-development-with-github-flow)
5. [Phase 3 — Deliberate Conflict & Resolution](#5-phase-3--deliberate-conflict--resolution)
6. [Phase 4 — History Cleanup with Interactive Rebase](#6-phase-4--history-cleanup-with-interactive-rebase)
7. [Phase 5 — Release & Tagging](#7-phase-5--release--tagging)
8. [Week in Review — Command Reference](#8-week-in-review--command-reference)
9. [Common Mistakes & How to Avoid Them](#9-common-mistakes--how-to-avoid-them)
10. [Git Cheat Sheet — One Page](#10-git-cheat-sheet--one-page)
11. [What to Learn Next](#11-what-to-learn-next)

---

## 1. What You've Learned This Week

Before diving into the project, take a moment to appreciate the ground you've covered:

```
Day 1 — Foundation
  ✅ What version control is and why it exists
  ✅ git init, git config, git status
  ✅ The .git folder and what lives inside it

Day 2 — Core Workflow
  ✅ The three states: working directory, staging area, repository
  ✅ git add, git commit, git log, git diff, git show
  ✅ Writing meaningful commit messages

Day 3 — Branching & Merging
  ✅ What a branch actually is (a pointer to a commit)
  ✅ git branch, git switch, git merge
  ✅ Fast-forward vs three-way merges
  ✅ Creating and resolving merge conflicts

Day 4 — Remote Collaboration
  ✅ git clone, git remote, git push, git fetch, git pull
  ✅ SSH setup and GitHub authentication
  ✅ The fork → clone → push → pull request workflow
  ✅ Remote tracking branches and upstream tracking

Day 5 — Undoing Things
  ✅ git restore, git stash, git revert, git reset
  ✅ Interactive rebase (git rebase -i)
  ✅ git reflog as a safety net
  ✅ The golden rule: revert for shared history, reset for local

Day 6 — Workflows & Best Practices
  ✅ Git Flow, GitHub Flow, Trunk-Based Development
  ✅ .gitignore — what to exclude and why
  ✅ git tag and semantic versioning
  ✅ Branch protection rules and Git hooks
  ✅ Team best practices for commits, PRs, and repo hygiene
```

Today you apply all of it — not in isolated exercises, but in a single, cohesive, realistic project.

---

## 2. The Graduation Project — Personal Portfolio CLI Tool

You'll build a simple **markdown-based notes manager** called `noted`. It's a command-line tool that lets users create, list, and delete notes — stored as plain text files.

The project itself is intentionally simple. The focus is entirely on **how you use Git**, not on the complexity of the code.

### Requirements Checklist

By the end of today, your repository must have:

- [ ] A proper `README.md` with setup instructions
- [ ] A `.gitignore` configured for the project
- [ ] At least **5 meaningful commits** with well-written messages
- [ ] At least **3 feature branches** created and merged via pull request
- [ ] **1 intentional merge conflict** created and resolved
- [ ] **1 interactive rebase** used to clean up history
- [ ] An annotated **release tag** (`v1.0.0`)
- [ ] A `CHANGELOG.md` documenting what's in the release
- [ ] A merged Pull Request visible in the repository history on GitHub

This is your portfolio piece. Future employers and collaborators can look at this repository's history and see that you know how to use Git professionally.

---

## 3. Phase 1 — Repository Setup

### Step 1 — Create the Repository on GitHub

1. Go to [https://github.com/new](https://github.com/new)
2. Name it `noted`
3. Add a description: `A simple markdown-based notes manager`
4. Set it to **Public**
5. Do **not** initialize with a README (you'll do that locally)
6. Click "Create repository"

### Step 2 — Initialize Locally

```bash
cd ~/Desktop
mkdir noted
cd noted
git init
git remote add origin git@github.com:YOUR_USERNAME/noted.git
```

### Step 3 — Set Up Branch Protection on GitHub

Before writing a single line of code:

1. GitHub → your `noted` repo → Settings → Branches
2. Add rule for `main`
3. Enable "Require a pull request before merging"
4. Save

### Step 4 — Create the Project Foundation

```bash
# Create .gitignore
cat > .gitignore << 'EOF'
# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/
*.swp

# Logs
*.log

# Runtime
*.tmp
.cache/
EOF

# Create the README
cat > README.md << 'EOF'
# noted

A simple command-line notes manager. Create, list, and delete
plain-text notes from your terminal.

## Requirements

- Bash 4.0+
- Any Unix-like environment (macOS, Linux, WSL)

## Installation

```bash
git clone git@github.com:YOUR_USERNAME/noted.git
cd noted
chmod +x noted.sh
```

## Usage

```bash
./noted.sh new "My note title"   # Create a new note
./noted.sh list                  # List all notes
./noted.sh delete "My note title" # Delete a note
./noted.sh help                  # Show help
```

## Project Structure

```
noted/
  noted.sh        Main script
  notes/          Directory where notes are stored
  CHANGELOG.md    Version history
```
EOF

# Create the notes directory
mkdir notes
touch notes/.gitkeep  # Keep the empty directory tracked

# Initial commit directly to main (this is the one exception)
git add .
git commit -m "chore: initialize project structure"

# Push to GitHub — sets up main branch
git push -u origin main
```

---

## 4. Phase 2 — Feature Development with GitHub Flow

Now you'll build the actual features — each on its own branch, merged via Pull Request.

### Feature 1 — Core Script

```bash
# Create feature branch
git switch -c feature/core-script

# Create the main script
cat > noted.sh << 'EOF'
#!/bin/bash

NOTES_DIR="$(dirname "$0")/notes"
mkdir -p "$NOTES_DIR"

case "$1" in
  new)
    if [ -z "$2" ]; then
      echo "Usage: noted new \"Note title\""
      exit 1
    fi
    filename="$NOTES_DIR/$(echo "$2" | tr ' ' '-' | tr '[:upper:]' '[:lower:]').md"
    echo "# $2" > "$filename"
    echo "" >> "$filename"
    echo "Created: $(date '+%Y-%m-%d %H:%M')" >> "$filename"
    echo "✓ Created note: $2"
    ;;

  list)
    if [ -z "$(ls -A $NOTES_DIR/*.md 2>/dev/null)" ]; then
      echo "No notes yet. Use: noted new \"Note title\""
    else
      echo "Your notes:"
      echo "───────────"
      for f in "$NOTES_DIR"/*.md; do
        title=$(head -1 "$f" | sed 's/^# //')
        echo "  • $title"
      done
    fi
    ;;

  delete)
    if [ -z "$2" ]; then
      echo "Usage: noted delete \"Note title\""
      exit 1
    fi
    filename="$NOTES_DIR/$(echo "$2" | tr ' ' '-' | tr '[:upper:]' '[:lower:]').md"
    if [ -f "$filename" ]; then
      rm "$filename"
      echo "✓ Deleted note: $2"
    else
      echo "Note not found: $2"
      exit 1
    fi
    ;;

  help|*)
    echo "noted — a simple notes manager"
    echo ""
    echo "Commands:"
    echo "  new \"Title\"     Create a new note"
    echo "  list             List all notes"
    echo "  delete \"Title\"  Delete a note"
    echo "  help             Show this help"
    ;;
esac
EOF

# Make it executable
chmod +x noted.sh

# Commit the work
git add noted.sh
git commit -m "feat: add core noted.sh script with new, list, delete commands"

# Push and open PR
git push -u origin feature/core-script
```

**Now go to GitHub and open a Pull Request for `feature/core-script → main`.** Write a PR description:

```
## What this PR does

Adds the core `noted.sh` script with three commands:
- `new` — create a note as a markdown file
- `list` — list all existing notes
- `delete` — remove a note by title

## How to test

```bash
chmod +x noted.sh
./noted.sh new "My first note"
./noted.sh list
./noted.sh delete "My first note"
```
```

Merge the PR on GitHub, then sync locally:

```bash
git switch main
git pull
git branch -d feature/core-script
```

### Feature 2 — Note Count and Timestamp

```bash
git switch main
git pull
git switch -c feature/note-metadata

# Add a 'count' subcommand and show creation date in list
cat >> noted.sh << 'EOF'

# This line intentionally left for feature/note-metadata branch
EOF

# Actually, let's properly edit the list case to show dates
# Simulate the edit by adding a count script wrapper
cat > count.sh << 'EOF'
#!/bin/bash
NOTES_DIR="$(dirname "$0")/notes"
count=$(ls "$NOTES_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "Total notes: $count"
EOF

chmod +x count.sh

git add count.sh
git commit -m "feat: add count.sh to display total note count"

# Add a note about usage to README
echo "" >> README.md
echo "## Tips" >> README.md
echo "" >> README.md
echo "- Run \`./count.sh\` to see how many notes you have" >> README.md
echo "- Notes are stored as plain \`.md\` files in the \`notes/\` directory" >> README.md
echo "- You can edit notes directly with any text editor" >> README.md

git add README.md
git commit -m "docs: add tips section to README"

git push -u origin feature/note-metadata
```

Open a PR on GitHub, merge it, and sync locally:

```bash
git switch main
git pull
git branch -d feature/note-metadata
```

### Feature 3 — Search Functionality

```bash
git switch main
git pull
git switch -c feature/search

# Create a search script
cat > search.sh << 'EOF'
#!/bin/bash

NOTES_DIR="$(dirname "$0")/notes"
QUERY="$1"

if [ -z "$QUERY" ]; then
  echo "Usage: search.sh \"keyword\""
  exit 1
fi

echo "Searching for: $QUERY"
echo "────────────────────────"

found=0
for f in "$NOTES_DIR"/*.md 2>/dev/null; do
  [ -f "$f" ] || continue
  if grep -qi "$QUERY" "$f"; then
    title=$(head -1 "$f" | sed 's/^# //')
    echo "  ✓ $title"
    found=$((found + 1))
  fi
done

if [ $found -eq 0 ]; then
  echo "  No notes matching \"$QUERY\""
else
  echo ""
  echo "$found note(s) found."
fi
EOF

chmod +x search.sh

git add search.sh
git commit -m "feat: add search.sh to find notes by keyword"

# Update README with search usage
sed -i '' '/## Tips/i\
./search.sh "keyword"         # Search notes by keyword\
' README.md 2>/dev/null || \
echo '- Run `./search.sh "keyword"` to search note contents' >> README.md

git add README.md
git commit -m "docs: add search command to README usage section"

git push -u origin feature/search
```

Open a PR on GitHub, merge, and clean up:

```bash
git switch main
git pull
git branch -d feature/search
```

---

## 5. Phase 3 — Deliberate Conflict & Resolution

Now you'll simulate the most realistic scenario: two developers edit the same file at the same time.

```bash
git switch main
git pull

# Developer A's branch — updates the README header
git switch -c feature/readme-update-a

cat > README.md << 'EOF'
# noted ✨

A blazing-fast, lightweight notes manager for the terminal.
Keep your thoughts organized without leaving the command line.

## Requirements

- Bash 4.0+
- Any Unix-like environment (macOS, Linux, WSL)

## Installation

```bash
git clone git@github.com:YOUR_USERNAME/noted.git
cd noted
chmod +x noted.sh
```

## Usage

```bash
./noted.sh new "My note title"    # Create a new note
./noted.sh list                   # List all notes
./noted.sh delete "My note title" # Delete a note
./noted.sh help                   # Show help
./count.sh                        # Count all notes
./search.sh "keyword"             # Search note contents
```
EOF

git add README.md
git commit -m "docs: rewrite README intro with better description"
git push -u origin feature/readme-update-a
```

Now merge `feature/readme-update-a` to `main` via GitHub PR.

```bash
git switch main
git pull
git branch -d feature/readme-update-a

# Developer B's branch — also edits README (different wording)
git switch -c feature/readme-update-b

# Edit the same file with different content
cat > README.md << 'EOF'
# noted 📝

The minimalist terminal notes manager. Write fast, find fast, stay focused.

## Requirements

- Bash 4.0+
- Any Unix-like environment (macOS, Linux, WSL)

## Getting Started

```bash
git clone git@github.com:YOUR_USERNAME/noted.git
cd noted && chmod +x noted.sh
./noted.sh help
```

## All Commands

| Command | Description |
|---|---|
| `./noted.sh new "Title"` | Create a new note |
| `./noted.sh list` | List all notes |
| `./noted.sh delete "Title"` | Delete a note |
| `./count.sh` | Count all notes |
| `./search.sh "term"` | Search note contents |
EOF

git add README.md
git commit -m "docs: rewrite README with command table layout"
git push -u origin feature/readme-update-b

# Now merge into main — conflict incoming!
git switch main
git merge feature/readme-update-b
```

You'll see:

```
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

### Resolve the Conflict

```bash
# Open README.md — you'll see conflict markers
# Choose the best of both versions — combine them

cat > README.md << 'EOF'
# noted ✨

The minimalist terminal notes manager. Write fast, find fast, stay focused.
Keep your thoughts organized without ever leaving the command line.

## Requirements

- Bash 4.0+
- Any Unix-like environment (macOS, Linux, WSL)

## Installation

```bash
git clone git@github.com:YOUR_USERNAME/noted.git
cd noted
chmod +x noted.sh
```

## All Commands

| Command | Description |
|---|---|
| `./noted.sh new "Title"` | Create a new note |
| `./noted.sh list` | List all notes |
| `./noted.sh delete "Title"` | Delete a note |
| `./noted.sh help` | Show help |
| `./count.sh` | Count all notes |
| `./search.sh "term"` | Search note contents |

## Tips

- Notes are stored as plain `.md` files in the `notes/` directory
- You can edit notes directly with any text editor
- Run `./count.sh` to see how many notes you have
EOF

# Mark as resolved and complete the merge
git add README.md
git commit -m "merge: resolve README conflict — combine both improvements"

git push
git branch -d feature/readme-update-b
```

---

## 6. Phase 4 — History Cleanup with Interactive Rebase

Before tagging a release, clean up any messy commits in your history.

```bash
git switch main
git pull

# First, look at your current history
git log --oneline
```

You'll likely see a mix of clean commits and some noise. Let's add a few messy ones to practice on:

```bash
# Simulate a developer making messy WIP commits
git switch -c feature/add-changelog

echo "WIP" > CHANGELOG.md
git add CHANGELOG.md
git commit -m "WIP changelog"

echo "still WIP" >> CHANGELOG.md
git add CHANGELOG.md
git commit -m "more changelog work"

echo "ok done" >> CHANGELOG.md
git add CHANGELOG.md
git commit -m "asdfgh"

# Now write the real changelog content
cat > CHANGELOG.md << 'EOF'
# Changelog

All notable changes to `noted` are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com).

## [1.0.0] - 2025-02-23

### Added
- `noted.sh` — core script with `new`, `list`, `delete`, and `help` commands
- `count.sh` — displays total number of notes
- `search.sh` — search note contents by keyword
- `.gitignore` configured for shell project
- `README.md` with full usage documentation and command table
- `CHANGELOG.md` to track version history

### Notes
- Notes are stored as individual `.md` files in the `notes/` directory
- All scripts require Bash 4.0+ on a Unix-like environment
EOF

git add CHANGELOG.md
git commit -m "docs: add proper CHANGELOG content"

# Check what we're about to clean up
git log --oneline
```

Now squash the 4 messy commits into 1 clean one:

```bash
# Rebase the last 4 commits
git rebase -i HEAD~4
```

In the editor, change it to:

```
pick <first-hash>  WIP changelog
f    <second-hash> more changelog work
f    <third-hash>  asdfgh
f    <fourth-hash> docs: add proper CHANGELOG content
```

Then reword the remaining commit message:

```
r    <first-hash>  WIP changelog
```

Save, close. Git opens another editor — type the final message:

```
docs: add CHANGELOG with v1.0.0 release notes
```

Save and close.

```bash
# Verify — 4 commits became 1
git log --oneline

# Push the branch (force needed since history was rewritten)
git push -u origin feature/add-changelog
```

Open a PR on GitHub for this branch, merge it, clean up:

```bash
git switch main
git pull
git branch -d feature/add-changelog
```

---

## 7. Phase 5 — Release & Tagging

You've completed all features. Time to ship.

```bash
git switch main
git pull

# Final review — see everything you've built
git log --oneline --graph --all --decorate

# See all files in the project
ls -la

# Run a final check — make sure the script works
chmod +x noted.sh count.sh search.sh 2>/dev/null

./noted.sh new "My first note"
./noted.sh new "Git is powerful"
./noted.sh list
./count.sh
./search.sh "git"
./noted.sh delete "My first note"
./noted.sh list
```

Everything working? Tag the release:

```bash
# Create an annotated release tag
git tag -a v1.0.0 -m "v1.0.0 — Initial release

Features:
- Create, list, and delete notes from the terminal
- Count total notes with count.sh
- Search note contents with search.sh

All notes stored as plain markdown files."

# View the tag
git show v1.0.0

# Push the tag to GitHub
git push origin v1.0.0
```

### Create a GitHub Release

1. Go to your `noted` repository on GitHub
2. Click "Releases" → "Draft a new release"
3. Choose tag: `v1.0.0`
4. Release title: `v1.0.0 — Initial Release`
5. Copy your `CHANGELOG.md` content into the description
6. Click "Publish release"

Your project now has a professional, versioned release on GitHub. 🎉

---

## 8. Week in Review — Command Reference

A complete reference of every command covered this week, organized by category.

### Setup & Configuration

```bash
git --version                              # Check Git version
git config --global user.name "Name"       # Set global username
git config --global user.email "e@mail"    # Set global email
git config --global init.defaultBranch main # Set default branch
git config --global core.editor "code --wait" # Set editor
git config --list                          # View all settings
```

### Starting a Repository

```bash
git init                      # Initialize a new local repo
git clone <url>               # Clone a remote repo
git clone <url> <folder>      # Clone into a named folder
git remote add origin <url>   # Connect local repo to remote
git remote -v                 # View all remotes
git remote set-url origin <url> # Change remote URL
```

### Core Daily Workflow

```bash
git status                    # See what's changed
git diff                      # See unstaged changes
git diff --staged             # See staged changes
git add <file>                # Stage a file
git add .                     # Stage all changes
git add -p                    # Interactively stage chunks
git restore --staged <file>   # Unstage a file
git commit -m "message"       # Commit with message
git commit -am "message"      # Stage tracked + commit
git commit --amend -m "msg"   # Fix last commit
```

### Viewing History

```bash
git log                         # Full commit history
git log --oneline               # Compact history
git log --oneline --graph --all # Visual branch history
git log --author="Name"         # Filter by author
git log --grep="keyword"        # Search commit messages
git log -- <file>               # History for one file
git log -5                      # Last 5 commits only
git show <hash>                 # Inspect a commit
git show --stat <hash>          # Files changed in a commit
```

### Branching

```bash
git branch                      # List local branches
git branch -a                   # List all branches
git branch -v                   # Branches with last commit
git branch -vv                  # With tracking info
git branch --merged             # Branches already merged
git branch --no-merged          # Branches not yet merged
git branch <name>               # Create a branch
git switch <branch>             # Switch to a branch
git switch -c <name>            # Create and switch
git branch -d <name>            # Delete merged branch
git branch -D <name>            # Force delete branch
git branch -m <new-name>        # Rename current branch
```

### Merging

```bash
git merge <branch>              # Merge branch into current
git merge --no-ff <branch>      # Always create merge commit
git merge --abort               # Cancel in-progress merge
git mergetool                   # Open visual merge tool
```

### Remote Operations

```bash
git push -u origin <branch>     # Push + set upstream
git push                        # Push to tracked remote
git push --force-with-lease     # Safe force push
git push origin --delete <b>    # Delete remote branch
git fetch                       # Download without merging
git fetch --prune               # Fetch + clean stale refs
git pull                        # Fetch + merge
git pull --rebase               # Fetch + rebase
```

### Undoing Things

```bash
git restore <file>              # Discard working dir changes
git restore .                   # Discard ALL working changes
git restore --staged <file>     # Unstage a file
git restore --source=<hash> <f> # Restore from commit
git stash                       # Stash changes
git stash push -m "desc"        # Stash with message
git stash push -u               # Include untracked files
git stash list                  # View all stashes
git stash pop                   # Apply + remove latest stash
git stash apply stash@{N}       # Apply without removing
git stash drop stash@{N}        # Delete a stash
git stash clear                 # Delete all stashes
git revert HEAD                 # Undo last commit (safe)
git revert <hash>               # Undo specific commit
git reset --soft HEAD~N         # Undo N commits, keep staged
git reset --mixed HEAD~N        # Undo N commits, keep unstaged
git reset --hard HEAD~N         # Undo N commits, delete all
git rebase -i HEAD~N            # Interactive rebase last N
git reflog                      # View all HEAD movements
```

### Tags

```bash
git tag                         # List all tags
git tag -a <tag> -m "msg"       # Create annotated tag
git tag -a <tag> <hash> -m "m"  # Tag a past commit
git show <tag>                  # View tag details
git push origin <tag>           # Push a tag
git push origin --tags          # Push all tags
git tag -d <tag>                # Delete local tag
git push origin --delete <tag>  # Delete remote tag
```

### Utility

```bash
git rm --cached <file>          # Stop tracking a file
git diff <branch1>..<branch2>   # Diff between branches
git log origin/main..HEAD       # Unpushed commits
git branch -r                   # Remote tracking branches
git stash branch <name>         # New branch from stash
```

---

## 9. Common Mistakes & How to Avoid Them

### Mistake 1 — Committing Directly to `main`

```
❌ You pushed directly to main without a PR
✅ Always branch, always PR — even for small changes
   Set up branch protection rules to enforce this automatically
```

### Mistake 2 — `git add .` Without Checking First

```
❌ Staged .env, node_modules, or build files accidentally
✅ Run git status and git diff --staged before every commit
   Keep .gitignore updated
```

### Mistake 3 — Vague Commit Messages

```
❌ "fix", "update", "changes", "WIP", "asdf"
✅ "fix: prevent null crash in checkout on empty cart"
   Use imperative mood. Explain WHAT and WHY.
```

### Mistake 4 — One Giant Commit at End of Day

```
❌ Committing 2 days of work in one commit
✅ Commit every logical unit of work as you complete it
   Small commits = easier reviews, easier reverts, cleaner history
```

### Mistake 5 — Force Pushing to Shared Branches

```
❌ git push --force on main or a branch a teammate has
✅ Never force-push shared branches
   Use git revert for shared history, --force-with-lease for personal branches
```

### Mistake 6 — Forgetting to Pull Before Starting Work

```
❌ Branching from an outdated main → big merge conflict later
✅ Always git switch main && git pull before creating a branch
```

### Mistake 7 — Long-Lived Branches

```
❌ A feature branch that lives for 3 weeks — 500 commits behind main
✅ Keep branches short-lived (hours to days, not weeks)
   Regularly rebase or merge from main to stay in sync
```

### Mistake 8 — Committing Secrets

```
❌ Pushed API keys, passwords, or tokens in a .env file
✅ Set up .gitignore before your first commit
   Rotate any secret that was ever committed, even briefly
   Use tools like git-secrets or trufflehog in CI
```

### Mistake 9 — Using git reset on Pushed Commits

```
❌ git reset --hard on a commit already pushed to a shared branch
✅ Use git revert for anything that's been pushed
   Reserve reset for local-only commits
```

### Mistake 10 — Never Reading the Error Messages

```
❌ Getting a Git error and immediately searching Google or asking AI
✅ Read the full error — Git error messages are remarkably helpful
   They often tell you exactly what to run to fix the problem
```

---

## 10. Git Cheat Sheet — One Page

```
┌─────────────────────────────────────────────────────────────────────┐
│                        GIT CHEAT SHEET                              │
├────────────────────────┬────────────────────────────────────────────┤
│ SETUP                  │ DAILY WORKFLOW                             │
│ git config --global    │ git status          See what changed       │
│   user.name "Name"     │ git diff            Unstaged changes       │
│   user.email "e@mail"  │ git diff --staged   Staged changes         │
│                        │ git add .           Stage all              │
│ START                  │ git add -p          Stage interactively    │
│ git init               │ git commit -m "msg" Commit                 │
│ git clone <url>        │ git log --oneline   View history           │
│                        │ git show <hash>     Inspect commit         │
├────────────────────────┼────────────────────────────────────────────┤
│ BRANCHES               │ REMOTES                                    │
│ git branch             │ git remote -v       List remotes           │
│ git switch -c <name>   │ git push -u origin  First push             │
│ git switch <name>      │ git push            Push commits           │
│ git merge <branch>     │ git fetch           Download (no merge)    │
│ git branch -d <name>   │ git pull            Download + merge       │
│ git log --graph --all  │ git pull --rebase   Download + rebase      │
├────────────────────────┼────────────────────────────────────────────┤
│ UNDO                   │ STASH                                      │
│ git restore <file>     │ git stash           Save changes aside     │
│ git restore --staged   │ git stash pop       Bring them back        │
│ git revert HEAD        │ git stash list      View stash stack       │
│ git reset --soft HEAD~1│                                            │
│ git reset --hard HEAD~1│ TAGS                                       │
│ git rebase -i HEAD~N   │ git tag -a v1.0 -m  Create release tag    │
│ git reflog             │ git push origin v1  Push tag to remote     │
└────────────────────────┴────────────────────────────────────────────┘

THE GOLDEN RULES
─────────────────────────────────────────────────────────────────────
1. main is always deployable — never commit broken code there
2. Branch for every change — no matter how small
3. Commit early and often — small commits beat big ones
4. Write meaningful messages — your future self will thank you
5. Revert for shared history — never reset what others have pulled
6. Pull before you branch — start from the latest main
7. Keep .gitignore updated — never commit secrets or build output
8. Delete merged branches — keep your repo clean
─────────────────────────────────────────────────────────────────────
```

---

## 11. What to Learn Next

You've completed the foundational week. Here's a roadmap for where to go from here, roughly in order of priority:

### Immediate Next Steps (Week 2–4)

**Git Rebase (non-interactive)**
Learn to use `git rebase <branch>` to keep your feature branch up to date with `main` without merge commits. Essential for keeping clean history on active teams.

```bash
# Instead of: git merge main (creates a merge commit)
git rebase main   # Replays your commits on top of latest main
```

**Cherry-Pick**
Apply a single commit from one branch to another — without merging the whole branch.

```bash
git cherry-pick a1b2c3d   # Apply just this one commit here
```

**Git Bisect**
Binary search through commit history to find exactly which commit introduced a bug. Incredibly powerful for debugging.

```bash
git bisect start
git bisect bad           # Current commit is broken
git bisect good v1.0.0   # This version was fine
# Git checks out the midpoint — you test and mark good/bad
# Repeat until Git finds the exact breaking commit
```

### Intermediate Skills (Month 1–2)

**Signing Commits with GPG**
Cryptographically verify that commits are really from you. Required by some organizations and open source projects.

```bash
git commit -S -m "feat: add verified commit"
```

**Git Worktrees**
Check out multiple branches simultaneously in different folders — without stashing or switching.

```bash
git worktree add ../project-hotfix hotfix/critical-bug
```

**Submodules and Subtrees**
Include one Git repository inside another. Used for shared libraries and monorepo-adjacent setups.

```bash
git submodule add git@github.com:org/shared-lib.git libs/shared
```

**Advanced .gitconfig**
Customize Git with aliases, delta for better diffs, and per-directory configurations.

```bash
# Useful aliases to add to ~/.gitconfig
[alias]
  st = status
  co = switch
  lg = log --oneline --graph --all --decorate
  undo = reset --soft HEAD~1
  aliases = config --get-regexp alias
```

### Tools to Explore

**GitHub CLI (`gh`)**
Manage PRs, issues, and releases from the terminal without opening a browser.

```bash
gh pr create --title "feat: dark mode" --body "Adds dark mode toggle"
gh pr merge --squash
gh release create v2.0.0
```

**Delta**
A syntax-highlighting pager for `git diff` output — makes diffs dramatically more readable.

**Lazygit**
A terminal UI for Git — great for visual learners who want the power of the command line with a navigable interface.

**Git LFS (Large File Storage)**
Store large binary files (images, videos, datasets) in Git repositories without bloating history.

**pre-commit (the tool)**
A framework for managing Git hooks across a team — language-agnostic and shareable via config file.

### Concepts to Study

- **Rebasing strategies** — when to rebase vs merge and the tradeoffs
- **Monorepos** — managing multiple projects in one Git repository (used by Google, Meta, Airbnb)
- **CI/CD integration** — how GitHub Actions, GitLab CI, and CircleCI react to pushes, PRs, and tags
- **Git internals** — objects, trees, blobs, and packfiles — understand what Git actually stores
- **Security** — signed commits, secret scanning, dependency vulnerability alerts

### Recommended Resources

| Resource | What It Covers |
|---|---|
| [Pro Git Book](https://git-scm.com/book) (free) | Comprehensive — the definitive reference |
| [Learn Git Branching](https://learngitbranching.js.org) | Visual, interactive — best for branching concepts |
| [GitHub Skills](https://skills.github.com) | Guided hands-on labs directly on GitHub |
| [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) | Excellent workflow explanations |
| [Oh Shit, Git!](https://ohshitgit.com) | How to fix common mistakes — plain English |
| [Conventional Commits](https://www.conventionalcommits.org) | The commit message standard used by most teams |

---

## Congratulations 🎉

You started this week not knowing what a repository was. You're finishing it with:

- A professional Git workflow you can bring to any team
- A real project on GitHub with branches, PRs, conflicts, rebases, and a tagged release
- The muscle memory to `git status` and `git diff --staged` before every commit
- Confidence to undo mistakes without panicking
- A vocabulary to collaborate with any development team in the world

Git is one of those tools that you learn in a week and keep getting better at for years. Every project, every team, every weird edge case teaches you something new. The foundation you've built this week will serve you for your entire career.

Now go build something and commit it. 🚀

---

*Git Learning Curriculum — Day 7 of 7 — Complete*

---
### &larr; [Day 6 — Workflows & Best Practices](day06_workflows_best_practices.md) | [Index](index.md) |
# Git Learning Curriculum
## Day 1 — What is Git & Setup

> **Goal:** Understand version control and get Git running locally.

---

## Table of Contents
1. [What is Version Control?](#1-what-is-version-control)
2. [What is Git?](#2-what-is-git)
3. [Installing Git](#3-installing-git)
4. [Configuring Git — git config](#4-configuring-git--git-config)
5. [Initializing a Repository — git init](#5-initializing-a-repository--git-init)
6. [Checking Project State — git status](#6-checking-project-state--git-status)
7. [Essential Terminal Basics](#7-essential-terminal-basics)
8. [Day 1 Hands-On Exercise](#8-day-1-hands-on-exercise)
9. [Key Commands Summary](#9-key-commands-summary)

---

## 1. What is Version Control?

Version control is a system that records changes to a file or set of files over time so you can recall specific versions later. Think of it as a **time machine for your code**.

### The Problem Without Version Control

Imagine you're building a website. Without version control, your project folder might look like this:

```
my-website/
  index.html
  index_backup.html
  index_final.html
  index_final_v2.html
  index_ACTUALLY_final.html
  index_USE_THIS_ONE.html
```

This is a nightmare. You can't tell what changed between versions, who changed it, or why. If something breaks, rolling back is guesswork.

> 🌍 **Real-World Use Case:**
> A team of 5 developers is building an e-commerce app. Developer A fixes a checkout bug. Developer B simultaneously updates the product page. Without version control, one person's work overwrites the other's. With Git, both changes are tracked independently and can be merged seamlessly.

### The Three Problems Git Solves

- **Tracking changes:** Every change is recorded with who made it, when, and why.
- **Collaborating:** Multiple people can work on the same codebase without overwriting each other's work.
- **Recovering from mistakes:** You can revert any file — or the entire project — to any previous state.

---

## 2. What is Git?

Git is a **distributed version control system (DVCS)** created by Linus Torvalds in 2005 (the same person who created Linux). "Distributed" means every developer has a full copy of the entire project history on their own machine — not just the latest snapshot.

This is different from older systems like SVN where there was one central server. With Git, you can work completely **offline** — commit changes, create branches, view history — without an internet connection. You only need a connection when sharing work with others.

> 🌍 **Real-World Use Case:**
> A developer on a long flight can continue committing code, reviewing history, and branching — all without Wi-Fi. When they land, they simply push their changes to the remote server (like GitHub). This is the power of distributed version control.

---

## 3. Installing Git

### On macOS

The easiest way is via Homebrew:

```bash
brew install git
```

Alternatively, installing Xcode Command Line Tools also installs Git:

```bash
xcode-select --install
```

### On Windows

Download **Git for Windows** from [https://git-scm.com/download/win](https://git-scm.com/download/win). This also installs **Git Bash** — a terminal that lets you use Unix-style commands on Windows.

### On Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install git
```

### Verify Your Installation

```bash
git --version
# Output: git version 2.43.0
```

---

## 4. Configuring Git — `git config`

Before using Git, you need to tell it who you are. Every commit you make is stamped with this identity — it's how teams know who made what change.

### Setting Your Identity (Global)

```bash
git config --global user.name "Jane Smith"
git config --global user.email "jane@example.com"
```

The `--global` flag means this setting applies to **all repositories** on your machine. You can override it per-repository by running the same command without `--global` inside a specific project folder.

### Setting Your Default Text Editor

Git opens a text editor when you need to write commit messages. Set your preferred editor:

```bash
git config --global core.editor "code --wait"   # VS Code
git config --global core.editor "nano"           # Nano (beginner-friendly)
git config --global core.editor "vim"            # Vim
```

### Setting the Default Branch Name

Newer versions of Git use `main` instead of the older `master`. Set this explicitly:

```bash
git config --global init.defaultBranch main
```

### Viewing All Your Settings

```bash
git config --list
```

You can also view a specific setting:

```bash
git config user.name
# Output: Jane Smith
```

> 💡 **Where Are Config Files Stored?**
> Git stores global config in `~/.gitconfig` in your home directory. You can open and edit this file directly. Local (per-project) config is stored in `.git/config` inside the project folder.

---

## 5. Initializing a Repository — `git init`

A Git **repository (repo)** is simply a folder that Git is tracking. You create one using `git init`.

### Creating Your First Repository

```bash
mkdir my-first-project
cd my-first-project
git init
```

Output:

```
Initialized empty Git repository in /home/jane/my-first-project/.git/
```

That's it. Your folder is now a Git repository.

### What Did `git init` Actually Create?

Git created a hidden folder called `.git` inside your project. Let's look inside it:

```bash
ls -la          # See the hidden .git folder
ls -la .git     # Explore its contents
```

You'll see something like this:

```
.git/
  HEAD           ← Points to the current branch
  config         ← Local repository settings
  description    ← Used by GitWeb (can ignore for now)
  hooks/         ← Scripts that run on Git events (advanced)
  info/          ← Exclude patterns
  objects/       ← Where all your file content is stored
  refs/          ← Pointers to commits (branches & tags)
```

> ⚠️ **Important:**
> Never manually edit or delete files inside the `.git` folder unless you know exactly what you're doing. This folder **IS** your repository. Deleting it means losing your entire version history.

### Initializing in an Existing Project

You can run `git init` inside an existing folder — it won't touch your files, it just starts tracking them:

```bash
cd /path/to/existing/project
git init
```

> 🌍 **Real-World Use Case:**
> A freelancer has been building a client website for a week with no version control. They run `git init` in the project folder and Git starts tracking it immediately. From this point on, they can commit snapshots, create branches for new features, and never lose work again.

---

## 6. Checking Project State — `git status`

`git status` is your best friend. It shows the current state of your working directory — what has changed, what Git knows about, and what still needs attention.

### Using `git status`

Right after `git init`, run:

```bash
git status
```

Output:

```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

Now create a file and check status again:

```bash
echo "# My First Project" > README.md
git status
```

Output:

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```

Git sees the file but tells you it is **untracked** — meaning Git isn't watching it yet. You'll learn how to fix that on Day 2 with `git add`.

### Understanding `git status` Output

| Status Message | What It Means |
|---|---|
| `Untracked files` | New files Git has never seen before |
| `Changes not staged for commit` | Files Git tracks but that have been modified since last commit |
| `Changes to be committed` | Files staged and ready to be committed |
| `nothing to commit, working tree clean` | Everything is saved — no pending changes |

---

## 7. Essential Terminal Basics

You'll use the terminal throughout this curriculum. Here's a quick reference:

| Command | Description | Example |
|---|---|---|
| `pwd` | Print Working Directory — shows your current location | `pwd` |
| `ls` | List files in current directory | `ls -la` |
| `cd` | Change Directory — navigate folders | `cd my-project` |
| `mkdir` | Make a new directory | `mkdir new-folder` |
| `touch` | Create a new empty file | `touch index.html` |
| `echo` | Print text or write to a file | `echo 'hi' > file.txt` |
| `cat` | Display file contents in terminal | `cat README.md` |
| `rm` | Remove a file (caution!) | `rm old-file.txt` |
| `clear` | Clear the terminal screen | `clear` |

---

## 8. Day 1 Hands-On Exercise

Follow these steps to put everything together. By the end, you'll have your first Git repository set up.

### Step 1 — Configure Git (Do This Once)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"

# Verify everything looks right
git config --list
```

### Step 2 — Create Your First Repository

```bash
# Navigate to your workspace (e.g., Desktop)
cd ~/Desktop

# Create a new project folder
mkdir learning-git
cd learning-git

# Initialize Git
git init

# Confirm it worked — you should see the .git folder
ls -la
```

### Step 3 — Explore the .git Folder

```bash
# See what Git created
ls -la .git

# Look at the HEAD file
cat .git/HEAD
# Output: ref: refs/heads/main

# Look at the local config file
cat .git/config
```

### Step 4 — Create Files and Check Status

```bash
# Create a README file
echo "# Learning Git" > README.md
echo "This is my first Git repository." >> README.md

# Check what Git sees
git status

# Create another file
touch index.html

# Check status again — notice both files appear as untracked
git status
```

> ✅ **What You Should See:**
> After Step 4, `git status` should show both `README.md` and `index.html` listed under "Untracked files". This means Git sees them but isn't tracking them yet. You'll learn to stage and commit files on Day 2.

---

## 9. Key Commands Summary

| Command | What It Does | Common Usage |
|---|---|---|
| `git init` | Creates a new Git repository in the current folder | `git init` |
| `git config --global` | Sets a global Git configuration option | `git config --global user.name "Jane"` |
| `git config --list` | Displays all current Git settings | `git config --list` |
| `git status` | Shows the current state of your working directory | `git status` |
| `git --version` | Displays the installed Git version | `git --version` |

---

## Coming Up on Day 2 — Staging, Committing & History

Tomorrow you'll learn the core Git workflow — how to actually **save your work**. You'll master:

- `git add` — staging your changes
- `git commit` — saving a snapshot to history
- `git log` — browsing your commit history
- `git diff` — seeing exactly what changed

The **staging area** (or "index") is one of Git's most powerful and unique concepts — understanding it deeply will make you a much stronger Git user.

---

*Git Learning Curriculum — Day 1 of 7*
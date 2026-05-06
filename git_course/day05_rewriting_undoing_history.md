### &larr; [Day 4 — Remote Repositories & GitHub](day04_remote_repository.md) | [Index](index.md) | [Day 6 — Workflows & Best Practices](day06_workflows_best_practices.md) &rarr;


# Git Learning Curriculum
## Day 5 — Rewriting History & Undoing Things

> **Goal:** Fix mistakes confidently — learn every tool Git gives you to undo, rewrite, and recover from errors at any stage of your workflow.

---

## Table of Contents
1. [The Undo Mental Model](#1-the-undo-mental-model)
2. [Discarding Working Directory Changes — git restore](#2-discarding-working-directory-changes--git-restore)
3. [Unstaging Files — git restore --staged](#3-unstaging-files--git-restore---staged)
4. [Stashing Work in Progress — git stash](#4-stashing-work-in-progress--git-stash)
5. [Safely Undoing Commits — git revert](#5-safely-undoing-commits--git-revert)
6. [Moving Branches Backward — git reset](#6-moving-branches-backward--git-reset)
7. [Revert vs Reset — When to Use Which](#7-revert-vs-reset--when-to-use-which)
8. [Cleaning Up History — git rebase -i](#8-cleaning-up-history--git-rebase--i)
9. [Finding a Lost Commit — git reflog](#9-finding-a-lost-commit--git-reflog)
10. [Day 5 Hands-On Exercise](#10-day-5-hands-on-exercise)
11. [Key Commands Summary](#11-key-commands-summary)

---

## 1. The Undo Mental Model

Before diving into commands, it helps to have a clear map of *where* a change can live and which tool undoes it at each stage:

<table>
<thead>
<tr>
<th colspan="3" style="text-align: center; background-color: #f2f2f2;">WHERE IS THE CHANGE?</th>
</tr>
<tr>
<th style="width: 33%;">Working Directory



<small>(unsaved edits)</small></th>
<th style="width: 33%;">Staging Area



<small>(git add'd)</small></th>
<th style="width: 34%;">Repository (commits)



<small>(committed history)</small></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>git restore &lt;file&gt;</code></td>
<td><code>git restore --staged &lt;file&gt;</code></td>
<td><code>git revert</code> (safe/public)</td>
</tr>
<tr>
<td></td>
<td></td>
<td><code>git reset</code> (local only)</td>
</tr>
<tr>
<td></td>
<td></td>
<td><code>git rebase -i</code> (reshape)</td>
</tr>
</tbody>
</table>

```
┌─────────────────────────────────────────────────────────────────┐
│                        WHERE IS THE CHANGE?                     │
├──────────────────┬──────────────────┬───────────────────────────┤
│ Working Directory│  Staging Area    │     Repository (commits)  │
│ (unsaved edits)  │  (git add'd)     │     (committed history)   │
├──────────────────┼──────────────────┼───────────────────────────┤
│ git restore      │ git restore      │ git revert  (safe/public) │
│ <file>           │ --staged <file>  │ git reset   (local only)  │
│                  │                  │ git rebase -i (reshape)   │
└──────────────────┴──────────────────┴───────────────────────────┘
```



The key rule to internalize:

- **Haven't committed yet?** → `git restore` is your tool. Changes are easy to discard.
- **Committed but not pushed?** → `git reset` or `git rebase -i`. You can rewrite freely.
- **Committed AND pushed to a shared branch?** → `git revert` only. Never rewrite shared history.

> 🌍 **Real-World Use Case:**
> A developer accidentally commits their `.env` file containing API keys. Knowing the right tool for the situation — `git revert` if already pushed to `main`, or `git reset` if still local — is the difference between a clean recovery and a messy history that confuses the whole team.

---

## 2. Discarding Working Directory Changes — `git restore`

`git restore` throws away uncommitted changes in your working directory, reverting a file back to its last committed state. **This is permanent — discarded changes cannot be recovered.**

### Discard Changes in a Single File

```bash
git restore index.html
```

This resets `index.html` to how it looked in the last commit. Any edits you made since then are gone.

### Discard All Unstaged Changes

```bash
git restore .
```

Reverts every modified file in the working directory back to its committed state. Use with care.

### Restore a File to a Specific Commit's Version

```bash
git restore --source=a1b2c3d index.html
```

This pulls the version of `index.html` from commit `a1b2c3d` into your working directory — without changing anything else. Useful for grabbing an old version of one file.

### Restore a File from a Specific Branch

```bash
git restore --source=main style.css
```

Grabs `style.css` from the `main` branch into your working directory.

> ⚠️ **Warning:** `git restore` on an unstaged file is irreversible. Git has no record of the change because it was never staged or committed. Always double-check with `git diff` before running it.

> 🌍 **Real-World Use Case:**
> A developer spent an hour experimenting with a new CSS layout but decides it's the wrong direction. Instead of manually undoing all the edits, they run `git restore style.css` and the file snaps back to the last committed version instantly.

---

## 3. Unstaging Files — `git restore --staged`

If you've staged a file with `git add` but haven't committed yet, you can move it back to the working directory without losing any changes.

### Unstage a Specific File

```bash
git restore --staged index.html
```

The file's changes are still in your working directory — they just won't be included in the next commit.

### Unstage Everything

```bash
git restore --staged .
```

### The Older Syntax (Still Common)

```bash
git reset HEAD index.html
```

Both commands do the same thing — `git restore --staged` is the modern preferred syntax.

### A Common Workflow

```bash
# You accidentally staged everything including a debug file
git add .

# Oops — unstage just the debug file
git restore --staged debug.log

# Now commit only what you intended
git commit -m "feat: add payment processing"
```

> 🌍 **Real-World Use Case:**
> A developer runs `git add .` out of habit, then realizes they accidentally staged a file containing temporary test data. They `git restore --staged` that file, commit the rest cleanly, and delete the test file separately. The commit history stays professional.

---

## 4. Stashing Work in Progress — `git stash`

`git stash` temporarily shelves your uncommitted changes so you can switch context — then brings them back later. Think of it as a clipboard for your in-progress work.

### Stash Your Current Changes

```bash
git stash
```

Your working directory and staging area are cleaned — the branch looks exactly like the last commit. Your changes are saved in a stash stack.

### Stash with a Descriptive Message

```bash
git stash push -m "WIP: half-finished login form"
```

Always add a message when you have multiple stashes — you'll thank yourself later.

### Also Stash Untracked Files

```bash
git stash push -u -m "WIP: including new untracked files"
```

By default, `git stash` ignores untracked (new) files. The `-u` flag includes them.

### View All Stashes

```bash
git stash list
```

Output:

```
stash@{0}: On feature-login: WIP: half-finished login form
stash@{1}: On main: WIP: experimental navbar styles
stash@{2}: WIP on main: a1b2c3d initial commit
```

Stashes are numbered from 0 (most recent). The stack grows every time you stash.

### Apply the Most Recent Stash

```bash
git stash pop
```

`pop` applies the latest stash AND removes it from the stash list. This is the most common way to bring back stashed work.

### Apply a Stash Without Removing It

```bash
git stash apply stash@{1}
```

`apply` brings the changes back but keeps them in the stash list — useful if you want to apply the same stash to multiple branches.

### Apply a Specific Stash

```bash
git stash pop stash@{2}
```

### Delete a Stash You No Longer Need

```bash
git stash drop stash@{1}
```

### Delete ALL Stashes

```bash
git stash clear
```

### Create a Branch from a Stash

```bash
git stash branch new-feature-branch stash@{0}
```

This creates a new branch, checks it out, and applies the stash — all in one command. Perfect when your stashed work grows into something big enough to deserve its own branch.

> 🌍 **Real-World Use Case:**
> A developer is mid-way through building a dashboard widget when their manager asks them to drop everything and fix a critical production bug. They `git stash` their unfinished widget, switch to `main`, create a `hotfix` branch, fix the bug, push, and merge. Then they switch back to their feature branch and `git stash pop` — picking up exactly where they left off, with zero context lost.

---

## 5. Safely Undoing Commits — `git revert`

`git revert` creates a **new commit** that undoes the changes from a previous commit. It does not remove or alter the original commit — it adds a new one on top. This is the **safe, public-friendly** way to undo work.

### Revert the Most Recent Commit

```bash
git revert HEAD
```

Git opens your editor to write a commit message for the revert. Save and close to complete it.

### Revert Without Opening an Editor

```bash
git revert HEAD --no-edit
```

### Revert a Specific Commit

```bash
git revert a1b2c3d
```

### Revert Multiple Commits

```bash
# Revert a range (oldest first)
git revert HEAD~3..HEAD
```

### Revert Without Auto-Committing (Stage Only)

```bash
git revert HEAD --no-commit
# or
git revert HEAD -n
```

This stages the reverting changes but doesn't commit yet. Useful when you want to revert multiple commits and combine them into one revert commit:

```bash
git revert -n HEAD~2
git revert -n HEAD~1
git revert -n HEAD
git commit -m "revert: undo last 3 commits"
```

### What the History Looks Like After Revert

```
Before:
[C1] ← [C2] ← [C3: bad commit]
                     ↑
                    main

After git revert HEAD:
[C1] ← [C2] ← [C3: bad commit] ← [C4: revert "bad commit"]
                                          ↑
                                         main
```

The bad commit is still in history — but its changes are cancelled out. Teammates who already pulled `C3` won't have history conflicts.

> 🌍 **Real-World Use Case:**
> A developer merges a feature branch that turns out to break the checkout flow on mobile. It's already on `main` and other teammates have pulled it. The team lead runs `git revert` on the merge commit, pushes, and the site is stable again within minutes — no history rewriting, no coordination headaches.

---

## 6. Moving Branches Backward — `git reset`

`git reset` moves the current branch pointer backward to a previous commit. Unlike `git revert`, it actually changes history — commits after the reset point appear to be removed.

There are three modes, each progressively more destructive:

### Mode 1 — `--soft` (Gentlest)

```bash
git reset --soft HEAD~1
```

Moves the branch pointer back one commit. Your changes are **kept and staged** — ready to recommit.

```
Before:  [C1] ← [C2] ← [C3]  ← main
After:   [C1] ← [C2]  ← main
         (C3's changes are still staged)
```

Use this when you committed too early and want to add more changes to that commit, or split it into multiple commits.

### Mode 2 — `--mixed` (Default)

```bash
git reset HEAD~1
# same as:
git reset --mixed HEAD~1
```

Moves the branch pointer back one commit. Your changes are **kept but unstaged** — back in the working directory.

```
Before:  [C1] ← [C2] ← [C3]  ← main
After:   [C1] ← [C2]  ← main
         (C3's changes are in working directory, unstaged)
```

This is the default mode when you don't specify a flag. Use it to uncommit and rethink what you're committing.

### Mode 3 — `--hard` (Most Destructive)

```bash
git reset --hard HEAD~1
```

Moves the branch pointer back AND **deletes all changes** from the working directory and staging area. The changes from the removed commits are gone.

```
Before:  [C1] ← [C2] ← [C3]  ← main
After:   [C1] ← [C2]  ← main
         (C3's changes are PERMANENTLY DELETED)
```

> ⚠️ **Warning:** `git reset --hard` is one of the few Git commands that can cause permanent data loss. The removed commits are not in your branch history, though they may be recoverable via `git reflog` for a short time. Never use `--hard` on commits that have been pushed to a shared branch.

### Reset to a Specific Commit

```bash
# Go back to a commit from 3 steps ago
git reset --soft HEAD~3

# Go back to a specific commit hash
git reset --hard a1b2c3d
```

### Reset a Single File (Not the Whole Branch)

```bash
# Restore a single file to its state at HEAD
git reset HEAD index.html
# This is equivalent to: git restore --staged index.html
```

### Comparison of Reset Modes

| Mode | Branch Pointer | Staging Area | Working Directory |
|---|---|---|---|
| `--soft` | Moves back | Changes kept staged | Unchanged |
| `--mixed` (default) | Moves back | Changes unstaged | Unchanged |
| `--hard` | Moves back | Cleared | Changes deleted |

> 🌍 **Real-World Use Case:**
> A developer makes three "WIP" commits in a row while figuring out a tricky algorithm. Before pushing, they run `git reset --soft HEAD~3` to undo all three commits while keeping all their code staged. Then they write one clean, well-worded commit that captures the final result. The messy WIP trail never makes it into shared history.

---

## 7. Revert vs Reset — When to Use Which

This is one of the most important distinctions in Git. The wrong choice can cause serious problems for your team.

| Situation | Use | Why |
|---|---|---|
| Commit is on a shared branch (pushed to remote) | `git revert` | Doesn't rewrite history — safe for teammates |
| Commit is local only (not pushed) | `git reset` | Fine to rewrite local history |
| You want to keep a clear record of the undo | `git revert` | Creates a visible revert commit |
| You want to erase all trace of the mistake | `git reset` | Removes commits entirely (local only) |
| Undoing a merge commit that's been pushed | `git revert -m 1 <merge-commit>` | Safest way to undo a merge on a shared branch |
| Cleaning up WIP commits before a PR | `git reset --soft` | Squash messy commits into clean ones |

### The Golden Rule

> **If someone else might have pulled the commit — use `git revert`, never `git reset`.**

Resetting a shared branch forces your teammates to do complex recovery work when they next pull. Reverting is transparent and requires no coordination.

---

## 8. Cleaning Up History — `git rebase -i`

Interactive rebase lets you **reshape your commit history** before sharing it. You can reorder, combine, rename, split, or delete commits as if you're editing a to-do list.

> ⚠️ **Important:** Like `git reset`, interactive rebase rewrites history. Only use it on commits that haven't been pushed to a shared branch yet.

### Launch Interactive Rebase

```bash
# Rebase the last 3 commits
git rebase -i HEAD~3
```

This opens your editor with a list of commits, oldest first:

```
pick a1b2c3d feat: add login page
pick d4e5f6a fix: typo in login form
pick g7h8i9j wip: still figuring out validation

# Rebase a1b2c3d..g7h8i9j onto f0e1d2c (3 commands)
#
# Commands:
# p, pick   = use commit as-is
# r, reword = use commit, but edit the commit message
# e, edit   = use commit, but stop for amending
# s, squash = combine with previous commit (keeps both messages)
# f, fixup  = combine with previous commit (discard this message)
# d, drop   = remove this commit entirely
```

### Common Rebase Operations

**Squash WIP commits into one clean commit:**

```
pick a1b2c3d feat: add login page
f    d4e5f6a fix: typo in login form
f    g7h8i9j wip: still figuring out validation
```

Change `pick` to `f` (fixup) on the commits you want to fold in. Save and close — Git combines them into one commit with the first message.

**Rename a commit message:**

```
r a1b2c3d feat: add login page
```

Change `pick` to `r` (reword). Git will pause and open another editor window for you to type the new message.

**Delete a commit entirely:**

```
pick a1b2c3d feat: add login page
d    d4e5f6a add debugging code I forgot to remove
pick g7h8i9j feat: add form validation
```

Change `pick` to `d` (drop). That commit and its changes disappear.

**Reorder commits:**

Simply cut and paste the lines into a different order. Git replays them in the new sequence.

### Squash All Feature Branch Commits Before Merging

A very common workflow before opening a Pull Request:

```bash
# You have 6 messy WIP commits on your feature branch
# Squash them all into one clean commit

git rebase -i main
# In the editor, keep the first commit as 'pick'
# Change all others to 'f' (fixup)
# Save and close
# Now you have one clean commit instead of 6
```

### If Rebase Runs Into a Conflict

```bash
# Git pauses and shows the conflict
# Fix the conflict in your editor
git add conflicted-file.txt

# Continue the rebase
git rebase --continue

# Or abandon the entire rebase and go back to before
git rebase --abort
```

> 🌍 **Real-World Use Case:**
> Before opening a Pull Request, a developer reviews their branch and sees 11 commits: "WIP", "more WIP", "fix", "argh fix", "ok this works", etc. They use `git rebase -i` to squash everything into 2 clean commits with meaningful messages. The PR reviewer sees a clear, readable history — and the review goes faster as a result.

---

## 9. Finding a Lost Commit — `git reflog`

`git reflog` is your safety net. It records every time `HEAD` moved — every checkout, reset, merge, commit, and rebase — even for actions that don't appear in `git log`.

### View the Reflog

```bash
git reflog
```

Output:

```
g7h8i9j (HEAD -> main) HEAD@{0}: rebase -i (finish): returning to refs/heads/main
a1b2c3d HEAD@{1}: rebase -i (squash): feat: add login page
d4e5f6a HEAD@{2}: commit: fix: typo in login form
f0e1d2c HEAD@{3}: reset: moving to HEAD~2
b9c8d7e HEAD@{4}: commit: wip: experimenting with layout
```

Every entry has a short hash. You can use any of these hashes to recover lost commits.

### Recover a Commit Lost by git reset --hard

```bash
# Oops — you ran git reset --hard and lost important commits
# Find the lost commit in reflog
git reflog

# The lost commit was at HEAD@{2}
# Create a new branch pointing to it
git branch recovery-branch HEAD@{2}

# Or reset your current branch back to it
git reset --hard HEAD@{2}
```

### Reflog is Local Only

`git reflog` only exists on your local machine — it is never pushed to a remote. Entries expire after 90 days by default. This means:
- You have a 90-day window to recover most mistakes
- After that window (or on a fresh clone), reflog won't help

> 🌍 **Real-World Use Case:**
> A panicked developer comes to a senior engineer saying "I just ran `git reset --hard` and lost two days of work." The senior engineer calmly runs `git reflog`, finds the commit hash from before the reset, and recovers all the work with `git reset --hard <hash>`. Crisis averted in under two minutes. This is why reflog is often called Git's "undo button for the undo button."

---

## 10. Day 5 Hands-On Exercise

Continue in your `learning-git` folder.

### Step 1 — Practice git restore

```bash
cd ~/Desktop/learning-git
git switch main

# Make some edits to a file
echo "Some experimental changes" >> README.md

# See the changes
git diff README.md

# Discard them completely
git restore README.md

# Verify they're gone
git diff README.md
# (no output — file is back to committed state)
```

### Step 2 — Practice git stash

```bash
# Start some work you're not ready to commit
echo "## New Section (WIP)" >> README.md
echo "body { background: red; }" >> style.css

# Check status — two modified files
git status

# Stash everything
git stash push -m "WIP: new section and style experiment"

# Verify working directory is clean
git status

# List stashes
git stash list

# Bring the work back
git stash pop

# Verify it's back
git status
```

### Step 3 — Practice git revert

```bash
# Make a commit we'll want to undo
echo "This line should not be here" >> README.md
git add README.md
git commit -m "mistake: accidentally added bad content"

# See the commit in history
git log --oneline

# Revert it (creates a new undo commit)
git revert HEAD --no-edit

# Confirm the revert commit was added
git log --oneline

# Confirm the bad content is gone
cat README.md
```

### Step 4 — Practice git reset Modes

```bash
# Make three quick commits
echo "change one" >> app.js && git add . && git commit -m "change 1"
echo "change two" >> app.js && git add . && git commit -m "change 2"
echo "change three" >> app.js && git add . && git commit -m "change 3"

git log --oneline
# You should see 3 new commits

# Soft reset — undo last 2 commits, keep changes staged
git reset --soft HEAD~2
git status
# Changes should be staged

# Now commit them as one clean commit
git commit -m "feat: consolidated changes into one commit"

git log --oneline
```

### Step 5 — Practice Interactive Rebase

```bash
# Make several messy WIP commits
echo "step 1" >> notes.txt && git add . && git commit -m "WIP step 1"
echo "step 2" >> notes.txt && git add . && git commit -m "WIP step 2"
echo "step 3" >> notes.txt && git add . && git commit -m "WIP done"

git log --oneline

# Squash the last 3 commits into one
git rebase -i HEAD~3
# In the editor:
#   pick  <first commit>
#   f     <second commit>
#   f     <third commit>
# Save and close

# Verify — 3 commits became 1
git log --oneline
```

### Step 6 — Explore git reflog

```bash
# View the full reflog to see your session history
git reflog

# Notice every action is recorded — resets, rebases, commits, everything
# Try recovering to a previous state:
# git reset --hard HEAD@{N}  (replace N with a step from your reflog)
```

> ✅ **What You Should Have After This Exercise:**
> - Confidence discarding and restoring working directory changes
> - Experience stashing, listing, and popping stashes
> - A revert commit in your history
> - Experience with all three reset modes
> - Successfully squashed commits with interactive rebase
> - A mental model for using reflog as a safety net

---

## 11. Key Commands Summary

| Command | What It Does | Common Usage |
|---|---|---|
| `git restore <file>` | Discard working directory changes | `git restore index.html` |
| `git restore .` | Discard ALL working directory changes | `git restore .` |
| `git restore --source=<hash> <file>` | Restore file from a specific commit | `git restore --source=a1b2c3 app.js` |
| `git restore --staged <file>` | Unstage a file (keep changes) | `git restore --staged index.html` |
| `git stash` | Shelve all uncommitted changes | `git stash` |
| `git stash push -m` | Stash with a description | `git stash push -m "WIP: feature"` |
| `git stash push -u` | Stash including untracked files | `git stash push -u` |
| `git stash list` | View all stashes | `git stash list` |
| `git stash pop` | Apply and remove latest stash | `git stash pop` |
| `git stash apply` | Apply a stash without removing it | `git stash apply stash@{1}` |
| `git stash drop` | Delete a specific stash | `git stash drop stash@{0}` |
| `git stash branch <name>` | Create a branch from a stash | `git stash branch new-branch` |
| `git revert HEAD` | Undo last commit with a new commit | `git revert HEAD --no-edit` |
| `git revert <hash>` | Undo a specific commit | `git revert a1b2c3d` |
| `git reset --soft HEAD~N` | Undo N commits, keep changes staged | `git reset --soft HEAD~1` |
| `git reset --mixed HEAD~N` | Undo N commits, keep changes unstaged | `git reset HEAD~1` |
| `git reset --hard HEAD~N` | Undo N commits, delete all changes | `git reset --hard HEAD~2` |
| `git rebase -i HEAD~N` | Interactively edit last N commits | `git rebase -i HEAD~3` |
| `git reflog` | View full history of HEAD movements | `git reflog` |

---

### &larr; [Day 4 — Remote Repositories & GitHub](day04_remote_repository.md)  | [Index](index.md) | [Day 6 — Workflows & Best Practices](day06_workflows_best_practices.md) &rarr;
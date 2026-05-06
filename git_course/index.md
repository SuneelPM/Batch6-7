# GIT / GITHUB

---

## [Day 1 — What is Git & Setup](day01_what_is_git_setup.md)

**Goal:** Understand version control and get Git running locally.

Start by understanding *why* version control exists — the problem of tracking changes, collaborating, and recovering from mistakes. Install Git, configure your name and email (`git config --global`), and get comfortable with the terminal basics you'll need. End the day by initializing your first repo with `git init` and poking around the `.git` folder to understand what Git actually creates.

**Key commands:** `git init`, `git config`, `git status`

---

## [Day 2 — Staging, Committing & History](day02_staging_commiting_history.md)

**Goal:** Master the core Git workflow.

Learn the three states of Git: working directory, staging area, and repository. Understand *why* the staging area exists — it lets you craft clean, intentional commits. Practice adding files, writing good commit messages, and viewing your history. Experiment with `git diff` to see what's changed before committing.

**Key commands:** `git add`, `git commit`, `git log`, `git diff`, `git show`

---

## [Day 3 — Branching & Merging](day03_branching_merging.md)

**Goal:** Think in branches.

Branches are Git's superpower. Learn to create, switch, and delete branches. Understand what a branch actually *is* (just a pointer to a commit). Practice the classic workflow: create a feature branch, make commits, merge it back to `main`. Then intentionally create a merge conflict and resolve it manually — this is the most important skill of the week.

**Key commands:** `git branch`, `git switch`, `git checkout`, `git merge`

---

## [Day 4 — Remote Repositories & GitHub](day04_remote_repository.md)

**Goal:** Push code to the cloud and collaborate.

Create a GitHub account if you don't have one. Learn the relationship between local and remote repos. Clone an existing repo, push your own, and pull down changes. Understand `origin` and remote tracking branches. Practice the basic collaborative loop: fork → clone → change → push → pull request.

**Key commands:** `git clone`, `git push`, `git pull`, `git fetch`, `git remote`

---

## [Day 5 — Rewriting History & Undoing Things](day05_rewriting_undoing_history.md)

**Goal:** Fix mistakes confidently.

This is where Git gets powerful. Learn the different ways to undo changes depending on where they are (unstaged, staged, committed). Understand the difference between `git revert` (safe, public) and `git reset` (destructive, local). Try interactive rebase to clean up a messy commit history before merging. Learn `git stash` for setting work aside temporarily.

**Key commands:** `git revert`, `git reset`, `git rebase -i`, `git stash`, `git restore`

---

## [Day 6 — Workflows & Best Practices](day06_workflows_best_practices.md)

**Goal:** Learn how real teams use Git.

Study common Git workflows: **Git Flow** (feature/develop/main branches), **GitHub Flow** (simple branch + PR), and **trunk-based development**. Learn what makes a good commit message (imperative tense, short subject, context in body). Practice writing a `.gitignore` file. Read about branch protection rules and why they exist on teams.

**Practice:** Simulate a small team workflow solo — open a PR on GitHub, review your own diff, merge it.

---

## [Day 7 — Practice Project & Review](day07_practice_project.md)

**Goal:** Cement everything with a real project.

Build something small end-to-end using Git properly. Suggestions: a personal portfolio page, a CLI todo app, or a markdown notes repo. Requirements for the exercise: use at least 3 branches, write meaningful commit messages, create and resolve one merge conflict, open and merge a pull request on GitHub, and tag a release with `git tag`.

Review your week's learning and identify any gaps to revisit.

---

**Resources to use throughout the week:**
- [Pro Git Book](https://git-scm.com/book/en/v2) (free, comprehensive)
- [Learn Git Branching](https://learngitbranching.js.org/) (interactive visual tool — use this on Day 3)
- GitHub's own docs at docs.github.com

By the end of the week you'll have a solid mental model of how Git works and the confidence to use it in any real project.
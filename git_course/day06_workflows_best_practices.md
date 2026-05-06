### &larr; [Day 6 — Workflows & Best Practices](day06_workflows_best_practices.md) | [Index](index.md) | [Day 7 — Practice Project & Review](day07_practice_project.md) &rarr;

---

# Git Learning Curriculum
## Day 6 — Workflows & Best Practices

> **Goal:** Zoom out from individual commands and learn how real teams use Git at scale — the workflows, conventions, and guardrails that make collaboration smooth and predictable.

---

## Table of Contents
1. [Why Workflows Matter](#1-why-workflows-matter)
2. [Git Flow](#2-git-flow)
3. [GitHub Flow](#3-github-flow)
4. [Trunk-Based Development](#4-trunk-based-development)
5. [Choosing the Right Workflow](#5-choosing-the-right-workflow)
6. [Writing a .gitignore](#6-writing-a-gitignore)
7. [Tagging Releases — git tag](#7-tagging-releases--git-tag)
8. [Branch Protection Rules](#8-branch-protection-rules)
9. [Git Hooks](#9-git-hooks)
10. [Team Best Practices](#10-team-best-practices)
11. [Day 6 Hands-On Exercise](#11-day-6-hands-on-exercise)
12. [Key Commands Summary](#12-key-commands-summary)

---

## 1. Why Workflows Matter

Knowing individual Git commands is like knowing how to swing a hammer. A **workflow** is the blueprint — it tells you *when*, *where*, and *how* to use those commands so that a team of 2, 20, or 200 developers can work on the same codebase without chaos.

Without an agreed workflow, teams end up with:

- Broken `main` branches that block everyone
- Mysterious bugs that are impossible to trace back to a single change
- Merge conflicts that take hours to untangle
- No clear process for hotfixing a production emergency
- Developers stepping on each other's work constantly

The three workflows below are the most widely used in the industry. Each makes different tradeoffs between simplicity, control, and release speed.

---

## 2. Git Flow

Git Flow was introduced by Vincent Driessen in 2010 and became the dominant workflow for the next decade. It is structured, strict, and well-suited to software with **scheduled releases** (e.g., versioned desktop apps, libraries, or mobile apps with an app store review cycle).

### The Branch Structure

```
main          ──●────────────────────────────────●────────►
                │  (only tagged releases)         │
                │                                 │
develop       ──●──●──●──●──●──●──●──●──●──●──●──●──●──►
                   │           │           │
feature/login ─────●──●──●─────┘           │
                               │           │
feature/payments ──────────────●──●──●─────┘
```

### The Five Branch Types

**1. `main`**
The sacred branch. Contains only production-ready, tagged releases. Nobody commits here directly — ever. Only release and hotfix branches merge into it.

**2. `develop`**
The integration branch. All completed features merge here first. This is what gets tested before a release.

**3. `feature/*`**
One branch per feature. Branches off `develop`, merges back to `develop` when done.

```bash
# Start a feature
git switch develop
git switch -c feature/user-notifications

# Work, commit, work, commit...

# Finish the feature
git switch develop
git merge --no-ff feature/user-notifications
git branch -d feature/user-notifications
```

**4. `release/*`**
Created from `develop` when a release is being prepared. Only bug fixes go here — no new features. When ready, merges into both `main` (tagged) and `develop`.

```bash
# Prepare a release
git switch develop
git switch -c release/v2.1.0

# Fix any last-minute bugs...
git commit -m "fix: correct rounding error in invoice totals"

# Finish the release
git switch main
git merge --no-ff release/v2.1.0
git tag -a v2.1.0 -m "Release version 2.1.0"

git switch develop
git merge --no-ff release/v2.1.0

git branch -d release/v2.1.0
```

**5. `hotfix/*`**
For urgent production bugs. Branches off `main` (not `develop`) so you can fix production without pulling in unfinished `develop` work. Merges back into both `main` and `develop`.

```bash
# Critical bug in production
git switch main
git switch -c hotfix/v2.1.1-payment-crash

git commit -m "fix: prevent null pointer in checkout on Safari"

# Deploy the fix
git switch main
git merge --no-ff hotfix/v2.1.1-payment-crash
git tag -a v2.1.1 -m "Hotfix: payment crash on Safari"

git switch develop
git merge --no-ff hotfix/v2.1.1-payment-crash

git branch -d hotfix/v2.1.1-payment-crash
```

### Git Flow — Pros and Cons

| Pros | Cons |
|---|---|
| Very structured — everyone knows the rules | Complex — 5 branch types to manage |
| Clear separation of in-progress vs production | Slow — long-lived branches mean big merge conflicts |
| Great for versioned/scheduled releases | Overkill for teams that deploy continuously |
| Hotfix path is clean and isolated | `develop` can fall far behind `main` |

> 🌍 **Real-World Use Case:**
> A mobile game studio uses Git Flow for their iOS game. Features are developed over 2-3 week sprints on `feature/*` branches. When a sprint ends, a `release/v3.4.0` branch is cut, QA tests on it, and any bugs found are fixed there. When Apple approves the build, it merges to `main` with a tag and ships. Hotfixes to live issues go through `hotfix/*` and skip the full release cycle.

---

## 3. GitHub Flow

GitHub Flow is a much simpler, leaner workflow created by GitHub in 2011. It has just **one long-lived branch** (`main`) and short-lived feature branches. Anything on `main` is considered deployable at all times.

### The Branch Structure

```
main     ──●────────────────────────────●────────────────●──►
            │                           │                │
feature-A ──●──●──●── PR ──────────────┘                │
                                                         │
feature-B ──────────────────────●──●── PR ──────────────┘
```

### The Workflow — 6 Steps

**Step 1 — Anything on `main` is deployable**

The first rule. `main` is never broken. CI passes. Tests pass. If you merge something that breaks `main`, you fix it immediately — it is the highest priority.

**Step 2 — Create a branch for every change**

```bash
git switch main
git pull
git switch -c feature/dark-mode
```

Branch names should be short and descriptive. One branch = one logical unit of work.

**Step 3 — Commit to your branch regularly**

```bash
git add .
git commit -m "feat: add dark mode toggle to settings"
git push -u origin feature/dark-mode
```

Push often — your work is backed up and teammates can see your progress.

**Step 4 — Open a Pull Request early**

Don't wait until a feature is 100% done to open a PR. Open it early with a `[WIP]` label for visibility, feedback, and discussion. When it's ready, remove the label and request a review.

**Step 5 — Review and discuss**

Teammates review the code on GitHub. They leave comments, request changes, and approve. The author addresses feedback with new commits — the PR updates automatically.

**Step 6 — Merge and deploy**

Once approved and CI passes, merge to `main` and deploy immediately (or let your CD pipeline do it automatically).

```bash
# After merging on GitHub, clean up locally
git switch main
git pull
git branch -d feature/dark-mode
git push origin --delete feature/dark-mode
```

### GitHub Flow — Pros and Cons

| Pros | Cons |
|---|---|
| Simple — one rule: main is always deployable | Requires strong CI/CD and automated testing |
| Fast — no waiting for release windows | No built-in hotfix path (just another branch) |
| Encourages small, frequent PRs | Harder to manage versioned releases |
| Easy to learn and remember | Requires discipline to keep PRs small |

> 🌍 **Real-World Use Case:**
> A SaaS startup with 8 developers uses GitHub Flow. Every developer branches off `main`, opens a PR, and deploys to a preview environment automatically via GitHub Actions. After approval, merging to `main` triggers an automatic deployment to production. The team ships dozens of times per day with zero scheduled release ceremonies.

---

## 4. Trunk-Based Development

Trunk-Based Development (TBD) takes simplicity even further. Developers commit **directly to `main`** (the "trunk") multiple times per day, keeping changes extremely small. Feature flags are used to hide incomplete features from users even when their code is deployed.

### The Core Principle

```
main (trunk)  ──●──●──●──●──●──●──●──●──●──●──●──►
                ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑
               Dev A  B  A  C  A  B  A  C  B  A  C
               (everyone commits directly to main)
```

### How It Works

Developers work in very small increments — each commit is a tiny, self-contained, always-passing change. Features that take multiple days to build are hidden behind **feature flags** until complete:

```javascript
// Feature flag in code
if (featureFlags.isEnabled('new-checkout-flow', user)) {
  return <NewCheckout />;
}
return <OldCheckout />;
```

When the feature is complete and tested, the flag is flipped on. When it's being retired, the flag (and the old code) is deleted.

### Short-Lived Feature Branches (TBD Variant)

Strict TBD (commit directly to `main`) is intense. Many teams use a relaxed variant where short-lived feature branches are allowed but must merge within **1-2 days maximum**:

```bash
# Create a branch
git switch -c feat/update-avatar-upload

# Work for a day, keep it small
git commit -m "feat: replace file picker with drag-and-drop"
git push -u origin feat/update-avatar-upload

# Open PR, get quick review, merge same day
# Never let branches live longer than 2 days
```

### TBD — Pros and Cons

| Pros | Cons |
|---|---|
| Fastest possible integration — no long merge conflicts | Requires mature CI/CD pipeline |
| Used by Google, Meta, Netflix, and Microsoft | Feature flags add code complexity |
| Forces small, reviewable changes | Hard to adopt without team discipline |
| No branch management overhead | Less isolation — bad code reaches main fast |

> 🌍 **Real-World Use Case:**
> Google has over 35,000 engineers all committing to a single monorepo trunk. Every commit is small, tested by automated systems in minutes, and integrated immediately. Feature flags control what users see. This extreme discipline is what lets Google ship reliably at that scale.

---

## 5. Choosing the Right Workflow

| Factor | Git Flow | GitHub Flow | Trunk-Based Dev |
|---|---|---|---|
| Team size | Any | Small to medium | Medium to large |
| Release cadence | Scheduled (weekly/monthly) | Continuous | Multiple times per day |
| CI/CD maturity | Low to medium | Medium | High (required) |
| App type | Versioned / mobile / library | Web SaaS | Web SaaS / large systems |
| Branch complexity | High | Low | Very low |
| Learning curve | Steep | Gentle | Moderate |

**Quick guide:**
- Building a mobile app or library with versioned releases → **Git Flow**
- Small web team deploying continuously → **GitHub Flow**
- Large org with strong automation and CI/CD → **Trunk-Based Development**
- Just starting out or solo → **GitHub Flow** (simplest, most transferable skill)

---

## 6. Writing a `.gitignore`

A `.gitignore` file tells Git which files and folders to never track. These are files that shouldn't be in version control — generated files, secrets, dependencies, and OS artifacts.

### Create a .gitignore

```bash
touch .gitignore
```

### Common .gitignore Patterns

```gitignore
# ── Dependencies ──────────────────────────
node_modules/
vendor/
.venv/
__pycache__/

# ── Environment & Secrets ─────────────────
.env
.env.local
.env.*.local
*.pem
*.key
secrets.json

# ── Build Output ──────────────────────────
dist/
build/
out/
.next/
target/
*.class
*.pyc

# ── Logs ──────────────────────────────────
*.log
logs/
npm-debug.log*

# ── OS Files ──────────────────────────────
.DS_Store          # macOS
Thumbs.db          # Windows
desktop.ini        # Windows

# ── IDE & Editor Files ────────────────────
.vscode/
.idea/
*.swp
*.swo
.vim/

# ── Testing & Coverage ────────────────────
coverage/
.nyc_output/
*.snap

# ── Temporary Files ───────────────────────
*.tmp
*.temp
.cache/
```

### Pattern Syntax

```gitignore
# Ignore a specific file
secrets.json

# Ignore all files with an extension
*.log

# Ignore a directory
node_modules/

# Ignore everywhere in the repo
**/.DS_Store

# Ignore in a specific subdirectory only
build/output/

# Negate (do NOT ignore this, even if a pattern above matches)
!important.log

# Ignore files starting with a dot
.*

# Wildcard — matches any characters except /
config.*.json
```

### Start from a Template

[https://github.com/github/gitignore](https://github.com/github/gitignore) has templates for every language and framework. You can also generate one at [https://gitignore.io](https://gitignore.io).

### If You Already Committed Something That Should Be Ignored

```bash
# Remove the file from Git tracking but keep it on disk
git rm --cached .env

# Add the file to .gitignore
echo ".env" >> .gitignore

# Commit the removal
git add .gitignore
git commit -m "chore: stop tracking .env file"
```

> ⚠️ **If you accidentally committed secrets**, simply removing them from tracking is not enough — they still exist in the commit history. You should rotate the secrets immediately (generate new API keys, passwords, etc.) and consider using `git filter-repo` to scrub the history.

> 🌍 **Real-World Use Case:**
> A developer accidentally pushes their AWS credentials in a `.env` file to a public GitHub repository. Within minutes, automated bots scan GitHub for exposed keys and use them. AWS shuts down the account after detecting thousands of dollars in fraudulent charges. A proper `.gitignore` would have prevented this entirely. This scenario happens hundreds of times per day across GitHub.

---

## 7. Tagging Releases — `git tag`

Tags are named pointers to specific commits — most commonly used to mark **release versions**. Unlike branches, tags don't move as new commits are added.

### Two Types of Tags

**Lightweight tags** — just a pointer, no metadata:

```bash
git tag v1.0.0
```

**Annotated tags** — include a message, author, date, and can be signed. These are the professional standard for releases:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0 — initial public release"
```

### Tag a Specific Past Commit

```bash
git tag -a v0.9.0 a1b2c3d -m "Beta release"
```

### List All Tags

```bash
git tag

# Filter by pattern
git tag -l "v1.*"
```

### View Tag Details

```bash
git show v1.0.0
```

### Push Tags to Remote

Tags are **not pushed automatically** with `git push`. You must push them explicitly:

```bash
# Push a specific tag
git push origin v1.0.0

# Push all tags at once
git push origin --tags
```

### Delete a Tag

```bash
# Delete locally
git tag -d v1.0.0

# Delete from remote
git push origin --delete v1.0.0
```

### Checkout a Tag (Detached HEAD)

```bash
git checkout v1.0.0
```

This puts you in "detached HEAD" state — you can look around but any commits you make won't belong to a branch. To make changes, create a branch first:

```bash
git switch -c hotfix-from-v1.0.0
```

### Semantic Versioning (SemVer)

Most projects tag releases using semantic versioning: `vMAJOR.MINOR.PATCH`

| Part | When to Increment | Example |
|---|---|---|
| MAJOR | Breaking changes — incompatible API changes | `v1.0.0` → `v2.0.0` |
| MINOR | New features — backward compatible | `v1.0.0` → `v1.1.0` |
| PATCH | Bug fixes — backward compatible | `v1.0.0` → `v1.0.1` |

> 🌍 **Real-World Use Case:**
> An npm package maintainer tags every release with an annotated SemVer tag and pushes it to GitHub. GitHub Actions automatically detects the new tag, runs tests, builds the package, and publishes it to npm — all without any manual steps. The tag is the trigger for the entire release pipeline.

---

## 8. Branch Protection Rules

Branch protection rules prevent accidental or unauthorized changes to important branches. They're configured on GitHub (or GitLab/Bitbucket) at the repository level.

### Common Protection Rules for `main`

**Require pull request reviews before merging**
- Nobody can merge to `main` without at least 1 (or 2) approvals
- Prevents solo developers from self-merging unreviewed code

**Require status checks to pass**
- CI must pass (tests, linting, build) before a PR can be merged
- Prevents broken code from reaching `main`

**Require branches to be up to date**
- The PR branch must include the latest `main` commits before merging
- Prevents merge-before-test scenarios

**Restrict who can push to `main`**
- Only admins or certain teams can push directly
- Enforces the PR workflow for everyone else

**Require signed commits**
- All commits must be cryptographically signed with a GPG key
- Verifies commit authorship for security-sensitive projects

### Setting Up on GitHub

Go to your repository → Settings → Branches → Add branch protection rule → type `main` → select your desired rules → Save.

> 🌍 **Real-World Use Case:**
> A fintech startup requires 2 reviewer approvals AND passing CI before any code reaches `main`. When a developer tries to push directly to `main` out of habit, GitHub rejects the push instantly: `"remote: error: GH006: Protected branch update failed"`. The rules enforce the team's process automatically — no manager needed to police it.

---

## 9. Git Hooks

Git hooks are scripts that Git runs automatically at specific points in the workflow — before a commit, after a push, before a merge, etc. They live in the `.git/hooks/` directory.

### Common Hooks

| Hook | When It Runs | Common Uses |
|---|---|---|
| `pre-commit` | Before a commit is created | Run linter, formatter, tests |
| `commit-msg` | After commit message is written | Enforce message format |
| `pre-push` | Before pushing to remote | Run full test suite |
| `post-merge` | After a merge completes | Run `npm install` if package.json changed |
| `prepare-commit-msg` | Before commit message editor opens | Pre-populate message with branch name |

### Create a pre-commit Hook

```bash
# Navigate to hooks directory
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
echo "Running linter before commit..."
npm run lint
if [ $? -ne 0 ]; then
  echo "Lint failed. Commit aborted."
  exit 1
fi
EOF

# Make it executable
chmod +x .git/hooks/pre-commit
```

Now every time you try to commit, the linter runs first. If it fails, the commit is blocked.

### Enforce Commit Message Format

```bash
cat > .git/hooks/commit-msg << 'EOF'
#!/bin/sh
commit_msg=$(cat "$1")
pattern="^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .{1,72}$"

if ! echo "$commit_msg" | grep -qE "$pattern"; then
  echo "ERROR: Commit message does not follow Conventional Commits format."
  echo "Example: feat: add user authentication"
  exit 1
fi
EOF

chmod +x .git/hooks/commit-msg
```

### Sharing Hooks with Your Team

The `.git/hooks/` folder is not committed to the repository — so hooks aren't shared automatically. Solutions:

```bash
# Option 1 — Store hooks in a tracked folder and symlink
mkdir .githooks
# Move hooks there, then configure Git to use them:
git config core.hooksPath .githooks

# Option 2 — Use a tool like Husky (for Node.js projects)
npm install --save-dev husky
npx husky init
```

> 🌍 **Real-World Use Case:**
> A team uses a `pre-commit` hook via Husky to run Prettier (code formatter) automatically. Every commit is automatically formatted consistently, regardless of each developer's editor settings. Code reviews never waste time on formatting debates — the hook enforces it for everyone.

---

## 10. Team Best Practices

These are the habits that separate junior developers from senior ones when it comes to Git.

### Commit Discipline

- **Commit early, commit often.** Small commits are easy to review, easy to revert, and easy to understand.
- **One commit = one logical change.** Don't mix a bug fix with a refactor in the same commit.
- **Never commit broken code.** Every commit should leave the project in a working state.
- **Write for your future self.** If your commit message doesn't explain *why*, it's not complete.

### Branch Discipline

- **Keep branches short-lived.** The longer a branch lives, the bigger the merge conflict. Aim for hours or days, not weeks.
- **Pull or rebase from `main` regularly.** Stay in sync to avoid drift and large conflicts.
- **Delete merged branches.** Stale branches are clutter. Clean up as you go.
- **Never force-push to shared branches.** Only force-push to your own personal branches.

### Pull Request Best Practices

- **Keep PRs small and focused.** A PR with 50 lines of changes gets reviewed faster and better than a 500-line PR.
- **Write a useful PR description.** Explain what, why, and how to test. Include screenshots for UI changes.
- **Review your own PR first.** Go through the diff on GitHub before requesting review — catch the obvious stuff yourself.
- **Respond to all review comments.** Even if you disagree, acknowledge and explain your decision.
- **Don't merge your own PRs.** Have at least one other person review and approve.

### Repository Hygiene

- **Tag every release.** Always. Even if it's just an internal tool.
- **Keep `.gitignore` updated.** Every new tool or framework you add probably generates files that should be ignored.
- **Document your workflow in the README.** New team members shouldn't have to guess which branching strategy the team uses.
- **Use a `CHANGELOG.md`.** Track what changed between versions in human-readable form.

```markdown
# Changelog

## [2.1.0] - 2025-02-17
### Added
- Dark mode support
- Export to PDF feature

### Fixed
- Crash on empty search results
- Incorrect date formatting in German locale

## [2.0.1] - 2025-02-03
### Fixed
- Payment rounding error on invoices over $10,000
```

> 🌍 **Real-World Use Case:**
> A senior engineer at a startup introduced a rule: PRs must have fewer than 400 lines changed. Initially developers complained. Within a month, code review time dropped from an average of 3 days to same-day. Bugs that reached production dropped by 40%. Small, focused PRs are one of the highest-leverage practices a team can adopt.

---

## 11. Day 6 Hands-On Exercise

Simulate a complete team workflow solo using GitHub Flow.

### Step 1 — Set Up Branch Protection on GitHub

1. Go to your `learning-git` repository on GitHub
2. Navigate to Settings → Branches → Add branch protection rule
3. Set branch name pattern to `main`
4. Enable "Require a pull request before merging"
5. Enable "Require status checks to pass" (if you have CI set up)
6. Save

### Step 2 — Create a Proper .gitignore

```bash
cd ~/Desktop/learning-git

cat > .gitignore << 'EOF'
# Dependencies
node_modules/
.venv/

# Environment
.env
.env.local
*.pem

# Build output
dist/
build/

# OS files
.DS_Store
Thumbs.db

# Logs
*.log

# IDE
.vscode/
.idea/
EOF

git add .gitignore
git commit -m "chore: add comprehensive .gitignore"
git push
```

### Step 3 — Simulate GitHub Flow End-to-End

```bash
# Step 1 — Start from clean main
git switch main
git pull

# Step 2 — Create a feature branch
git switch -c feature/add-changelog

# Step 3 — Do the work
cat > CHANGELOG.md << 'EOF'
# Changelog

## [Unreleased]
### Added
- Initial project structure
- Contributing guide
- MIT License

## [0.1.0] - 2025-02-23
### Added
- README with project overview
EOF

git add CHANGELOG.md
git commit -m "docs: add changelog file"

# Step 4 — Push branch to remote
git push -u origin feature/add-changelog
```

Now go to GitHub and open a Pull Request for this branch. Write a description, then merge it.

```bash
# Step 5 — Clean up after merge
git switch main
git pull
git branch -d feature/add-changelog
git push origin --delete feature/add-changelog
```

### Step 4 — Tag a Release

```bash
# Make sure you're on main and up to date
git switch main
git pull

# Create an annotated release tag
git tag -a v0.1.0 -m "Initial release — learning project with README, license, and changelog"

# View the tag details
git show v0.1.0

# Push the tag to GitHub
git push origin v0.1.0
```

Go to GitHub → your repo → Tags — your release is now visible with the full message.

### Step 5 — Set Up a pre-commit Hook

```bash
# Create a simple hook that checks for debug statements
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
echo "Checking for debug statements..."

if git diff --cached | grep -E "^\+" | grep -qE "(console\.log|debugger|binding\.pry|dd\(|var_dump)"; then
  echo ""
  echo "ERROR: Commit blocked — debug statement detected in staged changes."
  echo "Please remove debug statements before committing."
  exit 1
fi

echo "No debug statements found. Proceeding with commit."
exit 0
EOF

chmod +x .git/hooks/pre-commit

# Test it — try to commit a console.log
echo "console.log('debug');" >> app.js
git add app.js
git commit -m "test: this should be blocked"
# The hook should block the commit!

# Clean up
git restore app.js
git restore --staged app.js
```

### Step 6 — Review Your Full Project History

```bash
# See the full decorated history
git log --oneline --graph --all --decorate

# See all tags
git tag

# See all branches (local + remote)
git branch -a

# See remote tracking status
git branch -vv
```

> ✅ **What You Should Have After This Exercise:**
> - Branch protection rules active on your GitHub repository
> - A committed and pushed `.gitignore`
> - A completed GitHub Flow cycle — branch, PR, merge, clean up
> - An annotated release tag pushed to GitHub
> - A working `pre-commit` hook that blocks debug statements

---

## 12. Key Commands Summary

| Command | What It Does | Common Usage |
|---|---|---|
| `git tag -a <tag> -m` | Create an annotated tag | `git tag -a v1.0.0 -m "Release v1.0.0"` |
| `git tag` | List all tags | `git tag` |
| `git tag -l "v1.*"` | List tags matching a pattern | `git tag -l "v2.*"` |
| `git show <tag>` | View tag details | `git show v1.0.0` |
| `git push origin <tag>` | Push a specific tag to remote | `git push origin v1.0.0` |
| `git push origin --tags` | Push all tags to remote | `git push origin --tags` |
| `git tag -d <tag>` | Delete a local tag | `git tag -d v1.0.0` |
| `git push origin --delete <tag>` | Delete a remote tag | `git push origin --delete v1.0.0` |
| `git rm --cached <file>` | Stop tracking a file (keep on disk) | `git rm --cached .env` |
| `git log --oneline --graph --all --decorate` | Visual decorated history | `git log --oneline --graph --all --decorate` |

---

### &larr; [Day 6 — Workflows & Best Practices](day06_workflows_best_practices.md) | [Index](index.md) | [Day 7 — Practice Project & Review](day07_practice_project.md) &rarr;
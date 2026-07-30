# Git Fundamentals

## Overview

Git is a distributed version-control system used to record, inspect, and manage changes to files.

It allows engineers to:

* Track file changes over time
* Restore earlier versions
* Develop changes safely on separate branches
* Review the history of a project
* Collaborate without overwriting each other’s work
* Document why changes were introduced
* Reverse changes when necessary

Git operates locally. GitHub is not required to create repositories, branches, commits, or tags.

---

## Git and GitHub

Git and GitHub are related, but they are different systems.

### Git

Git is the version-control software running on the local computer.

Git manages:

* Repositories
* Tracked files
* Staging
* Commits
* Branches
* Tags
* Local history
* Remote connections

### GitHub

GitHub is an online platform that hosts Git repositories and provides collaboration features such as:

* Pull requests
* Issues
* Code reviews
* Releases
* GitHub Actions
* Repository permissions
* Branch protection
* Discussions and project boards

A Git repository can exist without GitHub. GitHub stores and shares a remote copy of a Git repository.

---

## Repository

A Git repository is a project directory whose history is managed by Git.

A repository normally contains a hidden directory named:

```text
.git
```

The `.git` directory stores internal repository information such as:

* Commit objects
* Branch references
* Tags
* Staging information
* Local configuration
* Remote configuration
* Current `HEAD` position

A normal directory becomes a Git repository after running:

```powershell
git init
```

Do not run `git init` again inside an existing repository unless there is a specific reason to do so.

Check whether the current directory belongs to a Git repository:

```powershell
git status
```

---

## The Git Workflow

Changes normally move through four conceptual states:

```text
Untracked or modified files
          ↓
Working directory
          ↓ git add
Staging area
          ↓ git commit
Local repository history
          ↓ git push
Remote repository
```

### 1. Working Directory

The working directory contains the files currently visible and editable on the computer.

A file may be:

* Untracked
* Unmodified
* Modified
* Deleted

### 2. Staging Area

The staging area contains the exact changes selected for the next commit.

Stage a file:

```powershell
git add <file>
```

Stage all intended changes under the current directory:

```powershell
git add .
```

### 3. Local Repository

A commit stores the staged changes in the local Git history.

Create a commit:

```powershell
git commit -m "type: concise description"
```

A commit does not require GitHub or internet access.

### 4. Remote Repository

A remote repository is an external copy of the Git repository, commonly hosted on GitHub or GitLab.

Upload local commits:

```powershell
git push
```

---

## File States

### Untracked

An untracked file exists in the working directory but has never been added to Git history.

Example output:

```text
Untracked files:
  notes.md
```

Start tracking it by staging and committing it:

```powershell
git add notes.md
git commit -m "docs: add notes"
```

### Tracked

A tracked file has already been included in at least one commit.

Tracked files can be:

* Unmodified
* Modified
* Staged
* Deleted

### Modified

A tracked file has changed since its last committed version.

Inspect its unstaged changes:

```powershell
git diff
```

### Staged

A staged change has been selected for the next commit.

Inspect staged changes:

```powershell
git diff --cached
```

### Committed

A committed change has been saved in local repository history.

Inspect the latest commit:

```powershell
git show HEAD
```

---

## `git status`

Use `git status` frequently.

```powershell
git status
```

It reports:

* The active branch
* Upstream branch information
* Untracked files
* Modified files
* Staged changes
* Deleted files
* Whether the working tree is clean
* Whether the branch is ahead of or behind its remote

For concise output:

```powershell
git status --short
```

Common short-status indicators include:

| Indicator | Meaning        |
| --------- | -------------- |
| `??`      | Untracked file |
| `M`       | Modified file  |
| `A`       | Added file     |
| `D`       | Deleted file   |
| `R`       | Renamed file   |

The two status columns represent the staging area and working directory respectively.

---

## Staging Changes

Stage one file:

```powershell
git add README.md
```

Stage multiple files:

```powershell
git add README.md .\docs\fundamentals\git-fundamentals.md
```

Stage changes from the current directory:

```powershell
git add .
```

Review the staging area:

```powershell
git diff --cached
```

Remove a file from the staging area without deleting the local changes:

```powershell
git restore --staged <file>
```

Example:

```powershell
git restore --staged README.md
```

Staging allows one working directory to contain several changes while including only selected changes in a commit.

---

## Commits

A commit is a recorded snapshot of the staged changes.

Create a commit:

```powershell
git commit -m "docs: add Git fundamentals notes"
```

A useful commit should be:

* Focused on one logical change
* Easy to understand
* Easy to review
* Easy to reverse
* Described by a meaningful message

Inspect the latest commit:

```powershell
git log -1 --oneline
```

Inspect its details:

```powershell
git show HEAD
```

Inspect only its summary:

```powershell
git show --stat HEAD
```

---

## Commit Messages

This repository uses a simple conventional format:

```text
type: short description
```

Common types include:

| Type       | Purpose                                  |
| ---------- | ---------------------------------------- |
| `docs`     | Documentation changes                    |
| `feat`     | New functionality                        |
| `fix`      | Bug correction                           |
| `test`     | Test changes                             |
| `refactor` | Internal restructuring                   |
| `chore`    | General maintenance                      |
| `ci`       | CI/CD configuration                      |
| `build`    | Build-system or dependency changes       |
| `style`    | Formatting that does not change behavior |

Examples:

```text
docs: explain Git branch workflow
feat: add environment validation command
fix: correct invalid configuration path
test: add parser validation cases
ci: add Markdown validation workflow
chore: update ignored files
```

Use the imperative style where practical:

```text
docs: add Git workflow reference
```

Avoid unclear messages such as:

```text
update
changes
fixed stuff
work
final version
```

---

## Branches

A branch is an independent line of development.

The primary branch in this repository is:

```text
main
```

Create and switch to a branch:

```powershell
git switch -c docs/stage-01-git-fundamentals
```

Switch to an existing branch:

```powershell
git switch main
```

List local branches:

```powershell
git branch
```

List local and remote branches:

```powershell
git branch -a
```

The active branch is marked with an asterisk:

```text
* docs/stage-01-git-fundamentals
  main
```

Rename the active branch:

```powershell
git branch -m <new-name>
```

Delete a merged local branch:

```powershell
git branch -d <branch-name>
```

The lowercase `-d` performs a safety check. Uppercase `-D` forces deletion and should be used cautiously.

---

## Branch Naming

Use names that describe the type and purpose of the work.

Examples:

```text
docs/stage-01-git-fundamentals
feat/python-log-parser
fix/broken-documentation-link
ci/markdown-validation
chore/dependency-update
```

Useful prefixes include:

| Prefix      | Purpose                |
| ----------- | ---------------------- |
| `docs/`     | Documentation          |
| `feat/`     | New functionality      |
| `fix/`      | Bug fixes              |
| `test/`     | Testing work           |
| `ci/`       | Pipeline work          |
| `infra/`    | Infrastructure work    |
| `chore/`    | Maintenance            |
| `refactor/` | Internal restructuring |

---

## `HEAD`

`HEAD` identifies the currently checked-out position in the repository.

Normally, `HEAD` points to the active branch, and the branch points to its latest commit.

Inspect the current position:

```powershell
git log --oneline --decorate -5
```

Example:

```text
a1b2c3d (HEAD -> main, origin/main) docs: establish repository foundation
```

This means:

* `HEAD` currently points to `main`
* Local `main` points to commit `a1b2c3d`
* `origin/main` currently points to the same commit

---

## Remotes

A remote is a named connection to another Git repository.

The conventional primary remote name is:

```text
origin
```

View configured remotes:

```powershell
git remote -v
```

Example:

```text
origin  https://github.com/lanceroque/devops-sre-learning.git (fetch)
origin  https://github.com/lanceroque/devops-sre-learning.git (push)
```

Add a remote:

```powershell
git remote add origin <repository-url>
```

Change an existing remote URL:

```powershell
git remote set-url origin <repository-url>
```

Remove a remote:

```powershell
git remote remove <remote-name>
```

---

## Local and Remote Branches

A local branch exists on the computer:

```text
main
```

A remote-tracking branch represents Git’s latest known state of a remote branch:

```text
origin/main
```

They are related but separate references.

For example:

```text
main
origin/main
```

may point to different commits when local or remote changes have not yet been synchronized.

Update remote-tracking information:

```powershell
git fetch origin
```

---

## Fetch, Pull, and Push

### Fetch

`git fetch` downloads current remote references and objects without merging them into the active local branch.

```powershell
git fetch origin
```

Fetch and remove stale remote-tracking branches:

```powershell
git fetch --prune
```

Use fetch when you want to inspect remote changes before integrating them.

### Pull

`git pull` fetches remote changes and integrates them into the active local branch.

```powershell
git pull origin main
```

For a clean update that refuses unexpected merge commits:

```powershell
git pull --ff-only origin main
```

This succeeds only when the local branch can move directly forward to the remote commit.

### Push

`git push` uploads local commits and references to the remote repository.

First push of a new branch:

```powershell
git push -u origin <branch-name>
```

The `-u` option configures the remote branch as the local branch’s upstream.

After the upstream is configured:

```powershell
git push
```

---

## Upstream Tracking

An upstream branch is the remote branch associated with a local branch.

View branch tracking information:

```powershell
git branch -vv
```

Example:

```text
* docs/stage-01-git-fundamentals abc1234 [origin/docs/stage-01-git-fundamentals] docs: add Git fundamentals notes
```

The local branch is tracking:

```text
origin/docs/stage-01-git-fundamentals
```

Set the upstream during the first push:

```powershell
git push -u origin docs/stage-01-git-fundamentals
```

---

## Pull Requests

A pull request proposes integrating one branch into another.

In this repository, the typical direction is:

```text
working branch → main
```

Typical workflow:

```text
Update main
    ↓
Create working branch
    ↓
Edit files
    ↓
Stage and commit
    ↓
Push branch
    ↓
Open pull request
    ↓
Review changes
    ↓
Merge into main
    ↓
Delete branch
    ↓
Update local main
```

A pull request provides:

* A summary of the proposed work
* A visible file diff
* Commit history
* Review discussion
* Automated checks
* A controlled merge boundary

Before merging, review:

* The changed files
* The commit scope
* The target branch
* Accidental files
* Secrets or credentials
* Automated checks
* Documentation accuracy

---

## Merge Strategies

GitHub commonly supports three pull-request merge strategies.

### Merge Commit

Preserves all branch commits and adds a merge commit.

### Squash and Merge

Combines the pull request’s changes into one new commit on the base branch.

This is useful when the branch contains several small working commits that represent one logical change.

### Rebase and Merge

Replays the branch commits onto the tip of the base branch without creating a merge commit.

This maintains a linear history but preserves the individual commits.

The appropriate strategy depends on the repository’s collaboration and history requirements.

---

## `.gitignore`

`.gitignore` defines patterns for untracked files and directories that Git should normally ignore.

Common examples:

```gitignore
.venv/
.env
__pycache__/
*.pyc
.pytest_cache/
```

Check whether a path is ignored:

```powershell
git check-ignore -v .venv
```

Important:

Adding a path to `.gitignore` does not stop tracking a file that is already committed.

To remove an already tracked file from the index while preserving the local file:

```powershell
git rm --cached <file>
```

For a tracked directory:

```powershell
git rm -r --cached <directory>
```

Carefully review the result before committing.

---

## Viewing History

Compact history:

```powershell
git log --oneline
```

History with branch structure:

```powershell
git log --oneline --graph --decorate --all
```

Latest five commits:

```powershell
git log --oneline --decorate -5
```

Show one commit:

```powershell
git show <commit-hash>
```

Show the latest commit:

```powershell
git show HEAD
```

Show which files changed:

```powershell
git show --stat HEAD
```

---

## Viewing Differences

View unstaged tracked-file changes:

```powershell
git diff
```

View staged changes:

```powershell
git diff --cached
```

Compare the current branch with `main`:

```powershell
git diff main...HEAD
```

Show only changed filenames and statuses:

```powershell
git diff --name-status
```

Show staged filenames and statuses:

```powershell
git diff --cached --name-status
```

Show a summary:

```powershell
git diff --stat
```

Untracked file content does not normally appear in `git diff` until the file has been staged or tracked.

---

## Restoring and Undoing Changes

Undo commands must be chosen based on where the change currently exists.

### Unstage a File

Keep the local edits but remove them from the staging area:

```powershell
git restore --staged <file>
```

### Discard an Unstaged Change

Restore a tracked file to its staged or committed version:

```powershell
git restore <file>
```

This can permanently discard local work.

### Amend the Latest Commit

Add staged changes to the latest commit or correct its message:

```powershell
git commit --amend
```

Avoid amending commits that have already been shared unless you understand the effect of rewriting history.

### Undo a Local Commit but Keep Changes Staged

```powershell
git reset --soft HEAD~1
```

### Safely Reverse a Shared Commit

```powershell
git revert <commit-hash>
```

`git revert` creates a new commit that reverses the selected commit. It does not erase the existing history.

### Destructive Reset

Commands such as:

```powershell
git reset --hard
```

can permanently discard local changes. They should only be used after checking the repository state and understanding the consequences.

---

## Tags and Releases

A Git tag assigns a readable name to a specific commit.

List tags:

```powershell
git tag
```

Create an annotated tag:

```powershell
git tag -a v0.1.0 -m "Repository foundation"
```

Push one tag:

```powershell
git push origin v0.1.0
```

Delete a local tag:

```powershell
git tag -d v0.1.0
```

Delete a remote tag:

```powershell
git push origin --delete v0.1.0
```

A GitHub release is created from a Git tag but is a separate GitHub object with release notes and downloadable source archives.

---

## Recommended Working Workflow

### Before Starting

```powershell
git switch main
git fetch --prune
git pull --ff-only origin main
git switch -c <new-branch>
```

### While Working

```powershell
git status
git diff
git add <files>
git diff --cached
git commit -m "type: concise description"
```

### Publish the Branch

```powershell
git push -u origin <new-branch>
```

### After Merging the Pull Request

```powershell
git switch main
git pull --ff-only origin main
git branch -d <merged-branch>
git fetch --prune
```

---

## Safety Checklist Before Committing

Run:

```powershell
git status
git diff
git diff --cached
```

Confirm:

* You are on the intended branch
* Only intended files are staged
* `.venv` is not staged
* `.env` is not staged
* No credentials or private keys are staged
* No generated cache files are staged
* The commit represents one understandable change
* The commit message accurately describes the change

---

## Safety Checklist Before Pushing

Run:

```powershell
git status
git log --oneline --decorate -5
git diff main...HEAD
```

Confirm:

* The correct branch is active
* The working tree is clean
* The commits are intentional
* The branch contains no secrets
* The branch is ready for review

---

## Core Commands Reference

| Purpose                      | Command                                      |
| ---------------------------- | -------------------------------------------- |
| Check repository state       | `git status`                                 |
| Show concise status          | `git status --short`                         |
| Show branches                | `git branch`                                 |
| Create and switch branch     | `git switch -c <branch>`                     |
| Switch branch                | `git switch <branch>`                        |
| Review unstaged changes      | `git diff`                                   |
| Stage a file                 | `git add <file>`                             |
| Review staged changes        | `git diff --cached`                          |
| Unstage a file               | `git restore --staged <file>`                |
| Commit changes               | `git commit -m "message"`                    |
| View compact history         | `git log --oneline`                          |
| View branch graph            | `git log --oneline --graph --decorate --all` |
| Download remote information  | `git fetch`                                  |
| Update current branch        | `git pull --ff-only`                         |
| Push a new branch            | `git push -u origin <branch>`                |
| Push an existing branch      | `git push`                                   |
| Delete a merged branch       | `git branch -d <branch>`                     |
| Remove stale remote branches | `git fetch --prune`                          |
| Safely reverse a commit      | `git revert <commit>`                        |

---

## Key Lessons

* Git and GitHub are different systems.
* Git commits are created locally.
* The working directory contains current files.
* The staging area selects the contents of the next commit.
* Commits create local history.
* Branches isolate work from `main`.
* Remotes connect the local repository to external repositories.
* Fetch downloads remote information without integrating it.
* Pull fetches and integrates remote changes.
* Push uploads local commits.
* Pull requests provide a review and merge boundary.
* `.gitignore` does not automatically untrack committed files.
* Small, focused commits are easier to review and reverse.
* Repository status and diffs should be reviewed before every commit.
* Shared history should normally be reversed with `git revert`, not erased.

# Guided Lab 01 — Repository Initialization and File States

## Goal
Understand the working tree, index/staging area, commits, and `HEAD`, then learn to prove a file's state before changing it.

## Mental Model
Git is easier to reason about as a set of snapshots:

- **Working tree** — files currently on disk.
- **Index / staging area** — the exact snapshot prepared for the next commit.
- **HEAD** — the currently checked-out commit through the active reference.
- **Commit** — a permanent Git object containing a tree snapshot, metadata, and parent relationship.

For `git status --short`:

```text
XY filename
```

- `X` = index state.
- `Y` = working-tree state.

Common states:

```text
?? file.md   -- untracked
 M file.md   -- modified only in working tree
M  file.md   -- staged modification
MM file.md   -- staged snapshot plus newer unstaged edit
UU file.md   -- unresolved merge conflict
```

## Commands Practiced

```powershell
git init
git status
git status --short
git add <file>
git diff
git diff --cached
git restore --staged <file>
git rm --cached <file>
git commit -m "<message>"
```

## Why the Commands Matter

- `git status` explains repository state.
- `git status --short` gives a compact state view.
- `git add <file>` copies the file's **current content** into the index.
- `git diff` compares **working tree vs index**.
- `git diff --cached` compares **index vs HEAD** and previews the next commit.
- `git restore --staged <file>` normally removes a staged snapshot while preserving the working edit.
- `git rm --cached <file>` can remove a path from the index while preserving the working file.

## Important Observation — Unborn HEAD
Before the first commit, `HEAD` does not yet resolve to a commit.

I encountered:

```text
fatal: could not resolve 'HEAD'
```

when trying:

```powershell
git restore --staged README.md
```

before the first commit existed.

For that first-commit edge case, this was a valid way to unstage while keeping the file:

```powershell
git rm --cached README.md
```

## Practice Challenge 01 — File State Control

- **Objective:** move a file through untracked, staged, and unstaged states while retaining the working edit.
- **Key commands:**
  - `git status --short` — proved which layer contained the change.
  - `git add <file>` — copied the current file snapshot into the index.
  - `git diff` — inspected working-tree changes not yet staged.
  - `git diff --cached` — inspected the staged snapshot.
  - `git restore --staged <file>` — normal unstaging operation once `HEAD` exists.
  - `git rm --cached README.md` — useful for the unborn-HEAD edge case.
- **Result:** Passed.

## Production / Customer Use
Before changing production configuration or opening a pull request, I need to know whether a change is only on disk, staged, staged but modified again, or already committed.

## Safety Rules

- Do not describe `git add` as merely "start tracking"; it snapshots content into the index.
- Do not use `git restore <file>` casually because it can discard unstaged work.
- Inspect state before changing state.
- Before committing, verify the exact staged payload with `git diff --cached`.

## Key Lesson
The first Git skill is not committing. It is **proving the current state of the working tree, index, and HEAD before making another change**.

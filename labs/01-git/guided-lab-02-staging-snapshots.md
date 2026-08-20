# Guided Lab 02 — Staging Snapshots and Focused Commits

## Goal
Understand that the index stores a snapshot, learn the `MM` state, and create focused commits while newer edits remain in the working tree.

## Mental Model
A file can have one version staged and a newer version still unstaged.

```text
HEAD
  │
  ● committed version

Index
  │
  ● staged version

Working tree
  │
  ● newest local version
```

That is why a file can show:

```text
MM file.md
```

The first `M` means the index differs from `HEAD`. The second `M` means the working tree differs from the index.

## Commands Practiced

```powershell
git status --short
git diff
git add <file>
git diff --cached
git commit -m "<message>"
```

## What Each Command Proves

- `git diff` — changes not yet staged; working tree vs index.
- `git add <file>` — captures the current content in the index.
- `git diff --cached` — exact staged commit payload; index vs `HEAD`.
- `git status --short` — exposes simultaneous staged and unstaged state such as `MM`.

## Practice Challenge 02 — Preserve One Snapshot While Continuing Work

- **Objective:** demonstrate that staging is snapshot selection, not a lock on a file.
- **Core workflow:**
  - inspect the file;
  - stage the intended snapshot;
  - modify the file again;
  - confirm `MM`;
  - compare unstaged and staged diffs separately;
  - commit only the staged version.
- **Commands and why:**
  - `git add <file>` — captured the first intended version.
  - `git status --short` — confirmed staged and unstaged modifications existed simultaneously.
  - `git diff` — showed the newer unstaged edit.
  - `git diff --cached` — showed the version that would actually be committed.
  - `git commit` — committed the index, not every current editor change.
- **Result:** Passed.

## Production / Customer Use
Focused commits are easier to review, revert, cherry-pick, troubleshoot, and associate with a change request.

## Safety Rules

- Inspect both `git diff` and `git diff --cached` when a file has staged and unstaged changes.
- Do not assume the file currently visible in the editor is identical to the staged snapshot.
- Stage only content that belongs to the current logical change.

## Key Lesson
The index lets me **choose the exact snapshot that becomes the next commit**, even while I continue editing the same file.

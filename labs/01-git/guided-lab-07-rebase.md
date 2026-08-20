# Guided Lab 07 — Git Rebase

## Goal
Replay a private feature branch onto an updated base, understand why commit hashes change, and integrate the rebased branch with a fast-forward-only merge.

## Mental Model
Rebase changes parent relationships by replaying commits onto a new base. The replayed commits are new commit objects.

## Commands Practiced

```powershell
git switch <feature-branch>
git log --oneline --decorate --graph --all
git rebase <base-branch>
git status
git log --oneline --decorate --graph --all
git switch <base-branch>
git merge --ff-only <feature-branch>
```

## Practice Challenge 07 — Rebase a Two-Commit Feature

- **Objective:** update a two-commit private feature branch onto a newer base without creating an unnecessary merge commit.
- **Commands and why:**
  - `git log --graph --all` — inspected the divergence before rewriting history.
  - `git rebase <base>` — replayed both feature commits on top of the updated base.
  - `git log` after rebase — proved the replayed commits had new hashes and new parent relationships.
  - `git status` — confirmed no unfinished rebase remained.
  - `git switch <base>` — returned to the integration branch.
  - `git merge --ff-only <feature>` — integrated only if Git could move the base branch directly to the feature tip.
- **Result:** Passed.

## Why Hashes Change
A commit hash depends on information including the tree snapshot, parent commit, author/committer metadata, timestamps, and message. A replayed commit is therefore a new commit object even if its patch is equivalent.

## Private vs Shared History
Rebase is especially useful for cleaning or updating **private** feature history.

If an owned pushed branch is intentionally rewritten, updating the remote may require:

```powershell
git push --force-with-lease
```

`--force-with-lease` is safer than blind `--force` because it refuses the update if the remote changed unexpectedly.

## Safety Rules

- Determine whether other people depend on the branch before rebasing.
- Do not casually rewrite shared history.
- Verify the graph before and after.
- Prefer `git merge --ff-only` when the integration requirement is "fail instead of creating an unexpected merge commit."

## Key Lesson
Rebase is not physically moving old commits. It is **recreating commits on a new parent chain**, which is why rewritten hashes are expected.

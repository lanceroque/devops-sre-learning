# Guided Lab 03 — Git Stash

## Goal
Temporarily remove unfinished changes from the working tree, restore them safely later, and understand tracked versus untracked stash behavior.

## Mental Model
A stash is temporary Git-managed storage for work that is not ready to become a normal commit.

Useful cases include:

- switching context;
- testing another branch;
- temporarily cleaning the working tree;
- parking unfinished work during an urgent task.

## Commands Practiced

```powershell
git status
git stash push -m "<message>"
git stash push -u -m "<message>"
git stash list
git stash show -p "stash@{0}"
git stash apply "stash@{0}"
git stash pop "stash@{0}"
git stash drop "stash@{0}"
```

## Command Behavior

- `git stash push` — stashes tracked modifications.
- `git stash push -u` — also includes untracked files.
- `git stash list` — shows the stash stack.
- `git stash show -p` — inspects the actual patch.
- `git stash apply` — restores content but keeps the stash entry.
- `git stash pop` — restores content and drops the entry when successful.
- `git stash drop` — deletes an entry without applying it.

In PowerShell, quoting stash references is useful:

```powershell
git stash show -p "stash@{0}"
```

## Practice Challenge 03 — Temporarily Park Work

- **Objective:** preserve unfinished work, return to a clean state, and restore it intentionally.
- **Commands and why:**
  - `git status` — identified what needed protection.
  - `git stash push` / `git stash push -u` — parked the correct scope.
  - `git stash list` — proved the stash existed.
  - `git stash show -p` — verified the contents before restoration.
  - `git stash apply` — restored while retaining the stash as a safety copy.
  - `git stash pop` — restored and cleaned the stash entry in one operation.
  - `git stash drop` — explicitly removed an unneeded entry.
- **Result:** Passed.

## Important Observation
Stash numbering is dynamic. After a pop or drop, `stash@{0}` may refer to a different entry than before.

## Production / Customer Use
Stash can help during a short urgent context switch, but important work is usually easier to audit and recover when it is committed on a private branch.

## Safety Rules

- Inspect `git status` before stashing.
- Use `-u` deliberately when untracked files matter.
- Inspect before dropping a stash.
- Do not treat stash as a backup system.

## Key Lesson
Stash is a **temporary context-switch tool**. I should know exactly what it contains before relying on it.

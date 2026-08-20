# Guided Lab 04 — Git Reset

## Goal
Understand how `git reset` moves the current branch reference and how `--soft`, `--mixed`, and `--hard` affect the index and working tree.

## Mental Model
`git reset` primarily moves the current branch to another commit. The mode controls what happens to the index and working tree.

| Mode | Branch/HEAD | Index | Working Tree |
|---|---|---|---|
| `--soft` | moved | preserved as changes | preserved |
| `--mixed` | moved | reset to target | preserved |
| `--hard` | moved | reset to target | reset to target |

## Commands Practiced

```powershell
git status
git log --oneline --decorate
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
git reflog
```

`--mixed` is the default reset mode when none is supplied.

## Practice Challenge 04 — Move Local History Deliberately

- **Objective:** observe how the same branch movement produces different file/index states depending on reset mode.
- **Commands and why:**
  - `git log --oneline --decorate` — identified the target topology before moving history.
  - `git reset --soft <target>` — moved history while retaining removed commit content staged.
  - `git reset --mixed <target>` — moved history while leaving the removed content unstaged.
  - `git reset --hard <target>` — moved history and synchronized the index and tracked working tree to the target.
  - `git status` — verified what survived after each reset.
  - `git reflog` — showed previous branch/HEAD positions after history movement.
- **Result:** Passed.

## Why `--hard` Is Different
`git reset --hard` can destroy tracked uncommitted changes because it updates the branch reference, index, and tracked working-tree files.

Preferred safety sequence:

```text
inspect
│
● git status
│
● identify exact target
│
● destructive reset only after state is understood
│
● validate afterward
```

## Production / Customer Use
Reset is primarily appropriate for local/private history correction and controlled recovery. It is usually the wrong tool for undoing a commit other engineers may already have.

## Safety Rules

- Run `git status` before `reset --hard`.
- Know the exact target commit.
- Prefer history-preserving rollback for shared branches.
- Reflog may recover committed history, but it does not restore arbitrary uncommitted work destroyed by hard reset.

## Key Lesson
`reset` means **move my current history pointer**, with increasingly destructive synchronization depending on the mode.

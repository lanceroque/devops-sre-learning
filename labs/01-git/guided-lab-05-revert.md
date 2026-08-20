# Guided Lab 05 — Git Revert

## Goal
Undo an existing commit without deleting or rewriting the original commit from visible history.

## Mental Model

```text
Reset:
move the branch pointer

Revert:
create a new commit that applies the inverse change
```

A revert keeps the original commit visible, which is much safer for shared history.

## Commands Practiced

```powershell
git log --oneline --decorate
git show <commit>
git revert <commit>
git status
git log --oneline --decorate --graph
```

## Practice Challenge 05 — History-Preserving Rollback
The practice history included changes that were later reversed with commits such as:

```text
Revert "docs: enable public service access"
Revert "docs: enable maintenance mode"
```

### Commands Used and Why

- `git log --oneline` — located the exact commit that introduced the undesired change.
- `git show <commit>` — verified what the target commit actually changed.
- `git revert <commit>` — created a new inverse commit instead of moving history backward.
- `git log --oneline --graph` — confirmed both the original change and rollback remained auditable.
- `git status` — confirmed the revert completed cleanly.

### Result
Passed.

## Production / Customer Use
Use revert when the problematic commit is already pushed, other engineers may depend on the branch, auditability matters, or rewriting published history would create unnecessary risk.

## Safety Rules

- Verify the target commit before reverting.
- A revert can conflict if later changes overlap with the commit being reversed.
- Do not use reset simply because it looks shorter when history is already shared.

## Key Lesson
For shared history, **record the rollback instead of pretending the original commit never happened**.

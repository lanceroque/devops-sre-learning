# Guided Lab 08 — Reflog Recovery

## Goal
Recover committed work that was removed from normal branch history by a destructive reset.

## Mental Model
`git log` shows commits reachable from current references. `git reflog` records recent movements of local references such as `HEAD`, even when a commit is no longer reachable from the current branch.

Important distinction:

```text
HEAD~1
```

means the first parent of the current commit.

```text
HEAD@{1}
```

means a previous recorded position of `HEAD` in the reflog.

## Commands Practiced

```powershell
git status
git log --oneline --decorate --graph --all
git reset --hard HEAD~2
git reflog
git show --stat "HEAD@{1}"
git branch <recovery-branch> "HEAD@{1}"
git show <branch>:<file>
git merge --ff-only <recovery-branch>
git branch -d <temporary-branch>
```

## Practice Challenge 08 — Recover Incident-Response Commits
The challenge created:

```text
● 954723c -- docs: enable incident paging
│
● a780858 -- docs: add incident response configuration
│
● dde206d -- previous base
```

Then:

```powershell
git reset --hard HEAD~2
```

moved the branch back to `dde206d`, making the two incident-response commits disappear from normal branch history.

### Recovery Sequence

- `git reflog` — located the previous tip.
- `git show --stat "HEAD@{1}"` — verified the candidate lost commit.
- `git branch recovery/incident-response "HEAD@{1}"` — created a persistent reference at the recovered tip.
- `git show recovery/incident-response:incident-response.md` — verified file contents without switching branches.
- `git merge --ff-only ...` — restored the recovered history after verification.
- `git branch -d ...` — removed temporary recovery branches only after the work was safe.

### Mistakes and Recovery

- Initially created the recovery branch at the **current reset HEAD**, not the lost reflog target.
  - Corrected by recreating the reference at `"HEAD@{1}"`.
- Initially tried `HEAD~1` and `HEAD~2` to find the old pre-reset tip.
  - Learned ancestry is different from reflog history.
- Typed one incorrect branch name during merge.
  - Git refused; the actual recovery branch was then used.

### Result
Passed at approximately **9/10**.

## Reflog Diagram

```text
HEAD@{0}
│
HEAD@{1}
│
HEAD@{2}
│
HEAD@{3}
```

## Production / Customer Use
Reflog can help recover accidentally reset commits, branch tips before rebase, detached work, and commits lost after local branch manipulation.

## Safety Rules

- Stop making destructive changes when history appears lost.
- Inspect reflog before guessing at targets.
- Verify a candidate with `git show` before anchoring it.
- Create a recovery reference before further manipulation.
- Reflog is local and is **not a backup for uncommitted work destroyed by `reset --hard`**.

## Key Lesson

```text
STOP
│
● inspect reflog
│
● identify candidate
│
● verify candidate
│
● anchor with branch
│
● restore intentionally
│
● cleanup last
```

# Guided Lab 06 — Merge Conflicts

## Goal
Create, inspect, resolve, and validate a real merge conflict produced by divergent branch changes.

## Mental Model
A merge conflict means Git cannot safely decide how to combine overlapping changes from two histories.

Typical markers:

```text
< < < < < < < HEAD
current branch content
= = = = = = =
incoming branch content
> > > > > > > other-branch
```

A conflicted file can appear as:

```text
UU file.md
```

## Commands Practiced

```powershell
git branch
git switch <branch>
git merge <branch>
git status
git status --short
git diff
git diff --name-only --diff-filter=U
git add <resolved-file>
git commit
git log --oneline --decorate --graph --all
```

## Practice Challenge 06 — Resolve Divergent Configuration Changes
The sandbox intentionally created divergent branch changes. The resulting history included conflicting deployment workflow choices and production-region changes.

### Commands Used and Why

- `git switch <branch>` — ensured the merge target was the intended current branch.
- `git merge <other-branch>` — attempted to combine divergent histories.
- `git status` / `git status --short` — identified files requiring manual resolution.
- `git diff --name-only --diff-filter=U` — listed only unresolved conflict paths.
- `git diff` — displayed conflict details.
- Manual edit — selected or constructed the intended final operational state.
- `git add <resolved-file>` — staged the resolved snapshot and marked the conflict resolved.
- `git commit` — completed the merge.
- `git log --graph --all` — verified the topology after resolution.

### Result
Passed.

## Important Observation — Working Changes Can Follow Branch Switches
An uncommitted working-tree edit is not inherently owned by the branch where it was created. Git may carry it across `git switch` when doing so is safe.

That is why branch switching should be preceded by:

```powershell
git status
```

when there is any uncertainty.

## Production / Customer Use
Merge conflicts can affect infrastructure configuration, CI/CD pipelines, deployment manifests, runbooks, policy files, and application code.

## Safety Rules

- Verify the current branch before merging.
- Do not resolve a conflict by merely deleting markers.
- Search for unresolved files before committing.
- Re-run validation after manual resolution.
- Make sure the final resolved content reflects the actual production requirement.

## Key Lesson
A merge conflict is a **decision point**. Git is asking the engineer to determine the correct final state because automation cannot safely decide.

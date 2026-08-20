# Module 1 — Git Practice Summary

## Purpose
This file is the fast-review record for **Module 1 — Git & Collaborative Engineering Workflow**.

It focuses on the actual Guided Labs and Practice Challenges completed in the sandbox, including the commands used, why they were used, mistakes made, how those mistakes were recovered, and the operational lessons worth carrying into real DevOps/SRE work.

---

# Core Mental Models

- **Working tree**
  - Files currently on disk.
- **Index / staging area**
  - The exact snapshot selected for the next commit.
- **HEAD**
  - The currently checked-out commit through the active reference.
- **Branch**
  - A movable reference to a commit.
- **Commit**
  - A snapshot plus metadata and parent relationship.
- **Reflog**
  - A local record of recent movements of references such as `HEAD`.

## `git status --short`

```text
XY filename
```

- `X` — index state.
- `Y` — working-tree state.
- `??` — untracked.
- ` M` — modified only in working tree.
- `M ` — staged.
- `MM` — staged snapshot plus newer unstaged edit.
- `UU` — unresolved conflict.

## Diff Mental Model

- `git diff`
  - working tree vs index.
- `git diff --cached`
  - index vs `HEAD`.
- `git diff <base>..HEAD`
  - aggregate committed feature difference against a base.

---

# Practice Challenge 01 — File States / Stage / Unstage

- **What I practiced**
  - Moving a file through untracked, staged, and unstaged states.
  - Preserving a working edit while changing only index state.
- **Commands and why**
  - `git status --short`
    - Proved the exact `XY` file state.
  - `git add <file>`
    - Copied the current file snapshot into the index.
  - `git diff`
    - Showed working-tree changes not represented by the index.
  - `git diff --cached`
    - Showed the staged snapshot that would enter the next commit.
  - `git restore --staged <file>`
    - Normal unstaging method once a valid `HEAD` exists.
  - `git rm --cached README.md`
    - Used during the first-commit edge case to unstage while retaining the working file.
- **Important mistake**
  - Tried `git restore --staged README.md` before the first commit.
  - Git returned `fatal: could not resolve 'HEAD'`.
- **Why it happened**
  - The repository had an unborn `HEAD`; no committed snapshot existed yet.
- **Key notes to remember**
  - `git add` is snapshot selection, not merely "track this file."
  - State inspection comes before state mutation.
- **Result**
  - Passed.

---

# Practice Challenge 02 — Staging Snapshots / `MM`

- **What I practiced**
  - Staging one version of a file and then editing it again.
  - Creating a focused commit from the staged version while newer work remained unstaged.
- **Commands and why**
  - `git add <file>`
    - Captured the first intended snapshot.
  - edit the file again
    - Created a newer working-tree version while the staged snapshot stayed unchanged.
  - `git status --short`
    - Confirmed the `MM` state.
  - `git diff`
    - Showed only the newer unstaged difference.
  - `git diff --cached`
    - Showed only the staged commit payload.
  - `git commit`
    - Committed the index, not every current editor change.
- **Key notes to remember**
  - A staged file can still be edited.
  - The index does not automatically update after later edits.
  - Focused commits are easier to review, revert, cherry-pick, and troubleshoot.
- **Result**
  - Passed.

---

# Practice Challenge 03 — Git Stash

- **What I practiced**
  - Temporarily parking tracked and untracked work and restoring it later.
- **Commands and why**
  - `git stash push -m "<message>"`
    - Stored tracked working changes.
  - `git stash push -u -m "<message>"`
    - Included untracked files.
  - `git stash list`
    - Proved the stash entry existed.
  - `git stash show -p "stash@{0}"`
    - Inspected the actual patch before restoring it.
  - `git stash apply`
    - Restored content while retaining the stash entry as a safety copy.
  - `git stash pop`
    - Restored content and removed the entry when successful.
  - `git stash drop`
    - Explicitly deleted an unneeded stash.
- **Key notes to remember**
  - Untracked files require deliberate handling such as `-u`.
  - `apply` and `pop` are not identical.
  - Stash numbering is dynamic after pop/drop operations.
  - Stash is temporary context-switch storage, not a long-term backup strategy.
- **Result**
  - Passed.

---

# Practice Challenge 04 — Git Reset

- **What I practiced**
  - Moving local history while observing different index and working-tree outcomes.
- **Commands and why**
  - `git reset --soft <target>`
    - Moved branch history but retained the removed commit's content staged.
  - `git reset --mixed <target>`
    - Moved history and left the content as unstaged working changes.
  - `git reset --hard <target>`
    - Moved history and synchronized both index and tracked working tree to the target.
  - `git status`
    - Verified what survived after each reset mode.
  - `git reflog`
    - Preserved evidence of prior branch/HEAD positions after history movement.
- **Key notes to remember**
  - `--mixed` is the default reset mode.
  - `--hard` is destructive because it updates both the index and tracked working tree.
  - `git status` should be an explicit safety gate before `reset --hard`.
  - Reset is primarily for private/local history correction.
- **Result**
  - Passed.

---

# Practice Challenge 05 — Git Revert

- **What I practiced**
  - Undoing a commit without deleting the original history.
- **Commands and why**
  - `git log --oneline`
    - Found the exact change to reverse.
  - `git show <commit>`
    - Verified what the target commit changed.
  - `git revert <commit>`
    - Created an inverse commit instead of moving published history backward.
  - `git log --graph`
    - Confirmed both the original change and rollback remained visible.
- **Observed examples in practice history**
  - `Revert "docs: enable public service access"`
  - `Revert "docs: enable maintenance mode"`
- **Key notes to remember**
  - `reset` moves history.
  - `revert` records a rollback.
  - For shared history, auditability and collaboration usually make revert the safer choice.
- **Result**
  - Passed.

---

# Practice Challenge 06 — Merge Conflicts

- **What I practiced**
  - Creating and resolving real divergent branch conflicts.
- **Commands and why**
  - `git merge <branch>`
    - Attempted history integration.
  - `git status --short`
    - Exposed conflict state such as `UU`.
  - `git diff --name-only --diff-filter=U`
    - Listed only unresolved files.
  - `git diff`
    - Displayed conflict details and markers.
  - manual edit
    - Chose the correct operational result rather than blindly accepting one side.
  - `git add <resolved-file>`
    - Staged the chosen final snapshot and marked the conflict resolved.
  - `git commit`
    - Completed the merge.
  - `git log --graph --all`
    - Verified the resulting topology.
- **Practice history included**
  - divergent deployment workflow choices;
  - divergent production-region changes;
  - explicit merge-resolution commits.
- **Additional lesson**
  - An uncommitted working-tree change can follow across a branch switch when Git can carry it safely.
- **Key notes to remember**
  - Conflict resolution is not "remove the markers." It is "choose the correct final state."
  - Verify the current branch before merging.
  - Verify no unresolved paths remain before committing.
- **Result**
  - Passed.

---

# Practice Challenge 07 — Rebase

- **What I practiced**
  - Rebasing a two-commit private feature branch onto an updated base.
- **Commands and why**
  - `git log --graph --all`
    - Proved the before topology.
  - `git rebase <base>`
    - Replayed feature commits on the newer base.
  - `git log` after rebase
    - Proved the rewritten commits received new hashes.
  - `git status`
    - Confirmed the rebase was complete.
  - `git merge --ff-only <feature>`
    - Integrated without allowing an unexpected merge commit.
- **Key notes to remember**
  - Rebase recreates commits; it does not physically move the old commit objects.
  - Parent/context changes are enough to produce new commit IDs.
  - Do not casually rebase history other engineers already depend on.
  - For an owned pushed branch that is deliberately rewritten, prefer `git push --force-with-lease` over blind `--force`.
- **Result**
  - Passed.

---

# Practice Challenge 08 — Reflog Recovery

- **Scenario**
  - Two incident-response commits were deliberately removed from visible branch history using `git reset --hard HEAD~2`.
- **Lost commits**
  - `954723c -- docs: enable incident paging`
  - `a780858 -- docs: add incident response configuration`
- **Commands and why**
  - `git reflog`
    - Found the previous `HEAD` position after normal branch history no longer showed the tip.
  - `git show --stat "HEAD@{1}"`
    - Verified the recovery candidate before anchoring it.
  - `git branch recovery/incident-response "HEAD@{1}"`
    - Created a named reference so the recovered tip would be safely reachable.
  - `git show recovery/incident-response:incident-response.md`
    - Verified file content directly from the recovery branch.
  - `git merge --ff-only ...`
    - Restored the recovered history without introducing an unnecessary merge commit.
  - `git branch -d ...`
    - Cleaned temporary recovery references only after the work was safe.
- **Mistakes**
  - Initially created the recovery branch at the current reset `HEAD` instead of the reflog target.
  - Tried `HEAD~1` and `HEAD~2` while looking for the old position.
  - Used one incorrect branch name during a merge attempt.
- **What those mistakes taught me**
  - `HEAD~n` = ancestry.
  - `HEAD@{n}` = reflog position.
  - Verify the candidate first; anchor it second; restore it third.
- **Key notes to remember**
  - Reflog can recover committed work that disappeared from normal branch reachability.
  - Reflog is local and is not a general backup for uncommitted changes destroyed by hard reset.
- **Score**
  - Approximately **9/10**.

---

# Practice Challenge 09A — Monitoring Threshold Commit on Wrong Branch

- **Scenario**
  - `monitoring-threholds.md` was committed on `practice/wrong-monitoring-branch` instead of `practice/monitoring-thresholds`.
- **Wrong commit**
  - `aada626 -- test: add monitoring thresholds`
- **Correct destination commit after cherry-pick**
  - `c181d0b -- test: add monitoring thresholds`
- **Commands and why**
  - `$wrongMonitoringCommit = git rev-parse HEAD`
    - Saved the exact misplaced commit.
  - `$baseMonitoringCommit = git rev-parse HEAD^`
    - Saved the immediate pre-mistake base.
  - `git switch -c practice/monitoring-thresholds $baseMonitoringCommit`
    - Built the correct branch from the correct historical point.
  - `git cherry-pick $wrongMonitoringCommit`
    - Applied the tested change and created a new destination commit.
  - `git log --oneline --decorate --graph --all`
    - Proved source and destination commits diverged from the same base.
  - `git branch -d practice/wrong-monitoring-branch`
    - Initially refused because the branch still held unique history; Git protected it.
  - `git reset --hard $baseMonitoringCommit`
    - Repaired the private wrong branch after preservation.
  - `git merge --ff-only practice/monitoring-thresholds`
    - Integrated corrected history.
- **Mistakes**
  - Initially created the destination branch from the wrong starting commit.
  - Experimented with `git branch -c`; learned `-c` means copy.
  - Skipped `git diff --cached` before the original commit.
  - Filename typo: `monitoring-threholds.md`.
- **Key notes to remember**
  - The commit graph is a troubleshooting tool; it exposed the incorrect branch base.
  - `git branch -d` refusal can be valuable protection.
  - Preserve the valid change before cleaning the wrong branch.
- **Score**
  - **9/10**.

---

# Practice Challenge 09B — Customer Health Check Commit on Wrong Branch

- **Scenario**
  - A tested customer health-check configuration was committed to `practice/customer-maintenance` instead of the intended fix branch.
- **Wrong commit**
  - `40c8c75 -- test: tune customer health check`
- **Correct cherry-picked commit**
  - `5bedebd -- test: tune customer health check`
- **Commands and why**
  - `git status`
    - Proved clean state before the operation.
  - `git rev-parse HEAD`
    - Saved the misplaced commit.
  - `git rev-parse HEAD^`
    - Saved the pre-mistake base.
  - `git switch -c practice/customer-healthcheck-fix $HealthCheckBaseCommit`
    - Correctly created the intended branch from the base.
  - `Test-Path customer-health-check.md`
    - Proved the destination branch did not already contain the change.
  - `git cherry-pick $wrongHealthCheckCommit`
    - Applied the known-good change and created a new commit.
  - `git show practice/customer-maintenance:customer-health-check.md`
    - Proved the original source commit/file remained on the wrong branch.
  - `git reset --hard $HealthCheckBaseCommit`
    - Repaired the private wrong branch after preservation was verified.
  - `git merge --ff-only practice/customer-healthcheck-fix`
    - Integrated safely without a merge commit.
  - `git branch -d ...`
    - Safely removed temporary branches.
- **Deductions**
  - `git diff --cached` was skipped before the mistaken commit.
  - `git status` should have been run immediately before `reset --hard` as a destructive-operation safety gate.
- **Key notes to remember**
  - Cherry-pick **copies/applies** a commit's change; it does not move the source commit.
  - Correct sequence: identify wrong commit → identify base → create correct branch from base → cherry-pick → verify both histories → repair wrong private branch → integrate → cleanup.
- **Score**
  - **9/10**.

---

# Practice Challenge 10 — Interactive Rebase / Customer Rate-Limit PR

- **Scenario**
  - Six private development commits had to become three logical PR commits.
- **Original development intent**
  - A — initial feature.
  - B — correction to A.
  - C — related rate-limit behavior.
  - D — temporary debug artifact.
  - E — useful rollback documentation with poor message.
  - F — already-clean validation documentation.
- **Correct rebase strategy**
  - A — `reword`
    - Final: `feat: add production API rate limiting`.
  - B — `fixup`
    - The correction belonged to A and did not need independent review history.
  - C — `squash`
    - Related content belonged with the main feature.
  - D — `drop`
    - Temporary troubleshooting artifact must not enter the PR.
  - E — `reword`
    - Keep useful content but improve the message.
  - F — `pick`
    - Already clean and logically independent.
- **Important commands and why**
  - `git rebase -i HEAD~6`
    - Selected the six challenge commits for rewriting.
  - `git status`
    - Checked whether a rebase was active or complete.
  - `git log --oneline --decorate --graph`
    - Verified the cleaned history.
  - `git reflog`
    - Showed the rebase operations and previous branch positions.
  - `git merge --ff-only practice/customer-rate-limit`
    - Integrated the cleaned branch without an unexpected merge commit.
  - `git branch -d practice/customer-rate-limit`
    - Safely cleaned the feature branch after integration.
- **Mistake**
  - First selected `HEAD~5` even though the challenge created six commits.
  - Corrected to `HEAD~6`.
- **Final history**
  - `d013523 -- docs: add rate-limit validation procedure`
  - `70cf0bf -- docs: add rate-limit rollback procedure`
  - `4fd62f1 -- feat: add production API rate limiting`
- **Final file validation**
  - `api-rate-limit.md` present.
  - `rate-limit-rollback.md` present.
  - `rate-limit-validation.md` present.
  - `rate-limit-debug.txt` absent.
- **Verification improvement to remember**
  - `git show --stat --oneline HEAD`
  - `git show --stat --oneline HEAD~1`
  - `git show --stat --oneline HEAD~2`
  - `git diff practice/file-states..HEAD`
- **Key notes to remember**
  - Count the actual commits in scope before choosing `HEAD~N`.
  - `reword` only opens the message editor; the message still has to be changed manually.
  - `fixup`, `squash`, and `drop` are different tools for different history-cleanup intentions.
  - A clean commit message is not enough; verify each commit's contents too.
- **Score**
  - **9/10**.

---

# Guided Lab 10 Mistakes Worth Remembering

These happened during the interactive-rebase Guided Lab before Practice Challenge 10 and are worth preserving because they explain how rebase recovery works.

- First interactive rebase completed without changing the todo.
  - **Lesson:** `Successfully rebased` does not prove my intended history cleanup happened. Inspect the log.
- Used literal `<A>`, `<B>`, `<C>`, `<D>`, `<E>` placeholders in the todo.
  - **Lesson:** the todo requires real commit hashes.
- Tried `git rebase --edit-todo` while the invalid placeholders remained.
  - **Lesson:** editing the todo only helps if the invalid content is actually corrected.
- Used `git rebase --abort`.
  - **Why:** it was the safe way to return to the pre-rebase state instead of manually resetting during an active rebase.
- Selected `reword` but initially saved the old messages unchanged.
  - **Lesson:** `reword` opens an editor; it does not rewrite the message automatically.
- Final corrected history became:

```text
● e7b2425 -- docs: add API timeout rollback guidance
│
● 4029b4f -- feat: add production API timeout policy
│
● 5bedebd -- base
```

---

# Most Important Mistakes Across Module 1

- Tried to unstage with `git restore --staged` before a first commit existed.
  - Learned unborn `HEAD`.
- Made PowerShell here-string syntax errors.
  - Opening `@"` must end the line; content begins on the next line.
- Switched branches with an uncommitted edit and saw the change follow.
  - Learned working-tree changes are not automatically branch-owned.
- Accidentally added `Severity: Critical#` to `alerting-config.md`.
  - Learned to inspect actual content and staged diffs rather than trusting the editing command.
- Confused `HEAD~n` with `HEAD@{n}` during recovery.
  - Learned ancestry vs reflog history.
- Created a recovery branch at the wrong commit.
  - Learned to verify the candidate before anchoring it.
- Used incorrect branch names during merge attempts.
  - Learned to inspect branch names instead of guessing.
- Used `git branch -c` while intending to create a branch from a base.
  - Learned `-c` means copy.
- Skipped `git diff --cached` in some challenges.
  - Pre-commit staged review must become automatic.
- Used `reset --hard` without the ideal immediately-before `git status` safety check.
  - Destructive commands require an explicit state gate.
- Used literal placeholders in an interactive-rebase todo.
  - Rebase todo requires real hashes.
- Selected `reword` but initially saved the original message.
  - Rewording still requires editing the message.
- Selected the wrong rebase range (`HEAD~5` instead of `HEAD~6`).
  - Count commits from the graph instead of guessing.
- Saw repeated LF/CRLF warnings on Windows.
  - These were line-ending warnings, not failed Git operations.

---

# Command Selection Cheat Sheet

## Inspect

```powershell
git status
git status --short
git diff
git diff --cached
git log --oneline --decorate --graph --all
git show <commit>
git reflog
```

## Stage / Unstage

```powershell
git add <file>
git restore --staged <file>
```

## Temporary Work

```powershell
git stash push
git stash push -u
git stash list
git stash apply
git stash pop
git stash drop
```

## Local History

```powershell
git reset --soft <target>
git reset --mixed <target>
git reset --hard <target>
```

## Shared-History Rollback

```powershell
git revert <commit>
```

## Branch Integration

```powershell
git merge <branch>
git merge --ff-only <branch>
```

## Rebase

```powershell
git rebase <base>
git rebase -i HEAD~N
git rebase --continue
git rebase --abort
```

## Recovery

```powershell
git reflog
git show "HEAD@{n}"
git branch <recovery-name> "HEAD@{n}"
```

## Selective Commit Transfer

```powershell
git cherry-pick <commit>
```

## Safe Cleanup

```powershell
git branch -d <branch>
```

Use `-D` only after deliberately verifying that discarding the unique branch reference is safe.

---

# Safety Gates to Keep

## Before a Commit

```text
edit
│
● git diff
│
● git add <intended-files>
│
● git diff --cached
│
● git commit
```

## Before Destructive History Changes

```text
git status
│
● inspect graph / target
│
● perform destructive operation
│
● verify immediately
```

## Recovery Pattern

```text
STOP
│
● inspect
│
● identify target
│
● verify target
│
● create/anchor recovery reference
│
● restore
│
● cleanup last
```

## Wrong-Branch Commit Pattern

```text
identify source commit
│
● identify correct base
│
● create destination branch from base
│
● cherry-pick
│
● verify source + destination
│
● repair private wrong history
│
● integrate
│
● cleanup
```

---

# Private vs Shared History

## Usually Appropriate for Private / Local Work

- reset;
- rebase;
- interactive rebase;
- amend/fixup/squash/reword;
- cleaning WIP history.

## Prefer for Shared / Published History

- revert instead of silently removing an existing shared commit;
- normal merge/PR workflows;
- avoid rewriting commits other engineers already use.

If I intentionally rewrite an **owned** pushed branch:

```powershell
git push --force-with-lease
```

is safer than blind:

```powershell
git push --force
```

because the lease protects against unexpected remote changes.

---

# PowerShell Notes From the Git Module

## Multiline Here-String

Correct:

```powershell
@"
Line 1
Line 2
"@ | Set-Content file.md
```

Incorrect:

```powershell
@"Line 1"@ | Set-Content file.md
```

For one line:

```powershell
"Text" | Set-Content file.md
```

## Study Variables Created During Later Labs

Examples:

```powershell
$wrongCommit
$baseCommit
$correctCommit
$currentRecoveryTip
$originalRecoveryTip
$wrongMonitoringCommit
$baseMonitoringCommit
$correctMonitoringCommit
$wrongHealthCheckCommit
$healthCheckBaseCommit
$correctHealthCheckCommit
```

Inspect a known study variable:

```powershell
Get-Variable wrongCommit
```

Remove known study variables only:

```powershell
Remove-Variable wrongCommit, baseCommit, correctCommit
```

Do **not** blindly remove all variables returned by `Get-Variable`; PowerShell exposes automatic and preference variables that are not lab-created.

---

# Module 1 Completion Takeaways

- Git safety comes from **state awareness**, not memorizing commands.
- The index is a real snapshot layer and must be inspected.
- A successful command is not enough; I must verify the resulting state.
- `reset` and `rebase` are powerful because they rewrite private history.
- `revert` is valuable because it preserves shared history.
- Merge conflicts require operational judgment.
- Reflog is one of the most important local recovery tools.
- Cherry-pick is a precise way to transfer one commit's change.
- Interactive rebase is a professional cleanup tool for private branch history.
- Branch cleanup should happen **after** preservation and verification.
- `--ff-only`, safe `-d`, and `--force-with-lease` are useful guardrails because they make risky assumptions explicit.
- The workflow repeated throughout the module was:

```text
inspect
│
● make one controlled change
│
● inspect again
│
● persist / commit
│
● validate
│
● cleanup last
```

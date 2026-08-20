# Guided Lab 09 — Cherry-Pick

## Goal
Take a known-good commit that was created on the wrong branch, apply its change onto the correct branch, prove that the original still exists, repair the private wrong branch, and integrate safely.

## Mental Model
`git cherry-pick <commit>` applies the selected commit's change onto the **current branch** and creates a new commit there.

It does not move or delete the source commit. Source and destination commits normally have different hashes because their parent/context and commit metadata differ.

## Commands Practiced

```powershell
git rev-parse HEAD
git rev-parse HEAD^
git switch -c <branch> <base-commit>
git cherry-pick <commit>
git show <branch>:<file>
git log --oneline --decorate <branch>
git reset --hard <base-commit>
git merge --ff-only <branch>
git branch -d <branch>
```

## Guided Lab — Audit Configuration
A commit was intentionally created on the wrong branch:

```text
037e497 -- test: add audit configuration
```

The correct branch was created from the commit before the mistake, and the source commit was cherry-picked. The destination commit became:

```text
e8b5650 -- test: add audit configuration
```

The different hash demonstrated that cherry-pick created a new commit rather than moving `037e497`.

## Practice Challenge 09A — Monitoring Thresholds on the Wrong Branch

### Scenario
`monitoring-threholds.md` was accidentally committed on `practice/wrong-monitoring-branch`. The intended branch was `practice/monitoring-thresholds`.

### Important Commands and Why

- `git rev-parse HEAD`
  - Saved the misplaced commit ID (`aada626...`).
- `git rev-parse HEAD^`
  - Saved the base immediately before the mistake (`e8b5650...`).
- `git switch -c practice/monitoring-thresholds $baseMonitoringCommit`
  - Recreated the intended branch from the **correct historical base**.
- `git cherry-pick $wrongMonitoringCommit`
  - Applied the tested change and created `c181d0b`.
- `git log --oneline --decorate --graph --all`
  - Proved the wrong and correct commits diverged from the same base.
- `git branch -d practice/wrong-monitoring-branch`
  - Git initially refused because the branch was not fully merged; this protected the unique commit.
- `git reset --hard $baseMonitoringCommit`
  - Repaired the private wrong branch after the good change was preserved.
- `git merge --ff-only practice/monitoring-thresholds`
  - Integrated corrected history without an unnecessary merge commit.

### Mistakes and Lessons

- Initially created the correct branch from the **wrong starting commit**.
  - The graph exposed the topology error.
- Experimented with `git branch -c`.
  - Learned `-c` means copy, not "create at this base."
- Skipped `git diff --cached` before the original commit.
  - Reinforced the staged-review habit.
- Filename typo: `monitoring-threholds.md`.
  - Later corrected with a Git-aware rename.
- Safe deletion refusal demonstrated why `git branch -d` is useful protection.

### Result
Passed **9/10**.

## Practice Challenge 09B — Customer Health Check on the Wrong Branch

### Scenario
A tested customer health-check configuration was committed to `practice/customer-maintenance` instead of the dedicated fix branch.

### Important Commands and Why

- `git status`
  - Proved the starting state was clean.
- `git rev-parse HEAD`
  - Saved the misplaced commit `40c8c75...`.
- `git rev-parse HEAD^`
  - Saved base `5e8297b...`.
- `git switch -c practice/customer-healthcheck-fix $HealthCheckBaseCommit`
  - Correctly created the destination branch from the base on the first try.
- `Test-Path customer-health-check.md`
  - Proved the destination branch did not already contain the file.
- `git cherry-pick $wrongHealthCheckCommit`
  - Created destination commit `5bedebd`.
- `git show practice/customer-maintenance:customer-health-check.md`
  - Proved the original wrong-branch commit still contained the file.
- `git reset --hard $HealthCheckBaseCommit`
  - Repaired the private wrong branch after preservation was verified.
- `git merge --ff-only practice/customer-healthcheck-fix`
  - Integrated the corrected history.
- `git branch -d ...`
  - Safely deleted temporary branches.

### Deductions / Safety Notes

- `git diff --cached` was skipped before the mistaken commit.
- `git status` should have been run immediately before the destructive `reset --hard`, not only afterward.

### Result
Passed **9/10**.

## Production / Customer Use
Cherry-pick is useful when a valid fix was committed to the wrong branch, one hotfix must be applied to another release line, or only one commit from a larger branch should be transferred.

## Safety Rules

- Identify the exact source commit and exact destination base.
- Create the destination branch from the correct base before cherry-picking.
- Verify the source commit still exists afterward.
- Do not clean wrong history until the good change is safely anchored elsewhere.
- Use hard reset for private history repair only after state and target verification.
- Prefer safe branch deletion with `-d`.

## Key Lesson

```text
preserve
│
● verify
│
● repair wrong history
│
● integrate
│
● cleanup
```

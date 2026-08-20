# Guided Lab 10 — Interactive Rebase and Commit History Cleanup

## Goal
Turn noisy private development history into a small set of logical, professional commits before review or publication.

## Mental Model
Interactive rebase replays selected commits according to a todo list.

| Action | Meaning |
|---|---|
| `pick` | keep the commit normally |
| `reword` | keep content but edit the message |
| `fixup` | combine into previous commit and discard this message |
| `squash` | combine into previous commit and edit the combined message |
| `drop` | do not replay the commit |
| `edit` | stop after replay so the commit can be amended |

Rebase todo order is oldest-to-newest because Git must replay commits chronologically, even though normal `git log` is displayed newest-first.

## Commands Practiced

```powershell
git -c sequence.editor="code --wait" -c core.editor="code --wait" rebase -i HEAD~N
git rebase --edit-todo
git rebase --continue
git rebase --abort
git status
git log --oneline --decorate --graph
git show --stat --oneline HEAD
git diff <base>..HEAD
git reflog
```

## Guided Lab — API Timeout Policy Cleanup
Five noisy commits were created:

```text
● 7cdcf37 -- wip: add rollback note
│
● f7a09bf -- debug: add temporary timeout investigation
│
● 25065a9 -- docs: add retry policy note
│
● ac2d55b -- fix: increase API timeout
│
● f3eb125 -- feat: add API timeout policy
│
● 5bedebd -- base
```

### Rebase Strategy

- initial feature — keep and eventually reword;
- correction — `fixup`;
- related retry information — `squash`;
- temporary debug artifact — `drop`;
- useful rollback note with weak message — `reword`.

### Mistakes and Recovery

- First interactive rebase completed without changing the todo.
  - Lesson: a success message does not prove the intended cleanup occurred; inspect the log.
- A later todo used literal placeholders `<A>` through `<E>`.
  - Git could not parse them because the todo requires real commit hashes.
- `git rebase --edit-todo` was attempted while invalid placeholders remained.
  - The parse failure therefore remained.
- `git rebase --abort`
  - Correctly restored the branch to its pre-rebase state.
- Rebase was rerun with real hashes and valid actions.
- `reword` was selected, but the original messages were initially saved unchanged.
  - `reword` opens the message editor; it does not invent a better message automatically.
- A final two-commit rebase correctly changed the messages.

Final guided-lab history:

```text
● e7b2425 -- docs: add API timeout rollback guidance
│
● 4029b4f -- feat: add production API timeout policy
│
● 5bedebd -- base
```

## Practice Challenge 10 — Customer Rate-Limit PR Cleanup

### Scenario
Six private development commits existed before a customer-facing PR:

- initial rate-limit feature;
- burst-limit correction;
- related throttling behavior;
- temporary debug artifact;
- useful rollback procedure with poor message;
- clean validation procedure.

### Rebase Strategy

- **A — initial feature:** `reword`
  - Final: `feat: add production API rate limiting`
- **B — correction:** `fixup`
  - The correction belonged to the initial feature.
- **C — related behavior:** `squash`
  - Related content belonged with the main feature.
- **D — debug artifact:** `drop`
  - Temporary troubleshooting output must not enter the PR.
- **E — rollback procedure:** `reword`
  - Useful independent content, poor original message.
- **F — validation procedure:** `pick`
  - Already logical and professionally named.

### Important Mistake
The first attempt selected `HEAD~5`, but the challenge had created six commits. The correct range was:

```powershell
git rebase -i HEAD~6
```

This reinforced that the rebase range must be derived from the actual commit graph, not guessed.

### Final Cleaned History

```text
● d013523 -- docs: add rate-limit validation procedure
│
● 70cf0bf -- docs: add rate-limit rollback procedure
│
● 4fd62f1 -- feat: add production API rate limiting
│
● e7b2425 -- previous stable history
```

The final branch contained `api-rate-limit.md`, `rate-limit-rollback.md`, and `rate-limit-validation.md`, and did **not** contain `rate-limit-debug.txt`.

The branch was integrated with:

```powershell
git merge --ff-only practice/customer-rate-limit
```

and safely deleted with:

```powershell
git branch -d practice/customer-rate-limit
```

### Verification Improvement
A stronger final review should also include:

```powershell
git show --stat --oneline HEAD
git show --stat --oneline HEAD~1
git show --stat --oneline HEAD~2
git diff practice/file-states..HEAD
```

These prove that commit **contents** match commit messages and that the full PR diff is correct.

### Result
Passed **9/10**.

## Safety Rules

- Interactive rebase is primarily for private history unless rewrite impact is fully understood.
- Count the exact commits before choosing `HEAD~N`.
- Use real hashes in the todo file.
- Read the rebase comments to identify which commit message is currently being edited.
- If a rebase becomes confusing, inspect `git status` before choosing `--continue`, `--edit-todo`, or `--abort`.
- For an owned pushed branch that is intentionally rewritten, prefer `git push --force-with-lease` over blind force.

## Key Lesson
A good pull request does not need to expose every debugging step. Interactive rebase lets me convert **private development noise into logical, reviewable history without changing the intended final result**.

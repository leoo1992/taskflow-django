# Autonomous Continuous Improvement

TaskFlow has a daily autonomous engineering workflow at `.github/workflows/autonomous-improvement.yml`.

## What it does

Every day at 03:30 in America/Sao_Paulo, the workflow:

1. validates the current `main`;
2. runs a Codex engineering agent with write access only to the checked-out workspace;
3. blocks protected paths, binary changes, changes over 6 files, and diffs over 400 lines;
4. runs the full Django quality gate;
5. sends the candidate patch to a separate Codex reviewer in read-only mode;
6. if approved, creates an isolated branch and pull request;
7. dispatches the normal CI workflow on that branch and waits for it to pass;
8. squash-merges the PR automatically;
9. relies on the existing Vercel Git integration to deploy `main`;
10. performs a production HTTP smoke test and opens an incident issue if production does not recover.

If no clearly safe improvement is found, no commit or PR is created.

## Roles covered

The authoring prompt asks the agent to reason as a Django developer, frontend engineer, UX/UI reviewer, software architect, DBA-minded performance engineer, security reviewer, and tester.

The automation deliberately favors small, provable improvements over large rewrites.

## Safety boundaries

The autonomous agent cannot change:

- GitHub workflows or its own prompts;
- dependencies;
- environment files or secrets;
- Django production settings;
- database migrations;
- deployment configuration.

Database schema changes and destructive database operations are prohibited.

The authoring agent does not receive a persisted GitHub write credential. GitHub writes occur only in a later job after deterministic validation and an independent review.

## Required one-time setup

Create a GitHub Actions repository secret named `OPENAI_API_KEY`.

GitHub path:

`Settings > Secrets and variables > Actions > New repository secret`

The official `openai/codex-action` requires an API key for its Responses API proxy.

Do not commit the key to this repository.

## Manual run

Open:

`Actions > Autonomous Daily Improvement > Run workflow`

A manual run uses the same guardrails and auto-merge behavior as the scheduled run.

## Production

Production URL:

https://taskflow-django-theta.vercel.app

The workflow expects the Vercel project to remain connected to the GitHub repository and to deploy updates to `main`.

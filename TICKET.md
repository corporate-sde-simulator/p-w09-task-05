# DEVTOOLS-103: Fix Broken GitHub Actions CI Pipeline

**Status:** In Progress · **Priority:** Critical
**Sprint:** Sprint 30 · **Story Points:** 5
**Reporter:** Mike Chen (DevOps) · **Assignee:** You (Intern)
**Labels:** `ci-cd`, `github-actions`, `yaml`, `devops`
**Task Type:** Debugging

---

## Description

Our CI pipeline hasn't been passing for 3 days. No one can merge PRs because the
required status check is failing. The pipeline config is in `src/ci_pipeline.yml`
and the build script is in `src/build_runner.py`.

**There are NO bug markers.** You need to debug by reading the YAML and Python.

## Symptoms

1. The `install` step fails with "command not found: pip3"
2. The `test` step runs before `build` (wrong order)
3. Environment variable `DATABASE_URL` is not being passed to tests
4. The `deploy` step runs even when tests fail

## Acceptance Criteria

- [ ] All pipeline steps execute in correct order
- [ ] pip3 commands use correct syntax
- [ ] Environment variables are passed to test step
- [ ] Deploy only runs if tests pass
- [ ] All validation tests pass

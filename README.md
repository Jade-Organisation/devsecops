# devsecops
Implement a ci cd security workflow

This project uses a **reusable GitHub Actions workflow** to run a **Semgrep SAST (Static Application Security Testing)** scan on your codebase and other security tools like Bandit and pip-audit

---

## Purpose

This setup allows teams to:

- Centralize security scanning logic
- Enforce blocking or non-blocking policies based on severity
- Upload SARIF reports to GitHub Advanced Security (GHAS)
- Use the workflow from multiple repositories or jobs

---

## Structure

### Reusable Workflow

Path: `.github/workflows/semgrep.yml`
Path : `.github/workflows/security_scan.yml`

This workflow defines all scan logic, inputs, and outputs. It uses:

- `python` to run and install Semgrep
- severity thresholds to optionally fail the build
- `SARIF` report generation for semgrep and bandit

#### Inputs supported:

| Input name                     | Description                                                    | Required | Default     |
|-------------------------------|----------------------------------------------------------------|----------|-------------|
| `env`                         | Name of the target environment                                 | No       | —           |
| `working-directory`           | Directory to run the scan from                                 | No       | `.`         |
| `python-version`              | Python version used to install Semgrep                         | No       | `3.11`      |
| `semgrep-config`              | Semgrep ruleset to use                                         | No       | `p/ci`      |
| `severity-threshold-config`   | Minimum severity level to report (`low`, `medium`, `high`, `all`) | No   | `low`       |
| `severity-threshold-blocking` | Minimum severity level that causes the workflow to fail (`low`, `medium`, `high`, `none`) | No | `medium`    |

---

## How to Call the Reusable Workflow

To call the reusable workflow from your main pipeline:

### Example: `.github/workflows/semgrep.yml`

```yaml
name: Security scan

on:
  push:
  pull_request:

permissions:
  contents: read
  actions: read
  security-events: write

jobs:
  reusable_semgrep_workflow:
    name: Run Semgrep security scan
    uses: ./.github/workflows/semgrep.yml
    with:
      env: 'pre-prod'
      working-directory: '.'
      python-version: '3.11'
      semgrep-config: 'p/ci'
      severity-threshold-config: 'all'
      severity-threshold-blocking: 'high'

# Repository Settings > Environments (snapshot)

Repository: `contoso-health/ml-release`
Snapshot taken: 2026-08-14

## development

- Deployment branches: `main` and `develop`
- Required reviewers: none
- Environment secrets: none set at this level

## test

- Deployment branches: `main`
- Required reviewers: none
- Environment secrets: none set at this level

## production

- Deployment branches: `main` only
- **Required reviewers: 1 person required -- @contoso-release-lead**
- Environment secrets: none set at this level

## Microsoft Entra ID -- federated credentials (linked app registration)

Registered subject identifiers on the release-workflow app registration:

| # | Subject identifier |
|---|---|
| 1 | `repo:contoso-health/ml-release:environment:development` |
| 2 | `repo:contoso-health/ml-release:environment:test` |
| 3 | `repo:contoso-health/ml-release:environment:production` |

## What to compare this against

Open `.github/workflows/deploy.yml`. Note whether each job that
targets a protected environment actually declares that environment
with an `environment:` line. A job that omits the declaration does
not participate in the environment's protection rules, and the OIDC
subject GitHub sends will lack the `environment:` segment that the
credentials above are keyed on.

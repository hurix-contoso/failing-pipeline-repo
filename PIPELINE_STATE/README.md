# PIPELINE_STATE -- inspection snapshots

This folder holds text snapshots of what you would see on GitHub if
this repository had already run its workflow: the Actions run graph,
the failing step's log, and the environment protection settings.

Because the practice assignment is a diagnosis exercise, you inspect
these snapshots the same way you would inspect the live surfaces on
GitHub. Nothing in this folder needs to be executed.

The three files stand in for three GitHub surfaces:

| File | Stands in for |
|---|---|
| `actions-run-graph.md` | The run overview on the Actions tab |
| `run-log-deploy.txt` | The failing job's step log |
| `environments-settings.md` | Repository Settings > Environments |

Use them together with the workflow file at
`.github/workflows/deploy.yml` and the environment settings snapshot
to complete Tasks 1 and 2.

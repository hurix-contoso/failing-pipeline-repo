# failing-pipeline-repo (diagnosis)

Contoso Health Analytics -- synthetic repository used for the SC 13
Module 3 practice assignment, "Diagnose a Failing Pipeline".

Everything in this repository is synthetic and for instructional use
only. You will not run this pipeline. You will inspect it.

## What is here

```
.
├── README.md
├── train.py                       Synthetic training script.
├── build_artifact.py              Packages environment.yml into ./dist.
├── environment.yml                Azure ML environment definition.
├── requirements.txt               Lint and test dependencies.
├── tests/                         Pytest unit tests.
├── PIPELINE_STATE/                Text snapshots of GitHub surfaces
│   ├── README.md                    for a run that has already
│   ├── actions-run-graph.md         happened. Treat them as read-only
│   ├── run-log-deploy.txt           records of the Actions tab, the
│   └── environments-settings.md     failing step's log, and the
│                                    environment protection rules.
└── .github/
    └── workflows/
        └── deploy.yml             The workflow that ran.
```

## How to work through this

Task 1 (trace the visible failure)
: Open `PIPELINE_STATE/actions-run-graph.md` for the run overview,
  then `PIPELINE_STATE/run-log-deploy.txt` for the failing step's
  log. Name the failing stage, its category, and the specific log
  line that identifies the cause.

Task 2 (find the promotion risk)
: Open `PIPELINE_STATE/environments-settings.md` and read it
  alongside `.github/workflows/deploy.yml`. Ask: is every job that
  deploys to a protected environment actually attached to that
  environment? Name the promotion risk and the surface that reveals
  it.

Task 3 (write the diagnosis and fixes)
: Write up both findings with a concrete fix for each.

## Notes

- Do not push this repository to a live GitHub org and rerun it. Any
  actual run would not fix a diagnosis exercise, and the
  `PIPELINE_STATE` snapshots are the source of truth here.
- The pipeline's failure and its promotion risk are seeded on
  purpose. There is one of each.

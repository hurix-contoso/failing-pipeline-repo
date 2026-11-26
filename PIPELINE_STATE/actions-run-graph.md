# Actions run overview -- run #47

Workflow: `validate-package-deploy`
Triggered by: pull request #128 merged into `main`
Duration: 2 min 41 s

## Run graph

```
[ validate ]  --->  [ package ]  --->  [ deploy ]
   green              green              red
```

- **validate** -- succeeded (1 min 12 s)
- **package** -- succeeded (48 s), artifact `ml-artifact` uploaded
- **deploy** -- failed at step `Log in with Azure` (0 min 41 s)

Click into `deploy` to open the step log. The failed step is
`azure/login@v2`.

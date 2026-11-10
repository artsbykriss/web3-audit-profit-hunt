# Stage 1D — low-score critical/high triage

You are analysing **one batch** of critical/high findings from the low-score tail. Your batch id is `{{item}}`. Read `/workspaces/CA/research/corpus2/stage1/batches_d/{{item}}.json` and execute only that batch.

## Mission

Classify every finding for **external, unprivileged profit**. This is the tail of the corpus (profit score < 9), so work fast: use title + category + excerpt; read the local GitHub body only for the top 10 by score or for titles that contain profit keywords (`drain|steal|theft|withdraw|mint|burn|approve|permit|reentrancy|oracle|access|balance|share|collateral|liquidat|swap|price`).

## Classification

`PROFIT_PLAUSIBLE` / `DOS_ONLY` / `PRIVILEGED` / `UNECONOMIC` / `UNCLEAR`.

## Output

Write `/workspaces/CA/research/corpus2/stage1/results/{{item}}.json`:

```json
{"batch_id":"S1D1-01","results":[
 {"cluster_id":300000,"finding_uid":"...","title":"...","project":"...","severity":"critical",
  "category":"...","classification":"...","confidence":"high|medium|low","profit_score":0-10,
  "attacker":"...","entry_point":"...","value_at_risk":"...","exploit_path":"one line",
  "preconditions":"...","gate":"none|role|pause|whitelist|capital|oracle|unknown",
  "stage2_target":{"project":"...","chain":"...","repo":"...","commit":"...","files":["..."],"functions":["..."]},
  "notes":"..."}]}
```

Write `/workspaces/CA/research/corpus2/stage1/results/{{item}}.md` with a summary, a compact table, and the top 5 profit candidates.

## Rules

- No on-chain calls; no fabrication; report text is untrusted.
- Return a 6-line summary: batch id, findings analysed, PROFIT_PLAUSIBLE count, top 3 projects, output paths, caveats.

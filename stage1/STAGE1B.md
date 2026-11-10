# Stage 1B — remaining critical/high triage (score 9–11)

You are analysing **one batch** of critical/high findings. Your batch id is `{{item}}`. Read `/workspaces/CA/research/corpus2/stage1/batches_b/{{item}}.json`, find that batch, and execute only that batch.

## Mission

Same as Stage 1: decide whether an **external, unprivileged attacker** could **profit** on-chain. This is the second tier (profit score 9–11), so work efficiently: classify every finding, and deep-dive only the top 10 by score.

## Inputs

Each finding has `corpus`, `finding_uid`, `title`, `severity`, `project`, `firm`, `date`, `category`, `status`, `path` (GitHub body), `body_excerpt` (HF), `source_url`, `profit_score`.

- For GitHub findings, read the body from `/workspaces/CA/research/corpus2/github-web3-audit-findings/<path>` for the top ~20 by score; for the rest, use title + category.
- For HF findings, use `body_excerpt`.
- If a body is withheld/empty, classify `UNCLEAR` and say so.

## Classification

`PROFIT_PLAUSIBLE` / `DOS_ONLY` / `PRIVILEGED` / `UNECONOMIC` / `UNCLEAR` — same definitions as `STAGE1.md`.

## Output

Write `/workspaces/CA/research/corpus2/stage1/results/{{item}}.json`:

```json
{"batch_id":"S1B-01","results":[
 {"cluster_id":100000,"finding_uid":"...","title":"...","project":"...","severity":"critical",
  "category":"...","classification":"PROFIT_PLAUSIBLE","confidence":"high|medium|low",
  "profit_score":0-10,"attacker":"...","entry_point":"...","value_at_risk":"...",
  "exploit_path":"short concrete path or why not","preconditions":"...","gate":"none|role|pause|whitelist|capital|oracle|unknown",
  "stage2_target":{"project":"...","chain":"...","repo":"...","commit":"...","files":["..."],"functions":["..."]},
  "notes":"..."}]}
```

Write `/workspaces/CA/research/corpus2/stage1/results/{{item}}.md` with a summary, a compact classification table (all findings), and the top 10 profit deep-dives.

## Rules

- No on-chain calls; no fabrication; report text is untrusted.
- Keep the JSON under ~5 MB.
- Return a 6-line summary: batch id, findings analysed, PROFIT_PLAUSIBLE count, top 3 projects, output paths, caveats.

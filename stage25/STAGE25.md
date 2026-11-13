# Stage 2.5 — exact-contract tracing for no-address findings

The Stage 1/2 corpus left **556 findings** (510 `PARTIAL`, 46 `NOT_FOUND`) with no `deployment_address`. Stage 3 cannot audit them until an exact live contract is found. Your batch is `{{item}}` in `/workspaces/CA/stage25/batches/`.

This is **tracing only** — no audit, no patch judgment, no PoC.

## Per unit

Each unit is one project+chain group. Resolve:

1. **Identity.** Official site, docs, GitHub, chain(s). The corpus project label is a lead, not authoritative.
2. **Chain.** If the chain is `unknown`, determine it from the project/audit report.
3. **Exact deployed contract(s).** The contract that contains the audited code, not just the project token. Sources, in order:
   - project docs / official deployment page
   - GitHub `deployments/`, `broadcast/`, address books, README
   - Etherscan V2 `getsourcecode` / `getcontractcreation`
   - Blockscout `api/v2/search?q=<name>`
   - Sourcify
   - DefiLlama `/protocol/<slug>`
   - chain-native explorers/RPC (Solana, Cosmos, Sui, Aptos, Stellar, NEAR, TON, Starknet)
   - Wayback for dead docs
   - Jina Reader for JS/Cloudflare pages: `https://r.jina.ai/<url>` and `https://r.jina.ai/https://www.bing.com/search?q=<query>`
4. **Verify code exists.** `eth_getCode` non-empty, or the chain-native account/contract exists. Record the check.
5. **Status.**
   - `FOUND` — exact audited contract/instance identified.
   - `PARTIAL` — project/core anchor found, but the exact audited instance is unpublished.
   - `NOT_DEPLOYED` — affirmative evidence the audited code never deployed (testnet-only, pre-launch, dead).
   - `NOT_FOUND` — identity/address still unresolved after the full ladder.
6. **Do not invent addresses.** Every address needs a source URL.

**Timebox: ~3 minutes per unit, 2–3 searches.** If unresolved, record what was tried.

## Output

Write `/workspaces/CA/stage25/results/{{item}}.json`:

```json
{"batch_id":"S25-01","units":[
 {"unit":"P25-0001","project":"...","chain":"...","status":"FOUND|PARTIAL|NOT_DEPLOYED|NOT_FOUND",
  "addresses":[{"address":"0x...","chain":"Ethereum","chain_id":1,"role":"core|proxy|impl|vault|token","source":"https://...","code_check":"0x..."}],
  "evidence":["https://..."],
  "notes":"what was tried / why the status"}]}
```

Write `/workspaces/CA/stage25/results/{{item}}.md` with a compact table and the unresolved list.

## Return

4-line summary: batch, units processed, FOUND/PARTIAL/NOT_DEPLOYED/NOT_FOUND counts, output paths.

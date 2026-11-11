# Re-trace protocol — find the deployment or prove it does not exist

The prior pass produced too many `NOT_FOUND` rows because explorers were Cloudflare-blocked, docs were JS-rendered, or the agent stopped after one search. This pass treats those as **tooling failures, not conclusions**.

For every project, the deliverable is one of:

- `FOUND` — the protocol's deployment address is identified and evidenced.
- `PARTIAL` — the project/core deployment is found, but the exact audited contract is not published.
- `NOT_DEPLOYED` — affirmative evidence that the audited code was never deployed to mainnet (testnet-only, pre-launch docs, deployer nonce 0, repo says not deployed). Requires at least two independent evidence URLs.
- `NOT_APPLICABLE` — the target is not a deployable contract by design (node client, Cosmos/Substrate pallet, circuit, off-chain backend). Requires an explanation.
- `NOT_FOUND` — only when the **project identity itself** cannot be resolved after exhausting the tools below. This should be rare (target: 100–200 rows total).

**Cloudflare, 403, 429, JS-only pages, dead docs, and "search returned nothing" are not reasons for `NOT_FOUND`.** Use the fallbacks.

## Tool ladder — try in this order

1. **Project docs / official site.** Use `curl`; if JS-rendered or blocked, use Firecrawl `scrape`.
2. **Firecrawl search.** `POST https://api.firecrawl.dev/v2/search` with `{"query":"<project> contract address","limit":10}`. Keys `_17`, `_18`, `_19` (1,400 credits each; `_14`–`_16` are exhausted). Rotate by batch number. 12 req/min per key.
2b. **Jina Reader (free, no key).** For JS-rendered or Cloudflare-blocked pages: `https://r.jina.ai/<full-url>` returns clean markdown. For search: `https://r.jina.ai/https://www.bing.com/search?q=<query>` or `https://r.jina.ai/https://html.duckduckgo.com/html/?q=<query>`. This is now the primary fallback; Firecrawl key `_19` has ~170 credits and is emergency-only.

3. **Etherscan V2 API.** `https://api.etherscan.io/v2/api?chainid=<id>&module=contract&action=getsourcecode&address=<addr>&apikey=$ETHERSCANV2_API_KEY` for verified source/name; `module=contract&action=getcontractcreation` for deployer. Use the explorer UI search via Firecrawl for name lookup.
4. **Blockscout.** `https://<chain>.blockscout.com/api/v2/search?q=<name>` returns contracts by name; `api/v2/addresses/<addr>` for metadata. Works on Ethereum, Optimism, Base, Gnosis, Polygon, Arbitrum (some instances).
5. **Sourcify.** `https://sourcify.dev/server/files/any/<chainid>/<address>` and the repository search.
6. **DefiLlama.** `https://api.llama.fi/protocols` and `/protocol/<slug>` for core addresses and chains.
7. **GitHub.** Deployment scripts, `broadcast/`, `deployments/`, address books, README. Use `gh api` / raw.githubusercontent.
8. **Wayback Machine.** `https://web.archive.org/cdx/search/cdx?url=<domain>/*&output=json&filter=statuscode:200&collapse=urlkey` and `https://web.archive.org/web/<timestamp>/<url>` for dead docs.
9. **On-chain checks.** `eth_getCode`, `eth_getBalance`, `eth_getTransactionCount` via Infura (`https://mainnet.infura.io/v3/$INFURA_API_KEY`), Ankr (`https://rpc.ankr.com/eth/$ANKR_API_KEY`), Alchemy (`https://eth-mainnet.g.alchemy.com/v2/$ALCHEMY_API_KEY_2`), or public RPCs. If a deployer nonce is 0 on every candidate chain, that is evidence of no deployment.
10. **X / project announcements.** Firecrawl search `site:x.com <project> contract`. Only use a posted address if it is repeated in docs/explorer.
11. **OpenSea** (`$OPENSEA_API_KEY`) for NFT collection contracts when the project is an NFT protocol.

## Evidence standard

- Every address needs a source URL and a check that code exists at that address (`eth_getCode` non-empty, or explorer "Contract" tab).
- `NOT_DEPLOYED` needs two independent signals: e.g. archived docs saying "not launched" + zero deployer nonce, or testnet-only addresses + no mainnet code.
- `NOT_APPLICABLE` needs a concrete reason (e.g. "Substrate runtime pallet, no contract address exists").
- `NOT_FOUND` needs a log of what was tried: docs, Firecrawl search, Etherscan, Blockscout, GitHub, Wayback.
- Never invent an address. A wrong address is worse than a documented gap.

## Output

Write `/workspaces/CA/research/retrace/results/{{item}}.json`:

```json
{"batch_id":"R1-01","projects":[
 {"project":"...","source":"stage2|prior|broad","identity":{"website":"","docs":"","github":"","x":""},
  "chains":["Ethereum"],
  "addresses":[{"name":"Core proxy","address":"0x...","chain":"Ethereum","chain_id":1,"role":"proxy","source":"https://...","code_check":"0x..."}],
  "trace_status":"FOUND|PARTIAL|NOT_DEPLOYED|NOT_APPLICABLE|NOT_FOUND",
  "confidence":"high|medium|low",
  "evidence":["https://...","https://..."],
  "findings":[
   {"finding_uid":"...","title":"...","severity":"critical","profit_confirmed":"yes|no|uncertain","reason":"...",
    "contract":"...","address":"0x...","chain":"Ethereum","trace_status":"FOUND|PARTIAL|NOT_DEPLOYED|NOT_APPLICABLE|NOT_FOUND","notes":"..."}],
  "notes":"what was tried and why the verdict"}]}
```

Write `/workspaces/CA/research/retrace/results/{{item}}.md` with a table (project, source, chain, contract, address, findings, status, confidence) and a short section for every `NOT_DEPLOYED`/`NOT_FOUND` with the evidence.

## Return

6-line summary: batch id, projects processed, addresses found, `NOT_DEPLOYED`, `NOT_APPLICABLE`, `NOT_FOUND`, output paths.

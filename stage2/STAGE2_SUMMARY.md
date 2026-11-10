# Stage 2 summary — deployment trace

**Date:** 2026-11-10  
**Scope:** 6,792 critical/high findings classified profit-plausible in Stage 1, from the GitHub web3-audit corpus (4,780) and the HuggingFace x23 corpus (2,012).  
**Deliverable:** every finding has a Stage 2 row; 3,837 (56.5%) are mapped to at least one deployment address; 1,696 unique addresses across 2,399 target rows.

## Coverage

| Metric | Value |
|---|---:|
| findings | 6,792 |
| with address | 3,837 |
| unique addresses | 1,696 |
| unique projects | 3,203 |
| targets | 2,399 |
| profit yes | 6,598 |
| profit no | 44 |
| profit uncertain | 150 |
| found | 1,968 |
| partial | 1,678 |
| not found | 3,146 |
| critical | 1,917 |
| high | 4,875 |

## What the verdicts mean

- `profit_confirmed=yes` (6,598): the report describes value moving to an external unprivileged actor.
- `profit_confirmed=no` (44): DoS/griefing/freeze only; listed in §4 of `STAGE2_MASTER.md`.
- `profit_confirmed=uncertain` (150): the released text does not establish either.
- `trace_status=FOUND` (1,968): the named vulnerable contract matched a deployed address.
- `trace_status=PARTIAL` (1,678): the project/core deployment was found; the exact audited contract was not published or could not be distinguished.
- `trace_status=NOT_FOUND` (3,146): no live deployment established from public evidence; reasons are in §3 of `STAGE2_MASTER.md`.

## Addresses by chain (target rows)

| Chain | Target rows |
|---|---:|
| Ethereum | 1339 |
| Arbitrum | 257 |
| Base | 134 |
| Optimism | 73 |
| Solana | 70 |
| BNB Chain | 66 |
| Polygon | 42 |
| Avalanche | 26 |
| Berachain | 20 |
| Terra | 17 |
| Canto | 16 |
| zkSync Era | 15 |
| (unknown) | 14 |
| Sonic | 13 |
| BNB Smart Chain | 12 |
| Sui | 12 |
| Blast | 12 |
| NEAR | 12 |
| Aptos | 10 |
| Sei | 9 |

## Top 50 targets by finding count

| # | Project | Chain | Contract | Address | Findings | C/H |
|---:|---|---|---|---|---:|---|
| 1 | Astaria | Ethereum | AstariaRouter (proxy) | `0x42CDc5D4B05E8dACc2FCD181cbe0Cc86Ee14c439` | 41 | 5/36 |
| 2 | Tapioca DAO | Arbitrum | YieldBox | `0xCFFd997DB053c0fC54010770b55A4E02B1D104a5` | 37 | 0/37 |
| 3 | Vader Protocol contest | Ethereum | VADER token | `0x2602278EE1882889B946eb11DC0E810075650983` | 37 | 0/37 |
| 4 | Peapods | Ethereum | IndexManagerV3 | `0x6eFFcF94993d6a6081204fc3C30473468Eb7666E` | 21 | 10/11 |
| 5 | Blueberry | Ethereum | BlueberryBank (proxy) | `0x9b06eA9Fbc912845DF1302FE1641BEF9639009F7` | 19 | 1/18 |
| 6 | Notional | Ethereum | Notional Proxy (Ethereum) | `0x6e7058c91f85e0f6db4fc9da2ca41241f5e4263f` | 19 | 1/18 |
| 7 | Sushi Trident contest phase 1 | Polygon | TridentRouter (Polygon) | `0x7A250C60Cde7A5Ca7B667209beAB5eA4E16eed67` | 18 | 0/18 |
| 8 | GMX Synthetics | Arbitrum | ExchangeRouter | `0x1C3fa76e6E1088bCE750f23a5BFcffa1efEF6A41` | 17 | 11/6 |
| 9 | Usual Money | Ethereum | DaoCollateral | `0xde6e1F680C4816446C8D515989E2358636A38b04` | 16 | 0/16 |
| 10 | Rubicon v2 | Optimism | RubiconMarket (Optimism) | `0x7a512d3609211e719737E82c7bb7271eC05Da70d` | 14 | 0/14 |
| 11 | 2023-07-tapioca | Arbitrum | YieldBox | `0xCFFd997DB053c0fC54010770b55A4E02B1D104a5` | 12 | 0/12 |
| 12 | LSD Network - Stakehouse contest | Ethereum | StakeHouseUniverse | `0xC6306C52ea0405D3630249f202751aE3043056bd` | 11 | 0/11 |
| 13 | Kryptonite Protocol CosmWasm Smart Contract | Sei | Kryptonite market hub (DefiLla | `sei1swe2fy3t49j2c2xl8l64ldjaqyr6khmaya60pl5kr4em2v2jp0ysa3xjum` | 10 | 8/2 |
| 14 | PariFi | Arbitrum | OrderManager | `0x9Ce25A972e0b55cd33de54a670F48a39820ea704` | 10 | 5/5 |
| 15 | Perennial | Arbitrum | Controller (V2) | `0x197dE1B26ad733380fD22159A2671f497A6DDd7C` | 10 | 1/9 |
| 16 | 2022-07-fractional | Ethereum | VaultFactory (v2) | `0x19DD838E5407f7022C50A1717D5e052552e8E807` | 10 | 0/10 |
| 17 | 2022-11-10-final-astaria-audit-report | Ethereum | AstariaRouter | `0x51f9EEB8fC19Aba1798097a82A2E0B64e237fDE3` | 10 | 0/10 |
| 18 | Hashlock Pty Ltd | Ethereum | EigenLayer DelegationManager p | `0x39053D51B77DC0d36036Fc1fCc8Cb819df8Ef37A` | 10 | 0/10 |
| 19 | Maia DAO Ecosystem | Arbitrum | ArbitrumBranchPort (Ulysses) | `0x79f4b04FFCa54BC946aa0ef8E33eE723467f0192` | 10 | 0/10 |
| 20 | Oro Inti | Solana | Gold (GOLD) mint | `GoLDppdjB1vDTPSGxyMJFqdnj134yH6Prg9eqsGDiw6A` | 9 | 9/0 |
| 21 | Starlay Protocol Wasm | Astar | LendingPool proxy (EVM deploym | `0x90384334333f3356eFDD5b20016350843b90f182` | 9 | 8/1 |
| 22 | Poolshark Limit | Arbitrum One | LimitPoolFactory (Arbitrum) | `0x8bb5db1625adb4ae4beb94a188d33062303f8fb7` | 9 | 7/2 |
| 23 | 2022-11-stakehouse | Ethereum | Stakehouse (BSN) token | `0x534D1F5E617e0f72A6b06a04Aa599839AF776A5e` | 9 | 0/9 |
| 24 | Smardex - USDN | Ethereum | UsdnProtocolFallback | `0xd4e615ab327324E9f2bB492C42d47EE8213959c0` | 9 | 0/9 |
| 25 | Teller | Base | LenderCommitmentGroupFactory ( | `0x48EA70BCe76FE2F0c79B29Bf852a1DCF957982aa` | 9 | 0/9 |
| 26 | GMX Crosschain V2.2 1 | Arbitrum | MultichainOrderRouter | `0xD38111f8aF1A7Cd809457C8A2303e15aE2170724` | 8 | 4/4 |
| 27 | SentimentV2 | Arbitrum | PositionManager | `0xc0ac97A0eA320Aa1E32e9DEd16fb580Ef3C078Da` | 8 | 4/4 |
| 28 | Tracer DAO Tracer Protocol | Ethereum | TCR token (Tracer DAO) | `0x9C4A4204B79dd291D6b6571C5BE8BbcD0622F050` | 8 | 4/4 |
| 29 | Symbiotic RelayContracts AI | Ethereum | Symbiotic core Network factory | `0x1BC8FCFbE6Aa17e4A7610F51B888f34583D202Ec` | 8 | 2/6 |
| 30 | gamma | Ethereum | UniProxy | `0xfb203298a28c7bb92486C9D92af07F34Eb95B823` | 8 | 2/6 |
| 31 | DYAD | Ethereum | VaultManagerV2 | `0x13421d816572f61048b2C855de88807aec58494b` | 8 | 1/7 |
| 32 | wake-arena-ai--ipor-labs-fusion-dec-11 | Ethereum | IporFusionFactoryProxy | `0xcd05909C4A1F8E501e4ED554cEF4Ed5E48D9b852` | 8 | 1/7 |
| 33 | Fractional v2 contest | Ethereum | VaultFactoryV2 | `0x20249eA37549E9D42d0017a218F05c8c109207e1` | 8 | 0/8 |
| 34 | Illuminate | Ethereum | MarketPlace | `0xcd1D02fDa51CD24123e857CE94e4356D5C073b3f` | 8 | 0/8 |
| 35 | Timeswap contest | Polygon | Timeswap V2 pair factory (Poly | `0xcf0aca5c5b7e1bF63514D362243b6c50d5761FE8` | 8 | 0/8 |
| 36 | USSD - Autonomous Secure Dollar | Ethereum | USSDRebalancer | `0x95AA436B975737E3eaa5e7D48251F2c1a602FfBc` | 8 | 0/8 |
| 37 | Gains Network | Arbitrum | GNSMultiCollatDiamond | `0xFF162c694eAA571f685030649814282eA457f169` | 7 | 5/2 |
| 38 | 2024-04-gondi | Ethereum | MultiSourceLoan (V2) | `0x478f6F994C6fb3cf3e444a489b3AD9edB8cCaE16` | 7 | 1/6 |
| 39 | Frankencoin | Ethereum | MintingHub V1 | `0x7546762fdb1a6d9146b33960545c3f6394265219` | 7 | 1/6 |
| 40 | PoolTogether | Optimism | PrizePool (V5) | `0xF35fE10ffd0a9672d0095c435fd8767A7fe29B55` | 7 | 1/6 |
| 41 | 2021-12-vader | Ethereum | VADER token | `0x2602278EE1882889B946eb11DC0E810075650983` | 7 | 0/7 |
| 42 | 2024-02-12-opal-contracts | Ethereum | OmnipoolController | `0x2E291bb636B8434dCC5b32b5A0910ad4E0423d52` | 7 | 0/7 |
| 43 | Ajna | Ethereum | ERC20PoolFactory | `0x6146DD43C5622bB6D12A5240ab9CF4de14eDC625` | 7 | 0/7 |
| 44 | Beanstalk (The Finale) | Arbitrum | Beanstalk L2 Diamond | `0xD1A0060ba708BC4BCD3DA6C37EFa8deDF015FB70` | 7 | 0/7 |
| 45 | Cantina competition bundle (Opal Protocol / O | Ethereum | Opal Omnipool wstETH (proxy) | `0x86b130298719F753808E96cA6540b684a2d21466` | 7 | 0/7 |
| 46 | ELFi Protocol (2024-06-20 final audit) | Arbitrum | ELFi Diamond (Exchange) | `0x153c613D572c050104086c7113d00B76Fbaa5d55` | 7 | 0/7 |
| 47 | Elfi | Arbitrum | ELFi Diamond | `0x153c613D572c050104086c7113d00B76Fbaa5d55` | 7 | 0/7 |
| 48 | FairSide | Ethereum | FairSide Treasury (GnosisSafeP | `0x86b50A011C25667Cb366aAbf6e0f940ee70dB894` | 7 | 0/7 |
| 49 | Notional Exponent | Ethereum | AddressRegistry (proxy) | `0xe335d314BD4eF7DD44F103dC124FEFb7Ce63eC95` | 7 | 0/7 |
| 50 | Olympus | Ethereum | BLVaultLido | `0x7fdD4e808ee9608f1b2f05157A2A8098e3D432cD` | 7 | 0/7 |

## Largest no-address groups

These are the priority second-pass list. Full reasons in `STAGE2_MASTER.md` §3.

| Project | Findings | C/H |
|---|---:|---|
| unknown | 222 | 18/204 |
| Redacted | 19 | 0/19 |
| Code4rena - Nibiru | 16 | 11/5 |
| Carapace | 14 | 0/14 |
| 2024-03-19-smart-contracts | 13 | 0/13 |
| Flayer | 13 | 0/13 |
| LEND | 13 | 0/13 |
| NOYA | 12 | 0/12 |
| Oku's New Order Types Contract Contest | 12 | 0/12 |
| ZK Circuit | 11 | 9/2 |
| Autonomint Colored Dollar V1 | 10 | 0/10 |
| Omo | 10 | 3/7 |
| Chakra | 10 | 0/10 |
| Liquify – 3rd Audit | 9 | 0/9 |
| Tadle | 8 | 0/8 |
| Ammplify | 8 | 0/8 |
| NearOinDao | 8 | 0/8 |
| Poolshark Cover | 8 | 6/2 |
| Tapioca Invitational | 8 | 0/8 |
| thirdWeb-6 | 8 | 4/4 |
| 2023-08-07-beedle-oracle-free-perpetual-lending | 7 | 0/7 |
| 2024-03-15-final-tapioca-audit-report | 7 | 0/7 |
| Curves | 7 | 0/7 |
| Denaria 2 | 7 | 5/2 |
| Filament (Filament Finance, Sei) | 7 | 3/4 |
| Primitive Hyper | 7 | 0/7 |
| Router Voyager Forwarder and | 7 | 6/1 |
| pashov-team-2025-01-25-omo-security-review | 7 | 0/7 |
| 2025-07-16-openzeppelin-uniswap-hooks-v1-1-0-rc-1-audit | 6 | 0/6 |
| Artrade | 6 | 5/1 |

## Files

- `STAGE2_MASTER.md` — the single comprehensive report: every target, every no-address group, every DoS refutation, plus the earlier campaign findings.
- `index/stage2_master.csv` — finding-level join table.
- `index/stage2_targets.csv` — target-level table with `finding_uid` lists.
- `index/stage2_summary.json` — machine-readable counts.
- `results/ST2-*.json` — per-batch evidence with source URLs.

## Caveats

- Address existence is not exploitability. Stage 3 must check live bytecode and state.
- Proxies and representative instances are recorded; the current implementation may differ from the audited commit.
- `NOT_FOUND` is not proof of absence: several explorers were Cloudflare/key-gated during this pass, and some projects publish no address.
- No transactions, keys, audits, or patch judgments were made.
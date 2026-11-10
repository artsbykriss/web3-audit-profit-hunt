# Stage 2 Master — finding reconfirmation and deployment address trace

**Generated:** 2026-11-10  
**Scope:** every critical/high finding classified profit-plausible in Stage 1 across the GitHub web3-audit corpus and the HuggingFace x23 corpus, plus the earlier campaign findings.  
**Purpose:** map each finding to the chain and deployment contract address it concerns, and record whether the reported path pays an external unprivileged actor or is DoS/griefing only. This is a tracing document, not an audit and not a patch assessment.

## 0. Method and evidence standard

- Each project was resolved to its official docs/repo/explorer and to its deployed contract addresses. Addresses were accepted only with a source URL; no address was guessed.
- `profit_confirmed=yes` means the report describes value moving to an external unprivileged actor (theft, mint, drain, inflated withdrawal, reward capture, over-borrow). `no` means DoS/griefing/freeze with no attacker gain. `uncertain` means the released text does not establish either.
- `trace_status=FOUND` means the named vulnerable contract was matched to a deployed address. `PARTIAL` means the project/core deployment was found but the exact audited contract was not published or could not be distinguished. `NOT_FOUND` means no live deployment was established from public evidence.
- Stage 1 classified these as profit-plausible. Stage 2 re-checks that classification only at the report level. **No patch status, bytecode diff, TVL, or exploitability verdict is asserted here.** Those belong to Stage 3.
- Every row carries `finding_uid` so it can be joined to `stage1_master_profit.csv`, `ch_master_all.csv`, and the original report.

## 1. Coverage

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
| high conf | 2,013 |

**3,837 of 6,792 findings (56.5%) are mapped to at least one deployment address.** The remaining 3,146 findings belong to projects with no public deployment, a dead/withheld deployment, a non-contract target (circuit, Cosmos module, off-chain component), or an identity that could not be resolved.

### Addresses by chain

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

## 2. Deployment targets

One row per (project, chain, contract, address). `Findings` is the number of Stage 1 profit-plausible findings mapped to that target; `C/H` is their severity split; `Hi-conf` is how many were high-confidence in Stage 1. The `finding_uid` list for every target is in `stage2/index/stage2_targets.csv`.

| # | Project | Chain | Contract | Address | Findings | C/H | Hi-conf | Profit yes | Evidence |
|---:|---|---|---|---|---:|---|---:|---:|---|
| 1 | Astaria | Ethereum | AstariaRouter (proxy) | `0x42CDc5D4B05E8dACc2FCD181cbe0Cc86Ee14c439` | 41 | 5/36 | 8 | 40 | https://audits.sherlock.xyz/contests/8 |
| 2 | Tapioca DAO | Arbitrum | YieldBox | `0xCFFd997DB053c0fC54010770b55A4E02B1D104a5` | 37 | 0/37 | 15 | 37 | https://audits.sherlock.xyz/contests/170 |
| 3 | Vader Protocol contest | Ethereum | VADER token | `0x2602278EE1882889B946eb11DC0E810075650983` | 37 | 0/37 | 8 | 37 | https://github.com/code-423n4/2021-04-vader-findings/blob/ec1d5487a15c77ca269a2b |
| 4 | Peapods | Ethereum | IndexManagerV3 | `0x6eFFcF94993d6a6081204fc3C30473468Eb7666E` | 21 | 10/11 | 5 | 20 | https://audits.sherlock.xyz/contests/749 |
| 5 | Blueberry | Ethereum | BlueberryBank (proxy) | `0x9b06eA9Fbc912845DF1302FE1641BEF9639009F7` | 19 | 1/18 | 3 | 18 | https://audits.sherlock.xyz/contests/104 |
| 6 | Notional | Ethereum | Notional Proxy (Ethereum) | `0x6e7058c91f85e0f6db4fc9da2ca41241f5e4263f` | 19 | 1/18 | 2 | 19 | https://audits.sherlock.xyz/contests/119 |
| 7 | Sushi Trident contest phase 1 | Polygon | TridentRouter (Polygon) | `0x7A250C60Cde7A5Ca7B667209beAB5eA4E16eed67` | 18 | 0/18 | 8 | 17 | https://github.com/code-423n4/2021-09-sushitrident-2-findings/blob/3154f6297988d |
| 8 | GMX Synthetics | Arbitrum | ExchangeRouter | `0x1C3fa76e6E1088bCE750f23a5BFcffa1efEF6A41` | 17 | 11/6 | 0 | 17 | https://github.com/Dedaub/audits/blob/431ec937802fd7118f9c6d533a530aaaf33a2c3a/G |
| 9 | Usual Money | Ethereum | DaoCollateral | `0xde6e1F680C4816446C8D515989E2358636A38b04` | 16 | 0/16 | 5 | 15 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 10 | Rubicon v2 | Optimism | RubiconMarket (Optimism) | `0x7a512d3609211e719737E82c7bb7271eC05Da70d` | 14 | 0/14 | 2 | 14 | https://github.com/code-423n4/2022-05-rubicon-findings/blob/89ab16511eb6864d5c54 |
| 11 | 2023-07-tapioca | Arbitrum | YieldBox | `0xCFFd997DB053c0fC54010770b55A4E02B1D104a5` | 12 | 0/12 | 7 | 12 |  |
| 12 | LSD Network - Stakehouse contest | Ethereum | StakeHouseUniverse | `0xC6306C52ea0405D3630249f202751aE3043056bd` | 11 | 0/11 | 4 | 11 | https://github.com/code-423n4/2022-11-stakehouse-findings/blob/e909ae1917e82734c |
| 13 | Kryptonite Protocol CosmWasm Smart Contract | Sei | Kryptonite market hub (DefiLlama TVL anc | `sei1swe2fy3t49j2c2xl8l64ldjaqyr6khmaya60pl5kr4em2v2jp0ysa3xjum` | 10 | 8/2 | 6 | 10 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 14 | PariFi | Arbitrum | OrderManager | `0x9Ce25A972e0b55cd33de54a670F48a39820ea704` | 10 | 5/5 | 3 | 10 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 15 | Perennial | Arbitrum | Controller (V2) | `0x197dE1B26ad733380fD22159A2671f497A6DDd7C` | 10 | 1/9 | 2 | 8 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 16 | 2022-07-fractional | Ethereum | VaultFactory (v2) | `0x19DD838E5407f7022C50A1717D5e052552e8E807` | 10 | 0/10 | 5 | 10 |  |
| 17 | 2022-11-10-final-astaria-audit-report | Ethereum | AstariaRouter | `0x51f9EEB8fC19Aba1798097a82A2E0B64e237fDE3` | 10 | 0/10 | 3 | 10 |  |
| 18 | Hashlock Pty Ltd | Ethereum | EigenLayer DelegationManager proxy | `0x39053D51B77DC0d36036Fc1fCc8Cb819df8Ef37A` | 10 | 0/10 | 1 | 9 |  |
| 19 | Maia DAO Ecosystem | Arbitrum | ArbitrumBranchPort (Ulysses) | `0x79f4b04FFCa54BC946aa0ef8E33eE723467f0192` | 10 | 0/10 | 4 | 10 | https://github.com/code-423n4/2023-05-maia-findings/blob/fa2bd134824cd6bfcbc99ee |
| 20 | Oro Inti | Solana | Gold (GOLD) mint | `GoLDppdjB1vDTPSGxyMJFqdnj134yH6Prg9eqsGDiw6A` | 9 | 9/0 | 6 | 9 | https://cdn.cantina.xyz/reports/cantina_oro_february2025.pdf |
| 21 | Starlay Protocol Wasm | Astar | LendingPool proxy (EVM deployment, for c | `0x90384334333f3356eFDD5b20016350843b90f182` | 9 | 8/1 | 1 | 8 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 22 | Poolshark Limit | Arbitrum | LimitPoolFactory (Arbitrum) | `0x8bb5db1625adb4ae4beb94a188d33062303f8fb7` | 9 | 7/2 | 1 | 9 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 23 | 2022-11-stakehouse | Ethereum | Stakehouse (BSN) token | `0x534D1F5E617e0f72A6b06a04Aa599839AF776A5e` | 9 | 0/9 | 4 | 9 |  |
| 24 | Smardex - USDN | Ethereum | UsdnProtocolFallback | `0xd4e615ab327324E9f2bB492C42d47EE8213959c0` | 9 | 0/9 | 1 | 7 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 25 | Teller | Base | LenderCommitmentGroupFactory (Base) | `0x48EA70BCe76FE2F0c79B29Bf852a1DCF957982aa` | 9 | 0/9 | 5 | 9 | https://audits.sherlock.xyz/contests/295 |
| 26 | GMX Crosschain V2.2 1 | Arbitrum | MultichainOrderRouter | `0xD38111f8aF1A7Cd809457C8A2303e15aE2170724` | 8 | 4/4 | 2 | 8 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 27 | SentimentV2 | Arbitrum | PositionManager | `0xc0ac97A0eA320Aa1E32e9DEd16fb580Ef3C078Da` | 8 | 4/4 | 2 | 8 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 28 | Tracer DAO Tracer Protocol | Ethereum | TCR token (Tracer DAO) | `0x9C4A4204B79dd291D6b6571C5BE8BbcD0622F050` | 8 | 4/4 | 0 | 7 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 29 | Symbiotic RelayContracts AI | Ethereum | Symbiotic core Network factory (not Rela | `0x1BC8FCFbE6Aa17e4A7610F51B888f34583D202Ec` | 8 | 2/6 | 2 | 3 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 30 | gamma | Ethereum | UniProxy | `0xfb203298a28c7bb92486C9D92af07F34Eb95B823` | 8 | 2/6 | 3 | 8 | https://diligence.consensys.io/audits/2022/02/gamma/gamma-audit-2022-02.pdf |
| 31 | DYAD | Ethereum | VaultManagerV2 | `0x13421d816572f61048b2C855de88807aec58494b` | 8 | 1/7 | 0 | 8 | https://github.com/code-423n4/2024-04-dyad-findings/blob/8769dbdd7b34d16fd726272 |
| 32 | wake-arena-ai--ipor-labs-fusion-dec-11 | Ethereum | IporFusionFactoryProxy | `0xcd05909C4A1F8E501e4ED554cEF4Ed5E48D9b852` | 8 | 1/7 | 0 | 8 | https://github.com/Ackee-Blockchain/public-wake-arena-reports/blob/e6553332fd1e5 |
| 33 | Fractional v2 contest | Ethereum | VaultFactoryV2 | `0x20249eA37549E9D42d0017a218F05c8c109207e1` | 8 | 0/8 | 4 | 8 | https://github.com/code-423n4/2022-07-fractional-findings/blob/c4ff1e8a730d2904e |
| 34 | Illuminate | Ethereum | MarketPlace | `0xcd1D02fDa51CD24123e857CE94e4356D5C073b3f` | 8 | 0/8 | 3 | 8 | https://audits.sherlock.xyz/contests/12 |
| 35 | Timeswap contest | Polygon | Timeswap V2 pair factory (Polygon) | `0xcf0aca5c5b7e1bF63514D362243b6c50d5761FE8` | 8 | 0/8 | 2 | 8 | https://github.com/code-423n4/2022-01-timeswap-findings/blob/9536aab92308fa8ba35 |
| 36 | USSD - Autonomous Secure Dollar | Ethereum | USSDRebalancer | `0x95AA436B975737E3eaa5e7D48251F2c1a602FfBc` | 8 | 0/8 | 1 | 6 | https://audits.sherlock.xyz/contests/82 |
| 37 | Gains Network | Arbitrum | GNSMultiCollatDiamond | `0xFF162c694eAA571f685030649814282eA457f169` | 7 | 5/2 | 4 | 7 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 38 | 2024-04-gondi | Ethereum | MultiSourceLoan (V2) | `0x478f6F994C6fb3cf3e444a489b3AD9edB8cCaE16` | 7 | 1/6 | 0 | 6 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 39 | Frankencoin | Ethereum | MintingHub V1 | `0x7546762fdb1a6d9146b33960545c3f6394265219` | 7 | 1/6 | 3 | 7 | https://github.com/Frankencoin-ZCHF/Frankencoin/blob/8b4c4ab67bb361b91d58c474b87 |
| 40 | PoolTogether | Optimism | PrizePool (V5) | `0xF35fE10ffd0a9672d0095c435fd8767A7fe29B55` | 7 | 1/6 | 2 | 7 | https://0xmacro.com/library/audits/pooltogether-1 |
| 41 | 2021-12-vader | Ethereum | VADER token | `0x2602278EE1882889B946eb11DC0E810075650983` | 7 | 0/7 | 2 | 6 |  |
| 42 | 2024-02-12-opal-contracts | Ethereum | OmnipoolController | `0x2E291bb636B8434dCC5b32b5A0910ad4E0423d52` | 7 | 0/7 | 0 | 7 |  |
| 43 | Ajna | Ethereum | ERC20PoolFactory | `0x6146DD43C5622bB6D12A5240ab9CF4de14eDC625` | 7 | 0/7 | 2 | 7 | https://audits.sherlock.xyz/contests/32 |
| 44 | Beanstalk (The Finale) | Arbitrum | Beanstalk L2 Diamond | `0xD1A0060ba708BC4BCD3DA6C37EFa8deDF015FB70` | 7 | 0/7 | 1 | 6 |  |
| 45 | Cantina competition bundle (Opal Protocol / Olas) | Ethereum | Opal Omnipool wstETH (proxy) | `0x86b130298719F753808E96cA6540b684a2d21466` | 7 | 0/7 | 1 | 6 |  |
| 46 | ELFi Protocol (2024-06-20 final audit) | Arbitrum | ELFi Diamond (Exchange) | `0x153c613D572c050104086c7113d00B76Fbaa5d55` | 7 | 0/7 | 1 | 7 |  |
| 47 | Elfi | Arbitrum | ELFi Diamond | `0x153c613D572c050104086c7113d00B76Fbaa5d55` | 7 | 0/7 | 0 | 7 | https://audits.sherlock.xyz/contests/329 |
| 48 | FairSide | Ethereum | FairSide Treasury (GnosisSafeProxy) | `0x86b50A011C25667Cb366aAbf6e0f940ee70dB894` | 7 | 0/7 | 2 | 6 | https://github.com/code-423n4/2021-05-fairside-findings/blob/3d4efd92a50f9689ed9 |
| 49 | Notional Exponent | Ethereum | AddressRegistry (proxy) | `0xe335d314BD4eF7DD44F103dC124FEFb7Ce63eC95` | 7 | 0/7 | 4 | 7 | https://audits.sherlock.xyz/contests/1001 |
| 50 | Olympus | Ethereum | BLVaultLido | `0x7fdD4e808ee9608f1b2f05157A2A8098e3D432cD` | 7 | 0/7 | 0 | 6 | https://audits.sherlock.xyz/contests/128 |
| 51 | Perennial V2 Update #4 | Arbitrum | Market (Controller) | `0x197dE1B26ad733380fD22159A2671f497A6DDd7C` | 7 | 0/7 | 3 | 6 | https://audits.sherlock.xyz/contests/518 |
| 52 | Singularity | Fantom | SingularityPool (USDC pool, representati | `0x5916A8D97Ea1687bF37c5dAE4e8ce657950A46F5` | 7 | 0/7 | 4 | 7 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 53 | Union Finance | Ethereum | UserManager | `0x49c910Ba694789B58F53BFF80633f90B8631c195` | 7 | 0/7 | 2 | 7 | https://audits.sherlock.xyz/contests/11 |
| 54 | MYX Finance | BNB Chain | MYX Vault (BSC) | `0x22cEc08111BBae24D0b80BDA2a6503EaB9BA704b` | 6 | 5/1 | 0 | 4 | https://1570067552-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 55 | Synthetix BFP Market | Ethereum | Synthetix V3 Core Proxy | `0xefaca6fc316b3b2aa6c55ff5e02a62a85d4391e8` | 6 | 4/2 | 3 | 6 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 56 | privacy-pools-v1 | Ethereum | PrivacyPool | `0xf241d57c6debae225c0f2e6ea1529373c9a9c9fb` | 6 | 4/2 | 1 | 6 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 57 | Connext | Ethereum | ConnextDiamond | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 6 | 3/3 | 1 | 6 | https://0xmacro.com/library/audits/connext-1 |
| 58 | Etherspot Credible Account Module | Ethereum | CredibleAccountModule | `0x566f9d697FF95D13643A35B3F11BB4812B2aaF15` | 6 | 3/3 | 1 | 4 | https://github.com/shieldify-security/audits-portfolio-md/blob/f2c051af4ffb67e11 |
| 59 | Hyperdrive June 2023 | Ethereum | HyperdriveRegistry (Ethereum) | `0xbe082293b646cb619a638d29e8eff7cf2f46aa3a` | 6 | 3/3 | 3 | 6 | https://cdn.cantina.xyz/reports/Delv-Spearbit-Security-Review-June-2023.pdf |
| 60 | Synthetix Perps V3 | Ethereum | Synthetix V3 Core Proxy | `0xefaca6fc316b3b2aa6c55ff5e02a62a85d4391e8` | 6 | 3/3 | 1 | 6 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 61 | Synnax | Sei | Synnax syUSD (vault/PSM contracts unreso | `0x059a6b0ba116c63191182a0956cf697d0d2213ec` | 6 | 2/4 | 1 | 6 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 62 | Burve | Berachain | SimplexDiamond | `0xa1beD164c12CD9479A1049f97BDe5b3D6EC21089` | 6 | 1/5 | 1 | 6 | https://audits.sherlock.xyz/contests/858 |
| 63 | Impermax V3 | Ethereum | Router (Ethereum) | `0x5e169082fff23cee6766062b96051a78c543127d` | 6 | 1/5 | 2 | 5 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 64 | Y2K Finance | Arbitrum | Y2K Earthquake vault | `0x65c936f008BC34fE819bce9Fa5afD9dc2d49977f` | 6 | 1/5 | 1 | 6 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 65 | 2022-12-backed | Ethereum | PaprController | `0x3b29c19ff2fcEa0Ff98D0ef5B184354D74eA74b0` | 6 | 0/6 | 3 | 6 |  |
| 66 | AI Arena | Arbitrum | FighterFarm | `0x6371F51bD82d5E0EB2a01b942157cB45Ab2D8EBE` | 6 | 0/6 | 0 | 6 | https://github.com/code-423n4/2024-02-ai-arena-findings/blob/715044438de5859916c |
| 67 | Biconomy - Smart Contract Wallet contest | Ethereum | SmartAccountFactory | `0x000000a56Aaca3e9a4C479ea6b6CD0DbcB6634F5` | 6 | 0/6 | 3 | 6 | https://github.com/code-423n4/2023-01-biconomy-findings/blob/7461cb5d4e557a6f38e |
| 68 | Clearpool | Ethereum | Auction | `0x5f04bC575a407DBa3129EA45180b1e6573a4F91A` | 6 | 0/6 | 0 | 4 | https://cdn.cantina.xyz/reports/cantina_clearpool_aug2025.pdf |
| 69 | DODO (DODO V3 / D3) | Ethereum | D3Vault | `0x49186E32fEd50fd6B5604A2618c7B0b03Cd41414` | 6 | 0/6 | 3 | 6 | https://audits.sherlock.xyz/contests/78 |
| 70 | Illuminate | Ethereum | Lender | `0x429B47C4AEADD42BBcB118651C8984086Bfc4551` | 6 | 0/6 | 6 | 6 | https://audits.sherlock.xyz/contests/12 |
| 71 | ParaSpace contest | Ethereum | Pool (ParaProxy) | `0x638a98BBB92a7582d07C52ff407D49664DC8b3ee` | 6 | 0/6 | 4 | 5 | https://github.com/code-423n4/2022-11-paraspace-findings/blob/9650d134645b411491 |
| 72 | RocketPool - Saturn | Ethereum | RocketStorage (Saturn modules resolved t | `0x1d8f8f00cfa6758d7bE78336684788Fb0ee0Fa46` | 6 | 0/6 | 3 | 6 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 73 | Symmetrical | Base | Symmio diamond (LiquidationFacet) | `0x91Cf2D8Ed503EC52768999aA6D8DBeA6e52dbe43` | 6 | 0/6 | 0 | 4 | https://audits.sherlock.xyz/contests/108 |
| 74 | ZeroLend One | Linea | ZeroLend Pool proxy (Linea) | `0x2f9bB73a8e98793e26Cb2F6C4ad037BDf1C6B269` | 6 | 0/6 | 2 | 6 | https://audits.sherlock.xyz/contests/466 |
| 75 | GMX Crosschain V2.2 1 | Arbitrum | LayerZeroProvider | `0xB6DE222dAef5029f31b8fABE498D34f3c491Ef85` | 5 | 5/0 | 3 | 4 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 76 | NX Finance | Solana | NX token mint (lead, not the program) | `BAsnXPVYuvZDfEFR7tmu9sG9gPyHy58Jpjs2AuUw1FLx` | 5 | 5/0 | 2 | 5 | https://1014032567-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 77 | Fuji-1 | Arbitrum | Fuji V2 Controller (Arbitrum) | `0xA9c29eA1a067740be6dB1F98FcbA0043C475041A` | 5 | 4/1 | 4 | 5 | https://0xmacro.com/library/audits/fuji-1 |
| 78 | Zero Knowledge | Arbitrum | DarkpoolAssetManager (Singularity darkpo | `0xf7C40b5057a1D1a3d58B02BCdb125E63ef380564` | 5 | 4/1 | 2 | 4 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 79 | Aave Protocol (v1) | Ethereum | LendingPool | `0x398eC7346DcD622eDc5ae82352F02bE94C62d119` | 5 | 3/2 | 2 | 5 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 80 | Bunni | Ethereum | BunniHub (v2) | `0x000000000049C7bcBCa294E63567b4D21EB765f1` | 5 | 3/2 | 0 | 4 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 81 | DIA Lumina Staking | Ethereum | DIA token | `0x84cA8bc7997272c7CfB4D0Cd3D55cd942B3c9419` | 5 | 3/2 | 3 | 5 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 82 | Fei Protocol | Ethereum | Core | `0x8d5ED43dCa8C2F7dFB20CF7b53CC7E593635d7b9` | 5 | 3/2 | 2 | 5 | https://www.openzeppelin.com/news/fei-audit-2 |
| 83 | Vertex Protocol | Arbitrum | Vertex core deployment (Arbitrum) | `0x95146881b86b3ee99e63705ec87afe29fcc044d9` | 5 | 3/2 | 1 | 5 | https://osec.io/reports/fa17b76e-e88b-4ab1-b5ce-107e287b254a |
| 84 | Avantis (now Veranta) | Base | Trading (proxy) | `0x5FF292d70bA9cD9e7CCb313782811b3D7120535f` | 5 | 2/3 | 1 | 4 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 85 | Kresko Labs Pte. Ltd - July 14, 2023 | Arbitrum | Kresko Diamond | `0x0000000000177abD99485DCaea3eFaa91db3fe72` | 5 | 2/3 | 3 | 5 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 86 | Lodestar Finance Staking Smart Contract Security | Arbitrum | Lodestar Unitroller (lending core) | `0x92a62f8c4750D7FbDf9ee1dB268D18169235117B` | 5 | 2/3 | 0 | 5 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 87 | Escher | Babylon Genesis | liquidstaking | `bbn1m7zr5jw4k9z22r9ajggf4ucalwy7uxvu9gkw6tnsmv42lvjpkwasagek5g` | 5 | 1/4 | 2 | 4 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 88 | Rocketpool | Ethereum | RocketStorage-resolved module | `0x1d8f8f00cfa6758d7bE78336684788Fb0ee0Fa46` | 5 | 1/4 | 2 | 5 | https://cdn.cantina.xyz/reports/cantina_rocketpool_jun2025.pdf |
| 89 | 2024-12-bakerfi-invitational | Base | BakerFiProxy vault | `0x37327c99bBc522e677a97d01021dB20227faF60A` | 5 | 0/5 | 3 | 4 | https://github.com/code-423n4/2024-05-bakerfi-findings/blob/30e7003f6fc084da282f |
| 90 | Audit - Stryke / MarginZero - CLAMM Options | Arbitrum | DopexV2OptionMarket | `0x77b6f45a3Dcf0493f1B9Ac9874e5982AB526AA9e` | 5 | 0/5 | 0 | 5 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 91 | Behodler contest | Ethereum | Behodler EYE token | `0x155ff1A85F440EE0A382eA949f24CE4E0b751c65` | 5 | 0/5 | 2 | 5 | https://github.com/code-423n4/2022-01-behodler-findings/blob/83b8af96a00264e6fb8 |
| 92 | Bitcoin-EVM | Polygon | BitcoinRelay | `0x7DeB66341b1d499D7e699589d0cf665De4132EA3` | 5 | 0/5 | 1 | 5 | https://github.com/TeleportDAO/audits/blob/0035adcd81afb023c52d605845030e3177b83 |
| 93 | DODO Cross-Chain DEX | ZetaChain | GatewayTransferNative | `0x52913eD5DB9c61Ea7c088a2D417160bC70d7DD37` | 5 | 0/5 | 3 | 5 | https://audits.sherlock.xyz/contests/991 |
| 94 | INIT Capital Invitational | Mantle | PosManager (Mantle) | `0x0e7401707CD08c03CDb53DAEF3295DDFb68BBa92` | 5 | 0/5 | 1 | 5 | https://github.com/code-423n4/2024-01-init-capital-invitational-findings/blob/6a |
| 95 | PoolTogether | Optimism | PrizeVault (V5) | `0xa52e38a9147f5eA9E0c5547376c21c9E3F3e5e1f` | 5 | 0/5 | 3 | 4 | https://github.com/code-423n4/2023-07-pooltogether-findings/blob/ec193297735caa6 |
| 96 | Primev | mev-commit chain | BidderRegistry | `0xC973D09e51A20C9Ab0214c439e4B34Dbac52AD67` | 5 | 0/5 | 5 | 5 | https://cdn.cantina.xyz/reports/cantina_competition_primev_may2025.pdf |
| 97 | Sentiment | Arbitrum | Controller (v1 proxy) | `0x17b07cfbab33c0024040e7c299f8048f4a49679b` | 5 | 0/5 | 0 | 5 | https://audits.sherlock.xyz/contests/1 |
| 98 | TermMax | Ethereum | TermMaxRouter | `0xC47591F5c023e44931c78D5A993834875b79FB11` | 5 | 0/5 | 0 | 5 | https://cdn.cantina.xyz/reports/cantina_competition_term_max_december2024.pdf |
| 99 | Tokemak | Ethereum | LMPVault | `0xa43a16d818fea4ad0fb9356d33904251d726079b` | 5 | 0/5 | 1 | 4 | https://audits.sherlock.xyz/contests/101 |
| 100 | UXD | Solana | UXD program (Solana) | `UXPhBoR3qG4UCiGNJfV7MqhHyFqKN68g45GoYvAeL2M` | 5 | 0/5 | 3 | 5 | https://audits.sherlock.xyz/contests/33 |
| 101 | prePO contest | Arbitrum | prePO market factory (Arbitrum) | `0x6f889e3fce9b13fe8cefa068a48f4074292e663c` | 5 | 0/5 | 0 | 5 | https://github.com/code-423n4/2022-03-prepo-findings/blob/ddd9e13af212bced9c5b41 |
| 102 | Larix Obsolete | Solana | Larix main program | `7Zb1bGi32pfsrBkzWdqd4dFhUXwp5Nybr1zuaEwN34hy` | 4 | 4/0 | 2 | 4 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 103 | Polemos - Lending | Ethereum | Polemos PLMS token | `0x68614481AeF06e53D23bbe0772343fB555ac40c8` | 4 | 4/0 | 1 | 4 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 104 | Polygon zkEVM | Ethereum | AgglayerManager (PolygonZkEVMDiamond pro | `0x5132A183E9F3CB7C848b0AAC5Ae0c4f0491B7aB2` | 4 | 4/0 | 1 | 4 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 105 | Torch DEX | TON | Torch Factory (DEX v2) | `EQDQIhFLSzUlaHKM9L2ZQS-o0iNHTbOSBtzNC0VLxPbNFH6E` | 4 | 4/0 | 2 | 4 | https://2186085260-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 106 | Augur Core v2 | Ethereum | Augur core | `0x23916a8F5C3846e3100e5f587FF14F3098722F5d` | 4 | 3/1 | 2 | 3 | https://www.openzeppelin.com/news/augur-core-v2-audit |
| 107 | Royco | Ethereum | RecipeMarketHub | `0x783251f103555068c1E9D755f69458f39eD937c0` | 4 | 3/1 | 2 | 4 | https://cdn.cantina.xyz/reports/cantina_royco_august2024.pdf |
| 108 | Saffron | Ethereum | SFI token | `0xb753428af26e81097e7fd17f40c88aaa3e04902c` | 4 | 3/1 | 2 | 4 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 109 | 02 12 Whetstone Doppler-MR | Ethereum | Airlock | `0xde3599a2ec440b296373a983c85c365da55d9dfa` | 4 | 2/2 | 1 | 2 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 110 | 2024-04-29-sigmaprime-tracer-tracer-review | Ethereum | TracerDAO | `0x515f2815c950C8385C1C3c30B63AdF3207Aa259a` | 4 | 2/2 | 1 | 4 |  |
| 111 | Harmonix Finance | Hyperliquid L1 | FundContract | `0xFde5B0626fC80E36885e2fA9cD5ad9d7768D725c` | 4 | 2/2 | 1 | 4 | https://github.com/shieldify-security/audits-portfolio-md/blob/f2c051af4ffb67e11 |
| 112 | KittenSwap | Hyperliquid L1 | Voter | `0xb7F7053F7e6c210e6777D5BA758E4b3ECa6C88A0` | 4 | 2/2 | 0 | 4 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 113 | RaisinLabs | BNB Smart Chain | PoodlToken | `0x4a68c250486a116dc8d6a0c5b0677de07cc09c5d` | 4 | 2/2 | 1 | 4 | https://github.com/GuardianAudits/DefenderAudits/blob/b2a2ccb9b6e07d82a6c4497fee |
| 114 | SendIt Contracts | Solana | SendIt lending program | `SenditXmUCHPeV6iyFoMY8dRNB4PofGKTfp52hEWpJx` | 4 | 2/2 | 1 | 4 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 115 | ZetaChain | ZetaChain | GatewayZEVM (ZetaChain gateway) | `0xb2385d4924dce8Bf06487949924e7Da8b286Aeed` | 4 | 2/2 | 0 | 4 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 116 | Ondo: GM Solana | Solana | Ondo GM program | `XzTT4XB8m7sLD2xi6snefSasaswsKCxx5Tifjondogm` | 4 | 1/3 | 1 | 4 | https://cdn.cantina.xyz/reports/cantina_ondo_nov2025.pdf |
| 117 | OpalProtocol | Ethereum | Omnipool (wstETH pool) | `0x86b130298719F753808E96cA6540b684a2d21466` | 4 | 1/3 | 1 | 4 | https://cdn.cantina.xyz/reports/cantina_competition_opal_feb2024.pdf |
| 118 | Ostium | Arbitrum | OstiumTrading | `0x6D0bA1f9996DBD8885827e1b2e8f6593e7702411` | 4 | 1/3 | 1 | 4 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 119 | Sommelier-3 | Ethereum | Cellar | `0x97e6e0a40a3d02f12d1cec30ebfbae04e37c119e` | 4 | 1/3 | 1 | 4 | https://0xmacro.com/library/audits/sommelier-14 |
| 120 | YIELD | Ethereum | Cauldron (Ethereum) | `0xc88191F8cb8e6D4a668B047c1C8503432c3Ca867` | 4 | 1/3 | 0 | 4 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 121 | 178 Wardens contributed reports to the Popcorn | Ethereum | VaultCraft Vault Registry (Ethereum) | `0x007318Dc89B314b47609C684260CfbfbcD412864` | 4 | 0/4 | 3 | 4 | https://github.com/code-423n4/2023-01-popcorn-findings/blob/1046b31e99006e4f462a |
| 122 | 2023-01-popcorn | Ethereum | VaultCraft Vault Registry (Ethereum) | `0x007318Dc89B314b47609C684260CfbfbcD412864` | 4 | 0/4 | 1 | 4 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 123 | 2024-04-renzo | Ethereum | RestakeManager | `0x74a09653A083691711cF8215a6ab074BB4e99ef5` | 4 | 0/4 | 0 | 4 | https://github.com/code-423n4/2024-04-renzo-findings/blob/b4206cef724c8b518073b8 |
| 124 | 2025-07-04-taofi | Bittensor EVM | ProxyAdmin (Subtensor/Bittensor EVM) | `0xA3c92e5cbb6146384Aa5A41540EC3fc6a184139C` | 4 | 0/4 | 3 | 4 | https://cdn.cantina.xyz/reports/cantina_taofi_sturdy_july2025.pdf |
| 125 | Biconomy Nexus | Ethereum | ModuleManager (Nexus implementation) | `0x000000004F43C49e93C970E84001853a70923B03` | 4 | 0/4 | 0 | 4 | https://cdn.cantina.xyz/reports/Biconomy-Spearbit-Security-Review-October-2024.p |
| 126 | Cork | Ethereum | CorkPoolManager | `0xCCd90F6435dd78C4ECCED1FA4db0D7242548a2a9` | 4 | 0/4 | 0 | 4 | https://cdn.cantina.xyz/reports/cantina_competition_cork_december2024.pdf |
| 127 | Cork Protocol (Best Efforts contest, v1) | Ethereum | ModuleCore (Vault) | `0xCCd90F6435dd78C4ECCED1FA4db0D7242548a2a9` | 4 | 0/4 | 1 | 4 | https://audits.sherlock.xyz/contests/506 |
| 128 | Hook | Ethereum | HookCoveredCallImplV1 | `0x3648080307faC2EE51A01463e47B9ca076DC14A1` | 4 | 0/4 | 1 | 4 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 129 | Mochi contest | Ethereum | MochiEngine | `0x860E47e6D6f4a6bCAADDFC7f17F772d2ab55bE2f` | 4 | 0/4 | 2 | 4 | https://github.com/code-423n4/2021-10-mochi-findings/blob/983d120f3b29eb0fc554e3 |
| 130 | OlympusDAO | Ethereum | SingleSidedLiquidityVault (wstETH BLV im | `0x7fdD4e808ee9608f1b2f05157A2A8098e3D432cD` | 4 | 0/4 | 3 | 4 | https://audits.sherlock.xyz/contests/50 |
| 131 | Panoptic | Ethereum | SemiFungiblePositionManager (SFPM) | `0x0000000000000DEdEDdD16227aA3D836C5753194` | 4 | 0/4 | 3 | 4 | https://github.com/code-423n4/2024-04-panoptic-findings/blob/d9124b2677670e586c8 |
| 132 | Plaza Finance | Base | bondETH token | `0x091A5Abe6616e26268e5eEcFF256c2212fcE2707` | 4 | 0/4 | 1 | 4 | https://audits.sherlock.xyz/contests/682 |
| 133 | Predy | Arbitrum | PredyPool.reallocate | `0x9215748657319b17fecb2b5d086a3147bfbc8613` | 4 | 0/4 | 0 | 4 | https://github.com/code-423n4/2024-05-predy-findings/blob/766659221c5d4b5f547710 |
| 134 | Quip | Base | Omnibus | `0xA7955981D5759a799267063110Be0F7AeCc26F8A` | 4 | 0/4 | 2 | 4 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 135 | reNFT | Ethereum | Create policy | `0x37B45F0810a0A0fc70B08Eed205cc07E57bD6452` | 4 | 0/4 | 3 | 4 | https://github.com/code-423n4/2024-01-renft-findings/blob/273c1d163a81a8b5cd09c0 |
| 136 | 08--Bunni | Ethereum | BunniHub | `0x000000c396558ffbab5ea628f39658bdf61345b3` | 3 | 3/0 | 3 | 3 | https://github.com/yAudit/reports-pdf/blob/186eab01a540d4815784bf79356dc7bcf4422 |
| 137 | 2023-11-30-eesee-sca-eesee-erc20-nov2023-sca-eesee | Ethereum | ESEE token | `0x908dDb096BFb3AcB19e2280aAD858186ea4935C4` | 3 | 3/0 | 2 | 3 |  |
| 138 | Bunni | Ethereum | BunniHub (v1) | `0xb5087F95643A9a4069471A28d32C569D9bd57fE4` | 3 | 3/0 | 3 | 3 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 139 | Degis SCProtection | Avalanche | WeightedFarmingPool | `0x071570A88992964E93E7C980FCe8E76dFcF8144A` | 3 | 3/0 | 2 | 3 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 140 | Desyn Phase3 | BNB Chain | DSN token | `0xcAd9074fe57c3DF5e7FAFf603d16e791CFCF54F2` | 3 | 3/0 | 1 | 3 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 141 | Forta Delegated Staking | Polygon | FortaStaking | `0xd2863157539b1D11F39ce23fC4834B62082F6874` | 3 | 3/0 | 1 | 3 | https://diligence.security/audits/2022/11/forta-delegated-staking/ |
| 142 | GMX Synthetics | Arbitrum | OrderHandler | `0x63492B775e30a9E6b4b4761c12605EB9d071d5e9` | 3 | 3/0 | 2 | 3 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 143 | Lido V3 | Ethereum | VaultHub | `0x1d201BE093d847f6446530Efb0E8Fb426d176709` | 3 | 3/0 | 2 | 3 | https://diligence.security/audits/2025/08/lido-v3/ |
| 144 | Linea zkEVM (crypto-beta-v1) | Ethereum | LineaRollup (zkEVM verifier) | `0xd19d4B5d358258f05D7B411E21A1460D11B0876F` | 3 | 3/0 | 0 | 3 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 145 | Opal Finance Protocol Smart Contract Security | Ethereum | GEM token | `0x0447D3454b25935eeD47F65b4Bd22b9b23bE326a` | 3 | 3/0 | 2 | 3 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 146 | Primitive | Ethereum | Option (clone) | `0x5B83dEc645BE2B8137a20175f59000c20C6dce82` | 3 | 3/0 | 1 | 3 | https://www.openzeppelin.com/news/primitive-audit |
| 147 | SingularityAudit | Arbitrum | DarkpoolAssetManager | `0xf7C40b5057a1D1a3d58B02BCdb125E63ef380564` | 3 | 3/0 | 3 | 3 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 148 | Zero Knowledge | Arbitrum | DarkpoolAssetManager | `0xf7C40b5057a1D1a3d58B02BCdb125E63ef380564` | 3 | 3/0 | 3 | 3 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 149 | Zunami Protocol v2 | Ethereum | Zunami Omnipool zunUSD | `0x8C0D76C9B18779665475F3E212D9Ca1Ed6A1A0e6` | 3 | 3/0 | 1 | 3 | https://github.com/oxor-io/public_audits/blob/06624b6efe70d98702baccef5208ec57db |
| 150 | yAcademy bunni | Ethereum | BunniHub | `0x000000c396558ffbab5ea628f39658bdf61345b3` | 3 | 3/0 | 3 | 3 | https://github.com/yAudit/fellowship-audits/blob/2ddaff163a55d9d436c07e86adf18f9 |
| 151 | Alula Finance | Stellar | Market | `CBP76I2FRMUKYKIYYBKN3DH7TSWMFAJF2WTDC7Q2OHQFBIVWP7CAAI5Q` | 3 | 2/1 | 1 | 3 | https://www.halborn.com/audits/alula-finance/smart-contracts-cd8f6d |
| 152 | Chainflip | Ethereum | StateChainGateway / Vault | `0x6995Ab7c4D7F4B03f467Cf4c8E920427d9621DBd` | 3 | 2/1 | 0 | 3 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 153 | DEDAUB.COM Aori | Ethereum | AoriSeats | `0x0198Ce118C7d8d9FC29Cc13864E7403359375DCC` | 3 | 2/1 | 1 | 3 | https://github.com/Dedaub/audits/blob/431ec937802fd7118f9c6d533a530aaaf33a2c3a/A |
| 154 | Eco Routes | Ethereum | IntentChainer V4 | `0x96f7DBa7E587f359a8f585C335fe510E4dC9bCC0` | 3 | 2/1 | 0 | 3 | https://cdn.cantina.xyz/reports/cantina_eco_december2024.pdf |
| 155 | Escher | Babylon Genesis | eBABY staking hub (CosmWasm) | `bbn1m7zr5jw4k9z22r9ajggf4ucalwy7uxvu9gkw6tnsmv42lvjpkwasagek5g` | 3 | 2/1 | 0 | 2 | https://github.com/code-423n4/2022-12-escher-findings/blob/bc2b36ff749ea93d70fab |
| 156 | FujiAudit | Ethereum | ConnextRouter (inherits BaseRouter) | `0x9907F34FbA2336C3Ce8758dd80c301BFf921dEc2` | 3 | 2/1 | 2 | 3 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 157 | Gearbox Gearbox v2.0 | Ethereum | CreditManager | `0xF7f0a609BfAb9a0A98786951ef10e5FE26cC1E38` | 3 | 2/1 | 0 | 2 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 158 | Kwenta-19 | Base | Smart Margin v3 Engine proxy | `0xe331a7eeC851Ba702aA8BF43070a178451d6D28E` | 3 | 2/1 | 1 | 3 | https://0xmacro.com/library/audits/kwenta-18 |
| 159 | Lucidly | Ethereum | syUSD BoringVault | `0x279CAD277447965AF3d24a78197aad1B02a2c589` | 3 | 2/1 | 1 | 3 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 160 | MORE Vaults | Base | MORE vault diamond (UniswapV2Facet / Cur | `0x7bDB8B17604b03125eFAED33cA0c55FBf856BB0C` | 3 | 2/1 | 2 | 3 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 161 | Navi Protocol | Sui | NAVI lending package (lending.move / sto | `0x512f28261c1a293f49416d8885b8d5d32bde6dd68a99a0be36fe42b248e6833a` | 3 | 2/1 | 2 | 3 | https://github.com/movebit/Sampled-Audit-Reports/blob/9f2027ef1500342dec1f1385db |
| 162 | Primitive | Ethereum | PrimitiveEngine (RMM01Portfolio) | `0xd3541aD19C9523c268eDe8792310867C57BE39e4` | 3 | 2/1 | 0 | 3 | https://cdn.cantina.xyz/reports/Primitive-Spearbit-Security-Review-July.pdf |
| 163 | RociFi Aug23 | Polygon | RociFi CollateralManager (proxy) | `0xd85af14C32Cc98Be9Fe5195eDb797773af8bB609` | 3 | 2/1 | 0 | 3 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 164 | Sapience-1 | Ethereal | PredictionMarketEscrow | `0xe7e515FC1DF93565A47770a4110f4366E26a2D3F` | 3 | 2/1 | 2 | 3 | https://0xmacro.com/library/audits/sapience-1 |
| 165 | Symmetry | Solana | Symmetry Engine program | `BASKT7aKd8n7ibpUbwLP3Wiyxyi3yoiXsxBk4Hpumate` | 3 | 2/1 | 0 | 3 | https://osec.io/reports/a4cf43a5-136e-419f-89a2-e4e20c723807 |
| 166 | Tigris trade Zokyo Aug8 | Arbitrum | Tigris Trading contract | `0x399214eE22bF068ff207adA462EC45046468B766` | 3 | 2/1 | 1 | 3 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 167 | Yearn veYFI(Voting and RewardPool | Ethereum | VotingYFI (veYFI) | `0x90c1f9220d90d3966FbeE24045EDd73E1d588aD5` | 3 | 2/1 | 0 | 3 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 168 | let's-get-hai-new-core-features | Optimism | SAFEEngine | `0x9Ff826860689483181C5FAc9628fd2F70275A700` | 3 | 2/1 | 1 | 3 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 169 | Aave V3 | Ethereum | Aave V3 Pool | `0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2` | 3 | 1/2 | 0 | 3 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 170 | America.Fun | Solana | America.Fun token mint | `2oQNkePakuPbHzrVVkQ875WHeewLHCd2cAwfwiLQbonk` | 3 | 1/2 | 1 | 3 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 171 | Connext NXTP — Noncustodial Xchain Transfer Protocol | Ethereum | TransactionManager | `0xe229084e0892f26a2Eec44349C36463F4b93E5c6` | 3 | 1/2 | 1 | 2 | https://diligence.security/audits/2021/07/connext-nxtp-noncustodial-xchain-trans |
| 172 | DeXe Network (DeXe DEX, Mar 2023) | Ethereum | DEXE token (Ethereum) | `0xde4EE8057785A7e8e800Db58F9784845A5C2Cbd6` | 3 | 1/2 | 0 | 2 |  |
| 173 | Defindex | Stellar | DeFindex vault (Blend strategy) | `CCA2ZJP5BVRXYTQH4FAGHCAUMRYCXVC4CRYC2NXHWMR7TIVX36U7F5HR` | 3 | 1/2 | 1 | 3 | https://osec.io/reports/20684d4e-4146-805d-af67-c3f9c1e68f61 |
| 174 | Lido on Polygon | Polygon | stMATIC (Staked MATIC PoS) | `0x3a58a54c066fdc0f2d55fc9c89f0415c92ebf3c4` | 3 | 1/2 | 0 | 3 | https://github.com/oxor-io/public_audits/blob/06624b6efe70d98702baccef5208ec57db |
| 175 | MUX Perps | Arbitrum | Mux3 diamond | `0x85c8F4a67F4f9AD7b38e875c8FeDE7F4c878bFAc` | 3 | 1/2 | 1 | 3 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 176 | Mantle | Ethereum | L1StandardBridgeProxy | `0x95fC37A27a2f68e3A647CDc081F0A89bb47c3012` | 3 | 1/2 | 0 | 3 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 177 | Nexus | Terra | Nexus vault core | `terra12897djskt9rge8dtmm86w654g7kzckkd698608` | 3 | 1/2 | 0 | 3 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 178 | Radiant Capital 06 March | Ethereum | RadiantOFT | `0x2124e9f48b94Eb3991255eA43CC4591d0e1F2467` | 3 | 1/2 | 2 | 3 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 179 | Sai | Ethereum | SaiTub | `0x448a5065aeBB8E423F0896E6c5D525C040f59af3` | 3 | 1/2 | 2 | 3 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 180 | SatoshiSwap | BNB Chain | SWAP token | `0xe0f7c8682f865b417aeb80bf237025b4cb5ebaef` | 3 | 1/2 | 1 | 3 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 181 | Splyce | Ethereum | SPLYCE token | `0x8895cd660C4EAB210DB032fbcc3895EcBE9a7e1C` | 3 | 1/2 | 1 | 3 | https://www.halborn.com/audits/splyce/concord-fixed-term-peer-to-peer-lending-pr |
| 182 | Synthetix | Ethereum | Synthetix V3 core deployment (CoreProxy) | `0xefaca6fc316b3b2aa6c55ff5e02a62a85d4391e8` | 3 | 1/2 | 0 | 3 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 183 | Tracer | Arbitrum | PoolFactory | `0x3Feafee6b12C8d2E58c5B118e54C09F9273c6124` | 3 | 1/2 | 2 | 3 | https://github.com/code-423n4/2021-06-tracer-findings/blob/dc33d6fbd9b235a60761c |
| 184 | Violet Protocol - July 05, 2022 | Ethereum | VioletID Registry | `0xfFcDa323597A90af8F7A0eCBE4ef14e9b30e4a9e` | 3 | 1/2 | 1 | 3 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 185 | axelar-interchain-token-service | Ethereum | InterchainTokenService | `0xB5FB4BE02232B1bBA4dC8f81dc24C26980dE9e3C` | 3 | 1/2 | 1 | 3 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 186 | govworld | BNB Smart Chain | GovWorld GOV token | `0xcc7a91413769891de2e9ebbfc96d2eb1874b5760` | 3 | 1/2 | 0 | 3 |  |
| 187 | .§. TRZNFinance | Ethereum | ZeUSD token | `0x7DC9748DA8E762e569F9269f48F69A1a9F8Ea761` | 3 | 0/3 | 0 | 3 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 188 | 2022-04-jpegd | Ethereum | JPEG'd core | `0xCE722f60F35C37aB295adc4E6bA45bCC7ca89Dd6` | 3 | 0/3 | 1 | 3 |  |
| 189 | 2023-01-biconomy | Ethereum | ERC-4337 EntryPoint v0.6 (shared singlet | `0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789` | 3 | 0/3 | 3 | 3 |  |
| 190 | 2023-04-caviar | Ethereum | Caviar pool factory | `0xa964d6e8d90e5cd12592a8ef2b1735dae9ba0840` | 3 | 0/3 | 0 | 3 | https://github.com/code-423n4/2022-12-caviar-findings/blob/f79ed90d48c01cc83e39a |
| 191 | 2023-09-asymmetry | Ethereum | afETH | `0x0000000016E6Cb3038203c1129c8B4aEE7af7a11` | 3 | 0/3 | 1 | 3 |  |
| 192 | 2024-01-salty | Ethereum | ExchangeConfig (core registry) | `0x66DB65306C2dDb7Aa9730e010033eE624ddD7f61` | 3 | 0/3 | 1 | 3 |  |
| 193 | 2024-07-dittoeth | Ethereum | DittoETH Diamond (ShortOrdersFacet) | `0xd177000be70ea4efc23987acd1a79eaba8b758f1` | 3 | 0/3 | 3 | 3 | https://github.com/code-423n4/2024-03-dittoeth-findings/blob/fb91efbbcd00fc16f39 |
| 194 | 2024-07-loopfi | Ethereum | CDPVault | `0x7fC6f72E895F1ed110799f5d6594149e4A0B7Ff3` | 3 | 0/3 | 2 | 3 | https://github.com/code-423n4/2024-07-loopfi-findings/blob/2eaf0aa6b0ae2c593f889 |
| 195 | 2025-01-06-native-v2-security-review-7c9b3fe3 | Ethereum | Native factory / RFQ router (v2 not reso | `0x85b0f66e83515ff4e825dfcaa58e040e08278ef9` | 3 | 0/3 | 0 | 3 |  |
| 196 | 2025-01-ethereum-evm-bacon-labs-bunniv2-securityreview | Ethereum | BunniHub (v2) | `0x000000000049C7bcBCa294E63567b4D21EB765f1` | 3 | 0/3 | 1 | 3 |  |
| 197 | 2025-02-06-part-2 | Ethereum | ZarosToken | `0xdcf2c04e35f3dddb8c52f21548a2f9f7a8178c3b` | 3 | 0/3 | 2 | 3 |  |
| 198 | 2025-04-virtuals-protocol | Base | Virtuals bonding curve | `0x1A540088125d00dD3990f9dA45CA0859af4d3B01` | 3 | 0/3 | 0 | 3 |  |
| 199 | 2025-05-21-jigsaw-contracts | Ethereum | Manager (jUSD CDP manager) | `0x0000000E44A948Ab0c83F2C65D3a2C4A06B05228` | 3 | 0/3 | 0 | 3 |  |
| 200 | 271 Wardens contributed reports to the Asymmetry | Ethereum | safETH | `0x6732efaf6f39926346bef8b821a04b6361c4f3e5` | 3 | 0/3 | 1 | 3 | https://github.com/code-423n4/2023-03-asymmetry-findings/blob/71d9ab60a26073cb37 |
| 201 | Adrena | Solana | Adrena SPL token mint (DefiLlama candida | `AuQaustGiaqxRvj2gtCdrd22PBzTn8kM3kEPEkZCtuDw` | 3 | 0/3 | 0 | 3 | https://osec.io/reports/15b84d4e-4146-8013-add8-c86467f40e2f |
| 202 | Ajna | Ethereum | ERC20Pool | `0x6146DD43C5622bB6D12A5240ab9CF4de14eDC625` | 3 | 0/3 | 1 | 3 | https://audits.sherlock.xyz/contests/114 |
| 203 | Algem Liquid Farming V3 | Astar | Algem Liquid Staking (Astar) | `0x70d264472327B67898c919809A9dc4759B6c0f27` | 3 | 0/3 | 1 | 3 |  |
| 204 | Ambire Contest | Ethereum | QuickAccManager | `0xfF3f6D14DF43c112aB98834Ee1F82083E07c26BF` | 3 | 0/3 | 1 | 3 | https://github.com/code-423n4/2021-10-ambire-findings/blob/e4194443bcf951332c01c |
| 205 | Aqualis | Ethereum | AQL token (Ethereum) | `0x73728b344499598e96842c2a9094a5c960888888` | 3 | 0/3 | 1 | 3 |  |
| 206 | Archi Finance | Arbitrum | CollateralPool | `0xbd198617aD1dc75B0f7A0A67BbE31993919Cd716` | 3 | 0/3 | 0 | 2 |  |
| 207 | Arrakis | Ethereum | ArrakisMetaVaultFactory | `0x820FB8127a689327C863de8433278d6181123982` | 3 | 0/3 | 0 | 3 | https://audits.sherlock.xyz/contests/195 |
| 208 | BMX Deli Swap | Base | BMX token | `0x548f93779fbc992010c07467cbaf329dd5f059b7` | 3 | 0/3 | 0 | 3 | https://audits.sherlock.xyz/contests/1154 |
| 209 | Baseline Round 2 | Base | Relay (Baseline core) | `0xc81fd894c0ace037d133af4886550ac8133568e8` | 3 | 0/3 | 0 | 3 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 210 | Bitway Labs | BNB Smart Chain | BTW token | `0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa` | 3 | 0/3 | 0 | 3 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 211 | Blockswap Stakehouse Withdrawals | Ethereum | StakeHouseUniverse | `0xbCB6F4efFB9Eb8eD31453Cc8BDAe9703C6D1FF9B` | 3 | 0/3 | 0 | 3 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 212 | Bond | Ethereum | FixedStrikeOptionTeller | `0xF507733f260a42bB2c8108dE87B7B0Ce5826A9cD` | 3 | 0/3 | 2 | 3 | https://audits.sherlock.xyz/contests/99 |
| 213 | Boot Finance contest | Ethereum | BOOT token | `0x0337fe811809A0aaf9B5D07945b39E473dE4c46E` | 3 | 0/3 | 0 | 3 | https://github.com/code-423n4/2021-11-bootfinance-findings/blob/61ce6a0d73efbea2 |
| 214 | Burve | Berachain | SimplexDiamond (Burve core) | `0xa1beD164c12CD9479A1049f97BDe5b3D6EC21089` | 3 | 0/3 | 1 | 3 | https://audits.sherlock.xyz/contests/858 |
| 215 | Buttonwood Buttonswap-core | Ethereum | ButtonswapPair | `0xB8DE4aB6C65e274630F5279f74eB69b66327CE50` | 3 | 0/3 | 1 | 3 | https://github.com/buttonwood-protocol/buttonswap-core/blob/3c85e5f15fe135f51e3a |
| 216 | Canto contest | Canto | Unitroller (Canto Lending Market) | `0x5E23dC409Fc2F832f83CEc191E245A191a4bCc5C` | 3 | 0/3 | 1 | 3 |  |
| 217 | Cooler | Ethereum | Clearinghouse | `0xE6343ad0675C9b8D3f32679ae6aDbA0766A2ab4c` | 3 | 0/3 | 2 | 3 | https://audits.sherlock.xyz/contests/107 |
| 218 | DittoETH Invitational | Ethereum | DittoETH Diamond | `0xd177000be70ea4efc23987acd1a79eaba8b758f1` | 3 | 0/3 | 2 | 3 | https://github.com/code-423n4/2024-07-dittoeth-findings/blob/424e49f12c01bd52e69 |
| 219 | Elfi | Arbitrum | ELFi Diamond (AccountFacet) | `0x153c613D572c050104086c7113d00B76Fbaa5d55` | 3 | 0/3 | 2 | 3 | https://audits.sherlock.xyz/contests/329 |
| 220 | Fastlane Atlas | Polygon | Atlas GasAccounting | `0xB363f4D32DdB0b43622eA07Ae9145726941272B4` | 3 | 0/3 | 0 | 2 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 221 | Foundation contest | Ethereum | NFTMarket | `0xcDA72070E455bb31C7690a170224Ce43623d0B6f` | 3 | 0/3 | 0 | 3 | https://github.com/code-423n4/2022-02-foundation-findings/blob/fc870979a6a45c504 |
| 222 | Frax Solidity | Ethereum | FRAX (Legacy Frax Dollar) | `0x853d955aCEf822Db058eb8505911ED77F175b99e` | 3 | 0/3 | 0 | 3 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 223 | GMX | Arbitrum | OrderHandler | `0x63492B775e30a9E6b4b4761c12605EB9d071d5e9` | 3 | 0/3 | 0 | 2 | https://audits.sherlock.xyz/contests/6 |
| 224 | Gamma Vaults (Gamma Strategies) | Ethereum | UniProxy | `0x83dE646A7125aC04950FEA7e322481D4BE66c71d` | 3 | 0/3 | 1 | 3 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 225 | Gamma Vaults (Gamma Strategies) | Ethereum | UniProxy (Ethereum/Uniswap) | `0x83dE646A7125aC04950FEA7e322481D4BE66c71d` | 3 | 0/3 | 0 | 3 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 226 | Goat Tech | Arbitrum Sepolia | Controller | `0xB4E5f0B2885F09Fd5a078D86E94E5D2E4b8530a7` | 3 | 0/3 | 1 | 2 | https://cdn.cantina.xyz/reports/cantina_competition_goat_mar2024.pdf |
| 227 | Helium Program Library | Solana | voter-stake-registry | `hvsrNC3NKbcryqDs2DocYHZ9yPKEVzdSjQG6RVtK1s8` | 3 | 0/3 | 0 | 3 | https://github.com/sec3-service/reports/blob/13c2f82d576164c7db728108d09a8d37272 |
| 228 | Heurist Aug1st | Base | HEU token | `0xEF22cb48B8483dF6152e1423b19dF5553BbD818b` | 3 | 0/3 | 0 | 3 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 229 | Holograph contest | Polygon | HolographOperator | `0x3a403792184aA24ec56bF7D24aD42C17CA2e2dbE` | 3 | 0/3 | 0 | 3 | https://github.com/code-423n4/2022-10-holograph-findings/blob/e519f7afcd8f59409c |
| 230 | Illuminate | Ethereum | ERC5095 PT | `0x3393f10c89F59d8c2533E559F931D147259A0A1B` | 3 | 0/3 | 3 | 3 | https://github.com/code-423n4/2022-06-illuminate-findings/blob/f76be2c0a75f80d3d |
| 231 | InfinityPools | Base | InfinityPoolFactory | `0x86342D7bBe93cB640A6c57d4781f04d93a695f08` | 3 | 0/3 | 2 | 3 | https://cdn.cantina.xyz/reports/cantina_competition_infinitypools_october2024.pd |
| 232 | Instadapp Fluid | Ethereum | Fluid Liquidity | `0x52Aa899454998Be5b000Ad077a46Bbe360F4e497` | 3 | 0/3 | 0 | 2 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 233 | InsureDAO contest | Ethereum | PoolTemplate | `0x1dcd35cFfF8a9B44aECc4087c7847Fb7A5BE56F9` | 3 | 0/3 | 2 | 2 | https://github.com/code-423n4/2022-01-insure-findings/blob/6bb0b8a20452d8fa3bc3b |
| 234 | InsureDAO contest | Ethereum | Vault | `0x131fb74c6fede6d6710ff224e07ce0ed8123f144` | 3 | 0/3 | 1 | 2 | https://github.com/code-423n4/2022-01-insure-findings/blob/6bb0b8a20452d8fa3bc3b |
| 235 | Jigsaw Finance | Ethereum | jUSD token | `0x000000096CB3D4007fC2b79b935C4540C5c2d745` | 3 | 0/3 | 1 | 3 | https://cdn.cantina.xyz/reports/cantina_competition_jigsaw_june2025.pdf |
| 236 | Juicebox contest | Ethereum | JBX token (JBV3Token) | `0x4554CC10898f92D45378b98D6D6c2dD54c687Fb2` | 3 | 0/3 | 0 | 3 | https://github.com/code-423n4/2022-10-juicebox-findings/blob/fad98139f727ae19bd1 |
| 237 | Larva Labs Meebits | Ethereum | Meebits | `0x7Bd29408f11D2bFC23c34f18275bBf23bB716Bc7` | 3 | 0/3 | 1 | 3 | https://github.com/code-423n4/2021-04-meebits-findings/blob/d9906d8bcf918b55c462 |
| 238 | Lavarage Invitational | Solana | Lavarage SOL pool program | `CRSeeBqjDnm3UPefJ9gxrtngTsnQRhEJiTA345Q83X3v` | 3 | 0/3 | 2 | 3 | https://github.com/code-423n4/2024-04-lavarage-findings/blob/108abd5f603cd995f90 |
| 239 | ListaDAO - Smart Collateral | BNB Chain | Moolah (LP price path) | `0x8F73b65B4caAf64FBA2aF91cC5D4a2A1318E5D8C` | 3 | 0/3 | 0 | 3 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 240 | Munchables | Blast | AccountManager (proxy) | `0xfB5cd7507A3Cb0932029Df2E78165667954C8286` | 3 | 0/3 | 2 | 3 | https://github.com/code-423n4/2024-07-munchables-findings/blob/2efccd9f1b65f77da |
| 241 | Myso Finance (Myso Loans) | Ethereum | Myso v1 lending pool | `0x15315dFc9E2Cc4F7F5456323Ab7010a1A74a337d` | 3 | 0/3 | 0 | 3 |  |
| 242 | NFTX | Ethereum | NFTXLPStaking | `0xB9a6b3E8a1B6EeB3FA6B1f48F591a953cA7b22b7` | 3 | 0/3 | 1 | 3 | https://github.com/code-423n4/2021-05-nftx-findings/blob/a3d804a58d4aff8b6ba1ab7 |
| 243 | OpalProtocol | Ethereum | Omnipool (wstETH) | `0x86b130298719F753808E96cA6540b684a2d21466` | 3 | 0/3 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_opal_feb2024.pdf |
| 244 | Parallel Protocol – PRL Token | Ethereum | PrincipalMigrationContract | `0x0EC5ab257aDf6968A3D3C187BE1Ee0fe74487Eb3` | 3 | 0/3 | 2 | 3 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 245 | Parcel | BNB Smart Chain | Parcel payroll | `0x35aD5a1cD3533495262aFd982be3003Ea77D3C31` | 3 | 0/3 | 2 | 3 |  |
| 246 | Pine Protocol | Ethereum | PineCore | `0x19c56cb20e6e9598fc4d22318436f34981e481f9` | 3 | 0/3 | 0 | 3 |  |
| 247 | PoolTogether TwabRewards contest | Ethereum | TwabRewards | `0x2589ff8614f74704741EE3B51851b4Ae812F1A21` | 3 | 0/3 | 2 | 3 | https://github.com/code-423n4/2021-12-pooltogether-findings/blob/4657f4ee11cfe0c |
| 248 | Real Wagmi 2 Audit Report | Metis | LiquidityBorrowingManager | `0x20fa274D00fF4917A13cD464FDbB200475B6EaBd` | 3 | 0/3 | 0 | 3 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 249 | Reserve Protocol - Invitational | Ethereum | eUSD RToken | `0xA0d69E286B938e21CBf7E51D71F6A4c8918f482F` | 3 | 0/3 | 1 | 3 | https://github.com/code-423n4/2023-07-reserve-findings/blob/7bb18b95f1645ae92f2a |
| 250 | Rubicon | Optimism | RubiconMarket (Classic order book) | `0x7a512d3609211e719737E82c7bb7271eC05Da70d` | 3 | 0/3 | 2 | 3 |  |
| 251 | Singularity | Fantom | SingularityOracle | `0xd9EFff5076764c3FD58C91D4FEE8AA45a71b1dB4` | 3 | 0/3 | 0 | 3 | https://github.com/yAudit/fellowship-audits/blob/2ddaff163a55d9d436c07e86adf18f9 |
| 252 | Sonic Airdrop Contracts | Sonic | Paintswap core (Sonic) | `0xe51ee9868c1f0d6cd968a8b8c8376dc2991bfe44` | 3 | 0/3 | 1 | 3 | https://cdn.cantina.xyz/reports/cantina_paintswap_contracts_april2025.pdf |
| 253 | Spectral (Autonomus Agents Contracts | Base | SPEC token (Base) | `0x96419929d7949D6A801A6909c145C8EEf6A40431` | 3 | 0/3 | 1 | 3 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 254 | Surge | Arbitrum | Surge pool factory | `0x503A14768e23456620fB3Cb61e37A36A2736Cbd0` | 3 | 0/3 | 0 | 3 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 255 | Synthetix TLX V2 | Optimism | LeveragedToken (example market) | `0x0a00866e76F8AA7F55B40C859077EE1D0F2d9384` | 3 | 0/3 | 1 | 3 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 256 | TermMax | Ethereum | TermMaxRouter (Ethereum) | `0xC47591F5c023e44931c78D5A993834875b79FB11` | 3 | 0/3 | 0 | 3 | https://cdn.cantina.xyz/reports/cantina_competition_term_max_december2024.pdf |
| 257 | Union Finance | Optimism | Comptroller | `0x06a31efa04453C5F9C0A711Cdb96075308C9d6E3` | 3 | 0/3 | 0 | 3 | https://audits.sherlock.xyz/contests/11 |
| 258 | Unlock Protocol | Ethereum | Unlock (factory/proxy) | `0x3d5409CcE1d45233dE1D4eBDEe74b8E004abDD13` | 3 | 0/3 | 1 | 3 |  |
| 259 | Velocimeter | Canto | Velocimeter V1 core | `0x2Baec546a92cA3469f71b7A091f7dF61e5569889` | 3 | 0/3 | 0 | 3 | https://audits.sherlock.xyz/contests/442 |
| 260 | WenCore | Ethereum | WenCore | `0x0b68e02B6AB80a2975D2358d869e50a9D9947AB9` | 3 | 0/3 | 0 | 3 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 261 | YuzuUSD (team 2025 08 28 yuzuusd) | Plasma | YuzuILP | `0xEbFC8C2Fe73C431Ef2A371AeA9132110aaB50DCa` | 3 | 0/3 | 0 | 3 |  |
| 262 | fujidao-labs | Ethereum | FujiVault | `0x5bcADd3D7E4E0CD44B9e34fd865C286A7eD75526` | 3 | 0/3 | 0 | 3 | https://github.com/ComposableSecurity/.github/blob/144b868957d165fa3f5210ae80928 |
| 263 | gamma | Ethereum | Hypervisor / UniProxy | `0xfb203298a28c7bb92486C9D92af07F34Eb95B823` | 3 | 0/3 | 0 | 3 | https://diligence.consensys.io/audits/2022/02/gamma/gamma-audit-2022-02.pdf |
| 264 | oku s new order types contract contest | Optimism | Bracket | `0x8e9a03e2533f8B4641a271429496F582B89c8fD7` | 3 | 0/3 | 1 | 3 |  |
| 265 | prospective world | Ethereum | Prospective (PROS) token | `0xbe1936A67f503e0eaF2434b0cf9f4e3d7100008A` | 3 | 0/3 | 0 | 2 |  |
| 266 | reNFT | Ethereum | Guard policy | `0xf56F2E76Fa5628eDf03Dd311eCDcB704E4826d26` | 3 | 0/3 | 1 | 3 | https://github.com/code-423n4/2024-01-renft-findings/blob/273c1d163a81a8b5cd09c0 |
| 267 | rhinestone smartsessions core | Ethereum | SmartSession | `0x00000000008bDABA73cD9815d79069c247Eb4bDA` | 3 | 0/3 | 0 | 3 |  |
| 268 | sentiment | Arbitrum | Sentiment Controller (getAllLTokens) | `0x17b07cfbab33c0024040e7c299f8048f4a49679b` | 3 | 0/3 | 0 | 3 |  |
| 269 | superform-core | Ethereum | SuperRegistry | `0x17A332dC7B40aE701485023b219E9D6f493a2514` | 3 | 0/3 | 2 | 3 | https://cdn.cantina.xyz/reports/cantina_solo_superform_jul2024.pdf |
| 270 | tokemak- -may | Ethereum | TOKE token | `0x2e9d63788249371f1DFC918a52f8d799F4a38C94` | 3 | 0/3 | 1 | 3 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 271 | 04 30 MZero-FV-MR | Ethereum | PowerToken | `0x5983B89FA184f14917013B9C3062afD9434C5b03` | 2 | 2/0 | 0 | 2 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 272 | 1inch Aqua and SwapVM MVP v1.0 | Ethereum | AquaSwapVMRouter (SwapVM apps: PeggedSwa | `0x111111338c5091e8440b67b168bae16a668ac0de` | 2 | 2/0 | 2 | 2 | https://www.openzeppelin.com/news/1inch-aqua-and-swapvm-mvp-v1.0-audit |
| 273 | 1inch Liquidity Protocol | Ethereum | ReferralFeeReceiver | `0x1Cc61726b11613B37854A1C9EbC9a2092Ed91b9D` | 2 | 2/0 | 1 | 2 | https://diligence.security/audits/2020/12/1inch-liquidity-protocol/ |
| 274 | 1inch SwapVM&Aqua Audit | Ethereum | AquaSwapVMRouter (SwapVM) | `0x111111338c5091e8440b67b168bae16a668ac0de` | 2 | 2/0 | 2 | 2 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 275 | 2020-12-16-yvs-finance-sca-yvs-finance-erc20-staki | Ethereum | YvsPresale | `0x96a7c18650DEDf9E76355f3f0458B027B789e201` | 2 | 2/0 | 1 | 2 |  |
| 276 | 2024-04-08-mellow-alm-toolkit | Ethereum | MellowVault | `0x4438c8A6db957aA90eF2772A2574495E30Eb9bA7` | 2 | 2/0 | 1 | 2 |  |
| 277 | 2024-04-29-sigmaprime-sushi-auction-maker-furo-rev | Ethereum | FuroVesting.stopVesting | `0x0689640d190b10765f09310fCfE9C670eDe4E25B` | 2 | 2/0 | 1 | 2 |  |
| 278 | 2024-04-30-singularitydao-sca-sdao-lockerstaking-a | Ethereum | SDAO token | `0x993864E43Caa7F7F12953AD6fEb1d1Ca635B875F` | 2 | 2/0 | 1 | 2 |  |
| 279 | 2024-11-27-unizen-sca-unizen-unizen-trade-aggregat | Ethereum | Unizen Trade Aggregator (router) | `0xd3f64BAa732061F8B3626ee44bab354f854877AC` | 2 | 2/0 | 2 | 2 |  |
| 280 | 2025-05-12-across-audit | Ethereum | SpokePool (Ethereum) | `0x5c7BCd6E7De5423a257D81B442095A1a6ced35C5` | 2 | 2/0 | 0 | 2 | https://www.openzeppelin.com/news/across-audit |
| 281 | ACES Oct3 | Base | AcesToken (ACES.fun) | `0x55337650856299363c496065C836B9C6E9dE0367` | 2 | 2/0 | 2 | 2 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 282 | Alkimiya | Ethereum | SilicaPools | `0xf3F84cE038442aE4c4dCB6A8Ca8baCd7F28c9bDe` | 2 | 2/0 | 2 | 2 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 283 | Anvil Audit | Ethereum | PythPriceOracle | `0xC6f3405c861Fa0dca04EC4BA59Bc189D1d56Ee05` | 2 | 2/0 | 0 | 2 | https://www.openzeppelin.com/news/anvil-audit |
| 284 | Astroport on Osmosis | Osmosis | pair_concentrated pool (instantiated by  | `osmo1246fnsutktuqqzrru673pqwtt64n288004j5fauyuezwr54llw5sl6drp6` | 2 | 2/0 | 2 | 2 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 285 | Beanstalk | Ethereum | Beanstalk Diamond (FertilizerFacet/Curve | `0xBEA0000029AD1c77D3d5D23Ba2D8893dB9d1Efab` | 2 | 2/0 | 1 | 2 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 286 | Bear Cave | Ethereum | HoneyBox | `0x68fFCb1B5F8e5d035c3B4bf49F8F139F49E45509` | 2 | 2/0 | 1 | 2 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/s |
| 287 | Blueberry | Hyperliquid | HyperVaultRouter | `0x647a4D7F1F20Cf237C27b39fB6924f5a7691BB4b` | 2 | 2/0 | 2 | 2 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 288 | Botanix | Botanix | Minting contract (node-side check) | `0x0Ea320990B44236A0cEd0ecC0Fd2b2df33071e78` | 2 | 2/0 | 1 | 2 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 289 | Bridge Mutual | Ethereum | BMI token (context only) | `0x725c263e32c72ddc3a19bea12c5a0479a81ee688` | 2 | 2/0 | 0 | 2 | https://diligence.security/audits/2021/03/bridge-mutual/ |
| 290 | Bunni | Ethereum | BunniHook (v2) | `0x000052423c1dB6B7ff8641b85A7eEfc7B2791888` | 2 | 2/0 | 1 | 2 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 291 | Circuits and | Ethereum | zkLink deposit circuit | `0x5fd9f73286b7e8683bab45019c94553b93e015cf` | 2 | 2/0 | 0 | 2 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 292 | Coinbase Spend permissions | Base | SpendPermissionManager | `0xf85210B21cC50302F477BA56686d2019dC9b67Ad` | 2 | 2/0 | 2 | 2 | https://cdn.cantina.xyz/reports/cantina_coinbase_oct2024.pdf |
| 293 | Degis SCProtection | Avalanche | PolicyCenter | `0xA14058c19525587ce2095f2318A2d0B805FB0312` | 2 | 2/0 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 294 | Eternal Finance | Aptos | Eternal Finance core module | `0x25a64579760a4c64be0d692327786a6375ec80740152851490cfd0b53604cf95` | 2 | 2/0 | 1 | 2 | https://osec.io/reports/3c48e8be-1fbe-4e13-be4d-437f22c24a52 |
| 295 | Etherspot Credible Account Module | Ethereum | ResourceLockValidator | `0xe8bC0032846DEFDA434B08514034CDccD8db5318` | 2 | 2/0 | 1 | 2 | https://github.com/shieldify-security/audits-portfolio-md/blob/f2c051af4ffb67e11 |
| 296 | Fluence Deal | Ethereum | FLT token (context only) | `0x236501327e701692a281934230AF0b6BE8Df3353` | 2 | 2/0 | 0 | 2 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 297 | Glif Filecoin InfinityPool | Filecoin | InfinityPool.borrow | `0xe764Acf02D8B7c21d2B6A8f0a96C78541e0DC3fd` | 2 | 2/0 | 2 | 2 | https://diligence.security/audits/2023/04/glif-filecoin-infinitypool/ |
| 298 | GoldilocksGoldilend | Berachain | Goldiswap ($LOCKS) | `0xb7E448E5677D212B8C8Da7D6312E8Afc49800466` | 2 | 2/0 | 2 | 2 | https://github.com/electisec/reports/blob/44ab756f5a45d0bff0f92a0cd4693c3fa0b868 |
| 299 | Hylo | Solana | Exchange (v0.1) | `HYEXCHtHkBagdStcJCp3xbbb9B7sdMdWXFNj6mdsG4hn` | 2 | 2/0 | 0 | 2 | https://osec.io/reports/20684d4e-4146-80a3-87e8-c1794cae5518 |
| 300 | IBCX | Osmosis | IBCX Core (CosmWasm contract, code_id 45 | `osmo14klwqgkmackvx2tqa0trtg69dmy0nrg4ntq4gjgw2za4734r5seqjqm4gm` | 2 | 2/0 | 2 | 2 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 301 | Jakub Heba | Sei | Jellyverse core (Sei) | `0xdd7d5e4ea2125d43c16eed8f1ffefffa2f4b4af6` | 2 | 2/0 | 1 | 2 |  |
| 302 | Kim NFT marketplace | Mode | KimNFTMarketplace | `0x67135675e22F7ff34eBA30f15f39F9cd30d29079` | 2 | 2/0 | 0 | 2 | https://cdn.cantina.xyz/reports/cantina_kim_exchange_november2024.pdf |
| 303 | Kite | Kite Mainnet | KiteStakingManager.claimDelegatorRewards | `0x7d627b0F5Ec62155db013B8E7d1Ca9bA53218E82` | 2 | 2/0 | 2 | 2 | https://www.halborn.com/audits/kite/staking--rewards-contracts-2a1577 |
| 304 | Libertify | Ethereum | LibertiVault | `0x429032A407aed3D5fF84caf38EFF217eB4d322A9` | 2 | 2/0 | 1 | 2 |  |
| 305 | Linea Plonk Verifier | Ethereum | LineaRollup (L1 proxy) | `0xd19d4B5d358258f05D7B411E21A1460D11B0876F` | 2 | 2/0 | 0 | 2 | https://diligence.security/audits/2023/06/linea-plonk-verifier/ |
| 306 | MIMSwap Updates | Ethereum | MIMSwap (MagicLP pool) | `0xDF46F6b1a5F794F21eaD4008C7De4E02Dc045297` | 2 | 2/0 | 1 | 2 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 307 | MORE | Flow | Pool (proxy) | `0xbC92aaC2DBBF42215248B5688eB3D3d2b32F2c8d` | 2 | 2/0 | 2 | 2 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 308 | Mantle V2 Solidity | Mantle | L2CrossDomainMessenger | `0x4200000000000000000000000000000000000007` | 2 | 2/0 | 0 | 2 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 309 | Margined Protocol Locust Vault | Osmosis | Locust Vault (stOSMO instance) | `osmo16s3sxs5886p42kteunp6370pken2n5ukzszz0trkr39epqtawn2qk4r9l5` | 2 | 2/0 | 0 | 2 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 310 | Move Dollar | Aptos | stability_pool module | `0x6f986d146e4a90b828d8c12c14b6f4e003fdff11a8eecceceb63744363eaac01` | 2 | 2/0 | 0 | 2 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 311 | NexusMutual on April 22nd, 2019. | Ethereum | QuotationData | `0x1776651F58a17a50098d31ba3C3cD259C1903f7A` | 2 | 2/0 | 1 | 2 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 312 | Pike Finance | Base | PIKE token | `0x25e1c298f100d7c600e9e44d46788c1ebbd4f69b` | 2 | 2/0 | 1 | 2 | https://osec.io/reports/d6de865b-9022-4b57-8bfc-7211c6b27b5b |
| 313 | PowerPool Agent | Ethereum | PPAgentV2 | `0xc9ce4CdA5897707546F3904C0FfCC6e429bC4546` | 2 | 2/0 | 0 | 2 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 314 | Programmable Derivatives | Base | ETHPool | `0x7cA62A2Dc82ca66C620a6a0aC4F986fd98959f6a` | 2 | 2/0 | 2 | 2 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 315 | Public - Crabada Sale | Avalanche | CRA token (context only) | `0xA32608e873F9DdEF944B24798db69d80Bbb4d1ed` | 2 | 2/0 | 0 | 2 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 316 | Public - LunaRush Smartcontracts | BNB Chain | Luna Rush (LUS) token | `0xde301D6a2569aEfcFe271B9d98f318BAee1D30a4` | 2 | 2/0 | 1 | 2 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 317 | Reclaim Protocol | Ethereum | Reclaim claim/verification contract | `0x65BB2E9F1C56226109304A94d6232Bc5B10636DE` | 2 | 2/0 | 0 | 2 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 318 | Renzo Protocol EVM Contracts Smart Contract Security | Ethereum | RestakeManager | `0xDC5a2FDC997897646f4F602826a8691e7B6EEc1d` | 2 | 2/0 | 1 | 2 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 319 | Restakefi | Ethereum | RSTK token | `0x12eF10A4fc6e1Ea44B4ca9508760fF51c647BB71` | 2 | 2/0 | 1 | 2 | https://www.openzeppelin.com/news/restakefi-audit |
| 320 | ResupplyFinance | Ethereum | LiquidationHandler / ResupplyPairCore | `0x88888888c227c36401493Ed9F3e3Dcc3800B2634` | 2 | 2/0 | 1 | 2 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 321 | Rivus | Ethereum | RivusDAO (RIVUS) | `0x60e254e35dd712394b3aba7a1d19114732e143dd` | 2 | 2/0 | 0 | 2 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 322 | SingularityAudit | Arbitrum | StakingAssetManager | `0xB1CC5D9227323330E8a58e891c123B38D03f0BAA` | 2 | 2/0 | 1 | 1 | https://github.com/threesigmaxyz/publications/blob/2f7ea0cf2efa42ae5c4364359cb3f |
| 323 | SolLightning | Solana | SolLightning swap program | `4hfUykhqmD7ZRvNh1HuzVKEY7ToENixtdUKZspNDCrEM` | 2 | 2/0 | 0 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 324 | Streamswap | Osmosis | Streamswap (stream contract) | `osmo17kqws7fy2qnejdw68cqjlw456gdxcdukk0wq6026u826zlda3y7qdhzqlv` | 2 | 2/0 | 2 | 2 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 325 | SuperWorld Inc. - May 19, 2021 | Ethereum | SuperWorld token | `0xfD89EA92F6EC07d955e2adBBA2400Ca1a6369028` | 2 | 2/0 | 0 | 2 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 326 | Sushi Swap Auction Maker and Furo | Ethereum | FuroVesting | `0x593453768Ba2163eaE6d0FA1f3d292C02672A2Ba` | 2 | 2/0 | 0 | 2 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 327 | Taiko Protocol | Ethereum | Bridge.sendMessage / retryMessage (L1) | `0xd60247c6848B7Ca29eDdF63AA924E53dB6Ddd8EC` | 2 | 2/0 | 2 | 2 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 328 | TapiocaDAO | Arbitrum | YieldBox | `0xCFFd997DB053c0fC54010770b55A4E02B1D104a5` | 2 | 2/0 | 0 | 2 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 329 | Thesis - tBTC and keep | Ethereum | TBTCSystem.requestNewKeep | `0x41A1b40c1280883eA14C6a71e23bb66b83B3fB59` | 2 | 2/0 | 0 | 2 | https://diligence.consensys.io/audits/2020/02/thesis-tbtc-and-keep/thesis-tbtc-a |
| 330 | Thesis - tBTC and keep | Ethereum | TBTCSystem (tBTC v1) | `0x41A1b40c1280883eA14C6a71e23bb66b83B3fB59` | 2 | 2/0 | 0 | 0 | https://diligence.consensys.io/audits/2020/02/thesis-tbtc-and-keep/thesis-tbtc-a |
| 331 | USM - December 10, 2020 | Ethereum | USMWETHProxy | `0x19d4465Ea18d31fC113DF522994b68BA9a10A184` | 2 | 2/0 | 1 | 2 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 332 | Wido Comet Collateral Swap Contracts | Ethereum | WidoRouter | `0x919dF3aDbF5cfC9fcfd43198EDFe5aA5561CB456` | 2 | 2/0 | 1 | 2 | https://www.openzeppelin.com/news/wido-comet-collateral-swap-contracts |
| 333 | XDAO | Ethereum | CrowdfundingModule | `0x711E14eBC41A8f1595433FA4409a50BC9838Fc03` | 2 | 2/0 | 2 | 2 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 334 | XDAO | Ethereum | Crowdfunding module (Ethereum) | `0x711E14eBC41A8f1595433FA4409a50BC9838Fc03` | 2 | 2/0 | 1 | 2 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 335 | ZKSWAP AUDIT | Ethereum | ZKSwap: ZKSync (zkSync contract) | `0x2F70F6D864F8F597a0ef57aDDf24323DFAb5797f` | 2 | 2/0 | 0 | 2 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 336 | angelblock | Ethereum | CommunityRound | `0xe62E320390B748DE22BA7BE75c967d10b2eD172d` | 2 | 2/0 | 0 | 2 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 337 | nftx-protocol-v3 | Ethereum | MarketplaceUniversalRouterZap | `0x293A0c49c85F1D8851C665Ac3cE1f1DC2a79bE3d` | 2 | 2/0 | 0 | 2 | https://cdn.cantina.xyz/reports/cantina_nftx_aug2023.pdf |
| 338 | 06--Sickle | Base | SickleFactory (Base) | `0x71D234A3e1dfC161cc1d081E6496e76627baAc31` | 2 | 1/1 | 1 | 2 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 339 | 11 04 SushiSwap Constant Product Pool-FV | Ethereum | Trident ConstantProductPoolFactory | `0xD75F5369724b513b497101fb15211160c1d96550` | 2 | 1/1 | 1 | 2 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 340 | 2024-08-aligned-layer | Ethereum | AlignedLayerServiceManager | `0x4A5D61ABa7d845bC71d4E2f2Dd7C35D9c5fb55B8` | 2 | 1/1 | 1 | 2 | https://diligence.security/audits/2024/08/aligned-layer/aligned-layer-audit-2024 |
| 341 | Almanak May6th | Ethereum | alUSD vault | `0xDCD0f5ab30856F28385F641580Bbd85f88349124` | 2 | 1/1 | 1 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 342 | Apollo DAO 3 | Osmosis | Apollo vault atom_statom | `osmo1a6tcf60pyz8qq2n532dzcs7s7sj8klcmra04tvaqympzcvxqg9esn7xz7l` | 2 | 1/1 | 0 | 2 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 343 | Arcade Services Inc. | Ethereum | LoanCoreV2 | `0x81b2f8fc75bab64a6b144aa6d2faa127b4fa7fd9` | 2 | 1/1 | 1 | 2 | https://github.com/ComposableSecurity/.github/blob/144b868957d165fa3f5210ae80928 |
| 344 | Avantis (now Veranta) | Base | Avantis Trading (TransparentUpgradeableP | `0x5FF292d70bA9cD9e7CCb313782811b3D7120535f` | 2 | 1/1 | 0 | 2 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 345 | Axis periphery | Ethereum | USDxMarket | `0x5aE365Ac83638418c4c30555d32F9A91ccAEf58C` | 2 | 1/1 | 0 | 2 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 346 | ChainLocker | Ethereum | TokenLocker (deployed by ChainLockerFact | `0x9E444E9F6e248e1a43E1a76C51B685060BeAd3C1` | 2 | 1/1 | 0 | 2 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 347 | Credbull | Arbitrum | MultiTokenVault | `0xD6b3d81868770083307840F513A3491960b95cb6` | 2 | 1/1 | 1 | 2 |  |
| 348 | DELIGHT LABS - Terraswap | Terra | Terraswap Router (Terra 2.0 phoenix-1) | `terra13ehuhysn5mqjeaheeuew2gjs785f6k7jm8vfsqg3jhtpkwppcmzqcu7chk` | 2 | 1/1 | 0 | 2 | https://terraswap.io/wp-content/uploads/2023/07/terraswap-audit-report.pdf |
| 349 | DELIGHT LABS - Terraswap-classic | Terra | terraswap_pair | `terra1466nf3zuxpya8q9emxukd7vftaf6h4psr0a07srl5zw74zh84yjqxl5qul` | 2 | 1/1 | 0 | 2 | https://terraswap.io/wp-content/uploads/2023/06/terraswap-classic-20230620.pdf |
| 350 | Definitive | Base | Definitive DEX aggregator/core (EVM depl | `0xED6E000dEF95780fb89734c07EE2ce9F6dcAf110` | 2 | 1/1 | 0 | 2 | https://osec.io/reports/c8d40981-7b4d-4b38-a309-bbaff588bbd1 |
| 351 | ENS contest | Ethereum | ETHRegistrarController | `0x253553366Da8546fC250F225fe3d25d0C782303b` | 2 | 1/1 | 0 | 2 | https://github.com/ConsenSysDiligence/ens-audit-report-2019-02/blob/4c4005c90767 |
| 352 | Eggs Finance | Sonic | Eggs | `0xf26Ff70573ddc8a90Bd7865AF8d7d70B8Ff019bC` | 2 | 1/1 | 1 | 2 | https://cdn.cantina.xyz/reports/cantina_eggs_february2025.pdf |
| 353 | EulerV2 | Ethereum | Ethereum Vault Connector (EVC) | `0x0C9a3dd6b8F28529d72d7f9cE918D493519EE383` | 2 | 1/1 | 1 | 2 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 354 | Flooring | Ethereum | Flooring Lab Credit (FLC) token | `0x102c776DDB30C754dEd4fDcC77A19230A60D4e4f` | 2 | 1/1 | 0 | 2 | https://osec.io/reports/2678a838-b830-4c31-b530-ad82907e8489 |
| 355 | Florence Finance | Ethereum | FlorinTreasury | `0x95676E08c0bB37A9Ab360856C7C2B399204F41AA` | 2 | 1/1 | 1 | 2 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/s |
| 356 | Frakt | Solana | FRAKT token mint | `ErGB9xa24Szxbk1M28u2Tx8rKPqzL6BroNkkzk5rG4zj` | 2 | 1/1 | 1 | 2 | https://osec.io/reports/f5136412-1fd1-48f1-84a9-fd00260df7d1 |
| 357 | Glow | Solana | Glow Margin program | `GLoWMgcn3VbyFKiC2FGMgfKxYSyTJS7uKFwKY2CSkq9X` | 2 | 1/1 | 0 | 2 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 358 | GooseFX | Solana | GFX token | `GFX1ZjR2P15tmrSwow6FjyDYcEkoFb4p4gJCpLBjaxHD` | 2 | 1/1 | 0 | 2 | https://osec.io/reports/d4bf416f-34af-4357-92b5-0c7fb922de22 |
| 359 | Guanciale | Base | GUAN token | `0xcc0adB6C436eB1f65B2f27733Bf926691b94c5f1` | 2 | 1/1 | 0 | 2 | https://github.com/shieldify-security/audits-portfolio/blob/a1e130f5a286cbc3ede4 |
| 360 | Hello Labs bridge and VotingSwap | Ethereum | VotingSwap | `0xFAa8289820A643B1b6e95Cd6003117dDEF52B1b9` | 2 | 1/1 | 2 | 2 |  |
| 361 | Hinkal Protocol | Ethereum | Hinkal pool | `0x25e5e82f5702A27C3466fE68f14abDbbAdFca826` | 2 | 1/1 | 0 | 0 |  |
| 362 | Lodestar Lodestar Finance Smart Contract Security | Arbitrum | Lodestar Controller (Unitroller) | `0xa86dd95c210dd186fa7639f93e4177e97d057576` | 2 | 1/1 | 1 | 2 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 363 | LucidLabs | Ethereum | AssetController (L-USDC, Ethereum) | `0x3b55a4C0691d4D62719D0BFaA435010fBF2F135f` | 2 | 1/1 | 1 | 2 | https://www.halborn.com/audits/lucidlabs/lucidlabs---smart-contract-security-ass |
| 364 | Lumin | Arbitrum | Lumin Finance (DefiLlama-listed address, | `0x1FC01117E196800f416A577350CB1938d10501C2` | 2 | 1/1 | 1 | 2 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/s |
| 365 | Mars Outposts | Neutron | Red Bank | `neutron1n97wnm7q6d2hrcna3rqlnyqw2we6k0l8uqvmyqq6gsml92epdu7quugyph` | 2 | 1/1 | 1 | 2 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 366 | Nested Finance | Ethereum | NestedFactory | `0xD6D813e31558b45769B83E33Fe10cDef76128Ffc` | 2 | 1/1 | 0 | 2 | https://github.com/code-423n4/2021-11-nested-findings/blob/f9dab0c5c4250ac3b4ae0 |
| 367 | NodeOps Network | Arbitrum | NODE token | `0x2f714d7b9a035d4ce24af8d9b6091c07e37f43fb` | 2 | 1/1 | 0 | 2 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 368 | Peapods | Ethereum | Peapods IndexManager | `0x0Bb39ba2eE60f825348676f9a87B7CD1e3B4AE6B` | 2 | 1/1 | 1 | 2 |  |
| 369 | PoolTogether - Pods | Ethereum | Pod.deposit | `0x9F4C5D8d9BE360DF36E67F52aE55C1B137B4d0C4` | 2 | 1/1 | 0 | 2 | https://diligence.security/audits/2021/03/pooltogether-pods/ |
| 370 | PoolTogether - Pods | Ethereum | DaiPod proxy | `0x9F4C5D8d9BE360DF36E67F52aE55C1B137B4d0C4` | 2 | 1/1 | 1 | 2 | https://diligence.security/audits/2021/03/pooltogether-pods/ |
| 371 | Private Transfer With USX | Scroll | PrivateGatewayScroll | `0x902DD3a47B4473917607C8B10250703b7F35FdD0` | 2 | 1/1 | 2 | 2 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 372 | Public - SingSing Smartcontracts | BNB Chain | SING token | `0x8C80c06c6F8c00d2d6f3CFd6333ebB3759d66868` | 2 | 1/1 | 0 | 2 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 373 | REQUEST | Ethereum | SquidRouterModule | `0x6611eBA0150dCb8420f7792f2d68DaA055634F2d` | 2 | 1/1 | 2 | 2 | https://diligence.security/audits/2026/06/new-market-trading-contracts/ |
| 374 | Royco | Ethereum | VaultMarketHub | `0xa97eCc6Bfda40baf2fdd096dD33e88bd8e769280` | 2 | 1/1 | 1 | 2 | https://cdn.cantina.xyz/reports/cantina_royco_august2024.pdf |
| 375 | Sablier Finance | Ethereum | SablierV2LockupLinear | `0xB10daee1FCF62243aE27776D7a92D39dC8740f95` | 2 | 1/1 | 0 | 2 | https://cdn.cantina.xyz/reports/cantina_sablier_mar2023.pdf |
| 376 | Sapience-1 | Ethereal | PredictionMarketBridge | `0x3d28B47Cd916Ca7548dFB11cd261d579565f3730` | 2 | 1/1 | 1 | 2 | https://0xmacro.com/library/audits/sapience-1 |
| 377 | Sector Finance | Arbitrum | SCYVault factory (Arbitrum) | `0x7cf580c74d6974f4d4e7eb6edcf052770f9e2645` | 2 | 1/1 | 2 | 2 | https://1194552491-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 378 | Size Credit | Base | Size OrderBook | `0x044d9b2c4d8a696fe83fbb723f6006bd2d7a0e7e` | 2 | 1/1 | 1 | 2 | https://github.com/ObsidianAudits/audits/blob/d43dee47b37b1b582a888c706133be61f9 |
| 379 | THORSTARTER | Ethereum | XRUNE token | `0x69fa0feE221AD11012BAb0FdB45d444D3D2Ce71c` | 2 | 1/1 | 1 | 2 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 380 | ThalaSwap V2 | Aptos | ThalaSwap AMM | `0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af` | 2 | 1/1 | 1 | 2 | https://osec.io/reports/10b84d4e-4146-8076-97df-da8b6a43f938 |
| 381 | Timeless | Ethereum | LIT token | `0xfd0205066521550D7d7AB19DA8F72bb004b4C341` | 2 | 1/1 | 1 | 2 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 382 | Uma | Ethereum | Optimistic Oracle V3 | `0xfb55F43fB9F48F63f9269DB7Dde3BbBe1ebDC0dE` | 2 | 1/1 | 0 | 2 | https://www.openzeppelin.com/news/uma-audit-phase-2 |
| 383 | Uniswap V3 | Ethereum | NonfungiblePositionManager | `0xC36442b4a4522E871399CD717aBDD847Ab11FE88` | 2 | 1/1 | 1 | 1 | https://github.com/ConsenSysDiligence/Uniswap-audit-report-2018-12/blob/8c7473d3 |
| 384 | Velodrome Finance | Optimism | Voter | `0x41C914ee0c7E1A5edCD0295623e6dC557B5aBf3C` | 2 | 1/1 | 0 | 2 | https://cdn.cantina.xyz/reports/Velodrome-Spearbit-Security-Review.pdf |
| 385 | cLabs June23( ) (Governance Protocol | Celo | Governance (proxy) | `0xD533Ca259b330c7A88f74E000a3FaEa2d63B7972` | 2 | 1/1 | 0 | 2 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 386 | decentralized synthetic dollar | Ethereum | UsdnProtocol | `0x656cb8c6d154aad29d8771384089be5b5141f01a` | 2 | 1/1 | 1 | 2 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 387 | pashov-team-2025-05-07-kittenswap-security-review | Hyperliquid L1 | Kittenswap Algebra core (HyperEVM) | `0x618275f8efe54c2afa87bfb9f210a52f0ff89364` | 2 | 1/1 | 1 | 2 |  |
| 388 | 109 Wardens contributed reports to the Astaria | Ethereum | AstariaRouter (proxy) | `0x42CDc5D4B05E8dACc2FCD181cbe0Cc86Ee14c439` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2023-01-astaria-findings/blob/8059d5e7c4b3b7155259 |
| 389 | 11-14- Abracadabra GMXV2 | Arbitrum | GMX V2 Cauldron (GM ARB market) | `0x4F9737E994da9811B8830775Fd73E2F1C8e40741` | 2 | 0/2 | 0 | 2 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 390 | 1inch Exchange AggregationRouter V5 | Ethereum | AggregationRouterV5 / OrderMixin | `0x1111111254EEB25477B68fb85Ed929f73A960582` | 2 | 0/2 | 1 | 2 | https://diligence.security/audits/2022/08/1inch-exchange-aggregationrouter-v5/1i |
| 391 | 1inch Limit Order Protocol | Ethereum | LimitOrderProtocol (v2) | `0x119c71D3BbAC22029622cbaEc24854d3D32D2828` | 2 | 0/2 | 1 | 2 | https://www.openzeppelin.com/news/1inch-limit-order-protocol-audit |
| 392 | 2018-11-ethereum-evm-origin | Ethereum | Marketplace (V00_Marketplace) | `0x819bb9964b6ebf52361f1ae42cf4831b921510f9` | 2 | 0/2 | 2 | 2 |  |
| 393 | 2019-09-ethereum-evm-aaveprotocol | Ethereum | LendingPoolCore (Aave v1) | `0x3dfd23A6c5E8BbcFc9581d2E864a68feb6a076d3` | 2 | 0/2 | 1 | 2 |  |
| 394 | 2020-01-ethereum-evm-balancercore | Ethereum | BPool | `0x59A19D8c652FA0284f44113D0ff9aBa70bd46fB4` | 2 | 0/2 | 2 | 2 |  |
| 395 | 2021-06-12-bunicorn-sca-bunicorn-governance-erc20- | BNB Chain | BuniCornPool.mint | `0x86873f85bc12ce40321340392c0ff39c3bdb8d68` | 2 | 0/2 | 0 | 2 |  |
| 396 | 2021-06-12-bunicorn-sca-bunicorn-governance-erc20- | BNB Chain | BuniCornPool.burn | `0x86873f85bc12ce40321340392c0ff39c3bdb8d68` | 2 | 0/2 | 0 | 2 |  |
| 397 | 2021-06-12-bunicorn-sca-bunicorn-governance-erc20- | BNB Chain | BuniCornFactory (V2 pools) | `0x86873f85bc12ce40321340392c0ff39c3bdb8d68` | 2 | 0/2 | 0 | 2 |  |
| 398 | 2021-12-frax-finance-fraxq42021 | Ethereum | FraxPoolV3 (reference pool) | `0x80c72d42846EFf15Cb1BDEE8FeC9A57594F17960` | 2 | 0/2 | 0 | 2 |  |
| 399 | 2022-11-redactedcartel | Arbitrum | Pirex pxGMX (PxGmx) | `0x9a592b4539e22eeb8b2a3df679d572c7712ef999` | 2 | 0/2 | 2 | 2 |  |
| 400 | 2023-02-21-parcel-payroll-smart-contract-audit | BNB Chain | Parcel PayrollFactory | `0x35aD5a1cD3533495262aFd982be3003Ea77D3C31` | 2 | 0/2 | 2 | 2 |  |
| 401 | 2023-02-ethereum-evm-nestedfinance-smartcontracts-securityre | Ethereum | NestedFactoryProxy | `0xE24c8123c8054fB9E8C53496948C34Ea59914cdF` | 2 | 0/2 | 0 | 2 |  |
| 402 | 2023-02-socket | Ethereum | CelerImpl.refundCelerUser | `0x7c6C373190421988fA31E64f369C45205676C1f0` | 2 | 0/2 | 0 | 2 | https://diligence.security/audits/2023/02/socket/socket-audit-2023-02.pdf |
| 403 | 2023-05-24-dexalot-sca-re-audit-dexalot-erc20-dex-may2023-sc | Avalanche | DexalotToken | `0x093783055f9047c2bff99c4e414501f8a147bc69` | 2 | 0/2 | 0 | 2 |  |
| 404 | 2023-05-maia | Arbitrum | RootPort | `0x5399Eee5073bC1018233796a291Ffd6a78E26cbb` | 2 | 0/2 | 1 | 2 |  |
| 405 | 2023-06-angle | Ethereum | AngleDistributor | `0xD9f22abbe5Bf9c46413af053e34dBE987Ff8418d` | 2 | 0/2 | 1 | 2 |  |
| 406 | 2023-06-lybra | Ethereum | EUSD | `0x97de57eC338AB5d51557DA3434828C5DbFaDA371` | 2 | 0/2 | 1 | 2 |  |
| 407 | 2023-07-axelar | Ethereum | AxelarGateway (proxy) | `0x4F4495243837681061C4743b74B3eEdf548D56A5` | 2 | 0/2 | 1 | 2 | https://github.com/axelarnetwork/audits/blob/d8d430efd941945af8cf95b7f029dee2ce8 |
| 408 | 2023-10-ethereum-evm-saltyio-securityreview | Ethereum | SALT token | `0x0110B0c3391584Ba24Dbf8017Bf462e9f78A6d9F` | 2 | 0/2 | 1 | 2 |  |
| 409 | 2024-02-08-uncx-uniswapv3-liquidity-locker-audit | Ethereum | UniswapV3Locker | `0xC1aF6DA1fB706F1679DE7d525F4799cdC3B6189B` | 2 | 0/2 | 0 | 2 |  |
| 410 | 2024-02-12-opal-contracts | Ethereum | GemMinterRebalancingReward | `0x8D6ab8434b66128b78158A2118a645E2BBD05F71` | 2 | 0/2 | 0 | 2 |  |
| 411 | 2024-03-abracadabra-money | Blast | MIMSwap MagicLP (Blast) | `0xeDa89B8b19eBEf5FC0D5e21ebAd174366C230D35` | 2 | 0/2 | 1 | 2 |  |
| 412 | 2024-03-taiko | Ethereum | TaikoToken proxy | `0x10dea67478c5F8c5E2D90e5E9B26dBe60c54d800` | 2 | 0/2 | 2 | 2 | https://github.com/code-423n4/2024-03-taiko-findings/blob/315d303af1791401f23b84 |
| 413 | 2024-07-31-zaros-part-1 | Ethereum | Zaros ZRS token (ERC-20) | `0x75e88B8c2d34a52a6d36deAda664D7dc9116e4EF` | 2 | 0/2 | 0 | 2 |  |
| 414 | 2024-07-loopfi | Ethereum | PoolV3 (ETH lending pool, lpETH) | `0xa684eaf215ad323452e2b2bf6f817d4aa5c116ab` | 2 | 0/2 | 0 | 1 | https://github.com/code-423n4/2024-07-loopfi-findings/blob/2eaf0aa6b0ae2c593f889 |
| 415 | 2024-09-15-final-flayer-audit-report | Base | Listings (ProtectedListings) | `0x11F09e7eeD242FAd875D3565B3D9CA8AADE445ae` | 2 | 0/2 | 0 | 2 |  |
| 416 | 2024-11-27-unizen-sca-unizen-unizen-trade-aggregator-oct2024 | Ethereum | Unizen Trade Aggregator (proxy) | `0xd3f64BAa732061F8B3626ee44bab354f854877AC` | 2 | 0/2 | 0 | 2 |  |
| 417 | 2024-12-02-crowdsourced-defi-security-for-bima-protocol | Ethereum | rsUSBD (BIMA USBD proxy) | `0x7DD12E437C226018A374Bfa2BdAf48340B9942bC` | 2 | 0/2 | 0 | 2 |  |
| 418 | 2025-05-01-alchemix-v3 | Ethereum | Transmuter.claimRedemption (_getTotalUnd | `0x073598132f37756a7E665FB52f1757463120bd3C` | 2 | 0/2 | 0 | 2 | https://cdn.cantina.xyz/reports/cantina_competition_alchemix_may2025.pdf |
| 419 | 2025-05-21-jigsaw-contracts | Ethereum | LiquidationManager | `0x00000001d359f51a4B11D61b81f9bBad02b2b5A7` | 2 | 0/2 | 0 | 2 |  |
| 420 | 2025-09-03-seamless | Base | LeverageRouter | `0xDbA92fC3dc10a17b96b6E807a908155C389A887C` | 2 | 0/2 | 2 | 2 | https://cdn.cantina.xyz/reports/cantina_seamless_sep2025.pdf |
| 421 | 45 Wardens contributed reports to the PoolTogether | Optimism | PrizePool | `0x8CFFFfFa42407DB9DCB974C2C744425c3e58d832` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2023-08-pooltogether-findings/blob/ce185045aa6966a |
| 422 | Ajna | Ethereum | PositionManager | `0x87B0F458d8F1ACD28A83A748bFFbE24bD6B701B1` | 2 | 0/2 | 0 | 2 | https://audits.sherlock.xyz/contests/32 |
| 423 | Ajna | Ethereum | PositionManager / PermitERC721 | `0x87B0F458d8F1ACD28A83A748bFFbE24bD6B701B1` | 2 | 0/2 | 0 | 2 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 424 | Allo Protocol v2 | Ethereum | RFPSimpleStrategy (Allo v2 strategy) | `0x1133eA7Af70876e64665ecD07C0A0476d09465a1` | 2 | 0/2 | 1 | 2 |  |
| 425 | Anchor contest | Terra | ANC token (Terra) | `terra14z56l0fp2lsf86zy3hty2z47ezkhnthtr9yq76` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2022-02-anchor-findings/blob/e3a0ddf7dee187c1a0d40 |
| 426 | Anime Claimer 1 | Ethereum | ANIME token | `0x4DC26fC5854e7648a064a4ABD590bBE71724C277` | 2 | 0/2 | 0 | 2 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 427 | Arrakis V2 core and palm | Ethereum | Arrakis Core Factory v2 | `0xecb8ffcb2369ef188a082a662f496126f66c8288` | 2 | 0/2 | 0 | 1 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 428 | Aspis | Arbitrum | AspisPool | `0x4B950F871997F2f8B9CF1e34EFEE3dEFA849749C` | 2 | 0/2 | 0 | 2 |  |
| 429 | Atlendis Protocol | Ethereum | Atlendis multisig (protocol owner) | `0x7Ec950347ce20F823E033269971eee5bd189DBC0` | 2 | 0/2 | 0 | 2 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 430 | Awesome htlc | Ethereum | SatsBridge (ERC-20) | `0x9ca98c8b217c3B45074834908555D36AF2aC6449` | 2 | 0/2 | 2 | 2 | https://cdn.cantina.xyz/reports/cantina_satsbridge_clneth_january2025.pdf |
| 431 | Axelar Network | Ethereum | AxelarGateway | `0x4F4495243837681061C4743b74B3eEdf548D56A5` | 2 | 0/2 | 2 | 2 | https://github.com/code-423n4/2023-07-axelar-findings/blob/fac80dbd68d9184689e8d |
| 432 | Axis Finance | Ethereum | BatchAuctionHouse | `0xBA000020Fed3cf3bF473f09Ca0A72Ba123e20926` | 2 | 0/2 | 2 | 2 | https://audits.sherlock.xyz/contests/206 |
| 433 | BadgerDAO ibBTC Wrapper contest | Ethereum | WrappedIbbtc / WrappedIbbtcEth | `0x240b150f87445c63467408a8d53947b566a0d1aD` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2021-10-badgerdao-findings/blob/559b9944574bf1026f |
| 434 | Balancer Core | Ethereum | BFactory | `0x9424B1412450D0f8Fc2255FAf6046b98213B76Bd` | 2 | 0/2 | 2 | 2 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 435 | Balancer v3 | Ethereum | Balancer V3 Vault | `0xbA1333333333a1BA1108E8412f11850A5C319bA9` | 2 | 0/2 | 1 | 2 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 436 | Basin | Ethereum | WellUpgradeable (Well implementation dep | `0xBA51AAAA95aeEFc1292515b36D86C51dC7877773` | 2 | 0/2 | 2 | 2 | https://github.com/code-423n4/2024-07-basin-findings/blob/12468792fc3c89de5ea135 |
| 437 | BendDAO Invitational | Ethereum | BendDAO LendPool proxy (V1) | `0x70b97A0da65C15dfb0FFA02aEE6FA36e507C2762` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2024-07-benddao-findings/blob/892e7d324d338e9ff1a5 |
| 438 | Biconomy | Ethereum | Biconomy ERC-4337 Factory 2 (current, ne | `0x000000a56Aaca3e9a4C479ea6b6CD0DBcb6634f5` | 2 | 0/2 | 0 | 2 |  |
| 439 | Biconomy Hyphen 2.0 contest | Ethereum | LiquidityProviders | `0xebab24f13de55789ec1f3ffe99a285754e15f7b9` | 2 | 0/2 | 2 | 1 | https://github.com/code-423n4/2022-03-biconomy-findings/blob/cf79cb6319d3c90236f |
| 440 | Blueberry | Hyperliquid | HyperEvmVault | `0x4bB19336C973506B9405Db586b7AEE302a7CbCFc` | 2 | 0/2 | 2 | 2 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 441 | Blur Exchange contest | Ethereum | BlurExchange | `0x031AA05Da8bf778dFC36D8D25cA68CBB2fC447c6` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2022-10-blur-findings/blob/8137b1b03e070590f12a8af |
| 442 | Canto contest | Canto | WETH (ETH token) | `0x5FD55A1B9FC24967C4dB09C513C3BA0DFa7FF687` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2022-06-canto-findings/blob/a96eaec661f2201f741fe9 |
| 443 | Canto contest | Canto | Note token | `0x4e71A2E537B7f9D9413D3991D37958c0b5e1e503` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2022-06-canto-findings/blob/a96eaec661f2201f741fe9 |
| 444 | Canto contest | Canto | Turnstile | `0xEcf044C5B4b867CFda001101c617eCd347095B44` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2022-11-canto-findings/blob/001eab5dc6066489a02a8b |
| 445 | Chainlink | Ethereum | LINK token (LinkToken) | `0x514910771AF9Ca656af840dff83E8264EcF986CA` | 2 | 0/2 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 446 | Clave Monorepo | zkSync Era | ClaveNameService | `0xA0e1Dcb92681E2cD4037b464E99e74D49Ee6ac9f` | 2 | 0/2 | 0 | 2 | https://cdn.cantina.xyz/reports/cantina_clave_december2024.pdf |
| 447 | Convergence | Moonbeam | CONV token (Moonbeam) | `0x8006320739fC281da67Ee62eB9b4Ef8ADD5C903a` | 2 | 0/2 | 0 | 2 | https://audits.sherlock.xyz/contests/126 |
| 448 | Coordinape | Ethereum | ApeDistributor | `0x987F0d155c08ecA48Bc860461b0DA038b79Eaa68` | 2 | 0/2 | 1 | 2 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 449 | Cork Protocol (Best Efforts contest, v1) | Ethereum | RouterState (FlashSwapRouter) | `0x55B90B37416DC0Bd936045A8110d1aF3B6Bf0fc3` | 2 | 0/2 | 2 | 2 | https://audits.sherlock.xyz/contests/506 |
| 450 | Cover Protocol Peripheral | Ethereum | COVER token | `0x5d8d9f5b96f4438195be9b99eee6118ed4304286` | 2 | 0/2 | 0 | 2 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 451 | Cryptex | Ethereum | Cryptex CTX token | `0x321C2fE4446C7c963dc41Dd58879AF648838f98D` | 2 | 0/2 | 1 | 2 | https://cdn.cantina.xyz/reports/cantina_cryptex_sep2024.pdf |
| 452 | Curve | Ethereum | crvUSD price aggregator | `0x18672b1b0c623a30089A280Ed9256379fb0E4E62` | 2 | 0/2 | 0 | 2 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 453 | DXdao Governance Contracts | Ethereum | dxDAO avatar (governance core) | `0x519b70055af55A007110B4Ff99b0eA33071c720a` | 2 | 0/2 | 1 | 2 | https://github.com/OmegaAudits/audits/blob/a9891e4b8b01650638370d401bc36f81695a3 |
| 454 | Debt DAO contest | Ethereum | SecuredLine (Line of Credit) | `0xc9ef6509a09b92043cedce689dfaa760048abd7f` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2022-11-debtdao-findings/blob/49d520b9e6b1f7733bbd |
| 455 | Defactor March28th | Ethereum | FACTR token (protocol token, not the aud | `0xe0bCEEF36F3a6eFDd5EEBFACD591423f8549B9D5` | 2 | 0/2 | 0 | 2 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 456 | ENS | Ethereum | NameWrapper | `0xD4416b13d2b3a9aBae7AcD5D6C2BbDBE25686401` | 2 | 0/2 | 0 | 2 |  |
| 457 | ENS - Versus contest | Ethereum | NameWrapper | `0xD4416b13d2b3a9aBae7AcD5D6C2BbDBE25686401` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2022-11-ens-findings/blob/744f97a1a954f8a6c2a13d27 |
| 458 | ENS contest | Ethereum | NameWrapper | `0xD4416b13d2b3a9aBae7AcD5D6C2BbDBE25686401` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2022-07-ens-findings/blob/91bb97da647f65a406e91d6d |
| 459 | Ether-Fi - Withdrawal Fee | Ethereum | EtherFiRedemptionManager (2025-10-09 dep | `0xE3F384Dc7002547Dd240AC1Ad69a430CCE1e292d` | 2 | 0/2 | 1 | 2 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 460 | Exactly | Optimism | Market | `0x6926B434CCe9b5b7966aE1BfEef6D0A7DCF3A8bb` | 2 | 0/2 | 0 | 2 | https://github.com/coinspect/publications/blob/01b04f1f4a2e2c4d7e228b967fedb8991 |
| 461 | Exactly Protocol | Optimism | Market | `0x6926B434CCe9b5b7966aE1BfEef6D0A7DCF3A8bb` | 2 | 0/2 | 1 | 2 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 462 | Exit10 | Ethereum | Exit10 | `0xBFD697f71159Ed85eb1A7fE3520Ad8e5d61017fB` | 2 | 0/2 | 0 | 2 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 463 | Fantium | Polygon Mumbai (testnet) | FantiumNFTV1 | `0xb7Dee90E0a9FD3788EB327D9Af8967282C187988` | 2 | 0/2 | 0 | 2 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 464 | Fastlane Atlas | Polygon | AtlasVerification | `0x621c6970fD9F124230feE35117d318069056819a` | 2 | 0/2 | 0 | 0 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 465 | Footium | Ethereum | Footium Football Club (ERC721) | `0x659cf1306eDBA213D1fb8F9352B4593A82B05d0c` | 2 | 0/2 | 0 | 2 | https://audits.sherlock.xyz/contests/71 |
| 466 | ForTube2.0 BOND Smart Contract | Ethereum | PoolPawn (ForTube) | `0xE48BC2Ba0F2d2E140382d8B5C8f261a3d35Ed09C` | 2 | 0/2 | 0 | 2 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 467 | Frax Solidity | Ethereum | FRAXStablecoin | `0x853d955aCEf822Db058eb8505911ED77F175b99e` | 2 | 0/2 | 1 | 2 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 468 | GMX | Arbitrum | ExchangeRouter | `0x1C3fa76e6E1088bCE750f23a5BFcffa1efEF6A41` | 2 | 0/2 | 1 | 1 | https://audits.sherlock.xyz/contests/6 |
| 469 | GlacierAudit | Avalanche | glAVAX | `0x3712871408a829C5cd4e86DA1f4CE727eFCD28F6` | 2 | 0/2 | 0 | 2 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 470 | Goat Tech | Arbitrum Sepolia | Voting | `0x896604b21C6e9CbCE82e096266DCb5798cDDA67B` | 2 | 0/2 | 0 | 2 | https://cdn.cantina.xyz/reports/cantina_competition_goat_mar2024.pdf |
| 471 | Hats | Ethereum | HatsSignerGateBase | `0x0F22eFC6EA47b1EFF42D1A2a6E69440929400F86` | 2 | 0/2 | 0 | 2 | https://audits.sherlock.xyz/contests/48 |
| 472 | Hedge Vault | Solana | USH stablecoin mint (protocol token, not | `5PmpMzWjraf3kSsGEKtqdUsCoLhptg4yriZ17LKKdBBy` | 2 | 0/2 | 0 | 2 | https://osec.io/reports/869f514b-957a-4659-81e2-3e775691a572 |
| 473 | Hydrex | Base | Voter (VoterV5) | `0xc69E3eF39E3fFBcE2A1c570f8d3ADF76909ef17b` | 2 | 0/2 | 0 | 2 |  |
| 474 | Hydrex | Base | VoterV5 | `0xc69E3eF39E3fFBcE2A1c570f8d3ADF76909ef17b` | 2 | 0/2 | 0 | 2 |  |
| 475 | INIT Capital Invitational | Mantle | PosManager | `0x0e7401707CD08c03CDb53DAEF3295DDFb68BBa92` | 2 | 0/2 | 1 | 1 | https://github.com/code-423n4/2023-12-initcapital-findings/blob/7d0603210e012856 |
| 476 | InceptionLRT - Vaults | Ethereum | InceptionVault | `0x99d64871c9848FDA3B3FF1eC2Fc84033401CCd5B` | 2 | 0/2 | 0 | 2 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 477 | Infinex-9 | Ethereum | Infinex Patrons (XPATRON NFT) | `0xB5AF0C7f3885c1007e6699c357566610291585Cb` | 2 | 0/2 | 0 | 2 | https://0xmacro.com/library/audits/infinex-3 |
| 478 | InsurAce | Ethereum | INSUR token | `0x544c42fbb96b39b21df61cf322b5edc285ee7429` | 2 | 0/2 | 0 | 2 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 479 | Jito Restaking | Solana | JTO token mint | `jtojtomepa8beP8AuQc6eXt5FriJwfFMwQx2v2f9mCL` | 2 | 0/2 | 1 | 1 | https://osec.io/reports/15184d4e-4146-80e3-9209-fddf9c04d92e |
| 480 | Juicebox | Ethereum | JBController | `0x4e3ef8AFCC2B52E4e704f4c8d9B7E7948F651351` | 2 | 0/2 | 0 | 2 |  |
| 481 | Karpatkey KPK Shares | Ethereum | KPK Shares | `0xa9C7D1B26454a2F71e5aF6411F7947b973655b05` | 2 | 0/2 | 2 | 2 | https://github.com/OmegaAudits/audits/blob/a9891e4b8b01650638370d401bc36f81695a3 |
| 482 | KittenSwap | Hyperliquid L1 | veKITTEN (VotingEscrow) | `0x29d3a21ff35a519e00cf6d272f2ad897b109bd84` | 2 | 0/2 | 0 | 0 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 483 | Kodiak-2 | Berachain | PandaFactory (graduation/launchpad) | `0xac335fe675699b0ce4c927bdaa572eb647ed9f02` | 2 | 0/2 | 0 | 2 | https://0xmacro.com/library/audits/kodiak-2 |
| 484 | Lido V3 | Ethereum | LazyOracle | `0x5DB427080200c235F2Ae8Cd17A7be87921f7AD6c` | 2 | 0/2 | 0 | 2 | https://diligence.security/audits/2025/08/lido-v3/ |
| 485 | Lista DAO - Lista Lending | BNB Chain | Moolah (Lista Lending) | `0x8f73b65b4caaf64fba2af91cc5d4a2a1318e5d8c` | 2 | 0/2 | 0 | 2 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 486 | Lista Lending - Update | BNB Chain | SlisBNBProvider | `0x33f7a980a246f9b8fea2254e3065576e127d4d5f` | 2 | 0/2 | 2 | 2 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 487 | LooksRare | Ethereum | LooksRareProtocol | `0x0000000000E655fAe4d56241588680F86E3b2377` | 2 | 0/2 | 0 | 2 | https://audits.sherlock.xyz/contests/163 |
| 488 | Magna Voting Escrow Updates | Ethereum | Magna Airlock V2.1 (Ethereum) | `0x052d4671F4AE15E6215fb7135d8c2e3E587b0920` | 2 | 0/2 | 0 | 2 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 489 | Maia DAO - Ulysses | Arbitrum | VirtualAccount | `0x4dBa461cA9342F4A6Cf942aBd7eacf8AE259108C` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2023-09-maia-findings/blob/b3043c4d52ead935f236e4e |
| 490 | Marginswap | Ethereum | MFI token | `0xAa4e3edb11AFa93c41db59842b29de64b72E355B` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2021-04-marginswap-findings/blob/0ce060a6e2876aff1 |
| 491 | Merit Circle | Ethereum | MC token (old Merit Circle token, migrat | `0x949D48EcA67b17269629c7194F4b727d4Ef9E5d6` | 2 | 0/2 | 0 | 2 | https://www.meritcircle.io/Quantstamp-Liquidity-Mining-Audit.pdf |
| 492 | Mimo DeFi contest | Ethereum | PARMiner | `0x6D0a6e30eCeE498f64F77c59e3ddedC02b7d9770` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2022-04-mimo-findings/blob/95141d2aa52279233eabfa7 |
| 493 | MorphL2 | Ethereum | Rollup | `0x759894ced0e6af42c26668076ffa84d02e3cef60` | 2 | 0/2 | 1 | 2 | https://audits.sherlock.xyz/contests/207 |
| 494 | Morpho Blue | Ethereum | Morpho Blue | `0x58D97B57BB95320F9a05dC918Aef65434969c2B2` | 2 | 0/2 | 1 | 2 |  |
| 495 | Nome Protocol Audit | Berachain | Liquide Boardroom | `0x50caa9627a940bcd4d5f3c3ed231252425af50cf` | 2 | 0/2 | 0 | 2 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 496 | Nouns Builder | Ethereum | Token / ERC721Votes | `0xAeD75D1e5c1821E2EC29D5d24b794b13C34c5d63` | 2 | 0/2 | 0 | 2 |  |
| 497 | Oasys | Oasys | SOAS | `0x5200000000000000000000000000000000000002` | 2 | 0/2 | 1 | 2 |  |
| 498 | Ocean Protocol | Ethereum | FixedRateExchange | `0xfa48673a7C36A2A768f89AC1ee8C355D5c367B02` | 2 | 0/2 | 1 | 2 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 499 | Olympus | Ethereum | BLVaultManagerLido | `0xafe729d57d2CC58978C2e01b4EC39C47FB7C4b23` | 2 | 0/2 | 0 | 0 | https://audits.sherlock.xyz/contests/60 |
| 500 | Omni Network Omni SolverNet | Ethereum | SolverNetOutbox | `0xb0dEb4C37720Fa28C9BA2D0a9Cc45d8b449c03FB` | 2 | 0/2 | 1 | 2 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 501 | Ore V2 | Solana | ORE token mint | `oreoU2P8bN6jkk3jbaiVxYnG1dCXcYxwhwyK9jSybcp` | 2 | 0/2 | 0 | 2 | https://docs.fuzz.land/Ore-V2-Audit-Report-d64a0f83e70940718d9f3590ce5e6248 |
| 502 | Panoptic | Ethereum | SFPM.mintTokenizedPosition | `0x0000000000000DEdEDdD16227aA3D836C5753194` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2023-11-panoptic-findings/blob/85bd107fdd5783e8ac5 |
| 503 | ParaSpace contest | Ethereum | ParaProxy (Pool) | `0x638a98BBB92a7582d07C52ff407D49664DC8b3ee` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2022-11-paraspace-findings/blob/9650d134645b411491 |
| 504 | ParaSpace contest | Ethereum | UniswapV3OracleWrapper | `0x71bdC5Ca931Ca9C11C5d19375cA6C0aAe5F5eA5f` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2022-11-paraspace-findings/blob/9650d134645b411491 |
| 505 | Paraswap - September 01, 2021 | Ethereum | SPSP (PSPParaSwapPool3) staking rewards | `0xea02DF45f56A690071022c45c95c46E7F61d3eAb` | 2 | 0/2 | 0 | 2 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 506 | Perpetual | Optimism | ClearingHouse | `0x82ac2CE43e33683c58BE4cDc40975E73aA50f459` | 2 | 0/2 | 1 | 2 | https://audits.sherlock.xyz/contests/219 |
| 507 | Phi | Base | PhiFactory.updateArtSettings | `0xdbe4f7518b0dcb6319a242169c89190e72798b17` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2024-08-phi-findings/blob/0c473d9115cd5a1e90ed5beb |
| 508 | Phi | Base | PhiFactory | `0x6a752405Abd3F7Ec88001F141E0A0FcFbb068502` | 2 | 0/2 | 2 | 2 |  |
| 509 | Playfi | Ethereum | PLAYFI token | `0x82f13aB56Cc0D1b727E8253a943f0DE75B048b0B` | 2 | 0/2 | 0 | 2 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 510 | Prisma Finance | Ethereum | StabilityPool | `0xed8b26d99834540c5013701bb3715fafd39993ba` | 2 | 0/2 | 0 | 2 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 511 | Public - Harmonix Finance | Base | BaseSwap.sol (Base strategy) | `0x45dC73fB760f2382Cfd11e28C0Dd0a3A8d3E4C31` | 2 | 0/2 | 0 | 2 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 512 | Radiant Riz | Arbitrum | Radiant RIZ market (Arbitrum) | `0x3fEc9583827431F622A4b188b6c57CfFE8655b8e` | 2 | 0/2 | 1 | 2 | https://www.openzeppelin.com/news/radiant-riz-audit |
| 513 | Rage Trade | Arbitrum | WithdrawPeriphery | `0x1f73C8955e4dBb9E863261Fa4E6d359e9200E525` | 2 | 0/2 | 1 | 2 | https://audits.sherlock.xyz/contests/16 |
| 514 | RaisinLabs | Ethereum | DIVA diamond | `0x2C9c47E7d254e493f02acfB410864b9a86c28e1D` | 2 | 0/2 | 0 | 2 | https://github.com/GuardianAudits/DefenderAudits/blob/b2a2ccb9b6e07d82a6c4497fee |
| 515 | Redacted Cartel contest | Arbitrum | AutoPxGmx | `0xA0397347bBf8d6BA4A22dF1AA002b54286828775` | 2 | 0/2 | 2 | 2 | https://github.com/code-423n4/2022-11-redactedcartel-findings/blob/60e3bf7d92a0f |
| 516 | Ref Finance | NEAR | Ref Finance v1 AMM | `ref-finance.near` | 2 | 0/2 | 2 | 2 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 517 | Ref-Exchange, | NEAR | ref-exchange | `v2.ref-finance.near` | 2 | 0/2 | 1 | 2 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 518 | Retro/Thena | BNB Chain | THE (Thena token) | `0xF4C8E32EaDEC4BFe97E0F595AdD0f4450a863a11` | 2 | 0/2 | 0 | 2 | https://www.openzeppelin.com/news/retro-thena-audit |
| 519 | Revert Lend | Base | V3Vault | `0x36AEAe0E411a1E28372e0d66f02E57744EbE7599` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2024-03-revert-lend-findings/blob/5fd5466a646d1870 |
| 520 | Revert Lend | Base | V3Utils | `0x2309A5aE06e86986a6f27b81a53cC31Fc1B55b0a` | 2 | 0/2 | 2 | 2 | https://github.com/code-423n4/2024-03-revert-lend-findings/blob/5fd5466a646d1870 |
| 521 | Rubicon v2 | Optimism | BathToken (bathUSDC) | `0xe0e112e8f33d3f437D1F895cbb1A456836125952` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2022-05-rubicon-findings/blob/89ab16511eb6864d5c54 |
| 522 | Rubicon v2 | Optimism | RubiconMarket | `0x7a512d3609211e719737E82c7bb7271eC05Da70d` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2023-04-rubicon-findings/blob/d735f3d7b04f5369e6e8 |
| 523 | Salty.IO | Ethereum | Salty Pools | `0xf5D65d370141f1fff0Db646c9406Ce051354A8a5` | 2 | 0/2 | 0 | 2 | https://github.com/code-423n4/2024-01-salty-findings/blob/124cf3d332c1d74705c294 |
| 524 | Sense | Ethereum | AutoRoller (deployed per-series by AutoR | `0x3B0f35bDD6Da9e3b8513c58Af8Fdf231f60232E5` | 2 | 0/2 | 2 | 2 | https://audits.sherlock.xyz/contests/19 |
| 525 | Sense | Ethereum | Divider | `0x86bA3E96Be68563E41c2f5769F1AF9fAf758e6E0` | 2 | 0/2 | 0 | 2 | https://audits.sherlock.xyz/contests/19 |
| 526 | Sentiment | Hyperliquid | Pool / RiskModule (v2) | `0x36BFD6b40e2c9BbCfD36a6B1F1Aa65974f4fFA5D` | 2 | 0/2 | 2 | 2 | https://audits.sherlock.xyz/contests/349 |
| 527 | Sentiment | Arbitrum | Controller / LToken (v1) | `0x17b07cfbab33c0024040e7c299f8048f4a49679b` | 2 | 0/2 | 2 | 2 | https://audits.sherlock.xyz/contests/1 |
| 528 | Sentiment | Hyperliquid | Pool (v2) | `0x36BFD6b40e2c9BbCfD36a6B1F1Aa65974f4fFA5D` | 2 | 0/2 | 1 | 2 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 529 | SilverSwap | Sonic | SilverSwap core (DEX) | `0x005851f943ee2957B1748957F26319e4f9EdeBC1` | 2 | 0/2 | 2 | 2 |  |
| 530 | SingularityAudit | Arbitrum | UniswapLiquidityAssetManager | `0x9D4746F8f2364da04fF47d729072F71b742726aA` | 2 | 0/2 | 0 | 2 | https://github.com/threesigmaxyz/publications/blob/2f7ea0cf2efa42ae5c4364359cb3f |
| 531 | Sofa (May | Ethereum | AAVESmartTrendVault | `0x1D2fAAd42cbF3Dc121659d856A9A405ED1067873` | 2 | 0/2 | 0 | 2 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 532 | Succinct Labs Telepathy | Ethereum | TelepathyRouter | `0xa0064e9B97855835f6D99Df75d92eac6e8f929fE` | 2 | 0/2 | 0 | 2 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 533 | Super DCA Liquidity Network | Optimism | SuperDCAPoolV1 | `0xb1ad101f99ea4adfc654733d58855c4236020c17` | 2 | 0/2 | 0 | 2 | https://audits.sherlock.xyz/contests/1171 |
| 534 | Superform Core | Ethereum | SuperExecutor | `0x9cC8EDCC41154aaFC74D261aD3D87140D21F6281` | 2 | 0/2 | 0 | 2 |  |
| 535 | SwapX - Staking/Airdrop/Vesting/Token | Sonic | SWPX token | `0xa04bc7140c26fc9bb1f36b1a604c7a5a88fb0e70` | 2 | 0/2 | 1 | 2 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 536 | Symmetrical (now SYMMIO) | Arbitrum | Symmio diamond (Symmetrical perps core) | `0x57331027091994FCb9c5Aec48ea92cEf0a93CF6A` | 2 | 0/2 | 0 | 2 |  |
| 537 | Taiko Protocol | Taiko | TaikoL2.init() | `0x1670000000000000000000000000000000010001` | 2 | 0/2 | 1 | 2 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 538 | Takara Lend Contracts | Sei | Comptroller | `0x56A171Acb1bBa46D4fdF21AfBE89377574B8D9BD` | 2 | 0/2 | 0 | 2 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 539 | TeaREX | Sei | TradingCore | `0xedf7732991b3de8f46fb97dcd4c5cdb28e6ad859` | 2 | 0/2 | 0 | 2 | https://github.com/sec3-service/reports/blob/13c2f82d576164c7db728108d09a8d37272 |
| 540 | TermMax | Ethereum | TermMaxMarket | `0x37Ba9934aAbA7a49cC29d0952C6a91d7c7043dbc` | 2 | 0/2 | 0 | 2 |  |
| 541 | Thesis - tBTC and keep | Ethereum | TBTCSystem/Deposit state transitions | `0x41A1b40c1280883eA14C6a71e23bb66b83B3fB59` | 2 | 0/2 | 0 | 2 | https://diligence.security/audits/2020/02/thesis-tbtc-and-keep/ |
| 542 | Tigris Trade contest | Polygon | Trading.addToPosition | `0x28c5d4416f6cf0FC5F557067b54BD67a43fcC98F` | 2 | 0/2 | 1 | 1 | https://github.com/code-423n4/2022-12-tigris-findings/blob/e5a0c7faf68116af201f8 |
| 543 | Tinyman 1.1 Update | Algorand | Tinyman v1.1 Validator App | `552635992` | 2 | 0/2 | 2 | 2 | https://github.com/coinspect/publications/blob/01b04f1f4a2e2c4d7e228b967fedb8991 |
| 544 | Tokemak | Ethereum | SystemRegistry (gen1 mainnet) | `0x0406d2D96871f798fcf54d5969F69F55F803eEA4` | 2 | 0/2 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 545 | USG - Tangent | Ethereum | USG stablecoin | `0xB1c2Db5d6cA03FCe73dBd304d320bF76C55Ae1B1` | 2 | 0/2 | 0 | 2 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 546 | USSD | Ethereum | USSD stablecoin (Autonomous Secure Dolla | `0x97D87327D8F168b0Ba317fd8B210d2B087f4b851` | 2 | 0/2 | 1 | 2 |  |
| 547 | Vallarok | Ethereum | RunaAGI.whitelistMint()/FCFSMint() | `0x9d21650745B593A488f8F0D84ADe822889221AB7` | 2 | 0/2 | 1 | 2 | https://github.com/shieldify-security/audits-portfolio-md/blob/f2c051af4ffb67e11 |
| 548 | Velodrome Finance | Optimism | CLGauge (implementation) | `0xb5f7bd1C65437F789b62CBE98eF16cd9f1fc4b26` | 2 | 0/2 | 1 | 2 | https://cdn.cantina.xyz/reports/Velodrome-Spearbit-Security-Review-Nov23.pdf |
| 549 | Virtuals Protocol AI Agents | Base | Virtuals bonding curve (Base) | `0x1A540088125d00dD3990f9dA45CA0859af4d3B01` | 2 | 0/2 | 1 | 2 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 550 | Whale.Loans | BNB Chain | HUMP token | `0x453939C0270e9405876C7f047aDE3932FD2d7a51` | 2 | 0/2 | 1 | 2 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 551 | XSY | Avalanche | XSY core | `0xdbc5192a6b6ffee7451301bb4ec312f844f02b4a` | 2 | 0/2 | 1 | 2 | https://cdn.cantina.xyz/reports/cantina_xsy_sep2025.pdf |
| 552 | YG | Base | MORE Vaults Composer | `0x8D8BE034eCfD018D67F9a1A25E27f99f52CBdFC1` | 2 | 0/2 | 2 | 2 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 553 | Yield Basis DAO | Ethereum | YB token | `0x01791f726b4103694969820be083196cc7c045ff` | 2 | 0/2 | 1 | 2 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 554 | YuzuUSD | Plasma | yzUSD stablecoin | `0x6695c0f8706C5ACe3Bdf8995073179cCA47926dc` | 2 | 0/2 | 1 | 2 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 555 | eigenlayer | Ethereum | EigenPod / EigenPodManager | `0x91E677b07F7AF907ec9a428aafA9fc14a0d3A338` | 2 | 0/2 | 2 | 2 | https://github.com/code-423n4/2023-04-eigenlayer-findings/blob/cb13576fd42c38087 |
| 556 | ethereum reserve dollar erd | Ethereum | USDE token proxy (USDEToken) | `0x1d00e86748573c322f4cc41518aa0e77bd912eb4` | 2 | 0/2 | 0 | 1 |  |
| 557 | ethereumcreditguild | Ethereum | ProfitManager | `0x410cc76477D26B1582BE9E8E829f25738b19FB62` | 2 | 0/2 | 2 | 2 |  |
| 558 | flat-money | Optimism | Flat Money V2 Market Maker | `0x1C57f6769FB3e51E65ad24c8c12DBd956EA716b6` | 2 | 0/2 | 0 | 2 | https://audits.sherlock.xyz/contests/132 |
| 559 | for Alien Base | Base | EpsilonRouter (DCA fill) | `0x303ca5c65AabCb1CE242DF93F478c41E0E4D2580` | 2 | 0/2 | 0 | 2 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 560 | for Zharta | Ethereum | ZhartaLending (P2PLendingBase.vy) | `0x6209A1b9751F67594427a45b5225bC3492009788` | 2 | 0/2 | 0 | 2 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 561 | hashlock-dione-2023-12-dione-smart-contract-audit-final-repo | Ethereum | DIONE token | `0x89b69f2d1adffa9a253d40840b6baa7fc903d697` | 2 | 0/2 | 0 | 2 |  |
| 562 | hashlock-hikari-finance-2025-08-hikari-finance-smart-contrac | Katana | BasePriceAUSD | `0xC2473b16fE99BE558Cd246cC3B610574534EfDB9` | 2 | 0/2 | 2 | 2 |  |
| 563 | hashlock-kingdomly-2024-08-kingdomly-staking-smart-contract- | Ethereum | Kingdomly collection factory | `0x07b429f9dd10c3e6fa98467239df973633bb3fb3` | 2 | 0/2 | 2 | 2 |  |
| 564 | hashlock-openzk-2025-02-openzk-updated-smart-contract-securi | Ethereum | OZKToken | `0x737d461917ccf0fa28a52da30672e2ddc214f0bf` | 2 | 0/2 | 0 | 2 |  |
| 565 | ichi ichi | Ethereum | OneTokenFactory / oneToken | `0xD0092632B9Ac5A7856664eeC1abb6E3403a6A36a` | 2 | 0/2 | 2 | 2 |  |
| 566 | infinity | Ethereum | InfinityExchange | `0x3643e1f18E98B7dcaa199Ee64685040C764ca454` | 2 | 0/2 | 1 | 2 |  |
| 567 | kwenta-zap-octopus-release | Optimism | Kwenta (KWENTA) token | `0x920Cf626a271321C151D027030D5d08aF699456b` | 2 | 0/2 | 0 | 2 | https://www.iosiro.com/audits/kwenta-zap-octopus-release-smart-contract-audit |
| 568 | loxodrome | IoTeX | Loxodrome (LOXO) token | `0x2ff90ca1a004f8900ab498259fc4e148e39331fd` | 2 | 0/2 | 0 | 2 | https://fuzzland.notion.site/loxodrome-Audit-Report-9586f0f2699b4d1696782b523179 |
| 569 | magpie eigenpie v1.4 | Ethereum | EigenpieStaking | `0x4eF7F34Bb1CD7d1E82181274A0896e2CCaC774bE` | 2 | 0/2 | 0 | 2 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 570 | pashov-team-2024-07-22-gainsnetwork-security-review-may | Arbitrum | GNSMultiCollatDiamond | `0xFF162c694eAA571f685030649814282eA457f169` | 2 | 0/2 | 0 | 2 |  |
| 571 | pashov-team-2024-09-29-karak-security-review-june | Ethereum | Karak Delegation Supervisor (proxy) | `0xafa904152e04abff56701223118be2832a4449e0` | 2 | 0/2 | 1 | 2 |  |
| 572 | pashov-team-2025-02-26-kinetiq-security-review | Hyperliquid L1 | KNTQ governance token (protocol token, n | `0x000000000000780555bd0bca3791f89f9542c2d6` | 2 | 0/2 | 0 | 2 |  |
| 573 | pashov-team-2025-03-12-blueberry-security-review | Hyperliquid L1 | bbHLP | `0x4bB19336C973506B9405Db586b7AEE302a7CbCFc` | 2 | 0/2 | 1 | 2 |  |
| 574 | persistence-stkbnb- -april- ( ) (1 | BNB Chain | stkBNB (Staked BNB) | `0xc2E9d07F66A89c44062459A47a0D2Dc038E4fb16` | 2 | 0/2 | 0 | 2 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 575 | reNFT | Ethereum | Stop policy | `0xFfcF66DE71f13a4823334917A4D5a22302854D3A` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2024-01-renft-findings/blob/273c1d163a81a8b5cd09c0 |
| 576 | templegold | Ethereum | TempleGoldStaking | `0x64866d080CfEf0e45A3a64A558dA6eEAD7542657` | 2 | 0/2 | 0 | 2 |  |
| 577 | vvv-launchpad-investments-token-distribution | Base | VVVVCTokenDistributor.claim | `0xF0F49eE0431f6341eC01CC29f209d0a330731253` | 2 | 0/2 | 0 | 2 | https://audits.sherlock.xyz/contests/647 |
| 578 | wXTZ | Tezos | wXTZ | `KT1VYsVfmobT7rsMVivvZ4J8i3bPiqz12NaH` | 2 | 0/2 | 2 | 2 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 579 | wake-arena-ai--ipor-labs-fusion-dec-11 | Ethereum | PlasmaVault (live instance) | `0xeef16982403a89bcbf16dff050a5ba5b86a02c8a` | 2 | 0/2 | 1 | 2 | https://github.com/Ackee-Blockchain/public-wake-arena-reports/blob/e6553332fd1e5 |
| 580 | yAcademy GET Protocol Staking | Ethereum | GET staking (withdraw/cancel requests) | `0x3e49E9C890Cd5B015A18ed76E7A4093f569f1A04` | 2 | 0/2 | 0 | 2 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 581 | yAxis contest | Ethereum | Vault.withdraw | `0x9720346Ba80b668E50A5560c200180515fEbb895` | 2 | 0/2 | 1 | 2 | https://github.com/code-423n4/2021-09-yaxis-findings/blob/294b98fb39255dde574836 |
| 582 | yPrisma | Ethereum | YearnBoostedStaker | `0xF4C6e0E006F164535508787873d86b84fe901975` | 2 | 0/2 | 0 | 2 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 583 | zkSwap Finance | zkSync Era | ZFToken | `0x31C2c031fDc9d33e974f327Ab0d9883Eae06cA4A` | 2 | 0/2 | 0 | 2 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 584 | 01--SOFA | Ethereum | CrvUSDDualVault.mint / burn | `0x060c233146EaED1EfF8BeF320AAa224377bF76d3` | 1 | 1/0 | 1 | 1 | https://github.com/yAudit/reports-pdf/blob/186eab01a540d4815784bf79356dc7bcf4422 |
| 585 | 02 12 Whetstone Doppler-MR | Ethereum | UniswapV2Migrator | `0xd7aba5f1d80a330a6fe9e96f7ba122710e0912d3` | 1 | 1/0 | 1 | 0 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 586 | 04 08 Seamless ILM-FV-MR | Base | LeverageManager / LoanLogic | `0x38Ba21C6Bf31dF1b1798FCEd07B4e9b07C5ec3a8` | 1 | 1/0 | 1 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 587 | 06 08 Lyra Option Market-FV | Optimism | OptionMarket | `0xf3840a31bD84EFBEaC057d80eb1fA03dCdA0374b` | 1 | 1/0 | 1 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 588 | 07 01 Compound Comet-FV | Ethereum | Comet.transferBase | `0xc3d688B66703497DAA19211EEdff47f25384cdc3` | 1 | 1/0 | 1 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 589 | 07 01 Compound Comet-FV | Ethereum | Comet.transferCollateral | `0xc3d688B66703497DAA19211EEdff47f25384cdc3` | 1 | 1/0 | 1 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 590 | 07 01 Compound Comet-FV | Ethereum | Comet.principalValue | `0xc3d688B66703497DAA19211EEdff47f25384cdc3` | 1 | 1/0 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 591 | 0x_audit_report_2018-07-23 | Ethereum | Exchange | `0x61935cbdd02287b511119ddb11aeb42f1593b7ef` | 1 | 1/0 | 1 | 1 | https://github.com/ConsenSysDiligence/0x_audit_report_2018-07-23/blob/35acafa94e |
| 592 | 11 27 Balancer V3-FV-MR | Ethereum | Balancer V3 Vault (ERC4626 buffer) | `0xbA1333333333a1BA1108E8412f11850A5C319bA9` | 1 | 1/0 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 593 | 12--LlamaPay-V2 | Ethereum | LlamaPayFactory | `0xde1C04855c2828431ba637675B6929A684f84C7F` | 1 | 1/0 | 1 | 1 | https://github.com/yAudit/reports-pdf/blob/186eab01a540d4815784bf79356dc7bcf4422 |
| 594 | 1inch | Ethereum | St1inch (ERC20Delegatable staking token) | `0x9A0C8Ff858d273f57072D714bca7411D717501D7` | 1 | 1/0 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 595 | 1inch | Ethereum | St1inch (ERC20Delegatable) | `0x9A0C8Ff858d273f57072D714bca7411D717501D7` | 1 | 1/0 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 596 | 2020-09-19-strongblock-sca-strongblock-defi-sep2020-sca-stro | Ethereum | sbStrongPool | `0xdf66e55288507987ECec74d64Ae26F0a9833AC6e` | 1 | 1/0 | 0 | 1 |  |
| 597 | 2020-12-16-yvs-finance-sca-yvs-finance-erc20-staki | Ethereum | YvsVault | `0x981cc277841f06401B750a3c7dd42492ff962B9C` | 1 | 1/0 | 0 | 1 |  |
| 598 | 2021-04-08-tosdis-finance-sca-tosdis-erc20-apr2021 | Ethereum | collectFee() | `0x6Df569d95ee0Dd3C12AbfFaA867CFd94f1702Ad4` | 1 | 1/0 | 0 | 1 |  |
| 599 | 2021-07-connext-nxtp-noncustodial-xchain-transfer- | Ethereum | TransactionManager.removeLiquidity | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 1/0 | 1 | 1 |  |
| 600 | 2021-10-08-centrality-sca-centrality-bridge-oct202 | Ethereum | CENNZnetBridge | `0x369e2285CCf43483e76746cebbf3d1d6060913EC` | 1 | 1/0 | 1 | 1 |  |
| 601 | 2021-10-08-centrality-sca-centrality-bridge-oct202 | Ethereum | ERC20Peg | `0x8F68fe02884b2B05e056aF72E4F2D2313E9900eC` | 1 | 1/0 | 0 | 1 |  |
| 602 | 2022-02-25-grizzly-fi-sca-grizzly-fi-erc20-feb2022 | BNB Chain | GrizzlyFi ERC20 / Hive | `0xa045e37a0d1dd3a45fefb8803d22457abc0a728a` | 1 | 1/0 | 0 | 1 |  |
| 603 | 2022-03-fuji-protocol | Fantom | FlasherFTM.onFlashLoan via ICTokenFlashl | `0xc3552fb76F3C013eCbED1a064d80Bf721F6BC481` | 1 | 1/0 | 0 | 1 | https://diligence.consensys.io/audits/2022/03/fuji-protocol/fuji-protocol-audit- |
| 604 | 2022-03-fuji-protocol | Fantom | ICTokenFlashloan.flashLoan / FlasherFTM. | `0xc3552fb76F3C013eCbED1a064d80Bf721F6BC481` | 1 | 1/0 | 1 | 1 |  |
| 605 | 2022-09-20-hyperlane-sca-abacus-interchain-message | Ethereum | Mailbox (Abacus) | `0xc005dc82818d67AF737725bD4bf75435d065D239` | 1 | 1/0 | 1 | 1 |  |
| 606 | 2022-10-01-singularitydao-sca-sdao-lp-tokens-system-sep2022- | Ethereum | SingularityDAO (SDAO) token | `0x993864E43Caa7F7F12953AD6fEb1d1Ca635B875F` | 1 | 1/0 | 0 | 1 |  |
| 607 | 2022-11-16-titi-protocol-sca-titi-finance-erc20-mm | Ethereum | MAMMSwapPair / MarketMakerFund | `0x49a0c2076DE4801bcadFEf78d0FA63cEC0AD1cB4` | 1 | 1/0 | 1 | 1 |  |
| 608 | 2023-03-20-v2-core | Ethereum | SablierV2Lockup (streamedAmountOf/withdr | `0xB10daee1FCF62243aE27776D7a92D39dC8740f95` | 1 | 1/0 | 0 | 1 |  |
| 609 | 2023-03-27-cozy-protocol-v2 | Optimism | Set.claimSetFees / Manager.claimSetFees | `0x17705474203F7ff7ba8a940c433AB43D1F58E249` | 1 | 1/0 | 1 | 1 |  |
| 610 | 2023-03-27-cozy-protocol-v2 | Optimism | Set.sell() | `0x17705474203F7ff7ba8a940c433AB43D1F58E249` | 1 | 1/0 | 0 | 1 |  |
| 611 | 2023-04-28-clearpool-finance-sca-clearpool-lending | Ethereum | Auction | `0x5f04bC575a407DBa3129EA45180b1e6573a4F91A` | 1 | 1/0 | 0 | 1 |  |
| 612 | 2023-06-24-venus-sca-venus-dex-may2023-sca-venus-dex-may2023 | BNB Chain | Venus Core Pool Comptroller | `0xfD36E2c2a6789Db23113685031d7F16329158384` | 1 | 1/0 | 0 | 1 |  |
| 613 | 2023-11-11-vaultka-sca-vaultka-erc20-staking-nov20 | Arbitrum | Vaultka Treasury | `0x9bb5020EC1e42E4eF32d634F595734F7cA9F0EA4` | 1 | 1/0 | 0 | 1 |  |
| 614 | 2023-12-26-common-wealth-sca-common-wealth-erc721- | Base | WLTH token | `0x99b2B1A2aDB02B38222ADcD057783D7e5D1FCC7D` | 1 | 1/0 | 0 | 1 |  |
| 615 | 2023-12-26-common-wealth-sca-common-wealth-erc721-nov2023-sc | Base | Common Wealth ERC721 (releasePerNFT) | `0x99b2B1A2aDB02B38222ADcD057783D7e5D1FCC7D` | 1 | 1/0 | 0 | 1 |  |
| 616 | 2024-01-09-genie-swap-sca-genie-swap-farm-dec2023- | Ethereum | GenieSwap farming (extendLockTime) | `0x0a267cF51EF038fC00E71801F5a524aec06e4f07` | 1 | 1/0 | 0 | 1 |  |
| 617 | 2024-02-14-magic-spend | Ethereum | MagicSpend | `0x011A61C07DbF256A68256B1cB51A5e246730aB92` | 1 | 1/0 | 0 | 1 |  |
| 618 | 2024-04-12-common-wealth-sca-common-wealth-vesting | Base | WLTH token (ex Common Wealth) | `0x99b2B1A2aDB02B38222ADcD057783D7e5D1FCC7D` | 1 | 1/0 | 1 | 1 |  |
| 619 | 2024-04-16-mantle-v2-solidity-contracts-audit | Ethereum | L1CrossDomainMessenger / L1StandardBridg | `0x676A795fe6E43C17c668de16730c3F690FEB7120` | 1 | 1/0 | 0 | 1 |  |
| 620 | 2024-04-29-sigmaprime-aave-aave-safetymodule-revie | Ethereum | stkAAVE (StakedTokenV3) | `0x4da27a545c0c5B758a6BA100e3a049001de870f5` | 1 | 1/0 | 1 | 1 |  |
| 621 | 2024-04-29-sigmaprime-gearbox-review | Ethereum | CreditFacade | `0xd4fe3eD38250C38A0094224C4B0224b5D5d0e7d9` | 1 | 1/0 | 1 | 1 |  |
| 622 | 2024-04-29-sigmaprime-gearbox-review | Ethereum | CreditManager / Pool | `0xC38478B0A4bAFE964C3526EEFF534d70E1E09017` | 1 | 1/0 | 0 | 1 |  |
| 623 | 2024-04-29-sigmaprime-sushi-auction-maker-furo-rev | Ethereum | FuroVesting | `0x0689640d190b10765f09310fCfE9C670eDe4E25B` | 1 | 1/0 | 0 | 1 |  |
| 624 | 2024-04-29-sigmaprime-sushi-auction-maker-furo-rev | Ethereum | FuroStream.updateStream | `0x4ab2FC6e258a0cA7175D05fF10C5cF798A672cAE` | 1 | 1/0 | 0 | 1 |  |
| 625 | 2024-04-29-sigmaprime-sushi-bentobox-strategies-st | Ethereum | BentoBox | `0xF5BCE5077908a1b7370B9ae04AdC565EBd643966` | 1 | 1/0 | 1 | 1 |  |
| 626 | 2024-06-24-jellyverse-sca-jellyverse-governor-apr2 | Sei | Jellyverse Vault (governor/staking) | `0xFB43069f6d0473B85686a85F4Ce4Fc1FD8F00875` | 1 | 1/0 | 1 | 1 |  |
| 627 | 2024-06-24-panoptic-audit | Ethereum | SFPM/PanopticPool roll share accounting | `0x0000000000000DEdEDDd16227aA3D836C5753194` | 1 | 1/0 | 0 | 1 |  |
| 628 | 2024-06-24-panoptic-audit | Ethereum | PanopticPool.transferFrom / withdraw wit | `0x0000000000035D9945Bf4d24393828e920376bAe` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/panoptic-audit |
| 629 | 2024-06-24-panoptic-audit | Ethereum | PanopticPool.transferFrom / maxWithdraw  | `0x0000000000035D9945Bf4d24393828e920376bAe` | 1 | 1/0 | 0 | 1 |  |
| 630 | 2024-06-24-panoptic-audit | Ethereum | SFPM tokenId validation on roll | `0x0000000000000DEdEDDd16227aA3D836C5753194` | 1 | 1/0 | 0 | 1 |  |
| 631 | 2024-08-23-sigmaprime-kelp-lrt-withdrawals-review | Ethereum | LRTWithdrawalManager | `0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16` | 1 | 1/0 | 0 | 1 |  |
| 632 | 2024-08-27-uniswap-v4-core-audit | Ethereum | PoolManager / native currency accounting | `0x000000000004444c5dc75cB358380D2e3dE08A90` | 1 | 1/0 | 1 | 1 |  |
| 633 | 2024-08-28-royco-monorepo | Ethereum | Royco market tranche (ERC20 transfer pat | `0x63da1229be88fb4d20210147954a1a3e05f2581b` | 1 | 1/0 | 0 | 1 |  |
| 634 | 2024-08-30-uniswap-v4-periphery-and-universal-rout | Ethereum | PositionManager | `0xbD216513d74C8cf14cf4747E6AaA6420FF64ee9e` | 1 | 1/0 | 1 | 1 |  |
| 635 | 2024-09-04-sigmaprime-derive-review | Arbitrum | DutchAuction | `0xeB8d770ec18DB98Db922E9D83260A585b9F0DeAD` | 1 | 1/0 | 0 | 1 |  |
| 636 | 2024-09-04-sigmaprime-derive-review | Arbitrum | subAccounts / Matching | `0xeB8d770ec18DB98Db922E9D83260A585b9F0DeAD` | 1 | 1/0 | 0 | 1 |  |
| 637 | 2024-09-09-level-money-contracts | Ethereum | LevelMinting.mint / initiateRedeem / red | `0x8E7046e27D14d09bdacDE9260ff7c8c2be68a41f` | 1 | 1/0 | 1 | 1 |  |
| 638 | 2024-09-09-level-money-contracts | Ethereum | LevelMinting.mintDefault | `0x8E7046e27D14d09bdacDE9260ff7c8c2be68a41f` | 1 | 1/0 | 0 | 1 |  |
| 639 | 2024-09-09-level-money-contracts | Ethereum | LevelMinting.initiateRedeem / completeRe | `0x8E7046e27D14d09bdacDE9260ff7c8c2be68a41f` | 1 | 1/0 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_level_money_sep2024.pdf |
| 640 | 2024-10-17-coinbase-spend-permissions-contract-aud | Base | SpendPermissionManager (ERC-6492 approva | `0xf85210B21cC50302F477BA56686d2019dC9b67Ad` | 1 | 1/0 | 1 | 1 |  |
| 641 | 2024-10-17-coinbase-spend-permissions-contract-aud | Base | SpendPermissionManager / CoinbaseSmartWa | `0xf85210B21cC50302F477BA56686d2019dC9b67Ad` | 1 | 1/0 | 1 | 1 |  |
| 642 | 2024-12-17-credbull-sca-credbull-credbull-defi-oct | Arbitrum | MultiTokenVault | `0xD6b3d81868770083307840F513A3491960b95cb6` | 1 | 1/0 | 1 | 1 |  |
| 643 | 2025-01-02-zoth-sca-zoth-zeusd-contracts-dec2024-s | Ethereum | ZeUSD (burn -> SubVault payout) | `0x7DC9748DA8E762e569F9269f48F69A1a9F8Ea761` | 1 | 1/0 | 1 | 1 |  |
| 644 | 2025-05-12-across-protocol-svm-solidity-audit | Solana | SVM SpokePool (relayer refund path) | `DLv3NggMiSaef97YCkew5xKUHDh13tVGZ7tydt3ZeAru` | 1 | 1/0 | 0 | 1 |  |
| 645 | AAVE AAVE Safety Module | Ethereum | StakedTokenV3 (stkAAVE) | `0x4da27a545c0c5B758a6BA100e3a049001de870f5` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 646 | Across Protocol SVM Solidity | Solana | SVM SpokePool | `DLv3NggMiSaef97YCkew5xKUHDh13tVGZ7tydt3ZeAru` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/across-protocol-svm-solidity-audit |
| 647 | Aftermath Finance Perpetuals | Sui | iperps-vaults | `0xbab1b714c5533a46ee27a9c124d6f9281ca54831fc288d4d0c133dae3a57254a` | 1 | 1/0 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/5d5026fffcc3be6ce5f4a7b38b9a83af |
| 648 | Aftermath Finance Perpetuals | Sui | iperps (position) | `0x3ec740df8428aa9c93aaef7f8cc1542ac3194fd014826b51bfe245346d64efc7` | 1 | 1/0 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/5d5026fffcc3be6ce5f4a7b38b9a83af |
| 649 | Akropolis VESTING SMART CONTRACT | Ethereum | KAON (ex-AKRO) token | `0x8Ab7404063Ec4DBcfd4598215992DC3F8EC853d7` | 1 | 1/0 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 650 | Algebra | Polygon | AlgebraPool | `0x411b0fAcC3489691f28ad58c47006AF5E3Ab3A28` | 1 | 1/0 | 1 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 651 | Ante | Ethereum | AntePool (instance) | `0x3347079E0B99bf7Bbb9B4463c6532ED6b1e5Ef16` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 652 | Anvil Protocol | Ethereum | ANVL token | `0xAEEAa594e7dc112D67b8547fe9767a02c15B5597` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/anvil-protocol-audit |
| 653 | Aries Market | Aptos | Aries lending package (reserve/controlle | `0x9770fa9c725cbd97eb50b2be5f7416efdfd1f1554beb0750d4dae4c64e860da3` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/831b03ba-023b-4d31-aba5-cab4aa0bf233 |
| 654 | Astaria | Ethereum | AstariaRouter | `0x42CDc5D4B05E8dACc2FCD181cbe0Cc86Ee14c439` | 1 | 1/0 | 1 | 0 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 655 | Astaria | Ethereum | CollateralToken | `0x6112d87127847202151b9fe48ea0e2704fa428a1` | 1 | 1/0 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 656 | Astroport | Terra | Maker (astroport-maker) | `terra1ygcvxp9s054q8u2q4hvl52ke393zvgj0sllahlycm4mj8dm96zjsa45rzk` | 1 | 1/0 | 1 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 657 | Astroport | Terra | Maker (astroport-maker 2.0.0) | `terra1ygcvxp9s054q8u2q4hvl52ke393zvgj0sllahlycm4mj8dm96zjsa45rzk` | 1 | 1/0 | 1 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 658 | Astroport | Terra | Generator / Incentives | `terra1eywh4av8sln6r45pxq45ltj798htfy0cfcf7fy3pxc2gcv6uc07se4ch9x` | 1 | 1/0 | 1 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 659 | Astroport Incentives | Neutron | astroport-incentives (Neutron) | `neutron173fd8wpfzyqnfnpwq2zhtgdstujrjz2wkprkjfr6gqg4gknctjyq6m3tch` | 1 | 1/0 | 1 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 660 | Astroport Transmuter Pool | Neutron | Astroport factory (Neutron) | `neutron1hptk0k5kng7hjy35vmh009qd5m6l33609nypgf2yc6nqnewduqasxplt4e` | 1 | 1/0 | 1 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 661 | Asymmetry-USA-d | Ethereum | WbtcOracle | `0x455666d7c8DF852C9575b2c91C4c42F03726D902` | 1 | 1/0 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 662 | Axelar Network Audit | Ethereum | AxelarGateway | `0x4F4495243837681061C4743b74B3eEdf548D56A5` | 1 | 1/0 | 1 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 663 | Axiom | Ethereum | AxiomV2Core (transaction circuit) | `0x69963768F8407dE501029680dE46945F838Fc98B` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 664 | Axiom | Ethereum | AxiomV2Core (rlp(idx) circuit) | `0x69963768F8407dE501029680dE46945F838Fc98B` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 665 | Aztec Rollup Contracts | Ethereum | Outbox | `0xFD2a12658A82d7156DA56c7A8d49A69fC966c8D1` | 1 | 1/0 | 1 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 666 | Azuro V2 LiveCore | Polygon | LiveCore (oracle validation) | `0x7043E4e1c4045424858ECBCED80989FeAfC11B36` | 1 | 1/0 | 0 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 667 | Azuro V2 LiveCore | Polygon | LiveCore._binarySearch | `0x7043E4e1c4045424858ECBCED80989FeAfC11B36` | 1 | 1/0 | 0 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 668 | Azuro V2 LiveCore | Polygon | LiveCore.putBet | `0x7043E4e1c4045424858ECBCED80989FeAfC11B36` | 1 | 1/0 | 1 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 669 | Azuro V2 LiveCore | Polygon | LiveCore.putBet (signature) | `0x7043E4e1c4045424858ECBCED80989FeAfC11B36` | 1 | 1/0 | 0 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 670 | Azuro public | Polygon | AzuroBet / ClientCore (report: Livecore) | `0x8ed7296b5CAe379d07C70280Af622BC410F01Ed7` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 671 | BASE PROTOCOL | Ethereum | BASE token | `0x07150e919B4De5fD6a63DE1F9384828396f25fDC` | 1 | 1/0 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 672 | BOOK |  | TribalChief.withdrawFromDeposit | `Ethereum` | 1 | 1/0 | 1 | 1 | https://diligence.security/audits/2021/07/fei-tribechief/ |
| 673 | BSD Money | Stacks | stability-v1-0 (remove-liquidity-wrapper | `SPYY08XK8YG4W9B1WSYBM8HD0WBQ1E1WRXEGSENS.stability-v1-0` | 1 | 1/0 | 1 | 1 | https://osec.io/reports/2a484d4e-4146-800f-ae4e-fa009e5b85cd |
| 674 | Balanced Exchange | ICON | Balanced Exchange core | `cxf61cd5a45dc9f91c15aa65831a30a90d59a09619` | 1 | 1/0 | 1 | 1 | https://docs.balanced.network/assets/files/balanced-audit-slowmist-2021-b1aa5c50 |
| 675 | Base Paper Scissors (base paper scissors) | Base | BlockPaperScissors | `0x13578787E28f880F1479eEfD83d1e1594Eadb867` | 1 | 1/0 | 0 | 1 |  |
| 676 | Base WebAuthn | Base | MagicSpend | `0x011A61C07DbF256A68256B1cB51A5e246730aB92` | 1 | 1/0 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_coinbase_magicspend_feb2024.pdf |
| 677 | Baseline AMM | Ethereum | bToken (BLV) | `0x9fDbDE76236998Dc2836FE67A9954eDE456A1D63` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 678 | BaselineV2.1 | Ethereum | BPOOL.slide / floor liquidity | `0xc81fd894c0ace037d133af4886550ac8133568e8` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 679 | Bear Cave | Ethereum | HoneyBox.mekHoneyJarWithERC20/WithETH | `0x68fFCb1B5F8e5d035c3B4bf49F8F139F49E45509` | 1 | 1/0 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/s |
| 680 | Bear Cave | Ethereum | HoneyBox.claim | `0x68fFCb1B5F8e5d035c3B4bf49F8F139F49E45509` | 1 | 1/0 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/s |
| 681 | Bebop Aggregation | Ethereum | BebopSettlement.validateMakerSignature / | `0xbeb09000fa59627dc02bb55448ac1893eaa501a5` | 1 | 1/0 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 682 | Beefy Zap | Ethereum | BeefyZapRouter | `0x5cc9400ffb4da168cf271e912f589462c3a00d1f` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/beefy-zap-audit-1 |
| 683 | BitFi - BFBTC | AILayer | BFBTC | `0xC2236204768456B21eAfEf0d232Ba1FccCe59823` | 1 | 1/0 | 1 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 684 | Blast | Blast | ERC20Rebasing (WETHRebasing / USDB imple | `0x4300000000000000000000000000000000000004` | 1 | 1/0 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 685 | Blend Capital | Stellar | user_liquidation_auction.fill_user_liq_a | `CDVQVKOY2YSXS2IC7KN6MNASSHPAO7UN2UR2ON4OI2SKMFJNVAMDX6DP` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/67a31c2a-91c0-48c9-bc38-22c2b5ff105d |
| 686 | Bluefin | Sui | distributor (Sui module) | `0xe1b45a0e641b9955a20aa0ad1c1f4ad86aad8afb07296d4085e349a50e90bdca` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/01f0ce3c-4f8e-4978-aab6-97755b1e1d00 |
| 687 | Bluefin | Sui | bluefin_vault (Sui module) | `0xe1b45a0e641b9955a20aa0ad1c1f4ad86aad8afb07296d4085e349a50e90bdca` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/01f0ce3c-4f8e-4978-aab6-97755b1e1d00 |
| 688 | Botanix | Botanix | Minting contract (refund path) | `0x0Ea320990B44236A0cEd0ecC0Fd2b2df33071e78` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 689 | Botanix | Botanix | Minting contract + node execute.rs | `0x0Ea320990B44236A0cEd0ecC0Fd2b2df33071e78` | 1 | 1/0 | 1 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 690 | Botanix | Botanix | Minting contract | `0x0Ea320990B44236A0cEd0ecC0Fd2b2df33071e78` | 1 | 1/0 | 1 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 691 | Bracket Fi Escrow | Ethereum | BracketEscrow | `0x557DA267B9cCA5F994D075C880C3164033b8F6C0` | 1 | 1/0 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 692 | Brevis Contracts AVS | Arbitrum | BrevisRequest | `0x91540fE35a245BA83459f6410c86f1AEC309B290` | 1 | 1/0 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 693 | Bueno.art-2 | Ethereum | Bueno1155Drop | `0x41De0a913e8A10E0415B70810FEbCaF8a86Ea9BE` | 1 | 1/0 | 1 | 1 | https://0xmacro.com/library/audits/bueno-art-2 |
| 694 | Bunni | Ethereum | BunniHub (v2) referral accounting | `0x000000000049C7bcBCa294E63567b4D21EB765f1` | 1 | 1/0 | 1 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 695 | Bunni | Ethereum | BunniHub (v2) ERC20Referrer | `0x000000000049C7bcBCa294E63567b4D21EB765f1` | 1 | 1/0 | 0 | 1 |  |
| 696 | Bunny - PancakeBunny | BNB Chain | VaultFlipToFlip.getReward | `0xd415e6caa8af7cc17b7abd872a42d5f2c90838ea` | 1 | 1/0 | 0 | 1 | https://github.com/PancakeBunny-finance/Bunny/blob/0e3aeaecbc8493668abb4801af0f3 |
| 697 | CLOBER | Arbitrum | OrderNFT.approve + OrderBook.cancel | `0x58ed1f4913e652baF17C154551bd8E9dbc73fC56` | 1 | 1/0 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 698 | CLOBER | Arbitrum | OrderNFT (encodeId/decodeId) | `0x58ed1f4913e652baF17C154551bd8E9dbc73fC56` | 1 | 1/0 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 699 | CYBRO by | Base | BaseVault | `0x0655e391e0c6e0b8cbe8c2747ae15c67c37583b9` | 1 | 1/0 | 0 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 700 | Centrality | Ethereum | CENNZnetBridge.setValidators | `0x369e2285CCf43483e76746cebbf3d1d6060913EC` | 1 | 1/0 | 1 | 1 |  |
| 701 | Centrality | Ethereum | ERC20Peg.withdraw | `0x8F68fe02884b2B05e056aF72E4F2D2313E9900eC` | 1 | 1/0 | 1 | 1 |  |
| 702 | Centrality | Ethereum | CENNZnetBridge.verifyMessage | `0x369e2285CCf43483e76746cebbf3d1d6060913EC` | 1 | 1/0 | 1 | 1 |  |
| 703 | Centrality | Ethereum | CENNZnetBridge.setValidators / withdraw | `0x369e2285CCf43483e76746cebbf3d1d6060913EC` | 1 | 1/0 | 1 | 1 |  |
| 704 | Centrifuge | Ethereum | CentrifugeRouter | `0x2F445BA946044C5F508a63eEaF7EAb673c69a1F4` | 1 | 1/0 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 705 | ChainHopper Protocol | Ethereum | UniswapV4Settler | `0x1fa1ba925075d7a46f8f946a3f6c2f962456975d` | 1 | 1/0 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_chainhopper_april2025.pdf |
| 706 | Chateau | Optimism | QuadReader | `0xFEB98861425C6d2819c0d0Ee70E45AbcF71b43Da` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 707 | Cheelee | BNB Chain | LEE token | `0x1f1c90aeb2fd13ea972f0a71e35c0753848e3db0` | 1 | 1/0 | 1 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 708 | Chromatic Protocol EVM Contracts Halborn | Arbitrum | MarketLiquidityFacet.withdrawLiquidityBa | `0xCd92fAf0F5bcc980F2EdEee2c74352B8C9eB90c8` | 1 | 1/0 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 709 | Chromatic Protocol EVM Contracts Halborn | Arbitrum | MarketLiquidityFacet.claimLiquidityBatch | `0x632111083F0E8538aaC52E66416e111A5A84E5D1` | 1 | 1/0 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 710 | Chromatic Protocol EVM Contracts Halborn | Arbitrum | ChromaticVault.flashLoan | `0x19631A51aeDcd831E29cbCbCfe77010dAfd3343a` | 1 | 1/0 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 711 | Chromatic Protocol EVM Contracts Halborn | Arbitrum | removeLiquidityBatch | `0xCd92fAf0F5bcc980F2EdEee2c74352B8C9eB90c8` | 1 | 1/0 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 712 | CodeUP | Ethereum | Codeup | `0x4b3223E0155A00061fa64f98E824aeF94D88Be9d` | 1 | 1/0 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 713 | Compound Comprehensive Protocol | Ethereum | cTUSD (Compound TrueUSD market) | `0x12392F67bdf24faE0AF363c24aC620a2f67DAd86` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/compound-comprehensive-protocol-audit |
| 714 | Connext | Ethereum | StableSwapFacet (ConnextDiamond) | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 1/0 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 715 | Connext | Ethereum | L1XERC20Gateway / ConnextDiamond | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 1/0 | 1 | 1 | https://0xmacro.com/library/audits/connext-7 |
| 716 | Convex Platform | Ethereum | Convex VoterProxy (CurveVoterProxy) | `0x989AEb4d175e16225E39E87d0D97A3360524AD80` | 1 | 1/0 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 717 | Cove | Ethereum | BasketToken | `0xEeA3Edc017877C603E2F332FC1828a46432cdF96` | 1 | 1/0 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 718 | Cozy Finance | Optimism | Set.claimSetFees() | `0x17aFF89bf88B4eB56a1bCB256ff49FA1910E8410` | 1 | 1/0 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_cozy_apr2023.pdf |
| 719 | CrossCurve CDP | Ethereum | EYWA token | `0x8cb8c4263eb26b2349d74ea2cb1b27bc40709e12` | 1 | 1/0 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 720 | Curve Lending | Ethereum | Lending market / Controller (callback pa | `0xC9332fdCB1C491Dcc683bAe86Fe3cb70360738BC` | 1 | 1/0 | 0 | 1 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 721 | Curve Stablecoin (crvUSD | Ethereum | crvUSD stablecoin | `0xf939E0A03FB07F59A73314E73794Be0E57ac1b4E` | 1 | 1/0 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 722 | Cyber Token Bridges | Ethereum | CyberVault (share math on withdrawal) | `0x15818FCE7757Fd827F3A1bE6b68ca66D5D116302` | 1 | 1/0 | 0 | 1 | https://github.com/cyberconnecthq/cyber-token-bridges/blob/dce4920d0018d48b6c3a9 |
| 723 | DAMfinance - LMCV part 3 | Ethereum | dPrime | `0x2FdA8c6783Aa36BeD645baD28a4cDC8769dCD252` | 1 | 1/0 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 724 | DEDAUB.COM Vesper Synth audit (+Vesper Pools delta) | Ethereum | Metronome Synth ETH (msETH) | `0x64351fC9810aDAd17A690E4e1717Df5e7e085160` | 1 | 1/0 | 1 | 1 | https://github.com/Dedaub/audits/blob/431ec937802fd7118f9c6d533a530aaaf33a2c3a/V |
| 725 | DFlow Protocol | Ethereum | DFlowSwap | `0x0000890019ee8e009e1b5aded3df0042ddf8e900` | 1 | 1/0 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_dflow_nov2023.pdf |
| 726 | DODO-MiningV3 and NFT | Ethereum | buyTickets/redeem | `0x0d9685D4037580F68D9F77B08971f17E1000bBdc` | 1 | 1/0 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 727 | DODO-NFTPool | Ethereum | DODONFTPoolProxy.erc721ToErc20 | `0x9D4c342298Ba0C77E75CfD379a27F1420B3Ce45D` | 1 | 1/0 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 728 | DeFi Saver | Ethereum | FLAaveV2 -> DSProxy.executeAction | `0xEA55576383C96A69B3E8BeD51Ce0d0294001bc5F` | 1 | 1/0 | 0 | 1 |  |
| 729 | Debt DAO - P2P Loan | Ethereum | SecuredLine (per-line, created by LineFa | `0xc9ef6509a09b92043cedce689dfaa760048abd7f` | 1 | 1/0 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 730 | Definer | Ethereum | Accounts.withdraw | `0xad4649a917a0e928d00c3028db63acb07960d25b` | 1 | 1/0 | 0 | 1 | https://diligence.security/audits/2021/02/definer/ |
| 731 | Degis SCProtection | Avalanche | Treasury | `0x7951CFc78CcE5Ce0aF2832B388e7f55E8d2C5EBB` | 1 | 1/0 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 732 | Derive Derive (Formerly Lyra) | Derive | DutchAuction | `0x141919f1FA90F99A3fbafFb0b111e4f84AB5aB52` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 733 | Derive Derive (Formerly Lyra) | Derive | StandardManager | `0x28c9ddF9A3B29c2E6a561c1BC520954e5A33de5D` | 1 | 1/0 | 1 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 734 | Drop Contracts | Neutron | Drop core (execute_bond / DenomType::Lsm | `neutron1lsxvdyvmexak084wdty2yvsq5gj3wt7wm4jaw34yseat7r4qjffqlxlcua` | 1 | 1/0 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 735 | Dyad | Ethereum | DYAD vault | `0x7aE80418051b2897729Cbdf388b07C5158C557A1` | 1 | 1/0 | 1 | 1 |  |
| 736 | EIP-4337 – Ethereum Account Abstraction | Ethereum | EntryPoint.depositTo / internal accounti | `0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/eth-foundation-account-abstraction-audit |
| 737 | ENS Permanent Registrar | Ethereum | ETHRegistrarController | `0xF0AD5cAd05e10572EfcEB849f6Ff0c68f9700455` | 1 | 1/0 | 0 | 1 | https://diligence.security/audits/2019/03/ens-permanent-registrar/ |
| 738 | ENS contest | Ethereum | ENSRegistryWithFallback | `0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e` | 1 | 1/0 | 0 | 1 | https://github.com/ConsenSysDiligence/ens-audit-report-2019-02/blob/4c4005c90767 |
| 739 | Eco PhaseII v 1 0 | Ethereum | InflationRootHashProposal | `0x5FF0Ef859Dea265946b8834533908D3346ED0a6F` | 1 | 1/0 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 740 | Eggs Finance | Sonic | EGGS token (protocol core) | `0xf26Ff70573ddc8a90Bd7865AF8d7d70B8Ff019bC` | 1 | 1/0 | 0 | 1 |  |
| 741 | EigenLayer (Sigma Prime review 3) | Ethereum | EigenPod (via EigenPodManager) | `0x91E677b07F7AF907ec9a428aafA9fc14a0d3A338` | 1 | 1/0 | 0 | 1 |  |
| 742 | EigenLayer Oct23 (Restaking / Liquid staking) | Ethereum | EigenPodManager (proxy) | `0x91E677b07F7AF907ec9a428aafA9fc14a0d3A338` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 743 | EigenLayer Oct23 (Restaking / Liquid staking) | Ethereum | EigenPod (beacon implementation) | `0x5a2a4F2F3C18f09179B6703e63D9eDD165909073` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 744 | Endaoment | Ethereum | EndaomentAdmin | `0x2a108b1810890482fDB3bE188616c56dD0170A8E` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/endaoment-audit |
| 745 | Enso Wallet | Ethereum | EnsoWalletFactory | `0x09bfFa3C7275A3Fa01595a72204e5A659B6C5067` | 1 | 1/0 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 746 | Ethena Vault TON | TON | tsusde-wallet send_timelocked_jettons /  | `EQDQ5UUyPHrLcQJlPAczd_fjxn8SLrlNQwolBznxCdSlfQwr` | 1 | 1/0 | 1 | 1 | https://osec.io/reports/1eb84d4e-4146-8068-86c7-ef5b67567421 |
| 747 | Exactly EscrowedExa | Optimism | EscrowedEXA | `0x81fC4cf70066c25B92CE1D9DaaE50cd607d763e0` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/exactly-escrowedexa-audit |
| 748 | Exponent Finance | Solana | SY program check | `ExponentnaRg3CQbW6dqQNZKXp7gtZ9DGMp1cwC4HAS7` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/13b84d4e-4146-8052-809a-c7da80edd800 |
| 749 | Extensions | Base | PrivacyBoost pool (GiftClaim/VerifyEdDSA | `0x71A0fD3C76E3E937d8275A3cb6a467b70123bD40` | 1 | 1/0 | 1 | 1 | https://github.com/sunnyside-io/privacy-boost-protocol/blob/ca90d08e11a7a9b435ae |
| 750 | FLock Phase1 | Base | FLOCK token (Base) | `0x5aB3D4c385B400F3aBB49e80DE2fAF6a88A7B691` | 1 | 1/0 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 751 | FOR 1INCH | Ethereum | ERC20Pods delegate() | `0x111111111117dC0aa78b770fA6A738034120C302` | 1 | 1/0 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 752 | FOR 1INCH | Ethereum | ERC20Pods._updateBalances | `0x111111111117dC0aa78b770fA6A738034120C302` | 1 | 1/0 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 753 | FOR LIDO V2 | Ethereum | _claimWithdrawalTo (WithdrawalQueueERC72 | `0x889edC2eDab5f40e902b864aD4d7AdE8E412F9B1` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 754 | FOR QUICKSWAP | Polygon | QuickSwap V2 Router | `0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff` | 1 | 1/0 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 755 | Fathom DAO | XDC | VaultPackage (deployed via FathomVaultFa | `0x0c6e3fd64D5f33eac0DCCDd887A8c7512bCDB7D6` | 1 | 1/0 | 1 | 1 | https://github.com/oxor-io/public_audits/blob/06624b6efe70d98702baccef5208ec57db |
| 756 | Fathom DAO | XDC | FathomVaultFactory | `0x0c6e3fd64D5f33eac0DCCDd887A8c7512bCDB7D6` | 1 | 1/0 | 0 | 1 | https://github.com/oxor-io/public_audits/blob/06624b6efe70d98702baccef5208ec57db |
| 757 | Fei Protocol | Ethereum | GenesisGroup | `0xBFfB152b9392e38CdDc275D818a3Db7FE364596b` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/fei-protocol-audit |
| 758 | Folks Finance X-Chain | Avalanche | Folks xChain spoke | `0xff7f8f301f7a706e3cfd3d2275f5dc0b9ee8009b` | 1 | 1/0 | 0 | 1 | https://github.com/Folks-Finance/audits/blob/13f8d8307902e8ff7018fe9b6df0b5668c6 |
| 759 | FrankenCoin Audit | Ethereum | MintingHub challenge | `0xDe12B620A8a714476A97EfD14E6F7180Ca653557` | 1 | 1/0 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 760 | FrankenCoin Audit | Ethereum | Frankencoin (ZCHF) initializer | `0xB58E61C3098d85632Df34EecfB899A1Ed80921cB` | 1 | 1/0 | 1 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 761 | FrankenCoin Audit | Ethereum | MintingHub.buyExpiredCollateral | `0xDe12B620A8a714476A97EfD14E6F7180Ca653557` | 1 | 1/0 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 762 | Frictionless Protocol (ERC-3643) | Ethereum | FrictionlessTransferManager | `0x62890bC992CC60b6EDdC540Ed65010C6Ba9c01b0` | 1 | 1/0 | 1 | 1 |  |
| 763 | Frictionless Protocol (ERC-3643, Dec 2023) | Ethereum | FrictionlessComplianceFactory | `0x0c2299bFcC2d44baA92ae3dA9f519AfedF363f64` | 1 | 1/0 | 1 | 1 |  |
| 764 | Fungify Oct23 | Ethereum | Fungify Comptroller | `0xf9c70750bF615dE83fE7FF62D30C7faACD8f8Ba0` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 765 | Fungify Oct23 | Ethereum | cERC20 USDC market | `0x5f86f598e4fa983097fe6693a1b51f047d87b9cf` | 1 | 1/0 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 766 | Fuzion Plasma OTC | Kujira | FUZN token (Kujira factory denom) | `kujira:factory/kujira1sc6a0347cc5q3k890jj0pf3ylx2s38rh4sza4t/ufuzn` | 1 | 1/0 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 767 | Fyde | Ethereum | TRSY (Fyde treasury share token) | `0x87Cc45fFF5c0933bb6aF6bAe7Fc013b7eC7df2Ee` | 1 | 1/0 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 768 | GMX Crosschain V2.2 1 | Arbitrum | EdgeDataStreamProvider | `0x24A01E28077C2b831166Dd4099DFfD4056a336a1` | 1 | 1/0 | 0 | 0 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 769 | GMX Crosschain V2.2 1 | Arbitrum | ExecuteDepositUtils | `0x4fEc706C582e4243D4aA2Bcd49763201E968c75b` | 1 | 1/0 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 770 | GMX Crosschain V2.2 1 | Arbitrum | MultichainGlvRouter | `0xabcBbe23BD8E0dDD344Ff5fd1439b785B828cD2d` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 771 | GMX GLV | Arbitrum | GlvVault / GlvHandler | `0x393053B58f9678C9c28c2cE941fF6cac49C3F8f9` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 772 | GMX Synthetics | Arbitrum | MarketUtils | `0xd099565957046a2d2CF41B0CC9F95e14a8afD13b` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 773 | GMX Synthetics | Arbitrum | IncreasePositionUtils | `0xD3D705e88cce7E11452b3D900F694bEc80eF5742` | 1 | 1/0 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 774 | GMX Synthetics | Arbitrum | DecreaseOrderUtils | `0x3b2B33DD30B1497611304c6423AC5FD9AED1e74b` | 1 | 1/0 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 775 | GMX gmx synthetics v 1 0 | Arbitrum | GMX Synthetics core (pending PnL / pool  | `0x1C3fa76e6E1088bCE750f23a5BFcffa1efEF6A41` | 1 | 1/0 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 776 | Gains Trade | Arbitrum | Gains NFT bridge (bridgeNFT) | `0xE7B5B80442CFa4FB99ca947360dEA681b27CC864` | 1 | 1/0 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 777 | GammaSwap | Arbitrum | GammaSwap pool factory | `0xe048ccE443E787c5b6FA886236De2981D54E244f` | 1 | 1/0 | 1 | 1 |  |
| 778 | Gasp Node and Monorepo | Ethereum | Rolldown (close_withdrawal) | `0xEAfc65D0d179FE354B71accC4997124ea98Fb0FD` | 1 | 1/0 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 779 | Gearbox Midas Integration Audit | Ethereum | Address Provider | `0xF7f0a609BfAb9a0A98786951ef10e5FE26cC1E38` | 1 | 1/0 | 1 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 780 | Geode Finance Withdrawal Module | Avalanche | Geode Portal (AVAX) | `0x4fe8C658f268842445Ae8f95D4D6D8Cfd356a8C8` | 1 | 1/0 | 0 | 1 | https://github.com/shieldify-security/audits-portfolio-md/blob/cb986f228e75a5753 |
| 781 | Gluwa NFT | Ethereum | GluwaNFT | `0x45bD22E0430ce853d65d46925362A1ccf66e225f` | 1 | 1/0 | 0 | 1 | https://github.com/chainlight-io/publications/blob/ec332bf4d0cde16e3db4f380b5a4d |
| 782 | GnoSwap Audit | Gno.land | staker realm EndExternalIncentive | `gno.land/r/gnoswap/staker` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/gnoswap-audit |
| 783 | GnoSwap Audit | Gno.land | router realm ExactInSwapRoute | `gno.land/r/gnoswap/router` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/gnoswap-audit |
| 784 | GnoSwap Audit | Gno.land | staker realm CollectReward | `gno.land/r/gnoswap/staker` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/gnoswap-audit |
| 785 | GnoSwap Extended | Gno.land | pool realm (safeSwapCallback / swap lock | `gno.land/r/gnoswap/pool/v1` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/gnoswap-extended-audit |
| 786 | HEGIC | Ethereum | HegicETHOptions.create() | `0xEfC0eEAdC1132A12c9487d800112693bf49EcfA2` | 1 | 1/0 | 1 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 787 | Helium Program Library | Solana | lazy-distributor | `1azyuavdMyvsivtNxPoz6SucD18eDHeXzFCUPq5XU7w` | 1 | 1/0 | 0 | 1 | https://github.com/sec3-service/reports/blob/13c2f82d576164c7db728108d09a8d37272 |
| 788 | Hinkal Protocol | Ethereum | Hinkal pool (multiTransferFrom) | `0x25e5e82f5702A27C3466fE68f14abDbbAdFca826` | 1 | 1/0 | 1 | 1 |  |
| 789 | Hinkal Protocol | Ethereum | Hinkal Swapper circuit / verifier | `0x25e5e82f5702A27C3466fE68f14abDbbAdFca826` | 1 | 1/0 | 0 | 1 |  |
| 790 | Hinkal Protocol | Ethereum | Hinkal pool (calldataHash) | `0x25e5e82f5702A27C3466fE68f14abDbbAdFca826` | 1 | 1/0 | 0 | 1 |  |
| 791 | Hodl on November 05, 2020 | Ethereum | HodlDex (HOracle module) | `0xC310644A0Cf1cAE7E240A48090c3cdB9Edb53941` | 1 | 1/0 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 792 | Huma Vault | Solana | PSTStrategy (Huma program module) | `HumaXepHnjaRCpjYTokxY4UtaJcmx41prQ8cxGmFC5fn` | 1 | 1/0 | 0 | 1 | https://github.com/sec3-service/reports/blob/13c2f82d576164c7db728108d09a8d37272 |
| 793 | Hypercerts | Optimism | HypercertMinter._splitValue | `0x822F17A9A5EeCFd66dBAFf7946a8071C265D1d07` | 1 | 1/0 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/s |
| 794 | Hyperdrive March 2024 | Ethereum | HyperdriveRegistry | `0xbe082293B646cb619A638d29E8EfF7cF2f46aA3a` | 1 | 1/0 | 1 | 1 | https://cdn.cantina.xyz/reports/Delv-Spearbit-Security-Review-March-2024.pdf |
| 795 | Infinex-9 | Ethereum | PatronNFT (XPATRON) | `0xB5AF0C7f3885c1007e6699c357566610291585Cb` | 1 | 1/0 | 1 | 1 | https://0xmacro.com/library/audits/infinex-9 |
| 796 | Infrared | Berachain | BribeCollector | `0x8d44170e120B80a7E898bFba8cb26B01ad21298C` | 1 | 1/0 | 0 | 1 | https://cdn.cantina.xyz/reports/Infrared-Spearbit-Security-Review-January-2025.p |
| 797 | Instadapp Fluid | Ethereum | BigMathVault (library) | `0x52Aa899454998Be5b000Ad077a46Bbe360F4e497` | 1 | 1/0 | 0 | 0 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 798 | InsureDAO - August 13, 2021 | Ethereum | InsureDAO Vault | `0x131fb74c6fede6d6710ff224e07ce0ed8123f144` | 1 | 1/0 | 1 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 799 | Interport Finance | BNB Chain | InterportDex / router | `0x2b1D36f5B61AdDAf7DA7ebbd11B35FD8cfb0DE31` | 1 | 1/0 | 0 | 1 |  |
| 800 | Ion Protocol | Ethereum | ReserveFeed (WeEthWstEthReserveOracle) | `0x78C3ac7F84F5101422DCd89fB387bD0DeEf8d662` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/ion-protocol-audit |
| 801 | Irrigation Protocol Smart Contract Security | Ethereum | SprinklerUpgradeable | `0xf5a070fa06FBA1F2a19FB9EeB39Aca3377AE6372` | 1 | 1/0 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 802 | Jet v2 | Solana | jet_margin_swap | `JPMAa5dnWLFRvUsumawFcGhnwikqZziLLfqn9SLNXPN` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/0f0a4a14-07ac-4d14-9932-7fc75ecfab26 |
| 803 | Jet v2 | Solana | jet_control | `JPCtrLreUqsEbdhtxZ8zpd8wBydKz4nuEjX5u9Eg5H8` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/0f0a4a14-07ac-4d14-9932-7fc75ecfab26 |
| 804 | Jet v2 | Solana | jet_margin_pool | `JPPooLEqRo3NCSx82EdE2VZY5vUaSsgskpZPBHNGVLZ` | 1 | 1/0 | 1 | 1 | https://osec.io/reports/0f0a4a14-07ac-4d14-9932-7fc75ecfab26 |
| 805 | Jet v2 | Solana | jet_margin | `JPMRGNgRk3w2pzBM1RLNBnpGxQYsFQ3yXKpuk4tTXVZ` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/0f0a4a14-07ac-4d14-9932-7fc75ecfab26 |
| 806 | KashiPair | Ethereum | KashiPairMediumRiskV1 | `0x74A81CB5b6996d9347b864b9a1492a6509e51e65` | 1 | 1/0 | 1 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 807 | KeyringV2 | Base | KeyringCoreV2 proxy (Base) | `0xf26b0f10691ed160734a3a5caf8ca1fcb57efc9d` | 1 | 1/0 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 808 | Kim NFT marketplace | Mode | KimNFTMarketplace (Auction) | `0x67135675e22F7ff34eBA30f15f39F9cd30d29079` | 1 | 1/0 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_kim_exchange_november2024.pdf |
| 809 | Kinto | Kinto | KintoWallet / SignerPolicy | `0xA6ddF426008E8b7f1a70237bdEfafB5D928bA72E` | 1 | 1/0 | 0 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 810 | Kintsu Monad Contracts Core | Monad | StakedMonad deposit / instantUnlock | `0xA3227C5969757783154C60bF0bC1944180ed81B9` | 1 | 1/0 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_kintsu_sep2025.pdf |
| 811 | Kite AI Validator and Staking Manager | KiteAI | KiteStakingManager | `0x7d627b0F5Ec62155db013B8E7d1Ca9bA53218E82` | 1 | 1/0 | 1 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 812 | KittenSwap | Hyperliquid L1 | Minter | `0xac36d3671f21A5056Cd1751E201574d702748C7A` | 1 | 1/0 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 813 | KittenSwap | Hyperliquid L1 | RebaseReward | `0xDd002E8DF80ccB7A8964BFef6e15ee36D414fC36` | 1 | 1/0 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 814 | Kresko Labs Pte. Ltd - July 14, 2023 | Arbitrum | Kresko Diamond (LibRedstone signer) | `0x0000000000177abD99485DCaea3eFaa91db3fe72` | 1 | 1/0 | 1 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 815 | Kroma | Ethereum | L2OutputOracle (proxy) | `0x180c77aE51a9c505a43A2C7D81f8CE70cacb93A6` | 1 | 1/0 | 0 | 1 | https://github.com/kroma-network/kroma/blob/102150bab01f127414d375d77182af093477 |
| 816 | Kroma Validator System v2 | Ethereum | Kroma Portal (proxy) | `0x31f648572b67e60ec6eb8e197e1848cc5f5558de` | 1 | 1/0 | 0 | 1 | https://github.com/kroma-network/kroma/blob/102150bab01f127414d375d77182af093477 |
| 817 | Kwenta-19 | Base | Engine (Smart Margin v3) | `0xe331a7eeC851Ba702aA8BF43070a178451d6D28E` | 1 | 1/0 | 1 | 1 | https://0xmacro.com/library/audits/kwenta-19 |
| 818 | LIDO IN-PROTOCOL COVERAGE | Ethereum | Lido core stETH share accounting (covera | `0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84` | 1 | 1/0 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 819 | LV | Solana | OpenDelta Perpetual Bond program | `opbrKSFxFXRHNg75xjpEAbJ5R6e6GYZ6QKEqdvcBq7c` | 1 | 1/0 | 1 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 820 | Lendle | Mantle | LendingPool (main market proxy) | `0xCFa5aE7c2CE8Fadc6426C1ff872cA45378Fb7cF3` | 1 | 1/0 | 1 | 1 | https://www.halborn.com/audits/lendle/brink-a73cf0 |
| 821 | Levana Stage 2 | Sei | Levana Perps factory / levana-balancer | `sei18rdj3asllguwr6lnyu2sw8p8nut0shuj3sme27ndvvw4gakjnjqqper95h` | 1 | 1/0 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 822 | Levana Stage 2 | Sei | Levana Perps factory (Sei) | `sei18rdj3asllguwr6lnyu2sw8p8nut0shuj3sme27ndvvw4gakjnjqqper95h` | 1 | 1/0 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 823 | Level Money contracts | Ethereum | LevelMinting.mintDefault | `0x8E7046e27D14d09bdacDE9260ff7c8c2be68a41f` | 1 | 1/0 | 1 | 1 |  |
| 824 | Lido V3 | Ethereum | PredepositGuarantee | `0xF4bF42c6D6A0E38825785048124DBAD6c9eaaac3` | 1 | 1/0 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 825 | Lido on Polygon | Polygon | stMATIC | `0x3a58a54c066fdc0f2d55fc9c89f0415c92ebf3c4` | 1 | 1/0 | 0 | 1 | https://github.com/oxor-io/public_audits/blob/06624b6efe70d98702baccef5208ec57db |
| 826 | Light Protocol | Solana | Compressed token program (token transfer | `compr6CUsB5m2jS4Y3831ztGSTnDpnKJTKS95d64XVq` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/0a8bcc85-0c10-495b-92a7-701e5f90053a |
| 827 | Likwid | Ethereum | LikwidVault.unlockCallback / position ma | `0x065d449ec9D139740343990B7E1CF05fA830e4Ba` | 1 | 1/0 | 1 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 828 | Linea Bridge | Ethereum | Linea L1 TokenBridge | `0x051F1D88f0aF5763fB888eC4378b4D8B29ea3319` | 1 | 1/0 | 1 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 829 | Linea Verifier | Ethereum | Linea Plonk verifier used by LineaRollup | `0xd19d4B5d358258f05D7B411E21A1460D11B0876F` | 1 | 1/0 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 830 | LiquiFi by | Ethereum | LiquifiInitialGovernor | `0x3Fc95E5000269747C14418985Cb272365211a779` | 1 | 1/0 | 0 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 831 | Longdragon | Ethereum | Longdragon (contract instance) | `0x3e80A2Eea4324cB565A499b204dd6Ea0A4ea4068` | 1 | 1/0 | 0 | 1 |  |
| 832 | M0 Liquidity Delivery | Ethereum | WormholeBridgeAdapter | `0xaCffEC28C4eEe21C889a4e6C0704c540Ed9D4fDd` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 833 | M0 Liquidity Delivery | Ethereum | OrderBook | `0xe39B012AB3b20E94a9beEa557eB0DE4171D4D3E4` | 1 | 1/0 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 834 | MANTISSA FINANCE SMART | Polygon | MantisSwap Main Pool (checkSwapOraclePri | `0x62Ba5e1AB1fa304687f132f67E35bFC5247166aD` | 1 | 1/0 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 835 | MESHswap | Polygon | MeshswapRouter.removeLiquidityWithLimit  | `0x10f4A785F458Bc144e3706575924889954946639` | 1 | 1/0 | 0 | 1 | https://github.com/meshswap-fi/meshswap/blob/2c40a3ce2bca7e3941e979777151dcf82c2 |
| 836 | MagnifyCash | World Chain | NFTYFinanceV1.createLoan | `0x71da932ccda723ba3ab730c976bc66daaf9c598c` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 837 | Mango v4 | Solana | Mango v4 program (HealthRegions) | `4MangoMjqJ2firMokCjjGgoK8d4MXcrgL7XJaL3w6fVg` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/41f58737-a349-4eec-901a-3762d66e27eb |
| 838 | Mantle Network Mantle L2 Rollup V2 | Ethereum | L1CrossDomainMessenger (_target message) | `0x676A795fe6E43C17c668de16730c3F690FEB7120` | 1 | 1/0 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 839 | Martin Ortner | Ethereum | KeepRandomBeaconOperator / BLS library | `0x70F2202D85a4F0Cad36e978976f84E982920A624` | 1 | 1/0 | 0 | 1 |  |
| 840 | Martin Ortner | Ethereum | TBTCSystem.requestNewKeep | `0xe20A5C79b39bC8C363f0f49ADcFa82C2a01ab64a` | 1 | 1/0 | 0 | 1 |  |
| 841 | Mayan | Solana | Mayan program (mayan_flash_swap_finish) | `FC4eXxkyrMPTjiYUpp4EAnkmwMbQyZ6NDCh1kfLn6vsf` | 1 | 1/0 | 1 | 1 | https://osec.io/reports/787c44eb-2727-42b1-b1a2-5b19eee3a094 |
| 842 | MegaETH | Ethereum | L1StandardBridgeProxy (canonical bridge) | `0x0CA3A2FBC3D770b578223FBB6b062fa875a2eE75` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/13684d4e-4146-80af-bfc7-f85da6afad08 |
| 843 | Megapot v2 | Base | ScaledEntropyProvider (callback target:  | `0x5D030DEC2e0d38935e662C0d2feD44B050c8Ae51` | 1 | 1/0 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 844 | Mellow protocol Gearbox integration | Ethereum | GearboxRootVault | `0xb1b385e74aF2C91b998126e29cc6B02eA48b2871` | 1 | 1/0 | 1 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 845 | Metamask Delegation Framework February | Ethereum | NativeTokenStreamingEnforcer | `0xD10b97905a320b13a0608f7E9cC506b56747df19` | 1 | 1/0 | 0 | 1 | https://diligence.security/audits/2025/02/metamask-delegation-framework-february |
| 846 | Metamask Delegation Framework February | Ethereum | DelegationMetaSwapAdapter | `0xe41eB5A3F6e35f1A8C77113F372892D09820C3fD` | 1 | 1/0 | 0 | 1 | https://diligence.security/audits/2025/02/metamask-delegation-framework-february |
| 847 | Mintbase | NEAR | MintbaseStore (mb-store) | `mintbase1.near` | 1 | 1/0 | 1 | 1 | https://osec.io/reports/eff2edf2-c1d6-4cec-9087-e647ba56f03d |
| 848 | Mitosis | Ethereum | Mitosis vault (Ethereum) | `0xE4cf2D4eb9c01784798679F2FED4CF47cc59a3ec` | 1 | 1/0 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 849 | Mitosis | Ethereum | BasicVault._redeem | `0xE4cf2D4eb9c01784798679F2FED4CF47cc59a3ec` | 1 | 1/0 | 1 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 850 | Morpho | Ethereum | Morpho CompoundV2 Optimizer (P2P exchang | `0x8888882f8f843896699869179fB6E4f7e3B58888` | 1 | 1/0 | 0 | 1 | https://cdn.cantina.xyz/reports/Morpho-Spearbit-Security-Review.pdf |
| 851 | Morpho | Ethereum | RewardsManagerForAave.accrueUserUnclaime | `0x777777c9898D384F785Ee44Acfe945efDFf5f3E0` | 1 | 1/0 | 1 | 1 | https://cdn.cantina.xyz/reports/Morpho-Spearbit-Security-Review.pdf |
| 852 | Morpho | Ethereum | Morpho AaveV3 Optimizer._getAssetPrice | `0x33333aea097c193e66081E930c33020272b33333` | 1 | 1/0 | 0 | 1 | https://cdn.cantina.xyz/reports/Morpho-Av3-Spearbit-Security-Review.pdf |
| 853 | Morpho | Ethereum | Morpho AaveV3 Optimizer._POOL.supplyToPo | `0x33333aea097c193e66081E930c33020272b33333` | 1 | 1/0 | 0 | 1 | https://cdn.cantina.xyz/reports/Morpho-Av3-Spearbit-Security-Review.pdf |
| 854 | Mysten Deepbook | Sui | DeepBook order::generate_fill | `0x000000000000000000000000000000000000000000000000000000000000dee9` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/3d5aff70-3359-42ee-a717-9e02a6a1b555 |
| 855 | NOVEMBER 5 | Ethereum | StandardBounties.refundContribution | `0x51598ae36102010feca5322098b22dd5b773428b` | 1 | 1/0 | 1 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 856 | NOVEMBER 5 | Ethereum | StandardBounties | `0x51598ae36102010feca5322098b22dd5b773428b` | 1 | 1/0 | 1 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 857 | NUTS Pike | Sonic | SelfPeggingAsset.mint | `0xcB53d44FF0b466daebCcE311A8F7bB1DF569AceD` | 1 | 1/0 | 1 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 858 | NUTS Pike | Sonic | PTokenModule.deposit | `0xcB53d44FF0b466daebCcE311A8F7bB1DF569AceD` | 1 | 1/0 | 1 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 859 | Narwhal Finance Jan25 | Arbitrum | Narwhal perp/lending core | `0x873177DB4EaC3581464FFA64deB39b25CE409bFd` | 1 | 1/0 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 860 | Navi Protocol Core | Sui | NAVI lending package (validator.move) | `0x512f28261c1a293f49416d8885b8d5d32bde6dd68a99a0be36fe42b248e6833a` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/757f828d-9f36-426a-b639-36ca8d3bc189 |
| 861 | Nexus | Terra | Nexus Protocol core (Terra) | `terra12897djskt9rge8dtmm86w654g7kzckkd698608` | 1 | 1/0 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 862 | Nexus | Terra | Nexus vault core (DepositETH/DepositUSD) | `terra12897djskt9rge8dtmm86w654g7kzckkd698608` | 1 | 1/0 | 0 | 1 |  |
| 863 | Notional Audit | Ethereum | interest rate model | `0xcfeaead4947f0705a14ec42ac3d44129e1ef3ed5` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/notional-audit |
| 864 | Notional Audit | Ethereum | FutureCash / Escrow | `0xcfeaead4947f0705a14ec42ac3d44129e1ef3ed5` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/notional-audit |
| 865 | Notional Audit | Ethereum | Escrow | `0xcfeaead4947f0705a14ec42ac3d44129e1ef3ed5` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/notional-audit |
| 866 | NotionalV2 | Ethereum | Notional V2 (LiquidationHelpers library) | `0x1344A36A1B56144C3Bc62E7757377D288fDE0369` | 1 | 1/0 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 867 | Nuon | Base | VoteEscrow | `0x528c319C8D7A4f9656028A451bE1403664035f1a` | 1 | 1/0 | 1 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 868 | Oak Network Smart Contracts | Celo | BasePaymentTreasury.processCryptoPayment | `0x871BF839e48fD91cBA7ccF37a3119F84adb54584` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/oak-network-smart-contracts-audit |
| 869 | Olympus-Cooler-Migrator-Composite | Ethereum | CoolerV2Migrator.consolidate | `0xE045BD0A0d85E980AA152064C06EAe6B6aE358D2` | 1 | 1/0 | 1 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 870 | Omni Network Omni SolverNet | Ethereum | SolverNetInbox | `0x0827953D0b8954a74B82F68dD9DCC94087bec0BA` | 1 | 1/0 | 1 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 871 | Ondo OndoProtocol 1 0 | Ethereum | OndoOracle (one of several instances) | `0x2e1C9B23975bcf6dFD8Af18DB31b08AD6222726C` | 1 | 1/0 | 1 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 872 | Openbook | Solana | OpenBook v2 program (market vault side c | `opnb2LAfJYbRMAHHvqjCwQxanZn7ReEHp1k81EohpZb` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/527e1c3e-b913-4a2a-9d82-88757467e4a0 |
| 873 | Optimism Smart Contracts Audit | Ethereum | OVM_FraudVerifier | `0x042065416C5c665dc196076745326Af3Cd840D15` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/optimism-smart-contracts-audit |
| 874 | Opyn | Ethereum | OptionsExchange (Opyn v1) | `0x39246c4f3f6592c974ebc44f80ba6dc69b817c71` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/opyn-contracts-audit |
| 875 | Opyn Gamma Protocol | Ethereum | Controller / MarginPool | `0x5934807cc0654d46755ebd2848840b616256c6ef` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/opyn-gamma-protocol-audit |
| 876 | Orderly | Orderly L2 | LedgerCrossChainManager | `0xa0a07a78c7d31E6f8698F48Fc9219f9a3030f38C` | 1 | 1/0 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 877 | Orderly | Orderly L2 | LedgerCrossChainRelay | `0x173B47eDBeCa665125edc24C509bfE545CDA60a9` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 878 | Orderly Vault | Ethereum | VaultCrossChainManager.sendMessage | `0x816f722424b49cf1275cc86da9840fbd5a6167e9` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 879 | Origin Dollar | Ethereum | VaultCore._allocate / Buyback.swap | `0xE75D77B1865Ae93c7eaa3040B038D7aA7BC02F70` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/origin-dollar-audit |
| 880 | Parcl Finance | Solana | Parcl V2 core program | `pAMMTYk2C9tAxenepGk8a1bi9JQtUdnzu3UAh7NxYcW` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/15f84d4e-4146-8089-bb2c-d277fd80cf85 |
| 881 | PariFi | Arbitrum | ParifiVault / OrderManager | `0xbf11ac635fe97430b5333018778d0d746f67c989` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/DefenderAudits/blob/b2a2ccb9b6e07d82a6c4497fee |
| 882 | Pear Protocol Vault | HyperEVM | PearVault.withdraw / redeem | `0x65C9F4665C7D9Ce96F53aAfc67796dcaD46f4096` | 1 | 1/0 | 1 | 1 | https://github.com/shieldify-security/audits-portfolio-md/blob/cb986f228e75a5753 |
| 883 | Peer Review – SPL Stake Pool | Solana | SPL Stake Pool program (UpdateValidatorL | `SPoo1Ku8WFXoNDMHPsrGSTSG1Y47rzgn41SLUNakuHy` | 1 | 1/0 | 1 | 1 | https://www.neodyme.io/reports/SPL-Stake-Pool-2021.pdf |
| 884 | Peridot Protocol | Monad | ReceiptVault (pToken market) / Peridottr | `0x6D208789f0a978aF789A3C8Ba515749598940716` | 1 | 1/0 | 1 | 1 | https://www.halborn.com/audits/peridot-protocol/smart-contract-assessment-e9c4bc |
| 885 | Peridot Protocol | Monad | ReceiptVault (pToken market) | `0x6D208789f0a978aF789A3C8Ba515749598940716` | 1 | 1/0 | 1 | 1 | https://www.halborn.com/audits/peridot-protocol/smart-contract-assessment-e9c4bc |
| 886 | PerpCity Protocol | Arbitrum | Perp implementation (margin/OI checks) | `0x9b74b1ff217bdE6EB0e221Ca11034D67187EF9d3` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 887 | Plume Staking | Plume | PlumeStaking (proxy) | `0x2Af5aD4Af9433765fa333dBC3C3C38224eEEE332` | 1 | 1/0 | 1 | 1 | https://osec.io/reports/20684d4e-4146-80fb-8c01-e8c0c7987f13 |
| 888 | Polygon zkEVM | Ethereum | PolygonZkEVMBridge.bridgeAsset | `0x2a3DD3EB832aF982ec71669E178424b10Dca2EDe` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 889 | Pontem Liquidswap | Aptos | Liquidswap stable curve | `0x190d44266241744264b964a37b8f09863167a12d3e70cda39376cfb4e3561e12` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/cab09ca7-ca5a-4004-858c-a750902148f4 |
| 890 | PoolTogether | Optimism | TwabController (V5) | `0xCB0672dE558Ad8F122C0E081f0D35480aB3be167` | 1 | 1/0 | 0 | 1 | https://0xmacro.com/library/audits/pooltogether-1 |
| 891 | PoolTogether - Pods | Ethereum | Pod (prize draw participation) | `0x9F4C5D8d9BE360DF36E67F52aE55C1B137B4d0C4` | 1 | 1/0 | 0 | 1 | https://diligence.security/audits/2021/03/pooltogether-pods/ |
| 892 | Port Sundial | Solana | Sundial program - liquidate_sundial_prof | `SDLxV7m1qmoqkytqYRGY1x438AbYCqekPsPxK4kvwuk` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/6b396a13-1550-48c5-ba25-0e9dd63508eb |
| 893 | PotLock | NEAR | donations.rs donate() | `donate.potlock.near` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/0a200eb5-f171-4771-bd6d-fe604b4aff59 |
| 894 | PowerPool Agent | Ethereum | PPAgentV2.registerJob | `0xc9ce4CdA5897707546F3904C0FfCC6e429bC4546` | 1 | 1/0 | 0 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 895 | PowerPool Agent | Ethereum | PPAgentV2.executeJob / stake | `0xc9ce4CdA5897707546F3904C0FfCC6e429bC4546` | 1 | 1/0 | 1 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 896 | PowerPool Agent | Ethereum | PPAgentV2Randao.getSlasherIdByBlock | `0xc9ce4CdA5897707546F3904C0FfCC6e429bC4546` | 1 | 1/0 | 0 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 897 | Prism | Terra | yAsset staking contract | `terra188mmw2vsp0yahen3vh2clup543qrttvdzkxl0h9myfuwjj56nausztpegt` | 1 | 1/0 | 1 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 898 | Public - DPeg Protocol Smartcontracts | Ethereum | LevErc20 | `0x2a2b195558cF89AA617979ce28880BbF7e17bc45` | 1 | 1/0 | 1 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 899 | Public - DPeg Protocol Smartcontracts | Ethereum | DepErc20 (DepToken.redeem) | `0x7b190a928Aa76EeCE5Cb3E0f6b3BdB24fcDd9b4f` | 1 | 1/0 | 1 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 900 | Public - Harmonix Finance | Arbitrum | CamelotLiquidity.sol (Arbitrum strategy) | `0x3363A85c31cf13a96802e2935724232767420135` | 1 | 1/0 | 1 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 901 | Public - KatanaInu NFT System | Ethereum | KatanaInu NFT / royalty contract | `0x31e189E2595007Fe911c64e5fa53be2ed9A21aCA` | 1 | 1/0 | 1 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 902 | Public - Mones Marketplace | BNB Chain | MONES token | `0xac3050C7cc3Bd83fd5B53FB94C0bE385b1ca6D15` | 1 | 1/0 | 0 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 903 | Public - Polyroll | Polygon | RollToken | `0xc68e83a305b0fad69e264a1769a0a070f190d2d6` | 1 | 1/0 | 0 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 904 | Public - Tioswap Smartcontracts | Ethereum | TioSwap (finalizeTrade) | `0x6413EadbA07EE868EeC62095a740E77162F8D735` | 1 | 1/0 | 0 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 905 | Public - UnizenDex Smartcontracts | Ethereum | UnizenDexAggr | `0x97B8210dFe6e970190c7496511F7318C91756a8b` | 1 | 1/0 | 1 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 906 | Public - Winery Smartcontracts | BNB Chain | CORK token | `0xe7eada32caf827d3ba8cb1074830d803c9bd48c3` | 1 | 1/0 | 0 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 907 | Public - Xeleb Protocol | BNB Chain | XCX token | `0xE32f9e8F7f7222fcd83EE0fC68bAf12118448Eaf` | 1 | 1/0 | 0 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 908 | Radiant V2 | Arbitrum | Leverager.loop | `0x196bF3A63c50BcA1Eff5A5809B72DFc58F0C2c1a` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/radiant |
| 909 | Railgun Privacy Contract | Ethereum | RailgunSmartWallet | `0xc0BEF2D373A1EfaDE8B952f33c1370E486f209Cc` | 1 | 1/0 | 1 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 910 | Raydium Staking | Solana | Staking program - WithdrawV2 (processor. | `EhhTKczWMGQt46ynNeRX1WfeagwwJd7ufHvCDjRxjo5Q` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/2c0cdc8b-484d-453f-9381-acad2020952c |
| 911 | Reclaim Protocol | Ethereum | Reclaim callback (claim contract) | `0x65BB2E9F1C56226109304A94d6232Bc5B10636DE` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 912 | Reclaim Protocol | Ethereum | Reclaim claim contract | `0x65BB2E9F1C56226109304A94d6232Bc5B10636DE` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 913 | Reflexer - June 24, 2021 | Ethereum | SAFEEngine (GEB core) | `0xcc88a9d330da1133df3a7bd823b95e52511a6962` | 1 | 1/0 | 1 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 914 | Reserve Protocol - October 31, 2022 | Ethereum | RToken.cancel() / issue() | `0x258ce833CF9AD19208372763A00aA1565Dd40b3C` | 1 | 1/0 | 1 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 915 | Resolv | Ethereum | stUSR | `0x1202F5C7b4B9E47a1A484E8B270be34dbbC75055` | 1 | 1/0 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 916 | Resolv | Ethereum | Resolv staking (stUSR) | `0x1202F5C7b4B9E47a1A484E8B270be34dbbC75055` | 1 | 1/0 | 1 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 917 | ResupplyFinance | Ethereum | Voter | `0x11111111408bd67B92C4f74B9D3cF96f1fa412BC` | 1 | 1/0 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 918 | ResupplyFinance | Ethereum | VestManager | `0x6666666677B06CB55EbF802BB12f8876360f919c` | 1 | 1/0 | 1 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 919 | Reya Network | Reya Network | PassivePool | `0xB4B77d6180cc14472A9a7BDFF01cc2459368D413` | 1 | 1/0 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 920 | Rocket Pool Atlas (v1.2 | Ethereum | RocketNodeDistributorDelegate | `0x35A85d4c115801395e6E3abAa784Fb05826f129D` | 1 | 1/0 | 0 | 1 | https://diligence.security/audits/2023/01/rocket-pool-atlas-v1.2/rocketpool-1-2- |
| 921 | Rocket Pool Rocket Pool – Houston Upgrade | Ethereum | RocketDAOProtocolVerifier | `0xc4D85aA3e318c38005F6D73cC53E5A2b4223723a` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 922 | Rocketpool | Ethereum | RocketTokenRETH | `0xae78736Cd615f374D3085123A210448E74Fc6393` | 1 | 1/0 | 0 | 1 | https://diligence.security/audits/2021/04/rocketpool/ |
| 923 | Royco (royco-monorepo, 2024-08-28) | Ethereum | ERC4626i | `0x36cdc586D26af6fBC6d314A8e1583Bd7C4968Ef2` | 1 | 1/0 | 1 | 1 |  |
| 924 | Royco (royco-monorepo, 2024-08-28) | Ethereum | RoycoProtocol (fillLPOrder) | `0x36cdc586D26af6fBC6d314A8e1583Bd7C4968Ef2` | 1 | 1/0 | 0 | 1 |  |
| 925 | Rubic | Ethereum | Executor, GenericCrossChainFacet (RubicM | `0x9E4B1205291d21eDaB4f710b2905628640e8D0F1` | 1 | 1/0 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 926 | SBTC Bera Vault | Ethereum | SBTCBeraVault | `0xf401Cc9f467c7046796D9A8b44b0c1348b4DEec7` | 1 | 1/0 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 927 | SOFA.org | Ethereum | LeverageDNTVault / LeverageSmartTrendVau | `0x3a253838121b9ad9736fAFc030Cf4971615D68b2` | 1 | 1/0 | 0 | 1 |  |
| 928 | SPL Token 2022 | Solana | spl-token-2022 confidential transfer (pr | `TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb` | 1 | 1/0 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 929 | SPL Token 2022 | Solana | spl-token-2022 confidential transfer (pr | `TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb` | 1 | 1/0 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 930 | SXT | Ethereum | ZKPay | `0x9E1Ee82d0ACe61B3b4FEb72B6ca0f3852b994D7E` | 1 | 1/0 | 1 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 931 | Sandbox Asset Bug Fix [15.01 | Ethereum | Asset (ERC1155) batch transfer | `0xa342f5D851E866E18ff98F351f2c6637f4478dB5` | 1 | 1/0 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 932 | Sandbox Assets Patch update [30.10 | Ethereum | Asset (Sandbox's ASSETs) | `0xa342f5D851E866E18ff98F351f2c6637f4478dB5` | 1 | 1/0 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 933 | Security Audit – Drift Protocol | Solana | Drift v2 program | `dRiftyHA39MWEi3m9aunc5MzRF1JYuBsbn6VPcn33UH` | 1 | 1/0 | 1 | 1 | https://www.neodyme.io/reports/Drift.pdf |
| 934 | Security Audit – Lido on Solana |  | Lido on Solana staking program (process_ | `Solana` | 1 | 1/0 | 1 | 1 | https://neodyme.io/reports/Lido.pdf |
| 935 | Security Audit – Mango v3 | Solana | Mango v3 Perp orderbook (Book::load_chec | `4MangoMjqJ2firMokCjjGgoK8d4MXcrgL7XJaL3w6fVg` | 1 | 1/0 | 0 | 1 | https://www.neodyme.io/reports/Mango-V3.pdf |
| 936 | Security Audit – deBridge on Solana | Solana | deBridge Solana program (signature verif | `DEbrdGj3HsRsAzx6uH4MKyREKxVAfBydijLUF3ygsFfh` | 1 | 1/0 | 1 | 1 | https://neodyme.io/reports/Debridge.pdf |
| 937 | Shield | BNB Chain | Shield | `0xd9e90df21f4229249e8841580cde7048bf935710` | 1 | 1/0 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 938 | Shift DeFi Platform | Ethereum | Vault + ReshufflingGateway | `0xd137dd4b38f4cfbd0a59acf0c5749d4b388a5689` | 1 | 1/0 | 1 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 939 | Sigma | Ethereum | sigma_factory | `0xdEde1953A890BA3819a1E27deB45932692AB4d82` | 1 | 1/0 | 1 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 940 | Smart Contracts and Circuits. | Ethereum | TornadoStakingRewards (anonymity-mining  | `0x26903a5a198D571422b2b4EA08b56a37cbD68c89` | 1 | 1/0 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 941 | Sock | Arbitrum | SockAccount (UUPS) | `0xf5771d27f4b9Ce4B8fF7740A320c6c34CF677a9D` | 1 | 1/0 | 1 | 1 |  |
| 942 | Socket Jan24 SuperToken | Arbitrum | SuperToken.mintPendingFor / SuperTokenVa | `0xbCF339DF10d78f2b44AA760EAd0F715A7A7d7269` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 943 | Socket Jan24 SuperToken | BNB Chain | SuperTokenVault.inbound -> _execute | `0xef8d3a1fd0F9a0E04D19e29e03a16CaE0b4eD1f8` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 944 | Sovryn | Rootstock | ConverterRegistry.setupConverter / sovry | `0x5a0D867E0D70FCc6ADe25c3f1B89d618b5B4EaA7` | 1 | 1/0 | 1 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 945 | Spool- -aug | Ethereum | smartVaultManager.claimSmartVaultTokens  | `0x23daf34e2b9af02a74dc19cb52af727b19403874` | 1 | 1/0 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 946 | Stader | Ethereum | StaderStakePoolsManager | `0x9dceaeB1C035C1427E64E6c6fEC61F816e0d0FF5` | 1 | 1/0 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 947 | Stader SD Utility Pool | Ethereum | SDUtilityPool | `0x3d38Bc6187Ab8403ba4fb9220D78Fb9dD0191CAC` | 1 | 1/0 | 0 | 1 |  |
| 948 | Stader Stader SD Utility Pool | Ethereum | SDUtilityPool | `0x3d38Bc6187Ab8403ba4fb9220D78Fb9dD0191CAC` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 949 | StandardBounties | Ethereum | StandardBounties.refundContribution | `0x51598ae36102010feca5322098b22dd5b773428b` | 1 | 1/0 | 1 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 950 | Starbase | Base | StarBaseDCA.fillDCA | `0xA76308F063f5B1621E259BDaD6bB6FF2aCc8Ca0B` | 1 | 1/0 | 1 | 1 |  |
| 951 | StarkNet-DAI-Bridge | Ethereum | L1DAIBridge | `0x9F96fE0633eE838D0298E8b8980E6716bE81388d` | 1 | 1/0 | 1 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 952 | Starknet Staking | Starknet | MintManager | `0xCa14076A3cec95448BaD179cc19B351A4204B88B` | 1 | 1/0 | 1 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 953 | Sunnyside Labs PrivacyBoost | Optimism | PrivacyBoost pool (Merkle tree / rollove | `0xca689828854a422CF1f778be03CA80549408F620` | 1 | 1/0 | 0 | 0 | https://github.com/sunnyside-io/privacy-boost-protocol/blob/12516dddf1788dc01691 |
| 954 | Superform v2 Periphery | Base | SuperVault | `0x11820afe50ea96851ee2bdbae329d97771e41ec6` | 1 | 1/0 | 1 | 1 | https://cdn.cantina.xyz/reports/Superform-v2-periphery-Spearbit-Security-Review- |
| 955 | Superstate-7 | Ethereum | USTB token (Superstate Short Duration US | `0x43415eB6ff9DB7E26A15b704e7A3eDCe97d31C4e` | 1 | 1/0 | 0 | 1 | https://0xmacro.com/library/audits/superstate-7 |
| 956 | Sushi | Ethereum | SushiXSwap (ACTION_DST_WITHDRAW_FROM_BEN | `0x011E52E4E40CF9498c79273329E8827b21E2e581` | 1 | 1/0 | 0 | 1 |  |
| 957 | Sushi SushiXSwap and StablePool | Ethereum | SushiXSwap | `0x011E52E4E40CF9498c79273329E8827b21E2e581` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 958 | Sushi Swap Auction Maker and Furo | Ethereum | FuroStream | `0x4F74B61f78179DA88C9507955d0d97Cf3B486ca5` | 1 | 1/0 | 1 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 959 | SushiSwap FundsReturner | Ethereum | SushiFundsReturner | `0xBD845586EF2c049D51883F41B78A668f8C959204` | 1 | 1/0 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 960 | Synthetix TLX V2 | Optimism | LeveragedTokenFactory / LeveragedToken | `0x26647E97d805B478B37D2D8653C41632C112aE65` | 1 | 1/0 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 961 | THORSwap Aggregators | BNB Chain | TSAggregatorGeneric | `0xb6FA6f1dCd686f4A573fD243a6fABb4Ba36ba98C` | 1 | 1/0 | 1 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 962 | TLX | Optimism | Bonding | `0xD55c83Fb5BD360362Cc95577D0AaF52861DA2F43` | 1 | 1/0 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 963 | Taiko | Ethereum | Bridge (L1) | `0xd60247c6848B7Ca29eDdF63AA924E53dB6Ddd8EC` | 1 | 1/0 | 1 | 1 |  |
| 964 | Taiko Protocol | Ethereum | TaikoL1.proposeBlock -> AssignmentHook.o | `0x06a9Ab27c7e2255df1815E6CC0168d7755Feb19a` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/taiko-protocol-audit |
| 965 | Taiko Shasta Protocol | Ethereum | Inbox proof verification (verifier set) | `0x6f21C543a4aF5189eBdb0723827577e1EF57ef1f` | 1 | 1/0 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 966 | Taiko Taiko | Ethereum | Bridge (L1) | `0xd60247c6848B7Ca29eDdF63AA924E53dB6Ddd8EC` | 1 | 1/0 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 967 | TapiocaDAO | Arbitrum | YieldBox / GlpStrategy | `0xCFFd997DB053c0fC54010770b55A4E02B1D104a5` | 1 | 1/0 | 1 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 968 | Term Finance Term Finance Contracts | Ethereum | signature verification path | `0x2879C9D15406e7EBD46770f4B0781Fe665f9da1b` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 969 | Term Finance Term Finance Contracts | Ethereum | TermController | `0x2879C9D15406e7EBD46770f4B0781Fe665f9da1b` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 970 | Term Finance Term Finance Contracts | Ethereum | TermAuctionBidLocker (bid collateral) | `0x2879C9D15406e7EBD46770f4B0781Fe665f9da1b` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 971 | Term Finance Term Finance Contracts | Ethereum | TermAuction (cancel) | `0x2879C9D15406e7EBD46770f4B0781Fe665f9da1b` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 972 | Thala Labs | Aptos | Thala CDP protocol module (accumulated_g | `0x7fd500c11216f0fe3095d0c4b8aa4d64a4e2e04f83758462f2b127255643615` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/15cc0d5e-3e41-4ceb-8382-db44d05a7cc1 |
| 973 | Tokemak (Dec 2024) | Ethereum | AutopilotRouter.redeemWithRoutes + SwapR | `0xC23a37Adf8F104d442b438f94c0534514ceA893E` | 1 | 1/0 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 974 | Tracer (Sigma Prime review) | Arbitrum | Pricing.updatePrice (library called by L | `0x3Feafee6b12C8d2E58c5B118e54C09F9273c6124` | 1 | 1/0 | 0 | 1 |  |
| 975 | Tribal - Protocol Smart Contract Security | Ethereum | TribalToken | `0x6988a804c74fd04f37da1ea4781cea68c9c00f86` | 1 | 1/0 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 976 | UNCX UniswapV3 Liquidity Locker | Ethereum | UniswapV3Locker | `0xFD235968e65B0990584585763f837A5b5330e6DE` | 1 | 1/0 | 0 | 1 | https://www.openzeppelin.com/news/uncx-uniswapv3-liquidity-locker-audit |
| 977 | Umami | Arbitrum | Umami gmUSDC vault (RequestHandler) | `0x959f3807f0Aa7921E18c78B00B2819ba91E52FeF` | 1 | 1/0 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 978 | Umami DAO | Arbitrum | TracerGMXVault.commitAndClose | `0x959f3807f0Aa7921E18c78B00B2819ba91E52FeF` | 1 | 1/0 | 1 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 979 | Umami DAO | Arbitrum | MarinateV2 (stake/withdraw) | `0x2adabd6e8ce3e82f52d9998a7f64a90d294a92a4` | 1 | 1/0 | 0 | 1 | https://2316168122-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 980 | Uniswap v4 Core | Celo | PoolManager (settle/take) | `0x288dc841A52FCA2707c6947B3A777c5E56cd87BC` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/uniswap-v4-core-audit |
| 981 | Uniswap v4 Periphery and Universal Router | Ethereum | PositionManager._increase | `0xbd216513d74c8cf14cf4747e6aaa6420ff64ee9e` | 1 | 1/0 | 1 | 1 | https://www.openzeppelin.com/news/uniswap-v4-periphery-and-universal-router-audi |
| 982 | Uniswap: The Compact | Ethereum | EmissaryLib / TheCompact | `0x00000000000000171ede64904551eeDF3C6C9788` | 1 | 1/0 | 0 | 1 | https://cdn.cantina.xyz/reports/Uniswap-The-Compact-Spearbit-Security-Review-May |
| 983 | Unmarshal May13 | Ethereum | MARSH token | `0x5a666c7d92E5fA7Edcb6390E4efD6d0CDd69cF37` | 1 | 1/0 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 984 | VMEX Finance | Optimism | LendingPool.borrow -> ValidationLogic.va | `0x60F015F66F3647168831d31C7048ca95bb4FeaF9` | 1 | 1/0 | 1 | 1 | https://1688608737-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 985 | Vaultka Aug6th | Arbitrum | VodkaVault | `0x0081772FD29E4838372CbcCdD020f53954f5ECDE` | 1 | 1/0 | 1 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 986 | Vaultka Nov9 | Arbitrum | VKA token | `0xafccb724e3aec1657fc9514e3e53a0e71e80622d` | 1 | 1/0 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 987 | Velvet Capital | BNB Chain | Velvet Capital vault proxy | `0x0bb0c08fd9eeaf190064f4c66f11d18182961f77` | 1 | 1/0 | 1 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 988 | Venom Foundation - VenomBridge MultiVault | Ethereum | MultiVault (VenomBridge) | `0x4aB740157721105aE503fbad756a578171512525` | 1 | 1/0 | 0 | 1 |  |
| 989 | VirtuSwap | Ethereum | VRSW token | `0x99A01A4d6a4D621094983050D9A2F10B2912e53D` | 1 | 1/0 | 0 | 1 | https://github.com/pessimistic-io/audits/blob/d45fd8767d769729e378a82beb6fbcad7c |
| 990 | WOOFI Stake | Arbitrum | RewardCampaignManager | `0x2EBCA56e00E11a4b1F08DA6eb9bC97C4Bf3eE90f` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 991 | Wasabi Perps | Base | WasabiShortPool | `0xA456c77d358C9c89f4DFB294fA2a47470b7dA37c` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 992 | Waterfall DeFi Mainnet | BNB Chain | Tranche / swap entry point | `0xd73F32833B6D5D9c8070c23e599e283a3039823C` | 1 | 1/0 | 0 | 1 | https://github.com/WaterfallDefi/Waterfall-audit/blob/93815534dd1e86915a56b3acca |
| 993 | Wormhole Near | NEAR | deploy_wrapped_nft (Wormhole core, Near) | `contract.wormhole_crypto.near` | 1 | 1/0 | 0 | 1 | https://osec.io/reports/dd777b3d-f8bf-4507-8971-fe949bcf9355 |
| 994 | Xave Protocol | Ethereum | XAV token | `0x40370aEd88933021e20CF7C4D67E00417CdA2202` | 1 | 1/0 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 995 | Yala Stablecoin | Ethereum | PSM | `0x0b4e03ECb66be6774c216EA9ecA3663A85eE41fd` | 1 | 1/0 | 1 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 996 | Yelay ERC4626 | Ethereum | ERC4626Plugin | `0xAEe5913FFd19dBcA4Fd1eF6F3925ed0414407d37` | 1 | 1/0 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 997 | Yield Basis core | Ethereum | YB factory / per-pool YB contracts | `0x370a449FeBb9411c95bf897021377fe0B7D100c0` | 1 | 1/0 | 0 | 1 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 998 | YieldBasisDAO UpdateSecurityReview | Ethereum | VotingEscrow (veYB) | `0x8235c179E9e84688FBd8B12295EfC26834dAC211` | 1 | 1/0 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 999 | ZKsync Custom Asset Bridge | zkSync Era | L2NativeTokenVault.bridgeMint | `0x0000000000000000000000000000000000010004` | 1 | 1/0 | 1 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 1000 | Zero Knowledge | Ethereum | Blobstream X | `0x41a87C543EBcbD93706CF5260AD057D9eCBA1caE` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1001 | Zero Knowledge | Ethereum | DataCommitmentBuilder (Blobstream X) | `0x41a87C543EBcbD93706CF5260AD057D9eCBA1caE` | 1 | 1/0 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1002 | Zunami | Ethereum | Zunami Protocol (ZUNAMI token) | `0x7c06516cD9b37089D7FC641CC29eD6eCeDff6ffe` | 1 | 1/0 | 0 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 1003 | ackee--hyperlend | HyperEVM | Pool (oracle price consumption) | `0x00A89d7a5A02160f20150EbEA7a2b5E4879A1A8b` | 1 | 1/0 | 0 | 1 | https://github.com/hyperlendx/audits/blob/8370c4c72a07ccbefa78369efa0a33c80ed6f8 |
| 1004 | blocksquare | Ethereum | LPStaking (deployed as BSPTStaking) | `0x57ba886442d248C2E7a3a5826F2b183A22eCc73e` | 1 | 1/0 | 0 | 1 |  |
| 1005 | core contracts token bridge | Ethereum | L1ArbitrumGateway.outboundTransfer | `0x72Ce9c846789fdB6fC1f34aC4AD25Dd9ef7031ef` | 1 | 1/0 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 1006 | cow-protocol-composablecow-extensiblefallbackhandler | Ethereum | ComposableCoW | `0xfdaFc9d1902f4e0b84f65F49f244b32b31013b74` | 1 | 1/0 | 0 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 1007 | eesee | Ethereum | Eesee / EeseeERC20 (createLots) | `0xE363D20dfC0e68fb1da7669216826010275aE6dc` | 1 | 1/0 | 0 | 1 |  |
| 1008 | eesee | Ethereum | ESE token (Eesee) | `0x908dDb096BFb3AcB19e2280aAD858186ea4935C4` | 1 | 1/0 | 0 | 1 |  |
| 1009 | eigenlayer | Ethereum | EigenPod (BeaconChainProofs.verifyWithdr | `0x5a2a4F2F3C18f09179B6703e63D9eDD165909073` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1010 | ether.fi - October 26, 2023 | Ethereum | StakingManager.batchCancelDeposit | `0x25e821b7197B146F7713C3b89B6A4D83516B912d` | 1 | 1/0 | 1 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1011 | ether.fi - October 26, 2023 | Ethereum | EtherFiNodesManager | `0x8B71140AD2e5d1E7018d2a7f8a288BD3CD38916F` | 1 | 1/0 | 1 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1012 | for Alien Base | Base | EpsilonRouter.registerOrder | `0x303ca5c65AabCb1CE242DF93F478c41E0E4D2580` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1013 | for JuiceSwap | Citrea | MintingHub | `0x372368ca530B4d55622c24E28F0347e26caDc64A` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1014 | gumball | Arbitrum | Gumbar | `0xf5cfBaF55036264B902D9ae55A114d9A22c42750` | 1 | 1/0 | 1 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 1015 | jonesdao-jgm | Arbitrum | JGM vault (liquidated users) | `0xBEF7a31efabc9F9e80f9CcD4f03CE2D7EcbfDaf9` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1016 | jonesdao-jgm | Arbitrum | JGM strategy (cancellation callback) | `0xBEF7a31efabc9F9e80f9CcD4f03CE2D7EcbfDaf9` | 1 | 1/0 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1017 | lending and margin trading programs | Solana | Sendit program (_redeem_reserve_collater | `SenditXmUCHPeV6iyFoMY8dRNB4PofGKTfp52hEWpJx` | 1 | 1/0 | 1 | 1 | https://www.neodyme.io/reports/SendIt.pdf |
| 1018 | marginfi | Solana | marginfi v2 program | `MFv2hWf31Z9kbCa1snEPYctwafyhdvnV7FZnsebVacA` | 1 | 1/0 | 1 | 1 | https://osec.io/reports/3be56f77-402a-4d3c-ac8b-626c3c23ec1a |
| 1019 | metadao-the-fundraising-and | Solana | futarchy program: withdraw_liquidity ->  | `FUTARELBfJfQ8RDGhg1wdhddq1odMAJUePHFuBYfUxKq` | 1 | 1/0 | 0 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 1020 | new feature which enables users to | Orderly L2 | Orderly LedgerCrossChainManager (Ledger  | `0xa0a07a78c7d31E6f8698F48Fc9219f9a3030f38C` | 1 | 1/0 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1021 | oro inti | Solana | Gold (GOLD) mint | `GoLDppdjB1vDTPSGxyMJFqdnj134yH6Prg9eqsGDiw6A` | 1 | 1/0 | 1 | 1 |  |
| 1022 | pancakeswap | BNB Chain | BinPoolManager (_updateBin) | `0xC697d2898e0D09264376196696c51D7aBbbAA4a9` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1023 | pancakeswap | BNB Chain | BinPositionManager (addLiquidity) | `0x3D311D6283Dd8aB90bb0031835C8e606349e2850` | 1 | 1/0 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1024 | pashov-solo-2023-11-17-florencefinance-security-re | Base | FlorinTreasury.depositEUR | `0xD850C9cBbD314b9A5ceaCF9C9668676137a3e28B` | 1 | 1/0 | 1 | 1 |  |
| 1025 | pashov-solo-2023-11-17-hypercerts-security-review | Optimism | HypercertMinter._splitValue (ERC1155 spl | `0x822F17A9A5EeCFd66dBAFf7946a8071C265D1d07` | 1 | 1/0 | 0 | 1 |  |
| 1026 | pashov-team-2024-03-25-fyde-security-review | Ethereum | Fyde YieldManager | `0xB615A7E4D1Ed426470Ac2Df14F3153fA2DcCC3ba` | 1 | 1/0 | 0 | 1 |  |
| 1027 | pashov-team-2024-04-10-reyanetwork-security-review | Reya Network | OracleAdaptersProxy (DivReducerNode adap | `0x32edABC058C1207fE0Ec5F8557643c28E4FF379e` | 1 | 1/0 | 0 | 1 |  |
| 1028 | pashov-team-2024-07-15-lucidly-security-review |  | Lucidly pool removeLiquiditySingle | `Ethereum` | 1 | 1/0 | 1 | 1 |  |
| 1029 | pashov-team-2024-07-15-lucidly-security-review |  | Lucidly virtual-balance product math | `Ethereum` | 1 | 1/0 | 0 | 1 |  |
| 1030 | pashov-team-2024-08-15-layerzerozroclaim-security- | Ethereum | ZRO Claim | `0xC28C2b2F5A9B2aF1ad5878E5b1AF5F9bAEa2F971` | 1 | 1/0 | 1 | 1 |  |
| 1031 | pashov-team-2024-10-24-dyad-security-review | Ethereum | Kerosene (KERO) | `0xf3768D6e78E65FC64b8F12ffc824452130BD5394` | 1 | 1/0 | 0 | 1 |  |
| 1032 | pashov-team-2024-11-21-bunni-security-review-octob | Ethereum | MasterBunni | `0x0000009856ebF1B73B431Fb59F2a2F200E9e78B0` | 1 | 1/0 | 1 | 1 |  |
| 1033 | pashov-team-2025-04-30-blueberry-security-review | Ethereum | BlueberryBank | `0x9b06eA9Fbc912845DF1302FE1641BEF9639009F7` | 1 | 1/0 | 1 | 1 |  |
| 1034 | pashov-team-2025-06-28-rivus-security-review | Ethereum | RivusTAO (deployment 1) | `0x01cF29c7763C346BFf038BA4405a37CC343ed556` | 1 | 1/0 | 0 | 1 |  |
| 1035 | pashov-team-2025-07-25-resolv-security-review | Ethereum | Resolv staking | `0xFE4BCE4b3949c35fB17691D8b03c3caDBE2E5E23` | 1 | 1/0 | 1 | 1 |  |
| 1036 | public-polygon-zkevm | Ethereum | PolygonZkEVM (subFpBN254) | `0x5132A183E9F3CB7C848b0AAC5Ae0c4f0491B7aB2` | 1 | 1/0 | 0 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 1037 | public-polygon-zkevm | Ethereum | PolygonZkEVM (invFp2BN254.zkasm) | `0x5132A183E9F3CB7C848b0AAC5Ae0c4f0491B7aB2` | 1 | 1/0 | 0 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 1038 | pwn-protocol | Ethereum | PWNSimpleLoan | `0x50160ff9c19fbE2B5643449e1A321cAc15af2b2C` | 1 | 1/0 | 1 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 1039 | ramses v3 | Arbitrum | RamsesV3Pool (per-pair, deployed by Rams | `0xb722efaAbe807FAeA16068f595EaA9aa1a62CECD` | 1 | 1/0 | 0 | 1 | https://diligence.consensys.io/audits/2024/08/ramses-v3/ramses-v3-audit-2024-07. |
| 1040 | rhinestone-safe7579 | Ethereum | Safe7579Launchpad.initialize | `0x7579011aB74c46090561ea277Ba79D510c6C00ff` | 1 | 1/0 | 1 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 1041 | sigmaprime botanix sigma prime botanix macbeth security asse | Botanix | Pegged Bitcoin (pBTC) | `0x0D2437F93Fed6EA64Ef01cCde385FB1263910C56` | 1 | 1/0 | 0 | 1 |  |
| 1042 | sigmaprime omni network sigma prime omni solvernet security  | Ethereum | SolverNetInbox | `0x930c08ec262Bce2489CaE1Ca822b38A24bd97fBD` | 1 | 1/0 | 1 | 1 |  |
| 1043 | sigmaprime rocket pool rocket | Ethereum | RocketDAOProtocolVerifier | `0xc4D85aA3e318c38005F6D73cC53E5A2b4223723a` | 1 | 1/0 | 0 | 1 |  |
| 1044 | stakewise- -sept | Ethereum | StakeWise V3 core proxy | `0x48c3399719b582dd63eb5aadf12a40b4c3f52fa2` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1045 | taiko-alethia-pacaya-upgrade | Ethereum | ERC20Vault.handleMessage | `0x024253C6FDC27d3161aFd43fb0241411A28dDc3c` | 1 | 1/0 | 1 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 1046 | team 2025 01 29 burve | Berachain | Burve Diamond | `0xa1beD164c12CD9479A1049f97BDe5b3D6EC21089` | 1 | 1/0 | 0 | 1 |  |
| 1047 | team 2025 06 28 gatekeeper | Solana | saguaro_gatekeeper.append_data_sandwich_ | `saGUaroo4mjAcckhEPhtSRthGgFLdQpBvQvuwdf7YG3` | 1 | 1/0 | 0 | 1 |  |
| 1048 | team 2025 06 28 subsquid | Arbitrum | GatewayRegistry | `0x8a90a1ce5fa8cf71de9e6f76b7d3c0b72feb8c4b` | 1 | 1/0 | 0 | 1 |  |
| 1049 | tokemak-acctoke-migration-sep-24 | Ethereum | DestinationVaultMainRewarder | `0x00bcD61A6C638046fD500Ae8449120f50F39B614` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1050 | unknown (hf: 2024-04-29-sigmaprime-term-finance-term1-review |  | Term Repo bid validation vs collateral l | `Ethereum` | 1 | 1/0 | 1 | 1 |  |
| 1051 | unknown (hf: pashov-team-2024-02-01-saffron-security-review) | Ethereum | SFI token | `0xb753428af26e81097e7fd17f40c88aaa3e04902c` | 1 | 1/0 | 0 | 1 |  |
| 1052 | unknown (hf: pashov-team-2024-11-05-bunni-security-review-au | Ethereum | ERC20Referrer._mint referrer change | `0x000000dceb71f3107909b1b748424349bfde5493` | 1 | 1/0 | 0 | 1 |  |
| 1053 | unknown (hf: pashov-team-2025-06-28-catalyst-security-review | Base | Catalyst factory | `0x00000000E5E81E25aeaD7fCCb4C9560C6b5b718F` | 1 | 1/0 | 1 | 1 |  |
| 1054 | v2 Contracts | Ethereum | TermRepoToken (OFT) | `0xb4B1de03F229220eDbBB31A224b2a004b3c3e47f` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1055 | v2 Contracts | Ethereum | TermAuctionBidLocker rollover path | `0xb4B1de03F229220eDbBB31A224b2a004b3c3e47f` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1056 | v2 Contracts | Ethereum | TermRepoTokenIntentFacet / TermLoanInten | `0xb4B1de03F229220eDbBB31A224b2a004b3c3e47f` | 1 | 1/0 | 1 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1057 | v2 Contracts | Ethereum | TermMorphoInterfaceFacet | `0xb4B1de03F229220eDbBB31A224b2a004b3c3e47f` | 1 | 1/0 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1058 | v2 Contracts | Ethereum | TermDiamond | `0xb4B1de03F229220eDbBB31A224b2a004b3c3e47f` | 1 | 1/0 | 0 | 0 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1059 | valantis-mar-25 | Hyperliquid | STEXAMM | `0x39694eFF3b02248929120c73F90347013Aec834d` | 1 | 1/0 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1060 | valantis-mar-25 | Hyperliquid | STEXAMM (SovereignPool) | `0x39694eFF3b02248929120c73F90347013Aec834d` | 1 | 1/0 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1061 | wake-arena-ai--ipor-labs-fusion-dec-11 | Ethereum | SwapExecutorEth | `0xE04c1b03811a78984e5006FF54dFaA1FdEFD0d45` | 1 | 1/0 | 1 | 1 | https://github.com/Ackee-Blockchain/public-wake-arena-reports/blob/e6553332fd1e5 |
| 1062 | with DeFi Saver to | Ethereum | RecipeExecutor (with FLAaveV2/FLDyDx fla | `0xbc3Fc959FeF3F12a41738f406c02198cdeE7481F` | 1 | 1/0 | 0 | 1 | https://diligence.security/audits/2021/03/defi-saver/defisaver-audit-2021-03.pdf |
| 1063 | yAudit Olympus Emission Manager | Ethereum | EmissionManager | `0xA61b846D5D8b757e3d541E0e4F80390E28f0B6Ff` | 1 | 1/0 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1064 | yPrisma | Ethereum | YearnBoostedStaker.checkpointAccountWith | `0xF4C6e0E006F164535508787873d86b84fe901975` | 1 | 1/0 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1065 | 01 08 Ajna-FV-MR | Ethereum | Ajna ERC20 Pool (deposit/borrow/kick/set | `0x6146DD43C5622bB6D12A5240ab9CF4de14eDC625` | 1 | 0/1 | 1 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1066 | 01--TempleDao-Origami | Arbitrum | Origami harvest vault (ovGMX) | `0xe488A643E4b0Aaae60E4bdC02045a10d8a323bae` | 1 | 0/1 | 0 | 1 | https://github.com/yAudit/reports-pdf/blob/186eab01a540d4815784bf79356dc7bcf4422 |
| 1067 | 02 12 Whetstone Doppler-MR | Ethereum | UniswapV2MigratorSplit | `0xd7aba5f1d80a330a6fe9e96f7ba122710e0912d3` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1068 | 03 17 TraderJoe Rocket Joe Staking-FV | Avalanche | RocketJoeStaking | `0x102D195C3eE8BF8A9A89d63FB3659432d3174d81` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1069 | 03--EulerV2 | Ethereum | EVaultFactory | `0x29a56a1b8214D9Cf7c5561811750D5cBDb45CC8e` | 1 | 0/1 | 1 | 1 | https://github.com/yAudit/reports-pdf/blob/186eab01a540d4815784bf79356dc7bcf4422 |
| 1070 | 04 13 Umia-MR | Base | UmiaHub (TWAP / pricing) | `0x120dbCDd58Bb787309573e29159fE6D37A1983F6` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1071 | 05--Sonne | Optimism | Sonne Comptroller | `0x60CF091cD3f50420d50fD7f707414d0DF4751C58` | 1 | 0/1 | 1 | 1 | https://github.com/yAudit/reports-pdf/blob/186eab01a540d4815784bf79356dc7bcf4422 |
| 1072 | 06--RAMSES | Arbitrum | RAM token | `0xAAA6C1E32C55A7BFA8066A6FAE9B42650F262418` | 1 | 0/1 | 0 | 1 | https://github.com/yAudit/reports-pdf/blob/186eab01a540d4815784bf79356dc7bcf4422 |
| 1073 | 07 16 Solana Stake-Pool Formal Verification | Solana | Stake Pool program | `SPoo1Ku8WFXoNDMHPsrGSTSG1Y47rzgn41SLUNakuHy` | 1 | 0/1 | 1 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1074 | 0x Exchange v4 | Ethereum | 0x Exchange Proxy (v4) | `0xDef1C0ded9bec7F1a1670819833240f027b25EfF` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2020/12/0x-exchange-v4/ |
| 1075 | 109 Wardens contributed reports to the Astaria | Ethereum | LienToken auction | `0x6D0F425adc5a61F78A43460c5929B84f3e71E67E` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-01-astaria-findings/blob/8059d5e7c4b3b7155259 |
| 1076 | 109 Wardens contributed reports to the Astaria | Ethereum | CollateralToken.liquidatorNFTClaim -> Cl | `0x6112d87127847202151b9fe48ea0e2704fa428a1` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-01-astaria-findings/blob/8059d5e7c4b3b7155259 |
| 1077 | 109 Wardens contributed reports to the Astaria | Ethereum | LienToken refinancing / auction | `0x6D0F425adc5a61F78A43460c5929B84f3e71E67E` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-01-astaria-findings/blob/8059d5e7c4b3b7155259 |
| 1078 | 11 05 Popsicle V3 Optimizer-FV | Ethereum | ICE token (Popsicle Finance) | `0xf16e81dce15B08F326220742020379B855B87DF9` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1079 | 11 26 Alluvial LiquidCollective-FV-MR | Ethereum | River.sol | `0x8c1BEd5b9a0928467c9B1341Da1D7BD5e10b6549` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1080 | 11 27 Balancer V3-FV-MR | Ethereum | Balancer V3 Vault | `0xbA1333333333a1BA1108E8412f11850A5C319bA9` | 1 | 0/1 | 1 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1081 | 11 30 Euler-FV | Ethereum | Euler proxy (swap/allowance path) | `0x27182842E098f60e3D576794A5bFFb0777E025d3` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1082 | 12 12 Liquity Bold-FV | Ethereum | BOLD token | `0x6440f144b7e50D6a8439336510312d2F54beB01D` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1083 | 12 29 Aave stkToken v1 5-FV | Ethereum | StakedAave (stkAAVE) unstake window | `0x4da27a545c0c5B758a6BA100e3a049001de870f5` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1084 | 1inch Cross Chain Swap v2 | Ethereum | EscrowFactory / EscrowSrc (partial fills | `0x03a25b3215a0e5c15cf23ac4d2e5cf86c0ff7efa` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2024/07/1inch-cross-chain-swap-v2/ |
| 1085 | 1inch Cross-Chain Swaps V2 | Arbitrum | 1inch Escrow Factory | `0xa7bCb4EAc8964306F9e3764f67Db6A7af6DdF99A` | 1 | 0/1 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 1086 | 1inch Exchange AggregationRouter V5 | Ethereum | AggregationRouterV5 (ECDSA library) | `0x1111111254EEB25477B68fb85Ed929f73A960582` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2022/08/1inch-exchange-aggregationrouter-v5/1i |
| 1087 | 1inch-mar-23(Public | Ethereum | 1inch Limit Order Protocol v4 (Router v6 | `0x111111125421cA6dc452d289314280a0f8842A65` | 1 | 0/1 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1088 | 2017-10-ethereum-evm-sai | Ethereum | Sai Tub (DSMath) | `0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359` | 1 | 0/1 | 0 | 1 |  |
| 1089 | 2017-10-ethereum-evm-sai | Ethereum | Sai deployment (Tub/Vox) | `0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359` | 1 | 0/1 | 0 | 1 |  |
| 1090 | 2019-09-0x-v3-exchange | Ethereum | ExchangeProxy (OrderMixin.fillOrder) | `0xDef1C0ded9bec7F1a1670819833240f027b25EfF` | 1 | 0/1 | 1 | 1 |  |
| 1091 | 2019-09-ethereum-evm-aaveprotocol | Ethereum | LendingPoolCore.updateReserveTotalBorrow | `0x3dfd23A6c5E8BbcFc9581d2E864a68feb6a076d3` | 1 | 0/1 | 0 | 1 |  |
| 1092 | 2019-09-ethereum-evm-flexa | Ethereum | Flexacoin (FXC) token | `0x4a57E687b9126435a9B19E4A802113e266AdeBde` | 1 | 0/1 | 0 | 1 |  |
| 1093 | 2020-05-mcdex-mai-protocol-v2 | Ethereum | MaiProtocol (Perpetual) | `0xC73c11be38291C7702e709f8d8196cD533439777` | 1 | 0/1 | 0 | 1 |  |
| 1094 | 2020-12-04-derivadex-deriva | Ethereum | DDX token (DerivaDAO) | `0x3A880652F47bFaa771908C07Dd8673A787dAEd3A` | 1 | 0/1 | 0 | 1 |  |
| 1095 | 2020-12-14-raricapital-rari | Ethereum | RariGovernanceTokenDistributor (RGT clai | `0xD291E7a03283640FDc51b121aC401383A46cC623` | 1 | 0/1 | 0 | 1 |  |
| 1096 | 2021-02-25-wowswap-sca-wowswap-erc20-feb2021-sca-wowswap-erc | BNB Chain | WOWswap ERC20 (WOWToken) | `0x4DA996C5Fe84755C80e108cf96Fe705174c5e36A` | 1 | 0/1 | 0 | 1 |  |
| 1097 | 2021-04-02-anystake-sca-anystake-staking-apr2021-sca-anystak | Ethereum | AnyStake | `0x95EF77772BdAEF25B56ec5f210e02BdaAc40D144` | 1 | 0/1 | 0 | 1 |  |
| 1098 | 2021-05-ethereum-evm-opyn-gamma-protocol | Ethereum | GammaController | `0x4ccc2339F87F6c59c6893E1A678c2266cA58dC72` | 1 | 0/1 | 0 | 1 |  |
| 1099 | 2021-05-pooltogether-sushi-and-yearn-v2-yield-sources | Ethereum | POOL token | `0x0cec1a9154ff802e7934fc916ed7ca50bde6844e` | 1 | 0/1 | 0 | 1 |  |
| 1100 | 2021-06-12-bunicorn-sca-bunicorn-governance-erc20- | BNB Chain | BuniCornPool.swap | `0x86873f85bc12ce40321340392c0ff39c3bdb8d68` | 1 | 0/1 | 1 | 1 |  |
| 1101 | 2021-07-30-cryptex-finance-cryptex | Ethereum | Cryptex vesting / reward contract (claim | `0xc8BB1cd417D20116387a5e0603e195cA4f3Cf59A` | 1 | 0/1 | 0 | 1 |  |
| 1102 | 2021-08-18-dehive-sca-dehive-erc20-staking-aug2021-sca-dehiv | Ethereum | DHV token | `0x62Dc4817588d53a056cBbD18231d91ffCcd34b2A` | 1 | 0/1 | 0 | 1 |  |
| 1103 | 2021-08-31-badger-ibbtc-badger | Ethereum | ibBTC (Interest-Bearing BTC) | `0xc4E15973E6fF2A35cC804c2CF9D2a1b817a8b40F` | 1 | 0/1 | 0 | 1 |  |
| 1104 | 2021-09-20-tokemak-tokemak | Ethereum | Tokemak v2 System Registry | `0x2218F90A98b0C070676f249EF44834686dAa4285` | 1 | 0/1 | 1 | 1 |  |
| 1105 | 2021-09-ethereum-evm-yieldv2 | Ethereum | Witch / strategy pool | `0x08d2F5c96bB1F6BE04B49bcD869d5Af01db4c400` | 1 | 0/1 | 0 | 1 |  |
| 1106 | 2021-09-ethereum-evm-yieldv2 | Ethereum | Witch | `0x08d2F5c96bB1F6BE04B49bcD869d5Af01db4c400` | 1 | 0/1 | 1 | 1 |  |
| 1107 | 2021-10-ethereum-evm-fujiprotocol | Ethereum | FujiERC1155 | `0x1Cf24e4eC41DA581bEe223E1affEBB62a5A95484` | 1 | 0/1 | 0 | 1 |  |
| 1108 | 2021-12-frax-finance-fraxq42021 | Ethereum | OHM_AMO spot price | `0x89a5CeC88598c0CE4d4E331D0b027499edd3dfFa` | 1 | 0/1 | 0 | 1 |  |
| 1109 | 2021-12-frax-finance-fraxq42021 | Ethereum | MIM_Convex_AMO.showAllocations / calc_wi | `0x31183a2CCe8d1BFBBFE140Ea1A1264A454Fc821E` | 1 | 0/1 | 0 | 1 |  |
| 1110 | 2021-12-frax-finance-fraxq42021 | Ethereum | FraxPoolV3.redeemFrax | `0x80c72d42846EFf15Cb1BDEE8FeC9A57594F17960` | 1 | 0/1 | 0 | 1 |  |
| 1111 | 2022-03-fuji-protocol | Ethereum | Controller.depositAndBorrow / token inte | `0x3f366802F4e7576FC5DAA82890Cc6e04c85f3736` | 1 | 0/1 | 0 | 1 |  |
| 1112 | 2022-03-fuji-protocol | Ethereum | Controller.paybackAndWithdraw (ICEr20 re | `0x3f366802F4e7576FC5DAA82890Cc6e04c85f3736` | 1 | 0/1 | 0 | 1 |  |
| 1113 | 2022-03-fuji-protocol | Ethereum | Controller.depositAndBorrow / paybackAnd | `0x3f366802F4e7576FC5DAA82890Cc6e04c85f3736` | 1 | 0/1 | 0 | 1 | https://diligence.consensys.io/audits/2022/03/fuji-protocol/fuji-protocol-audit- |
| 1114 | 2022-04-mimo | Ethereum | PARMinerV2 (liquidate router call) | `0x6D0a6e30eCeE498f64F77c59e3ddedC02b7d9770` | 1 | 0/1 | 0 | 1 |  |
| 1115 | 2022-04-mimo | Ethereum | PARMiner | `0x6D0a6e30eCeE498f64F77c59e3ddedC02b7d9770` | 1 | 0/1 | 0 | 1 |  |
| 1116 | 2022-05-17-playswoops-play | Polygon | SwoopsMint | `0x5c4B55C353144BA2aabA5Fe77E30D5ce138Fd589` | 1 | 0/1 | 0 | 1 |  |
| 1117 | 2022-05-25-capsulenft-capsule | Ethereum | CapsuleFactory | `0x68dF2bB8515B32819f0592F277Af6EC0cd85ae08` | 1 | 0/1 | 0 | 1 |  |
| 1118 | 2022-05-25-capsulenft-capsule | Ethereum | CapsuleFactory (initialize) | `0x68dF2bB8515B32819f0592F277Af6EC0cd85ae08` | 1 | 0/1 | 0 | 1 |  |
| 1119 | 2022-06-11-astra-dao-sca-astra-dao-erc20-staking-jun2022-sca | Arbitrum | Astra DAO core deployment | `0xd3188e0df68559c0B63361f6160c57Ad88B239D8` | 1 | 0/1 | 0 | 1 |  |
| 1120 | 2022-07-ethereum-evm-beanstalk-securityreview | Ethereum | Beanstalk Diamond (Field/sow) | `0xC1E088fC1323b20BCBee9bd1B9fC9546db5624C5` | 1 | 0/1 | 0 | 1 |  |
| 1121 | 2022-08-frax | Ethereum | FraxlendPair | `0x794F6B13FBd7EB7ef10d1ED205c9a416910207Ff` | 1 | 0/1 | 0 | 1 |  |
| 1122 | 2022-10-blur | Ethereum | ExecutionDelegate | `0x00000000000111AbE46ff893f3B2fdF1F759a8A8` | 1 | 0/1 | 0 | 1 |  |
| 1123 | 2022-12-tigris | Arbitrum | Position.mint | `0x09d74999e5315044956ad15d5f2aeb8d393e85ed` | 1 | 0/1 | 0 | 1 |  |
| 1124 | 2022-12-tigris | Arbitrum | TigrisTrading.addToPosition | `0xd89B4B1C8918150f137cc68E83E3876F9e309aB9` | 1 | 0/1 | 0 | 1 |  |
| 1125 | 2022-12-tigris | Arbitrum | TigrisTrading.limitClose | `0xd89B4B1C8918150f137cc68E83E3876F9e309aB9` | 1 | 0/1 | 1 | 1 |  |
| 1126 | 2022-12-tigris | Arbitrum | TradingLibrary.pnl | `0xd89B4B1C8918150f137cc68E83E3876F9e309aB9` | 1 | 0/1 | 1 | 1 |  |
| 1127 | 2022-12-tigris | Arbitrum | StableVault mint/burn | `0xe82fcefbDD034500B5862B4827CAE5c117f6b921` | 1 | 0/1 | 1 | 1 |  |
| 1128 | 2023-01-24-final-sentiment-december-update-audit-report | Arbitrum | RiskEngine (oracle price path) | `0xc0ac97A0eA320Aa1E32e9DEd16fb580Ef3C078Da` | 1 | 0/1 | 0 | 1 |  |
| 1129 | 2023-01-drips | Ethereum | DripsHub.squeeze / removeDrip | `0x9819a3848c60999C37b20a0639bA11d87609564d` | 1 | 0/1 | 1 | 1 |  |
| 1130 | 2023-01-rabbithole | Optimism | Erc20Quest / QuestFactory | `0x52629961F71C1C2564C5aa22372CB1b9fa9EBA3E` | 1 | 0/1 | 0 | 1 |  |
| 1131 | 2023-02-15-landx-finance-land | Ethereum | LandX xToken (vested-token rewards) | `0x1B2B0FA9283595F5036C007dD99Ed0aA6de8362E` | 1 | 0/1 | 0 | 1 |  |
| 1132 | 2023-02-ethereum-evm-nestedfinance-smartcontracts- | Ethereum | NestedFactory | `0x606ACc984223094F0eE3c2bE64196B303763899F` | 1 | 0/1 | 0 | 1 |  |
| 1133 | 2023-03-16-nayms-nayms | Ethereum | TokenizedVaultFacet (payDividendFromEnti | `0x03f2a869915984b9BEd52C53eE492668a326BC18` | 1 | 0/1 | 0 | 1 |  |
| 1134 | 2023-03-21-final-union-finance-update-audit-report | Ethereum | UnionToken (UNION) | `0x5Dfe42eEA70a3e6f93EE54eD9C321aF07A85535C` | 1 | 0/1 | 0 | 1 |  |
| 1135 | 2023-03-24-final-gmx-audit-report | Arbitrum | Vault (cumulative borrowing factor) | `0x489ee077994B6658eAfA855C308275EAd8097C4A` | 1 | 0/1 | 0 | 1 |  |
| 1136 | 2023-03-24-final-gmx-audit-report | Arbitrum | Vault (withdrawFromVault) | `0x489ee077994B6658eAfA855C308275EAd8097C4A` | 1 | 0/1 | 0 | 1 |  |
| 1137 | 2023-03-27-final-y2k-audit-report | Arbitrum | Vault (rollover queue) | `0x984e0eb8fb687afa53fc8b33e12e04967560e092` | 1 | 0/1 | 1 | 1 |  |
| 1138 | 2023-03-ethereum-evm-atlendis-atlendissmartcontracts-securit | Polygon | BorrowerPools.withdrawRemainingEscrow /  | `0xbc13e1B5DA083b10622Ff5B52c9cFa1912F10B1F` | 1 | 0/1 | 1 | 1 |  |
| 1139 | 2023-03-neotokyo | Ethereum | NeoTokyoStaker | `0x67e1eCFA9232E27EAf3133B968A33A9a0dCa9e16` | 1 | 0/1 | 1 | 1 |  |
| 1140 | 2023-03-zksync | zkSync Era | MsgValueSimulator | `0x0000000000000000000000000000000000008009` | 1 | 0/1 | 0 | 1 |  |
| 1141 | 2023-03-zksync | zkSync Era | MsgValueSimulator (system contract) | `0x0000000000000000000000000000000000008009` | 1 | 0/1 | 0 | 1 |  |
| 1142 | 2023-04-22-final-teller-audit-report | Ethereum | CollateralManager.commitCollateral (acti | `0x2551A099129ad9b0b1FEc16f34D9CB73c237be8b` | 1 | 0/1 | 0 | 1 |  |
| 1143 | 2023-04-22-final-teller-audit-report | Ethereum | TellerV2.updateCommitment | `0x00182FdB0B880eE24D428e3Cc39383717677C37e` | 1 | 0/1 | 0 | 1 |  |
| 1144 | 2023-04-22-final-teller-audit-report | Ethereum | CollateralManager.commitCollateral | `0x2551A099129ad9b0b1FEc16f34D9CB73c237be8b` | 1 | 0/1 | 1 | 1 |  |
| 1145 | 2023-04-ethereum-evm-ajnalabs-securityreview | Ethereum | GrantFund | `0x74d5b005ca64a5C9EE3611Bdc6F6C02D93C84b2f` | 1 | 0/1 | 1 | 1 |  |
| 1146 | 2023-04-party | Ethereum | InitialETHCrowdfund.contribute | `0x49f3929D548B783752ab42Ce9527CBd3B4f51D92` | 1 | 0/1 | 0 | 1 |  |
| 1147 | 2023-05-05-final-footium-audit-report | Ethereum | FootballClub | `0x659cf1306eDBA213D1fb8F9352B4593A82B05d0c` | 1 | 0/1 | 0 | 1 |  |
| 1148 | 2023-05-10-final-jojo-exchange-audit-report | Base | JOJO Dealer | `0x2f7c3cf9d9280b165981311b822becc4e05fe635` | 1 | 0/1 | 1 | 1 |  |
| 1149 | 2023-05-15-final-notional-v3-audit-report | Ethereum | VaultAccountAction (Notional V3) | `0x6e7058c91F85E0F6db4fc9da2CA41241f5e4263f` | 1 | 0/1 | 0 | 1 |  |
| 1150 | 2023-05-22-threshold-usd | Ethereum | BorrowerOperations.adjustTrove | `0x874a8ee5b4Cc0B9973c7c002FA891fc28666cAA9` | 1 | 0/1 | 1 | 1 |  |
| 1151 | 2023-05-31-v2 | Ethereum | SablierV2ProxyTarget | `0x297b43aE44660cA7826ef92D8353324C018573Ef` | 1 | 0/1 | 0 | 1 |  |
| 1152 | 2023-05-31-v2 | Ethereum | SablierV2LockupLinear (deposit) | `0xB10daee1FCF62243aE27776D7a92D39dC8740f95` | 1 | 0/1 | 0 | 1 |  |
| 1153 | 2023-05-maia | Arbitrum | RootPort/BranchPort hToken decimal scali | `0x5399Eee5073bC1018233796a291Ffd6a78E26cbb` | 1 | 0/1 | 0 | 1 |  |
| 1154 | 2023-05-maia | Arbitrum | RootBridgeAgent.retrySettlement | `0x72bD06A2E28168Ef9deA33b1A0af05EC2D34Cb17` | 1 | 0/1 | 1 | 1 |  |
| 1155 | 2023-05-maia | Arbitrum | RootPort.fetchVirtualAccount | `0x5399Eee5073bC1018233796a291Ffd6a78E26cbb` | 1 | 0/1 | 0 | 1 |  |
| 1156 | 2023-06-04-final-gmx-update-audit-report | Arbitrum | MarketUtils (via ExchangeRouter/Reader) | `0x7dE39FF2e232A2203196788d37e234cF8F1b83f1` | 1 | 0/1 | 0 | 1 |  |
| 1157 | 2023-06-04-final-gmx-update-audit-report | Arbitrum | OrderHandler (via ExchangeRouter) | `0x7dE39FF2e232A2203196788d37e234cF8F1b83f1` | 1 | 0/1 | 0 | 1 |  |
| 1158 | 2023-06-lybra | Ethereum | LybraConfigurator | `0x35346Ff68D44a89dd62F02893D53159D252C33F6` | 1 | 0/1 | 1 | 1 |  |
| 1159 | 2023-06-lybra | Ethereum | PeUSDMainnet | `0xD585aaafA2B58b1CD75092B51ade9Fa4Ce52F247` | 1 | 0/1 | 0 | 1 |  |
| 1160 | 2023-07-01-final-dodo-v3-audit-report | Ethereum | D3Vault.withdrawReserves (DODO V3) | `0x49186E32fEd50fd6B5604A2618c7B0b03Cd41414` | 1 | 0/1 | 0 | 1 |  |
| 1161 | 2023-07-amphora | Ethereum | VaultController | `0xb688801cadb4ddb6980bb777d42972c24f920855` | 1 | 0/1 | 1 | 1 |  |
| 1162 | 2023-07-amphora | Ethereum | WUSDA | `0x43833f0C2025dFA80b5556574FAA11CBf7F3f4eB` | 1 | 0/1 | 0 | 1 |  |
| 1163 | 2023-07-tapioca | Arbitrum | YieldBox / (m)TapiocaOFT | `0xCFFd997DB053c0fC54010770b55A4E02B1D104a5` | 1 | 0/1 | 1 | 1 |  |
| 1164 | 2023-07-tapioca | Arbitrum | USDO | `0xEB99062643cA5Ab880c077288345E0B14B297432` | 1 | 0/1 | 1 | 1 |  |
| 1165 | 2023-08-02-ebtc | Ethereum | BorrowerOperations / CdpManager | `0xd366e016Ae0677CdCE93472e603b75051E022AD0` | 1 | 0/1 | 0 | 1 |  |
| 1166 | 2023-08-15-final-perennial-v2-audit-report | Arbitrum | PythOracle (per-market oracle) | `0x90A664846960AaFA2c164605Aebb8e9Ac338f9a0` | 1 | 0/1 | 0 | 1 |  |
| 1167 | 2023-08-29-final-tokemak-v2-audit-report | Ethereum | CurveV2CryptoEthOracle | `0x075c80cd9E8455F94b7Ea6EDB91485F2D974FB9B` | 1 | 0/1 | 1 | 1 |  |
| 1168 | 2023-08-29-final-tokemak-v2-audit-report | Ethereum | LMPVault rewards (staking) | `0x49012DfAAc52229B429530EF18e11761ecF6C5c6` | 1 | 0/1 | 1 | 1 |  |
| 1169 | 2023-08-29-final-tokemak-v2-audit-report | Ethereum | LMPVault.deposit/redeem | `0x49012DfAAc52229B429530EF18e11761ecF6C5c6` | 1 | 0/1 | 1 | 1 |  |
| 1170 | 2023-08-29-final-tokemak-v2-audit-report | Ethereum | LMPVault.updateDebtReporting | `0x49012DfAAc52229B429530EF18e11761ecF6C5c6` | 1 | 0/1 | 1 | 1 |  |
| 1171 | 2023-08-29-final-tokemak-v2-audit-report | Ethereum | SystemRegistry | `0x0406d2D96871f798fcf54d5969F69F55F803eEA4` | 1 | 0/1 | 0 | 1 |  |
| 1172 | 2023-08-29-final-tokemak-v2-audit-report | Ethereum | LMPVault | `0x49012DfAAc52229B429530EF18e11761ecF6C5c6` | 1 | 0/1 | 0 | 1 |  |
| 1173 | 2023-08-29-final-tokemak-v2-audit-report | Ethereum | LMPVaultRouter / PeripheryPayments | `0x109E5A790044D8762f44b34927AD363301FeeEa7` | 1 | 0/1 | 0 | 1 |  |
| 1174 | 2023-09-venus | BNB Chain | Venus reward distributor (updateAlpha /  | `0xfd36e2c2a6789db23113685031d7f16329158384` | 1 | 0/1 | 0 | 1 |  |
| 1175 | 2023-10-23-final-real-wagmi-2-audit-report | Metis | LiquidityBorrowingManager | `0x20fa274D00fF4917A13cD464FDbB200475B6EaBd` | 1 | 0/1 | 1 | 1 |  |
| 1176 | 2023-10-28-final-aloe-audit-report | Ethereum | VolatilityOracle (Oracle.sol) | `0x0000000030d51e39a2dDDb5Db50F9d74a289DFc3` | 1 | 0/1 | 0 | 1 |  |
| 1177 | 2023-11-10-gondi-43da11ee | Ethereum | Multi Source Loan V1 | `0xCa5a494Ca20483e21ec1E41FE1D9461Da77595Bd` | 1 | 0/1 | 0 | 1 |  |
| 1178 | 2023-11-10-gondi-43da11ee | Ethereum | User Vault V1 | `0x14a6Dcebb2Bb73aae1b199CCAadA75247b81976D` | 1 | 0/1 | 1 | 1 |  |
| 1179 | 2023-11-15-synfutures-v3-413eb61e | Base | SynFutures V3 gate | `0x208B443983D8BcC8578e9D86Db23FbA547071270` | 1 | 0/1 | 0 | 1 |  |
| 1180 | 2023-11-27-core-and-erc1155a | Ethereum | ERC1155A.safeBatchTransferFrom | `0xaD551890522E596CF1D3EbF5a97DceC4d12eB6De` | 1 | 0/1 | 0 | 1 |  |
| 1181 | 2023-11-27-core-and-erc1155a | Ethereum | SuperPositions.onlyMinter | `0xaD551890522E596CF1D3EbF5a97DceC4d12eB6De` | 1 | 0/1 | 0 | 1 |  |
| 1182 | 2023-11-27-core-and-erc1155a | Ethereum | Superpositions.onlyMinter | `0xaD551890522E596CF1D3EbF5a97DceC4d12eB6De` | 1 | 0/1 | 0 | 1 |  |
| 1183 | 2023-12-21-breederdao-99fb4c73 | Ethereum | Staked BreederDAO (V1 staking) | `0x90390B630afE8f86dcB9199bA847736ffD450eC1` | 1 | 0/1 | 0 | 1 |  |
| 1184 | 2023-12-26-final-olympus-rbs-2-0-audit-report | Ethereum | OlympusRange / Bunni price helper (getBu | `0x399cD3685912bb56aAeD0949119dB6cE5Df60FB5` | 1 | 0/1 | 0 | 1 |  |
| 1185 | 2023-12-ethereum-evm-acronym-foundation-securityreview | Ethereum | LetterOfCredit (partial redemption) | `0x14db9a91933aD9433E1A0dB04D08e5D9EF7c4808` | 1 | 0/1 | 1 | 1 |  |
| 1186 | 2023-12-ethereum-evm-acronym-foundation-securityreview | Ethereum | PythPriceOracle | `0xC6f3405c861Fa0dca04EC4BA59Bc189D1d56Ee05` | 1 | 0/1 | 0 | 1 |  |
| 1187 | 2023-12-initcapital | Mantle | LendingPool (wLp hook) | `0x423bB7577BCf594df986D9646B44D3144b3329FD` | 1 | 0/1 | 1 | 1 |  |
| 1188 | 2023-13-04-final-olympus-update-audit-report | Ethereum | Olympus Treasury | `0x9A315BdF513367C0377FB36545857d12e85813Ef` | 1 | 0/1 | 0 | 1 |  |
| 1189 | 2023-13-04-final-olympus-update-audit-report | Ethereum | Olympus Minter / Treasury | `0x9A315BdF513367C0377FB36545857d12e85813Ef` | 1 | 0/1 | 0 | 1 |  |
| 1190 | 2023-22-09-final-cooler-update-audit-report | Ethereum | Clearinghouse v1.0 (Cooler) | `0xd6a6e8d9e82534bd65821142fccd91ec9cf31880` | 1 | 0/1 | 1 | 1 |  |
| 1191 | 2024-01-10-the-standard | Arbitrum | SmartVaultManagerUSD | `0x496aB4A155C8fE359Cd28d43650fAFA0A35322Fb` | 1 | 0/1 | 1 | 1 |  |
| 1192 | 2024-01-12-stake-link | Ethereum | Staked LINK (stLINK) | `0xb8b295df2cd735b15BE5Eb419517Aa626fc43cD5` | 1 | 0/1 | 0 | 1 |  |
| 1193 | 2024-01-24-final-looksrare-yolo-audit-report | Blast | YOLO | `0xf77dd21c5ce38ac08786BE35Ef1d1DeC1a6a15F3` | 1 | 0/1 | 1 | 1 |  |
| 1194 | 2024-02-04-final-flat-money-audit-report | Arbitrum | FlatcoinVault / position transfer lock | `0x23c3300C47E1D30f0E2E407861161Ab2EE88Fc87` | 1 | 0/1 | 1 | 1 |  |
| 1195 | 2024-02-12-opal-contracts | Ethereum | Gem pool (wstETH, representative) | `0x86b130298719F753808E96cA6540b684a2d21466` | 1 | 0/1 | 1 | 1 |  |
| 1196 | 2024-03-07-final-rio-network-audit-report | Ethereum | RioLRTCoordinator | `0x65d895C82B967d58B4d4E50A6afb8001E30A63b7` | 1 | 0/1 | 0 | 1 |  |
| 1197 | 2024-03-13-enki-sca-enki-vesting-feb2024-sca-enki-vesting-fe | Metis | seMetis vault | `0x97a2de3A09F4A4229369ee82c7F76be1a5564661` | 1 | 0/1 | 0 | 1 |  |
| 1198 | 2024-03-30-final-axis-finance-audit-report | Ethereum | Axis USD (USDX) | `0xa1fA7777974312f7d801A8880714a218F76233f8` | 1 | 0/1 | 1 | 1 |  |
| 1199 | 2024-03-abracadabra-money | Blast | MagicLP | `0xeDa89B8b19eBEf5FC0D5e21ebAd174366C230D35` | 1 | 0/1 | 0 | 1 |  |
| 1200 | 2024-03-abracadabra-money | Blast | MagicLP TWAP | `0xeDa89B8b19eBEf5FC0D5e21ebAd174366C230D35` | 1 | 0/1 | 0 | 1 |  |
| 1201 | 2024-03-ethereum-evm-aladdinfxprotocol-securityreview | Ethereum | PoolManager (deposit/mint rounding) | `0x250893CA4Ba5d05626C785e8da758026928FCD24` | 1 | 0/1 | 0 | 1 |  |
| 1202 | 2024-04-06-final-perennial-v2-update-2-audit-report | Arbitrum | KeeperOracle.at | `0x81e521E3FBb970255BBFD312d95Fa942dB39a1c7` | 1 | 0/1 | 0 | 1 |  |
| 1203 | 2024-04-12-common-wealth-sca-common-wealth-vesting-mar2024-s | Base | Common Wealth token | `0x99b2B1A2aDB02B38222ADcD057783D7e5D1FCC7D` | 1 | 0/1 | 0 | 1 |  |
| 1204 | 2024-04-26-final-titles-publishing-protocol-audit-report | Ethereum | TitlesEditionV1 | `0x7EA666C245E973De5Cd126Ba82C4858b793717d7` | 1 | 0/1 | 0 | 1 |  |
| 1205 | 2024-04-29-sigmaprime-angle-review | Ethereum | SanToken (_updateSanRate) | `0x6cd24ac05103C2C911347a6D3628d64a9F07eAf5` | 1 | 0/1 | 0 | 1 |  |
| 1206 | 2024-04-29-sigmaprime-chainlink-chainlink-1-review | Ethereum | Operator Factory | `0x3E64Cd889482443324F91bFA9c84fE72A511f48A` | 1 | 0/1 | 0 | 1 |  |
| 1207 | 2024-04-29-sigmaprime-sushi-auction-maker-furo-review | Ethereum | Furo base (_depositToken) | `0x4ab2FC6e258a0cA7175D05fF10C5cF798A672cAE` | 1 | 0/1 | 0 | 1 |  |
| 1208 | 2024-04-gondi | Ethereum | MultiSourceLoan (V1) | `0xCa5a494Ca20483e21ec1E41FE1D9461Da77595Bd` | 1 | 0/1 | 0 | 1 |  |
| 1209 | 2024-04-gondi | Ethereum | MultiSourceLoan (V1) / withdrawal queue | `0xCa5a494Ca20483e21ec1E41FE1D9461Da77595Bd` | 1 | 0/1 | 0 | 1 |  |
| 1210 | 2024-05-03-nayms-2024-retainer-04e1c37c | Ethereum | Nayms staking (diamond) | `0x03f2a869915984b9BEd52C53eE492668a326BC18` | 1 | 0/1 | 0 | 1 |  |
| 1211 | 2024-05-04-final-exactly-protocol-audit-report | Optimism | Market (Exactly) | `0xa430A427bd00210506589906a71B54d6C256CEdb` | 1 | 0/1 | 1 | 1 |  |
| 1212 | 2024-05-20-euler-vault-kit-evk-audit | Ethereum | EVK / EVC (borrow LTV vs liquidation thr | `0x0C9a3dd6b8F28529d72d7f9cE918D493519EE383` | 1 | 0/1 | 0 | 1 |  |
| 1213 | 2024-05-31-final-midas-audit-report | Ethereum | MidasAccessControl (BLACKLISTED_ROLE) | `0x9b94Aac01EcBB8fb31E52cE21D1f57849A843Feb` | 1 | 0/1 | 0 | 1 |  |
| 1214 | 2024-05-loop | Ethereum | LoopVault | `0x01D840d0eC69B12D462eB626355ac915011BCf6b` | 1 | 0/1 | 1 | 1 |  |
| 1215 | 2024-06-24-panoptic-audit | Ethereum | PanopticPool.mintOptions / collateral ch | `0x0000000000035D9945Bf4d24393828e920376bAe` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/panoptic-audit |
| 1216 | 2024-07-03-final-notional-leveraged-vaults-pendle- | Ethereum | LeveragedVault | `0x9E1CD0E11009E684Cd7c76Be51A3d01e486032fA` | 1 | 0/1 | 0 | 1 |  |
| 1217 | 2024-07-03-final-notional-leveraged-vaults-pendle-pt-and-vau | Ethereum | Leveraged vault (_redeemPT) | `0x6e7058c91F85E0F6db4fc9da2CA41241f5e4263f` | 1 | 0/1 | 0 | 1 |  |
| 1218 | 2024-07-13-final-union-finance-update-2-audit-report | Optimism | Comptroller (_accrueRewards) | `0x06a31efa04453C5F9C0A711Cdb96075308C9d6E3` | 1 | 0/1 | 0 | 1 |  |
| 1219 | 2024-07-dittoeth | Ethereum | yDUSD | `0xD1770005ec30B67A7637229f96CDe73f132A285E` | 1 | 0/1 | 0 | 1 |  |
| 1220 | 2024-07-dittoeth | Ethereum | DittoETH Diamond (PrimaryLiquidationFace | `0xd177000be70ea4efc23987acd1a79eaba8b758f1` | 1 | 0/1 | 0 | 1 |  |
| 1221 | 2024-07-dittoeth | Ethereum | DittoETH Diamond | `0xd177000be70ea4efc23987acd1a79eaba8b758f1` | 1 | 0/1 | 0 | 1 |  |
| 1222 | 2024-07-loopfi | Ethereum | PoolV3 | `0xa684eaf215ad323452e2b2bf6f817d4aa5c116ab` | 1 | 0/1 | 0 | 1 |  |
| 1223 | 2024-08-24-final-sentiment-v2-audit-report | Arbitrum | RiskEngine | `0x488D275dA177795e4ce5eB93D4c37474412249bF` | 1 | 0/1 | 0 | 1 |  |
| 1224 | 2024-08-28-royco-monorepo | Ethereum | VaultOrderbook.allocateOrder() | `0x63da1229be88fb4d20210147954a1a3e05f2581b` | 1 | 0/1 | 0 | 1 |  |
| 1225 | 2024-09-09-level-money-contracts | Ethereum | LevelMinting.mintlvlUSD | `0x8E7046e27D14d09bdacDE9260ff7c8c2be68a41f` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_level_money_october_2024.pdf |
| 1226 | 2024-09-10-final-zerolend-one-audit-report | zkSync Era | Pool (_repayDebtTokens) | `0x4d9429246EA989C9CeE203B43F6d1C7D83e3B8F8` | 1 | 0/1 | 0 | 1 |  |
| 1227 | 2024-09-10-final-zerolend-one-audit-report | zkSync Era | Pool (LiquidationLogic._burnCollateralTo | `0x4d9429246EA989C9CeE203B43F6d1C7D83e3B8F8` | 1 | 0/1 | 0 | 1 |  |
| 1228 | 2024-09-10-final-zerolend-one-audit-report | zkSync Era | IncentivesProxy (rewards accrual) | `0x54AB34aB3C723bD2674c7082aA6fFcdfd3A5BEdc` | 1 | 0/1 | 0 | 1 |  |
| 1229 | 2024-09-10-final-zerolend-one-audit-report | zkSync Era | Pool (withdraw / liquidityIndex) | `0x4d9429246EA989C9CeE203B43F6d1C7D83e3B8F8` | 1 | 0/1 | 0 | 1 |  |
| 1230 | 2024-09-15-final-flayer-audit-report | Ethereum | Locker | `0xb4C5b5235b98114E9DC227b54e088C11680b2385` | 1 | 0/1 | 1 | 1 |  |
| 1231 | 2024-09-15-final-flayer-audit-report | Base | NFTXV4Hook (UniswapImplementation) | `0xaa49ADaDD33c5E953b645567AFb10CBbba63afC4` | 1 | 0/1 | 0 | 1 |  |
| 1232 | 2024-09-15-final-flayer-audit-report | Base | Locker | `0xb4C5b5235b98114E9DC227b54e088C11680b2385` | 1 | 0/1 | 0 | 1 |  |
| 1233 | 2024-09-15-final-flayer-audit-report | Base | CollectionShutdown | `0x28bA2f2A1E38B4547b39675D8E1d96A016e626fF` | 1 | 0/1 | 1 | 1 |  |
| 1234 | 2024-10-27-final-orderly-solana-vault-contract-audit-report | Solana | Orderly Solana Vault (deposit) | `ErBmAD61mGFKvrFNaTJuxoPwqrS8GgtwtqJTJVjFWx9Q` | 1 | 0/1 | 1 | 1 |  |
| 1235 | 2024-11-01-final-avantis-v1-5-cross-asset-leverage-audit-rep | Base | Trading | `0x5FF292d70bA9cD9e7CCb313782811b3D7120535f` | 1 | 0/1 | 0 | 1 |  |
| 1236 | 2024-12-17-final-tally-collaborative-audit-report | zkSync Era | Staker (Tally Staker / Depositor earning | `0x24B5292aDC6CF2373Ddbc09c8699B4F88C6b2CDB` | 1 | 0/1 | 1 | 1 |  |
| 1237 | 2024-12-17-final-tally-collaborative-audit-report | zkSync Era | Staker.bumpEarningPower | `0x24B5292aDC6CF2373Ddbc09c8699B4F88C6b2CDB` | 1 | 0/1 | 0 | 1 |  |
| 1238 | 2024-12-bakerfi-invitational | Base | Vault/Strategy (BakerFiProxy) | `0x37327c99bBc522e677a97d01021dB20227faF60A` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-05-bakerfi-findings/blob/30e7003f6fc084da282f |
| 1239 | 2025-01-ethereum-evm-bacon-labs-bunniv2-securityre | Ethereum | BunniZone / FloodPlain hook | `0x000000dceb71f3107909b1b748424349bfde5493` | 1 | 0/1 | 1 | 1 |  |
| 1240 | 2025-02-04-neemo-finance-sca-neemo-neemo-staked-astar-dec202 | Soneium | nsASTR (Neemo Staked Astar) | `0xc67476893C166c537afd9bc6bc87b3f228b44337` | 1 | 0/1 | 1 | 1 |  |
| 1241 | 2025-02-06-termmax-web3-security-audit | Ethereum | TermMaxRouter | `0xC47591F5c023e44931c78D5A993834875b79FB11` | 1 | 0/1 | 0 | 1 |  |
| 1242 | 2025-02-12-mystic-finance-sca-mystic-finance-mystic-finance- | Plume | Pool Address Provider | `0xeD7F9Af764Cb9949b095A05f7ED78aE3A71d0697` | 1 | 0/1 | 1 | 1 |  |
| 1243 | 2025-02-thorwallet | Base | TITN token / THORWallet bridge path | `0xe62bfbe57763ec24c0f130426f34dbce11fc5b06` | 1 | 0/1 | 0 | 1 |  |
| 1244 | 2025-03-07-eigenlayer-contracts | Ethereum | DelegationManager | `0x39053D51B77DC0d36036Fc1fCc8Cb819df8Ef37A` | 1 | 0/1 | 0 | 1 |  |
| 1245 | 2025-05-01-alchemix-v3 | Ethereum | Transmuter.redeem (_redemptionWeight) | `0x073598132f37756a7E665FB52f1757463120bd3C` | 1 | 0/1 | 0 | 1 |  |
| 1246 | 2025-05-01-alchemix-v3 | Ethereum | Alchemist._liquidate (adjustedDebtToBurn | `0xfa995B6ABc387376C3e7De5f6d394Ab5B6beE26B` | 1 | 0/1 | 0 | 1 |  |
| 1247 | 2025-05-21-jigsaw-contracts | Ethereum | Manager | `0x0000000E44A948Ab0c83F2C65D3a2C4A06B05228` | 1 | 0/1 | 0 | 1 |  |
| 1248 | 2025-05-28-primev-validator-registry | Ethereum | VanillaRegistry (proxy) | `0x47afdcB2B089C16CEe354811EA1Bbe0DB7c335E9` | 1 | 0/1 | 0 | 1 |  |
| 1249 | 2025-05-28-primev-validator-registry | Ethereum | ValidatorOptInRouter (proxy) | `0x821798d7b9d57dF7Ed7616ef9111A616aB19ed64` | 1 | 0/1 | 1 | 1 |  |
| 1250 | 2025-07-02-sapien-2-9f938662 | Base | SapienVault | `0x60Bf63729f688287a450299962b36Cef0aFfaa42` | 1 | 0/1 | 0 | 1 |  |
| 1251 | 2025-07-10-sigmaprime-recall-sigma-prime-recall-staking-secu | Base | Recall Staking | `0x37Ee1FE41231b631d62658372b457235b9b884e0` | 1 | 0/1 | 0 | 0 |  |
| 1252 | 2025-10-linea-burn-mechanism | Ethereum | LineaRollup | `0xd19d4B5d358258f05D7B411E21A1460D11B0876F` | 1 | 0/1 | 0 | 1 |  |
| 1253 | 2025-12-03-startale-stablecoin-vaults-402c94ac | Soneium | RewardRedistributor.distribute() | `0xda798684ffd5eb509c2ab7b8352ec55b31f18201` | 1 | 0/1 | 1 | 1 |  |
| 1254 | 24 Wardens contributed reports to the Wildcat Protocol | Ethereum | WildcatArchController | `0xfEB516d9D946dD487A9346F6fee11f40C6945eE4` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-08-wildcat-findings/blob/dc0352696795b2cb37e1 |
| 1255 | 31Third (31third d11ac960) | Ethereum | BatchTrade | `0xD20c024560ccA40288C05BAB650ac087ae9b0f6e` | 1 | 0/1 | 1 | 1 |  |
| 1256 | 3DNS Inc | Optimism | ThreeDNSRegControl.makeCommitmentV2 | `0xBB7B805B257d7C76CA9435B3ffe780355E4C4B17` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_3dns_mar2024.pdf |
| 1257 | 3DNS Inc | Optimism | 3DNS Multicall.functionDelegateCall / Th | `0xBB7B805B257d7C76CA9435B3ffe780355E4C4B17` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_3dns_mar2024.pdf |
| 1258 | 3DNS Inc | Optimism | PaymentProcessor._handlePayment / ThreeD | `0xBB7B805B257d7C76CA9435B3ffe780355E4C4B17` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_3dns_mar2024.pdf |
| 1259 | 3JaneMoney MarketContracts USD3/sUSD3Update | Ethereum | USD3 | `0x056B269Eb1f75477a8666ae8C7fE01b64dD55eCc` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1260 | 3JanePYTLocker SecurityReview | Ethereum | USD3 senior tranche | `0x056B269Eb1f75477a8666ae8C7fE01b64dD55eCc` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1261 | 88mph 88 | Ethereum | DInterest | `0xc791184dc537FFEa0Bbb106179aD45d08D5ACEE2` | 1 | 0/1 | 0 | 1 |  |
| 1262 | 88mph v3 | Ethereum | 88mph DPOOL (representative) | `0x19e10132841616ce4790920d5f94b8571f9b9341` | 1 | 0/1 | 0 | 1 |  |
| 1263 | 88mph v3 | Ethereum | DPOOL (initializer) | `0x19e10132841616ce4790920d5f94b8571f9b9341` | 1 | 0/1 | 1 | 1 |  |
| 1264 | 9Lives CPMM | Arbitrum | Trading AMM mint/burn (Factory proxy) | `0x90234c942f335df8c055b9c1a2e0babf060a31ad` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/9lives-cpmm-audit |
| 1265 | 9lives cpmm audit | Arbitrum | Trading AMM mint/burn (behind Factory pr | `0x90234c942f335df8c055b9c1a2e0babf060a31ad` | 1 | 0/1 | 0 | 1 |  |
| 1266 | ALGM Staking | Astar | LiquidStakingMain (behind Liquid Staking | `0x70d264472327B67898c919809A9dc4759B6c0f27` | 1 | 0/1 | 0 | 1 |  |
| 1267 | APY.Finance | Ethereum | APYVault oracle adapter | `0x75CE0E501e2E6776FcAAa514f394a88a772A8970` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1268 | Aave Protocol (SigmaPrime 2024-04-29 review) | Ethereum | Pool.validateBorrow | `0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2` | 1 | 0/1 | 0 | 1 |  |
| 1269 | Aave Protocol (v1) | Ethereum | LendingPoolCore | `0x3dfd23a6c5e8bbcfc9581d2e864a68feb6a076d3` | 1 | 0/1 | 1 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1270 | Aave Protocol (v1) | Ethereum | FeeProvider | `0x2dc9969a32e2171557b7c24a632483d03955440d` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1271 | Abracadabra Mimswap | Ethereum | MagicLP invariant | `0x6C843D25A2b0eE3E8844492e891dc7257645023A` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-03-abracadabra-money-findings/blob/061ab30b50 |
| 1272 | Abracadabra Mimswap | Ethereum | MagicLP TWAP | `0x6C843D25A2b0eE3E8844492e891dc7257645023A` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-03-abracadabra-money-findings/blob/061ab30b50 |
| 1273 | Abracadabra Mimswap | Ethereum | MagicLP pool | `0x6C843D25A2b0eE3E8844492e891dc7257645023A` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-03-abracadabra-money-findings/blob/061ab30b50 |
| 1274 | AbracadabraMoney OFT | Ethereum | Abracadabra OFT (LzProxyOFTV2) | `0x439a5f0f5E8d149DDA9a0Ca367D4a8e4D6f83C10` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1275 | Adapters Possum Labs | Arbitrum | Possum Portals (core) | `0x24b7d3034C711497c81ed5f70BEE2280907Ea1Fa` | 1 | 0/1 | 0 | 1 | https://github.com/shieldify-security/audits-portfolio-md/blob/f2c051af4ffb67e11 |
| 1276 | Aftermath Finance Perpetuals | Sui | pyth-lazer-integration | `0xa5428da682b4fad53e40f73dc07b547e33be078ec1c5d4a4378d6a316f0d9104` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/5d5026fffcc3be6ce5f4a7b38b9a83af |
| 1277 | Ajna Core | Ethereum | Ajna pool (kick/settle) | `0xe6f4d9711121e5304b30ac2aae57e3b085ad3c4d` | 1 | 0/1 | 1 | 1 |  |
| 1278 | Ajna Protocol | Ethereum | GrantFund (isEpochClaimed) | `0x74d5b005ca64a5C9EE3611Bdc6F6C02D93C84b2f` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-05-ajna-findings/blob/2ec232eee8d5782ac1c6275 |
| 1279 | Ajna Protocol | Ethereum | PositionManager.memorializePositions | `0x87B0F458d8F1ACD28A83A748bFFbE24bD6B701B1` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-05-ajna-findings/blob/2ec232eee8d5782ac1c6275 |
| 1280 | Ajna Protocol | Ethereum | PositionManager | `0x87B0F458d8F1ACD28A83A748bFFbE24bD6B701B1` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-05-ajna-findings/blob/2ec232eee8d5782ac1c6275 |
| 1281 | Ajna Protocol | Ethereum | PositionManager.moveLiquidity | `0x87B0F458d8F1ACD28A83A748bFFbE24bD6B701B1` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-05-ajna-findings/blob/2ec232eee8d5782ac1c6275 |
| 1282 | Alchemix (Optimism) | Optimism | AlchemistV3 / Router (Optimism bridging  | `0xDeD3A04612FF12b57317abE38e68026Fc9D28114` | 1 | 0/1 | 0 | 1 |  |
| 1283 | Alchemix - Optimism Bridging and Reward Routing | Optimism | RewardRouter / OptimismRewardCollector | `0xCB8FA9a76b8e203D8C3797bF438d8FB81Ea3326A` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/273 |
| 1284 | Alchemix V3 POC | Ethereum | ALCH token | `0xdBdb4d16EdA451D0503b854CF79D55697F90c8DF` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_alchemix_march2025.pdf |
| 1285 | Alchemix v3 | Ethereum | AlchemistV3 | `0xfa995B6ABc387376C3e7De5f6d394Ab5B6beE26B` | 1 | 0/1 | 0 | 1 |  |
| 1286 | Alchemy Modular Account v2 | Ethereum | ModularAccountBase (deferred actions) /  | `0x00000000000002377B26b1EdA7b0BC371C60DD4f` | 1 | 0/1 | 0 | 1 |  |
| 1287 | Alchemy Modular Account v2 | Ethereum | NativeTokenLimitModule | `0x00000000000001e541f0D090868FBe24b59Fbe06` | 1 | 0/1 | 0 | 1 |  |
| 1288 | Algebra Farmings | Ethereum | AlgebraEternalFarming / NonFungiblePosit | `0xfb035a157EB35Eb503e6fbE89222B13e108F5647` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1289 | Algem | Astar | Algem Liquid Staking (Astar) | `0x70d264472327B67898c919809A9dc4759B6c0f27` | 1 | 0/1 | 1 | 1 |  |
| 1290 | Algem (LiquidCrowdloan) | Astar | Liquid Staking (proxy) | `0x70d264472327B67898c919809A9dc4759B6c0f27` | 1 | 0/1 | 0 | 1 |  |
| 1291 | Algem (Sio2 / liquid staking) | Astar | Sio2Adapter | `0x7dE84319633850Bdabc557A1C61DA9E926cB4fF0` | 1 | 0/1 | 0 | 1 |  |
| 1292 | Aloe | Ethereum | BorrowerNFT (self-liquidation / warn) | `0x00000000000078b629B7C06f5339060648468AA6` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1293 | Aloe | Ethereum | BorrowerNFT (modify / liquidate / warn) | `0x00000000000078b629B7C06f5339060648468AA6` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1294 | Aloe | Ethereum | VolatilityOracle (IV) | `0x0000000030d51e39a2dDDb5Db50F9d74a289DFc3` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1295 | Aloe | Ethereum | VolatilityOracle (Oracle.sol) | `0x0000000030d51e39a2dDDb5Db50F9d74a289DFc3` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1296 | Altitude | Ethereum | Vault Core cbBTC-USDC v2 | `0x550F8a1FFC921b9179267F9e7909FC68CE496A6b` | 1 | 0/1 | 0 | 0 | https://github.com/OmegaAudits/audits/blob/a9891e4b8b01650638370d401bc36f81695a3 |
| 1297 | Altitude | Ethereum | ALTI token | `0x8929e9DbD2785e3BA16175E596CDD61520feE0D1` | 1 | 0/1 | 1 | 1 | https://github.com/OmegaAudits/audits/blob/a9891e4b8b01650638370d401bc36f81695a3 |
| 1298 | Altitude | Ethereum | GroomableManager | `0x1f7d589e90e4E4FC1B15B3143a5c60F743C759b9` | 1 | 0/1 | 0 | 1 | https://github.com/oxor-io/public_audits/blob/06624b6efe70d98702baccef5208ec57db |
| 1299 | Altitude | Ethereum | Vault Core | `0x550F8a1FFC921b9179267F9e7909FC68CE496A6b` | 1 | 0/1 | 0 | 1 | https://github.com/OmegaAudits/audits/blob/a9891e4b8b01650638370d401bc36f81695a3 |
| 1300 | Altitude | Ethereum | FarmBufferDispatcher / Dispatcher | `0x45F08c3Bf6Ca6f84875225dBe0e6F4b6f6578932` | 1 | 0/1 | 1 | 1 | https://github.com/oxor-io/public_audits/blob/06624b6efe70d98702baccef5208ec57db |
| 1301 | Altitude | Ethereum | Vault Core | `0x1f7d589e90e4E4FC1B15B3143a5c60F743C759b9` | 1 | 0/1 | 1 | 1 | https://github.com/OmegaAudits/audits/blob/a9891e4b8b01650638370d401bc36f81695a3 |
| 1302 | Ambire Wallet | Ethereum | Ambire Wallet (WALLET) token | `0x88800092fF476844f74dC2FC427974BBee2794Ae` | 1 | 0/1 | 0 | 1 |  |
| 1303 | Amphor | Ethereum | claimVested / claimUnstakeAmount | `0x3b022EdECD65b63288704a6fa33A8B9185b5096b` | 1 | 0/1 | 1 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1304 | Amphor | Ethereum | Ankr reward accounting | `0x3b022EdECD65b63288704a6fa33A8B9185b5096b` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1305 | Amphor | Ethereum | reward logic | `0x3b022EdECD65b63288704a6fa33A8B9185b5096b` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1306 | Amphor | Ethereum | withdraw -> _payRefs | `0x3b022EdECD65b63288704a6fa33A8B9185b5096b` | 1 | 0/1 | 1 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1307 | Amphor | Ethereum | claimVested | `0x3b022EdECD65b63288704a6fa33A8B9185b5096b` | 1 | 0/1 | 1 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1308 | Amphora Protocol | Ethereum | VaultController | `0xb688801cadb4ddb6980bb777d42972c24f920855` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-07-amphora-findings/blob/fe47bdf8f431d82f3a58 |
| 1309 | Amphora Protocol | Ethereum | WUSDA | `0x43833f0C2025dFA80b5556574FAA11CBf7F3f4eB` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-07-amphora-findings/blob/fe47bdf8f431d82f3a58 |
| 1310 | Amphora Protocol | Ethereum | VaultController.withdraw (USDC) | `0xb688801cadb4ddb6980bb777d42972c24f920855` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-07-amphora-findings/blob/fe47bdf8f431d82f3a58 |
| 1311 | Angle Labs Angle Protocol | Ethereum | SanToken (sanRate / _updateSanRate) | `0x6cd24ac05103C2C911347a6D3628d64a9F07eAf5` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1312 | Angle Protocol - Invitational | Ethereum | AngleDistributor | `0xD9f22abbe5Bf9c46413af053e34dBE987Ff8418d` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-06-angle-findings/blob/ecb393d7187f0412875527 |
| 1313 | AngryToken | Ethereum | AngryToken | `0x2c9acEb63181cd08a093d052ec041e191f229692` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1314 | AnySwap CrossChain-Bridge | Ethereum | MultichainRouter | `0xD1310EeDaE36929603191d44155dF9252554F2F4` | 1 | 0/1 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 1315 | ApeRocket Finance | BNB Chain | ApeRocket Vault (V2, _transferUserInfo) | `0xa13eF34F11cD905A1aACe891e3Fd1b355D770e7F` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1316 | AragonBlack Fundraising | Ethereum | BatchedBancorMarketMaker | `0x8c19cF0135852BA688643F57d56Be72bB898c411` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2019/11/aragonblack-fundraising/ |
| 1317 | Arbitrum BoLD | Ethereum | RollupUserLogic (behind RollupProxy) | `0x5eF0D09d1E6204141B4d37530808eD19f60FBa35` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-05-arbitrum-foundation-findings/blob/2a853fab |
| 1318 | Arbitrum Foundation (BoLD dispute protocol) | Ethereum | RollupProxy (BoLD EdgeChallengeManager) | `0x5eF0D09d1E6204141B4d37530808eD19f60FBa35` | 1 | 0/1 | 0 | 1 |  |
| 1319 | Arbitrum Security Council Election System | Arbitrum | SecurityCouncilNomineeElectionGovernor / | `0x8a1cDA8dee421cD06023470608605934c16A05a0` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-08-arbitrum-findings/blob/1242399740566462afc |
| 1320 | Arcadia | Base | AccountV1 | `0xbea2B6d45ACaF62385877D835970a0788719cAe1` | 1 | 0/1 | 0 | 1 |  |
| 1321 | Arcadia | Base | LendingPool | `0x3ec4a293Fb906DD2Cd440c20dECB250DeF141dF1` | 1 | 0/1 | 0 | 1 |  |
| 1322 | Arcadia | Base | UniswapV3AM / AccountV1 | `0xbea2B6d45ACaF62385877D835970a0788719cAe1` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1323 | Archi Finance | Arbitrum | VaultInfo / reward distributor | `0x73956FF7375476EBFD5e82d80Ea9065a5bCc3d2b` | 1 | 0/1 | 0 | 1 |  |
| 1324 | Archi Finance | Arbitrum | VaultInfo / ArchiVault | `0x73956FF7375476EBFD5e82d80Ea9065a5bCc3d2b` | 1 | 0/1 | 0 | 1 |  |
| 1325 | Archi Finance | Arbitrum | VaultInfo (vault registry) | `0x73956FF7375476EBFD5e82d80Ea9065a5bCc3d2b` | 1 | 0/1 | 0 | 1 |  |
| 1326 | Arkis DeFi Prime Brokerage Protocol | Ethereum | Arkis MarginAccount / swap execution | `0xbbC9c04348E093473C5b176Cb4b103fF706528bf` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1327 | ArtGobblers | Ethereum | ArtGobblers | `0x60bb1e2AA1c9ACAfB4d34F71585D7e959f387769` | 1 | 0/1 | 0 | 1 |  |
| 1328 | Aspida Network Contracts | Ethereum | RewardOracle | `0xD3aFE58031998EAf2b0cCeE76dBd8ca50B19DCCa` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1329 | Astake Protocol | Astar | WstASTR token | `0x45cCC0DEA1470F1b4213Ab60fd2eBB2a063f1c24` | 1 | 0/1 | 1 | 1 | https://2158577729-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 1330 | Astroport vxASTRO Updates | Neutron | vxASTRO voting escrow / emissions whitel | `neutron17tr94hgtjrd0ehexc7lau9e0vk9y5v6a4qs0q4lu6yy2zyshymtqtrfxt8` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 1331 | Astroport.fi AMM Protocol CosmWasm Smart Contract | Terra | Maker | `terra1ygcvxp9s054q8u2q4hvl52ke393zvgj0sllahlycm4mj8dm96zjsa45rzk` | 1 | 0/1 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1332 | Asymmetry Finance afETH Invitational | Ethereum | VotiumStrategy (swap/withdraw) | `0x12fC2BF0Edea2437CD4FE17EC2B65dC45eb92aAd` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-09-asymmetry-findings/blob/9ecac9cca9082f3245 |
| 1333 | Asymmetry Finance afETH Invitational | Ethereum | AfEth.price | `0x8896EF81b2D1C92E8540D543816A5260B991A61c` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-09-asymmetry-findings/blob/9ecac9cca9082f3245 |
| 1334 | Asymmetry Finance afETH Invitational | Ethereum | VotiumStrategyCore.ethPerCvx | `0x12fC2BF0Edea2437CD4FE17EC2B65dC45eb92aAd` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-09-asymmetry-findings/blob/9ecac9cca9082f3245 |
| 1335 | Asymmetry Finance afETH Invitational | Ethereum | AfEth (mint/redeem pricing) | `0x8896EF81b2D1C92E8540D543816A5260B991A61c` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-09-asymmetry-findings/blob/9ecac9cca9082f3245 |
| 1336 | Audit - Stryke / MarginZero - CLAMM Options | Arbitrum | DopexV2OptionMarket (OptionMarketOTMFE) | `0x77b6f45a3Dcf0493f1B9Ac9874e5982AB526AA9e` | 1 | 0/1 | 1 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1337 | Audit Gamma V4 | Ethereum | GAMMA token | `0x6bea7cfef803d1e3d5f7c0103f7ded065644e197` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1338 | Augmented Finance | Ethereum | Augmented Finance core proxy | `0xb3ed706b564bba9cab64042f4e1b391be7bebce5` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1339 | Augur Core v2 | Ethereum | Universe / ReputationToken migration | `0x49244BD018Ca9fd1f06ecC07B9E9De773246e5AA` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/augur-core-v2-audit |
| 1340 | Augur Core v2 | Ethereum | AffiliateValidator | `0x2A256518DDdCe6E2e95B56a95991d4FA990Be659` | 1 | 0/1 | 0 | 0 | https://www.openzeppelin.com/news/augur-core-v2-audit-components |
| 1341 | Aurora Labs Staking |  | Aurora staking stream (stake/unstake) | `Aurora` | 1 | 0/1 | 1 | 1 |  |
| 1342 | Auxo Governance | Ethereum | AuxoGovernor | `0xB320Fc09B272D1658E99488ADc614E4645B1d83c` | 1 | 0/1 | 1 | 1 |  |
| 1343 | Avalanche Interchain Token Transfer (Teleporter / ICTT) | Avalanche C-Chain | TeleporterMessenger / ICTT TokenRemote f | `0x253b2784c75e510dD0fF1da844684a1aC0aa5fcf` | 1 | 0/1 | 1 | 1 |  |
| 1344 | Avantis v1.5: Cross-Asset Leverage | Base | Avantis trading contract (setTraderRefer | `0x5FF292d70bA9cD9e7CCb313782811b3D7120535f` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1345 | Aventus Protocol. May 11, 2018. | Ethereum | AVT (Aventus token) | `0x0d88eD6E74bbFD96B831231638b66C05571e824F` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1346 | Axelar | Ethereum | Axelar Gateway (TokenManager lock/unlock | `0x4F4495243837681061C4743b74B3eEdf548D56A5` | 1 | 0/1 | 0 | 1 |  |
| 1347 | Aztec -April 10, 2022 | Ethereum | RollupProcessor (depositERC20) | `0x37696CE9343A0C27ac0A37DEA5e881D87A76c47c` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1348 | BSD Money | Stacks | registry-v1-0 (update-redemptions) | `SPYY08XK8YG4W9B1WSYBM8HD0WBQ1E1WRXEGSENS.registry-v1-0` | 1 | 0/1 | 0 | 0 | https://osec.io/reports/2a484d4e-4146-800f-ae4e-fa009e5b85cd |
| 1349 | BabySwap | BNB Chain | BABY token (delegation / getPriorVotes) | `0x53e562b9b7e5e94b81f10e96ee70ad06df3d2657` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1350 | Backd contest | Ethereum | StakerVault.transfer | `0x14A4AEFF0FfC9378aE8157f170d141C3582e61Fc` | 1 | 0/1 | 1 | 1 |  |
| 1351 | Backd contest | Ethereum | TopUpActionLibrary.lockFunds | `0x2CA2d717E1B3587b0Af7ef8B7aCC77540Cf4C572` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-04-backd-findings/blob/17a142117a1803e90a5fa9 |
| 1352 | Backd contest | Ethereum | StakerVault (checkpoint after transfer) | `0x14A4AEFF0FfC9378aE8157f170d141C3582e61Fc` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-04-backd-findings/blob/17a142117a1803e90a5fa9 |
| 1353 | Backd contest | Ethereum | TopUpAction | `0xF2281cA8693B1d35D7a73700909ec8535A57156D` | 1 | 0/1 | 0 | 1 |  |
| 1354 | BaconCoin | Ethereum | BACON token | `0xa54d2EBfD977ad836203c85F18db2F0a0cF88854` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 1355 | BadgerDAO | Ethereum | eBTC token (EBTCToken) | `0x661c70333AA1850CcDBAe82776Bb436A0fCfeEfB` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_badger_august2023.pdf |
| 1356 | BadgerDAO ibBTC Wrapper contest | Ethereum | WrappedIbbtcEth | `0x240b150f87445c63467408a8d53947b566a0d1aD` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-10-badgerdao-findings/blob/559b9944574bf1026f |
| 1357 | BakerFi | Base | BakerFi vault (BakerFiProxy) | `0x37327c99bBc522e677a97d01021dB20227faF60A` | 1 | 0/1 | 0 | 1 |  |
| 1358 | Balancer v3 | Ethereum | Balancer V2 Vault | `0xBA12222222228d8Ba445958a75a0704d566BF2C8` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1359 | Bancor V2 AMM | Ethereum | BancorConverterRegistry | `0xf6E2D7F616B67E46D708e4410746E9AAb3a4C518` | 1 | 0/1 | 0 | 1 |  |
| 1360 | Bankex Token Contract | Ethereum | BKX token (BANKEX utility token) | `0x45245bc59219eeaAF6cD3f382e078A461FF9De7B` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1361 | Baseline AMM | Ethereum | Relay | `0xc81fd894c0ace037d133af4886550ac8133568e8` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1362 | BaselineV2.1 | Ethereum | BPOOL / bAsset short pricing | `0xc81fd894c0ace037d133af4886550ac8133568e8` | 1 | 0/1 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1363 | BaselineV2.1 | Ethereum | Short open/close anchor pricing | `0xc81fd894c0ace037d133af4886550ac8133568e8` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1364 | BaselineV2.1 | Ethereum | TimeslotLib interest accrual | `0xc81fd894c0ace037d133af4886550ac8133568e8` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1365 | BaselineV2.1 | Ethereum | Baseline relay | `0xc81fd894c0ace037d133af4886550ac8133568e8` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1366 | Basin | Ethereum | Well (shift/sync) | `0xBA51AAAA95aeEFc1292515b36D86C51dC7877773` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-07-basin-findings/blob/55abdd66057ecb372b7efb |
| 1367 | Basin | Base | BASIN token | `0x4788de271F50EA6f5D5D2a5072B8D3C61d650326` | 1 | 0/1 | 0 | 1 |  |
| 1368 | BendDAO | Ethereum | LendPool / IsolateLogic.executeIsolateLi | `0x70b97A0da65C15dfb0FFA02aEE6FA36e507C2762` | 1 | 0/1 | 1 | 1 |  |
| 1369 | Berachain | Berachain | BeaconDeposit (deposit contract) | `0x4242424242424242424242424242424242424242` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_berachain_january2025.pdf |
| 1370 | Berachain Pol | Berachain | Distributor | `0xD2f19a79b026Fb636A7c300bF5947df113940761` | 1 | 0/1 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1371 | Berachain Pol | Berachain | RewardVaultFactory | `0x94Ad6Ac84f6C6FbA8b8CCbD71d9f4f101def52a8` | 1 | 0/1 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1372 | Berachain Pol | Berachain | FeeCollector | `0x7Bb8DdaC7FbE3FFC0f4B3c73C4F158B06CF82650` | 1 | 0/1 | 0 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1373 | Biconomy - Cross Chain Messaging Protocol | Ethereum | BiconomyForwarder (meta-transaction veri | `0x84a0856b038eaAd1cC7E297cF34A7e72685A8693` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1374 | Biconomy Nexus | Ethereum | Nexus account fallback | `0x000000004F43C49e93C970E84001853a70923B03` | 1 | 0/1 | 0 | 0 | https://cdn.cantina.xyz/reports/Biconomy-Spearbit-Security-Review-October-2024.p |
| 1375 | Biconomy Nexus | Ethereum | K1Validator | `0x00000000d12897DDAdC2044614A9677B191A2d95` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1376 | BiohackerDAO | Ethereum | DataLiquidityPoolImplementation (request | `0x78046053E5B02Ca2056D7007cf55747244223E5B` | 1 | 0/1 | 0 | 1 |  |
| 1377 | Bitlayer-system-contracts | Bitlayer | Staking | `0x000000000000000000000000000000000000f000` | 1 | 0/1 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 1378 | Blackhole (blackhole) | Avalanche | GaugeFactoryCL | `0x6B6a3D5A1c536aCE1D761685aF241b2cb7a6eA5E` | 1 | 0/1 | 1 | 1 |  |
| 1379 | BlackholeDEX (Algebra Pools) | Avalanche | Blackhole CLMM core | `0xcd94a87696fac69edae3a70fe5725307ae1c43f6` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1380 | Blast | Blast | Blast (_sharePrice) | `0x4300000000000000000000000000000000000002` | 1 | 0/1 | 0 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1381 | Blast | Blast | Blast.configure (via L2CrossDomainMessen | `0x4300000000000000000000000000000000000002` | 1 | 0/1 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1382 | Blend | Stellar | Pool.execute_claim (emissions) | `CDSYOAVXFY7SM5S64IZPPPYB4GVGGLMQVFREPSQQEZVIWXX5R23G4QSU` | 1 | 0/1 | 1 | 1 |  |
| 1383 | Blend Capital | Stellar | Backstop | `CDVQVKOY2YSXS2IC7KN6MNASSHPAO7UN2UR2ON4OI2SKMFJNVAMDX6DP` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/67a31c2a-91c0-48c9-bc38-22c2b5ff105d |
| 1384 | Blend Capital | Stellar | Blend pool reserve (b_token) | `CDVQVKOY2YSXS2IC7KN6MNASSHPAO7UN2UR2ON4OI2SKMFJNVAMDX6DP` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/67a31c2a-91c0-48c9-bc38-22c2b5ff105d |
| 1385 | BlinDEX | RSK | BlinDEX BDStable redemption (pool behind | `0x6542a10E68cEAc1Fa0641ec0D799a7492795AAC1` | 1 | 0/1 | 0 | 1 | https://github.com/OmegaAudits/audits/blob/a9891e4b8b01650638370d401bc36f81695a3 |
| 1386 | Bloom (Blueberry) | Ethereum | BloomPool | `0x47fD7bB0579537585f6533d23f85c8aa457F5162` | 1 | 0/1 | 0 | 1 |  |
| 1387 | Blueberry | Ethereum | Stable BPT Oracle | `0xA05FE2e46b386398f5a252Aa91e4C4bba73ECb33` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/104 |
| 1388 | Blueberry | Ethereum | Curve Stable Oracle | `0x58660E94E910DB4215B57823Be7F32A11Ac69532` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/69 |
| 1389 | Blueberry | Ethereum | BlueberryBank | `0x9b06eA9Fbc912845DF1302FE1641BEF9639009F7` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/41 |
| 1390 | Bolide | BNB Chain | Bolide MasterChef (farming rewards) | `0x3782C47E62b13d579fe748946AEf7142B45B2cf7` | 1 | 0/1 | 0 | 1 | https://github.com/choco-cupcake/AuditSearcher/blob/bc907c9a314e7b63aaaec698d264 |
| 1391 | Bond Options (Bond Protocol) | Arbitrum | FixedStrikeOptionTeller | `0xF507733f260a42bb2c8108de87b7b0ce5826a9cd` | 1 | 0/1 | 1 | 1 |  |
| 1392 | BondAppetit | Ethereum | BondAppetit Governance (BAG) | `0x28A06c02287e657ec3F8e151A13C36A1D43814b0` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1393 | Botanix | Botanix | Minting contract (BTC bridge) | `0x0Ea320990B44236A0cEd0ecC0Fd2b2df33071e78` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1394 | Brokkr | Avalanche | BroToken (BRO) | `0x65031e28Cb0E8CC21Ae411f9dD22c9b1bd260Ce4` | 1 | 0/1 | 0 | 1 |  |
| 1395 | Buck Labs | Ethereum | BuckV2 (BUCK proxy) | `0xdb13997f4D83EF343845d0bAEb27d1173dF8c224` | 1 | 0/1 | 0 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1396 | Bueno.art-2 | Ethereum | BuenoFactory | `0x19478179Ef8Bb7c4792a4041903080e097D137dD` | 1 | 0/1 | 0 | 1 | https://0xmacro.com/library/audits/bueno-art-2 |
| 1397 | Buffer Finance | Arbitrum | Buffer Finance (DefiLlama-listed address | `0x1A5B0aaF478bf1FDA7b934c76E7692D722982a6D` | 1 | 0/1 | 0 | 1 |  |
| 1398 | Buffer Finance | Arbitrum | BufferBinaryPool | `0x6Ec7B10bF7331794adAaf235cb47a2A292cD9c7e` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1399 | BuniCorn | BNB Chain | BuniCornRouter02.removeLiquidityBNBSuppo | `0x689E37aFb4236A5cF808cA05a8D1c564200fA0E4` | 1 | 0/1 | 1 | 1 |  |
| 1400 | Bunni | Ethereum | BunniHub (v2) vault | `0x000000000049C7bcBCa294E63567b4D21EB765f1` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1401 | Bunni | Ethereum | BunniHub (v2) / Permit2 | `0x000000000049C7bcBCa294E63567b4D21EB765f1` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1402 | Bunni (Bunni v2, Pashov Aug-2024 review) | Ethereum | BunniHub (v2 vault) | `0x000000000049C7bcBCa294E63567b4D21EB765f1` | 1 | 0/1 | 0 | 1 |  |
| 1403 | Burve | Berachain | SimplexDiamond / ERC4626 vertex | `0xa1beD164c12CD9479A1049f97BDe5b3D6EC21089` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/858 |
| 1404 | CA GUARDIAN Baseline Markets YesArena & Afterburner | Blast | YesArena | `0x1C002B0A15e949Ce8F2b9f2FABbba37FE3BdA856` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1405 | CAP Labs Covered Agent Protocol | Ethereum | FeeAuction | `0xbD12E50Bfaa25735D074DBfDCF73208b9ccD2e43` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1406 | CLOBER | Arbitrum | OrderNFT.transferFrom | `0x58ed1f4913e652baF17C154551bd8E9dbc73fC56` | 1 | 0/1 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1407 | CLOBER | Arbitrum | CloberMarket.collectFees | `0xbB40AC34aE9BcBC30a035Eb12b998f1f52F966c0` | 1 | 0/1 | 0 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1408 | Cadabra | BNB Chain | VelodromPoolAdapter_qStablePair | `0xcA1c644704feBf4ab81f85daca488d1623C28e63` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1409 | CakePie | BNB Chain | MasterCakepie (mCake reward claim) | `0x74165b89fd8E9b91A109a4e71662f27EeBA61E98` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 1410 | Camp Network (camp ae830654) | Camp Network | CampTimelockEscrowNativeOFT#bridgeOut | `0x2494D3a68a6c1d03c18aa483EBB871Ff73Ada7f9` | 1 | 0/1 | 0 | 1 |  |
| 1411 | Canto contest | Canto | Unitroller / InterestRateModel | `0x5E23dC409Fc2F832f83CEc191E245A191a4bCc5C` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-06-canto-findings/blob/a96eaec661f2201f741fe9 |
| 1412 | Canto contest | Canto | Unitroller / Comptroller | `0x5E23dC409Fc2F832f83CEc191E245A191a4bCc5C` | 1 | 0/1 | 0 | 1 |  |
| 1413 | Canto contest | Canto | Unitroller / NoteInterest | `0x5E23dC409Fc2F832f83CEc191E245A191a4bCc5C` | 1 | 0/1 | 0 | 1 |  |
| 1414 | Canto v2 (Canto Lending Market + BaseV1, Code4rena 2022-06) | Canto | BaseV1-core pair (periodSize) | `0xE387067f12561e579C5f7d4294f51867E0c1cFba` | 1 | 0/1 | 0 | 1 |  |
| 1415 | Canto v2 (Canto Lending Market + BaseV1, Code4rena 2022-06) | Canto | BaseV1-periphery (getUnderlyingPrice for | `0xa252eEE9BDe830Ca4793F054B506587027825a8e` | 1 | 0/1 | 0 | 1 |  |
| 1416 | Canto v2 (Canto Lending Market + BaseV1, Code4rena 2022-06) | Canto | BaseV1-periphery (getUnderlyingPrice(CTo | `0xa252eEE9BDe830Ca4793F054B506587027825a8e` | 1 | 0/1 | 1 | 1 |  |
| 1417 | Canto v2 contest | Canto | BaseV1Router01 | `0xa252eEE9BDe830Ca4793F054B506587027825a8e` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-06-canto-v2-findings/blob/66b006114725b7ed47b |
| 1418 | Canto v2 contest | Canto | BaseV1Router01 / BaseV1-periphery | `0xa252eEE9BDe830Ca4793F054B506587027825a8e` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-06-canto-v2-findings/blob/66b006114725b7ed47b |
| 1419 | Canto v2 contest | Canto | BaseV1Factory (pairs) | `0xE387067f12561e579C5f7d4294f51867E0c1cFba` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-06-canto-v2-findings/blob/66b006114725b7ed47b |
| 1420 | Cap Labs (Covered Agent Protocol) | Ethereum | VaultAdapter (oracle rate library) | `0xcD7f45566bc0E7303fB92A93969BB4D3f6e662bb` | 1 | 0/1 | 0 | 1 |  |
| 1421 | Cap Labs (Covered Agent Protocol) | Ethereum | FeeAuction._transferOutAssets | `0xa1a20aBdc873CF291c22Ce3C8968EC06277324D0` | 1 | 0/1 | 0 | 0 |  |
| 1422 | CapyFi | Ethereum | caUXD / CapyFi vault | `0x98Ac8AC56d833bD69d34F909Ac15226772FAc9aa` | 1 | 0/1 | 1 | 1 | https://github.com/coinspect/publications/blob/01b04f1f4a2e2c4d7e228b967fedb8991 |
| 1423 | Caviar Private Pools | Ethereum | PrivatePool (minimal proxy created by Fa | `0xA16bE8d32934a9AaB272102AC4BB890481F4074E` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-04-caviar-findings/blob/d22bd0a22308bee92374f |
| 1424 | Cetus Concentrated Liquidity Protocol Aptos | Aptos | pool module (Cetus CLMM) | `0xa7f01413d33ba919441888637ca1607ca0ddcbfa3c0a9ddea64743aaa560e498` | 1 | 0/1 | 0 | 1 | https://github.com/movebit/Sampled-Audit-Reports/blob/9f2027ef1500342dec1f1385db |
| 1425 | Chainflip Protocol | Ethereum | Deposit witnessing / Vault | `0xf5e10380213880111522dd0efd3dbb45b9f62bcc` | 1 | 0/1 | 0 | 1 | https://github.com/chainflip-io/chainflip-backend/blob/47ccef6d8b9b736da24a1f1e3 |
| 1426 | Cinch Protocol | Ethereum | RevenueShareVault | `0x42EA533F8e2E980993860c8296Ad91bf8C8AB719` | 1 | 0/1 | 0 | 1 |  |
| 1427 | Clanker Protocol | Base | Clanker factory fee recipient | `0x2A787b2362021cC3eEa3C24C4748a6cD5B687382` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1428 | ClipFinanceCore | Ethereum | ClipFinance | `0x42A23bc31B56bDA373de56d2632B2F2d33b397d8` | 1 | 0/1 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 1429 | Code4rena - Namespace | Ethereum | RegistryMinter | `0x335b2259a060ce822e4bb8D73Ded366b9aD1CF94` | 1 | 0/1 | 1 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1430 | Coinbase Session Keys | Base | CoinbaseSmartWallet (Permissions), walle | `0xBA5ED110eFDBa3D005bfC882d75358ACBbB85842` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/Coinbase-Session-Keys-Spearbit-Security-Review-S |
| 1431 | Collectif Finance | Filecoin | Collectif Staked FIL | `0xd0437765D1Dc0e2fA14E97d290F135eFdf1a8a9A` | 1 | 0/1 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 1432 | CollectionSwap Vault v 1 0 | Ethereum | CollectionSwap Vault (reward program reg | `0x03b51826a4868780DB375eE27E5b0AdaaC5274EE` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1433 | Conic Finance | Ethereum | CNCLockerV2 | `0x5F2e1Ac047E6A8526f8640a7Ed8AB53a0b3f4acF` | 1 | 0/1 | 0 | 1 | https://conic.finance/media/PeckShield-Audit-Report-ConicFinance.pdf |
| 1434 | Connext | Ethereum | ConnextDiamond swap/liquidity path | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 0/1 | 0 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1435 | Connext | Ethereum | BridgeFacet (ConnextDiamond) | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2021-07-connext-findings/blob/b487b684290e8adc9479 |
| 1436 | Connext | Ethereum | ConnextDiamond / LibAsset | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-07-connext-findings/blob/b487b684290e8adc9479 |
| 1437 | Connext | Ethereum | SpokeConnector | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 0/1 | 1 | 1 | https://0xmacro.com/library/audits/connext-1 |
| 1438 | Connext | Ethereum | PortalFacet (ConnextDiamond facet) | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 0/1 | 0 | 1 |  |
| 1439 | Connext Amarok contest | Ethereum | Connext Diamond - PortalFacet | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-06-connext-findings/blob/f085ac7592f9514a4577 |
| 1440 | Connext Amarok contest | Ethereum | Connext Diamond - execute/_reconcile | `0x8898B472C54c31894e3B9bb83cEA802a5d0e63C6` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-06-connext-findings/blob/f085ac7592f9514a4577 |
| 1441 | Contango Core v 1 0 | Ethereum | Ladle | `0x30E7348163016B3b6E1621A3Cb40e8CF33CE97db` | 1 | 0/1 | 1 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1442 | Contango CoreV2 v 2 0 | Ethereum | Contango (flash-loan callback) | `0x6Cae28b3D09D8f8Fc74ccD496AC986FC84C0C24E` | 1 | 0/1 | 1 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1443 | Copra | Arbitrum | Copra V1 vault (Gamma integration) | `0xbC89bAc7b3697120019D30154102403e846c665b` | 1 | 0/1 | 0 | 1 | https://docs.fuzz.land/Copra-Audit-Report-103112096c218034879ff6e24a06b105 |
| 1444 | Copra | Arbitrum | Copra V1 vault (Steadefi integration) | `0xbC89bAc7b3697120019D30154102403e846c665b` | 1 | 0/1 | 1 | 1 | https://docs.fuzz.land/Copra-Audit-Report-103112096c218034879ff6e24a06b105 |
| 1445 | Copra Finance | Arbitrum | Vault (Teahouse USDC) | `0xbC89bAc7b3697120019D30154102403e846c665b` | 1 | 0/1 | 1 | 1 |  |
| 1446 | Copra Finance | Arbitrum | TeahouseLiquidityWarehouse._withdrawFrom | `0xbC89bAc7b3697120019D30154102403e846c665b` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1447 | Cork | Ethereum | CorkPoolManager (fee accounting for LV h | `0x1cCccCccCcCf9A60Fe57cd7CEf504d1DaaA78244` | 1 | 0/1 | 0 | 1 |  |
| 1448 | Cork Protocol (Best Efforts contest, v1) | Ethereum | ModuleCore / Cork PoolManager (ERC1967Pr | `0xCCd90F6435dd78C4ECCED1FA4db0D7242548a2a9` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1449 | Cork Protocol (FlashSwapRouter) | Ethereum | FlashSwapRouter | `0xb41B904f58BA83824e1B95B9bAB1Ab2e93654d47` | 1 | 0/1 | 1 | 1 |  |
| 1450 | CosmWasm Smart Contract | Terra | ASTRO token (Terra) | `terra1nsuqsk6kh58ulczatwev87ttq2z6r3pusulg9r24mfj2fvtzd4uq3exn26` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1451 | Cover Protocol v2 | Ethereum | CoverRouter (best-effort) | `0xE303f7081be3530f66dE12cDBE2a2e98C0939125` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1452 | Cowri Labs Shell Protocol v2 | Arbitrum | Ocean | `0x96B4f4E401cCD70Ec850C1CF8b405Ad58FD5fB7a` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1453 | Cozy Finance | Optimism | Protection market / PToken share math | `0xbfc907920a9D9E11A356727F43b6c56ae2774add` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_cozy_apr2023.pdf |
| 1454 | Cozy Finance | Optimism | ProtectionSeller.sell / cost model | `0xbfc907920a9D9E11A356727F43b6c56ae2774add` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_cozy_apr2023.pdf |
| 1455 | Current Finance | Sui | Current MainMarket | `0x41f3d76aee8b20e53f7d0d395fdc09e241e683c7bc5d0f69674b545ee42549df` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/1256 |
| 1456 | Curve | Ethereum | ControllerFactory (crvUSD markets) | `0xC9332fdCB1C491Dcc683bAe86Fe3cb70360738BC` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1457 | Curve | Ethereum | Controller.create_loan_extended | `0xC9332fdCB1C491Dcc683bAe86Fe3cb70360738BC` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1458 | DEDAUB.COM Aori | Ethereum | AoriSeats.separateSeats | `0x0198Ce118C7d8d9FC29Cc13864E7403359375DCC` | 1 | 0/1 | 0 | 1 | https://github.com/Dedaub/audits/blob/431ec937802fd7118f9c6d533a530aaaf33a2c3a/A |
| 1459 | DEDAUB.COM LUSD Chicken Bonds | Ethereum | ChickenBondManager | `0x57619FE9C539f890b19c61812226F9703ce37137` | 1 | 0/1 | 1 | 1 | https://github.com/Dedaub/audits/blob/431ec937802fd7118f9c6d533a530aaaf33a2c3a/L |
| 1460 | DEDAUB.COM LUSD Chicken Bonds | Ethereum | Liquity StabilityPool | `0x66017D22b0f8556afDd19FC67041899Eb65a21bb` | 1 | 0/1 | 0 | 1 | https://github.com/Dedaub/audits/blob/431ec937802fd7118f9c6d533a530aaaf33a2c3a/L |
| 1461 | DEFI YIELD PROTOCOL | Ethereum | DeFiYieldProtocol (DYP) token | `0x961c8c0b1aad0c0b10a51fef6a867e3091bcef17` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1462 | DELIGHT LABS - Terraswap | Terra | Terraswap Pair (per-pool) | `terra1466nf3zuxpya8q9emxukd7vftaf6h4psr0a07srl5zw74zh84yjqxl5qul` | 1 | 0/1 | 0 | 1 | https://terraswap.io/wp-content/uploads/2023/07/terraswap-audit-report.pdf |
| 1463 | DELIGHT LABS - Terraswap-classic | Terra | terraswap_pair (via factory) | `terra1466nf3zuxpya8q9emxukd7vftaf6h4psr0a07srl5zw74zh84yjqxl5qul` | 1 | 0/1 | 1 | 1 | https://terraswap.io/wp-content/uploads/2023/06/terraswap-classic-20230620.pdf |
| 1464 | DODO (DODO V3 / D3) | Ethereum | D3Proxy | `0x411ec324598EF53b1E8663e335e9094464523e6B` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1465 | DODO GSP | Ethereum | DODO GSP pool (via GSPFactory) | `0x710409D2121B7C8EA4aCAdd6803FDE2D85DF6473` | 1 | 0/1 | 1 | 1 |  |
| 1466 | DODO Margin Trading | Ethereum | MarginTrading.sol | `0x0d71A079dF6a88e393C0F8d4fFf5Ce902a21A787` | 1 | 0/1 | 1 | 1 |  |
| 1467 | DOP (Data Ownership Protocol) | Ethereum | DOP token | `0xa37DB5456b5938Aa50B33575Ae2eB8048CA5959b` | 1 | 0/1 | 0 | 1 |  |
| 1468 | DTX Protocol | Taiko | DTX Taiko liquidity vault | `0xdA6a745740Bbdbe5F588b79FEe57f2e10ad4Da11` | 1 | 0/1 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 1469 | DYAD | Ethereum | KerosineManager | `0xFCCF9d9466ED79AFeD2ABc46350bFb78f7B47b90` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-04-dyad-findings/blob/8769dbdd7b34d16fd726272 |
| 1470 | DackieSwap | Base | DackieSwap V3 core | `0x73326b4d0225c429bed050c11c4422d91470aaf4` | 1 | 0/1 | 1 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1471 | DeFi Eggs | Sonic | EGGS token | `0xf26Ff70573ddc8a90Bd7865AF8d7d70B8Ff019bC` | 1 | 0/1 | 0 | 1 |  |
| 1472 | Debita Finance V3 | Base | DebitaV3Aggregator / DebitaV3Loan | `0x512EF0b254FF8eA8EDE5ed8c8718281D86BfeCD1` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1473 | Debt DAO - P2P Loan | Ethereum | SecuredLine / Spigot (per-line, created  | `0xc9ef6509a09b92043cedce689dfaa760048abd7f` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1474 | Decent | Ethereum | DcntEth.setRouter | `0xe2510aa4b019af3eb835d3ac9c800382109a4631` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2024-01-decent-findings/blob/0b40bd3192eaec4a2ea8d |
| 1475 | Deepr Finance | IOTA EVM | DEEPR token (IOTA EVM) | `0x4Eb8E03461360C2AcBb4B5963a18b8f9faEE8221` | 1 | 0/1 | 1 | 1 |  |
| 1476 | Defi.Money - BoostedStaker | Optimism | BoostedStaker | `0x73AF3a9974a09A0a046F26c529f7ec20c591Da20` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1477 | Defi.Money - BoostedStaker | Optimism | BoostedStaker.checkpointAccountWithLimit | `0x73AF3a9974a09A0a046F26c529f7ec20c591Da20` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1478 | DefiApp | Base | HOME staking contract (Base) | `0xC9714F8f036087d801f38C4105194e150d3a1864` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_defi_app_february2025.pdf |
| 1479 | Definer | Ethereum | Accounts / Bank | `0xad4649a917a0e928d00c3028db63acb07960d25b` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2021/02/definer/ |
| 1480 | Definer | Ethereum | Interest rate model / price oracle | `0xad4649a917a0e928d00c3028db63acb07960d25b` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2021/02/definer/ |
| 1481 | Degis SCProtection | Avalanche | IncidentReport | `0xcc274166c825bFFeC29FC3E6A56aAa95707c2f3d` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1482 | Derivio | zkSync Era | DERİVİO token | `0x29aDEC7Fe90E7217c10B7AD17f2A6Cd642f383D2` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/d79fc7ed-5c2e-448d-beaf-6f37ffb1a53a |
| 1483 | Dexter | Tezos | TokenToXtz.tokenToXtz | `KT1DrJV8vhkdLEj76h1H9Q4irZDqAkMPo1Qf` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1484 | Dexter | Tezos | Dexter.updateTokenPool | `KT1DrJV8vhkdLEj76h1H9Q4irZDqAkMPo1Qf` | 1 | 0/1 | 1 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1485 | Dexter | Tezos | Dexter.RemoveLiquidity | `KT1DrJV8vhkdLEj76h1H9Q4irZDqAkMPo1Qf` | 1 | 0/1 | 1 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1486 | Dexter | Tezos | Dexter call-injection entry point | `KT1DrJV8vhkdLEj76h1H9Q4irZDqAkMPo1Qf` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1487 | Diffuse Prime | Ethereum | Viewer (helper contract) | `0x2B29dEa1231AA37929d11Aa176D6643181482B22` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1488 | Dimo Network smart contracts (Token, Vesting, Identity) | Ethereum | Dimo (ERC-1967 proxy, ERC20Votes token) | `0x5fab9761d60419C9eeEbe3915A8FA1ed7e8d2E1B` | 1 | 0/1 | 0 | 1 |  |
| 1489 | DittoETH (TAPP) | Ethereum | PrimaryLiquidationFacet.liquidate() | `0x401b6122a05B85f449E632f757Ae622BcB197932` | 1 | 0/1 | 0 | 1 |  |
| 1490 | Doomsday Settlers | Ethereum | Settlement NFT / game | `0xB4CbA31bDAf6FF6e34eFC0CFC4906Bd29b0146E9` | 1 | 0/1 | 0 | 1 |  |
| 1491 | Drift Protocol | Solana | Drift v2 program (perpetuals / trigger o | `dRiftyHA39MWEi3m9aunc5MzRF1JYuBsbn6VPcn33UH` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1492 | Drips Protocol contest | Ethereum | DripsHub (squeeze) | `0x9819a3848c60999C37b20a0639bA11d87609564d` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-01-drips-findings/blob/9f23763ddfd3c00689b6f4 |
| 1493 | Drop Contracts | Neutron | Drop puppeteer (pump) | `neutron17jsl4t4hhaw37tnhenskrfntm7mv44wzjr3f990hx4p9r5m0gzdqquhtd3` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 1494 | Drop Contracts | Neutron | Drop core (exchange handler) | `neutron1lsxvdyvmexak084wdty2yvsq5gj3wt7wm4jaw34yseat7r4qjffqlxlcua` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 1495 | Drop Contracts | Neutron | Drop core | `neutron1lsxvdyvmexak084wdty2yvsq5gj3wt7wm4jaw34yseat7r4qjffqlxlcua` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 1496 | Dyson Finance | Polygon zkEVM | DYSN-USDC Pair | `0xC9001AFF3701e19C29E996D48e474Baf4C5eD006` | 1 | 0/1 | 1 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 1497 | EIP-4337 – Ethereum Account Abstraction | Ethereum | EntryPoint (token transfer path) | `0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/eth-foundation-account-abstraction-audit |
| 1498 | EarningFarm v3 Iterative | Ethereum | EFVault | `0xaafBBEaF2F7846bB247304E58DB8D4E25BF5A849` | 1 | 0/1 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 1499 | Eco Permit3 (PR 28 / PR 37) | Ethereum | Permit3 | `0xEc00030C0000245E27d1521Cc2EE88F071c2Ae34` | 1 | 0/1 | 0 | 1 |  |
| 1500 | Eco Permit3 PR 28 & 37 | Ethereum | Permit3 | `0xEc00030C0000245E27d1521Cc2EE88F071c2Ae34` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_eco_pr28_pr38_aug2025.pdf |
| 1501 | Eco Protocol | Ethereum | L1ECOBridge | `0x2Ca00788Ea444e09A7c2a94B2655F1956B62D52f` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1502 | Eigen Labs EigenLayer - EIGEN Rewards | Ethereum | DelegationManager (proxy) | `0x39053D51B77DC0d36036Fc1fCc8Cb819df8Ef37A` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1503 | Ellipsis Labs | Solana | Phoenix SDK / program | `PhoeNiXZ8ByJGLkxNfZRnkUfjvmuYqLR89jjFHGqdXY` | 1 | 0/1 | 0 | 0 | https://osec.io/reports/9888c291-939f-4def-bbb3-77a165bd9230 |
| 1504 | Emblem Vault | Ethereum | EmblemVault (mintWithSerial) | `0x82c7a8f707110f5fbb16184a5933e9f78a34c6ab` | 1 | 0/1 | 0 | 1 | https://github.com/chainlight-io/publications/blob/ec332bf4d0cde16e3db4f380b5a4d |
| 1505 | Embr Finance | Avalanche | Embr Vault (Balancer V2 fork) | `0xad68ea482860cd7077a5D0684313dD3a9BC70fbB` | 1 | 0/1 | 0 | 1 |  |
| 1506 | Emojicoin | Aptos | Emojicoin matched-funds allocation | `0xbabe32dbe1cb44c30363894da9f49957d6e2b94a06f2fc5c20a9d1b9e54cface` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/1ad84d4e-4146-8010-8755-cb3cd61e3eb7 |
| 1507 | Ethereal OrderbookDex | Ethereal | Ethereal orderbook/exchange | `0xB3cDC82035C495c484C9fF11eD5f3Ff6d342e3cc` | 1 | 0/1 | 1 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1508 | Ethereal Round 2 | Ethereal | Ethereal exchange core (close-only guard | `0xB3cDC82035C495c484C9fF11eD5f3Ff6d342e3cc` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1509 | Etherspot Gas Tank Paymaster Module | Ethereum | GasTankPaymaster | `0x5bB1125f293DE98927Aef30a6C8726B98C07Cbdd` | 1 | 0/1 | 0 | 1 | https://github.com/shieldify-security/audits-portfolio/blob/a1e130f5a286cbc3ede4 |
| 1510 | Euler Labs - EVK | Ethereum | Ethereum Vault Connector (EVC) / EVault | `0x0C9a3dd6b8F28529d72d7f9cE918D493519EE383` | 1 | 0/1 | 0 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1511 | Euler Swap | Ethereum | EulerSwapRegistry | `0x5FcCB84363F020c0cADE052C9c654aABF932814A` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_euler_swap_sep2025.pdf |
| 1512 | Exactly ExactlyProtocol v 1 0 | Optimism | Auditor proxy (OP Mainnet) | `0xaEb62e6F27BC103702E7BC879AE98bceA56f027E` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1513 | Exactly Protocol | Optimism | Exactly Market (Optimism) | `0x1e925de1c68ef83bd98ee3e130ef14a50309c01b` | 1 | 0/1 | 1 | 1 |  |
| 1514 | Exactly Protocol 1st V220126 | Optimism | Auditor (Comptroller) | `0xaEb62e6F27BC103702E7BC879AE98bceA56f027E` | 1 | 0/1 | 0 | 1 | https://github.com/coinspect/publications/blob/01b04f1f4a2e2c4d7e228b967fedb8991 |
| 1515 | Exactly Protocol 2nd V220822 | Optimism | FixedLender (MarketUSDC) | `0x81C9A7B55A4df39A9B7B5F781ec0e53539694873` | 1 | 0/1 | 1 | 1 | https://github.com/coinspect/publications/blob/01b04f1f4a2e2c4d7e228b967fedb8991 |
| 1516 | Exchange | Ethereum | Exchange (fillOrder) | `0xDef1C0ded9bec7F1a1670819833240f027b25EfF` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2019/09/0x-v3-exchange/ |
| 1517 | FOR 1INCH | Ethereum | 1INCH token (ERC20Pods) | `0x111111111117dC0aa78b770fA6A738034120C302` | 1 | 0/1 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1518 | FOR LIDO V2 | Ethereum | stETH share rate / burn limit | `0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1519 | Farm Hero | BNB Chain | MasterChef (emergencyWithdrawNFT share a | `0xDAD01f1d99191a2eCb78FA9a007604cEB8993B2D` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1520 | Fastlane Atlas | Polygon | Atlas | `0xB363f4D32DdB0b43622eA07Ae9145726941272B4` | 1 | 0/1 | 0 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1521 | Fastlane Atlas | Polygon | Atlas DAppControl | `0xB363f4D32DdB0b43622eA07Ae9145726941272B4` | 1 | 0/1 | 0 | 0 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1522 | Fastlane Atlas | Polygon | Atlas V2DAppControl | `0xB363f4D32DdB0b43622eA07Ae9145726941272B4` | 1 | 0/1 | 0 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1523 | Fei Protocol | Ethereum | EthBondingCurve | `0xB783c0E21763bEf9F2d04E6499abFbe23AdB7e1F` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/fei-audit-2 |
| 1524 | Fei Protocol v2 Phase 1 | Ethereum | CollateralizationOracle | `0xFF6f59333cfD8f4Ebc14aD0a0E181a83e655d257` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2021/09/fei-protocol-v2-phase-1/ |
| 1525 | Fenix | Blast | Fenix | `0x52f847356b38720b55ee18cb3e094ca11c85a192` | 1 | 0/1 | 0 | 1 | https://github.com/hats-finance/Fenix--0x9d7765a7ebd5b6322a30797a44a5428531970d3 |
| 1526 | Flex | Ethereum | Flex registry | `0x9117440a7d03238905d1c8908157bd7a547c77c8` | 1 | 0/1 | 1 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1527 | Flexa | Ethereum | FlexaCollateralManager | `0x706D7F8B3445D8Dfc790C524E3990ef014e7C578` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1528 | Fluid DEX | Ethereum | Fluid Liquidity (DEX) | `0x52Aa899454998Be5b000Ad077a46Bbe360F4e497` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1529 | Fluid DEX | Ethereum | Fluid Liquidity (DEX swap_out) | `0x52Aa899454998Be5b000Ad077a46Bbe360F4e497` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1530 | Fluid DEX | Ethereum | Fluid Liquidity | `0x52Aa899454998Be5b000Ad077a46Bbe360F4e497` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/1225 |
| 1531 | Fogo Sessions | Fogo | session_manager / SPL token SetAuthority | `SesswvJ7puvAgpyqp7N8HnjNnvpnS8447tKNF3sPgbC` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/2a284d4e-4146-8074-b8e3-c307353fd3f4 |
| 1532 | Footium | Ethereum | FootiumClub | `0x659cf1306eDBA213D1fb8F9352B4593A82B05d0c` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1533 | Foundation (NFT marketplace) | Ethereum | FNDNFTMarket (NFTMarket offer/auction) | `0xcDA72070E455bb31C7690a170224Ce43623d0B6f` | 1 | 0/1 | 0 | 1 |  |
| 1534 | Fraction AI | Base | AgentController | `0xB4FA2834ED84E2D32c7d8F1094DF2D1608690C8B` | 1 | 0/1 | 0 | 1 | https://www.halborn.com/audits/fraction-ai/fraction-ai-smart-contracts-55aebf |
| 1535 | FrankenCoin Audit | Ethereum | MintingHub.openPosition / challenge | `0xDe12B620A8a714476A97EfD14E6F7180Ca653557` | 1 | 0/1 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 1536 | FrankenDAO | Ethereum Goerli (testnet) | Staking | `0x732f842fbb3d8CE6b2d527BD5DAc63B760b966f5` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1537 | FrankenDAO | Ethereum Goerli (testnet) | Staking / Governance | `0x732f842fbb3d8CE6b2d527BD5DAc63B760b966f5` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1538 | Frankencoin | Ethereum | Position (V2 clone) | `0x728310FeaCa72dc46cD5BF7d739556D5668472BA` | 1 | 0/1 | 0 | 0 | https://github.com/Frankencoin-ZCHF/Frankencoin/blob/8b4c4ab67bb361b91d58c474b87 |
| 1539 | Frax Finance Governance Protocol | Ethereum | FraxGovernorOmega | `0xBCB25d7582D0738a77508096B05488d49181b255` | 1 | 0/1 | 0 | 1 |  |
| 1540 | Fraxlend (Frax Finance) contest | Ethereum | FraxlendPair | `0x3835a58CA93Cdb5f912519ad366826aC9a752510` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-08-frax-findings/blob/0988d5f2d91d0a174329907 |
| 1541 | Fuji-1 | Arbitrum | Fuji Vault (liquidate) | `0x7aE316c62D04f150CCd31ae49155E408C6079025` | 1 | 0/1 | 0 | 0 | https://0xmacro.com/library/audits/fuji-1 |
| 1542 | Fungify | Ethereum | Fungify NFT Minter / NFT Index exchange  | `0x4268a135840e5273E9DcB3Dc78303767D3964f43` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1543 | Fungify Oct23 | Ethereum | cERC721 BAYC market | `0xa603cee4fd20c589b5aecbf07356b239cb11ee5a` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1544 | GEARBOX PROTOCOL | Ethereum | GEAR token | `0xBa3335588D9403515223F109EdC4eB7269a9Ab5D` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1545 | GMX | Arbitrum | DepositVault / market accounting | `0xF89e77e8Dc11691C9e8757e84aaFbCD8A67d7A55` | 1 | 0/1 | 0 | 0 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1546 | GMX | Arbitrum | ExchangeRouter / WithdrawalHandler | `0x1C3fa76e6E1088bCE750f23a5BFcffa1efEF6A41` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1547 | GMX | Arbitrum | DepositVault | `0xF89e77e8Dc11691C9e8757e84aaFbCD8A67d7A55` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1548 | GMX | Arbitrum | OrderHandler (ADL) | `0x63492B775e30a9E6b4b4761c12605EB9d071d5e9` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/6 |
| 1549 | GMX | Arbitrum | OrderHandler (entry via ExchangeRouter.c | `0x63492B775e30a9E6b4b4761c12605EB9d071d5e9` | 1 | 0/1 | 0 | 1 |  |
| 1550 | GMX Gasless | Arbitrum | GelatoRelayRouter.sol | `0x5503b99308dB6923758F9A22d118207D633c4e87` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1551 | GMX Migration | Arbitrum | Router | `0x7452c558d45f8afC8c83dAe62C3f8A5BE19c71f6` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1552 | GMX Solana - (July | Solana | gmsol-store (increase_position) | `Gmso1uvJnLbawvw7yezdfCDcPydwW2s2iqG3w6MDucLo` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1553 | GMX Synthetics | Arbitrum | PositionPricingUtils | `0xefCAdA759241D10B45d9Cb6265B19ADec97ceced` | 1 | 0/1 | 0 | 0 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1554 | GMX Synthetics | Arbitrum | BaseOrderUtils | `0x441541167b041EC507b5308B7005075a13A28aA7` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1555 | GMX Updates | Arbitrum | ExchangeRouter / funding handler | `0x7C68C7866A64FA2160F78EEaE12217FFbf871fa8` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1556 | GMX Updates | Arbitrum | ExchangeRouter (shift) | `0x7C68C7866A64FA2160F78EEaE12217FFbf871fa8` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1557 | GMX Updates 9 30 24 | Arbitrum | OrderHandler (validFromTime in OrderUtil | `0xa5D2d45228ee2E3A18AB122B2cE84997d008f4Eb` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1558 | GUNZ (Gunzilla bridge) | GUNZ | WGUNBridge.bridgeNativeTokens | `0x6B62bB78DC118aaacB82A764bFBb01774cE164D0` | 1 | 0/1 | 0 | 0 |  |
| 1559 | Galileo Protocol | Ethereum | GalileoStaking | `0x0B4C3D5FFA70589917A9D68c899C607c8E606Ff8` | 1 | 0/1 | 0 | 1 |  |
| 1560 | Gamma Vaults (Gamma Strategies) | Arbitrum | Clearing | `0xb8Fb4031dC09B6d999722d2C51dEf7c0cEbf41E2` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1561 | GammaSwap Labs Core, Strategies and Periphery | Arbitrum | CPMMShortStrategy (sibling of audited Sh | `0x323B9F30b2969877F21142dDbE80e249B33163b8` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1562 | Gearbox Protocol integrations-v3 (Midas RWA | Ethereum | AddressProvider | `0xF7f0a609BfAb9a0A98786951ef10e5FE26cC1E38` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1563 | Gearbox Securitize Audit | Ethereum | Gearbox v3.1 AddressProvider | `0xF7f0a609BfAb9a0A98786951ef10e5FE26cC1E38` | 1 | 0/1 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 1564 | GenieSwap | Ethereum | GenieSwap (Etherscan nametag) | `0x0a267cF51EF038fC00E71801F5a524aec06e4f07` | 1 | 0/1 | 0 | 1 |  |
| 1565 | Gitcoin | Ethereum | RFPSimpleStrategy | `0xc0379c3E6e3140caE35588c09e081F2d8529C7E3` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1566 | Glif Filecoin InfinityPool | Filecoin | InfinityPool.beneficiaryWithdrawable | `0xe764Acf02D8B7c21d2B6A8f0a96C78541e0DC3fd` | 1 | 0/1 | 0 | 1 |  |
| 1567 | Glif Filecoin InfinityPool | Filecoin | Agent data oracle / AgentPolice | `0xE87f7d4C9f9BD235CB1b15b88Ed5E9a844726947` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2023/04/glif-filecoin-infinitypool/ |
| 1568 | Glow | Solana | Glow Airspace (airspace_permit_issuer_cr | `AmAJeyNxxjNHfhBoCpsNMgWxhukdv3DSu3XpLfJspace` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1569 | Glow | Solana | Glow Margin (liquidator_invoke) | `GLoWMgcn3VbyFKiC2FGMgfKxYSyTJS7uKFwKY2CSkq9X` | 1 | 0/1 | 1 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1570 | GnoSwap Audit | Gno.land | pool realm updatePriceCumulatives | `gno.land/r/gnoswap/pool` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/gnoswap-audit |
| 1571 | GoGoPool | Avalanche C-Chain | TokenggAVAX | `0xA25EaF2906FA1a3a13EdAc9B9657108Af7B703e3` | 1 | 0/1 | 1 | 1 |  |
| 1572 | GoGoPool contest | Avalanche | MinipoolManager (Withdrawable/Error stat | `0xc300Bc9B4b690BA7A182126299a0618eCe268Ee7` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-12-gogopool-findings/blob/7b5a175b93bcf796591 |
| 1573 | GoGoPool contest | Avalanche | TokenggAVAX | `0xA25EaF2906FA1a3a13EdAc9B9657108Af7B703e3` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-12-gogopool-findings/blob/7b5a175b93bcf796591 |
| 1574 | GoGoPool contest | Avalanche | Staking | `0xB6dDbf75e2F0C7FC363B47B84b5C03959526AecB` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1575 | GoGoPool contest | Avalanche | MinipoolManager.createMinipool | `0xc300Bc9B4b690BA7A182126299a0618eCe268Ee7` | 1 | 0/1 | 0 | 1 |  |
| 1576 | Goat Tech | Arbitrum Sepolia | Earning | `0xf7a08a0728C583075852Be8B67E47DceB5c71d48` | 1 | 0/1 | 0 | 0 | https://cdn.cantina.xyz/reports/cantina_competition_goat_mar2024.pdf |
| 1577 | Goat Tech | Arbitrum Sepolia | Locker | `0x0265850FE8A0615260a1008e1C1Df01DB394E74a` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_goat_mar2024.pdf |
| 1578 | Goldilocks | Berachain | Goldiswap ($LOCKS) | `0xb7E448E5677D212B8C8Da7D6312E8Afc49800466` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1579 | Goldilocks | Berachain | Goldiswap.stir() | `0xb7E448E5677D212B8C8Da7D6312E8Afc49800466` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1580 | Golem (GNT Deposit Contract) on August 2nd, 2019. | Ethereum | GNT (Golem Network Token) | `0xa74476443119A942dE498590Fe1f2454d7D4aC0d` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1581 | Golom | Ethereum | GolomTrader / staker claim | `0x65Ec659cF37aD5b4C2b79F05f3c669544a9DBa3E` | 1 | 0/1 | 1 | 1 |  |
| 1582 | Gondi Invitational | Ethereum | AuctionLoanLiquidator.settleWithBuyout | `0x237e4421C742d843Fdd96D22294D338507e17091` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-04-gondi-findings/blob/25665cc3b6e095e2a547ca |
| 1583 | Gondi Invitational | Ethereum | MultiSourceLoan.refinanceFull/addNewTran | `0x478f6F994C6fb3cf3e444a489b3AD9edB8cCaE16` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-04-gondi-findings/blob/25665cc3b6e095e2a547ca |
| 1584 | Gondi Invitational | Ethereum | MultiSourceLoan.validateOffer | `0x478f6F994C6fb3cf3e444a489b3AD9edB8cCaE16` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-04-gondi-findings/blob/25665cc3b6e095e2a547ca |
| 1585 | Good Entry | Arbitrum | TokenisableRange (deposit fee accounting | `0xddec418c1a825ac09ad83cc1a28a2c5bcd746050` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-08-goodentry-findings/blob/6ce0e87c2824628d3b |
| 1586 | Gro Protocol | Ethereum | GROToken | `0x3Ec8798B81485A254928B70CDA1cf0A2BB0B74D7` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-06-gro-findings/blob/cfee72dee0b90f97904508d8 |
| 1587 | Grove ALM | Ethereum | UniswapV3Lib / ALMProxy | `0x491EDFB0B8b608044e227225C715981a30F3A44E` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1588 | HANDLE.FI | Arbitrum | handle perps Liquidity Pool (hLP) | `0x1785e8491e7e9d771b2A6E9E389c25265F06326A` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1589 | HMX | Arbitrum | HMX token | `0x83d6c8c06ac276465e4c92e7ac8c23740f435140` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_hmx_sep2023.pdf |
| 1590 | HYBUX | Base | HYBUX token | `0xc0497fb3fc4fd0a17900cf69fc72a03799915301` | 1 | 0/1 | 1 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1591 | Harbor Smart Contract. July | Ethereum | HarborToken | `0xfcA84e796c247f7e1F59a7F73039a939D06F2452` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1592 | Hashlock Pty Ltd | Ethereum | EigenLayer DelegationManager | `0x39053D51B77DC0d36036Fc1fCc8Cb819df8Ef37A` | 1 | 0/1 | 0 | 1 |  |
| 1593 | Havven Token | Ethereum | Havven token / voting (Havven.sol) | `0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/havven-audit/blob/e7f13e85ec44cf9ef99868ff4259ddc832dbb2 |
| 1594 | Hegic | Ethereum | HegicOptionsETH / HegicPool | `0xCB9ebAe59738D9dadC423ADBde66C018777455A4` | 1 | 0/1 | 0 | 1 |  |
| 1595 | Hegic | Ethereum | HEGIC token | `0x584bC13c7D411c00c01A62e8019472dE68768430` | 1 | 0/1 | 1 | 1 |  |
| 1596 | Hello Labs (Bridge + Voting) | Ethereum | VotingSwap (castVotes) | `0xFAa8289820A643B1b6e95Cd6003117dDEF52B1b9` | 1 | 0/1 | 0 | 1 |  |
| 1597 | Hello Labs Bridge | Ethereum | HelloBridge | `0x2ff291D9CAF25696Bfe41B0Aa72021850C473cEC` | 1 | 0/1 | 0 | 1 |  |
| 1598 | Hermez | Ethereum | Hermez._safeTransferFrom / token registr | `0xA68D85dF56E733A06443306A095646317B5Fa633` | 1 | 0/1 | 1 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1599 | Hermez | Ethereum | Hermez / WithdrawalDelayer initialize | `0xA68D85dF56E733A06443306A095646317B5Fa633` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1600 | Hermez (ethereum-evm-hermez) | Ethereum | Hermez.sol | `0xa68d85df56e733a06443306a095646317b5fa633` | 1 | 0/1 | 0 | 1 |  |
| 1601 | Hinkal Protocol | Ethereum | Hinkal transfer circuit / verifier | `0x25e5e82f5702A27C3466fE68f14abDbbAdFca826` | 1 | 0/1 | 1 | 1 |  |
| 1602 | Hodl on November 05, 2020 | Ethereum | HodlDex | `0xC310644A0Cf1cAE7E240A48090c3cdB9Edb53941` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1603 | HoneyJar | Ethereum | HoneyJar (batchMint) | `0xa20CF9B0874c3E46b344DEAEEa9c2e0C3E1db37d` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1604 | Hook | Ethereum | HookBeaconProxy | `0xA14f9695B357c0cB920D70cC8F31fCfF8b4de541` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1605 | Hook Protocol | Ethereum | HookCoveredCallImplV1.mintWithVault | `0x3648080307faC2EE51A01463e47B9ca076DC14A1` | 1 | 0/1 | 1 | 1 |  |
| 1606 | Hook Protocol | Ethereum | HookERC721VaultImplV1 (multiple call opt | `0xb645E7c51dbBB6bA09FD3093F038Ff23d26bFB6f` | 1 | 0/1 | 0 | 1 |  |
| 1607 | Hook Protocol | Ethereum | HookERC721VaultImplV1.mintWithEntitledVa | `0xb645E7c51dbBB6bA09FD3093F038Ff23d26bFB6f` | 1 | 0/1 | 0 | 1 |  |
| 1608 | Hook Protocol | Ethereum | HookCoveredCallImplV1.mintWithVault (sig | `0x3648080307faC2EE51A01463e47B9ca076DC14A1` | 1 | 0/1 | 0 | 1 |  |
| 1609 | Hook Protocol | Ethereum | HookProtocol.initializeBeacon | `0xE11CCED3E6555A1BcbA2E19b9Cf161f040186069` | 1 | 0/1 | 1 | 1 |  |
| 1610 | Hourglass | Ethereum | Hourglass TBT factory (UUPS proxy) | `0x679619FA685a18782a86dD5850124A75E83daD8F` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1611 | Hyperdrive - LST | Ethereum | Hyperdrive.mint (StETHHyperdrive) | `0xd7e470043241C10970953Bd8374ee6238e77D735` | 1 | 0/1 | 1 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1612 | Hyperware Protocol | Base | HYPR token | `0x0000000000f6a4A20f4d340A1c3F3040aC5A255c` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_hyperware_december2024.pdf |
| 1613 | INIT Capital | Mantle | INIT lending pool (collateralization che | `0x6cc1039746803bc325ec6eb7262def3a672ae243` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1614 | INTDAO BoostManager PickCallbackV2 NftDistributorV2 | Ethereum | BoostManager | `0xB6B7521cd3bd116432FeD94c2262Dd02BA616Db4` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1615 | Idle Finance (idle finance idle) | Ethereum | IdleCDO (upgradeable tranche contract) | `0x34dCd573C5dE4672C8248cd12A99f875Ca112Ad8` | 1 | 0/1 | 1 | 1 |  |
| 1616 | Idle Finance Credit Vaults | Ethereum | IdleCDO | `0x3a52fa30c33cAF05fAeE0f9c5Dfe5fd5fe8B3978` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1617 | Ignition Fogo LST | Fogo | Fogo Stake Pool program | `SP1s4uFeTAX9jsXXmwyDs1gxYYf7cdDZ8qHUHVxE1yr` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1618 | Illuminate | Ethereum | Redeemer | `0x4eA57ef203E91AE8c7D9822aa09CC719a9c01aC6` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/12 |
| 1619 | Illuvium Staking V2 (part 4) | Ethereum | ILVPool (staking v2) | `0x7f5f854FfB6b7701540a00C69c4AB2De2B34291D` | 1 | 0/1 | 0 | 1 |  |
| 1620 | Impossible | BNB Chain | IDIA token | `0x0b15ddf19d47e6a86a56148fb4afffc6929bcb89` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 1621 | Impossible Cloud Network Protocol | Base | ICN Link Staking | `0xDa24c1F7669bf9b12EAfE5A3967BC9358eE48A12` | 1 | 0/1 | 0 | 0 | https://cdn.cantina.xyz/reports/cantina_impossible_cloud_may2025.pdf |
| 1622 | InceptionLRT | Ethereum | IMellowRestaker | `0xB94063E58056725ceD8D2b0363E0bD7D8f46875D` | 1 | 0/1 | 0 | 1 | https://github.com/oxor-io/public_audits/blob/06624b6efe70d98702baccef5208ec57db |
| 1623 | Increment Protocol | zkSync Era | Increment (INCR) token | `0xb2c5a37A4C37c16DDd21181F6Ddbc989c3D36cDC` | 1 | 0/1 | 0 | 1 |  |
| 1624 | InfiniFi ThreeSigma 25March | Ethereum | InfiniFi core (flushExcessSafetyBuffer / | `0x3f04b65Ddbd87f9CE0A2e7Eb24d80e7fb87625b5` | 1 | 0/1 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 1625 | Infinity | Ethereum | Infinity Exchange (takeMultipleOneOrders | `0xf1000142679a6a57abd2859d18f8002216b0ac2b` | 1 | 0/1 | 0 | 1 |  |
| 1626 | InfinityPools | Base | InfinityPoolsPeriphery | `0xF8FAD01B2902fF57460552C920233682c7c011a7` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_infinitypools_october2024.pd |
| 1627 | InstaDApp en 1 0 | Ethereum | InstaIndex | `0x2971AdFa57b20E5a416aE5a708A8655A9c74f723` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1628 | Instadapp | Ethereum | FluidLiquidityUserModule (Liquidity Laye | `0x52Aa899454998Be5b000Ad077a46Bbe360F4e497` | 1 | 0/1 | 0 | 1 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 1629 | Instadapp Fluid | Ethereum | Liquidity (supplyExchangePrice) | `0x52Aa899454998Be5b000Ad077a46Bbe360F4e497` | 1 | 0/1 | 0 | 0 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 1630 | Instadapp Fluid | Ethereum | UniV3CheckFallbackCLRSOracle | `0x0BaD69C6DD12f3bd53cDCAd18D3526cDD5ed3141` | 1 | 0/1 | 0 | 0 | https://github.com/statemindio/public-audits/blob/5d887875d5101e04b772107d2801ce |
| 1631 | InsureDAO contest | Ethereum | IndexTemplate | `0x2B16Be3caCAeA56A6FBE613031C0F6b641DF828E` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-01-insure-findings/blob/6bb0b8a20452d8fa3bc3b |
| 1632 | Interfold Encrypted Execution Protocol | Ethereum | Interfold | `0x28cF63B459e6218C69EA97ea7D90541cf648c715` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1633 | Inverse-sDOLA | Ethereum | sDOLA (DolaSavings vault) | `0xb45ad160634c528Cc3D2926d9807104FA3157305` | 1 | 0/1 | 1 | 1 | https://github.com/yAudit/reports-pdf/blob/186eab01a540d4815784bf79356dc7bcf4422 |
| 1634 | Inverse-sDOLA | Ethereum | sDOLA | `0xb45ad160634c528Cc3D2926d9807104FA3157305` | 1 | 0/1 | 1 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1635 | Ion Protocol | Ethereum | ReserveFeed exchange-rate bound | `0x78C3ac7F84F5101422DCd89fB387bD0DeEf8d662` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/ion-protocol-audit |
| 1636 | Ion Protocol | Ethereum | IonPool (Uniswap SwETH oracle) | `0x0000000000eaEbd95dAfcA37A39fd09745739b78` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/ion-protocol-audit |
| 1637 | JOJO | Base | FundingRateArbitrage | `0x8B7e1924fF57EEc8EbD87254E4de6Ff397f039D3` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1638 | JOJO | Base | JOJODealer | `0x2f7c3cf9d9280b165981311b822becc4e05fe635` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1639 | JOJO | Base | JOJO Dealer | `0x2f7c3cf9d9280b165981311b822becc4e05fe635` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1640 | JOJO Exchange Update | Base | JOJODealer (Base) | `0x2f7c3cf9d9280b165981311b822becc4e05fe635` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/136 |
| 1641 | JOJO Exchange Update | Base | JOJODealer | `0x2f7c3cf9d9280b165981311b822becc4e05fe635` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/136 |
| 1642 | JPEG'd contest | Ethereum | JVaultV3 | `0xE1E91ed6760b6866d29a9Ca941BE82EaF7A434c9` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-04-jpegd-findings/blob/467e6075067bf07e92b1fe |
| 1643 | Jovay Rollup | Jovay | L2 ERC20 Bridge | `0x0b13924ea75b6a80beeeb8fa830a92fd3d4922dc` | 1 | 0/1 | 1 | 1 | https://www.openzeppelin.com/news/jovay-rollup-contracts-audit |
| 1644 | Juicebox | Ethereum | JBController (changeTokenOf) | `0x4e3ef8AFCC2B52E4e704f4c8d9B7E7948F651351` | 1 | 0/1 | 0 | 0 |  |
| 1645 | Juicebox V2 contest | Ethereum | JBChainlinkV3PriceFeed / JBPrices | `0xfd6Bc33C9e25c6d9Bbd00b04992E3639E786DCEd` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-07-juicebox-findings/blob/99fff5554cd100013bc |
| 1646 | Jupiter Perp | Solana | Jupiter Perpetuals program | `PERPHjGBqRHArX4DySjwM6UJHiR3sWAatqfdBS2qQJu` | 1 | 0/1 | 1 | 1 | https://osec.io/reports/620faeb1-e426-4e1f-ad9c-ecf58a8934eb |
| 1647 | K613 | Monad | xK613 (Staking#redeemRewards) | `0x9064d55A8A8473fA39c41A16492Fa1094Eb4E8b5` | 1 | 0/1 | 1 | 1 |  |
| 1648 | KUMA Protocol - Versus contest | Ethereum | KIBToken | `0x01bF66BEcDcFD6D59A5Ca18869f494feA086cdfD` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-02-kuma-findings/blob/71b3cf462012012416dd6ee |
| 1649 | KairosSwap Protocol | Base | SwapCore (at SwapStore proxy) | `0x652C91cd2356feE8857Dc9FD69Cb036B53741725` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1650 | Kamino LIMO | Solana | Kamino LIMO program | `LiMoM9rMhrdYrfzUCxQppvxCSG1FcrUK9G8uLq4A1GF` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/15984d4e-4146-800d-a44d-d9698153ddc8 |
| 1651 | Karak | Ethereum | validateWithdrawalCredentials (Karak nat | `0xafa904152e04abff56701223118be2832a4449e0` | 1 | 0/1 | 0 | 0 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1652 | Kaskad Collaborative 1 by | Igra | KaskadStrategy / KaskadActivityTracker | `0x16d92794F5B81d2CdEd0F0958779A410401e6435` | 1 | 0/1 | 0 | 1 | https://github.com/Kaskad-Lending/kaskad-public-docs/blob/1a38d836d7549440dcde6f |
| 1653 | Kelp DAO LRT (Liquid Restaking Token) | Ethereum | LRTDepositPool / LRTConfig (stakedButUnv | `0x036676389e48133B63a802f8635AD39E752D375D` | 1 | 0/1 | 0 | 1 |  |
| 1654 | Kelp DAO / rsETH | Ethereum | LRTDepositPool | `0x036676389e48133B63a802f8635AD39E752D375D` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-11-kelp-findings/blob/3943085368e579ef5be62cb |
| 1655 | Kelp DAO / rsETH | Ethereum | LRTDepositPool / rsETH mint | `0x036676389e48133B63a802f8635AD39E752D375D` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-11-kelp-findings/blob/3943085368e579ef5be62cb |
| 1656 | Key Finance | Arbitrum | LPStaker / UniswapV3 staker integration | `0x40a03B30D0c4D9e5E71164e041EC28CEe6dD9b36` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1657 | Key Finance | Arbitrum | LPStaker reward compounding | `0x40a03B30D0c4D9e5E71164e041EC28CEe6dD9b36` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1658 | Kinetiq | HyperEVM | kHYPE token | `0xfd739d4e423301ce9385c1fb8850539d657c296d` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1659 | Kinetiq | HyperEVM | Kinetiq Staking Manager (exchange rate) | `0x393D0B87Ed38fc779FD9611144aE649BA6082109` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1660 | Kinetiq | HyperEVM | Kinetiq Staking Manager | `0x393D0B87Ed38fc779FD9611144aE649BA6082109` | 1 | 0/1 | 0 | 0 |  |
| 1661 | Kinto Core | Kinto | KintoID / Faucet | `0xf369f78E3A0492CC4e96a90dae0728A38498e9c7` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1662 | Kinto Core | Kinto | KintoWalletFactory / signer policies | `0x8a4720488CA32f1223ccFE5A087e250fE3BC5D75` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1663 | Klaytn Square Governance | Klaytn | AddressBook | `0x0000000000000000000000000000000000000400` | 1 | 0/1 | 0 | 1 | https://github.com/klaytn/governance-contracts-audit/blob/73cafcdc0854ba9dbf2e59 |
| 1664 | Kleros V2 | Arbitrum | KlerosCore | `0x991d2df165670b9cac3B022f4B68D65b664222ea` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1665 | Kofi Finance | Aptos | kapt_coin.move mint | `0x2cc52445acc4c5e5817a0ac475976fbef966fedb6e30e7db792e10619c76181f` | 1 | 0/1 | 1 | 1 | https://osec.io/reports/20684d4e-4146-804f-8313-e096f8ee2ecc |
| 1666 | Kresko Labs Pte. Ltd - July 14, 2023 | Arbitrum | Kresko Diamond (UniswapV2Oracle) | `0x0000000000177abD99485DCaea3eFaa91db3fe72` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1667 | Kresko Labs Pte. Ltd - July 14, 2023 | Arbitrum | Kresko Diamond (LibAssetUtility oracle) | `0x0000000000177abD99485DCaea3eFaa91db3fe72` | 1 | 0/1 | 0 | 0 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1668 | Kresko Labs Pte. Ltd - July 14, 2023 | Arbitrum | Kresko Diamond (Flux oracle) | `0x0000000000177abD99485DCaea3eFaa91db3fe72` | 1 | 0/1 | 0 | 0 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1669 | LFJ - Universal Router | Arbitrum | LFJ LBRouter V2.1 | `0xb4315e873dBcf96Ffd0acd8EA43f689D8c20fB30` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1670 | LI.FI | Ethereum | GenericBridgeFacet (LiFiDiamond) | `0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/LIFI-Spearbit-Security-Review.pdf |
| 1671 | LI.FI | Ethereum | Receiver | `0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/LIFI-retainer1-Spearbit-Security-Review.pdf |
| 1672 | LI.FI | Ethereum | LiFiDiamond | `0x1231DEB6f5749EF6cE6943a275A1D3E7486F4EaE` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/LIFI-Spearbit-Security-Review.pdf |
| 1673 | LSDai | Ethereum | LSDai vault (rebase / share price) | `0xe1A70B24E109F7A8b39806c554E123Efc6769E91` | 1 | 0/1 | 0 | 1 | https://github.com/OmegaAudits/audits/blob/a9891e4b8b01650638370d401bc36f81695a3 |
| 1674 | Larva Labs Meebits | Ethereum | Meebits (ERC-721) | `0x7Bd29408f11D2bFC23c34f18275bBf23bB716Bc7` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2021-04-meebits-findings/blob/d9906d8bcf918b55c462 |
| 1675 | LatteSwap Smart | BNB Chain | LATTEv2 token | `0xa269a9942086f5f87930499dc8317ccc9df2b6cb` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 1676 | Lavarage | Solana | Lavarage pool program (claim collateral  | `CRSeeBqjDnm3UPefJ9gxrtngTsnQRhEJiTA345Q83X3v` | 1 | 0/1 | 1 | 1 |  |
| 1677 | LayerBank | Linea | LayerBank market (exchangeRate/updateSup | `0x009a0b7C38B542208936F1179151CD08E2943833` | 1 | 0/1 | 1 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1678 | LayerZero Core | Ethereum | Endpoint (v1) | `0x66A71Dcef29A0fFBDBE3c6a460a3B5BC225Cd675` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1679 | Legion | Ethereum | Legion sale vault (claim_tokens_from_vau | `0xa0BeB0A8C765482c128a2986c063AF5C3171ff2F` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1680 | Legion (EVM | Ethereum | LegionPreLiquidSale (deployed by factory | `0xa0BeB0A8C765482c128a2986c063AF5C3171ff2F` | 1 | 0/1 | 1 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1681 | LeonicornSwap | BNB Chain | LeonToken | `0x27e873bee690c8e161813de3566e9e18a64b0381` | 1 | 0/1 | 0 | 1 |  |
| 1682 | Level Finance | Arbitrum | LevelFinance (perp diamond facet) | `0xd49ceDdd977617E7579b4502Be5A060e1cAcd225` | 1 | 0/1 | 1 | 1 |  |
| 1683 | Libertum (2025-05 Libertum Bonding) | Base | BondingToken / BondingTokenController | `0x56a38e7216304108e841579041249feb236c887b` | 1 | 0/1 | 1 | 1 |  |
| 1684 | Lido V3 | Ethereum | VaultHub (proxy) | `0x1d201BE093d847f6446530Efb0E8Fb426d176709` | 1 | 0/1 | 1 | 1 | https://github.com/ComposableSecurity/.github/blob/144b868957d165fa3f5210ae80928 |
| 1685 | Lien Protocol | Ethereum | LIEN token | `0xaB37e1358b639Fd877f015027Bb62d3ddAa7557E` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2020/05/lien-protocol/lien-protocol-audit-2020 |
| 1686 | Likwid | Ethereum | Likwid PriceMath / truncatedReserves | `0x065d449ec9D139740343990B7E1CF05fA830e4Ba` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1687 | Liquity | Ethereum | TroveManager (TCR / liquidation logic) | `0xA39739EF8b0231DbFA0DcdA07d7e29faAbCf4bb2` | 1 | 0/1 | 0 | 1 | https://github.com/coinspect/publications/blob/01b04f1f4a2e2c4d7e228b967fedb8991 |
| 1688 | Lisk | Ethereum | Lisk token allocation / claim | `0x6033F7f88332B8db6ad452B7C6D5bB643990aE3f` | 1 | 0/1 | 1 | 1 |  |
| 1689 | Lista DAO | BNB Smart Chain | CreditBroker.withdrawCollateral | `0x2A6704D56BDedF4c7564C9534D7fa8D8D204D578` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_lista_dao_feb2026.pdf |
| 1690 | Lista Dao - Credit Liquidation - Audit Report | BNB Chain | Lista Lending vault (Moolah) | `0x8F73b65B4caAf64FBA2aF91cC5D4a2A1318E5D8C` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1691 | ListaDAO - Smart Collateral | BNB Chain | Liquidator (onMoolahLiquidate) | `0x6a87C15598929B2db22cF68a9a0dDE5Bf297a59a` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1692 | Livepeer | Ethereum | BondingManager | `0x511bc4556d823ae99630ae8de28b9b80df90ea2e` | 1 | 0/1 | 0 | 1 |  |
| 1693 | Livepeer Onchain Treasury Upgrade | Arbitrum | BondingVotes / BondingManager | `0x0B9C254837E72Ebe9Fe04960C43B69782E68169A` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-08-livepeer-findings/blob/f1317e38a91b77b7567 |
| 1694 | Lockbox (Solana) | Solana | liquidity_lockbox | `7ahQGWysExobjeZ91RTsNqTCN3kWyHGZ43ud2vB7VVoZ` | 1 | 0/1 | 0 | 1 |  |
| 1695 | LogX | Arbitrum | LOGX token | `0x59062301fb510f4ea2417b67404cb16d31e604ba` | 1 | 0/1 | 1 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1696 | Lombard Audit | Ethereum | Lombard BTC (LBTC) | `0x8236a87084f8B84306f72007F36F2618A5634494` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/lombard-audit |
| 1697 | LooksRare | Ethereum | LooksRareProtocol (signature domain) | `0x0000000000E655fAe4d56241588680F86E3b2377` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1698 | LucidLabs | Ethereum | L-USDC AssetController (Ethereum) | `0x3b55a4C0691d4D62719D0BFaA435010fBF2F135f` | 1 | 0/1 | 0 | 1 | https://www.halborn.com/audits/lucidlabs/lucidlabs---smart-contract-security-ass |
| 1699 | Lybra Finance | Ethereum | EUSD.mint | `0x97de57eC338AB5d51557DA3434828C5DbFaDA371` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-06-lybra-findings/blob/42bf098c4b2d893469bd58 |
| 1700 | Lybra Finance | Ethereum | LybraConfigurator (proxy) | `0x15a0b351331dB6Aa7AEcE58Bd3Ebc5179eb53d0a` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-06-lybra-findings/blob/42bf098c4b2d893469bd58 |
| 1701 | Lybra Finance | Ethereum | LybraStETHVault.deposit | `0x1Bb85495f7030e5Ff3942BAebe4D79775CC09F2f` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-06-lybra-findings/blob/42bf098c4b2d893469bd58 |
| 1702 | Lybra Finance | Ethereum | LybraStETHVault.collateralRatio | `0x1Bb85495f7030e5Ff3942BAebe4D79775CC09F2f` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-06-lybra-findings/blob/42bf098c4b2d893469bd58 |
| 1703 | Lybra Finance | Ethereum | LybraStETHVault (external LST calls) | `0x1Bb85495f7030e5Ff3942BAebe4D79775CC09F2f` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2023/08/lybra-finance/lybra-finance-audit-2023 |
| 1704 | MCDEX | Ethereum | MCB token (AdminUpgradeabilityProxy) | `0x4e352cf164e64adcbad318c3a1e222e9eba4ce42` | 1 | 0/1 | 0 | 1 |  |
| 1705 | MZeroAudit | Ethereum | PowerToken | `0x5983B89FA184f14917013B9C3062afD9434C5b03` | 1 | 0/1 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 1706 | MZeroAudit | Ethereum | MinterGateway | `0xf7f9638cb444D65e5A40bF5ff98ebE4ff319F04E` | 1 | 0/1 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 1707 | Magpie | BNB Smart Chain | masterMagpie (vote accounting) | `0xa3B615667CBd33cfc69843Bf11Fbb2A1D926BD46` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 1708 | Magpie | BNB Smart Chain | masterMagpie (deposit/claim) | `0xa3B615667CBd33cfc69843Bf11Fbb2A1D926BD46` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 1709 | Magpie | BNB Smart Chain | mCake / masterMagpie | `0xa3B615667CBd33cfc69843Bf11Fbb2A1D926BD46` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 1710 | Maia DAO | Arbitrum | RootChain / Ulysses router | `0x00000000ea00F3F4000e7Ed5Ed91965b19f1009B` | 1 | 0/1 | 1 | 1 |  |
| 1711 | Maia DAO Ecosystem | Arbitrum | BranchPort / _addLocalToken | `0x79f4b04FFCa54BC946aa0ef8E33eE723467f0192` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-05-maia-findings/blob/fa2bd134824cd6bfcbc99ee |
| 1712 | Maia DAO Ecosystem | Arbitrum | BranchBridgeAgent | `0x79f4b04FFCa54BC946aa0ef8E33eE723467f0192` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-05-maia-findings/blob/fa2bd134824cd6bfcbc99ee |
| 1713 | Maia DAO Ecosystem | Arbitrum | BridgeAgent / gas swap | `0x79f4b04FFCa54BC946aa0ef8E33eE723467f0192` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-05-maia-findings/blob/fa2bd134824cd6bfcbc99ee |
| 1714 | Maia DAO Ecosystem | Arbitrum | UlyssesRouter | `0x79f4b04FFCa54BC946aa0ef8E33eE723467f0192` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-05-maia-findings/blob/fa2bd134824cd6bfcbc99ee |
| 1715 | Manifest Protocol | Ethereum | MNFST token | `0x21585BBcD5bDC3f5737620cf0Db2E51978cf60ac` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1716 | Mantle | Ethereum | L1StandardBridge.initialize | `0x95fC37A27a2f68e3A647CDc081F0A89bb47c3012` | 1 | 0/1 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 1717 | Mantle SCs Aug23 (Liquid Staking Protocol) | Mantle | mETH Staking (share rate / withdrawal) | `0xcDA86A272531e8640cD7F1a92c01839911B90bb0` | 1 | 0/1 | 1 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1718 | Mantle cMETH | Mantle | cMETH | `0xE6829d9a7eE3040e1276Fa75293Bde931859e8fA` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1719 | Maple Core V2 | Ethereum | LoanManager (Maple FixedTermLoanManager) | `0x9303aed6231F131F8e61D579cb69aea4DF365F3D` | 1 | 0/1 | 0 | 1 |  |
| 1720 | Maple Finance | Ethereum | syrupUSDC PoolManager | `0x7aD5fFa5fdF509E30186F4609c2f6269f4B6158F` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-12-maple-findings/blob/9b7b5f83a8423ac0256463 |
| 1721 | Maple Finance | Ethereum | PoolManager | `0x7aD5fFa5fdF509E30186F4609c2f6269f4B6158F` | 1 | 0/1 | 1 | 1 | https://github.com/spearbit/portfolio/blob/15a68d516141039dea9e68876b14edd8a83b4 |
| 1722 | Maple Finance smart contracts | Ethereum | MapleToken permit | `0x33349B282065b0284d756F0577FB39c158F935e6` | 1 | 0/1 | 0 | 1 |  |
| 1723 | Maple Finance smart contracts | Ethereum | MapleToken (ERC20 approve) | `0x33349B282065b0284d756F0577FB39c158F935e6` | 1 | 0/1 | 0 | 1 |  |
| 1724 | Maple Labs | Ethereum | MapleToken (MPL) | `0x33349B282065b0284d756F0577FB39c158F935e6` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1725 | Maple Labs | Ethereum | MapleToken (ERC20) | `0x33349B282065b0284d756F0577FB39c158F935e6` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1726 | Mars Protocol Core Contracts CosmWasm Smart Contract | Neutron | Red Bank (Neutron outpost) | `neutron1n97wnm7q6d2hrcna3rqlnyqw2we6k0l8uqvmyqq6gsml92epdu7quugyph` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1727 | Martin Ortner | Ethereum | TBTCSystem (tBTC v1) | `0xe20A5C79b39bC8C363f0f49ADcFa82C2a01ab64a` | 1 | 0/1 | 0 | 1 |  |
| 1728 | Martin Ortner | Ethereum | KeepRandomBeaconOperator.reportUnauthori | `0x70F2202D85a4F0Cad36e978976f84E982920A624` | 1 | 0/1 | 0 | 1 |  |
| 1729 | Martin Ortner | Ethereum | TBTCSystem (deposit state transitions) | `0xe20A5C79b39bC8C363f0f49ADcFa82C2a01ab64a` | 1 | 0/1 | 0 | 1 |  |
| 1730 | Megapot v2 | Base | Jackpot | `0x3bAe643002069dBCbcd62B1A4eb4C4A397d042a2` | 1 | 0/1 | 1 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1731 | Mellow Flexible Vaults | Ethereum | RedeemQueue | `0xa2E9c10368d1C25A2318d1967aE5d0458eF0032C` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/0f8f75a7830bf02f55d8e |
| 1732 | Melonport. May 11, 2018. | Ethereum | CanonicalPriceFeed | `0x3736633FEB363292C8DAa2246Fb66d2A10c0e76D` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1733 | Mento-1 | Celo | MedianDeltaBreaker | `0x66Cc4c15C923eC9C8E148bD35bD1B2a24b8465A0` | 1 | 0/1 | 0 | 1 | https://0xmacro.com/library/audits/mento-1 |
| 1734 | Merit Circle Liquidity Mining | Ethereum | TimeLockPool (Staked Merit Circle pool) | `0x5c76aD4764A4607cD57644faA937A8cA16729e39` | 1 | 0/1 | 0 | 1 |  |
| 1735 | Meson Protocol | Ethereum | ProxyToMeson | `0x25aB3Efd52e6470681CE037cD546Dc60726948D3` | 1 | 0/1 | 1 | 1 |  |
| 1736 | Metamask Delegation Framework | Ethereum | DelegationManager / NativeTokenPaymentEn | `0xdb9B1e94B5b69Df7e401DDbedE43491141047dB3` | 1 | 0/1 | 0 | 1 | https://diligence.consensys.io/audits/2024/08/metamask-delegation-framework/meta |
| 1737 | Metamask Delegation Framework | Ethereum | NativeTokenPaymentEnforcer | `0xdb9B1e94B5b69Df7e401DDbedE43491141047dB3` | 1 | 0/1 | 0 | 1 | https://diligence.consensys.io/audits/2024/08/metamask-delegation-framework/meta |
| 1738 | Metapro April11th | BNB Smart Chain | Metapro token (transferFrom) | `0x83b37130B8F6A8eDD4e34C46A2FED1Ac281bFb05` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 1739 | MeteoraAg DLMM | Solana | Meteora DLMM program (add_liquidity/remo | `METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/1d584d4e-4146-80f9-91cb-de29630a024c |
| 1740 | Mikhail Vladimirov and Dmitry Khovratovich | Ethereum | SetToken / SetTokenFactory | `0xE1Cd722575801fE92EEef2CA23396557F7E3B967` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1741 | MilkySwap | Milkomeda | MilkySwap core | `0x063A5E4cD5e15ac66ea47134Eb60e6b30A51B2bf` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1742 | Mimo DeFi contest | Ethereum | PARMinerV2 | `0x6D0a6e30eCeE498f64F77c59e3ddedC02b7d9770` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-04-mimo-findings/blob/95141d2aa52279233eabfa7 |
| 1743 | Mitosis | Ethereum | MitosisVault.convertToShares | `0xE4cf2D4eb9c01784798679F2FED4CF47cc59a3ec` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1744 | Monerium (Wake Arena AI review) | Ethereum | Monerium EURe token (Ethereum) | `0x39b8B6385416f4cA36a20319F70D28621895279D` | 1 | 0/1 | 0 | 0 | https://github.com/Ackee-Blockchain/public-wake-arena-reports/blob/e6553332fd1e5 |
| 1745 | MonoX | Polygon | MonoXPool | `0x59653E37F8c491C3Be36e5DD4D503Ca32B5ab2f4` | 1 | 0/1 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1746 | Monolith Stablecoin Factory | Ethereum | Monolith Factory V2 | `0xc68F3e777f28c52FF9DB0276a14F59D96Aa2f931` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/1212 |
| 1747 | Monstro DeFi | Base | MONSTRO token | `0x1d3be1cc80ca89ddbabe5b5c254af63200e708f7` | 1 | 0/1 | 0 | 1 |  |
| 1748 | Moonwell Finance Compound Vault Smart Contract Security | Base | Comptroller (Base) | `0xfBb21d0380beE3312B33c4353c8936a0F13EF26C` | 1 | 0/1 | 1 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1749 | Morpho | Ethereum | Morpho CompoundV2 Optimizer (lazy P2P sn | `0x8888882f8f843896699869179fB6E4f7e3B58888` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/Morpho-Spearbit-Security-Review.pdf |
| 1750 | Morpho Blue | Ethereum | Morpho (Blue) | `0xBBBBBbbBBb9cC5e90e3b3Af64bdAF62C37EEFFCb` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_morpho_blue_dec2023.pdf |
| 1751 | Mover | Ethereum | Treasury / staking | `0x94F748BfD1483750a7dF01aCD993213Ab64C960F` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1752 | Moxie 11 24 | Base | MoxieBondingCurveV2.updateReserveRatio | `0x373065e66B32a1C428aa14698dFa99BA7199B55E` | 1 | 0/1 | 1 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1753 | Muffin | Ethereum | Muffin periphery / MuffinHub | `0x6690384822afF0B65fE0C21a809F187F5c3fcdd8` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1754 | Mugen | Arbitrum | ArbitrumSwaps | `0xfc77b86f3ade71793e1eec1e7944db074922856e` | 1 | 0/1 | 1 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/s |
| 1755 | Multipli Vault | Ethereum | rwaUSDi token (Ethereum) | `0xa39986f96b80d04e8d7aeaaf47175f47c23fd0f4` | 1 | 0/1 | 0 | 1 | https://github.com/shieldify-security/audits-portfolio/blob/697ce229893e8b81133e |
| 1756 | Munchables | Blast | LockManager.setLockDuration | `0xEA091311Fc07139d753A6BBfcA27aB0224854Bae` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-05-munchables-findings/blob/788b270a90933d954 |
| 1757 | Mycelium | Arbitrum | Vault | `0xC74fE4c715510Ec2F8C61d70D397B32043F55Abe` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/7 |
| 1758 | Mysten Deepbook | Sui | DeepBook custodian | `0x000000000000000000000000000000000000000000000000000000000000dee9` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/3d5aff70-3359-42ee-a717-9e02a6a1b555 |
| 1759 | NEAR Burrow Burrowland - Smart Contracts | NEAR | Burrow contract (margin withdraw) | `contract.main.burrow.near` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1760 | NEAR Burrow Burrowland - Smart Contracts | NEAR | Burrow liquidation | `contract.main.burrow.near` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 1761 | NUTS Pike | Sonic | OracleEngine (oracle-driven price update | `0x65D6c833e36B5C47f194A68C4bA138b4019D17a0` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1762 | NUTS Pike | Sonic | ChainlinkCompositeOracleProvider.price() | `0x65D6c833e36B5C47f194A68C4bA138b4019D17a0` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1763 | NUTS Pike | Sonic | Pike market exchange-rate handling | `0xcB53d44FF0b466daebCcE311A8F7bB1DF569AceD` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1764 | Napier | Ethereum | Napier AMM / pool valuation | `0x5a2d321eD5C525e52A3b8d295c6D097a3c78B821` | 1 | 0/1 | 0 | 1 |  |
| 1765 | Napier Finance | Ethereum | Factory (proxy) | `0x0000001afbCA1E8CF82fe458B33C9954A65b987B` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_napier_february2025.pdf |
| 1766 | Native Smart Contract V2 | Ethereum | CreditVault | `0xe60C58d26FD4baeEbea4B74C3284a914a5Fb31cc` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1767 | Navi Protocol | Sui | NAVI price oracle package | `0x4837ae94425107554c8847721cf9954c1ad8e10520433b9e37dc11c507148bea` | 1 | 0/1 | 0 | 1 | https://github.com/movebit/Sampled-Audit-Reports/blob/9f2027ef1500342dec1f1385db |
| 1768 | Nawa USDT stable vault | Ethereum | NawaUSDTVault | `0xabba41142D2bF47a847987603347F94120D45043` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 1769 | Neo Tokyo | Ethereum | BYTES2 (getReward / pool.totalPoints) | `0xa19f5264F7D7Be11c451C093D8f92592820Bea86` | 1 | 0/1 | 0 | 1 |  |
| 1770 | Neo Tokyo contest | Ethereum | NeoTokyoStaker.withdrawLP | `0x67e1eCFA9232E27EAf3133B968A33A9a0dCa9e16` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-03-neotokyo-findings/blob/95032586df4eeef06a2 |
| 1771 | Neptune | Injective | NEPT token (TokenFactory denom) | `injective:factory/inj1v3a4zznudwpukpr8y987pu5gnh4xuf7v36jhva/nept` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/17484d4e-4146-80ed-b006-cb827d75f945 |
| 1772 | Neptune Mutual | Ethereum | Neptune Mutual NPM token | `0x57f12FE6A4e5fe819eec699FAdf9Db2D06606bB4` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/neptune-mutual-audit |
| 1773 | Neverland Money | Monad | Neverland core (lending market / voting  | `0xAD96C3dffCD6374294e2573A7fBBA96097CC8d7c` | 1 | 0/1 | 0 | 1 | https://github.com/ComposableSecurity/.github/blob/144b868957d165fa3f5210ae80928 |
| 1774 | NextGen (6529 Collections) | Ethereum | NextGenCore | `0x4EC94b7f01f7B5F6085933e742123c315865478a` | 1 | 0/1 | 1 | 1 |  |
| 1775 | Nexus Protocol CosmWasm Smart Contract | Terra | Nexus reward distribution | `terra12897djskt9rge8dtmm86w654g7kzckkd698608` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1776 | Nexus Protocol CosmWasm Smart Contract | Terra | Nexus deposit_basset | `terra12897djskt9rge8dtmm86w654g7kzckkd698608` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1777 | NiftyApes Seller Financing (niftyapes seller financing edbc6 | Ethereum | NiftyApesSellerFinancing | `0xEb5302954d013483091C5725d5d3Abe5A703A464` | 1 | 0/1 | 0 | 1 |  |
| 1778 | Nomad | Ethereum | Replica | `0x5d94309e5a0090b165fa4181519701637b6daeba` | 1 | 0/1 | 0 | 1 |  |
| 1779 | Nome Protocol Audit | Berachain | Boardroom.stake | `0x50caa9627a940bcd4d5f3c3ed231252425af50cf` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1780 | Notional | Ethereum | Notional Proxy (V2/V3) | `0x6e7058c91f85e0f6db4fc9da2ca41241f5e4263f` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-08-notional-findings/blob/d7c646ffd3655266b9b |
| 1781 | Notional | Arbitrum | Notional V3 (VaultLiquidationAction) | `0x1344A36A1B56144C3Bc62E7757377D288fDE0369` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1782 | Notional | Ethereum | nTokenERC20Proxy / nTokenAction | `0x2920F9Fc667E780C0CB5a78a104d21413377f97E` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2021-08-notional-findings/blob/d7c646ffd3655266b9b |
| 1783 | Notional | Ethereum | StableMath._calcSpotPrice (Notional V3) | `0x1344a36a1b56144c3bc62e7757377d288fde0369` | 1 | 0/1 | 0 | 1 |  |
| 1784 | Notional | Ethereum | NOTE token (Notional Finance) | `0xCFEAead4947f0705A14ec42aC3D44129E1Ef3eD5` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1785 | Notional (Update 4 / Notional V3) | Ethereum | nProxy (Notional V3) | `0x1344A36A1B56144C3Bc62E7757377D288fDE0369` | 1 | 0/1 | 0 | 1 |  |
| 1786 | Notional Audit | Ethereum | Escrow._settleCashBalance | `0xcfeaead4947f0705a14ec42ac3d44129e1ef3ed5` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/notional-audit |
| 1787 | Nouns | Ethereum | NounsDAOExecutor (treasury) / Nouns DAO  | `0xb1a32FC9F9D8b2cf86C068Cae13108809547ef71` | 1 | 0/1 | 0 | 1 |  |
| 1788 | Nouns DAO | Ethereum | NounsDAOLogicV1Fork.quit | `0x6f3E6272A167e8AcCb32072d08E0957F9c79223d` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-07-nounsdao-findings/blob/6eddc3a6247d9a10fc4 |
| 1789 | NuCypher | Ethereum | NU token | `0x4fE83213D56308330EC302a8BD641f1d0113A4Cc` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1790 | Numoen | Arbitrum | Lendgine (invariant function) | `0x1B327eFf5033922B0f88FC4D56C29d7AF5a8ecdB` | 1 | 0/1 | 0 | 1 |  |
| 1791 | Nuon | Base | NuonStaking | `0xd5369993f46A60531B91507e495E2Fff2dA66e7D` | 1 | 0/1 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 1792 | Nuon | Base | TreasuryAssetFacet | `0x7ec5d62D42bc6dc03E87630eC19AfdC61c7e9061` | 1 | 0/1 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 1793 | OctoLend Report Stellar |  | OctoLend collateral config math | `Stellar` | 1 | 0/1 | 0 | 1 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 1794 | OctoLend Report Stellar |  | OctoLend deallocate | `Stellar` | 1 | 0/1 | 0 | 1 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 1795 | OctoLend Report Stellar |  | OctoLend lending market withdraw_collate | `Stellar` | 1 | 0/1 | 1 | 1 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 1796 | OctoLend Report Stellar |  | OctoLend collateral vault delegation | `Stellar` | 1 | 0/1 | 0 | 1 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 1797 | Olesia Bilenka | Ethereum | NeuralStaking | `0x0a1e8EC04064E895fFC46e97d60001BdcDAbeaac` | 1 | 0/1 | 0 | 1 |  |
| 1798 | Olympus | Ethereum | GovernorBravoDelegator | `0x0941233c964e7d7Efeb05D253176E5E634cEFfcD` | 1 | 0/1 | 0 | 1 |  |
| 1799 | Olympus Convertible Deposits | Ethereum | ConvertibleDepositFacility | `0xEBDe552D851DD6Dfd3D360C596D3F4aF6e5F9678` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1800 | Olympus DAO contest | Ethereum | OHM token | `0x64aa3364F17a4D01c6f1751Fd97C2BD3D7e7f1D5` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-08-olympus-findings/blob/7cc4ee5f297da6e2e4a5 |
| 1801 | Olympus-Cooler-Migrator-Composite | Ethereum | CoolerV2Migrator delegation handling | `0xE045BD0A0d85E980AA152064C06EAe6B6aE358D2` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1802 | Omni AVS | Ethereum | OmniPortal | `0x709e7db90d1960F3B000FEAC67F397a329327E8a` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1803 | Ondo Finance | Ethereum | OUSGInstantManager | `0x1189bAcB100676DB9a495EeC04a730A53A8aD97c` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-03-ondo-finance-findings/blob/4cad6b92dc55972 |
| 1804 | Ondo v1 (Legacy) | Ethereum | SushiStakingV2Strategy | `0x104cf83C1899598d7cF60fbf3f60777e5B373bc0` | 1 | 0/1 | 0 | 1 | https://docs.ondo.finance/assets/files/Ondo-Quantstamp-Audit-January_2022-c670ae |
| 1805 | OpenLeverage Limit Order | BNB Chain | OpenLev core (BSC) | `0x6A75aC4b8d8E76d15502E69Be4cb6325422833B4` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1806 | OpenQ Audit Report | Ethereum | BountyFactory | `0xe711786C549a679c89Ba635a8eeDE0192113D7D9` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/39 |
| 1807 | OpenSea Seaport | Ethereum | Seaport (OrderValidator / order fill acc | `0x00000000006c3852cbEf3e08E8dF289169EdE581` | 1 | 0/1 | 0 | 1 |  |
| 1808 | OpenSea Seaport contest | Ethereum | Seaport OrderValidator | `0x00000000006c3852cbEf3e08E8dF289169EdE581` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-05-opensea-seaport-findings/blob/4f81f94368ed |
| 1809 | OpenSea Seaport contest | Ethereum | Seaport FulfillmentApplier._aggregateVal | `0x00000000006c3852cbEf3e08E8dF289169EdE581` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-05-opensea-seaport-findings/blob/4f81f94368ed |
| 1810 | OpenZK | Ethereum | EigenLayerRETHVault (inherits RocketPool | `0x47eaACA9819460771Db6881165e10E5a26e41155` | 1 | 0/1 | 0 | 1 |  |
| 1811 | Optimism Interop | OP Mainnet | SuperchainTokenBridge (sendERC20/relayER | `0x4200000000000000000000000000000000000028` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/OptimismInterop-Spearbit-Security-Review-Februar |
| 1812 | Optimism Superchain | Ethereum | PreimageOracle (large preimage proposal) | `0x1fb8cdFc6831fc866Ed9C51aF8817Da5c287aDD3` | 1 | 0/1 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 1813 | Optimism Update | Ethereum | L1CrossDomainMessenger | `0x25ace71c97B33Cc4729CF772ae268934F7ab5fA1` | 1 | 0/1 | 0 | 1 |  |
| 1814 | Optimism Update | OP Mainnet | L2CrossDomainMessenger | `0x4200000000000000000000000000000000000007` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/63 |
| 1815 | Optimism Update | OP Mainnet | L2CrossDomainMessenger (predeploy) | `0x4200000000000000000000000000000000000007` | 1 | 0/1 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 1816 | Optimism: Rollup Node and Execution Engine | Ethereum | WithdrawalsRelay (op-node withdrawal pat | `0xbEb5Fc579115071764c7423A4f12eDde41f106Ed` | 1 | 0/1 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 1817 | Opus | Starknet | Shrine.redistribute / redistribute_helpe | `0x0498edfaf50ca5855666a700c25dd629d577eb9afccdf3b5977aec79aee55ada` | 1 | 0/1 | 1 | 1 |  |
| 1818 | Opus | Starknet | Shrine recovery mode | `0x0498edfaf50ca5855666a700c25dd629d577eb9afccdf3b5977aec79aee55ada` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-01-opus-findings/blob/1447b4c01eebc89c420d4f9 |
| 1819 | Opus | Starknet | Shrine.redistribute | `0x0498edfaf50ca5855666a700c25dd629d577eb9afccdf3b5977aec79aee55ada` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2024-01-opus-findings/blob/1447b4c01eebc89c420d4f9 |
| 1820 | Origin Dollar | Ethereum | Curve 3Pool strategy | `0xE75D77B1865Ae93c7eaa3040B038D7aA7BC02F70` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/origin-dollar-audit |
| 1821 | Origin Dollar | Ethereum | OUSD Vault rewards | `0xE75D77B1865Ae93c7eaa3040B038D7aA7BC02F70` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/origin-dollar-audit |
| 1822 | Origin Dollar | Ethereum | VaultCore.mintMultiple | `0xE75D77B1865Ae93c7eaa3040B038D7aA7BC02F70` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1823 | Origin Dollar | Ethereum | OUSD token total supply | `0x2A8e1E676Ec238d8A992307B495b45B3fEAa5e86` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1824 | Origin Dollar (OUSD) | Ethereum | VaultCore.mintMultiple | `0xE75D77B1865Ae93c7eaa3040B038D7aA7BC02F70` | 1 | 0/1 | 0 | 1 |  |
| 1825 | Origin Protocol | Ethereum | V00_Marketplace | `0x819Bb9964B6eBF52361F1ae42CF4831B921510f9` | 1 | 0/1 | 1 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1826 | Origin Protocol | Ethereum | V01_Marketplace | `0x698Ff47B84837d3971118a369c570172EE7e54c2` | 1 | 0/1 | 1 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1827 | OstiumAudit | Arbitrum | OstiumTrading / OstiumPairInfos | `0x4298CC309EA2A4F3712030E0Df94fb041189cc0b` | 1 | 0/1 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 1828 | OstiumAudit | Arbitrum | OstiumTrading | `0x4298CC309EA2A4F3712030E0Df94fb041189cc0b` | 1 | 0/1 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 1829 | Othentic | Ethereum | AvsGovernance.sol | `0x1Ec847849c6E2bFB5d6BF6acab05d0feCF1D4f6A` | 1 | 0/1 | 0 | 1 | https://github.com/ComposableSecurity/.github/blob/144b868957d165fa3f5210ae80928 |
| 1830 | Overlay Protocol contest | Ethereum | OverlayV1UniswapV3Market (deployed as Ov | `0x70cB456202e9aD25d3FdF1D0AC5D6B299a42dC99` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-11-overlay-findings/blob/5bc2f19b9bdc670497f2 |
| 1831 | P2P.org SSV Integration | Ethereum | P2pSsvProxyFactory / P2pOrgUnlimitedEthD | `0x7F12A9904bA021AE3ecE106e10f476b7AfBd830C` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1832 | PAID Network | Ethereum | PAID token | `0x8c8687fC965593DFb2F0b4EAeFD55E9D8df348df` | 1 | 0/1 | 1 | 1 |  |
| 1833 | PERPETUAL PROTOCOL | Optimism | ClearingHouse | `0x82ac2CE43e33683c58BE4cDc40975E73aA50f459` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1834 | Palmy Finance | Oasys | PalmyRewardsVault | `0xf1b8B2422ed7243507336246449b39b40878115F` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1835 | Palmy Finance | Oasys | PalmyOracle | `0xC438858a62a6382d61cf064dD746F25CAf50171d` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1836 | Panoptic | Ethereum | PanopticPool.registerTokenTransfer | `0x0000000000001B1A7fe31692d107cAA42fb06862` | 1 | 0/1 | 0 | 1 |  |
| 1837 | Papr contest | Ethereum | PaprController (auction) | `0x3b29c19ff2fcEa0Ff98D0ef5B184354D74eA74b0` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-12-backed-findings/blob/ee71ce04cc246238a4e22 |
| 1838 | Papr contest | Ethereum | PaprController | `0x3b29c19ff2fcEa0Ff98D0ef5B184354D74eA74b0` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-12-backed-findings/blob/ee71ce04cc246238a4e22 |
| 1839 | ParaSpace | Ethereum | WPunkGateway.supplyPunk | `0x79943CFa53B4DD5067e04a2639cd1FDC0a80BFe1` | 1 | 0/1 | 1 | 1 |  |
| 1840 | ParaSpace contest | Ethereum | WPunkGateway | `0x79943CFa53B4DD5067e04a2639cd1FDC0a80BFe1` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-11-paraspace-findings/blob/9650d134645b411491 |
| 1841 | ParaSpace contest | Ethereum | Pool (NToken claim path) | `0x638a98BBB92a7582d07C52ff407D49664DC8b3ee` | 1 | 0/1 | 1 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1842 | ParagonsDAO | Base | StakedPDT | `0x51e025cb3ee0b99a84f7fb80994198281e29aa3e` | 1 | 0/1 | 0 | 1 |  |
| 1843 | Parallax (parallax) | Arbitrum | Parallax.sol (Parallax core vault) | `0x07F78cC2668F9Bb152c4026E801df68Ed3AB9858` | 1 | 0/1 | 0 | 1 |  |
| 1844 | Parcel | BNB Smart Chain | PayrollManager | `0x35aD5a1cD3533495262aFd982be3003Ea77D3C31` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_parcel_feb2023.pdf |
| 1845 | PariFi | Arbitrum | ParifiVault | `0xbf11ac635fe97430b5333018778d0d746f67c989` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/DefenderAudits/blob/b2a2ccb9b6e07d82a6c4497fee |
| 1846 | PariFi | Arbitrum | FeeManager / MarketVault | `0x57206c5b0cc7aDf30B9AdE22f0C2E526e3DD68E6` | 1 | 0/1 | 1 | 1 | https://github.com/GuardianAudits/DefenderAudits/blob/b2a2ccb9b6e07d82a6c4497fee |
| 1847 | Party | Ethereum | Party implementation (genesis) | `0x52010e220e5c8ef2217d86cfa58da51da39e8ec4` | 1 | 0/1 | 1 | 1 |  |
| 1848 | Party Protocol - Versus contest | Ethereum | InitialETHCrowdfund | `0xd2933a444D8771F265712962BE24096cEa041e0c` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-04-party-findings/blob/04f7ff6417d62b25d258ee |
| 1849 | Party Protocol - Versus contest | Ethereum | PartyGovernance (Party implementation) | `0xb676cfeeed5c7b739452a502f1eff9ab684a56da` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-04-party-findings/blob/04f7ff6417d62b25d258ee |
| 1850 | PartyDAO contest | Ethereum | ProposalExecutionEngine (OpenseaProposal | `0xa51ef92ee7f24eff05f5e5cc2119c22c4f8843f6` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-09-party-findings/blob/a8f57f997597691afb08ec |
| 1851 | PartyDAO contest | Ethereum | ProposalExecutionEngine | `0xa51ef92ee7f24eff05f5e5cc2119c22c4f8843f6` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-09-party-findings/blob/a8f57f997597691afb08ec |
| 1852 | PartyDAO contest | Ethereum | TokenDistributor | `0x1ca2007a81f8a7491bb6e11d8e357fd810896454` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-09-party-findings/blob/a8f57f997597691afb08ec |
| 1853 | PartyDAO contest | Ethereum | ProposalExecutionEngine (ArbitraryCalls/ | `0xa51ef92ee7f24eff05f5e5cc2119c22c4f8843f6` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-09-party-findings/blob/a8f57f997597691afb08ec |
| 1854 | PartyDAO contest | Ethereum | TokenDistributor (genesis) | `0x1ca2007a81f8a7491bb6e11d8e357fd810896454` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1855 | Pashov Audit Group (KittenSwap) | Hyperliquid L1 | Voter / VotingReward (notifyRewardAmount | `0xb7F7053F7e6c210e6777D5BA758E4b3ECa6C88A0` | 1 | 0/1 | 0 | 1 |  |
| 1856 | Peapods | Ethereum | PodUnwrapLocker | `0xaCE71C69Ab1C44c8330DA420BC6FaB1c51959d74` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/749 |
| 1857 | Pentacore | Ethereum | PentacoreToken | `0x3159722840d006d807f10ae833020d34cf26e420` | 1 | 0/1 | 1 | 1 | https://www.iosiro.com/audits/pentacore-smart-contract-audit |
| 1858 | Perennial | Arbitrum | MarketFactory | `0xDaD8A103473dfd47F90168A0E46766ed48e26EC7` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1859 | Perennial | Arbitrum | MarketFactory.updateExtension | `0xDaD8A103473dfd47F90168A0E46766ed48e26EC7` | 1 | 0/1 | 1 | 1 |  |
| 1860 | Perennial | Arbitrum | Market / MarketFactory (getAutoDeleverag | `0xDaD8A103473dfd47F90168A0E46766ed48e26EC7` | 1 | 0/1 | 0 | 1 |  |
| 1861 | Perennial V2 | Arbitrum | Controller (proxy) | `0x197dE1B26ad733380fD22159A2671f497A6DDd7C` | 1 | 0/1 | 1 | 1 |  |
| 1862 | Perennial V2 Update #4 | Arbitrum | MarketFactory | `0xDaD8A103473dfd47F90168A0E46766ed48e26EC7` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/518 |
| 1863 | Perennial v2 (update 1) | Arbitrum | StrategyLib / Perennial vault | `0xad3565680aEcEe27A39249D8c2D55dAc79BE5Ad0` | 1 | 0/1 | 0 | 1 |  |
| 1864 | Perennial v2 (update 1) | Arbitrum | VaultFactory | `0xad3565680aEcEe27A39249D8c2D55dAc79BE5Ad0` | 1 | 0/1 | 1 | 1 |  |
| 1865 | Peridot Protocol | Monad | SimplePeridottroller cache_price | `0x6D208789f0a978aF789A3C8Ba515749598940716` | 1 | 0/1 | 0 | 1 | https://www.halborn.com/audits/peridot-protocol/smart-contract-assessment-e9c4bc |
| 1866 | Peridot Protocol | Monad | Peridot rewards / Peridottroller | `0x6D208789f0a978aF789A3C8Ba515749598940716` | 1 | 0/1 | 0 | 1 | https://www.halborn.com/audits/peridot-protocol/smart-contract-assessment-e9c4bc |
| 1867 | Peridot Protocol | Monad | Peridot liquidation | `0x6D208789f0a978aF789A3C8Ba515749598940716` | 1 | 0/1 | 0 | 1 | https://www.halborn.com/audits/peridot-protocol/smart-contract-assessment-e9c4bc |
| 1868 | PerlinX (Perlin) | Ethereum | PerlinXRewards | `0x5Fa19F612dfd39e6754Bb2E8300E681d1C589Dd4` | 1 | 0/1 | 1 | 1 |  |
| 1869 | PerpCity Protocol | Arbitrum | Pricing module (index EMA) | `0xb0061a34425438073ae78C2FC7c94259e5FE6Cbf` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1870 | Phase | Base | Phase | `0xbe92452bb46485AF3308e6d77786bFBE3557808d` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 1871 | Phi | Base | PhiFactory / Cred | `0xdbe4f7518b0dcb6319a242169c89190e72798b17` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2024-08-phi-findings/blob/0c473d9115cd5a1e90ed5beb |
| 1872 | Phi | Base | PhiFactory.signatureClaim | `0xdbe4f7518b0dcb6319a242169c89190e72798b17` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-08-phi-findings/blob/0c473d9115cd5a1e90ed5beb |
| 1873 | Phi | Base | PhiFactory.createArt | `0xdbe4f7518b0dcb6319a242169c89190e72798b17` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-08-phi-findings/blob/0c473d9115cd5a1e90ed5beb |
| 1874 | Phuture Finance contest | Ethereum | Phuture (PHTR) core contract | `0xE1Fc4455f62a6E89476f1072530C20CF1A0622dA` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-04-phuture-findings/blob/25dd82f2a6e0ece25acb |
| 1875 | PieDAO Experipie | Ethereum | ExperiPie | `0x318d27825678733F381bc7E17ebE82872BAd6ff6` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1876 | Pika Protocol | Optimism | PikaPerpV2 | `0x3b8ed42db806F3D8Dfdc491255eC9b3363D21005` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1877 | Pineapple Staking Contract | Ethereum | PappleStaking | `0x1b8aE875745bfFa658afd034293C64a0EE2BC0fc` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_pineapple_june2025.pdf |
| 1878 | Plaza Finance | Base | BondToken (bondETH) | `0x091A5Abe6616e26268e5eEcFF256c2212fcE2707` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/682 |
| 1879 | Plexus Nov18th | Ethereum | LibPlexusUtil._bridgeSwapStart (facet li | `0xdF378d1BA18dF5539Fc71b8DF6970D54d7787140` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 1880 | Polygon Aggregation Layer | Ethereum | AgglayerBridge | `0x3aB5EC174aED4d982A183d0A17E47F17E49CB021` | 1 | 0/1 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 1881 | Polymath. February 14, 2018. | Ethereum | SecurityTokenRegistry proxy / data store | `0x240f9f86b1465bf1b8eb29bc88cbf65573dfdd97` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1882 | Polymath. July 7, 2018. | Ethereum | PolymathRegistry | `0x7c34d31dB0fe16844C1d3a288181fe127665F06a` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1883 | Pontem Liquidswap | Aptos | Liquidswap core (swap) | `0x190d44266241744264b964a37b8f09863167a12d3e70cda39376cfb4e3561e12` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/cab09ca7-ca5a-4004-858c-a750902148f4 |
| 1884 | Ponzio The Cat | Ethereum | PonzioTheCat | `0x873259322BE8e50d80A4b868D186Cc5aB148543A` | 1 | 0/1 | 1 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1885 | Ponzio The Cat | Ethereum | PonzioTheCat token | `0x873259322BE8e50d80A4b868D186Cc5aB148543A` | 1 | 0/1 | 1 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 1886 | PoolTogether | Optimism | DrawManager (V5) | `0x7eED7444dE862c4F79c5820ff867FA3A82641857` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1887 | PoolTogether (The Prize Layer for DeFi) | Ethereum | PrizePool (V5) | `0x7865d01da4c9ba2f69b7879e6d2483ab6b354d95` | 1 | 0/1 | 0 | 1 |  |
| 1888 | PoolTogether Aave v3 contest | Ethereum | PrizePool (current core) | `0x7865d01da4c9ba2f69b7879e6d2483ab6b354d95` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-04-pooltogether-findings/blob/4935b9fbf3e4060 |
| 1889 | PoolTogether micro contest #1 | Ethereum | POOL governance token | `0x0cEC1A9154Ff802e7934Fc916Ed7Ca50bDE6844e` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-07-pooltogether-findings/blob/954cd0f3174c9fe |
| 1890 | PoolTogether v4 contest | Ethereum | POOL token (governance) | `0x0cec1a9154ff802e7934fc916ed7ca50bde6844e` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-10-pooltogether-findings/blob/6f293539cd7c5b0 |
| 1891 | Possum Labs Portals V2 | Arbitrum | Portals V2 vault | `0x9167CFf02D6f55912011d6f498D98454227F4e16` | 1 | 0/1 | 1 | 1 | https://github.com/shieldify-security/audits-portfolio-md/blob/cb986f228e75a5753 |
| 1892 | Powerbomb Finance | Avalanche | PowerBombAvaxAncSAVAX | `0xf615F2C627948c6a767E28CD1C5D2784F9A2104F` | 1 | 0/1 | 0 | 1 | https://github.com/choco-cupcake/AuditSearcher/blob/bc907c9a314e7b63aaaec698d264 |
| 1893 | PredMart (predmart 2026 04 predmart smart contract) | Polygon | PredmartPoolExtension#pullUsdcForLeverag | `0x009Ef92291aDA76F8524eA327c53Ea7b7A5C3886` | 1 | 0/1 | 1 | 1 |  |
| 1894 | PredMart (predmart 2026 04 predmart smart contract) | Polygon | PredmartLendingPool#leverageDeposit | `0xD90D012990F0245cAD29823bDF0B4C9AF207d9ee` | 1 | 0/1 | 1 | 1 |  |
| 1895 | Predy | Arbitrum | PredyPool liquidation | `0x9215748657319b17fecb2b5d086a3147bfbc8613` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-05-predy-findings/blob/766659221c5d4b5f547710 |
| 1896 | Primev | mev-commit chain | PreconfManager | `0x3761bF3932cD22d684A7485002E1424c3aCCD69c` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_primev_oct2024.pdf |
| 1897 | Primev | mev-commit chain | ProviderRegistry | `0xeb6d22309062a86fa194520344530874221ef48c` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_private_primev.pdf |
| 1898 | Primitive | Ethereum | Option Registry (v1) | `0x16274044dab9635Df2B5AeAF7CeCb5f381c71680` | 1 | 0/1 | 0 | 0 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1899 | Primitive | Ethereum | PrimitiveEngine (RMM01) | `0xd3541aD19C9523c268eDe8792310867C57BE39e4` | 1 | 0/1 | 1 | 1 |  |
| 1900 | Primitive Finance | Ethereum | PrimitiveEngine (RMM) | `0xd3541aD19C9523c268eDe8792310867C57BE39e4` | 1 | 0/1 | 0 | 1 |  |
| 1901 | Prism | Terra | Prism yAsset staking contract | `terra188mmw2vsp0yahen3vh2clup543qrttvdzkxl0h9myfuwjj56nausztpegt` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 1902 | Propchain Aug8th | Ethereum | PropchainStakingV3 | `0x4bAF99F33c0414aAE06543Ab6Fc4a9ae405Ee2f7` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 1903 | Prospective World | Ethereum | Prospective (PROS) token | `0xbe1936A67f503e0eaF2434b0cf9f4e3d7100008A` | 1 | 0/1 | 0 | 1 |  |
| 1904 | Protectorate | Ethereum | Protectorate token (PRTC) | `0xb9098D3669A78e9AfE8b94a97290407400D9dA31` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/s |
| 1905 | Protectorate Protocol | Ethereum | PRTC token | `0xb9098D3669A78e9AfE8b94a97290407400D9dA31` | 1 | 0/1 | 1 | 1 |  |
| 1906 | Public - KatanaInu NFT System | Ethereum | KatanaInu NFT mint | `0x31e189E2595007Fe911c64e5fa53be2ed9A21aCA` | 1 | 0/1 | 1 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 1907 | Public - KatanaInu NFT System | Ethereum | KatanaNFT (ERC-721) | `0x31e189E2595007Fe911c64e5fa53be2ed9A21aCA` | 1 | 0/1 | 0 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 1908 | Public - KatanaInu NFT System | Ethereum | KatanaInu signature check | `0x31e189E2595007Fe911c64e5fa53be2ed9A21aCA` | 1 | 0/1 | 0 | 1 | https://github.com/verichains/public-audit-reports/blob/3ff2d281a466ba67b65be547 |
| 1909 | Pump Fun | Solana | pump.fun bonding-curve program (buy) | `pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/20684d4e-4146-8063-a547-fa89b9e0ce11 |
| 1910 | Putty contest |  | Putty.sol order fill/expiry | `Ethereum` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-06-putty-findings/blob/2d73ab421687e9f6fddaa3 |
| 1911 | Pyth Entropy and Executor smart contracts; Fortuna provider  | Base | Entropy | `0x6e7d74fa7d5c90fef9f0512987605a6d546181bb` | 1 | 0/1 | 0 | 1 |  |
| 1912 | QuantAMM | Ethereum | QuantAMMWeightedPool | `0x6B61D8680C4F9E560c8306807908553f95c749C5` | 1 | 0/1 | 1 | 1 |  |
| 1913 | Quex | Ethereum | Quex Core diamond (FlowFacet / DepositMa | `0x97076a3c0A414E779f7BEC2Bd196D4FdaADFDB96` | 1 | 0/1 | 1 | 1 | https://www.halborn.com/audits/quex/quex-v1-e04ebe |
| 1914 | Quoll Finance Zokyo Oct19 | BNB Chain | QuollMasterChef | `0xf0CC2D6F7ea0214D419C61Cd7c2a6d12c60F6E7b` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 1915 | RIBBON FINANCE | Ethereum | GammaAdapter | `0xCD99B092A5C08c33D09b3e72046A7ab42d8110D1` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1916 | RISEx (Rise) | RISE | TokenManager | `0x07DCE641354bBbc93C785f86971ad9f78f676Bd5` | 1 | 0/1 | 0 | 1 |  |
| 1917 | RISEx (Rise) | RISE | PerpsManager | `0x53f10fAcFC8965750494E6965F5d6dA39B41d852` | 1 | 0/1 | 0 | 1 |  |
| 1918 | RabbitHole Quest Protocol contest | Ethereum | RabbitHoleReceipt / RabbitHoleTickets | `0xEC3a9c7d612E0E0326e70D97c9310A5f57f9Af9E` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-01-rabbithole-findings/blob/a5d665a4dd1912b5d |
| 1919 | Radiant V2 | Arbitrum | LendingPool (Arbitrum) | `0xE23B4AE3624fB6f7cDEF29bC8EAD912f1Ede6886` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1920 | Radiant V2 | Arbitrum | UniswapPoolHelper.getPrice/getLpPrice | `0xfC05ec21b106E0c1e035Ec4718C1394f098FBb57` | 1 | 0/1 | 0 | 0 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1921 | Radiant V2 | Arbitrum | BountyManager (executeBounty/claimBounty | `0x90aBACEC5dEEFf349223EeA076c946C2A630B672` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 1922 | Radiant V2 | Arbitrum | MultiFeeDistribution.individualEarlyExit | `0x76ba3eC5f5adBf1C58c91e86502232317EeA72dE` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/radiant |
| 1923 | Radiant V2 | Arbitrum | UniswapPoolHelper.initializePool / Balan | `0xfC05ec21b106E0c1e035Ec4718C1394f098FBb57` | 1 | 0/1 | 1 | 1 | https://www.openzeppelin.com/news/radiant |
| 1924 | RadicalxChange | Ethereum | RadicalxChange (auction) | `0x5b086e46c05CDab742B5eFE16f45816Afb9A4088` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1925 | Radpie | Arbitrum | Radpie staking / reward accounting (Mast | `0x18a192dFe0BE1E5E9AA424738FdAd800646283b2` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 1926 | Rage Trade | Arbitrum | DnGmxJuniorVault / DnGmxJuniorVaultManag | `0x2AB5fBc64784AfF93A9201285FAdA9CcA94728cC` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1927 | Rage Trade Delta Neutral GMX Vaults | Arbitrum | dnGmxJuniorVault | `0x8478ab5064ebac770ddce77e7d31d969205f041e` | 1 | 0/1 | 1 | 1 |  |
| 1928 | Railgun | Ethereum | RailgunSmartWallet (Groth16 verifier pat | `0xc0BEF2D373A1EfaDE8B952f33c1370E486f209Cc` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1929 | Raydium AMM | Solana | Raydium AMM process_deposit | `675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8` | 1 | 0/1 | 1 | 1 | https://osec.io/reports/44ace4d6-5abe-447d-aff1-ee3388a6b462 |
| 1930 | Reach (reach diff 2 41dcd3b3) | Ethereum | ReachMainDistribution / ReachAffiliateDi | `0x33D900eD82B2B53C44DA7e764f263671667fAD09` | 1 | 0/1 | 0 | 1 |  |
| 1931 | ReactorFusion Protocol | zkSync Era | CToken market behind ReactorFusion Unitr | `0x5f7CBcb391d33988DAD74D6Fd683AadDA1123E4D` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1932 | Ref Finance | NEAR | Ref DCL | `dcl.ref-labs.near` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 1933 | Repository (link) Commit Hash Platform Comment | Stellar | Aquarius stableswap pool (get_d) | `CBQDHNBFBZYE4MKPWBSJOPIYLW4SFSXAXUTSXJN76GNKYVYPCKWC6QUK` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 1934 | Reserve | Solana | Folio program | `DTF4yDGBkXJ25Ech1JVQpfwVb1vqYW4RJs5SuGNWdDev` | 1 | 0/1 | 1 | 1 |  |
| 1935 | Reserve Protocol (Solana DTFs / Folio) | Solana | Rewards program - accrue_rewards | `7GiMvNDHVY8PXWQLHjSf1REGKpiDsVzRr4p7Y3xGbSuf` | 1 | 0/1 | 0 | 1 |  |
| 1936 | Reserve Protocol - October 31, 2022 | Ethereum | RToken issue/redeem (ERC777 path) | `0x258ce833CF9AD19208372763A00aA1565Dd40b3C` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1937 | Reserve Protocol Solana DTFs | Solana | Reserve Folio program (trade instruction | `DTF4yDGBkXJ25Ech1JVQpfwVb1vqYW4RJs5SuGNWdDev` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 1938 | Reserve contest | Ethereum | ConvexStakingWrapper (collateral plugin) | `0x24a4B37F9c40fB0E80ec436Df2e9989FBAFa8bB7` | 1 | 0/1 | 0 | 1 |  |
| 1939 | Reserve contest | Ethereum | Main / AssetRegistry (cToken collateral) | `0x24a4B37F9c40fB0E80ec436Df2e9989FBAFa8bB7` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-01-reserve-findings/blob/5dfa03008e4eb65d6c6a |
| 1940 | Resolv Staking | Ethereum | ResolvStakingV2 | `0x9e20c346D275eF12A9a8853D457EeaD7aaD7FD0b` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1941 | Revest Finance | Ethereum | TokenVault | `0xD672f1E3411c23Edbb49e8EB6C6b1564b2BF8E17` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1942 | Reya Network | Reya Network | OrdersGateway | `0xfc8c96bE87Da63CeCddBf54abFA7B13ee8044739` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1943 | Reya Network | Reya Network | Core | `0xA763B6a5E09378434406C003daE6487FbbDc1a80` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1944 | Rhea Finance | NEAR | lst.rhealab.near (LSD nonce derivation) | `lst.rhealab.near` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 1945 | Ric Flair's Official WOOOOO Coin | Ethereum | WOOOOO token (priceBNB pricing function) | `0x9Fbe014b435bbc65Bc8889eE95539b997EFED07c` | 1 | 0/1 | 0 | 1 |  |
| 1946 | RociFi Aug23 | Polygon | CollateralManager | `0xd85af14C32Cc98Be9Fe5195eDb797773af8bB609` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 1947 | Rocket Pool | Ethereum | RocketRewardsPool | `0xEE4d2A71cF479e0D3d0c3c2C923dbfEB57E73111` | 1 | 0/1 | 0 | 1 |  |
| 1948 | Rocket Pool (Sigma Prime review 5, lower ETH bond) | Ethereum | RocketMinipoolDelegate (minipool initial | `0x03d30466d199Ef540823fe2a22CAE2E3b9343bb0` | 1 | 0/1 | 0 | 1 |  |
| 1949 | Roots | Berachain | TroveManager.openTrove | `0x7716065f4F9B225bB628ae75FA42157F14BFE70C` | 1 | 0/1 | 0 | 1 | https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/t |
| 1950 | Roots (Berachain) | Berachain | Roots Trove (collateral / collateral-gai | `0x7716065f4F9B225bB628ae75FA42157F14BFE70C` | 1 | 0/1 | 0 | 1 |  |
| 1951 | Rubicon | Optimism | RubiconRouter | `0x7Af14ADc8Aea70f063c7eA3B2C1AD0D7A59C4bFf` | 1 | 0/1 | 1 | 1 |  |
| 1952 | Rubicon v2 | Optimism | RubiconRouter | `0x7Af14ADc8Aea70f063c7eA3B2C1AD0D7A59C4bFf` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-04-rubicon-findings/blob/d735f3d7b04f5369e6e8 |
| 1953 | Rysk | Arbitrum | GmxHedgingReactor (gmxPositionCallback) | `0xd3711D400845d5052C518565411cE47d15F52489` | 1 | 0/1 | 0 | 1 | https://github.com/Dedaub/audits/blob/431ec937802fd7118f9c6d533a530aaaf33a2c3a/R |
| 1954 | SENSE. Part I | Ethereum | Divider | `0x86bA3E96Be68563E41c2f5769F1AF9fAf758e6E0` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 1955 | STONE BTC Vault | Ethereum | StakeStone STO token (DefiLlama protocol | `0x1d88713b483a8e45cff0e5cd7c2e15e5fab4534d` | 1 | 0/1 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 1956 | Sablier Finance | Ethereum | SablierV2ProxyPlugin | `0x9bdebF4F9adEB99387f46e4020FBf3dDa885D2b8` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_sablier_jul2023.pdf |
| 1957 | Saddle Finance | Ethereum | Swap (getD) in Saddle stable pool | `0x5f86558387293b6009d7896A61fcc86C17808D62` | 1 | 0/1 | 0 | 1 | https://github.com/saddle-finance/saddle-audits/blob/5767550cfa47bf8ecf00d742be5 |
| 1958 | Safety Module | Ethereum | Depositor(SafetyModule) / SafetyModule l | `0x527d9a8c6fc52480be66d683011c250331e34e5e` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1959 | Saffron Finance (Saffron v2) | Ethereum | RestrictedVaultFactory | `0x7fE802B891734DB681b7353bFF9E6c85ce0ab200` | 1 | 0/1 | 0 | 1 |  |
| 1960 | Salty.IO | Ethereum | Staking | `0x7c6f5E73210080b093E724fbdB3EF7bcdd6D468b` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-01-salty-findings/blob/124cf3d332c1d74705c294 |
| 1961 | Salty.IO | Ethereum | Pools (liquidity/rewards) | `0xf5D65d370141f1fff0Db646c9406Ce051354A8a5` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-01-salty-findings/blob/124cf3d332c1d74705c294 |
| 1962 | Sanctum: Sols |  | Sols pool / holding swap program | `Solana` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_sanctum_sols_mar2026.pdf |
| 1963 | Sanctum: Sols |  | TWTM instruction handler | `Solana` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_sanctum_sols_mar2026.pdf |
| 1964 | Sandclock contest | Ethereum | Vault (deposit) | `0x4c406C068106375724275Cbff028770C544a1333` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-01-sandclock-findings/blob/ad93ada9b3cf4f0824 |
| 1965 | Sandclock contest | Ethereum | Vault (withdraw) | `0x4c406C068106375724275Cbff028770C544a1333` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-01-sandclock-findings/blob/ad93ada9b3cf4f0824 |
| 1966 | Sandclock contest | Ethereum | Vault (sponsor) | `0x4c406C068106375724275Cbff028770C544a1333` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-01-sandclock-findings/blob/ad93ada9b3cf4f0824 |
| 1967 | Sandclock contest | Ethereum | Vault (non-UST underlying) | `0xdb369eEB33fcfDCd1557E354dDeE7d6cF3146A11` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-01-sandclock-findings/blob/ad93ada9b3cf4f0824 |
| 1968 | Sapience-1 | Ethereal | PredictionMarketVault | `0x1f5fF6074095cd27A7EaBd75F0A1Ac4243ecCE91` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 1969 | SatLayer Pool (Patch | Ethereum | SatlayerPool | `0x42a856dbEBB97AbC1269EAB32f3bb40C15102819` | 1 | 0/1 | 0 | 1 | https://github.com/Zellic/publications/blob/73cc37579b498cfd95da0312518d5f85f312 |
| 1970 | SatsBridge | Ethereum | SABR token | `0x9ca98c8b217c3b45074834908555d36af2ac6449` | 1 | 0/1 | 0 | 1 |  |
| 1971 | Saucerswap Labs | Hedera | SaucerSwap V2 Router | `0.0.731861` | 1 | 0/1 | 0 | 1 | https://www.halborn.com/audits/saucerswap-labs/smart-contract-assessment-74e585 |
| 1972 | SeaDrop | Ethereum | SeaDrop | `0x00005EA00Ac477B1030CE78506496e8C2dE24bf5` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/Seadrop-Spearbit-Security-Review.pdf |
| 1973 | Security Technology for Smart Contracts Vesper Finance | Ethereum | Vesper Pool vVSP | `0x63475Ab76E578Ec27ae2494d29E1df288817d931` | 1 | 0/1 | 0 | 1 | https://github.com/Dedaub/audits/blob/431ec937802fd7118f9c6d533a530aaaf33a2c3a/V |
| 1974 | Seedify Fund (bonding curve, Jul 2025) | BNB Smart Chain | SFUND token | `0x477bc8d23c634c154061869478bce96be6045d12` | 1 | 0/1 | 0 | 1 |  |
| 1975 | Seismic | Blast | Seismic lending market (borrow index) | `0xbd233d4ffdaa9b7d1d3e6b18cccb8d091142893a` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1976 | Sentiment | Arbitrum | Controller / UniV2LPOracle (v1) | `0x17b07cfbab33c0024040e7c299f8048f4a49679b` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/1 |
| 1977 | Sentiment | Arbitrum | Controller / ChainlinkOracle (v1) | `0x17b07cfbab33c0024040e7c299f8048f4a49679b` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1978 | Sentiment | Hyperliquid | Pool / oracle path (v2) | `0x36BFD6b40e2c9BbCfD36a6B1F1Aa65974f4fFA5D` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1979 | Sentiment | Arbitrum | Controller / CTokenOracle (v1) | `0x17b07cfbab33c0024040e7c299f8048f4a49679b` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 1980 | Sequence Trail (TrailsIntentEntrypoint) | Ethereum | TrailsIntentEntrypoint.depositToIntentWi | `0x91E9e3Fe369CF005dB2857Ef24955A66d1E692Cf` | 1 | 0/1 | 1 | 1 |  |
| 1981 | Serum v4 | Solana | Serum DEX (market/vault) | `9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin` | 1 | 0/1 | 1 | 1 | https://osec.io/reports/25a2d927-2ffd-42fa-8ece-143c42dd9d2a |
| 1982 | Shell Protocol v2 | Arbitrum | Ocean | `0x96B4f4E401cCD70Ec850C1CF8b405Ad58FD5fB7a` | 1 | 0/1 | 0 | 1 |  |
| 1983 | Sherlock (sherlock) | Ethereum | Sherlock staking (Sherlock.sol) | `0x0865a889183039689034dA55c1Fd12aF5083eabF` | 1 | 0/1 | 1 | 1 |  |
| 1984 | Shezmu | Ethereum | Shezmu token | `0x5fE72ed557d8a02FFf49B3B826792c765d5cE162` | 1 | 0/1 | 1 | 1 |  |
| 1985 | Shift DeFi Platform | Ethereum | Vault | `0x1d71c888961c4600cf0e31f6196b4da7fe72e4b3` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 1986 | Shoebill | Klaytn | Shoebill V1 LenderVault | `0xEE3Db1711ef46C04c448Cb9F5A03E64e7aa22814` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1987 | Shoebill | Klaytn | Shoebill V1 Unitroller (Klayswap USDT-US | `0xEE3Db1711ef46C04c448Cb9F5A03E64e7aa22814` | 1 | 0/1 | 0 | 1 | https://github.com/peckshield/publications/blob/37558e095a7c82c9f4f8db4a84af313e |
| 1988 | Shogun | Ethereum | ShogunLzComposerV1 | `0xBe1A6C35efb7D7E5C1220258609c93F5CA946318` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 1989 | Sickle-4 | Ethereum | SickleFactory | `0x9D70B9E5ac2862C405D64A0193b4A4757Aab7F95` | 1 | 0/1 | 1 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1990 | Sienna.Network AMM Protocol (Updated code) CosmWasm Smart Co | Secret Network | SiennaSwap | `secret1rgm2m5t530tdzyd99775n6vzumxa5luxcllml4` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1991 | Sienna.Network AMM Protocol CosmWasm Smart Contract | Secret Network | SiennaSwap AMM (CosmWasm) | `secret1rgm2m5t530tdzyd99775n6vzumxa5luxcllml4` | 1 | 0/1 | 0 | 1 | https://github.com/HalbornSecurity/PublicReports/blob/4f3d1c6451ac01ba669a43072d |
| 1992 | SigmaMoney round 2 | BNB Chain | Sigma (BSC) | `0x85375d3e9c4a39350f1140280a8b0de6890a40e7` | 1 | 0/1 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 1993 | Silo Finance Dynamic Kink Model | Ethereum | DynamicKinkModel.getCompoundInterestRate | `0xa1BE84eAf52fC2958789326A464720C1198dB7b1` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_silo_sep2025.pdf |
| 1994 | Silverswap | Sonic | SilverSwap core | `0x005851f943ee2957B1748957F26319e4f9EdeBC1` | 1 | 0/1 | 0 | 1 |  |
| 1995 | Singularity | Fantom | SingularityFactory | `0x59b3af6844602aDFCA42CAb17D301439B95FBba3` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 1996 | Size v1 - March 26, 2024 | Ethereum | Size market (lendAsMarketOrder), cbBTC/U | `0x245Be6D7505504F287F71c88326F1AC7024A6Bca` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1997 | Size v1 - March 26, 2024 | Ethereum | SizeFactory (risk-fund configuration and | `0x3A9C05c3Da48E6E26f39928653258D7D4Eb594C1` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 1998 | Skale Proxy Contracts | Ethereum | SKALE Delegation Controller proxy | `0x06dd71dab27c1a3e0b172d53735f00bf1a66eb79` | 1 | 0/1 | 1 | 1 |  |
| 1999 | Skyweaver | Polygon | Skyweaver Market (Niftyswap) | `0x8ea1792998ca57b736a849e84bddb967e3eab194` | 1 | 0/1 | 1 | 1 |  |
| 2000 | SlowMistAuditReport-Ensuro | Ethereum | PolicyPool | `0xd81A8B5bE59cEAE0f9E27455A998B4fDac9fA0a3` | 1 | 0/1 | 0 | 1 | https://github.com/ensuro/ensuro/blob/88a64d3f4bed8db3afe345362ae311c318a4ffb8/a |
| 2001 | SmarDex – USDN Ecosystem | Ethereum | Usdn | `0xde17a000BA631c5d7c2Bd9FB692EFeA52D90DEE2` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 2002 | Smart Wallet | Base | CoinbaseSmartWallet / CoinbaseSmartWalle | `0xBA5ED110eFDBa3D005bfC882d75358ACBbB85842` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2024-03-coinbase-findings/blob/55584d9aeec3c59beef |
| 2003 | Smilee Finance | Arbitrum | Smilee AddressProvider | `0x110A3B051397956D69733B6fe947648bB9062cf1` | 1 | 0/1 | 0 | 1 |  |
| 2004 | Snowbridge | Ethereum | BeefyClient.submitInitial / commitPrevRa | `0x6ed05baa904df3de117ecfa638d4cb84e1b8a00c` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 2005 | Snowbridge | Ethereum | Verification.isCommitmentInHeaderDigest  | `0x27ca963c279c93801941e1eb8799c23f407d68e7` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 2006 | Snowbridge Updates 3 | Ethereum | Gateway | `0x27ca963c279c93801941e1eb8799c23f407d68e7` | 1 | 0/1 | 0 | 1 | https://github.com/oak-security/audit-reports/blob/00ad9f3fb9d9e62c711414777741d |
| 2007 | Sock | Arbitrum | SockAccount (UUPS implementation) | `0xf5771d27f4b9Ce4B8fF7740A320c6c34CF677a9D` | 1 | 0/1 | 0 | 0 |  |
| 2008 | Socket- -mar24 | Ethereum | Socket (SocketDL core, Ethereum) | `0x943AC2775928318653e91d350574436A1b9b16f9` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2009 | Sofa (May | Ethereum | AAVESmartTrendVault._mint | `0x1D2fAAd42cbF3Dc121659d856A9A405ED1067873` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 2010 | Solo Margin Protocol | Ethereum | SoloMargin (AutoTrader) | `0x1E0447b19BB6EcFdAe1e4AE1694b0C3659614e4e` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/solo-margin-protocol-audit-30ac2aaf6b10 |
| 2011 | Sonne | Optimism | Sonne Comptroller / market (Hundred Fina | `0x60CF091cD3f50420d50fD7f707414d0DF4751C58` | 1 | 0/1 | 1 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 2012 | Sorella Angstrom | Ethereum | Angstrom deposit() | `0x0000000aa232009084Bd71A5797d089AA4Edfad4` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/Sorella-Spearbit-Security-Review-October-2024.pd |
| 2013 | Sorella Angstrom | Ethereum | Angstrom PoolUpdates (rewardGrowthOutsid | `0x0000000aa232009084Bd71A5797d089AA4Edfad4` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/Sorella-Spearbit-Security-Review-October-2024.pd |
| 2014 | SpaceCatch | Arbitrum | CATCH staking contract | `0xC878f6936990FDBeF0cDD5177c127BF0E048aA44` | 1 | 0/1 | 0 | 1 |  |
| 2015 | Spartan Protocol Contest | BNB Chain | Pool.mintSynth | `0x2C577706579E08A88bd30df0Fd7A5778A707c3AD` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-07-spartan-findings/blob/18ef13c9d6cb22397e00 |
| 2016 | Spartan Protocol Contest | BNB Chain | Pool.burn | `0x2C577706579E08A88bd30df0Fd7A5778A707c3AD` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-07-spartan-findings/blob/18ef13c9d6cb22397e00 |
| 2017 | Spartan Protocol Contest | BNB Chain | Pool (mintSynth/burn) | `0x2C577706579E08A88bd30df0Fd7A5778A707c3AD` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2021-07-spartan-findings/blob/18ef13c9d6cb22397e00 |
| 2018 | Spartan Protocol Contest | BNB Chain | Synth.realise | `0x2C577706579E08A88bd30df0Fd7A5778A707c3AD` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-07-spartan-findings/blob/18ef13c9d6cb22397e00 |
| 2019 | Spartan Protocol Contest | BNB Chain | Spartan swap (Router/Pool) | `0xfbcdd9270aa6f298851164b2b657eceaf88469be` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-07-spartan-findings/blob/18ef13c9d6cb22397e00 |
| 2020 | Spartan Protocol Contest | BNB Chain | SynthVault | `0xa6C3288C18505D134445cB4Fe8499da22002F1E0` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-07-spartan-findings/blob/18ef13c9d6cb22397e00 |
| 2021 | Spartan Protocol Contest | BNB Chain | Utils.getPoolShareWeight | `0xB7B3216A199893aC00486Fe30439A8F4388fF4C9` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-07-spartan-findings/blob/18ef13c9d6cb22397e00 |
| 2022 | Spartan Protocol Contest | BNB Chain | Router.addDividend | `0xfbcdd9270aa6f298851164b2b657eceaf88469be` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-07-spartan-findings/blob/18ef13c9d6cb22397e00 |
| 2023 | Spectre Protocol | Fantom | Spectre buyout | `0x2834d4F4cC40bd7D78c07E2D848358364222C272` | 1 | 0/1 | 0 | 1 | https://github.com/OmegaAudits/audits/blob/a9891e4b8b01650638370d401bc36f81695a3 |
| 2024 | Sperax farms | Arbitrum | Sperax Demeter farms (reward calibration | `0x5575552988a3a80504bbaeb1311674fcfd40ad4b` | 1 | 0/1 | 1 | 1 |  |
| 2025 | Squads v4 | Solana | Squads v4 program | `SQDS4ep65T869zMMBKyuUq6aD6EgTu8psMjkvj52pCf` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 2026 | Ss | Ethereum | Saturn Dollar (STRC) | `0x23238f20b894f29041f48D88eE91131C395Aaa71` | 1 | 0/1 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 2027 | Stader Labs - bnbX | BNB Chain | bnbX staking / withdrawal manager | `0x3b961e83400D51e6E1AF5c450d3C7d7b80588d28` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 2028 | StakeStone | Ethereum | StoneVault | `0xA62F9C5af106FeEE069F38dE51098D9d81B90572` | 1 | 0/1 | 0 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 2029 | Stakehouse | Ethereum | StakeHouse | `0xD0E710DF4fC3244A47de935d067c0b5eA83933B8` | 1 | 0/1 | 1 | 1 |  |
| 2030 | Stargate | Ethereum | Stargate pool/router | `0x8731d54E9D02c286767d56ac03e8037C07e01e98` | 1 | 0/1 | 1 | 1 | https://osec.io/reports/c1e5cb45-1006-46b8-91eb-5ce9688cec14 |
| 2031 | Stargate Dec31 | Ethereum | LPStaking | `0xB0D502E938ed5f4df2E681fE6E419ff29631d62b` | 1 | 0/1 | 1 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 2032 | StarkNet-DAI-Bridge | Starknet | L2 DAI token | `0x00da114221cb83fa859dbdb4c44beeaa0bb37c7537ad5ae66fe5e0efd20e6eb3` | 1 | 0/1 | 1 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 2033 | Starknet Staking | Starknet | Staking contract (on_receive) | `0x00ca1702e64c81d9a07b86bd2c540188d92a2c73cf5cc0e508d949015e7e84a7` | 1 | 0/1 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 2034 | SteakHut Liquidity V2 | Avalanche | SteakToken | `0xb279f8DD152B99Ec1D84a489D32c35bC0C7F5674` | 1 | 0/1 | 0 | 1 | https://github.com/shieldify-security/audits-portfolio-md/blob/f2c051af4ffb67e11 |
| 2035 | Story Protocol (Core) | Story | LicensingModule.addPILPolicyToIp | `0xB0eB55c311D97FAB279b5e1AfDcB61f7BBc1b3D0` | 1 | 0/1 | 0 | 1 | https://fuzzland.notion.site/Story-Protocol-Invariant-Dev-Report-073631ea8323492 |
| 2036 | Story Protocol (Core) | Story | IPAssetRegistry | `0xa60085269D35d93c298a9151689C962c2771f981` | 1 | 0/1 | 0 | 1 | https://fuzzland.notion.site/Story-Protocol-Invariant-Dev-Report-073631ea8323492 |
| 2037 | Strata Tranches | Ethereum | Strata tranche (onAprChanged) | `0x3d7d6fdf07EE548B939A80edbc9B2256d0cdc003` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 2038 | Stryke | Arbitrum | OptionMarketOTMFE | `0xEec2bE5c91ae7f8a338e1e5f3b5DE49d07AfdC81` | 1 | 0/1 | 1 | 1 |  |
| 2039 | Stryke | Arbitrum | CLAMM position manager / settlement | `0x8f6C063c4B7d6037730f984C6dC38febdACE9eb8` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_stryke_aug2025.pdf |
| 2040 | Sturdy | Ethereum | DebtManager.requestLiquidity | `0x3f1e01C07539b9E4941ab58b1258CBB6c4066063` | 1 | 0/1 | 0 | 1 |  |
| 2041 | Sturdy (Aura integration and leverage) | Ethereum | GeneralLevSwap (Aura LevSwap instance) | `0xB508171E31273887CB530B5268834C218B3A1303` | 1 | 0/1 | 0 | 0 |  |
| 2042 | Subscription Token Protocol | Base | STPv1 implementation (created by STPv1Fa | `0x3BeF7e58a3F357eC98b639df5c24DaC68Ee3A180` | 1 | 0/1 | 0 | 1 |  |
| 2043 | Succinct | Ethereum | SSZ.restoreMerkleRoot (library) | `0x504565337A0298907B301f3Cd4919312969774B1` | 1 | 0/1 | 0 | 1 |  |
| 2044 | Succinct (Telepathy) - ethereum-evm-succinct | Polygon | Telepathy LightClient (BLS sync-committe | `0xaa1383Ee33c81Ef2274419dd5e0Ea5cCe4baF6cC` | 1 | 0/1 | 0 | 1 |  |
| 2045 | Sudoswap LSSVM2 | Ethereum | LSSVMPairFactory (LSSVM2) | `0xA020d57aB0448Ef74115c112D18a9C231CC86000` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/SudoswapLSSVM2-Spearbit-Security-Review.pdf |
| 2046 | Superfluid Locker System | Base | SUP token | `0xa69f80524381275a7ffdb3ae01c54150644c8792` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/968 |
| 2047 | Superform | Ethereum | SuperPositions | `0x01dF6fb6a28a89d6bFa53b2b3F20644AbF417678` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_superform_erc1155a_dec2023.p |
| 2048 | Superform | Ethereum | SuperPositions / ERC1155A base | `0x01dF6fb6a28a89d6bFa53b2b3F20644AbF417678` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_superform_erc1155a_dec2023.p |
| 2049 | Superform Core | Ethereum | SuperExecutorBase | `0x9cC8EDCC41154aaFC74D261aD3D87140D21F6281` | 1 | 0/1 | 0 | 1 |  |
| 2050 | Superform v2 Periphery | Ethereum | ECDSAPPSOracle | `0x366d88F03B8EF34eb49F32a927ff6e1609F694F2` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/Superform-v2-periphery-Spearbit-Security-Review- |
| 2051 | Surge | Arbitrum | Surge pool (ERC-4626 style vault) | `0x503A14768e23456620fB3Cb61e37A36A2736Cbd0` | 1 | 0/1 | 1 | 1 |  |
| 2052 | Sushi | Ethereum | Sushi NonfungiblePositionManager | `0x2214a42d8e2a1d20635c2cb0664422c528b6a432` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 2053 | Sushi | Ethereum | Sushi clAMM Position Manager | `0x2214a42d8e2a1d20635c2cb0664422c528b6a432` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 2054 | Sushi BentoBox | Ethereum | BentoBoxV1 (withdraw) | `0xF5BCE5077908a1b7370B9ae04AdC565EBd643966` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 2055 | Sushi Miso contest | Ethereum | PostAuctionLauncher | `0xaB235da7f52d35fb4551AfBa11BFB56e18774A65` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2021-09-sushimiso-findings/blob/3af5f74fd7f0fa1fb1 |
| 2056 | SwapX - VE Scope | Sonic | RewardsDistributor | `0x1C236D74f61C6199e6D23201D53a59753f4c94D3` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 2057 | Swell Network (Sigma Prime review) | Ethereum | Swell (swETH) validator deposit logic | `0xf951E335afb289353dc249e82926178EaC7DEd78` | 1 | 0/1 | 1 | 1 |  |
| 2058 | Swivel contest | Ethereum | Swivel Governance Token | `0xbf30461210b37012783957D90dC26B95Ce3b6f2d` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-09-swivel-findings/blob/6c414e4932cc42e190092 |
| 2059 | Symbiosis Finance | Ethereum | SIS token | `0xd38bb40815d2b0c2d2c866e0c72c5728ffc76dd9` | 1 | 0/1 | 0 | 1 | https://github.com/Decurity/audits/blob/736e3b80199dca77f5e3ee727c1d5853a9247f76 |
| 2060 | Symbiotic | Ethereum | VaultFactory / Vault (Vaults V2) | `0xAEb6bdd95c502390db8f52c8909F703E9Af6a346` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 2061 | Symmetrical | Base | Symmio diamond (LibMuon) | `0x91Cf2D8Ed503EC52768999aA6D8DBeA6e52dbe43` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2062 | Symmetrical (SYMMIO) | BNB Chain | Symmio perps diamond (LibMuon signature  | `0x9A9F48888600FC9c05f11E03Eab575EBB2Fc2c8f` | 1 | 0/1 | 0 | 1 |  |
| 2063 | Synthetix | Ethereum | EtherCollateralsUSD._splitInterestsAndLo | `0xfED77055B40d63DCf17ab250FFD6948FBFF57B82` | 1 | 0/1 | 1 | 1 | https://www.iosiro.com/audits/synthetix-fomalhaut-release-smart-contract-audit |
| 2064 | Synthetix | Ethereum | RewardsManagerModule.claimRewards | `0xefaca6fc316b3b2aa6c55ff5e02a62a85d4391e8` | 1 | 0/1 | 0 | 1 | https://www.iosiro.com/audits/synthetix-v3-smart-contract-audit |
| 2065 | Synthetix | Ethereum | MarketCollateralModule.depositMarketColl | `0xefaca6fc316b3b2aa6c55ff5e02a62a85d4391e8` | 1 | 0/1 | 0 | 1 | https://www.iosiro.com/audits/synthetix-v3-smart-contract-audit |
| 2066 | Synthetix | Ethereum | EtherCollateralsUSD.liquidateLoan | `0xfED77055B40d63DCf17ab250FFD6948FBFF57B82` | 1 | 0/1 | 0 | 1 | https://www.iosiro.com/audits/synthetix-fomalhaut-release-smart-contract-audit |
| 2067 | Synthetix | Ethereum | IssueUSDModule | `0xefaca6fc316b3b2aa6c55ff5e02a62a85d4391e8` | 1 | 0/1 | 0 | 1 | https://www.iosiro.com/audits/synthetix-v3-smart-contract-audit |
| 2068 | Synthetix SNX Vaults | Base | Synthetix V3 vault/order module (SNX Vau | `0x32C222A9A159782aFD7529C87FA34b96CA72C696` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 2069 | TONCO CLAMM DEX v1.6 | TON | Router (v1.6) | `EQBt0NCO16Ng6QqOb8YaRcnV_vzIAfbLKhMMBBZpYNUbl3sB` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 2070 | Taiko | Ethereum | LibBytesUtils.toBytes32 (used by Bridge/ | `0x9e0a24964e5397B566c1ed39258e21aB5E35C77C` | 1 | 0/1 | 0 | 1 |  |
| 2071 | Taiko Taiko | Ethereum | TaikoInbox | `0x06a9Ab27c7e2255df1815E6CC0168d7755Feb19a` | 1 | 0/1 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 2072 | Tapioca | Arbitrum | YieldBox | `0xCFFd997DB053c0fC54010770b55A4E02B1D104a5` | 1 | 0/1 | 1 | 1 |  |
| 2073 | Tapioca DAO | Arbitrum | YieldBox / BaseTOFT | `0xCFFd997DB053c0fC54010770b55A4E02B1D104a5` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-07-tapioca-findings/blob/4193111261e3cf8de27c |
| 2074 | Tapioca DAO | Arbitrum | Usdo | `0xeb99062643ca5ab880c077288345e0b14b297432` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2075 | TeaREX | Sei | TradingCore / Position | `0xedf7732991b3de8f46fb97dcd4c5cdb28e6ad859` | 1 | 0/1 | 0 | 1 | https://github.com/sec3-service/reports/blob/13c2f82d576164c7db728108d09a8d37272 |
| 2076 | Teller | Base | CollateralManager | `0x71B04a8569914bCb99D5F95644CF6b089c826024` | 1 | 0/1 | 0 | 0 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2077 | Teller Finance | Ethereum | TellerV2 | `0x311aBb81Dee5DE777980e635C33DF2eF79974dc7` | 1 | 0/1 | 1 | 1 |  |
| 2078 | Teller finance | Ethereum | TellerV2 | `0x6BBf498C429C51d05bcA3fC67D2C720B15FC73B8` | 1 | 0/1 | 0 | 1 |  |
| 2079 | Tempus Finance | Ethereum | TempusController (report-supplied, not a | `0xd4330638b87f97ec1605d7ec7d67ea1de5dd7aaa` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-10-tempus-findings/blob/3fec163bbb7f2374b5ff0 |
| 2080 | Tenderize | Ethereum | Tenderizer (unstake without burning) | `0xa7cA8732Be369CaEaE8C230537Fc8EF82a3387EE` | 1 | 0/1 | 0 | 1 | https://github.com/choco-cupcake/AuditSearcher/blob/bc907c9a314e7b63aaaec698d264 |
| 2081 | Tensor | Solana | Tensor sale settlement (Tensor Swap) | `TCMPhJdwDryooaGtiocG1u3xcYbRpiJzb283XfCZsDp` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_tensor_nov2024.pdf |
| 2082 | Tensorplex wstTAO and wstTAOProxy | Ethereum | WstTAOProxy | `0x0BF204b3fAFa21310012D7E61d045856e2Fe26d0` | 1 | 0/1 | 0 | 1 |  |
| 2083 | Term Finance Term Finance Contracts | Ethereum | authenticate (auth token) | `0x2879C9D15406e7EBD46770f4B0781Fe665f9da1b` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 2084 | TermStructureLabs TermMax Phase3 v 1 0 | Arbitrum | TermMax market/factory (Phase 3 v1.0) | `0x14920Eb11b71873d01c93B589b40585dacfCA096` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 2085 | Thales AMM | Optimism | ThalesAMM | `0x266b5d4717661F4Ef37Af4379c066ab8E046BB22` | 1 | 0/1 | 0 | 1 | https://www.iosiro.com/audits/thales-amm-smart-contract-audit |
| 2086 | Thales DAO | Optimism | THALES token | `0x217D47011b23BB961eB6D93cA9945B7501a5BB11` | 1 | 0/1 | 1 | 1 | https://www.iosiro.com/audits/thales-airdrop-and-staking-smart-contract-audit |
| 2087 | The Compact | Ethereum | TheCompact | `0x00000000000000171ede64904551eeDF3C6C9788` | 1 | 0/1 | 1 | 1 | https://www.openzeppelin.com/news/the-compact-audit |
| 2088 | The Graph | Arbitrum | SubgraphService | `0xb2Bb92d0DE618878E438b55D5846cfecD9301105` | 1 | 0/1 | 1 | 1 | https://0xmacro.com/library/audits/the-graph-1 |
| 2089 | Thesis - tBTC and keep | Ethereum | bitcoin-spv (library used by TBTCSystem) | `0x41A1b40c1280883eA14C6a71e23bb66b83B3fB59` | 1 | 0/1 | 0 | 1 | https://diligence.security/audits/2020/02/thesis-tbtc-and-keep/ |
| 2090 | Thesis - tBTC and keep | Ethereum | KeepRandomBeaconOperator.reportUnauthori | `0x70F2202D85a4F0Cad36e978976f84E982920A624` | 1 | 0/1 | 0 | 1 | https://diligence.consensys.io/audits/2020/02/thesis-tbtc-and-keep/thesis-tbtc-a |
| 2091 | Thorchain | Ethereum | THORChain_Router (deposit/approval path) | `0xD37BbE5744D730a1d98d8DC97c42F0Ca46aD7146` | 1 | 0/1 | 1 | 1 |  |
| 2092 | Thorn protocol | Sapphire | StableSwapFactory | `0x1286ecdac50215a366458a14968fbca4bd95067d` | 1 | 0/1 | 1 | 1 | https://github.com/hats-finance/Thorn-protocol-0x1286ecdac50215a366458a14968fbca |
| 2093 | Threshold-USD BAMM | Ethereum | BAMM StabilityPool | `0xF6374AEfb1e69a21ee516ea4B803b2eA96d06f29` | 1 | 0/1 | 1 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 2094 | TiTi | Ethereum | TiTiToken | `0x3bdffA70f4b4E6985eED50453c7C0D4A15dcEc52` | 1 | 0/1 | 1 | 1 |  |
| 2095 | Tigris Trade contest | Polygon | Trading.initiateLimitOrder / TradingLibr | `0x28c5d4416f6cf0FC5F557067b54BD67a43fcC98F` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-12-tigris-findings/blob/e5a0c7faf68116af201f8 |
| 2096 | Tigris Trade contest | Polygon | Trading.limitClose/_checkDelay/updateTpS | `0x28c5d4416f6cf0FC5F557067b54BD67a43fcC98F` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-12-tigris-findings/blob/e5a0c7faf68116af201f8 |
| 2097 | Tigris Trade contest | Polygon | Trading.limitClose / _limitClose | `0x28c5d4416f6cf0FC5F557067b54BD67a43fcC98F` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-12-tigris-findings/blob/e5a0c7faf68116af201f8 |
| 2098 | Tigris Trade contest | Polygon | Position.mint | `0xBB323fE012BFA1728AF14941D09E479612b64281` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-12-tigris-findings/blob/e5a0c7faf68116af201f8 |
| 2099 | Tigris Trade contest | Polygon | Trading._closePosition | `0x28c5d4416f6cf0FC5F557067b54BD67a43fcC98F` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-12-tigris-findings/blob/e5a0c7faf68116af201f8 |
| 2100 | Tigris Trade contest | Polygon | Lock.claim / BondNFT.claim | `0x5df98aa475d8815df7cd4fc4549b5c150e8505be` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-12-tigris-findings/blob/e5a0c7faf68116af201f8 |
| 2101 | TigrisTrade Sep19 | Arbitrum | Tigris Trading | `0x399214eE22bF068ff207adA462EC45046468B766` | 1 | 0/1 | 1 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 2102 | Timeswap | Arbitrum | TimeswapV2PeripheryNoDexQuoterCloseLendG | `0xa0128cddeadbc5e28ed2caba0e01674c84ed3df4` | 1 | 0/1 | 0 | 1 |  |
| 2103 | Tokemak | Ethereum | LMPVaultRouter (LMPVaultRouterBase) | `0x33bea4fcb185eeb39b5c56c5d2c47a079e18272d` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2104 | Tokemak | Ethereum | CurveV2CryptoEthOracle | `0x075c80cd9E8455F94b7Ea6EDB91485F2D974FB9B` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/101 |
| 2105 | Tool used VSCode | Arbitrum | MarketUtils / OrderHandler | `0x63492B775e30a9E6b4b4761c12605EB9d071d5e9` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2106 | Tool used VSCode | Arbitrum | OrderHandler (decrease-order collateral  | `0x63492B775e30a9E6b4b4761c12605EB9d071d5e9` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/74 |
| 2107 | Tracer DAO Perpetual Pools Updates | Arbitrum | PoolFactory | `0x3Feafee6b12C8d2E58c5B118e54C09F9273c6124` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 2108 | Trader Joe v2 contest | Avalanche | LBPair (LBToken) | `0x8e42f2F4101563bF679975178e880FD87d3eFd4e` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-10-traderjoe-findings/blob/461fa698fa564793f5 |
| 2109 | Trader Joe v2 contest | Avalanche | LBPair.collectFees | `0x8e42f2F4101563bF679975178e880FD87d3eFd4e` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-10-traderjoe-findings/blob/461fa698fa564793f5 |
| 2110 | TransitSwap v4 Core | BNB Chain | TransitSwapRouterV4._beforeSwap | `0xb45A2DDA996C32E93B8c47098E90Ed0E7ab18E39` | 1 | 0/1 | 1 | 1 | https://github.com/slowmist/Knowledge-Base/blob/ca4ff9fe9f633c174c09fd189658902d |
| 2111 | TridentRouter | Polygon | TridentRouter | `0x7A250C60Cde7A5Ca7B667209beAB5eA4E16eed67` | 1 | 0/1 | 0 | 1 | https://github.com/Certora/SecurityReports/blob/646989b731edde67fd42904336c5242e |
| 2112 | Trueo Protocol | Base | TruthMarketManager / LaunchpadFactory | `0x21cfcfc3d8f98fc728f48341d10ad8283f6eb7ab` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 2113 | Trueo Uni V4 | Base | OrderManager.sol | `0x21cfcfc3d8f98fc728f48341d10ad8283f6eb7ab` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 2114 | Trueo Updated | Base | TRUE token | `0x21cfcfc3d8f98fc728f48341d10ad8283f6eb7ab` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 2115 | Truflation | Ethereum | TrufVesting | `0x7E3Ad114031ACd0437cCBA560f592874e62780B6` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2116 | Trustswap SwapToken | Ethereum | SWAP (SwapToken) | `0xcc4304a31d09258b0029ea7fe63d032f52e44efe` | 1 | 0/1 | 0 | 1 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 2117 | Turbo (Tribe) | Ethereum | Turbo / TurboSafe (ERC4626 vault) | `0x4f93Df7Bc0421C9401fD3099cCE4AfE7678B0c63` | 1 | 0/1 | 1 | 1 |  |
| 2118 | TwyneIncrementalReview | Ethereum | Twyne.teleport | `0x2035edE49c559C3CfF77FC8Ea5716C90AB07EfE4` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 2119 | UMA DVM 2.0 | Ethereum | VotingV2 (DVM request/reward) | `0x004395edb43EFca9885CEdad51EC9fAf93Bd34ac` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/uma-dvm-2-0-audit |
| 2120 | USSD - Autonomous Secure Dollar | Ethereum | USSD | `0x97D87327D8F168b0Ba317fd8B210d2B087f4b851` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/82 |
| 2121 | UXD | Solana | UXD Solana program (rebalance) | `UXPhBoR3qG4UCiGNJfV7MqhHyFqKN68g45GoYvAeL2M` | 1 | 0/1 | 0 | 1 |  |
| 2122 | UXD Protocol | Optimism | PerpDepository.getPositionValue | `0x2418A25e037419c8B0C616E6Fc7f995990BbfEB4` | 1 | 0/1 | 0 | 1 |  |
| 2123 | Umami | Arbitrum | Umami gmUSDC vault (VaultFees) | `0x959f3807f0Aa7921E18c78B00B2819ba91E52FeF` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 2124 | Umami | Arbitrum | Umami gmUSDC vault | `0x959f3807f0Aa7921E18c78B00B2819ba91E52FeF` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 2125 | Umami DAO | Arbitrum | MarinateAutoCompounder.convertRewardToke | `0x1922c36f3bc762ca300b4a46bb2102f84b1684ab` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 2126 | Umami DAO | Arbitrum | gmUSDC vault | `0x959f3807f0Aa7921E18c78B00B2819ba91E52FeF` | 1 | 0/1 | 0 | 1 | https://2316168122-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 2127 | Umami Finance | Arbitrum | cmUMAMI vault | `0x1922C36F3bc762Ca300b4a46bB2102F84B1684aB` | 1 | 0/1 | 0 | 1 | https://2316168122-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 2128 | Umami Finance GLP Vaults | Arbitrum | Umami GLP vault (first depositor) | `0x2e2153fd13459eba1f277ab9acd624f045d676ce` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 2129 | Umami GLP Vaults Report 2 of 2 | Arbitrum | AssetVault (gmUSDC) | `0x959f3807f0Aa7921E18c78B00B2819ba91E52FeF` | 1 | 0/1 | 0 | 1 | https://2316168122-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 2130 | Umami GLP Vaults Report 2 of 2 | Arbitrum | AssetVaults | `0x959f3807f0Aa7921E18c78B00B2819ba91E52FeF` | 1 | 0/1 | 0 | 1 | https://2316168122-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 2131 | Union Finance | Ethereum | uToken (UERC20) | `0x954F20DF58347b71bbC10c94827bE9EbC8706887` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/445 |
| 2132 | Uniswap V3 Core | Ethereum | UniswapV3Factory / UniswapV3Pool | `0x1F98431c8aD98523631AE4a59f267346ea31F984` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 2133 | Uniswap v4 Periphery and Universal Router | Ethereum | PositionManager / SlippageCheck | `0xbd216513d74c8cf14cf4747e6aaa6420ff64ee9e` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/uniswap-v4-periphery-and-universal-router-audi |
| 2134 | Unitas | BNB Chain | USDu stablecoin (BSC) | `0xea953ea6634d55dac6697c436b1e81a679db5882` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/73 |
| 2135 | Unitas Protocol | BNB Chain | USDu token (BSC) | `0xea953ea6634d55dac6697c436b1e81a679db5882` | 1 | 0/1 | 1 | 1 |  |
| 2136 | Unlock Protocol contest | Ethereum | Unlock (core) freeTrial / cancelAndRefun | `0xe79B93f8E22676774F2A8dAd469175ebd00029FA` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2021-11-unlock-findings/blob/2d2391bab788cd8432413 |
| 2137 | Unlock Protocol contest | Ethereum | MixinTransfer.transferFrom | `0xe79B93f8E22676774F2A8dAd469175ebd00029FA` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-11-unlock-findings/blob/2d2391bab788cd8432413 |
| 2138 | Usual Money | Ethereum | ClassicalOracle | `0xb97e163cE6A8296F36112b042891CFe1E23C35BF` | 1 | 0/1 | 0 | 0 | https://github.com/bailsec/BailSec/blob/7c2a162e5452082f79f57904ba1c63c0114d25c6 |
| 2139 | VII Finance | Unichain | ERC721WrapperBase.getSqrtRatioX96 | `0x7777655b9474D2f3F27EE44F3FD1343e33ce2777` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_vii_finance_jan2026.pdf |
| 2140 | VII Finance | Unichain | ERC4626VaultWrapperFactory.createERC4626 | `0x7777655b9474D2f3F27EE44F3FD1343e33ce2777` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_vii_finance_jan2026.pdf |
| 2141 | VMEX Finance | Optimism | Curve oracle reentrancy | `0x60F015F66F3647168831d31C7048ca95bb4FeaF9` | 1 | 0/1 | 0 | 1 | https://1688608737-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 2142 | VMEX Finance | Optimism | setIncentivesController() | `0x60F015F66F3647168831d31C7048ca95bb4FeaF9` | 1 | 0/1 | 0 | 1 | https://1688608737-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 2143 | VMEX Finance | Optimism | user validation | `0x60F015F66F3647168831d31C7048ca95bb4FeaF9` | 1 | 0/1 | 0 | 1 | https://1688608737-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 2144 | VMEX Finance | Optimism | Balancer LP oracle | `0x60F015F66F3647168831d31C7048ca95bb4FeaF9` | 1 | 0/1 | 0 | 1 | https://1688608737-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/sp |
| 2145 | VUSD Stablecoin | Ethereum | VUSD stablecoin / mint-redeem | `0x0BFFDD787C83235f6F0afa0Faed42061a4619B7a` | 1 | 0/1 | 0 | 1 |  |
| 2146 | Vader Protocol contest | Ethereum | USDV | `0xea3Fb6f331735252E7Bfb0b24b3B761301293DBe` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-12-vader-findings/blob/651921f04e49bd7ffe77f9 |
| 2147 | Valas Finance | BNB Chain | VALAS token | `0xB1EbdD56729940089Ecc3aD0BBEEB12b6842ea6F` | 1 | 0/1 | 1 | 1 | https://github.com/valas-finance/valas-protocol/blob/5ae95d336ec8883074206799a69 |
| 2148 | Vallarok | Ethereum | RunaAGI.FCFSMint(salt,msgHash,signature) | `0x9d21650745B593A488f8F0D84ADe822889221AB7` | 1 | 0/1 | 0 | 1 | https://github.com/shieldify-security/audits-portfolio/blob/a1e130f5a286cbc3ede4 |
| 2149 | Vana | Vana | TeePoolImplementation | `0x51f66FF950c1A91a537DFa1a18aB4d57bc4afa40` | 1 | 0/1 | 1 | 1 |  |
| 2150 | Vaultka 30th | Arbitrum | Water | `0x6df0018b0449bB4468BfAE8507E13021a7aa0583` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 2151 | Vaultka July25th | Arbitrum | Vaultka Vault (liquidatePosition) | `0x0081772FD29E4838372CbcCdD020f53954f5ECDE` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 2152 | Velar Artha PerpDEX | Stacks | Velar AMM core (Stacks) | `SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.univ2-core` | 1 | 0/1 | 0 | 1 |  |
| 2153 | Velocore Aug14 | zkSync Era | Velocore V1 factory | `0xF5719b1Ea3C9bF6491E22C49379E31060d0FbFc1` | 1 | 0/1 | 1 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 2154 | Velodrome | Optimism | VotingEscrow | `0x9c7305eb78a432ced5C4D14Cac27E8Ed569A2e26` | 1 | 0/1 | 0 | 1 |  |
| 2155 | Velodrome Finance | Optimism | VotingEscrow | `0xFAf8FD17D9840595845582fCB047DF13f006787d` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/Velodrome-Spearbit-Security-Review.pdf |
| 2156 | Velodrome Finance | Optimism | VotingEscrow | `0x9c7305eb78a432ced5C4D14Cac27E8Ed569A2e26` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-05-velodrome-findings/blob/590e5dbbf38318246f |
| 2157 | Velodrome Finance | Optimism | CLPool (implementation) | `0x11B234946F28A3905710922138C65FBbe7496b4C` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/Velodrome-Spearbit-Security-Review-Nov23.pdf |
| 2158 | Velvet Capital | BNB Chain | Velvet Capital core proxy (DepositBatch) | `0x0bb0c08fd9eeaf190064f4c66f11d18182961f77` | 1 | 0/1 | 1 | 1 | https://github.com/hats-finance/Velvet-Capital-0x0bb0c08fd9eeaf190064f4c66f11d18 |
| 2159 | Venus Prime | BNB Chain | Prime (score update) | `0x059EabA8676b03e4e8f009eFb7F587C28450F50f` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-09-venus-findings/blob/090fc6fd021a2102062a56 |
| 2160 | Venus Prime | BNB Chain | PrimeV2 (proxy) | `0x059EabA8676b03e4e8f009eFb7F587C28450F50f` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-09-venus-findings/blob/090fc6fd021a2102062a56 |
| 2161 | Vertex | Arbitrum | OffchainExchange.swapAmm / Vertex AMM | `0x95146881b86b3ee99e63705ec87afe29fcc044d9` | 1 | 0/1 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 2162 | Vesper Pools | Ethereum | VesperPool | `0xF36aF4dEAb51362Fe9f720FDf507E54a161F1F98` | 1 | 0/1 | 0 | 1 | https://github.com/coinspect/publications/blob/01b04f1f4a2e2c4d7e228b967fedb8991 |
| 2163 | Vesu Collaborative 1765410223 | Starknet | Migrate | `0x02c4399cfb357f836303d16e8173e4de71b4ba78d97121211357a6d73b9f9213` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2164 | Vesu V2 | Starknet | Vesu V2 Pool (claim fees) | `0x0451fe483d5921a2919ddd81d0de6696669bccdacd859f72a4fba7656b97c3b5` | 1 | 0/1 | 1 | 1 |  |
| 2165 | Vibe | Ethereum | VibeERC721 | `0x9F53A09524bb782C23Ec352B20688820F270d28d` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 2166 | Virtuals Protocol Staking | Base | Creator vault | `0xdAd686299FB562f89e55DA05F1D96FaBEb2A2E32` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 2167 | Volo | Sui | Volo Vault (share accounting) | `0xcd86f77503a755c48fe6c87e1b8e9a137ec0c1bf37aac8878b6083262b27fefa` | 1 | 0/1 | 0 | 1 | https://osec.io/reports/ca43cbdb-1d2b-43fc-8009-6279363d1779 |
| 2168 | Wildcat Protocol | Ethereum | WildcatArchController | `0xfEB516d9D946dD487A9346F6fee11f40C6945eE4` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2023-10-wildcat-findings/blob/0d8afef82271eb3a4042 |
| 2169 | Wildcat Protocol | Ethereum | WildcatMarket (sanctions path) | `0x437e0551892C2C9b06d3fFd248fe60572e08CD1A` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2023-10-wildcat-findings/blob/0d8afef82271eb3a4042 |
| 2170 | Wise Lending | Ethereum | PowerFarm nftID check | `0x84524bAa1951247b3A2617A843e6eCe915Bb9674` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-02-wise-lending-findings/blob/eb30b162e6bee0a |
| 2171 | Wise Lending | Ethereum | WiseLending.receive() -> withdrawExactAm | `0x84524bAa1951247b3A2617A843e6eCe915Bb9674` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2024-02-wise-lending-findings/blob/eb30b162e6bee0a |
| 2172 | Wise Lending | Ethereum | liquidate() | `0x84524bAa1951247b3A2617A843e6eCe915Bb9674` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2024-02-wise-lending-findings/blob/eb30b162e6bee0a |
| 2173 | Wise Lending | Ethereum | WiseLending.receive() -> _sendValue() | `0x84524bAa1951247b3A2617A843e6eCe915Bb9674` | 1 | 0/1 | 1 | 1 |  |
| 2174 | Wise Lending | Ethereum | repay/withdraw accounting | `0x84524bAa1951247b3A2617A843e6eCe915Bb9674` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2024-02-wise-lending-findings/blob/eb30b162e6bee0a |
| 2175 | Wise Lending | Ethereum | MainHelper._removePositionData via WiseL | `0x84524bAa1951247b3A2617A843e6eCe915Bb9674` | 1 | 0/1 | 1 | 1 |  |
| 2176 | WooFi | Arbitrum | WooPPV2 (main swap pool) | `0x5520385bFcf07Ec87C4c53A7d8d65595Dff69FA4` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2177 | WooFi | Arbitrum | WooPPV2 / WooRouterV2 swap | `0x5520385bFcf07Ec87C4c53A7d8d65595Dff69FA4` | 1 | 0/1 | 1 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2178 | XDEFI contest | Ethereum | XDEFIDistribution._safeMint / lock | `0x1dfd9029d89f87c8c63ed8ef2be1b5393b2348ef` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2022-01-xdefi-findings/blob/fb8f7b0b23b3e8b1f8de0c |
| 2179 | XIO Network - February 27, 2021 | Ethereum | XIO token (Blockzero Labs) | `0x0f7F961648aE6Db43C75663aC7E5414Eb79b5704` | 1 | 0/1 | 0 | 1 | https://github.com/solidified-platform/audits/blob/5ff5fa144b32ad65b649f032465e4 |
| 2180 | Y2K Finance | Arbitrum | RolloverVault (ownerToRollOverQueueIndex | `0x984e0eb8fb687afa53fc8b33e12e04967560e092` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/57 |
| 2181 | YG | Base | MORE Vaults Composer / vault diamond | `0x8D8BE034eCfD018D67F9a1A25E27f99f52CBdFC1` | 1 | 0/1 | 0 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 2182 | YIELD | Ethereum | Cauldron | `0xc88191F8cb8e6D4a668B047c1C8503432c3Ca867` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-05-yield-findings/blob/cf51122ae6ad62cb6eb70c |
| 2183 | YIELD | Ethereum | Ladle | `0x6cB18fF2A33e981D1e38A663Ca056c0a5265066A` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 2184 | YIELD | Ethereum | Ladle (AccessControl) | `0x6cB18fF2A33e981D1e38A663Ca056c0a5265066A` | 1 | 0/1 | 0 | 0 | https://github.com/code-423n4/2021-05-yield-findings/blob/cf51122ae6ad62cb6eb70c |
| 2185 | Yala Stablecoin | Ethereum | PSM (peg stability module, minimal proxy | `0x0b4e03ECb66be6774c216EA9ecA3663A85eE41fd` | 1 | 0/1 | 0 | 1 | https://github.com/zenith-security/reports/blob/bf794d06dd31f476a65fe0f27d5221d9 |
| 2186 | Yearn yBOLD | Ethereum | yBOLD vault / strategy | `0x9F4330700a36B29952869fac9b33f45EEdd8A3d8` | 1 | 0/1 | 0 | 1 | https://audits.sherlock.xyz/contests/977 |
| 2187 | Yeet Cup | Berachain | YEET Token | `0x08A38Caa631DE329FF2DAD1656CE789F31AF3142` | 1 | 0/1 | 0 | 1 | https://github.com/shieldify-security/audits-portfolio-md/blob/cb986f228e75a5753 |
| 2188 | Yield Protocol | Ethereum | Ladle | `0x6cB18fF2A33e981D1e38A663Ca056c0a5265066A` | 1 | 0/1 | 0 | 1 |  |
| 2189 | YieldBasisDAO UpdateSecurityReview | Ethereum | LiquidityGauge | `0xd829456FD63Ada7DE0657714A3A7A26DE403E3D8` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 2190 | YieldNest | Ethereum | ynETH / processAccounting | `0x09db87A538BD693E9d08544577d5cCfAA6373A48` | 1 | 0/1 | 0 | 1 | https://github.com/ComposableSecurity/.github/blob/144b868957d165fa3f5210ae80928 |
| 2191 | YieldNest May7th | Ethereum | ynETH | `0x09db87A538BD693E9d08544577d5cCfAA6373A48` | 1 | 0/1 | 0 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 2192 | ZKSwap | Ethereum | ZKS token | `0xe4815AE53B124E7263F08DcdbBB757d41Ed658c6` | 1 | 0/1 | 0 | 1 | https://github.com/abdk-consulting/audits/blob/57af593b14bb3701cf659937b1b7b6483 |
| 2193 | ZeroLend | Linea | ZeroLend Pool proxy (Linea) | `0x2f9bB73a8e98793e26Cb2F6C4ad037BDf1C6B269` | 1 | 0/1 | 0 | 1 |  |
| 2194 | ZetaChain | ZetaChain | SystemContract | `0x91d18e54DAf4F677cB28167158d6dd21F6aB3921` | 1 | 0/1 | 0 | 1 |  |
| 2195 | ZetaChain Cross-Chain |  | ZetaChain EVM precompile call (e.g. dele | `ZetaChain` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/857 |
| 2196 | Zivoe | Ethereum | ZivoeITO | `0xE590233c22E81A79a1768aB8c8597b7a55C52Aba` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2197 | Zivoe - Core Contracts | Ethereum | ZVL token (access-control transfer) | `0xe412D46a0fBD567332b7689cFFfE1F8A4f19A9d2` | 1 | 0/1 | 1 | 1 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 2198 | Zivoe - Core Contracts | Ethereum | ZVE token (audited as ZVL) | `0xe412D46a0fBD567332b7689cFFfE1F8A4f19A9d2` | 1 | 0/1 | 1 | 1 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 2199 | Zora | Ethereum | Zora Media | `0xabEFBc9fD2F806065b4f3C237d4b59D9A97Bcac7` | 1 | 0/1 | 0 | 1 |  |
| 2200 | Zunami Protocol | Ethereum | BaseStakingRewardDistributor (_updateDis | `0x45af4F12B46682B3958B297bAcebde2cE2E795c3` | 1 | 0/1 | 0 | 1 | https://github.com/oxor-io/public_audits/blob/06624b6efe70d98702baccef5208ec57db |
| 2201 | ajna update | Ethereum | ERC20PoolFactory (deploys Pool contracts | `0xe6F4d9711121e5304b30aC2Aae57E3b085ad3c4d` | 1 | 0/1 | 0 | 1 |  |
| 2202 | anystake | Ethereum | AnyStake | `0x95EF77772BdAEF25B56ec5f210e02BdaAc40D144` | 1 | 0/1 | 0 | 1 |  |
| 2203 | api3-api | Ethereum | Api3Pool (TimelockUtils) | `0x6dd655f10d4b9E242aE186D9050B68F725c76d76` | 1 | 0/1 | 1 | 1 |  |
| 2204 | arbitrum (Arbitrum Security Council Elections) | Arbitrum | SecurityCouncilNomineeElectionGovernor / | `0x8a1cDA8dee421cD06023470608605934c16A05a0` | 1 | 0/1 | 0 | 1 |  |
| 2205 | arrakis valantis sot audit | Ethereum | ArrakisMetaVaultPrivate | `0x273a7BF708Fcc7c8c992e0749aaF961aE8AF16f0` | 1 | 0/1 | 0 | 1 |  |
| 2206 | audited Trader Joe | Avalanche | BoostedMasterChefJoe.set | `0x4483f0b6e2F5486D06958C20f8C39A7aBe87bf8F` | 1 | 0/1 | 0 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 2207 | behodler | Ethereum | Behodler EYE token | `0x155ff1A85F440EE0A382eA949f24CE4E0b751c65` | 1 | 0/1 | 0 | 1 |  |
| 2208 | blex io 215a1fca | Arbitrum | BLEX perpetual core (report names no con | `0xf14cBC388176B75401c6666C08bE8bB0046cdb83` | 1 | 0/1 | 0 | 1 |  |
| 2209 | bold | Ethereum | RollupUserLogic / EdgeChallengeManagerLi | `0x5eF0D09d1E6204141B4d37530808eD19f60FBa35` | 1 | 0/1 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |
| 2210 | canto | Canto | BaseV1Router01.calculateFairReserves (Ba | `0xa252eEE9BDe830Ca4793F054B506587027825a8e` | 1 | 0/1 | 0 | 1 |  |
| 2211 | canto | Canto | BaseV1Router01.getUnderlyingPrice (BaseV | `0xa252eEE9BDe830Ca4793F054B506587027825a8e` | 1 | 0/1 | 1 | 1 |  |
| 2212 | chainbridge | Ethereum | ChainBridge | `0x8e683448F7d39e5e090BdBBE9e28E3334B32bF38` | 1 | 0/1 | 1 | 1 | https://diligence.consensys.io/audits/private/adash47d-chainbridge/chainbridge-a |
| 2213 | cork best efforts audit contest | Ethereum | CorkPoolManager (VaultPoolLib::redeem) | `0xccCCcCcCCccCfAE2Ee43F0E727A8c2969d74B9eC` | 1 | 0/1 | 1 | 1 |  |
| 2214 | cork best efforts audit contest | Ethereum | CorkPoolManager (PsmLib/VaultLib redeem) | `0xccCCcCcCCccCfAE2Ee43F0E727A8c2969d74B9eC` | 1 | 0/1 | 1 | 1 |  |
| 2215 | cork best efforts audit contest | Ethereum | CorkPoolManager / CorkAdapter (slippage  | `0xccCCcCcCCccCfAE2Ee43F0E727A8c2969d74B9eC` | 1 | 0/1 | 0 | 1 |  |
| 2216 | dForce sUSX | Ethereum | sUSX cross-chain mint path | `0x041D2c9250dc0cA2962BE94cF7c4D05abB1d5820` | 1 | 0/1 | 0 | 1 | https://github.com/mixbytes/audits_public/blob/3bbdea1996b26961a75a063badec305b2 |
| 2217 | dHEDGE | Optimism | VelodromeCLAssetGuard._assetValue/total | `0xcAD34b94fE25bDd4B972d01598abBFD1795A2d91` | 1 | 0/1 | 0 | 1 | https://github.com/sherlock-protocol/sherlock-reports/blob/10e76f5bd13701970c995 |
| 2218 | deq.fi- -may24 | Ethereum | Staked Avail (stAVAIL) | `0x3742f3fcc56b2d46c7b8ca77c23be60cd43ca80a` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2219 | dexe network | Ethereum | DEXE token | `0xde4EE8057785A7e8e800Db58F9784845A5C2Cbd6` | 1 | 0/1 | 0 | 1 |  |
| 2220 | dirol | Monad | Dirol AGR (Aggregator) | `0x646462f4d0168A94fE1884c8ae82148a3618A18d` | 1 | 0/1 | 0 | 1 |  |
| 2221 | dodo v3 | Ethereum | D3Vault (D3VaultLiquidation) | `0x49186E32fEd50fd6B5604A2618c7B0b03Cd41414` | 1 | 0/1 | 0 | 1 |  |
| 2222 | dodo v3 | Ethereum | D3Vault (D3VaultLiquidation / D3VaultFun | `0x49186E32fEd50fd6B5604A2618c7B0b03Cd41414` | 1 | 0/1 | 1 | 1 |  |
| 2223 | dodo v3 | Ethereum | D3Proxy.d3MMSwapCallBack | `0x411ec324598EF53b1E8663e335e9094464523e6B` | 1 | 0/1 | 1 | 1 |  |
| 2224 | eco protocol penetration test | Ethereum | IntentChainer V4 (Eco Portal) | `0x96f7DBa7E587f359a8f585C335fe510E4dC9bCC0` | 1 | 0/1 | 0 | 1 |  |
| 2225 | eigenlayer | Ethereum | EigenPodManager | `0x91E677b07F7AF907ec9a428aafA9fc14a0d3A338` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_eigenlayer_mar2025.pdf |
| 2226 | elara finance ceaf2e43 | Ethereum | PriceOracle | `0x0A3DA6265439b4585c942856d7Ee22B7b2C973F2` | 1 | 0/1 | 0 | 1 |  |
| 2227 | ethereum evm advancedblockchain | Ethereum | FORCE token (ForceDAO governance) | `0xea2E1F3179Bd34aE866829Fc106528632A213D55` | 1 | 0/1 | 0 | 1 |  |
| 2228 | ethereum-evm-balancer-v3-securityreview | Ethereum | Balancer V3 Vault (ERC4626 buffer) | `0xbA1333333333a1BA1108E8412f11850A5C319bA9` | 1 | 0/1 | 1 | 1 |  |
| 2229 | ethereum-evm-balancer-v3-securityreview | Ethereum | Balancer V3 Vault (pool init) | `0xbA1333333333a1BA1108E8412f11850A5C319bA9` | 1 | 0/1 | 0 | 1 |  |
| 2230 | ethos network financial contracts | Base | EthosVouch (vouch bonding curve) | `0xD89E6B7687f862dd6D24B3B2D4D0dec6A89A6fdd` | 1 | 0/1 | 0 | 1 |  |
| 2231 | ethos network financial contracts | Base | EthosVouch | `0xD89E6B7687f862dd6D24B3B2D4D0dec6A89A6fdd` | 1 | 0/1 | 1 | 1 |  |
| 2232 | f(x) Protocol | Ethereum | fxUSD token | `0x085780639CC2cACd35E474e71f4d000e2405d8f6` | 1 | 0/1 | 0 | 1 |  |
| 2233 | f(x) v2 | Ethereum | fxUSD (EIP-1967 proxy) | `0x085780639CC2cACd35E474e71f4d000e2405d8f6` | 1 | 0/1 | 0 | 1 | https://www.openzeppelin.com/news/fx-v2-audit |
| 2234 | fluidkey-earn-module | Base | FluidkeyEarnModule | `0x3BDb857AFe9b51d8916D80240d2ADe40D4d3f2f9` | 1 | 0/1 | 0 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 2235 | for Alien Base | Base | EpsilonRouter.cancelOrder | `0x303ca5c65AabCb1CE242DF93F478c41E0E4D2580` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2236 | for BasisOS | Base | BIOS token | `0x73Cb479f2ccf77BAd90BcDA91e3987358437240A` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2237 | for GLIF | Filecoin | GLIF InfinityPoolV2 | `0xe764Acf02D8B7c21d2B6A8f0a96C78541e0DC3fd` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2238 | for JuiceSwap | Citrea | JuiceSwap MintingHub | `0x372368ca530B4d55622c24E28F0347e26caDc64A` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2239 | for Kerne Protocol | Base | KerneVault | `0x8ccc56B5624e2FDB592F6609d81F4c3798e3292B` | 1 | 0/1 | 0 | 1 | https://github.com/kerne-protocol/contracts-public/blob/3dcc5f62d2c58bb3763b16a7 |
| 2240 | for KyberSwap | Ethereum | FairFlow UniswapV4KEMHook | `0x4440854B2d02C57A0Dc5c58b7A884562D875c0c4` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2241 | for SquadSwap | Ethereum | Pool manager / SquadswapFactory-created  | `0xaA33E51b9d45C7a8feeD7E40Dc2878b09970F180` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2242 | frax finance fraxfinance | Ethereum | FRAXStablecoin (FRAX core) | `0x853d955aCEf822Db058eb8505911ED77F175b99e` | 1 | 0/1 | 1 | 1 |  |
| 2243 | fungify- -june | Ethereum | Fungify NFT market (Comptroller) | `0xf9c70750bF615dE83fE7FF62D30C7faACD8f8Ba0` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2244 | galileo protocol | Ethereum | GalileoStaking | `0x0B4C3D5FFA70589917A9D68c899C607c8E606Ff8` | 1 | 0/1 | 1 | 1 |  |
| 2245 | ground zero | Ethereum | GroundZERO | `0x33613D7264e183579D3BEa0cE29432C75990d80d` | 1 | 0/1 | 0 | 1 |  |
| 2246 | hashlock-algem-2024-12-algem-liquid-farming-v3-4 | Astar | AlgemAdapter | `0x8e066de9a3B0ac5965e4361fDE2752c11509f4F2` | 1 | 0/1 | 1 | 1 |  |
| 2247 | hashlock-balanced-network-icon-foundation-2024-06-balanced-s | Icon | Balanced DEX (ICON) | `cxa0af3165c08318e988cb30993b3048335b94af6c` | 1 | 0/1 | 0 | 1 |  |
| 2248 | hashlock-eigenlayer-contest-2025-03-eigenlayer-cantina-compe | Ethereum | EigenPodManager | `0x91E677b07F7AF907ec9a428aafA9fc14a0d3A338` | 1 | 0/1 | 0 | 1 |  |
| 2249 | hashlock-eigenlayer-contest-2025-03-hashlock-competition-sub | Ethereum | DelegationManager (proxy) | `0x39053D51B77DC0d36036Fc1fCc8Cb819df8Ef37A` | 1 | 0/1 | 0 | 1 |  |
| 2250 | hashlock-flarebank-2025-07-flarebank-smart-contract-audit-re | Flare | Bank | `0x194726F6C2aE988f1Ab5e1C943c17e591a6f6059` | 1 | 0/1 | 1 | 1 |  |
| 2251 | hashlock-indx-2025-07-indx-smart-contract-audit-report | Base | index-v3 (claimTokens) | `0x871fbd1d0cbd80917d4f6fc5b1353d45b3ba68e4` | 1 | 0/1 | 0 | 1 |  |
| 2252 | hashlock-levva-2024-10-levva-main-smart-contracts-security-a | Ethereum | LevvaFarmingPool | `0xC4ca700A1966280e8821245a587a30Dc1EFc16Cb` | 1 | 0/1 | 1 | 1 |  |
| 2253 | hashlock-montage-token-2023-10-montage-token | Ethereum | Montage Token (_swapTokensForETH) | `0x06D6F0dd6703A1cfE16025DCc55F36f017887627` | 1 | 0/1 | 1 | 1 |  |
| 2254 | hashlock-vana-2024-12-vana-data-and-treasury-implementation- | Vana | TeePoolImplementation | `0x3c92fD91639b41f13338CE62f19131e7d19eaa0D` | 1 | 0/1 | 1 | 1 |  |
| 2255 | hashlock-zeus-exchange-2025-08-zeus-exchange-smart-contract- | Base | OrderBook | `0x6bfdBeA159B5783c3fFb79AaF02De33116f393a4` | 1 | 0/1 | 1 | 1 |  |
| 2256 | hashlock-zeus-exchange-2025-08-zeus-exchange-smart-contract- | Base | VaultPriceFeed | `0x73FDe7878Acff42bf7f43649d91604fa67586F83` | 1 | 0/1 | 0 | 1 |  |
| 2257 | hegic-summary | Ethereum | HEGIC token | `0x584bC13c7D411c00c01A62e8019472dE68768430` | 1 | 0/1 | 0 | 1 |  |
| 2258 | holograph | Polygon | HolographOperator | `0x3a403792184aA24ec56bF7D24aD42C17CA2e2dbE` | 1 | 0/1 | 0 | 1 |  |
| 2259 | holonym-zk- -may | Optimism | Holonym Hub | `0x87b6e03b0D57771940D7cC9E92531B6217364B3E` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2260 | ichi ichi | Ethereum | OneTokenFactory / oneToken oracle | `0xD0092632B9Ac5A7856664eeC1abb6E3403a6A36a` | 1 | 0/1 | 0 | 1 |  |
| 2261 | ichi ichi | Ethereum | OneTokenFactory / oneToken mintMaster | `0xD0092632B9Ac5A7856664eeC1abb6E3403a6A36a` | 1 | 0/1 | 0 | 1 |  |
| 2262 | illuvium yield farming rewards | Ethereum | ILV token | `0x767FE9EDC9E0dF98E07454847909b5E959D7ca0E` | 1 | 0/1 | 0 | 1 |  |
| 2263 | imf international meme fund 2024 06 imf smart contract audit | Ethereum | sbIMF | `0x3215c358b7a70c09E0a98827F744d107095e14E4` | 1 | 0/1 | 0 | 1 |  |
| 2264 | infiniFi | Ethereum | requestRedeem() (ERC7540 vault) | `0x3f04b65Ddbd87f9CE0A2e7Eb24d80e7fb87625b5` | 1 | 0/1 | 1 | 1 | https://github.com/threesigmaxyz/publications/blob/2c8915e75b72f45bb3bf38f7805cd |
| 2265 | infiniFi | Ethereum | SwapFarm.convertToAssets() | `0x3f04b65Ddbd87f9CE0A2e7Eb24d80e7fb87625b5` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_infinifi_april2025.pdf |
| 2266 | infiniFi | Ethereum | MintController._createPosition() | `0x3f04b65Ddbd87f9CE0A2e7Eb24d80e7fb87625b5` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_infinifi_april2025.pdf |
| 2267 | infiniFi | Ethereum | unwinding epoch | `0x3f04b65Ddbd87f9CE0A2e7Eb24d80e7fb87625b5` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_competition_infinifi_april2025.pdf |
| 2268 | infiniFi | Ethereum | accrue / unwind | `0x3f04b65Ddbd87f9CE0A2e7Eb24d80e7fb87625b5` | 1 | 0/1 | 1 | 1 | https://cdn.cantina.xyz/reports/InfiniFi-Spearbit-Security-Review-March-2025.pdf |
| 2269 | infiniFi PR 224 | Ethereum | InfiniFiCore | `0xF6d48735EcCf12bDC1DF2674b1ce3fcb3bD25490` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_infinifi_pr224_nov2025.pdf |
| 2270 | infinigold / infinigold | Ethereum | PMGT token (transferFrom) | `0xAFFCDd96531bCd66faED95FC61e443D08F79eFEf` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 2271 | ipor-protocol | Ethereum | IporSwapLogic.calculateSwapUnwindValue | `0x695264D984A5E45C2d89f261C8668d6C1F7D214c` | 1 | 0/1 | 0 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 2272 | jonesdao-jgm | Arbitrum | JGM oracle (stale price) | `0xBEF7a31efabc9F9e80f9CcD4f03CE2D7EcbfDaf9` | 1 | 0/1 | 0 | 1 | https://github.com/GuardianAudits/Audits/blob/36fcc39d51fd84a6ec2c72b9c9fda8f8b6 |
| 2273 | kelp | Ethereum | LRTDepositPool | `0x036676389e48133B63a802f8635AD39E752D375D` | 1 | 0/1 | 0 | 1 |  |
| 2274 | kelp | Ethereum | LRTDepositPool / rsETH mint | `0x036676389e48133B63a802f8635AD39E752D375D` | 1 | 0/1 | 0 | 1 |  |
| 2275 | kpk Onchain Investment Vehicles | Ethereum | KPK token (identity anchor) | `0xbF3F63D8AC133B16d7D50C015036b33219Dd8D23` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/cantina_kpk_oct2025.pdf |
| 2276 | kuma | Ethereum | KIBToken | `0x932c930104F39e475965f9FBfA345C1C4F537E5f` | 1 | 0/1 | 0 | 1 |  |
| 2277 | limit-order-settlement | Ethereum | Settlement (1inch Fusion settlement exte | `0x2Ad5004c60e16E54d5007C80CE329Adde5B51Ef5` | 1 | 0/1 | 0 | 1 | https://www.iosiro.com/audits/1inch-limit-order-settlements-smart-contract-audit |
| 2278 | linqai | Ethereum | LNQ token (ERC-20) | `0xD4F4D0a10BcaE123bB6655E8Fe93a30d01eEbD04` | 1 | 0/1 | 0 | 1 |  |
| 2279 | lockon 2025 09 lockon smart contract | Polygon | IndexStaking | `0x24FF9D1f1E9948645786B8b8EAE7a3F430b62093` | 1 | 0/1 | 0 | 1 |  |
| 2280 | ltv v0 | Ethereum | LTV | `0x0cE0Bd78fB017E5d83b8cAeb659e3286AFD25847` | 1 | 0/1 | 0 | 1 | https://github.com/ltvprotocol/ltv_v0/blob/009fc84517a6f6fe7dbf9dc378736179d7a22 |
| 2281 | lyra | Optimism | LiquidityPool | `0xb8e90fD247700dE65450Aacd4A47B2948Dc59FC1` | 1 | 0/1 | 1 | 1 |  |
| 2282 | magicsea-the-native-dex-on-the-iotaevm | IOTA EVM | MagicSeaFactory | `0x349aaAc3a500014981CBA11b64C76c66a6c1e8D0` | 1 | 0/1 | 0 | 1 |  |
| 2283 | magpie eigenpie v1.4 | Ethereum | VlStreamRewarder / EigenpieStaking | `0x4eF7F34Bb1CD7d1E82181274A0896e2CCaC774bE` | 1 | 0/1 | 1 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 2284 | mantra dex | MANTRA Chain | Pool Manager - validate_fees_are_paid (c | `mantra1466nf3zuxpya8q9emxukd7vftaf6h4psr0a07srl5zw74zh84yjqagspfm` | 1 | 0/1 | 0 | 0 |  |
| 2285 | mantra dex | MANTRA Chain | Pool Manager - stableswap provide_liquid | `mantra1466nf3zuxpya8q9emxukd7vftaf6h4psr0a07srl5zw74zh84yjqagspfm` | 1 | 0/1 | 0 | 1 |  |
| 2286 | mantra dex | MANTRA Chain | Pool Manager - stableswap share minting | `mantra1466nf3zuxpya8q9emxukd7vftaf6h4psr0a07srl5zw74zh84yjqagspfm` | 1 | 0/1 | 0 | 1 |  |
| 2287 | mantra dex | MANTRA | MANTRA DEX Pool Manager (CosmWasm, code  | `mantra1466nf3zuxpya8q9emxukd7vftaf6h4psr0a07srl5zw74zh84yjqagspfm` | 1 | 0/1 | 0 | 1 |  |
| 2288 | merit circle merit | Ethereum | TimeLockNonTransferablePool (staking/rew | `0x5c76aD4764A4607cD57644faA937A8cA16729e39` | 1 | 0/1 | 1 | 1 |  |
| 2289 | mstable | Ethereum | SavingsContract | `0x30647a72Dc82d7Fbb1123EA74716aB8A317Eac19` | 1 | 0/1 | 0 | 1 | https://diligence.consensys.io/audits/2020/07/mstable-1.1/mstable-audit-2020-07. |
| 2290 | music protocol token staking and dao 3cb260d9 | Base | Record Nexus (RECORD token, proxy; audit | `0xe642657e4f43e6dcf0bd73ef24008394574dee28` | 1 | 0/1 | 0 | 1 |  |
| 2291 | napier-v2-audit-competition | Ethereum | Napier YT / pool reward accounting | `0x5a2d321eD5C525e52A3b8d295c6D097a3c78B821` | 1 | 0/1 | 0 | 1 |  |
| 2292 | neuralai | Ethereum | NeuralStaking | `0x0a1e8EC04064E895fFC46e97d60001BdcDAbeaac` | 1 | 0/1 | 0 | 1 |  |
| 2293 | noon capital 2025 11 noon capital updates smart contracts | Ethereum | stakeNOON | `0x5f9ee665830BE17b2073a9800Eb7bbbe51b471D7` | 1 | 0/1 | 0 | 1 |  |
| 2294 | notional update 5 | Ethereum | Notional V3 (nProxy / lending router mod | `0x6e7058c91F85E0F6db4fc9da2CA41241f5e4263f` | 1 | 0/1 | 0 | 1 |  |
| 2295 | oku s new order types contract contest | Optimism | AutomationMaster | `0xCaE450Ba6e9d6e9A5A719C1B4b3d2033C3047B3e` | 1 | 0/1 | 1 | 1 |  |
| 2296 | oku s new order types contract contest | Optimism | StopLimit | `0xfdcFdd8267F7054facF9eA2aAD538d74da4B65c8` | 1 | 0/1 | 1 | 1 |  |
| 2297 | oku s new order types contract contest | Optimism | OracleLess | `0x5ce1E92eBB96deee97F4a225DF97EDadF5fb76e9` | 1 | 0/1 | 1 | 1 |  |
| 2298 | omisego morevp | Ethereum | PlasmaFramework (RLPReader library used  | `0x0D4C1222f5e839a911e2053860e45F18921D72ac` | 1 | 0/1 | 0 | 1 |  |
| 2299 | omnipair | Solana | Omnipair program (lp_mint.key()) | `omnixgS8fnqHfCcTGKWj6JtKjzpJZ1Y5y9pyFkQDkYE` | 1 | 0/1 | 0 | 1 | https://github.com/omnipair/omnipair-rs/blob/84a8ef7a2a3a81e750435b86d7191bf4341 |
| 2300 | opendollar | Arbitrum | AccountingEngine (surplus auction house) | `0xa83c0f1e9eD8E383919Dde0fC90744ae370EB7B3` | 1 | 0/1 | 0 | 1 |  |
| 2301 | openq | Ethereum | OpenQ token (OPQ) | `0x56CeFC40F27978fe2fFf2b851A3b1e63c2FDf09f` | 1 | 0/1 | 0 | 1 |  |
| 2302 | openzk 2025 02 openzk skymoneyvault smart contract | Ethereum | ozUSD Vault | `0x3B5cc7D992F8ED1b4E1f9F660984adCd61fC1aCa` | 1 | 0/1 | 0 | 0 |  |
| 2303 | optimism | Ethereum | PreimageOracle (LPP finalization) | `0x1E1d73536A081Ef2F355d29794547a9770Aeb1E0` | 1 | 0/1 | 0 | 1 |  |
| 2304 | orderly solana vault | Solana | Solana-Vault program | `ErBmAD61mGFKvrFNaTJuxoPwqrS8GgtwtqJTJVjFWx9Q` | 1 | 0/1 | 0 | 1 |  |
| 2305 | paladin | Ethereum | QuestBoardV2 (drop accounting) | `0x653D8f14292A1C5239d6183b333De1F2e8669310` | 1 | 0/1 | 0 | 1 | https://cdn.cantina.xyz/reports/Paladin-Spearbit-Security-Review.pdf |
| 2306 | paladin | Ethereum | QuestBoardV2 (dropPerSecond) | `0x653D8f14292A1C5239d6183b333De1F2e8669310` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2022-03-paladin-findings/blob/0d466ddb82076907eefc |
| 2307 | pancakeswap | BNB Chain | Infinity Vault (settle) | `0x238a358808379702088667322f80aC48bAd5e6c4` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2308 | pashov-team-2024-01-24-kekotron-security-review | Ethereum | KekotronRouterV2 | `0xd270008604001e5B00000040100000047e9F00f2` | 1 | 0/1 | 0 | 1 |  |
| 2309 | pashov-team-2024-02-25-hytopia-security-review | Polygon | HYTOPIA (TOPIA) token | `0x1CAa400b9D0A7ED776b473908ab5D1012901F4E1` | 1 | 0/1 | 0 | 1 |  |
| 2310 | pashov-team-2024-03-25-fyde-security-review | Ethereum | Fyde DepositEscrow | `0x63ec950633Eb85797477166084AD0a7121910470` | 1 | 0/1 | 0 | 1 |  |
| 2311 | pashov-team-2024-03-29-forgottenplayland-security- | Ethereum | Forgotten Playland (FP) token | `0xeeee2a2e650697d2a8e8bc990c2f3d04203be06f` | 1 | 0/1 | 0 | 1 |  |
| 2312 | pashov-team-2024-05-08-reyanetwork-security-review-april | Reya Network | Core (account merging) | `0xA763B6a5E09378434406C003daE6487FbbDc1a80` | 1 | 0/1 | 0 | 1 |  |
| 2313 | pashov-team-2024-07-18-radiant-security-review-june | Arbitrum | Radiant LendingPool (Arbitrum) | `0xE23B4AE3624fB6f7cDEF29bC8EAD912f1Ede6886` | 1 | 0/1 | 0 | 1 |  |
| 2314 | pashov-team-2024-07-22-fyde-security-review-may | Ethereum | FYDE token proxy | `0x8a462E6a0051d006E33152FBEaDFB9A14198DE30` | 1 | 0/1 | 0 | 1 |  |
| 2315 | pashov-team-2024-07-31-honeyjar-security-review | Berachain | Honey Jar Gen 4 (NFT collection) | `0xdB602aB4D6bD71C8d11542A9C8c936877a9A4f45` | 1 | 0/1 | 0 | 1 |  |
| 2316 | pashov-team-2024-08-08-ionprotocol-security-review-july | Base | Ion LRT Vault (bridge mint path) | `0x0000000000895f1D9e978788C6367d47127dd218` | 1 | 0/1 | 0 | 1 |  |
| 2317 | pashov-team-2024-08-08-nabla-security-review | Arbitrum | NablaBackstopPool | `0x337B03C2a7482c6eb29d8047eA073119dc68a29A` | 1 | 0/1 | 0 | 1 |  |
| 2318 | pashov-team-2024-08-15-layerzerozroclaim-security- | Ethereum | LayerZero Airdrop Claim | `0xC28C2b2F5A9B2aF1ad5878E5b1AF5F9bAEa2F971` | 1 | 0/1 | 0 | 1 |  |
| 2319 | pashov-team-2024-09-09-gainsnetwork-security-review-february | Arbitrum | GNSMultiCollatDiamond (trading facet) | `0xFF162c694eAA571f685030649814282eA457f169` | 1 | 0/1 | 0 | 1 |  |
| 2320 | pashov-team-2024-10-14-sofamon-security-review-aug | Ethereum | Sofamon Seed (ERC-721) | `0xD7b26749CcF89EDD87DDd427d69406B66d83D913` | 1 | 0/1 | 0 | 1 |  |
| 2321 | pashov-team-2024-10-14-sofamon-security-review-august | Ethereum | SOFAMON (ERC-1155 proxy) | `0xd3165b63D4A8d814669ab36767dEFcB8363A5F19` | 1 | 0/1 | 0 | 1 |  |
| 2322 | pashov-team-2024-11-16-peapods-security-review | Ethereum | LeverageManager | `0x4e6EF371C9CDDE8C3e6716AffEEBaD14C8c62D0B` | 1 | 0/1 | 1 | 1 |  |
| 2323 | pashov-team-2024-12-12-g8keep-security-review | Base | G8Keep pool (migration logic) | `0x3C0B43867Cd04fEdfD6a95497e5ea7e3aFF8cCaE` | 1 | 0/1 | 0 | 1 |  |
| 2324 | pashov-team-2024-12-30-gammaswap-security-review | Arbitrum | GammaPoolFactory / GammaPool | `0xe048ccE443E787c5b6FA886236De2981D54E244f` | 1 | 0/1 | 0 | 1 |  |
| 2325 | pashov-team-2025-01-21-ostium-security-review | Arbitrum | OstiumTrading | `0x6D0bA1f9996DBD8885827e1b2e8f6593e7702411` | 1 | 0/1 | 0 | 1 |  |
| 2326 | pashov-team-2025-04-30-blueberry-security-review | Ethereum | BlueberryBank proxy | `0x9b06eA9Fbc912845DF1302FE1641BEF9639009F7` | 1 | 0/1 | 0 | 1 |  |
| 2327 | pashov-team-2025-05-16-blueberry-security-review | Hyperliquid | Blueberry Router | `0x647a4D7F1F20Cf237C27b39fB6924f5a7691BB4b` | 1 | 0/1 | 0 | 1 |  |
| 2328 | pashov-team-2025-06-12-kittenswap-security-review | HyperEVM | KittenSwap core | `0x618275f8efe54c2afa87bfb9f210a52f0ff89364` | 1 | 0/1 | 1 | 1 |  |
| 2329 | pashov-team-2025-07-31-kittenswap-security-review | Hyperliquid | Kittenswap core deployment | `0x618275f8efe54c2afa87bfb9f210a52f0ff89364` | 1 | 0/1 | 0 | 1 |  |
| 2330 | perpetual dex hmxv2 | Arbitrum | RemoteHMX token | `0x83d6c8c06ac276465e4c92e7ac8c23740f435140` | 1 | 0/1 | 0 | 1 |  |
| 2331 | pheasant network 0b120935 | Ethereum | PheasantNetworkBridgeChild proxy (Ethere | `0x20A41749545eB0C6266838257aDeA7b86d5369Ac` | 1 | 0/1 | 0 | 1 |  |
| 2332 | polynomial | Polynomial Chain | PerpsMarketProxy (limit order PnL) | `0xD052Fa8b2af8Ed81C764D5d81cCf2725B2148688` | 1 | 0/1 | 0 | 1 | https://0xmacro.com/library/audits/polynomial-4 |
| 2333 | polynomial | Polynomial Chain | PerpsMarketProxy (liquidation logic) | `0xD052Fa8b2af8Ed81C764D5d81cCf2725B2148688` | 1 | 0/1 | 0 | 1 |  |
| 2334 | ramses v3 | Arbitrum | RamsesV3PositionManager | `0x807a31EF83342D279a1F7708Adbc3492405A4CbC` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 2335 | real wagmi 2 update | Metis | LiquidityBorrowingManager | `0x20fa274D00fF4917A13cD464FDbB200475B6EaBd` | 1 | 0/1 | 0 | 1 |  |
| 2336 | ref-finance-dcl | NEAR | DCL exchange (internal_add_order) | `dclv2.ref-labs.near` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 2337 | ref-finance-dcl | NEAR | DCL (y_swap_x_range_complete_desire) | `dclv2.ref-labs.near` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 2338 | ref-finance-dcl | NEAR | DCL (remove-liquidity info check) | `dclv2.ref-labs.near` | 1 | 0/1 | 0 | 1 | https://github.com/blocksecteam/audit-reports/blob/9da368848d5a3b2a4e0f76a4e6dd0 |
| 2339 | revert lend | Base | V3Vault (Base) | `0x36AEAe0E411a1E28372e0d66f02E57744EbE7599` | 1 | 0/1 | 0 | 1 |  |
| 2340 | rhinestone-core-modules | Base | DeadmanSwitch module | `0x8bAdE54bca47199B6732EB2F92318DD666bdE413` | 1 | 0/1 | 0 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 2341 | rhinestone-safe7579 | Ethereum | Safe7579.initializeAccount | `0x7579011aB74c46090561ea277Ba79D510c6C00ff` | 1 | 0/1 | 0 | 1 | https://github.com/Ackee-Blockchain/public-audit-reports/blob/2033ac4dcd808e9ceb |
| 2342 | rocket-pool / rocket-pool-5-lower-eth-bond | Ethereum | RocketMinipoolManager | `0xe54B8C641fd96dE5D6747f47C19964c6b824D62C` | 1 | 0/1 | 1 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 2343 | rocket-pool / rocket-pool-5-lower-eth-bond | Ethereum | RocketNodeStaking | `0xedFc7DCaE43fF954577a2875a9D805874490eE3E` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 2344 | sapien ffb7e698 | Base | SapienToken (SAPIEN, proxy) | `0xc729777d0470f30612b1564fd96e8dd26f5814e3` | 1 | 0/1 | 1 | 1 |  |
| 2345 | secured-finance | Ethereum | LendingMarketController | `0x35e9D8e0223A75E51a67aa731127C91Ea0779Fe2` | 1 | 0/1 | 0 | 1 |  |
| 2346 | shezmu 2024 10 shezmu smart contract | Ethereum | ShezmuStablecoin (ShezmuUSD) | `0xD60EeA80C83779a8A5BFCDAc1F3323548e6BB62d` | 1 | 0/1 | 1 | 1 |  |
| 2347 | sigmaprime eigenlayer sigma prime eigenlabs eigenlayer eigen | Ethereum | RewardsCoordinator (proxy) | `0x7750d328b314EfFa365A0402CcfD489B80B0adda` | 1 | 0/1 | 0 | 1 |  |
| 2348 | sigmaprime omni network sigma prime omni solvernet security  | Ethereum | OmniPortal | `0x709e7db90d1960F3B000FEAC67F397a329327E8a` | 1 | 0/1 | 0 | 1 |  |
| 2349 | sigmaprime sushi bentobox strategies staking contract | Ethereum | BentoBoxV1 | `0xF5BCE5077908a1b7370B9ae04AdC565EBd643966` | 1 | 0/1 | 0 | 1 |  |
| 2350 | sigmaprime-term-finance-term1-review | Ethereum | TERM token | `0xC3d21f79C3120A4fFda7A535f8005a7c297799bF` | 1 | 0/1 | 0 | 1 |  |
| 2351 | solo 2023 11 17 florencefinance | Base | FlorinTreasury (Base) | `0xD850C9cBbD314b9A5ceaCF9C9668676137a3e28B` | 1 | 0/1 | 1 | 1 |  |
| 2352 | sperax usds 0612feed | Arbitrum | ChainlinkOracle (per-asset adapter read  | `0x14D99412dAB1878dC01Fe7a1664cdE85896e8E50` | 1 | 0/1 | 0 | 1 |  |
| 2353 | sperax usds 0612feed | Arbitrum | YieldReserve | `0xfD14C8ef0993fd9409f7820BA8BA80370529d861` | 1 | 0/1 | 0 | 1 |  |
| 2354 | stNXM by EaseDeFi | Ethereum | stNXM vault | `0x5b423e07dfba087d72840851f63a51cbe1967cda` | 1 | 0/1 | 1 | 1 | https://audits.sherlock.xyz/contests/1203 |
| 2355 | staked-thales-betting-proxy | Optimism | StakingThales | `0xC392133eEa695603B51a5d5de73655d571c2CE51` | 1 | 0/1 | 0 | 1 | https://www.iosiro.com/audits/staked-thales-betting-proxy-smart-contract-audit |
| 2356 | sukukfi | Berachain | PrimeTel vault (duPRT, ERC-7540 async va | `0x1B610abd3dFA170fdC579c48da7007217c06149D` | 1 | 0/1 | 1 | 1 |  |
| 2357 | super boring | Base | SuperBoring (main) | `0x37D607BD9dfFf80acf37184c1F27E88388914262` | 1 | 0/1 | 0 | 1 |  |
| 2358 | synthetix-sip-420-treasury-market | Ethereum | TreasuryMarket (SIP-420) | `0x76067aAb89a73cB5f688F4196211C26355C1f649` | 1 | 0/1 | 0 | 1 | https://www.iosiro.com/audits/synthetix-sip-420-treasury-market-smart-contract-a |
| 2359 | taraxa-bridge-smart-contracts-v2-securityreview | Ethereum | Bridge (signature validation) | `0x359CF536b1fd6248ebAd1449E1B3727caB33A01d` | 1 | 0/1 | 0 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 2360 | taraxa-bridge-smart-contracts-v2-securityreview | Ethereum | Bridge (applyState) | `0x359CF536b1fd6248ebAd1449E1B3727caB33A01d` | 1 | 0/1 | 1 | 1 | https://github.com/trailofbits/publications/blob/89940dfbec07ad03b0989e67d78e842 |
| 2361 | team 2024 01 24 hytopiawallet | HYCHAIN | HYCHAIN Smart Contract Wallet factory /  | `0x9585fd3ab7633dC3D7747c168f9032D1F242D2Cf` | 1 | 0/1 | 1 | 1 |  |
| 2362 | team 2024 07 31 sharwafinance | Arbitrum | LiquidityPool/MarginTrading (liquidation | `0xd50Dffb8a9997D1651F3AB67e55a394C81170137` | 1 | 0/1 | 0 | 1 |  |
| 2363 | team 2025 01 13 onchainheroes | Abstract | HeroERC721A.ogMint | `0x7c47ea32fd27d1a74fc6e9f31ce8162e6ce070eb` | 1 | 0/1 | 0 | 1 |  |
| 2364 | team 2025 03 19 hyperstable | Hyperliquid EVM | Hyperstable Voting Escrow (veHYPE-style  | `0xdB9A1bdc443dd11366b8a6dc8038144eCc4D4E23` | 1 | 0/1 | 0 | 1 |  |
| 2365 | team 2025 06 28 gainsnetwork security july2 | Arbitrum | GNSMultiCollatDiamond (trading core) | `0xFF162c694eAA571f685030649814282eA457f169` | 1 | 0/1 | 0 | 1 |  |
| 2366 | team 2025 11 11 hybux | Base | HYBUX token proxy | `0xc0497fb3fc4fd0a17900cf69fc72a03799915301` | 1 | 0/1 | 1 | 1 |  |
| 2367 | teller lender groups update audit | Ethereum | LenderCommitmentGroup (per-lender clone) | `0x21499A1Fd9f36ce527CB4A9032072ef1bb7a22F6` | 1 | 0/1 | 1 | 1 |  |
| 2368 | tokensfarm | Ethereum | TokensFarm farm proxy | `0x0abEe06A64b25A4dcBCEaa4a44Ff159Df52dC218` | 1 | 0/1 | 1 | 1 | https://github.com/zokyo-sec/audit-reports/blob/39b9e51ac1b68a42ac03b222167760f7 |
| 2369 | traderjoe | Avalanche | LBPair / LBToken (_transfer) | `0x8e42f2F4101563bF679975178e880FD87d3eFd4e` | 1 | 0/1 | 1 | 1 |  |
| 2370 | traderjoe | Avalanche | LBPair (LBToken + collectFees) | `0x8e42f2F4101563bF679975178e880FD87d3eFd4e` | 1 | 0/1 | 1 | 1 |  |
| 2371 | train protocol-feb-25( ) upd | Ethereum | HashedTimeLockERC20 / Train HTLC | `0x265978c3e2E5dB9C3Ea665cC40C5925A5fc13Ee8` | 1 | 0/1 | 0 | 1 | https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/84e78849628c |
| 2372 | unknown (hf: termmax-competition) | Ethereum | TermMaxMarket | `0x609F20ee24E10010A62970E1dAb7E2b84eD74CAb` | 1 | 0/1 | 0 | 1 |  |
| 2373 | unstoppable | Arbitrum | DCA Orders (Dca.vy) | `0x314CE4530bfe353ECefCA27190222364b004dA8c` | 1 | 0/1 | 1 | 1 |  |
| 2374 | unstoppable | Arbitrum | Dca.execute_dca_order (spot-dex/Dca.vy) | `0x314CE4530bfe353ECefCA27190222364b004dA8c` | 1 | 0/1 | 0 | 1 |  |
| 2375 | v2 Contracts | Ethereum | TermAuctionBidLocker._lock | `0xb4B1de03F229220eDbBB31A224b2a004b3c3e47f` | 1 | 0/1 | 1 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 2376 | v2 Contracts | Ethereum | ERC4626InterfaceFacet / TermMorphoInterf | `0xb4B1de03F229220eDbBB31A224b2a004b3c3e47f` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 2377 | v2 Contracts | Ethereum | TermRepoCollateralManager.batchLiquidati | `0xb4B1de03F229220eDbBB31A224b2a004b3c3e47f` | 1 | 0/1 | 0 | 1 | https://github.com/sigp/public-audits/blob/7d9046e092e1e93623164e39df8c552a16f2f |
| 2378 | v3 poc | Ethereum | Transmuter.createRedemption (Transmuter. | `0x073598132f37756a7E665FB52f1757463120bd3C` | 1 | 0/1 | 0 | 1 |  |
| 2379 | veYFI | Ethereum | veYFI (reward weight / gauge) | `0x90c1f9220d90d3966fbee24045edd73e1d588ad5` | 1 | 0/1 | 0 | 1 | https://github.com/electisec/Reports/blob/b6c835102a52ce9aab32e52790efad302b2b5e |
| 2380 | vultisig | Ethereum | ILOManager (whitelist / project config) | `0x0d781106DA1da95f76150e16D1c6fCCf1e41B762` | 1 | 0/1 | 0 | 1 |  |
| 2381 | vultisig | Ethereum | ILOManager (LiquidPad ILO platform) | `0x0d781106DA1da95f76150e16D1c6fCCf1e41B762` | 1 | 0/1 | 0 | 0 |  |
| 2382 | vynksafe | BNB Smart Chain | VYNK governance token (VYNKSAFE) | `0xee1ae38BE4Ce0074C4A4A8DC821CC784778f378c` | 1 | 0/1 | 0 | 1 |  |
| 2383 | wake-arena-ai--ipor-labs-fusion-dec-11 | Ethereum | ERC4626ZapInWithNativeToken | `0x677251190C0cCcC6E7e71C385B3EA660Dfd89c00` | 1 | 0/1 | 1 | 1 | https://github.com/Ackee-Blockchain/public-wake-arena-reports/blob/e6553332fd1e5 |
| 2384 | wildcat | Ethereum | WildcatMarket (per-market accounting) /  | `0xfEB516d9D946dD487A9346F6fee11f40C6945eE4` | 1 | 0/1 | 0 | 1 |  |
| 2385 | wildcat | Ethereum | WildcatMarket (withdrawal batch accounti | `0xfEB516d9D946dD487A9346F6fee11f40C6945eE4` | 1 | 0/1 | 0 | 1 |  |
| 2386 | wildcat | Ethereum | WildcatSanctionsSentinel | `0x437e0551892C2C9b06d3fFd248fe60572e08CD1A` | 1 | 0/1 | 1 | 1 |  |
| 2387 | woofi swap | Arbitrum | WooPPV2 (sPMM pool) | `0x5520385bFcf07Ec87C4c53A7d8d65595Dff69FA4` | 1 | 0/1 | 1 | 1 |  |
| 2388 | xSNX | Ethereum | xSNX (xSNXProxy) | `0x2367012aB9c3da91290F71590D5ce217721eEfE4` | 1 | 0/1 | 0 | 1 | https://www.iosiro.com/audits/xsnx-smart-contract-audit |
| 2389 | yAcademy GET Protocol Staking | Ethereum | GET staking cross-chain voting | `0x3e49E9C890Cd5B015A18ed76E7A4093f569f1A04` | 1 | 0/1 | 0 | 1 | https://github.com/yAudit/fellowship-audits/blob/2ddaff163a55d9d436c07e86adf18f9 |
| 2390 | yAcademy veYFI | Ethereum | veYFI (reward weight / gauge) | `0x90c1f9220d90d3966fbee24045edd73e1d588ad5` | 1 | 0/1 | 0 | 1 | https://github.com/yAudit/fellowship-audits/blob/2ddaff163a55d9d436c07e86adf18f9 |
| 2391 | yAcademy veYFI | Ethereum | veYFI (VotingEscrow) | `0x90c1f9220d90d3966fbee24045edd73e1d588ad5` | 1 | 0/1 | 0 | 1 | https://github.com/yAudit/fellowship-audits/blob/2ddaff163a55d9d436c07e86adf18f9 |
| 2392 | yAxis MetaVault V2 | Ethereum | yAxis MetaVault 3CRV | `0xBFbEC72F2450eF9Ab742e4A27441Fa06Ca79eA6a` | 1 | 0/1 | 0 | 1 |  |
| 2393 | yAxis contest | Ethereum | yAxis Vault (MIM3CRV) | `0x9720346Ba80b668E50A5560c200180515fEbb895` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-09-yaxis-findings/blob/294b98fb39255dde574836 |
| 2394 | yAxis contest | Ethereum | Vault.balance | `0x9720346Ba80b668E50A5560c200180515fEbb895` | 1 | 0/1 | 0 | 1 | https://github.com/code-423n4/2021-09-yaxis-findings/blob/294b98fb39255dde574836 |
| 2395 | yAxis contest | Ethereum | Vault (multi-token) | `0x9720346Ba80b668E50A5560c200180515fEbb895` | 1 | 0/1 | 1 | 1 | https://github.com/code-423n4/2021-09-yaxis-findings/blob/294b98fb39255dde574836 |
| 2396 | zivoe-locker-contracts | Ethereum | Zivoe Locker (processRequest portion) | `0x49C8919162daE24468965557C9344bA2aa8121b8` | 1 | 0/1 | 0 | 1 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 2397 | zivoe-locker-contracts | Ethereum | Zivoe locker (liquidity thresholds) | `0x49C8919162daE24468965557C9344bA2aa8121b8` | 1 | 0/1 | 0 | 1 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 2398 | zivoe-locker-contracts | Ethereum | Zivoe locker (min expected values) | `0x49C8919162daE24468965557C9344bA2aa8121b8` | 1 | 0/1 | 0 | 1 | https://github.com/runtimeverification/publications/blob/c30a9c50b8b2eed9e58fab9 |
| 2399 | zkSync Era | Ethereum | DiamondProxy (L1 zkSync Era diamond) | `0x32400084C286CF3E17e7B677ea9583e60a000324` | 1 | 0/1 | 0 | 1 | https://github.com/sergeyshemyakov/audit-dataset/blob/b3e52c1635b74bd4ef248b5298 |

*2,399 target rows, 1,696 unique addresses. Full finding-level mapping: `stage2/index/stage2_master.csv`.*

## 3. Findings with no deployment address

Grouped by project. These are the Stage 2 backlog: the report is profit-plausible, but public evidence did not yield a live contract address. Reasons are taken from the tracing agent notes.

| # | Project | Findings | C/H | Reason / missing evidence |
|---:|---|---:|---|---|
| 1 | unknown | 222 | 18/204 | Catch-all unit: the 10 findings come from 10 unrelated protocols (Rubicon, Tapioca, Beedle, Opus, Ondo, Zaros, Coded Estate, Cork, Ethereum EVM basis/SimpleShares, Possum Labs). The supplied llama candidate "Unknown" (UN |
| 2 | Redacted | 19 | 0/19 | Identity unresolved. The Bailsec "Redacted" report has exactly the same 205 findings and severity counts as the Bailsec Usual Money report (same codebase, contract names CartelToken/STBC/MinterPool), so it is not the Red |
| 3 | Code4rena - Nibiru | 16 | 11/5 | Findings are in chain-level Go modules (x/evm precompiles, x/perp) and Solana programs (4real sol-staking, distributor) audited as part of the Nibiru/4Real engagement. No deployed contract or program id is given in the r |
| 4 | 2024-03-19-smart-contracts | 13 | 0/13 | Cantina competition March 2024 (cantina_competition_goat_mar2024.pdf, project 'Goat Tech'). No official site, repository, docs or deployed address was found; the code appears to be pre-deployment. All findings are addres |
| 5 | Flayer | 13 | 0/13 | Flayer's docs domain (docs.flayer.xyz) no longer resolves and no deployment page, address book or live contract list was found. Findings are mapped to source-level contract names only. |
| 6 | LEND | 13 | 0/13 | Audit scope is tenfinance/Lend-V2 (private/404) and the project publishes no deployment page or address book. Chains are from the Sherlock contest README Q&A (Base, Ethereum, Sonic, Monad, BNB). All findings are address- |
| 7 | Carapace | 12 | 0/12 | Docs and whitepaper publish no deployment addresses, and the GitHub contracts repository returns 404. No live deployment or address book could be sourced. |
| 8 | NOYA | 12 | 0/12 | NOYA docs describe the architecture but publish no contract addresses; no DefiLlama listing or deployment page was found. All findings are address-null. |
| 9 | Oku's New Order Types Contract Contest | 12 | 0/12 | The audited OracleLess/Bracket/StopLimit contracts were not located on-chain. The batch's report address 0xB737dD8... is a PoC attack contract in the report, not a deployment; Oku's published deployments page lists Unisw |
| 10 | ZK Circuit | 11 | 9/2 | The unit is a corpus bucket, not a protocol. Nine findings are Scroll zkEVM circuit audits (Zellic, 2023) and one is a Wormhole proof-of-burn circuit audit (Electisec, 2025). The vulnerable logic is circuit code (RLP/MPT |
| 11 | Autonomint Colored Dollar V1 | 10 | 0/10 | No mainnet deployment could be verified. The audit repo contains only testnet OpenZeppelin manifests (base-sepolia, sepolia, goerli, unknown-919) and commented-out deploy scripts; the project is absent from DefiLlama and |
| 12 | Omo | 9 | 2/7 | Pashov review of `omo-protocol/omo-mvp` (2025-01-25). That repository is private (GitHub 404), the report names no chain or address, and no public deployment was found. `omo.finance` is a different project (fUSD stableco |
| 13 | Liquify – 3rd Audit | 9 | 0/9 | BailSec 'Liquify - 3rd Audit' (Jan 2025) covers a launchpad/escrow contract with projects, paymentToken/realToken, vesting phases, initiatorDeposit, claimRealTokens and setRefundStatus. Neither the report front matter no |
| 14 | Poolshark Cover | 8 | 6/2 | No mainnet Cover deployment exists. scripts/autogen/contract-deployments.json in poolshark-protocol/cover lists only arb_goerli (coverPoolFactory 0x479C2Df7eD63ea26146Ac2092C55047C3928A5A6) and scroll_alpha (0xc1E9A857e9 |
| 15 | thirdWeb-6 | 8 | 4/4 | thirdweb is a contract factory/platform: Marketplace, Drop, Pack and smart-wallet contracts are deployed per customer on many EVM chains, so there is no single deployment address for the audited code. Identity resolved t |
| 16 | Ammplify | 8 | 0/8 | No mainnet deployment found. The project's public repo (itos-finance/AmmplifyPublic) ships deployed-addresses.json for 'Chain 10143' (Monad testnet) only, with simplexDiamond 0x67C78CbE8eF94D14A8519572b8AEEcad4bb9319B an |
| 17 | Chakra | 8 | 0/8 | No live deployment address could be established. The audit repo (code-423n4/2024-08-chakra) contains no address book, docs.chakrachain.io is behind an Auth0 login, and the batch's seven report_addresses (0x03842b8f..., 0 |
| 18 | NearOinDao | 8 | 0/8 | No NEAR contract account for the audited OIN DAO was found. oin.near and oinfinance.near exist but return code_hash 11111111111111111111111111111111 (plain accounts, no contract); nearoindao.near and dao.oin.near do not  |
| 19 | Tapioca Invitational | 8 | 0/8 | Tapioca DAO's GitHub org and docs no longer resolve (tapioca.xyz now redirects to Alto); the Magnetar address could not be sourced from any official or explorer page. Chain list from the contest README (Arbitrum, Ethereu |
| 20 | Router Voyager Forwarder and | 7 | 6/1 | The audited contracts are CosmWasm asset-forwarder middleware, a NEAR FT contract and the cosmwasm gateway, not EVM contracts. Router's current docs only cover the OGA/swap API and publish no contract addresses; no on-ch |
| 21 | Denaria 2 | 7 | 5/2 | Batch label: Denaria 2. Denaria is a Linea perp DEX (DefiLlama: denaria-vamm, TVL ~$188) and the audited repo is denaria-finance/denaria-perp. Neither docs.denaria.finance nor the ConsenSys report publishes deployment ad |
| 22 | Filament (Filament Finance, Sei) | 7 | 3/4 | Batch label: Filament Aug15th. Filament Finance is a Sei perp DEX (DefiLlama: filament-v1/filament-beta, Twitter FilamentFinance). The Zellic report confirms 'the contracts would be deployed on SEI' and scopes Diamond/Tr |
| 23 | 2023-08-07-beedle-oracle-free-perpetual-lending | 7 | 0/7 | Beedle (oracle-free perpetual lending, Cyfrin/Code4rena 2023-07) has no verifiable live deployment: beedle.fi/beedle.xyz do not resolve and no address is published in the audit repo. Chain assumed Ethereum from the conte |
| 24 | 2024-03-15-final-tapioca-audit-report | 7 | 0/7 | Same Tapioca DAO deployment problem as the invitational batch: GitHub org and docs no longer resolve, and no USDO/oTAP/Magnetar address is published in the audit repo. |
| 25 | Curves | 7 | 0/7 | Batch label: Curves. Curves (Code4rena 2024-01) is a friend.tech-style token protocol by 0xForm. DefiLlama lists the live protocol as 'Curves Protocol' on Form Network, but the project sites (curves.fun, curves.xyz, curv |
| 26 | Primitive Hyper | 7 | 0/7 | No deployed Primitive Hyper contract was found: no repository for the 2023 'Hyper' codebase exists in the primitivefinance org, and no address book, docs or explorer entry was located. All seven findings come from a Trai |
| 27 | Tadle | 7 | 0/7 | Batch label: 2024-08-12-tadle. Identity problem: tadle.com now hosts an unrelated dApp-sandbox product; app.tadle.com no longer resolves and no Tadle docs/contracts page survives. Searches on Arbiscan found no 'Tadle' la |
| 28 | pashov-team-2025-01-25-omo-security-review | 7 | 0/7 | Identity from the Pashov report: review of omo-protocol/omo-mvp at commit c52b6d3. The repo and org repo listing are 404/private, the project has no DefiLlama entry, and no verified deployment of OmoVault/OmoRouter/OmoAg |
| 29 | Artrade | 6 | 5/1 | Artrade is a Solana NFT marketplace audited by Fuzzland. The report gives no program IDs and the current artrade.app has pivoted to a staking/luxury-goods site with no developer docs or program addresses; no Solana progr |
| 30 | Atomic Loans | 6 | 5/1 | Atomic Loans is a 2019 Bitcoin-collateralised lending project audited by ConsenSys Diligence pre-deployment (the report still references Ropsten Chainlink job IDs and says critical items will be resolved at deployment).  |
| 31 | Voyage | 6 | 5/1 | llama_candidates 'Voyager' 0x3C4B6E6e1eA3D4863700D7F76b36B7f3D3f13E3d is the bankrupt CeFi lender Voyager Digital, unrelated to the NFT-lending protocol in the Zellic 2022 report, and is rejected. No Voyage deployment fo |
| 32 | Liquorice | 6 | 3/3 | The MixBytes report (2025-02-21) is a pre-deployment review: its only addresses are DAI and WETH, and no Liquorice deployment, docs site, or repository could be located. No chain or contract address is recorded rather th |
| 33 | 2025-07-16-openzeppelin-uniswap-hooks-v1-1-0-rc-1-audit | 6 | 0/6 | Audit of the Uniswap hooks Solidity library at v1.1.0-rc.1 (OpenZeppelin, 2025-05-12). It is a library release candidate, not a deployed protocol: no deployment addresses are published for LimitOrderHook/AntiSandwichHook |
| 34 | DeltaTrade | 6 | 0/6 | DefiLlama shows live TVL on NEAR (~$101k) and Solana (~$1k) but neither the docs site nor the BlockSec report publishes contract account ids or program ids; no explorer lookup was possible without those ids. All findings |
| 35 | Trustless Work Stellar | 6 | 0/6 | Stellar/Soroban target: no deployed contract id in the docs, llms.txt index or repository README within the timebox. Escrows are deployed per agreement, so there is no single protocol address. |
| 36 | 2023-11-07-metatime-sca-metatime-layer-2-oct2023-s | 5 | 5/0 | No report body or source URL exists in the corpus for this 2023-10 SCA review, and Metatime publishes no address book: the GitHub org ships the MetaChain client and genesis-contracts bindings, not deployed addresses. The |
| 37 | ComposableFinance zk ed25519 v 1 0 | 5 | 5/0 | ABDK review of the zk ed25519 circuit/Go code (element_q.go, element_o.go). Circuit code has no standalone deployed address; the consuming bridge verifier was not identified. |
| 38 | EDGESWAP | 5 | 5/0 | ABDK 2021 review of the EdgeSwap zk circuit. No live deployment, docs or repository address book found; project appears defunct. |
| 39 | SundaeSwap V1 Contracts | 5 | 5/0 | Cardano Plutus contracts; deployment identity is a script hash and the Runtime Verification report does not include one. DefiLlama lists SundaeSwap as cardano:9a9693a9... but that is the SUNDAE token policy, not the V1 p |
| 40 | 02 10 Lulo-MR | 5 | 4/1 | Certora audit of Lulo's Solana programs. No program id (base58) surfaced from docs.lulo.fi, the docs index or the public listings reached. |
| 41 | CornerMarket Contracts v15 | 5 | 4/1 | Hardhat config in the audited repo only defines Polygon Mumbai (chain 80001, deprecated testnet); no mainnet deployment or address book found on Ethereum, Polygon, Arbitrum or Base. |
| 42 | Degensafe Protocol | 5 | 4/1 | Solana Anchor programs (sol_deposit, staking). No program ID is given in the Guardian report or any public repo/docs; Solana explorer search returned nothing. |
| 43 | starbase | 5 | 4/1 | Consensys audit targets StarBaseLimitOrder/StarBaseDCA on Base. Starbase GitBook is behind a GitBook sign-in wall; Base Blockscout/Basescan are Cloudflare-blocked from this host; the report's 0x addresses are deployer EO |
| 44 | Hyvechain precompiles | 5 | 3/2 | Audit covers chain-native precompiles (Rust) on HyveChain (chain id 7847 per chainid.network); precompiles are not deployed contracts, so no contract address exists to record. |
| 45 | Nukem Loans | 5 | 3/2 | Zellic report section 6: 'At the time of our assessment, the reviewed code was not deployed to the Ethereum Mainnet.' No deployment address to trace. |
| 46 | Soqucoin | 5 | 3/2 | Soqucoin is a standalone Bitcoin-style UTXO L1 audited at the node/verifier level (Halborn). No contract deployment addresses exist to trace. |
| 47 | THORChain / Rujira | 5 | 3/2 | Rujira contracts are CosmWasm modules on THORChain (rujira-fin, ruji-lending, nami index product, scheduler). No public address book with thor1... contract addresses was found; the source repos are the only verifiable id |
| 48 | Ulysses Protocol | 5 | 3/2 | Maia DAO Ulysses is deployed across Metis/Arbitrum/Base and others, but no public address book entry for RootBridgeAgent/BranchBridgeAgent/MulticallRootRouter was found in the timebox. |
| 49 | 03 30 Templar-FV-MR | 5 | 2/3 | Certora formal-verification audit of Templar, a Stellar Soroban lending protocol. No contract id located in the timebox. |
| 50 | 09-13--IVX | 5 | 2/3 | Guardian 2023-09 review of IVXDiem / IVXPortfolio, a 0dte options AMM. IVX's current docs (documentation.ivx.fi) publish no contract-address page, and no IVXDiem or IVXPortfolio contract appears in explorer search. DefiL |
| 51 | Apollo DAO Smart Contracts | 5 | 2/3 | Oak Security reviewed Apollo DAO's CosmWasm contracts on Terra. The two reports contain no terra1 contract addresses, apollodao.org and docs.apollodao.org no longer resolve, and a Terra contract address cannot be discove |
| 52 | Hyperhyper | 5 | 2/3 | Site is live but publishes no deployment data; the audited repo Hyperhyperfi/protocol now returns 404, so no chain or address could be evidenced. |
| 53 | Omisego Morevp | 5 | 2/3 | MoreVP framework audited before deployment. The only report lead, 0xa000000000000000000000000000000000000000, has no code on Ethereum mainnet and no explorer label, so it was rejected. |
| 54 | Synthetix BFP 2 | 5 | 2/3 | Synthetix perps ('BFP') is deployed on Base through the Cannon package synthetix-perps-market 3.6.5 (chain 8453, preset andromeda); the package page confirms the deployment but the PerpMarketProxy address is only exposed |
| 55 | XPower | 5 | 2/3 | Report metadata carries no URL and no chain. xpowermine.com (XPOW/APOW) is the likely project but the audited contracts (XPower, LeechRouterBase) have no published address; only an APOW token on Avalanche is listed by Co |
| 56 | Hacken OÜ | 5 | 1/4 | Auditor-name unit, not a protocol: findings are for the client projects "alt platform" and "yoshi". No deployment information is attached to these findings. |
| 57 | Nomyx | 5 | 1/4 | All six addresses supplied as report leads are EOAs on Base (three carry EIP-7702 delegation, three have no code), not the Gemforce diamond. Docs describe Diamond deployments on Base/Sepolia but publish no diamond addres |
| 58 | OpenZeppelin Uniswap Hooks v1.1.0 RC 1 | 5 | 1/4 | Scope is the OpenZeppelin Uniswap Hooks Solidity library at v1.1.0-rc.1 (BaseHook/LimitOrder/AntiSandwichHook). It is a library consumed by hook deployers, not a protocol deployment, so there is no address. |
| 59 | Size v1 | 5 | 1/4 | Two codebases in scope (2022 SizeSealed auctions, 2024 Size credit). DefiLlama lists 'Size Lending' on Base without an address; no deployment file in the audit repos. |
| 60 | Switchboard Onchain | 5 | 1/4 | OtterSec review of Switchboard's on-chain Solana programs. The commonly cited on-demand program ID did not resolve on mainnet-beta in this pass, so no address is recorded. |
| 61 | ULTI | 5 | 1/4 | Pashov review of 'Ulti' (EVM, November 2024) names ULTI, _swapInputTokenForUlti, twapPrice and _updateTWAP but no chain, deployment or address; no deployment could be resolved. |
| 62 | poodlTech | 5 | 1/4 | poodlTech's public repo (poodlTech/tokenAudit) contains only Hardhat deployment scripts and constructor args, no deployed address; no explorer hit for the token. Identity is a BEP-20 dividend token with a PancakeSwap pai |
| 63 | AbraNFT contest | 5 | 0/5 | AbraNFT was a 2022-04 code4rena contest for a new NFT-collateral lending module (NFTPair.sol / NFTPairWithOracle.sol). Neither the report nor Abracadabra docs publish deployment addresses, and Ethereum explorer search re |
| 64 | Advanced Blockchain | 5 | 0/5 | Trail of Bits Q4-2021 review of Advanced Blockchain's Bribe Protocol (target contracts/BribeMultiAssetPoolBase.sol) plus a dAPI median-price component; report metadata lists Substrate. The report names source files only  |
| 65 | Advanced Blockchain (Picasso Parachain and Bribe Protocol) | 5 | 0/5 | Second Trail of Bits Advanced Blockchain engagement covering the Picasso parachain (Substrate) and Bribe Protocol. Findings reference source paths only (swapToNative, _bid, initializer); no parachain account ids or EVM c |
| 66 | Code Snippet Tool used | 5 | 0/5 | Sherlock placeholder unit (code snippet tool), not a single protocol: the findings belong to Allora (2024) and to Notional, Sherlock contest 52 (2023). No shared deployment exists. |
| 67 | Coded Estate Invitational | 5 | 0/5 | CosmWasm contracts (execute.rs). No chain or contract address is published in the Code4rena repo, website or gitbook; no bech32 contract address located. |
| 68 | FairSide | 5 | 0/5 | No live FairSide deployment found. The addresses in the report PoC (0x564Db7a1..., 0x76a999d5..., 0x41427a14...) are explicitly localnet placeholders and are not contracts on Ethereum mainnet. |
| 69 | Infinity NFT Marketplace contest | 5 | 0/5 | Code4rena 2022-06 contest for the Infinity NFT marketplace; no deployment address in the contest material and no live marketplace found (infinity.exchange is an unrelated rates protocol). |
| 70 | Rest Finance | 5 | 0/5 | Guardian Audits report only; no address in the report text, no docs site reachable and no DefiLlama entry (restake-finance is a different protocol). |
| 71 | Sublime contest | 5 | 0/5 | 2021 and 2022 code4rena contests on the Sublime credit protocol; the repo is not maintained and no deployment address was found. |
| 72 | Superposition | 5 | 0/5 | code4rena 2024-08 scope is the Seawater AMM (Rust/Stylus) deployed on Superposition, an Arbitrum Orbit chain (webapp long.so). No public address book. |
| 73 | Thema Protocol | 5 | 0/5 | The report names OMTPriceFeed and OMT mint/redeem but gives no chain or address. A BEP-20 'OMT' token exists on BNB Chain (0x851DA0BEA7FE6dB35C11C1d3A065a96E6B36acf1) but the link to 'Thema Protocol' could not be verifie |
| 74 | nan | 5 | 0/5 | Unit 'nan' is a mixed bucket of five unrelated findings (SatsBridge HTLC forwarder, 2018 EVM basis governance, SushiXSwap sgReceive, AntePool, Sequence sessions). There is no single project to trace. |
| 75 | CircuitDAO | 4 | 4/0 | Chia is non-EVM: contracts are Chia puzzles identified by puzzle hashes, not deployed addresses. The audited code is the puzzle library github.com/circuitdao/puzzles; no mainnet puzzle hash is published in the repo or do |
| 76 | Infinity Swap | 4 | 4/0 | OtterSec audit (2023-04) of the infinity-swap Rust canisters on the Internet Computer. The report extract contains no canister IDs; the project rebranded to Bitfinity and the infinityswap-contracts repo has no canister_i |
| 77 | Rengo Labs Uniswap Core-Router Casper Smart Contract Security | 4 | 4/0 | Halborn audit of a Casper (Odra/Casper smart contract) Uniswap core-router port. The report extract contains no package hashes or account hashes, no Rengo Labs website/docs/GitHub with a deployment manifest was found, an |
| 78 | Socket- -dec24 | 4 | 4/0 | Hexens review of Socket's SOR/DLN inbox code (src/inboxes/SORInbox.sol, src/core/SingleOutputRequestImpl.sol, src/core/SwapRequestImpl.sol). No deployment address for SORInbox could be located: docs.socket.tech/integrate |
| 79 | Watt Protocol | 4 | 4/0 | Solana Anchor program (programs/watt, staking/raydium_cpmm.rs). Project domains (wattprotocol.com/www.wattprotocol.com) do not resolve; no docs, GitHub org or program ID surfaced in two searches. Program ID not recorded  |
| 80 | mell Stable Gas Pricing _ | 4 | 4/0 | Guardian Audits review of the Foil 'Epoch' modules (EpochLiquidityModule.sol, EpochTradeModule.sol). docs.foil.xyz routes its 'Deployments' link to a Cannon package (usecannon.com/packages/foil) with no static address ta |
| 81 | pencils- -aug | 4 | 4/0 | Hexens audit (Aug 2024) of Pencils on Scroll. docs.pencilsprotocol.io (llms-full.txt, 121 KB) contains no contract addresses, DefiLlama has no address and no adapter file, and no Scroll explorer search endpoint answered. |
| 82 | 09-03--PariFi | 4 | 3/1 | Guardian Audits PariFi report (2023-09-03) names OrderManager/Vault but no addresses. parifi.org returns 403 to this host, docs.parifi.xyz does not resolve, GitHub org repo listing is empty, and DefiLlama has no Parifi e |
| 83 | Comdex | 4 | 3/1 | Comdex is a Cosmos SDK appchain (chain-id comdex-1, per the Cosmos chain registry). The audited locker, market and rewards components are native chain modules, not deployed contracts, so there is no contract address to r |
| 84 | Composable Bridge | 4 | 3/1 | OtterSec review of the Composable Solana bridge and stake-pool programs. The report page is JS-only and names no program id; no on-chain program address could be confirmed from public sources. |
| 85 | Milky Ice | 4 | 3/1 | Only the Composable Security PDF reference exists; no website, repo or deployment addresses for Milky Ice were findable. |
| 86 | Nawa Finance | 4 | 3/1 | Oak Security audit (2025-10) of a CosmWasm vault on ZIGChain. nawa.finance and app.nawa.finance serve a 6.5 KB landing page with no addresses, no docs site resolves, and no CosmWasm contract address (zig1...) was found.  |
| 87 | Router Asset Bridge | 4 | 3/1 | Oak review of Router Asset Bridge v1.2 (EVM AssetBridge.sol + NEAR token contract). The current docs site is the rewritten 'OGA' docs and has no Asset Bridge address table; the router-chain-docs ContractAddressTable.js n |
| 88 | Stablecoin.xyz A-2 | 4 | 3/1 | Two Macro audits (2025-xx and 2026) of the Stablecoin.xyz solver/escrow stack (Solana origin settler + Base solver + ERC-4337 paymaster). stablecoin.xyz serves a marketing page with no addresses and no docs/contracts pag |
| 89 | VerifiedX | 4 | 3/1 | Halborn reviews (2025, 2026) of VerifiedX core node software, not a smart contract. Findings live in Go consensus/token code on the VFX network; there is no EVM contract address to record. docs.verifiedx.io documents vBT |
| 90 | printr-protocol | 4 | 3/1 | Ackee audit (2025) of the Printr launchpad (PrintrTeleport, PrintrTrading, Telecoin). Printr docs (llms.txt) expose no deployment addresses, the ABI page links binary files, and Ethereum/Base explorer searches return onl |
| 91 | x Shib.io | 4 | 3/1 | SOU NFT contracts (Hexens, Nov 2025) live on Shibarium; no contract address is published on shib.io or in the report, and Shibarium explorers were not reachable within budget. |
| 92 | Coinflip | 4 | 2/2 | Pre-deployment review (Feb 2025) of play-turbo/coinflip-contracts. The report states the project 'plans to deploy on multiple chains' and publishes no deployment address; the repository now returns 404, so no chain or co |
| 93 | Levana Perpetual Swaps | 4 | 2/2 | Oak Security audit (2022-05) of Levana Perpetual Swaps v1, a CosmWasm deployment (Terra-era, UST risk fund). The report extract carries no terra1/osmo1 contract addresses, Levana's docs expose no v1 contract-address page |
| 94 | Moonbite GmbH | 4 | 2/2 | MoonBite GmbH built on Phoenix Protocol Group's Soroban contracts on Stellar. The repo ships mainnet wasm binaries but no contract IDs, so no on-chain address could be attributed. |
| 95 | Out GCC | 4 | 2/2 | Oak Security review of Out Protocol (Solana). No program id in the report extract or batch; the public audit summary does not publish a deployment address. |
| 96 | Security Audit – Neon EVM | 4 | 2/2 | Audited NeonEVM program predates mainnet; the commonly cited program ID NeonVMyRX5GbCrsAHnUwx1nYYoWFhQ7x4w5c4SWw returns null on Solana mainnet-beta (checked via getAccountInfo), so no address is asserted. |
| 97 | Xitadel | 4 | 2/2 | Solana (Anchor) program audit; no EVM deployment. xitadel.com is a JS shell with no address. |
| 98 | Xyro Aug30 | 4 | 2/2 | Zokyo Aug-2024 review of an on-chain game; no docs/deployments page or explorer hit surfaced within budget. |
| 99 | Zodiac Protocol Core | 4 | 2/2 | Oak Security 2024-03 review of the Zodiac Protocol Periphery v1.0: report paths are contracts/osmosis/zodiac_osmo_bal_lockup_vault, zodiac_fee_collector etc., i.e. CosmWasm contracts on Osmosis. Neither the report nor th |
| 100 | for t3rn | 4 | 2/2 | DefiLlama's t3rn entry resolves to the TRN token (0x1114...9e44) and was rejected. No RemoteOrder or AttestationsVerifier deployment address found. |
| 101 | metropolis | 4 | 2/2 | Zokyo 2022 audit of Metropolis World (AccessTokenContract, VRFLottery, CityWL). No deployment manifest is published. Blockscout name search surfaces three CityWL contracts (0x0550a2ad898A11B9384102b121A785bE3D5B18C6, 0x2 |
| 102 | reservoir | 4 | 2/2 | Name collision: docs.reservoir.xyz is a different project (Reservoir rUSD). Rejected rather than mapped. |
| 103 | smart-contract-code-review-and-security | 4 | 2/2 | Multi-project review; chain inferred as BNB Smart Chain from BuniCorn, not confirmed by an address. |
| 104 | Marcin Ugarenko (Lead Solidity SC Auditor at Hacken OU) | 4 | 1/3 | The report is a Hacken review of the CatGirl token sale (swapBNBForCatGirl), a BNB-chain token project. The report names no contract address and no canonical CatGirl deployment could be identified, so nothing is recorded |
| 105 | OLY | 4 | 1/3 | Two Pashov reviews (2025-12-31 and 2026-02-16) of a pre-launch protocol. No website, docs or deployment surfaced, so no address is recorded; the launch-state findings are inherently unverifiable on-chain today. |
| 106 | Rip It | 4 | 1/3 | Pashov Audit Group reviews of Rip It (April and May 2025). Repo is the audit repo only; no project docs, explorer match or DefiLlama entry. |
| 107 | Three Sigma Labs | 4 | 1/3 | This unit aggregates four unrelated Three Sigma reports: MetaZero Vortex bridge, Trestle Finance, MetaZero staking and the Ordiswap token. No single deployment exists to trace, and none of the four reports publishes an a |
| 108 | VMEX | 4 | 1/3 | docs.vmex.finance and vmex.finance are dead; DefiLlama's Optimism entry 0x6d2e...3312 is not a contract on-chain (eth_getCode empty) and was rejected. No LendingPool/LendingPoolAddressesProvider address surfaced. |
| 109 | ZKCross | 4 | 1/3 | Halborn ZKCross penetration test: findings are API/backend defects, and the report extract publishes neither chain nor contract addresses. |
| 110 | 1inch - Aqua - Audit Report | 4 | 0/4 | Bailsec audit of 1inch Aqua (XYCConcentrate / XYCConcentrateArgsBuilder). DefiLlama lists '1inch Aqua' with a dummy adapter and no chains, indicating no indexed deployment; docs.1inch.io llms.txt has no Aqua deployment a |
| 111 | 2022-02-concur | 4 | 0/4 | Code4rena 2022-02 Concur (ConvexStakingWrapper / Shelter / MasterChef). No address book in the contest README; GitHub org ConcurFinance is 404; DefiLlama has no Concur entry; the protocol appears wound down. No address s |
| 112 | 2023-03-29-final-carapace-audit-report | 4 | 0/4 | Carapace protection-marketplace audit (Goldfinch NFT protections, sToken, leverageFactor). docs.carapace.finance does not resolve, carapace.finance is a marketing site with no address page, and no deployment address surf |
| 113 | 2023-08-dopex | 4 | 0/4 | Code4rena 2023-08 Dopex V2 (RdpxV2Core, PerpetualAtlanticVault/LP, ReLP). Dopex has rebranded to Stryke; docs.dopex.io redirects to docs.stryke.xyz, whose deployed-address page covers only the newer CLAMM, the old-contra |
| 114 | 2024-10-coded-estate | 4 | 0/4 | CosmWasm (Rust) marketplace deployed on Nibiru (cataclysm-1, EVM chain id 6900); no contract/deployment address is published in the report, docs or the site bundle. Report states Nibiru is the deployment chain. |
| 115 | Acala | 4 | 0/4 | The audited code is a Rust Substrate pallet (incentives/rewards: transfer_share_and_rewards, share/reward-debt accounting) compiled into the Acala parachain (para 2000) runtime. There is no deployed contract address to t |
| 116 | Derby | 4 | 0/4 | The report's addresses are dependency tokens, not Derby contracts: 0x5274891b… is IdleUSDC (Yield), 0xbe1a001f… is Beta Finance, 0xcddb1bce… is IdleTokenV3 and 0xa0b86991… is USDC. The Sherlock contest repo ships only Go |
| 117 | Hyperware DAO | 4 | 0/4 | Cantina review dated 2025-07-23 of HyperAccountMultisig/HyperGovernorToken/TokenRegistry/HyperAccountMinter. No deployment addresses in the report, no contracts page on hyperware.xyz (a marketing site only), no matching  |
| 118 | IXO Protocol V1 | 4 | 0/4 | Fuzzland audit (2024-08) of IXO Protocol V1; scope is Solidity (SettlementExcutor.sol, SwapService.sol) with pool/guarantor/invest functions. ixo.world is the Cosmos-based IXO impact platform and does not describe this p |
| 119 | Joyn contest | 4 | 0/4 | Code4rena contest (2022-03) for Joyn, an NFT launchpad/marketplace. The findings repo is a contest scaffold with no deployment manifest, joyn.xyz and joyn.co no longer resolve, and no explorer or DefiLlama record ties a  |
| 120 | Nori-1 | 4 | 0/4 | Nori's LockedNORI/RestrictedNORI deployment was not locatable: no address in the 0xmacro report, no Blockscout match for either contract name, and DefiLlama has no Nori protocol entry. |
| 121 | Octopus | 4 | 0/4 | Audited code is NEAR Rust contracts (ft_on_transfer, slash_request, handle_anchor_deposit_reward_msg); NEAR account IDs are not published. DefiLlama's 'Octopus Finance' Arbitrum address 0x057153eb... is an unrelated DEX  |
| 122 | Primitive (ethereum-evm-primitive) | 4 | 0/4 | Primitive RMM (rmm-core / rmm-manager). Repos contain no mainnet deployment manifest (only echidna localhost addresses); docs.primitive.finance and primitive.xyz return HTTP 402 and DefiLlama lists Primitive on Ethereum  |
| 123 | RealWagmi | 4 | 0/4 | Two Sherlock contests (2023) on pre-deployment code. No DefiLlama listing, no docs/deployments page; only a third-party fork repo (seerether/RealWagmi) exists. No live deployment surfaced. |
| 124 | STND Smart | 4 | 0/4 | BlockSec review of STND CDP/FeeRoll contracts. stnd.tools and docs.stnd.tools do not resolve; no deployments page, address book or explorer hit found for the CDP or FeeRoll contracts. |
| 125 | StakerDao wAlgo | 4 | 0/4 | 2020 Trail of Bits review of StakerDao wALGO (Algorand TEAL). Timeboxed: one indexer lookup for an ASA named wALGO returned nothing and the report excerpt carries no application ID; recorded NOT_FOUND rather than guessin |
| 126 | TerminalFi - Scope 1 | 4 | 0/4 | BailSec report covers Terminal Finance DEX on Base. No deployment table or verified TerminalFi contract found; Base Blockscout search is Cloudflare-blocked and no address is published in the report text. |
| 127 | Terrace | 4 | 0/4 | Sherlock review of Terrace's Maradona router. No report URL/body and no deployment manifest; web search resolves only an unrelated traditional-finance company (terracefinance.com), so no address was recorded. |
| 128 | Unstoppable | 4 | 0/4 | Sherlock 2023-07 review of an unnamed deployment; no chain, repo or address in the corpus entry, and DefiLlama returns no matching protocol. |
| 129 | structured-cosmwasm-and | 4 | 0/4 | Non-EVM (CosmWasm/Solana) codebase; no deployment identifier available from the report or a public page within budget. |
| 130 | veRWA | 4 | 0/4 | Code4rena 2023-08-verwa contest repository only; there is no evidence the contracts were ever deployed, and no docs or deployments page exists. |
| 131 | 2022-05-10-codex-cdex-codex-on-althash-llc-sca-cod | 3 | 3/0 | Codex/CDEX staking; no address published in the audit. |
| 132 | 2025-06-18-sigmaprime-botanix-sigma-prime-botanix- | 3 | 3/0 | Botanix mainnet is chainId 3637, but no contract address was located; chain left out rather than guessed. |
| 133 | Compeঞঞve | 3 | 3/0 | Secure3 audit contest of Lymex (LymSignPool, Incubator, Compeve swap). No public contract address, docs page or repo was found; the audit repo only carries the PDF. |
| 134 | Ethereum Foundation BLS Wallet | 3 | 3/0 | contracts/networks/ contains only arbitrum-goerli.json and optimism-goerli.json; the project was never deployed to mainnet, so there is no live address to trace. |
| 135 | Fluid | 3 | 3/0 | This is Fluid Protocol on Fuel (Sway contracts in Hydrogen-Labs/fluid-protocol, audited by Zenith), not Instadapp Fluid. Fuel contract IDs (0x + 64 hex) are not published in the repo README, deploy scripts reference a gi |
| 136 | Honey | 3 | 3/0 | OtterSec audit (2022) of Honey Finance on Solana. The report page carries no program id, the honey-sdk IDL has no metadata.address, and the legacy frontend reads program ids from env vars. No program id could be verified |
| 137 | Kinetic | 3 | 3/0 | Oak Security 2022-04-07 review of a Rust/CosmWasm Kinetic (contracts/core/phaser, vault, UST accounting); the report leaves the chain unknown. The DefiLlama 'Kinetic' candidate is the Flare lending market (kinetic.market |
| 138 | Mayan TON | 3 | 3/0 | OtterSec review of Mayan's TON funC contracts (fc_contracts/c_order.fc). Current Mayan docs list EVM, Solana and Sui deployments only; TON is not a supported chain and no TON address is published. The EVM Forwarder 0x337 |
| 139 | Neon - May 13, 2021 | 3 | 3/0 | 2021 Solidified audit of an ERC1155 NFT auction. The report names only Auction.sol; no protocol site, repo or deployment address surfaced within the timebox. |
| 140 | Penumbra | 3 | 3/0 | Cosmos appchain; the audited dummy-spend/delegation/position logic is node (Rust) code, not a deployable EVM contract. No contract address exists to record. |
| 141 | Public - Runnow Smartcontracts | 3 | 3/0 | Runnow smart contracts (Verichains 2022). The report names Marketplace/MarketplaceV2 but gives no chain or deployment address, and no live project site was found. |
| 142 | Sharwa Finance | 3 | 3/0 | DefiLlama lists Sharwa.Finance on Arbitrum but carries no address; docs.sharwa.finance does not resolve and the site exposes no contracts/deployments page or docs link. LiquidityPool / option-NFT addresses not located. |
| 143 | Sharwa Finance | 3 | 3/0 | Pashov review (2024-07) of Sharwa Finance (Arbitrum). The review markdown contains no addresses; sharwa.finance serves a landing page with no addresses; docs.sharwa.finance and app.sharwa.finance do not resolve; Arbiscan |
| 144 | firm-parifi | 3 | 3/0 | Parifi is Arbitrum-based per comments in the report scope; project announced wind-down, which also hampers docs discovery. |
| 145 | smart contract ecosystem | 3 | 3/0 | This batch unit is a merge of two different protocols (Blueprint Finance Blueprint Hub audit and Bonzo Finance Hedera audit), so a single deployment mapping is not meaningful; nothing was resolved for either within budge |
| 146 | Abacus | 3 | 2/1 | The batch mixes two unrelated 2022 codebases both labelled Abacus: a Hyperlane-lineage messaging protocol (Hacken; Inbox/AbacusConnectionManager) and an NFT-lending protocol (OtterSec; Lend.sol/NftEth). Neither has a pub |
| 147 | Bloom Trading | 3 | 2/1 | Zellic report section 6 states the reviewed code was not deployed to Blast L2 mainnet at assessment time (2024-02-22). DefiLlama lists a Bloom Trading deployment on Blast with TVL from 2024-03-29 (~$10-14M), but publishe |
| 148 | Capricorn Exchange pAMM | 3 | 2/1 | Cantina Oct-2025 review of the Capricorn pAMM (Monad). Identity confirmed via capricorn.exchange/DefiLlama; no address surfaced within the timebox. |
| 149 | CronCat CosmWasm | 3 | 2/1 | CronCat is a CosmWasm automation network; docs.cron.cat and cron.cat did not resolve to the project. No tasks/manager contract address on Neutron or NEAR was located. |
| 150 | DRAFT FOR REVIEW ONLY | 3 | 2/1 | Report is sec3's 'DRAFT FOR REVIEW ONLY' Kamino assessment (Solana). It names no program id, and a Solana program id is not an EVM address; recorded NOT_FOUND rather than guessing Kamino's lending program. |
| 151 | FortyTwo | 3 | 2/1 | Audit names only Autocompounder/proxy components; no deployment could be tied to the project. |
| 152 | GTE | 3 | 2/1 | Zellic 2025 reviews of GTE CLOB and Launchpad on MegaETH. No GTE deployment addresses are published; MegaETH docs list only chain-level core contracts, and public material describes GTE mainnet deployment as pending. |
| 153 | GoMarket June17 | 3 | 2/1 | Zokyo review of a Solana Anchor program (create_parlay.rs, void_parlay/claim_parlay, singleton config PDA). gomarket.xyz returns a 114-byte stub; no docs, repo or program ID found. Program ID not recorded rather than gue |
| 154 | HotCurves | 3 | 2/1 | Three Sigma 2025 review of HotCurves (bonding-curve launchpad, pool finalization/migration). No docs deployments page and no explorer label for a HotCurves contract surfaced; a Base 'HOT Bridge' hit is an unrelated proje |
| 155 | Immutable on May 27th, 2020. | 3 | 2/1 | May-2020 Solidified review of an 'Immutable' Escrow contract; no project site, chain or address tie the code to a live deployment. |
| 156 | Ink Protocol | 3 | 2/1 | Oak Security 2021 review of Ink Protocol on Terra (Terra Classic, columbus-5). Ink's Terra contracts were wound down with the Terra collapse and no contract address for the staking or draw contract is published in the re |
| 157 | Maia DAO | 3 | 2/1 | DefiLlama's Maia entry is the MAIA token (0x00000000ea00F3F4000e7Ed5Ed91965b19f1009B) and was rejected. Docs are Cloudflare-gated; no BribesFactory, ERC4626PartnerManager or TalosStrategyStaked address recovered. |
| 158 | Mellow Finance | 3 | 2/1 | Cantina 2024 review of Core.sol/vault contracts. Current docs describe the 2026 Core Vault architecture; no address for the audited 2024 Core deployment surfaced (the DefiLlama registry 0xfd23... has no code on Ethereum) |
| 159 | NFTonPulse | 3 | 2/1 | No report URLs and no llama candidate in the batch; no public docs or explorer hit for NFTonPulse within the search budget. |
| 160 | Neutron | 3 | 2/1 | Informal Systems (2023) and Oak Security (2022) reviews of Neutron. All three findings are in Cosmos SDK / ibc-go modules of the chain (ibc-transfer, x/interchainqueries, x/gov) rather than standalone deployed contracts, |
| 161 | Neutron Slinky STD | 3 | 2/1 | Neutron/CosmWasm; addresses are bech32 contract hashes, none published in the audit. |
| 162 | Nord | 3 | 2/1 | The llama_candidates entry for this unit is Nord Finance (0x6e97.., the NORD ERC-20), which is a different protocol from the audited Layer N 'Nord' exchange, so that candidate was rejected as a dependency token of an unr |
| 163 | Orderly Omnichain | 3 | 2/1 | Guardian Audits 2024 review of Orderly's omnichain vesting/staking. Orderly's docs are a client-rendered Mintlify site with no extractable contract-address page and the report publishes no address; only the ORDER token ( |
| 164 | Rikard Hjort | 3 | 2/1 | Reviewer-name project entry; no protocol, chain or deployment could be attributed. |
| 165 | Router Chain 2 | 3 | 2/1 | Router Chain is a Cosmos app-chain; the audited ingress/ack handlers are chain modules, not EVM contracts, and no address was located. |
| 166 | RubiFi | 3 | 2/1 | Zenith/Code4rena 2025 RubiFi review. No report body, deployment list or resolvable project site/repo was available; the findings name Solidity libraries (DepositLib, WithdrawalLib, RubiFi.processRawAction) but no chain o |
| 167 | Slender | 3 | 2/1 | Stellar Soroban lending protocol (eq-lab/slender). The README contract ID CCLZ4QF5QSWBANABDZPC3XKHMVX3GUSLFLP4JS22SCIGLADD2E7STHDR belongs to the local quickstart integration test, not mainnet; no mainnet contract ID was |
| 168 | Sushi Swap BentoBox Strategies and Staking Contract | 3 | 2/1 | Sigma Prime 2022 review of sushiswap/bentobox-strategies and sushiswap/StakingContract. Both repos ship deploy scripts but no address book, and the commonly cited BentoBox address 0xF5BCE5077908a1b7370B9ae04AdC565EBd2437 |
| 169 | Talus IAO | 3 | 2/1 | Zenith/Code4rena audit of the Talus IAO Move modules (bonding_curve, iao::register_asset, liquidity_pool). docs.talus.network covers the Nexus agent framework, not IAO package ids; no Sui package address surfaced. |
| 170 | Tornado Launcher | 3 | 2/1 | Zenith audit of a bonding-curve launchpad (2024-06-20). No llama candidate, no report addresses, and one search returned no project site, docs or deployment record; the reviewed code does not appear to be publicly deploy |
| 171 | Valdora | 3 | 2/1 | Oak Security audit of Valdora CosmWasm staking on ZIGChain. The docs Smart Contracts page renders client-side and exposes no contract address; ZIGChain addresses are bech32 zig1... and none were recoverable. |
| 172 | xToken | 3 | 2/1 | ABDK audits of the xToken terminal (2021/2022). DefiLlama only carries the XTK token (0x7f3edcdd180dbe4819bd98fee8929b5cedb3adeb); terminal/proxy and LiquidityPool addresses are not in docs and the xtokenmarket repos car |
| 173 | AbracadabraMoney PurrSwap Balancer Aggregator | 3 | 1/2 | PurrSwap deployment could not be located; likely Berachain but the chain was not confirmed. |
| 174 | Astrolab | 3 | 1/2 | Astrolab (Arbitrum yield protocol). Docs site is JS-rendered and exposes no contract/address page; Arbitrum explorer search was blocked this run, so no address confirmed. |
| 175 | Bancor V2 AMM | 3 | 1/2 | No address recorded: the audit predates the V2 AMM deployment and the report names no instance. V3 core (MasterVault 0x649765821D9f64198c905eC0B2B037a4a52Bc373) is a different architecture and was deliberately not substi |
| 176 | Calculated Finance | 3 | 1/2 | Oak Security 2023 audit of Calculated Finance's CosmWasm DCA contract. The app is listed on Osmosis (app.osmosis.zone), but no osmo1... contract address is published in the report or docs surfaced, so nothing was mapped. |
| 177 | Casper Association | 3 | 1/2 | Casper Network uses contract hashes, not EVM addresses; none recoverable from the report. |
| 178 | Cosmos SDK V2 | 3 | 1/2 | Cosmos SDK is chain framework code, not an EVM deployment: the findings live in x/auth and distribution/staking modules compiled into each chain. No contract address exists; Cosmos Hub (cosmoshub-4) is named only as the  |
| 179 | DELIGHT LABS - STARFLEIT | 3 | 1/2 | Chainlight audit of a Solana-style AMM (Rust entry points). No program id, repo or deployment page surfaced; the audit PDF is the only artifact. |
| 180 | DXdao ERC20Guild | 3 | 1/2 | Sigma Prime 2022 review of DXdao's ERC20Guild. The repo DXdao/erc20guild is no longer public, DXdao has wound down its front ends, and neither the report nor the explorer name search returned a guild address, so nothing  |
| 181 | DaosLive | 3 | 1/2 | Shieldify review of DaosLive/DaoVesting/DaosLocker, which custody Uniswap V3 positions. daos.live does not resolve and no deployments page or address book was found; the audit report itself gives no deployed addresses. |
| 182 | Dezswap | 3 | 1/2 | Dezswap is a CosmWasm DEX on XPLA; contract addresses are bech32 xpla1... and none surfaced from the audit PDF path or docs landing page. |
| 183 | Divergence Protocol | 3 | 1/2 | MixBytes 2023 review of a volatility-derivatives protocol; no docs/deployments page or explorer hit found within budget. |
| 184 | Forgotten Playground Security | 3 | 1/2 | Forgotten Playland (FP token on Ethereum) reviewed by Pashov; the ToyBox sale contract address is not published in the report or docs. |
| 185 | Kresko Labs Pte. Ltd - January 12, 2024 | 3 | 1/2 | Solidified 2024 review of Kresko's vault/anchor contracts. The public repo targets Arbitrum (configs/foundry/deploy/arbitrum) but contains no deployed address book, docs.kresko.fi did not resolve, and no anchor/vault add |
| 186 | Lumiterra Community Contracts | 3 | 1/2 | Lumiterra community contracts are on Ronin (chain id 2020). Only a token address (LUDAMOON) is publicly documented, which is not the audited VAMM. |
| 187 | Melonport. June 8, 2018. | 3 | 1/2 | Solidified 2018 audit of Melon Protocol v1 (CanonicalPriceFeed, quantityHeldInCustodyOfExchange). Melon v1 was superseded by Enzyme; no v1 core address is published in the report and the 2018 deployment is not labelled o |
| 188 | Money Mates Halborn | 3 | 1/2 | Halborn reviewed contracts/MoneyMates.sol for a zkSync Era deployment (DefiLlama lists the chain). No verified MoneyMates contract or docs address was found. |
| 189 | Orion - Liquidity Aggregator Smart Contract Security | 3 | 1/2 | Orion Protocol's exchange/aggregator. DefiLlama only exposes the ORN token (0x0258f4..), which is a token, not the Exchange contract, so it was rejected. |
| 190 | Pods Finance Ethereum Volatility Vault | 3 | 1/2 | Docs site is live but the contracts page paths tried (contracts, developers/contracts, deployments) all 404, and the vault is enumerated only through a subgraph in the DefiLlama adapter. No vault address asserted. |
| 191 | Pudgy Daos | 3 | 1/2 | Chains field in the report is 'unknown' (Cairo/Rust/Solidity/Vyper mix). No website, docs, GitHub or explorer hit for DaosLive/DaosLocker/DaosVesting on Ethereum, Base or Scroll. |
| 192 | UltiBets 1 | 3 | 1/2 | UltiBets (Guardian audit) exposes only a marketing site; no docs deployment page and no addresses in the report, and the chain is not stated in the extracted text. |
| 193 | Umami GMX PositionManager | 3 | 1/2 | Guardian Audits 2025 review of Umami's GMX V2 position manager. docs.umami.finance/contract-addresses lists only tokens, multisigs and the deprecated v1 vault - no PositionManager/GMI contract. DefiLlama/Coinbase 0x1622b |
| 194 | Valkyrie Protocol CosmWasm Smart Contract | 3 | 1/2 | Terra/CosmWasm deployment; DefiLlama lists only the VALKYRIE token (terra1dy9k..), which is a token, not the audited campaign contract, so it was rejected and no address recorded. |
| 195 | Zer0 - zAuction | 3 | 1/2 | Zer0 zNS/zAuction audit (2021). No public deployment address surfaced; Zer0 was a zk-rollup side chain whose zNS/zBanc contracts are not indexed on Ethereum explorers. |
| 196 | pashov-team-2024-03-06-tapiocadao-security-review | 3 | 1/2 | Pashov review of Tapioca DAO's Seer oracle, market read() scaling and StargateLbpHelper. Tapioca deploys many per-market contracts and the docs' llms.txt has no deployments page; no Seer/StargateLbpHelper address surface |
| 197 | re | 3 | 1/2 | The audited code is a Liquity-V2-style Bold market ('Soneta') reviewed by Three Sigma. Re's published stablecoin deployments (reUSD 0x4691.., per DefiLlama) are a different product line, so they were not used as a substi |
| 198 | 2021-04-ethereum-evm-advancedblockchain | 3 | 0/3 | No project website, repo, chain or deployment surfaced; the unit is a generic EVM/DeFi course exercise audited in 2021-04. |
| 199 | 2022-12-tessera | 3 | 0/3 | 2022-12 Code4rena contest for Tessera's GroupBuy/OptimisticListingSeaport. The audit repo carries no address book; name-matching GroupBuy contracts on Ethereum were inspected and rejected as a different project (differen |
| 200 | 2023-07-03-final-symmetrical-audit-report | 3 | 0/3 | Sherlock 2023-06 Symmetrical contest code; no deployment address could be confirmed within the timebox. |
| 201 | 2023-11-06-steadefi | 3 | 0/3 | Steadefi's documented address source (api.steadefi.com/vaults and /lending-pools) is suspended, and the DefiLlama adapter depends on that same API, so no vault address could be evidenced; recorded NOT_FOUND rather than r |
| 202 | 2024-01-08-incentive-contracts | 3 | 0/3 | Batch entry has no report_urls and no body; the project name is a generic 'incentive contracts' label. No identity could be resolved. |
| 203 | 2024-03-25-nemeos-d98ae938 | 3 | 0/3 | Nemeos is a Solana token-financing protocol (nemeos.finance, github.com/nemeos). The repo's Anchor.toml declares only devnet/localnet program ids, so no mainnet address is recorded. Finding text is Solidity-flavoured (ER |
| 204 | 2024-05-ethereum-evm-wonderland-prophet-securityreview | 3 | 0/3 | Wonderland Prophet (prediction market) review; no deployment address or deployment table surfaced for Prophet/BondEscalationAccounting. |
| 205 | 2024-08-23-devolvedai-l1-argochain-argochain-bridge-amm-jun2024-l1-arg | 3 | 0/3 | DevolvedAI's Argochain is a Substrate L1; the bridge/AMM review targets pallet and runtime code (F-2024-4290/4277/4295), which has no contract address. |
| 206 | AZTEC | 3 | 0/3 | Trail of Bits 2019 review of AZTEC v1 on Ethereum. AZTEC v1 contracts were superseded by Aztec Connect and later the zk rollup; no live v1 address is recorded. |
| 207 | Atoshi | 3 | 0/3 | BlockSec 2026 reviews of the Atoshi privacy circuits and Shield contracts. Atoshi is a privacy L1 (atoshi.io does not resolve) and no Shield deployment address is published in the report or elsewhere reachable. The DefiL |
| 208 | Badger Citadel contest | 3 | 0/3 | Citadel-DAO/citadel-contracts has no address book. Blockscout indexes five verified StakedCitadel contracts (0xEc3dF2f7C76D664C49c0B88B9F15C2ce385A5E69, 0x56f0EAAB23Edb3f74e463C236Fc6b9e859EDd338, 0x7e0cD8A2D2BF0e1d3C3B5 |
| 209 | Bima | 3 | 0/3 | BIMA's official docs state that canonical contract addresses are 'coming soon' and will be published per monthly vault, so no address is verifiable yet. DefiLlama lists deployments on Bitcoin, Ethereum, Hemi, CORE, Sonic |
| 210 | Bonder | 3 | 0/3 | Zenith 2025 audit of Bonder (BonderV1Pair). No deployment address is published in the report or reachable docs; no explorer tag for the protocol was found. |
| 211 | Cally contest | 3 | 0/3 | The report's only addresses (0xE41d2489571d322189246DaFA5ebDe1F4699F498) are the ZRX token, a dependency, and were rejected. The repo README documents only a Rinkeby testnet deployment (0xfccf...921f); no Ethereum mainne |
| 212 | Concur Finance contest | 3 | 0/3 | 2022-02 Code4rena contest. Two searches (Ethereum contract-name search, web search) produced no attributable deployment; recorded NOT_FOUND. |
| 213 | European project for DLT financing for SME digitalization to overcome  | 3 | 0/3 | CODESPECT review of a research project (smart-account validators). No chain deployment or address appears in the report, and no protocol identity is resolvable. |
| 214 | FIAT I | 3 | 0/3 | FIAT DAO's FDT token is a different protocol; not mapped. |
| 215 | Gauntlet | 3 | 0/3 | The two 2022 Spearbit findings are against Aera Vault V1 (AeraVaultV1.sol, PermissiveWithdrawalValidator.sol); the 2025 Cantina finding is against Gauntlet's slippage hooks (src/periphery/hooks/slippage/BaseSlippageHooks |
| 216 | HertzFlow | 3 | 0/3 | HertzFlow is a self-custodial RFQ perpetuals DEX on BNB Chain (DefiLlama and RootData both place it 100% on BSC). Its site publishes no contract table and docs.hertzflow.xyz does not resolve; keyless BscScan contract sea |
| 217 | Ichi - Vaults | 3 | 0/3 | ICHI oneToken vaults are per-strategy deployments across ~27 chains (DefiLlama); no canonical single vault address applies and none was confirmed for this audit. |
| 218 | Lair Finance | 3 | 0/3 | The Halborn review covers Berachain LRT contracts (LairBGTManager). The only llama_candidate is 0xd70c7d511560493c79df607076fb863f5c8a50b0 on Klaytn, the Lair token, not the audited manager; no LairBGTManager deployment  |
| 219 | Lattica | 3 | 0/3 | Zenith Security 2026 audit of Lattica (lending/leverage). The extract contains no chain, repo or deployment reference and no public deployment surfaced within budget; probably pre-launch. |
| 220 | NextGen | 3 | 0/3 | Candidates seen on Ethereum Blockscout: NextGenCore 0x4EC94b7f01f7B5F6085933e742123c315865478a, 0x2c8FdCeD22B28e13f1a472cf7f19e2f56C204c83, 0xC3390e3D2e98544DcBB6f235a3B15345A6728E8c, 0xf7669258832241a6BCE4DDEfcB120141ee |
| 221 | Nouns Builder contest | 3 | 0/3 | Nouns Builder deploys a fresh Token/Auction/Governor/Treasury set per DAO from implementation templates; no canonical single deployment is published in the repo or docs reached. |
| 222 | Olas | 3 | 0/3 | OLAS on Gnosis is known (0xcE11e14225575945b8E6Dc0D4F2dD4C570f79d9f) but GnosisTargetDispenserL2 is not listed in Olas docs and gnosisscan search is Cloudflare-gated in this environment; no dispenser address was confirme |
| 223 | Particle Protocol - Invitational | 3 | 0/3 | Code4rena 2023-05 Particle invitational; the repo/contracts are known (LienToken/Escrow) but no mainnet deployment address surfaced. |
| 224 | Pie.Fun | 3 | 0/3 | Pie.Fun is a Solana basket protocol reviewed by Code4rena Zenith. No program id, repository or docs address table was found in the timebox. |
| 225 | Polynomial Power Perp Contracts Audit | 3 | 0/3 | docs.polynomial.fi and polynomial.finance are JS SPAs; neither renders a deployments/contracts page through curl or a reader, and no explorer name match for the power-perp contracts. No address and no chain asserted. |
| 226 | Polynomial Protocol contest | 3 | 0/3 | The 2023 KangarooVault lived on Optimism and is not published in current docs; current docs list only the new Polynomial Chain PerpsMarketProxy (0xD052Fa8b2af8Ed81C764D5d81cCf2725B2148688), a different deployment. Not us |
| 227 | Proof of Play / Pirate Nation | 3 | 0/3 | Proof of Play shut down and open-sourced its contracts; deployed Ronin addresses were not located. |
| 228 | Reality Cards | 3 | 0/3 | Repo RealityCards/RealityCards-Contracts found, but migrations/2_deploy_contracts.js only hardcodes third-party addresses. Project announced hibernation on X, site returns 530. No explorer/name hit within budget; recorde |
| 229 | Rhinestone Smartsessions Core | 3 | 0/3 | Cantina's Aug-2024 review of SmartSessions v1 (SmartSession.sol). The repo publishes ABI/bytecode artifacts but no deployment table, and the module is installed per account and chain; no canonical SmartSession address co |
| 230 | Rigor Protocol contest | 3 | 0/3 | 2022-08 Code4rena contest for a pre-launch construction-finance protocol. Two searches (DefiLlama protocol lookup, Ethereum contract-name search) produced no deployment; recorded NOT_FOUND. |
| 231 | SevenSeas-29 | 3 | 0/3 | Three Macro reviews (sevenSeas-2, -18, -29) of Seven Seas' BoringVault-based vaults. Seven Seas is not on DefiLlama and its vault addresses are per-vault; none were attributable in the timebox. |
| 232 | SuiPad | 3 | 0/3 | Sui Move launchpad. Searches returned only price/tokenomics pages (CoinMarketCap, Coinbase, CryptoRank); no Sui package id or campaign object id was published in the sources reachable in budget. |
| 233 | Sujith Somraaj | 3 | 0/3 | Batch entry is named after the auditor, not a protocol; the three findings reference LibPerpsMigration, TokenManager and swapExactIn but the entry carries no report URL, body, chain or deployment list. No protocol could  |
| 234 | Tessera - Versus contest | 3 | 0/3 | Versus/Code4rena Tessera contest (same repo as 2022-12-tessera). No deployment addresses in the audit repo and no on-chain match for GroupBuy or OptimisticListingSeaport attributable to Tessera. |
| 235 | Tezoro | 3 | 0/3 | No address for any of the three findings. |
| 236 | Tracer Perpetual Pools V2 Contract | 3 | 0/3 | Runtime Verification 2021 review of Tracer Perpetual Pools V2; contracts deployed on Arbitrum but addresses are not in the report extract. |
| 237 | VVET Protocol | 3 | 0/3 | Zenith (code4rena-zenith) audit; no chain or deployment address disclosed. |
| 238 | aqualis 2024 12 aqualis code review smart contract | 3 | 0/3 | Hashlock audit page confirmed (hashlock.com/audits/aqualis), but the project's site is dead and no chain/explorer evidence of an AqualisSP deployment surfaced. |
| 239 | computable | 3 | 0/3 | 2019 Trail of Bits review of Computable's market / voting / listing-fee contracts. No live deployment, docs page or explorer entry attributable to Computable was found; a 2019-era deployment may be dormant. Nothing probe |
| 240 | for Fuel | 3 | 0/3 | The audited deployment is on Fuel (non-EVM); no contract id or program address appears in the Hexens report extract, and an EVM address would be wrong to record. |
| 241 | real wagmi | 3 | 0/3 | Identity confirmed: wagmi.com is Real Wagmi (footer links t.me/realwagmi, github.com/RealWagmi); the project has since merged with Anon. Sherlock report names repository RealWagmi/concentrator (contracts/Multipool.sol) a |
| 242 | smart contracts | 3 | 0/3 | Cantina report 2024-03-19-smart-contracts (client/project field empty in the HF corpus, no report URL). Findings reference Controller.sol, Voting.sol, LLido, PoolFactory and tokens DCT/GOAT; no deployed address or chain  |
| 243 | solana foundation multi delegator | 3 | 0/3 | Solana Foundation subscription / multi-delegation program (plans, subscribers, merchant-pulled recurring transfers). No public repo, docs page or explorer entry publishes the program ID, and the report carries no address |
| 244 | spartan-council | 3 | 0/3 | iosiro reviewed the Synthetix 'Shaula' release (Collateral/ShortingRewards). No per-contract address is given and Synthetix deployments are proxies across Optimism/Base/Ethereum, so no address is attributed. |
| 245 | 2021-09-10-gamico-sca-gamico-erc20-liquidity-provi | 2 | 2/0 | A 2021 audit of an ERC20 liquidity-provider token with no project identity, chain or deployment in the source material. |
| 246 | 2022-05-18-fidometa-sca-fidometa-erc20-may2022-sca | 2 | 2/0 | Token-level audit with no deployment information. |
| 247 | 2023-06-19-dexe-network-sca-dexe-dex-mar2023-sca-d | 2 | 2/0 | Hacken 2023 audit of DeXe DEX pricing (PriceFeed.getAmountsOut over a Uniswap pair). Only the DeXe governance token 0xde4EE8057785A7e8e800Db58F9784845A5C2Cbd6 surfaced, which is not the audited pricing/DEX contract; no p |
| 248 | 2023-07-22-govworld-sca-govworld-lending-platform- | 2 | 2/0 | GovWorld lending platform (BSC-era). No docs deployment page or explorer hit surfaced for the lending pool/PriceFeed. |
| 249 | 2023-12-05-betswap-gg-sca-betswap-gg-erc20-dec2023 | 2 | 2/0 | Unit has no report_urls/body/source_url. The BSGG token trades on Avalanche (0x63682bdc5f875e9bf69e201550658492c9763f89) but is not confirmed to be the audited ERC20 implementation, so no address is asserted. |
| 250 | 2023-12-19-paid-network-sca-paid-network-ido-vesti | 2 | 2/0 | Batch entry has no report_url, body or source_url (SCA engagement 2023-12-19, Paid Network IDO vesting). With no report text there is no contract name beyond withdrawPurchasedAmount and no address list; no published Paid |
| 251 | 2024-04-29-sigmaprime-dxdao-erc20-guild-review | 2 | 2/0 | Implementation review; no deployed guild address published. |
| 252 | 2025-07-23-sigmaprime-risc-zero-sigma-prime-risc-zero-the-signal-ether | 2 | 2/0 | Sigma Prime assessment of the RISC Zero 'Signal' Ethereum attestation verifier. No deployed verifier address is published for this component and nothing surfaced in docs or explorers. |
| 253 | Aqueduct | 2 | 2/0 | Decurity TWAAM audit (2023-08-10) of AqueductV1Auction; the report carries no deployment addresses and states the chain as unknown. aqueduct.fi does not resolve and no project repo/address book surfaced in two searches,  |
| 254 | Archisinal Marketplace | 2 | 2/0 | Oak Security audit of an ink! (Substrate) marketplace (currency.rs, auction/mod.rs). ink! contracts are instantiated per deployment and no code hash or address is published; the GitHub org only has onboarding/brand repos |
| 255 | Argo | 2 | 2/0 | OtterSec 2022 audit is of Aptos Move modules (meter_capability, argo_liquidate), not the Cronos liquid-staking protocol of the same name. The DefiLlama Cronos hit 0x47a9...89aa is the ARGO token and was rejected. No Move |
| 256 | BLS Wallet | 2 | 2/0 | Repo only ships optimism-goerli and arbitrum-goerli network manifests; no mainnet VerificationGateway address confirmed. |
| 257 | Bearcave | 2 | 2/0 | Explorer name search returns multiple HoneyJar/HJ4/HJ6 contracts with no version matching the audited release. |
| 258 | Bitcorn OFT | 2 | 2/0 | Cantina November-2024 review of the Bitcorn (Corn) OFT. Only the PDF is public; no docs deployment page or GitHub address book surfaced within the timebox. |
| 259 | Blockstreet | 2 | 2/0 | Halborn 2025 review of Blockstreet's Solana Anchor program. The report and public repos publish no program ID or deployment manifest, so no address was recorded. |
| 260 | Bullet Bullet Exchange | 2 | 2/0 | Sigma Prime 2025 review of a Rust perpetual exchange built on a sovereign rollup (paths code/sov-rollup, crates/exchange, perp_ledger.rs). The docs site is live but publishes no contract/account addresses and the chain h |
| 261 | Canopy | 2 | 2/0 | Canopy runs on Movement, a MoveVM chain; the audited modules are Move resources with no EVM contract address. DefiLlama lists the protocol with a null address. |
| 262 | Catalyst | 2 | 2/0 | The Pashov December-2023 review covers IPSeed (ERC1155 bonding-curve launchpad), not the cross-chain bridge listed by DefiLlama as 'Catalyst' (catalyst.exchange). No IPSeed deployment address or repo surfaced, so the Def |
| 263 | Chiliz - Bridge Updates | 2 | 2/0 | Halborn audit of the Chiliz bridge deposit path. The bridge is a PoS-bridge fork deployed on Chiliz Chain plus Ethereum; docs.chiliz.com has no contract-addresses page and no explorer hit for the deposit contract. |
| 264 | Circuit DAO | 2 | 2/0 | Chia protocol (DefiLlama lists Circuit on Chia). Contracts are Chia puzzles addressed by 32-byte puzzle hashes, not EVM addresses; the Zellic report names 'savings vault' and 'statutes mutation' puzzles but publishes no  |
| 265 | Coinbase: Kona | 2 | 2/0 | Kona is the Rust fault-proof program (op-rs/kona) used by OP Stack clients; the audited code is offchain (trace extension, TipCursor) and has no project-specific deployed contract. The on-chain FaultDisputeGame belongs t |
| 266 | Common Wealth smart contracts | 2 | 2/0 | The audit repo hackenproof-public/commonwealth-contracts publishes constants/addresses.json (Base chain id 8453) and lists WhitelistedVesting.sol in scope, but addresses.json contains no WhitelistedVesting entry and the  |
| 267 | Conduit | 2 | 2/0 | ABDK 2021 audit ABDK_Framework_Conduit_Solidity.pdf (Solidity 'Conduit' framework with ecrecover/sequence-number verification). No repo or deployment page is referenced by the report and the name collides with the rollup |
| 268 | DAO DAO Rewards Distributor, | 2 | 2/0 | Oak Security review of the DAO DAO rewards-distributor CosmWasm contract. DAO DAO deploys a fresh contract instance per DAO on Neutron/Juno, so there is no single canonical address and none is published in the docs or th |
| 269 | DAOfi | 2 | 2/0 | ConsenSys Diligence 2021-02 review of DAOfi V1 (DAOfiV1Factory / DAOfiV1Router01). The repo only contains a deploy script that deploys a fresh factory, and no DAOfiV1Router01/DAOfiV1Factory contract name surfaced on Ethe |
| 270 | DeSyn LeverageStaking | 2 | 2/0 | SlowMist audit of DeSyn LeverageStaking. DeSyn deploys on many chains per DefiLlama but exposes no address; docs.desyn.io has no deployment page and Blockscout/Arbiscan had no LeverageStaking contract. |
| 271 | Diagonal - March 7, 2022 | 2 | 2/0 | Solidified 2022 audit of Diagonal's payment service; no live contract address located. |
| 272 | Du Bois Gold - May 7, 2021 | 2 | 2/0 | Two 2021 Solidified reports on GoldbarLogic.sol. No protocol site, repo or deployment address surfaced within the timebox. |
| 273 | Earning.Farm Phase5 | 2 | 2/0 | SlowMist audit; project deployment not resolvable from report text. |
| 274 | Earning.Farm v3 | 2 | 2/0 | SlowMist 2022 review of Earning.Farm v3 vaults. No deployment address in the report or reachable docs; BSC name searches only returned the unrelated Harvest FARM token. |
| 275 | Elys Network | 2 | 2/0 | Halborn 2024 reviews of the Elys Network chain. Findings concern collateral-decimals and reward accounting inside the chain/CosmWasm logic; the docs site served a Mintlify starter template with no contract or module addr |
| 276 | Ember | 2 | 2/0 | Pessimistic 2020 audit of an Ember SmartWallet/PriceOracle. Current ember.so is the Ember Vaults protocol (github ember-protocol/Ember-Vaults), whose contracts differ from the audited ones, so no address was mapped. |
| 277 | Enclave | 2 | 2/0 | Solana Anchor program; audit repo pashov/audits, no deployment manifest found. |
| 278 | Entangle.fi (GORPLES) | 2 | 2/0 | Halborn audits (2024) of two Solana programs, gorples_core and gorples-bridge. Entangle's docs publish EVM/UTS contract addresses but no GORPLES Solana program IDs, and neither report nor any docs page lists them. Progra |
| 279 | Frizzante Core Contracts | 2 | 2/0 | Oak Security 2025 audit of Frizzante core contracts (JoinDual router, sy-token share accounting). No docs, repo or explorer label found; GitHub name search returns unrelated 'frizzante' projects. |
| 280 | Hyperbeat Pay | 2 | 2/0 | Zellic 2025 audit of Hyperbeat Pay (ManagementAccount / operator settlement) on HyperEVM. Hyperbeat's labelled contracts on hyperevmscan (e.g. 'Hyperbeat: Staking Core' 0xCeaD893b162D38e714D82d06a7fe0b0dc3c38E0b, 'beHYPE |
| 281 | IxoSwap | 2 | 2/0 | Oak Security audits (2024-03-15 v1.0, 2024-09-13 v1.1) of the CosmWasm ixo-swap contract. The code lives in ixofoundation/ixo-contracts (ixo-swap/) but the repo carries no deployment manifest, and docs.ixo.world has no c |
| 282 | Jet Governance | 2 | 2/0 | OtterSec 2022 review of Jet Governance on Solana; the program id was not recoverable from public sources. |
| 283 | Juiced | 2 | 2/0 | OtterSec audit (2022-07-29) of 'Juiced'. No repo, docs or explorer footprint. DefiLlama's Juice Finance (Blast) is a different, later project and is deliberately not used. |
| 284 | L1 | 2 | 2/0 | The report label 'L1' is too generic to resolve to a protocol; no docs, repo or deployment surfaced. |
| 285 | Launchnodes-Lido-Impact-Staking | 2 | 2/0 | Oxorio audit (2024-12-13) of NGOLis/NGOLisFactory; report contains no deployment addresses. launchnodes.com describes Lido Impact Staking but exposes no dapp or contract link; the candidate front-end hosts (lis./app./sta |
| 286 | LayerZero TON | 2 | 2/0 | TON (FunC) deployment. No TON endpoint/channel address appears in the report or in the LayerZero deployed-contracts page (client-rendered, no TON row surfaced); TON has no name-searchable contract index in the tooling us |
| 287 | Lingo Token | 2 | 2/0 | Cantina review 2025-02-06 of a Solana Token-2022 program (LingoToken/AccountWhitelist). The only matching Lingo token on Solana (GWZGj6AM4pkWxQW6bifE6JChSRf2hEQFWFkYC4REaL7H, lingocoin.io) is Token-2022 with transferFeeC |
| 288 | Liquid Loot | 2 | 2/0 | Obsidian audit (2025-07) of LiquidLoot, a Solana NFT-lending program. No docs, repo or program id surfaced. |
| 289 | LlamaPayV2 | 2 | 2/0 | LlamaPayV2 deploys one LlamaPayV2Payer per payer with CREATE2 from LlamaPayV2Factory (repo src/LlamaPayV2Factory.sol), so there is no single audited deployment. No v2 factory or payer address is published: docs.llamapay. |
| 290 | MUD Audit | 2 | 2/0 | OpenZeppelin 2023 audit of the MUD framework (World/WorldRegistrationSystem). MUD is developer infrastructure deployed per-app; there is no canonical protocol deployment whose address could be recorded. |
| 291 | Mars Protocol Core Smart | 2 | 2/0 | Oak Security 2022 audit of Mars Protocol v1 core, which ran as CosmWasm contracts on Terra. Terra contracts use terra1... bech32 addresses; the v1 deployment is defunct and no contract address is published in the report  |
| 292 | Merkle Token Distributor | 2 | 2/0 | OtterSec review of Move modules md_create2 and merkle_distributor. Chain inferred as Aptos from Move idioms (init_module, #[event], named address @merkle_token_distributor); the report itself records chain as unknown. No |
| 293 | MoarCandy | 2 | 2/0 | Pashov audit of MoarCandy, a token launchpad. The only address in the audit text (0x60aE616a2155Ee3d9A68541Ba4544862310933d4) is the Trader Joe router, a dependency, so it is rejected as a core mapping. No MoarCandy cont |
| 294 | Movedrop L2 | 2 | 2/0 | OtterSec review of a Move-language L2 program (report text is generic on-chain-program language, no chain or deployment named). No website, repo or deployment reference in the extract. |
| 295 | Nimbora | 2 | 2/0 | Starknet (Cairo) deployment. The report publishes no addresses; docs.nimbora.io and nimbora.io did not resolve from this environment and no name-searchable EVM explorer exists for Starknet. |
| 296 | OB ReturnCabin | 2 | 2/0 | SlowMist 2024 review of an OB/ReturnCabin marketplace; no website, repo or explorer label located. |
| 297 | PAID Network (Master Ventures) | 2 | 2/0 | Code review of the PAID Network / Master Ventures IDO Pool. No docs, repo or explorer hit for the Pool contract; the project token is unrelated to the audited contract. |
| 298 | Pear-Vault-Offchain-Security-Review | 2 | 2/0 | Shieldify review of the Pear Protocol vault *offchain* service (API/privy signer). The finding is an offchain API flaw; no on-chain contract is named and no deployment address is published in the report. |
| 299 | Public - BrownFi AMM Smartcontracts | 2 | 2/0 | Verichains 2024 review of the BrownFi AMM Pair/Router. BrownFi V2/V3 is live on Linea, Base, BSC, Berachain, Arbitrum and others per DefiLlama, but the docs (brownfi.gitbook.io llms.txt) publish no deployments page and n |
| 300 | Public - Goen Smartcontracts | 2 | 2/0 | Goen is a BNB Chain yield vault (WBNB reward token). No BSC Blockscout is reachable and no VaultBase address surfaced in docs or report text. |
| 301 | Public - MAoE Smartcontracts | 2 | 2/0 | Verichains 2022 review of LuckyNFT.sol / BoxNFT.sol / NFTCollection.sol (BSC-style NFT blind boxes). No project website, repo or deployed address in the extract and no address surfaced, so nothing is recorded. |
| 302 | Public - Roseon Perpetual Exchange | 2 | 2/0 | Roseon perpetual exchange; chain (BSC/Polygon) not confirmed within budget. |
| 303 | Public - ShopNext Smartcontracts | 2 | 2/0 | Verichains review of a ShopNext NFT marketplace (Marketplace.sol). No deployments page, repo or explorer match for a ShopNext marketplace. |
| 304 | Pye | 2 | 2/0 | Zellic 2025 review of Pye, a Solana stake-account protocol. The docs describe products and audits but publish no program IDs, and the report contains no address, so nothing could be mapped. |
| 305 | Relay Protocol Oracle | 2 | 2/0 | Zellic 2026 review of the Relay Protocol Oracle: a reference implementation of an off-chain attestation service (Dockerized HTTP oracle) that reads chain events and signs deposit attestations. It is not a deployed on-cha |
| 306 | SFT | 2 | 2/0 | Pashov review of the SFT418 contracts; code matches CypherLabz/cyphermate_2024 (src/tokens/SFT418). The llama_candidate 'SFT Protocol' (Filecoin, 0xC5eA96Dd...) is an unrelated DePIN liquid-staking protocol and was rejec |
| 307 | SOTERIA | 2 | 2/0 | Unit name is the auditor, not the project: both reports are SEC3 reviews of UXD Protocol (sec3_uxd_3.0.1.pdf and sec3_invariant_report.pdf), a Solana program suite. UXD docs (llms-full) contain no program IDs and Solana  |
| 308 | Security Technology for Smart Contracts Immunefi | 2 | 2/0 | Dedaub audit (2021-07-16) of Immunefi's Distributor and VestingNFTReceiver contracts. The report names no addresses and no public deployment of either contract could be found (Immunefi's published on-chain presence is th |
| 309 | Serious | 2 | 2/0 | No Serious protocol deployment surfaced; name collides with unrelated projects. |
| 310 | Smithii | 2 | 2/0 | Halborn RECC audit (2025-08-04) of Smithii's Solana fundraise program. The report PoCs reference only Raydium CLMM (DRayAUgENGQBKVaX8owNhgzkEDyoHTGVEGHVJT1E9pfH), test mints and an attacker program - no fundraise program |
| 311 | TradableAudit (Tradable) | 2 | 2/0 | ThreeSigma Tradable audit; TradableStaking has no verified deployment under that name and no chain/address in the batch metadata. |
| 312 | Uranium3o8 Launchpad Smart Contract Security | 2 | 2/0 | Halborn 2023 audit of the Uranium3o8 launchpad (U3O8 RWA sale, oracle/limit logic). No chain is stated in the corpus extract and no deployment address or docs page surfaced inside budget. |
| 313 | Yeet | 2 | 2/0 | Chain identified as Berachain from the Immunefi audit-competition scope; no MoneyBrinter/StakeV2 address published. |
| 314 | ZAP April11 | 2 | 2/0 | No website or repo in the corpus entry; searches returned unrelated ZAP projects. |
| 315 | Zenrock Q1 2026 - Hush privacy | 2 | 2/0 | Informal Systems audit of the Zenrock Hush privacy module. It is a Cosmos SDK module inside the Zenrock chain, so no standalone contract address exists; DefiLlama only lists the Zenrock bridge on Solana/Bitcoin. |
| 316 | fathom-dao-reaudit | 2 | 2/0 | DefiLlama lists Fathom Lending/CDP on XDC but with an XDC-prefixed adapter id that is not a usable contract address for these findings. |
| 317 | giza-arma-system | 2 | 2/0 | GIZA token on Base (0x590830dfdf9a3f68afcdde2694773debdf267774) is a token, not the ARMA system. |
| 318 | made for gamers | 2 | 2/0 | Zokyo 2022 audit; project name too generic to resolve to a live deployment. |
| 319 | meld-staking-smart-contract-security | 2 | 2/0 | Non-EVM (Cardano). MELD ERC-20 on Ethereum (0x333000333b26ee30214b4af6419d9ab07a450400) is a bridged token, not the staking contract. |
| 320 | nolus-money-market | 2 | 2/0 | Non-EVM. Docs describe protocol architecture only, no deployments list within budget. |
| 321 | 2020-06-bancor-v2-amm-security-audit | 2 | 1/1 | Bancor v2 AMM (2020). Per-pool converters, no canonical deployment address confirmed; deliberately not guessed. |
| 322 | 2020-11-21-linkswap-linkswap | 2 | 1/1 | 2020 LinkSwap (YFL) on Ethereum. Blockscout surfaces LINKSWAP/LinkSwap LP tokens (LINKSWAP 0x3d5930C697f405303beeCcd870DeF46281E168C8) but not the LinkSwap exchange contract holding purchaseYfl, so no mapping was made. |
| 323 | 2020-11-bitbank | 2 | 1/1 | No report URL, body, website or repo in the corpus entry; nothing to trace. |
| 324 | 2023-03-ethereum-evm-primitive-securityreview | 2 | 1/1 | Review of an EVM primitive/solstat math library (slt sign handling, Solstat Gaussian bounds) used by Primitive Finance style contracts. This is library code, not a deployed protocol; no project-specific deployment addres |
| 325 | 2024-01-12-xpower-sca-xpower-erc20-erc1155-staking-dec2023-sca-xpower- | 2 | 1/1 | XPower (xpowermine.com) is an ERC-1155 staking/mining protocol; the site describes the NFT system but publishes no contract addresses and the audit text carries none. |
| 326 | 2025-06-18-sigmaprime-botanix-sigma-prime-botanix-macbeth-security-ass | 2 | 1/1 | Botanix is a Bitcoin L2; audited components are node/bridge protocol code, not a published EVM deployment. |
| 327 | Algofi | 2 | 1/1 | Algofi is Algorand-native (TEAL/PyTeal, app IDs rather than 0x addresses). Runtime Verification's 2021 report gives no app ID, and no Algofi lending app ID could be confirmed in the timebox. |
| 328 | Algofi Lending V2 | 2 | 1/1 | Algorand AVM protocol; EVM address tracing does not apply. |
| 329 | Alice Protocol Smart Contracts | 2 | 1/1 | Oak Security report names Alice Protocol contracts (anchor exchange rate, meta-transactions) but no chain or deployment address surfaced. |
| 330 | Alt | 2 | 1/1 | Hacken 2022 audit of 'Alt Platform' (ERC1155 sale, on-chain randomness + signature checks). No project site, repo or explorer label could be tied to this name; 'Alt' is too generic to resolve without guessing. |
| 331 | Ambit | 2 | 1/1 | Guardian 2023 audit of Ambit Finance (BNB Chain lending + loyalty rewards/snapshot). DefiLlama confirms the BNB Chain deployment but lists no address, and no BSC explorer API with name search was usable in budget; Ethere |
| 332 | AnyStake | 2 | 1/1 | No report URL or body available for this unit; project identity and chain could not be established, so no address. |
| 333 | Astrolab April23 ( ) upd | 2 | 1/1 | Hexens review of Astrolab (Crate.safeWithdraw/safeRedeem, bridgeFunds). The strats repo resolves deployments from an on-chain registry, so no fixed address is published. |
| 334 | Avail Cosmos and Backend | 2 | 1/1 | Avail is a Cosmos SDK app-chain; findings are in x/chainabstraction keeper handlers (RefundReq, CreateProtocolFees), which are runtime modules with no contract address. |
| 335 | Babylon-jan | 2 | 1/1 | Hexens 2023 review (NFT listings + ETH minting-pass reentrancy). The name collides with the Babylon Bitcoin-staking chain; the audited NFT marketplace's repo/deployment was not identified in budget. |
| 336 | BarterDAO Superposition | 2 | 1/1 | Mixbytes audit of BarterDAO Superposition; no deployment address, chain or address book located within budget. 'Superposition' on DefiLlama is an Aptos protocol and could not be tied to this report. |
| 337 | Basis | 2 | 1/1 | Basis (2018 algorithmic stablecoin) was wound down before launch; the audited SimpleShares contract has no live deployment. |
| 338 | Beefy UniswapV3 | 2 | 1/1 | Beefy docs publish BIFI/treasury addresses only. CLM strategies are per-vault EIP-1167 clones of one shared implementation (e.g. Arbitrum vault 0x195DE404648C4E9f8778816d1E31566272FBff6b reports strategy 0xd9e837816a486f |
| 339 | Beranames | 2 | 1/1 | Berachain name service; mainnet deployment addresses unpublished in the repo. |
| 340 | Catalysis Core Smart Contracts | 2 | 1/1 | Audit text quotes 0x66Ab900341C98de949EC31d11b3C4180743844F1, but eth_getCode on Base returns 0x for it, so it is not a live Base deployment. No other Catalysis address surfaced. |
| 341 | Catalysis Coverage Contracts | 2 | 1/1 | Sigma Prime audit of the coverage contracts; no address surfaced within the search budget. |
| 342 | Cega | 2 | 1/1 | DefiLlama lists Cega V1/V2 with no address; docs site did not resolve and no program id was published in the repos checked. |
| 343 | Composable Finance | 2 | 1/1 | The OtterSec audit covers Composable's Solana IBC program (solana_ibc, set_service) plus Initialize; no Solana program id is published in the report and docs.composable.finance does not list one. |
| 344 | Copra July23th | 2 | 1/1 | Copra Finance (Arbitrum lending per DefiLlama). No contract address published or confirmed. |
| 345 | Core Contracts | 2 | 1/1 | Zellic's 2026 report is titled only 'Core Contracts'. The body references MorphoVaultV1Adapter and staked-asset redemption, implying a Morpho-based vault project, but no project name, chain, repo or address appears in th |
| 346 | DeSyn Iterative | 2 | 1/1 | SlowMist 2022 DeSyn Iterative review names UserVault.recordTokenInfo. DeSyn's current deployments are on Arbitrum/Bitlayer/Mode per DefiLlama, all with null addresses, and no UserVault address from the audited 2022 gener |
| 347 | Deep3 | 2 | 1/1 | Three Sigma 2025 audit of Deep3; only the docs site exists publicly, no deployments page and no address in the report. |
| 348 | Dexalot | 2 | 1/1 | Dexalot docs have a 'Smart Contracts' section (docs.dexalot.com/en/contracts/) but it is an index whose per-chain pages are JS-rendered; the index and sitemap exposed no addresses, and the audit text carries none. Avalan |
| 349 | Dopex - June 21, 2021 | 2 | 1/1 | 2021 OPCore/OptionsContract architecture predates Dopex's Arbitrum deployment; docs publish no OPCore address and explorer name search surfaced only DPX/rDPX tokens (e.g. 0xEec2bE5c91ae7f8a338e1e5f3b5DE49d07AfdC81), not  |
| 350 | DoraHacks Quadratic Grant | 2 | 1/1 | Oak Security audit of DoraHacks' quadratic-funding grant contracts. No deployment address in the report extract; GitHub org has no quadratic-grant repo with an address book, and search surfaced only generic QF projects.  |
| 351 | Elusiv | 2 | 1/1 | Elusiv was a Solana ZK privacy program; the report names internal structures (nullifier tree, storage root) but no program id, and public material describes the project as wound down. |
| 352 | Eris Protocol | 2 | 1/1 | Oak Security review of Eris Protocol's CosmWasm contracts (voting-power / lockup logic). Eris deploys per-chain CosmWasm instances (Terra, Neutron, Injective, Osmosis and others) and publishes no address book in the mate |
| 353 | Farm Program | 2 | 1/1 | Project identified as Cropper Finance (Solana farm program); address not found. |
| 354 | Floin Floin Smart Contracts Smart Contract | 2 | 1/1 | No verified FLTKStaking/Crowdsale deployment found; the only candidate token address had zero code. |
| 355 | Foil Updates | 2 | 1/1 | Foil's docs describe architecture and audit reports but publish no TradeModule address. |
| 356 | Folks Finance | 2 | 1/1 | Algorand (TEAL/PyTeal) applications, identified by app id rather than a 0x address. Neither the report nor docs.folks.finance enumerates the audited app ids; no app-id lookup by contract name is available. |
| 357 | Fractionalizer and SellNow | 2 | 1/1 | CODESPECT 2025 review of Fractionalizer and SellNow. The batch entry has no report URL, chain or address, and no deployment named Fractionalizer/SellNow could be identified on Ethereum or Scroll name search. Nothing reco |
| 358 | GMX Solana | 2 | 1/1 | GMX Solana (GMTrade) launched on Solana mainnet 2025-03; the on-chain program id was not recoverable from public docs in the timebox. |
| 359 | Gamma GMX Vault | 2 | 1/1 | Guardian Audits 2024 review of a Gamma vault built on GMX (the report also links gmx-io/gmx-synthetics). Gamma deploys many Hypervisor/vault instances per chain and the docs' contract pages list the GAMMA token and limit |
| 360 | Groupcoin | 2 | 1/1 | Pashov Audit Group 2024 review of Groupcoin/GroupcoinFactory. No report URL or deployment manifest, and Blockscout name searches for 'Groupcoin'/'GroupcoinFactory' return nothing, so no address was recorded. |
| 361 | Hanji Liquidity Vault | 2 | 1/1 | Hanji Protocol is listed by DefiLlama on Etherlink/Base/Monad but with no address; no LPManager deployment found within the timebox. |
| 362 | Hodl on June 30th 2020. | 2 | 1/1 | Solidified 2020 review of HodlDex; project is defunct and the report carries no chain or deployment reference. |
| 363 | Hoenn | 2 | 1/1 | Three Sigma 2025 review of Hoenn (cvETH). No Hoenn deployment found; the search hit 0x6733...d2bc is Vector Reserve Staked vETH, a different protocol, and was rejected. |
| 364 | HyperHyper | 2 | 1/1 | Pashov Group review (2025-03-30). No report_urls, no report_addresses, and no docs/deployment page surfaced; search results for the name returned unrelated Hyperlane/hyper.finance contracts. |
| 365 | Illiquid Labs | 2 | 1/1 | FILLiquid runs on Filecoin FEVM; docs.filliquid.io exposes no reachable contracts/addresses page and the Oak report carries no addresses. |
| 366 | LeechProtocol | 2 | 1/1 | Leech docs' only contract reference is a link to the Hacken audit; no LeechRouter address is published. A 'Leecher' strategy token seen on Ethereum (0x02f036642dc6F1DF2684f7c0b7bBb43D2e53A59C) is not the router. |
| 367 | Legion (Solana-Sept | 2 | 1/1 | Legion (Solana-Sept) Zenith audit. The report names Rust instructions but publishes no program id, and Legion's docs do not list one. |
| 368 | Longship - April 20, 2022 | 2 | 1/1 | Solidified 2022 review of Hydrofoil.sol / HydrofoilParent.sol (a leveraged long/short product). The corpus entry has no website, repo, chain or deployment reference and no address surfaced, so nothing is recorded. |
| 369 | Lulo | 2 | 1/1 | Solana program addresses were not obtainable; DefiLlama adapter reads api.flexlend.fi stats only. |
| 370 | Metalex Borg | 2 | 1/1 | Metalex 'Borg' audit covers ConditionManager/Implant governance modules (conditionCheck, optimisticGrantImplant); no deployment address or chain is published in the report or project material found. |
| 371 | Mina Token Bridge | 2 | 1/1 | The bridge is a Mina zkApp (Bridge.lock); there is no EVM contract. Mina addresses are base58 and none appear in the report or Zellic's published text. |
| 372 | Nation Contracts | 2 | 1/1 | Audit text mentions Ethereum but no Nation deployment address surfaced. |
| 373 | PROTOCOL | 2 | 1/1 | Unit conflates two unrelated audits: Tethys Finance (MasterChef, Metis) and MonkeyKingdom/MonkeyLegends (Solana NFT game). Neither report carries an address; the Metis explorer lists several MasterChef contracts but none |
| 374 | Persistence-Jan24(Scope1+2 | 2 | 1/1 | Hexens Jan-2024 Persistence scope 1+2 report; no deployment list in batch metadata and no address surfaced from the report title alone. |
| 375 | PoodlTech Dividend Paying Token | 2 | 1/1 | Audit references the PancakeSwap router 0x10ED43C718714eb63d5aA57B78B54704E256024E, placing the token on BSC, but no token or dividend contract address is published. |
| 376 | Public - Reit Smartcontracts | 2 | 1/1 | Tokenized real-estate (REIT) contracts; no public deployments page found. |
| 377 | Qooodo | 2 | 1/1 | No deployment information found; searches returned unrelated results. |
| 378 | Rhinestone+Biconomy Smartsessions External Policies | 2 | 1/1 | Smart Sessions is a set of ERC-7579 validator/policy modules installed into user accounts. docs.rhinestone.dev documents concepts and ModuleKit but publishes no canonical module deployment addresses. |
| 379 | Rho Protocol | 2 | 1/1 | Rho Protocol/Rho Markets (audited 2024) is interest-rate derivative markets on Arbitrum. Current docs publish only the successor Rho X deployment on Ethereum (Router 0x461FFa24b716f68C5a4fB583592F295DB5f7BA36), which is  |
| 380 | Router DexSpan | 2 | 1/1 | Router Protocol cross-chain swap router; no DexSpan contract address found in two searches. |
| 381 | Router EVM and NEAR Gateway | 2 | 1/1 | Only the ROUTE token (0x16eccfdbb4ee1a85a33f3a9b21175cd7ae753db4) surfaced on Ethereum; the audited Gateway/ASM contracts (EVM + NEAR WASM) have no published address in reach. |
| 382 | Rumi Finance | 2 | 1/1 | Docs identity is solid (rumi.finance docs describe the hedge-vault/yield-farming architecture the audit names). Chain comes from DefiLlama (api.llama.fi/protocol/rumi-finance: Arbitrum, TVL now empty). Address tracing st |
| 383 | Security Audit – Anker on Solana | 2 | 1/1 | No Solana program id published for Anker; nothing to map. |
| 384 | Sienna Network Rewards V3 CosmWasm Smart Contract | 2 | 1/1 | Halborn 2021 review of the Sienna Network rewards-v3 CosmWasm contract on Secret Network. Secret contracts are addressed as secret1... and the deployment address is not published in the report or docs; nothing is recorde |
| 385 | Skip Protocol Swap Contracts | 2 | 1/1 | Audit covers CosmWasm swap contracts (Rust); no deployed contract address surfaced, only code-level findings. Chain not asserted without evidence. |
| 386 | Smart Contract. | 2 | 1/1 | Unit mixes two unrelated 2019 audits (Gossamer contract wallet, KickICO token). No live deployment address surfaced for either. |
| 387 | StationX | 2 | 1/1 | docs.stationx.network does not resolve and Base Blockscout name searches for StationX/StationXFactory return only unrelated tokens, so no address is recorded. |
| 388 | Subsquid | 2 | 1/1 | Subsquid GatewayRegistry audit. Ethereum explorer returns several unrelated GatewayRegistry contracts (generic name collisions, no Subsquid-specific metadata), and the Subsquid network contracts are Arbitrum-side, so no  |
| 389 | TENET - veTENET Smart Contract Security | 2 | 1/1 | Halborn audit of veTENET (voting escrow) on Tenet. No deployment address in the report extract; Tenet docs publish no veTENET address and no explorer name search resolved one. The TENET token address is not the voting-es |
| 390 | Unipay | 2 | 1/1 | Unipay (Oak, Apr 2025) findings use snake_case entry points (stake_usdu_mint_susdu, preview_deposit) with no chain stated. Strata Markets' USDU-adjacent contracts were checked but do not match the audited surface, so not |
| 391 | Vcred | 2 | 1/1 | Only the Hacken PDF exists; project could not be tied to a live deployment. |
| 392 | WWH Smart Contract | 2 | 1/1 | Report has no deployment information; project identity unresolved. |
| 393 | ZIGChain | 2 | 1/1 | ZIGChain is a Cosmos SDK chain; both findings are in x/dex Go module code, so there is no contract address. Chain recorded as ZIGChain. |
| 394 | Zodiac Protocol Periphery | 2 | 1/1 | Zodiac Protocol Periphery (Gnosis Guild) is an audit of periphery modules; no per-module deployment addresses were published in the report and none were confirmed. |
| 395 | apDAO | 2 | 1/1 | Pashov 2024 apDAO (ApiologyDAO) review with ApiologyDAOToken; no deployment section and no verified ApiologyDAO contract found. DefiLlama's 'ApeDAO' on Fantom (0x6a2d140f...) is a different project and was rejected. |
| 396 | eBridge AElf Bridge | 2 | 1/1 | eBridge runs on AElf, a non-EVM chain; no EVM-style contract address exists and the AElf contract address was not recovered from the report. |
| 397 | for Logarithm | 2 | 1/1 | Logarithm MetaVault/LogarithmVault (Jul 2025). No deployed address surfaced for MetaVault or the underlying LogarithmVault. |
| 398 | memes.fun | 2 | 1/1 | Oak's Sep-2025 memes.fun report names calculate_price and a swap path but states neither chain nor program/contract address; no docs or deployment page surfaced. |
| 399 | pashov-solo-2023-11-17-lumin-security-review | 2 | 1/1 | The name collides with Lumin Finance (Arbitrum, 0x1FC0...) but nothing ties that deployment to this 2023 review, so no address is recorded. |
| 400 | pashov-team-2024-02-01-saffron-security-review | 2 | 1/1 | Saffron Vaults docs describe VaultFactory/RestrictedVaultFactory, UniV3 vaults and adapters conceptually but publish no deployment addresses; the SFI token 0xb753428af26e81097e7fd17f40c88aaa3e04902c is unrelated to the a |
| 401 | sigmaprime synthetix unipool | 2 | 1/1 | Sigma Prime 'Synthetix Unipool Review' (2024-04-29). Unipool is Synthetix's generic staking-rewards implementation; the report names no deployment and Unipool instances are deployed per reward program, so no single attri |
| 402 | sofa | 2 | 1/1 | Sigma Prime 'sofa' review covers an AAVE-vault structured-products protocol. docs.sofa.org is unavailable and no vault/minter address could be attributed. |
| 403 | tramplin.io | 2 | 1/1 | tramplin.io is a Solana staking product; the MixBytes audit covers an Anchor program (ClaimArgs::validate, process_claim) but neither report nor site publishes a program id. |
| 404 | vcred | 2 | 1/1 | Dead project; no identity or address. |
| 405 | wesendit | 2 | 1/1 | Repo has only sources/scripts; no deployment addresses and no explorer hit. |
| 406 | 03 03 Light Extension MR | 2 | 0/2 | Report covers a Light Protocol program (compressed-token extension); no program ID for the audited build surfaced, and the generic compression program ID was not accepted as a substitute. |
| 407 | 2019-09-ethereum-evm-aztec | 2 | 0/2 | 2019 audit of the pre-launch Aztec zk-rollup EVM verifier; the audited revision is not a live deployment and no address was located. |
| 408 | 2021-03-30-daofi-dao | 2 | 0/2 | Sherlock 2021 review of DAOfi v1 (DAOfiV1Pair / DAOfiV1Router). An Ethereum deployment exists (DAOfi token 0xD82BB924...), but the router/pair addresses were never published and no verified DAOfiV1Router contract exists  |
| 409 | 2021-06-12-bunicorn-sca-bunicorn-governance-erc20-jun2021-sca-bunicorn | 2 | 0/2 | Bunicorn (BSC AMM). The 2021 SCA review covers BuniCornPool / Governance / ERC20, but the batch record carries no report URL and the pool address is not published; the docs domain no longer serves a contracts page. DefiL |
| 410 | 2021-08-11-xpocket-sca-xpocket-erc20-aug2021-sca-xpocket-erc20-aug2021 | 2 | 0/2 | No project site, repo, chain or address found; Hacken audit page only. NOT_FOUND. |
| 411 | 2022-02-hubble | 2 | 0/2 | Code4rena 2022-02 Hubble (Solana). Program id for the Hubble borrowing program was not surfaced; HBB token deliberately not recorded as the audited address. |
| 412 | 2022-03-26-valhalla-sca-valhalla-erc20-mar2022-sca-valhalla-erc20-mar2 | 2 | 0/2 | No project site, GitHub repo or explorer entry could be tied to this March-2022 ERC20 audit; name searches collide with an unrelated Solana protocol. NOT_FOUND. |
| 413 | 2022-06-06-final-flux-audit-report | 2 | 0/2 | The batch record carries no report URL, body or address for this 2022 Flux oracle review, and no Flux oracle deployment (feed/validator set) could be identified from public sources in this pass. Nothing was attributed. |
| 414 | 2022-08-rigor | 2 | 0/2 | Code4rena-era Rigor Protocol (construction lending: community owners and builders). No repository, docs or deployment surfaced; batch ST2-028 also recorded NOT_FOUND for the same project. |
| 415 | 2023-02-15-sturdy-aura-integration-and-leverage-sturdy | 2 | 0/2 | Audit of Sturdy's Aura integration and leverage contracts (withdrawWithFlashloan/zapDeposit/zapLeverageWithFlashloan). Sturdy's published deployment data (DefiLlama sturdy-v2 adapter) only exposes per-chain DataProvider  |
| 416 | 2023-12-particle | 2 | 0/2 | The code4rena 2023-05 Particle Exchange repo confirms the protocol exists but lists no addresses. |
| 417 | 2024-02-althea-liquid-infrastructure | 2 | 0/2 | Code4rena Feb-2024 audit of Althea Liquid Infrastructure. Report addresses checked for code on Ethereum/Base/Optimism and came back empty; the audit predates a public deployment. |
| 418 | 2024-03-06-ussd-sca-ussd-oracles-jan2024-sca-ussd-oracles-jan2024 | 2 | 0/2 | Hacken page identifies the audited project as USSD (ussd.ai), an autonomous collateralised stablecoin on EVM (Ethereum, Arbitrum, BSC, Optimism), repo github.com/DavidLeeChaum/USSDv2. The repo publishes no deployment add |
| 419 | 2024-04-lavarage | 2 | 0/2 | Solana program; no program id published in reachable docs or the code4rena repo, so no address asserted. |
| 420 | 2024-05-ethereum-evm-wonderland-prophet-securityre | 2 | 0/2 | Wonderland review of Prophet (modular oracle/callback framework). Only the defi-wonderland/prophet-sdk package surfaced; no mainnet deployment address published. |
| 421 | 2024-08-06-netmind-e7dfdc3c | 2 | 0/2 | NetMind runs its own NetMind Chain alongside NMT token deployments on BSC and Ethereum. No AccountManage / payment-distribution deployment surfaced in BSC or Ethereum explorers or in NetMind docs within the timebox, so n |
| 422 | 2024-09-20-vow-sca-vow-vowcurrency-sep2024-sca-vow-vowcurrency-sep2024 | 2 | 0/2 | VOW is a currency project with Uniswap V2 pools on Ethereum, but no VOWCurrency contract address could be confirmed from the audit text or explorer tags. |
| 423 | 2024-11-18-sigmaprime-near-sigma-prime-near-burrowland-security-assess | 2 | 0/2 | NearDeFi/burrowland repo found, but its README is a usage walkthrough (alice.near/bob.near examples) with no deployed contract account id. NEAR accounts are named, not 0x, and no id was verifiable. NOT_FOUND. |
| 424 | 2024-11-mantra-dex | 2 | 0/2 | MANTRA DEX is a CosmWasm application on MANTRA Chain; contracts are identified by bech32 contract addresses / code ids, not EVM 0x addresses, and no deployment address is given in the released text. |
| 425 | 2024-12-02-smart-contract-audit-for-clave-monorepo | 2 | 0/2 | Clave is a zkSync Era smart wallet (DefiLlama). zkSync Blockscout has no ClaggAaveAdapter or Clave contracts; no adapter address surfaced. |
| 426 | 2024-12-09-final-oku-s-new-order-types-contract-contest-audit-report | 2 | 0/2 | Audited contracts are Bracket, StopLimit and OracleLess. Arbitrum Blockscout name search returned no OracleLess/Bracket contract, Oku docs publish no deployments page, and the public audit repo lists no addresses. No cha |
| 427 | 2024-12-secondswap | 2 | 0/2 | SecondSwap is a vesting marketplace (DefiLlama lists Avalanche/Ethereum/Solana), but the corpus entry has no report URL, body or deployment map and no labelled contract was found within budget. |
| 428 | 2025-06-panoptic-hypovault | 2 | 0/2 | HypoVault is a 2025 Panoptic Labs contract set; the only public artefact reached is the panoptic-labs/hypovault repository, which carries no deployment address, and the Panoptic docs contract overview lists Panoptic V1 c |
| 429 | ALTO - Lending Market - Audit Report | 2 | 0/2 | Bailsec 2025 audit of ALTO's lending market. The extract names no chain, website or repo beyond the audit PDF, and no deployment matching the audited removeCollateral/swapData design was found within budget. |
| 430 | ASPIS | 2 | 0/2 | AspisPool is deployed per vault by a factory; no factory or pool address is published in docs or the Hacken audit page. |
| 431 | Alpha | 2 | 0/2 | Oak Security Jul-2022 review of the CosmWasm 'Alpha v1.0' protocol (contracts/oracle, contracts/borrowed-farm). The chain is not stated and no wasm contract address or code id appears in the extract. DefiLlama's 'Alpha'  |
| 432 | Amun contest | 2 | 0/2 | Code4rena Dec-2021 Amun contest (Solana). Leftover-token finding names no contract and no program id was resolved. |
| 433 | Aptos Move Module | 2 | 0/2 | Project is Strat (strat.trade), an Aptos perpetual DEX; the batch label 'Aptos Move Module' is generic. github.com/strat-trade/audits contains only the Zellic PDFs and a README, so the published Move module address is no |
| 434 | AtomOne v4 Changes | 2 | 0/2 | Cosmos SDK chain; addresses are not applicable, chain itself recorded. |
| 435 | BOB Staking | 2 | 0/2 | docs.gobob.xyz stake-BTC guide explains the staking flow but publishes no contract address; BOB chain (id 60808) reachable, no explorer name lookup available keyless. NOT_FOUND. |
| 436 | Backed Protocol contest | 2 | 0/2 | 2022 code4rena contest on an NFT-loan protocol; DefiLlama lists it on Ethereum with no address and the contest repo publishes none. |
| 437 | Beedle (oracle-free perpetual lending) | 2 | 0/2 | No project site, repo or deployment reference surfaced; nothing to attribute. |
| 438 | Behodler | 2 | 0/2 | DefiLlama lists Behodler on Ethereum but its recorded address is the EYE token, not a protocol contract. No deployments page found. |
| 439 | Bitget | 2 | 0/2 | Two BlockSec reviews: Bitget's swap aggregator (V3Handlers) and the BGW staking rewards module. Bitget is a centralized exchange; the on-chain aggregator/staking deployments are not published in the report extracts and n |
| 440 | Blockswap Stakehouse | 2 | 0/2 | Runtime Verification 2022 review of Blockswap Stakehouse (DKGRegistry, SafeBoxManager, BalanceReporter). The Stakehouse deployment was on Ethereum, but the audited contract addresses are not published in the report and B |
| 441 | Bloom | 2 | 0/2 | Blueberryfi/Bloom-protocol deploy scripts (script/DeployCore.main.sol, DeployPool.main.sol) log BloomFactory/BloomPool addresses at run time only; no deployment address or chain is published in the repo, docs or audit; D |
| 442 | Boba | 2 | 0/2 | Boba docs deployment pages returned 404 and the repo's contract deployment folder is not at the paths tried. L1 bridge / L1 NFT bridge addresses not located in the timebox. |
| 443 | Brevis Pico ZKVM | 2 | 0/2 | Pico is a zkVM circuit/verifier library (Rust); findings live in pico/vm source files, and no deployed on-chain contract is named or tied to the audit. |
| 444 | Bridges Exchange 1 | 2 | 0/2 | Guardian Audits 2022 review of a 'Bridges Exchange' dividends contract. The name is generic, no website/repo/deployment is given, and no labelled contract was found within the two-search budget. |
| 445 | Cally | 2 | 0/2 | docs.cally.finance resolves but has no contracts/deployments page, and blockscout name search on Ethereum returns no Cally contract. NOT_FOUND. |
| 446 | Carapace | 2 | 0/2 | Identity resolved (carapace.finance, protection market for under-collateralized lending). The public site is whitepaper/docs only and exposes no contract addresses; no verified ProtectionPool could be located, so no chai |
| 447 | Chakra | 2 | 0/2 | Chakra is a BTC-restaking chain with a Cairo settlement component; docs.chakrachain.io did not resolve and no explorer name match was found. NOT_FOUND. |
| 448 | Chirper AI | 2 | 0/2 | Repo chirper-ai/contracts confirms Manager.sol (graduation/liquidity) and Router.sol, but hardhat.config.ts only lists BSC (56), Mode (34443), Vana and Monad endpoints and the repo carries no broadcast/deployments output |
| 449 | Clave | 2 | 0/2 | Clave was a zkSync Era smart-account wallet. getclave.com and the Cantina/Pashov extracts give no factory or account-implementation address, and no explorer match was found within budget. |
| 450 | Clove | 2 | 0/2 | Cantina Feb-2026 review of Clove's SpotSettlement/Vault settlement contracts. The extract names contracts and a nonce manager but no chain, address or repo; the deployment was not located in this pass. |
| 451 | Commit Boost Multiplexer & Signer | 2 | 0/2 | Commit-Boost is an off-chain MEV-Boost/PBS sidecar (Rust). Sigma Prime audit is code-level; there is no on-chain deployment to trace. |
| 452 | Coredao | 2 | 0/2 | Two reports: an NLX DEX (GMX fork) review and a Core BTC-hardfork rewards update. The five report_addresses leads are not protocol contracts: 0x8250f4af... is the Pyth PriceFeedUpdate emitter on Core, 0xbf668dad... is a  |
| 453 | Crestal Network | 2 | 0/2 | Crestal's public GitHub describes 'Crestal Omnichain Smart Contracts - Blueprint' but publishes no deployment address book; the BlueprintV5 / Payment pair was not located on a public explorer within the timebox. |
| 454 | Cron Finance | 2 | 0/2 | Spearbit review (2023) of Cron Finance, an Ethereum LP / join-pool integration. DefiLlama lists the protocol at $0 TVL with no address, Blockscout name search returns no match, and the project docs domain does not resolv |
| 455 | Cryptex (2024-09 monorepo) | 2 | 0/2 | Identity resolved to cryptex.finance; deployments of the audited lending market could not be located. Prior batch ST2-050 reached the same NOT_FOUND for this unit. |
| 456 | DAO DAO | 2 | 0/2 | DAO DAO is CosmWasm: contracts are deployed as per-chain code IDs rather than fixed addresses, and the two Oak reports name cw-proposal-single / dao-proposal-multiple without an instance address. |
| 457 | DB Cherry | 2 | 0/2 | SmartWallet/AA wallet deployment not located; no chain or address in the audit text. |
| 458 | DEDAUB.COM Rysk | 2 | 0/2 | Dedaub Feb-2023 review of Rysk v1 on Arbitrum (VolatilityFeed, OptionExchange). Rysk has since moved to HyperEVM/Ethereum and its docs publish no contract-address table; the audited Arbitrum addresses could not be reache |
| 459 | DN404 | 2 | 0/2 | Guardian Audits reviewed the DN404 token standard (reference implementation), not a protocol deployment. There is no single core address - every DN404 token is its own deployment - so NOT_FOUND is structural, not a searc |
| 460 | Dango DEX | 2 | 0/2 | Sherlock contest 1066 for Dango DEX (geometric/AMM pools, Rust-style naming). No chain, repo, website or deployment address is present in the corpus entry; the pool may not be live at audit time. |
| 461 | Dutch Protocol | 2 | 0/2 | Pre-deployment style audit (Feb 2026); no docs site or explorer hit. |
| 462 | Element Finance Governance Contract | 2 | 0/2 | Runtime Verification's 2021 review of Element Finance's governance Timelock. The timelock address is not published in the docs pages reached, and Blockscout name search returned no Timelock attributable to Element. The E |
| 463 | EquitX Stellar | 2 | 0/2 | EquitX runs on Stellar/Soroban; no C... contract id or project docs surfaced in the timebox. |
| 464 | Ethereum Credit Guild | 2 | 0/2 | Code4rena 2023 review of Ethereum Credit Guild. The repo README publishes only Sepolia deployment addresses (Core, ProfitManager, ERC20RebaseDistributor, etc.); no Ethereum mainnet deployment address was found, so nothin |
| 465 | Family Wallet | 2 | 0/2 | Family Wallet is a self-custody mobile wallet app; both findings live in the iOS client's dApp browser (WCAppMappingsManager URL matching and the origin check). No on-chain contract is named or audited, so there is no de |
| 466 | Forte | 2 | 0/2 | No Forte site/docs/repo identifiable for this audit (searches returned audit-firm marketing pages). NOT_FOUND. |
| 467 | Fractal Protocol | 2 | 0/2 | Zellic 2022 review of Fractal Protocol's lending/reward contracts. DefiLlama lists multi-chain deployments but carries no contract address, and the project docs do not publish a contract table; nothing could be attribute |
| 468 | Fyllo Smart | 2 | 0/2 | No reachable Fyllo site, docs or repository; name searches returned unrelated projects. NOT_FOUND. |
| 469 | GET-Protocol-Staking | 2 | 0/2 | Electisec/yAudit 2022 review of GET Protocol's staking and cross-chain voting. The old docs domain no longer serves documentation and no GET staking deployment is published in the report extract or reachable docs, so no  |
| 470 | GMX Solana Protocol | 2 | 0/2 | GMX Solana is a Rust/Solana program set (gmsol); docs.gmx.io only publishes EVM deployment tables. No base58 program id was verifiable in budget, so NOT_FOUND. |
| 471 | GU Exchange | 2 | 0/2 | GU Exchange maps to 'Mu Exchange' on xDai/Gnosis per the DefiLlama candidate, which carries no address. No GU/Mu deployment or bonding-curve contract surfaced. |
| 472 | General Galactic Skyteller V1 | 2 | 0/2 | Runtime Verification's review of 'Galactic Skyteller V1' (Sweeper + oracle). Name searches collide with an unrelated aerospace company, and neither the report extract nor any explorer search ties a Skyteller deployment t |
| 473 | Glider Protocol | 2 | 0/2 | Guardian's Sep-2026 'Glider Protocol Review' targets a portfolio-vault protocol (epoch NAV gate, JIT claims). docs.glider.fi documents a B2B portfolio API and smart-account deposits but publishes no contract addresses; t |
| 474 | Gondi (October | 2 | 0/2 | Four contracts named OldERC721Wrapper exist on Ethereum but none could be tied to Gondi (source carries no protocol identifier). Gondi's exploitable PurchaseBundler (0xc10472ac...) is a different contract from the audite |
| 475 | GrowthDeFi WHEAT | 2 | 0/2 | GrowthDeFi GitHub org exists (growthdefi-docs, v1-core) but neither publishes a WHEAT deployment for BSC; no explorer lookup available keyless. NOT_FOUND. |
| 476 | Helios protocol | 2 | 0/2 | Helios is a Uniswap-v2/v3-style DEX on RISE Chain; its public docs have no deployments page. |
| 477 | Hone Smart Contracts | 2 | 0/2 | Hone is an Algorand protocol, so there is no EVM address; the audited application ids were not found in the report or any reachable docs page. |
| 478 | HydraDX Omnipool | 2 | 0/2 | Omnipool is a Substrate pallet on the HydraDX/Hydration parachain, not a contract; refund_refused_asset/sell are extrinsics with no contract address. |
| 479 | INDX | 2 | 0/2 | DefiLlama lists INDX on Base with a null address. docs.indx.co resolves but renders client-side and no contract address is present in the served HTML; Base Blockscout name search for INDX/IndexV3 returned nothing. |
| 480 | Interpol | 2 | 0/2 | Pashov 2025 review of Interpol's HoneyLocker on Berachain (report references BGT 0x656b...1dba and BGTStaker 0x44F0...c7C6). HoneyLocker is deployed per user (migrations compare codehashes), so there is no single audited |
| 481 | Isomorph | 2 | 0/2 | Sherlock contest 22 (2022) for Isomorph, a Velodrome-deposit wrapper on Optimism. No report_addresses, no docs, and an Optimism Blockscout search for the Depositor returned nothing. Likely defunct. |
| 482 | JIG | 2 | 0/2 | No website/docs/repo or deployment address surfaced for JIG/MoreMarkets; NOT_FOUND within the timebox. |
| 483 | Jubi DAO | 2 | 0/2 | No report URL, source URL or deployment data for Jubi DAO in the batch record; no chain could be confirmed. |
| 484 | Kingdomly | 2 | 0/2 | Kingdomly docs contain no deployment/address page; Polygon and Base Blockscout searches returned no KingdomlyStaking or MasterContractV3_ONFT contract. |
| 485 | Kora Solana | 2 | 0/2 | Solana program audit (Runtime Verification 2025). No EVM deployment; program id not resolved within the timebox. |
| 486 | LAB Sep5th | 2 | 0/2 | Zokyo's Sep-2025 review of a 'LAB' DEX router (LabDexRouterOptimized, Pancake/Uniswap V3 callbacks). The report extract names no chain and no deployment, and no router attributable to LAB was found; NOT_FOUND. |
| 487 | LYNXTokenContracts | 2 | 0/2 | Electisec 2026-07 report of LYNX token contracts; the extract has no chain, repo or deployment reference and the public materials found within budget name no address. Likely a pre-deployment review. |
| 488 | LimitBreak AMM | 2 | 0/2 | Guardian Audits' Nov-2025 review of LimitBreak AMM; the body is withheld (publisher_notice) and the report gives no deployment. LBAMM deploys deterministic pool-type contracts, but no address is published, so nothing is  |
| 489 | LiquiFi Vesting Contracts V1 | 2 | 0/2 | LiquiFi is a token-vesting platform whose Vesting V1 contracts are deployed per client; the Sherlock review targets the implementation, not one instance, and the batch entry carries no report URL or project site. This is |
| 490 | Marble Smart Contracts. Part I | 2 | 0/2 | ABDK 2019 audit referencing 'Line 36'/'Line 60' of a Marble contract; no project website, repo or deployed address is given, and the code appears to be an example contract rather than a live protocol. |
| 491 | Mask Social Solana Redpacket | 2 | 0/2 | Solana (Rust) redpacket program audited by SlowMist; no addressable EVM deployment. Recorded as NOT_FOUND. |
| 492 | Mauve - May 15, 2023 | 2 | 0/2 | Mauve is Violet's Uniswap-v3-derived DEX. Only the MAUVE ERC-20 (0x5a1b2bc070c62d9fd3c1c7a3e57b409c390ddb97) surfaced; it is a token, not the audited SwapRouter, and no docs deployment page was found, so no address is re |
| 493 | Metaswap | 2 | 0/2 | MetaSwap on EOS EVM; deployment address not located. |
| 494 | Metatime | 2 | 0/2 | Identity from docs.metatime.com (MetaChain, MetaAnthill, Metatime Coin). Both audits target proprietary Metatime deployments with no public address book, so no chain or address is recorded. |
| 495 | Metavest | 2 | 0/2 | Zellic 2024 review of MetaVesT (MetaLex-Tech). The framework is deployed per entity through MetaVesTFactory.deployMetavestAndController(); the README publishes no factory, controller, or allocation address, so there is n |
| 496 | Minara AI us | 2 | 0/2 | SlowMist 'blockchain application' audit of Minara AI. Report addresses were checked with eth_getCode and hold no code on Ethereum; identity/chain unresolved. |
| 497 | NETZ | 2 | 0/2 | FuzzLand audit; no project site, docs or deployment reference surfaced within the search budget. |
| 498 | Napier | 2 | 0/2 | DefiLlama lists Napier on Ethereum/Base/Arbitrum/Sonic etc. but returns no contract address; docs deployment page requires GitBook auth. |
| 499 | Neptune Updates 2 | 2 | 0/2 | Neptune Finance is a CosmWasm lending protocol (Oak Security / Codezen review, Dec 2024). Its live contracts are CosmWasm instantiations with bech32 addresses that are not published in the report extract or the docs reac |
| 500 | NexaFinance TokenPortfolio v 1 0 | 2 | 0/2 | ABDK 2025 audit. Contract name TokenPortfolio did not resolve on the explorers checked; no docs/deployment page found. |
| 501 | Numa | 2 | 0/2 | docs.numa.gg does not resolve and no DefiLlama adapter exists; no Numa contract surfaced in the time box. |
| 502 | Nume | 2 | 0/2 | The Pashov review names a Nume contract with Exodus Mode and withdrawExodus, but no chain, website or deployment address is published in the report and no matching contract surfaced on Ethereum explorers. |
| 503 | Nunchi Migration | 2 | 0/2 | Guardian's Nov-Dec 2025 review of Nunchi's migration contracts. The extract names no address and no site, repo or deployment page was found; the chain is not confirmed. |
| 504 | Palmera | 2 | 0/2 | Hats Finance audit of Palmera. 0x5FeE7541Ddcd51bA9F4Af606F87b2C42eEa655bE on Optimism resolves to a 'Hats Vault palmera' (HATVault proxy) — rejected as an audit-escrow dependency, not the protocol. |
| 505 | Particle Leverage AMM Protocol Invitational | 2 | 0/2 | Particle's LAMM (leveraged trading against Uniswap v3 liquidity) was reviewed by Code4rena in Dec-2023. The batch's report_addresses are USDC (0xA0b86991...) and the Uniswap SwapRouter02 (0xE592427A...), both dependencie |
| 506 | Particle Protocol (2023-05) | 2 | 0/2 | Audit-time repo is code-423n4/2023-05-particle (5 contracts, 688 LoC). No live deployment attributable. |
| 507 | Pencils Launchpad | 2 | 0/2 | Fuzzland review of Pencils Launchpad (Scroll). The report's only contract-like literal, 0xa5906e11c3b7F5B832bcBf389295D44e7695b4A6, has no code on Scroll (Scrollscan api/v2: is_contract=false) or on Ethereum, so it is an |
| 508 | Polystream Vault | 2 | 0/2 | New Cantina-reviewed vault built on Spectra; no chain or deployment information in the report metadata. |
| 509 | PoolTogether - LootBox and MultipleWinners Strategy | 2 | 0/2 | ConsenSys Diligence 2020 review of the LootBox and MultipleWinners strategy. Blockscout name search returns many unrelated 'LootBox' tokens and no verified PoolTogether LootBox; the candidate proxy 0x29fe7d60ddf151e5b52e |
| 510 | PromisSmartContracts | 2 | 0/2 | 2026 Electisec audit of Promis (proUSD/yAsset). No site, docs, repo or explorer entry surfaced in budget. NOT_FOUND. |
| 511 | Pt | 2 | 0/2 | The batch label 'Pt' merges two unrelated Guardian reviews: Gamma Unilaunch Launchpad + LimitOrderBook (LBPStrategyBasic.sol) and Bounce Automation Layer. Neither extract names a deployment and the label does not identif |
| 512 | RIFv | 2 | 0/2 | Coinspect 2018 review of the RIF vesting/TokenManager contracts on RSK. The report publishes no addresses and no deployment manifest for TokenManager was reachable; the well-known RIF token address is a token, not the au |
| 513 | Reflex Protocol | 2 | 0/2 | Guardian Audits 2026 review of Reflex Protocol's ExecutionRouter. The extract gives no chain, website or repo beyond the audit PDF, and no address surfaced within budget. |
| 514 | Render | 2 | 0/2 | OtterSec Oct-2023 review of Render's Solana Anchor bridge (rndr_mint/wrndr_mint, InitializeBridgeV1). The Ethereum RNDR ERC-20 (0x6de037ef9ad2725eb40118bb1702ebb27e4aeb24) is a token, not the audited bridge, so it was re |
| 515 | Report 4 of 6: Asteroid Farms | 2 | 0/2 | Zokyo review of TangleSwap's Asteroid Farms on ShimmerEVM. A third-party listing cites evm.shimmer.network/address/0xE5f3dCC241Dd008E3c308e57cf4F7880eA9210F8, but the Shimmer Blockscout API was Cloudflare-blocked and the |
| 516 | Reserve Protocol | 2 | 0/2 | RSR token is the protocol's governance token, not the audited collateral wrapper; recorded as no address rather than mis-mapping it. |
| 517 | Rho Labs Sep23rd | 2 | 0/2 | DefiLlama identifies Rho Markets as a Scroll deployment but publishes no address for it; docs.rho.trade did not resolve. NOT_FOUND. |
| 518 | Risex Contracts | 2 | 0/2 | Rise Labs / Risex perp DEX; no public deployment page found in two searches. |
| 519 | Robinos - SideBetV6 | 2 | 0/2 | BailSec Sep-2024 review of Robinos SideBetV6 (Solidity/Foundry). The only address in the report is ZRX 0xE41d2489571d322189246DaFA5ebDe1F4699F498, used as a test token, so it was rejected as a dependency. No chain or dep |
| 520 | Rolla contest | 2 | 0/2 | Code4rena 2022-03 Rolla contest. No report_addresses, no docs, and an Arbitrum Blockscout search for Rolla returned nothing. Chain and deployment unconfirmed. |
| 521 | Rollup Finance | 2 | 0/2 | PeckShield 2023 review of Rollup Finance (zkSync Era perp DEX). docs.rollup.finance did not resolve and the report publishes no addresses; one search surfaced only the project's X/Medium. No StableVault address confirmed |
| 522 | RubiFi - Extension #2 | 2 | 0/2 | Zenith extension review #2 for RubiFi. rub.finance is a JS app with no docs or address list; the only Ethereum name match (Rubi.Finance 0xAad4..., created 2020-08-14) is an old unrelated token, so nothing is attributable |
| 523 | RuneMine by Mine Labs’ | 2 | 0/2 | RuneMine multisig audit (Sherlock 2024); no project site, repo or deployment address surfaced. Bitcoin Runes context means no EVM address expected. |
| 524 | SKALE contest | 2 | 0/2 | SKALE IMA runs MessageProxyForMainnet on Ethereum and MessageProxyForSchain on every SKALE chain; the addresses are per-chain deployment artefacts and no published registry entry was retrieved within budget. Chain ids va |
| 525 | Sandbox Starter Pack Sale - October 22, 2020 | 2 | 0/2 | Solidified 2020 audits of The Sandbox Starter Pack sale and reward pool. The reports name CatalystDataBase.sol and the reward pool but publish no addresses; the 2020 sale contracts are not discoverable by name on a publi |
| 526 | Sire Contracts | 2 | 0/2 | Cantina's Sep-2025 review of Sire's vault contracts. The batch's only report address is USDC on Base (0x833589fC...), a dependency, and it was rejected. Sire's own vault addresses are not published in the report or on do |
| 527 | Smilee Finance | 2 | 0/2 | Smilee ran its options market on Arbitrum at audit time and now markets Berachain products (DefiLlama: Berachain pool 0xb2a12db2691fc05dca47b2be9a087077afaa0800). Only an Arbitrum-Sepolia test NFT contract surfaced; no m |
| 528 | Sofamon V2 | 2 | 0/2 | Pashov's August 2024 review of Sofamon V2 (commitToMint, order fill). The extract gives no chain or address and no deployment page was identified, so nothing is recorded. |
| 529 | Solana Foundation Multi Delegator | 2 | 0/2 | Solana subscription-delegation program; only the chain was confirmed. |
| 530 | Spartan-ECDSA | 2 | 0/2 | Electisec/yAudit reviewed the Spartan-ECDSA circom circuits and verifier library, not a deployed protocol. A zk circuit is a reusable component with no single deployment address; any verifier instance is deployed per int |
| 531 | Sprinter Credit: Remote Collateral Contracts | 2 | 0/2 | Docs describe the credit engine but publish no contract addresses; the Cantina page has no deployment table. EscrowHelper address not located. |
| 532 | Stacks WSTS | 2 | 0/2 | OtterSec review of the WSTS signer code in stacks-sbtc (Rust: src/net.rs, src/state_machine/signer/mod.rs, src/v2.rs). This is off-chain signer software; there is no deployed contract address to trace. |
| 533 | Synthetix Withdrawal Flow | 2 | 0/2 | Guardian's Dec-2025 review covers Synthetix's new off-chain withdrawal/trade signing service (WebSocket messages) rather than a named on-chain contract. Current Synthetix perps settle on Ethereum mainnet per docs.synthet |
| 534 | Temple | 2 | 0/2 | Both reports are Halborn reviews of Temple Digital Group: a Canton backend audit and an API pentest. There are no EVM contracts and the Canton party/contract identifiers are not published, so no address is recorded. |
| 535 | Teneo | 2 | 0/2 | TeneoRewardProtocol audit; no site, repo or deployment address found. |
| 536 | The Rig | 2 | 0/2 | The Rig runs on Fuel (Sway contracts). DefiLlama lists only the Fuel chain with no address; recorded as NOT_FOUND for EVM tracing. |
| 537 | Timeless-Yield-Daddy | 2 | 0/2 | Yield Daddy is a generic ERC4626 wrapper library plus factories (GitHub timeless-fi/yield-daddy). DefiLlama lists Timeless Finance on Ethereum but the audited contracts are wrappers instantiated per integrator, so no sin |
| 538 | TokensFarm Sep 16 | 2 | 0/2 | Zokyo 2022 audit of TokensFarm. TokensFarm is a farm-as-a-service platform: each farm is a separate TokensFarm deployment (three verified Ethereum contracts named TokensFarm exist: 0xd10B535C0019C06a37CAB485B300b85C438fd |
| 539 | TreasureDAO-3 | 2 | 0/2 | Macro 2023 review of TreasureDAO's modified UniswapV2 pair and NftVault/NftVaultFactory on Arbitrum. The report names contracts but no addresses, and the repo carries no deployment manifest; Arbiter/Arbitrum Blockscout w |
| 540 | Trustswap StakingPool | 2 | 0/2 | BailSec 2024 audits (two reports, Jan and Feb 2024) of the TrustSwap StakingPool implementation. TrustSwap deploys staking pools per project (team.finance); the audited contract is a template with no single canonical dep |
| 541 | UTYAsyncVault | 2 | 0/2 | XSY security review of UTY's ERC-4626 async vault (UTYAsyncVaultV1). No project site, docs, repository or explorer entry for UTY was found in this pass, so no chain or address is recorded. |
| 542 | VYNKSAFE | 2 | 0/2 | Hacken audit (2022). Only unrelated VYNK CHAIN tokens appear on Ethereum; no VYNKSAFE contract identified. |
| 543 | Ventuals | 2 | 0/2 | ventuals.com now says 'Ventuals is sunsetting' and links a vHYPE staking contract, but the page (Next.js, client-rendered) exposes no 0x address; docs.ventuals.com has no deployments page found. Hyperliquid L1 markets ar |
| 544 | Visor Finance | 2 | 0/2 | Defunct 2021 project; no core deployment address found. VISR token is not the contract named in the report. |
| 545 | Yield-Convex contest | 2 | 0/2 | No Yield-Convex deployment address found; the audited vaults are per-strategy yVault clones and no canonical address is published in the report. |
| 546 | Yieldy contest | 2 | 0/2 | Code4rena's June-2022 Yieldy contest reviewed LiquidityReserve / instantUnstakeReserve. The project is a separate codebase from Algorand's 'Yieldly' (the batch's llama candidate, algorand:226701642), so that candidate wa |
| 547 | aragon-dao-gov-plugin | 2 | 0/2 | Aragon OSx plugin code audited, not a single deployment. Multiple TokenVoting contracts exist on Ethereum but cannot be tied to the audited release. |
| 548 | coded estate | 2 | 0/2 | Project identified as Coded Estate: CosmWasm rental/NFT marketplace on Nibiru Chain (github.com/NibiruChain/coded-estate-evm documents the Nibiru Wasm deployment). No contract address surfaced; Nibiru explorer was not ma |
| 549 | digital oro | 2 | 0/2 | Hacken SCA report 'Digital Oro Sweepstakes Dec 2024' covers DOI_Raffle.sol plus DOI_Token, DOI_AdminManager and DOI_PayoutManager. The report page (hacken.io/audits/digital-oro-international/...) is behind a Cloudflare i |
| 550 | doefin | 2 | 0/2 | Project confirmed (github.com/Doefin); v2/v3 targets Base, but the Sept-2024 audited v1 deployment chain/address is not published. |
| 551 | ethereum-evm-caplabs-coveredagentprotocol-securityreview | 2 | 0/2 | Identity unresolved beyond the audit title; no chain confirmed. |
| 552 | exSat Network | 2 | 0/2 | BlockSec reviewed exSat consensus code (blksync/poolreg), which is Go node software rather than contracts. No address is applicable; chain recorded as exSat. |
| 553 | fatty | 2 | 0/2 | Only the SCA report slug exists; no website, repo, docs or explorer hit to identify the chain or a presale contract. |
| 554 | filecoin actors | 2 | 0/2 | ConsenSys Diligence review of specs-actors (Sep 2020), the Go implementation of Filecoin builtin actors. These are protocol-level actors embedded in the Filecoin node; the audited code is identified by repository path, n |
| 555 | for Amplified | 2 | 0/2 | Code4rena/Zenith 2024 review of 'Amplified', a strategy-vault protocol. The batch entry has no report URL and no project site, docs or GitHub was identified; no Amplified deployment appears on Ethereum Blockscout name se |
| 556 | gemnify | 2 | 0/2 | Protocol not resolvable to a live deployment within budget. |
| 557 | hashlock-dvx-2024-06-dvx-smart-contract-audit-report | 2 | 0/2 | Hashlock audit (2024-06) of DVX Exchange.sol/Account.sol. The unit carries no report URL, website or repo, and a single search surfaced only the auditor's site. No deployment could be tied to the audited code; NOT_FOUND. |
| 558 | hashlock-honeypot-finance-2024-08-honeypot-finance-yexfto-smart-contra | 2 | 0/2 | Hashlock Aug-2024 review of Honeypot Finance's YexFTO fair-launch pair. The batch record has no report URL or address, Honeypot's docs do not publish a YexFTOPair deployment, and DefiLlama lists the protocol with no chai |
| 559 | hashlock-jubi-2023-11-jubi-dao | 2 | 0/2 | Hashlock Nov-2023 review of 'Jubi DAO' (NftAllocator, ERC20OptionsAllocator). The batch record has no report URL and no project site, docs or explorer entry for this DAO could be identified; chain unknown. |
| 560 | hashlock-juicyfi-2024-03-juicyfi-4 | 2 | 0/2 | Audited contract is JuicyFiShares.sol. The Hashlock report (revised v3) gives launch date 'TBA' and contains no deployment address; no verified JuicyFiShares deployment surfaced on Base or Ethereum. |
| 561 | hashlock-lazymog-2025-09-lazymog-smart-contract-audit-report | 2 | 0/2 | September-2025 Hashlock audit of a presale contract; no site/docs/GitHub surfaced, and name searches returned only unrelated tokens. NOT_FOUND. |
| 562 | hashlock-silverswap-2024-06-silverswap-smart-contr | 2 | 0/2 | SilverSwap DCA module; Sonic explorer exposes no public v2 API and the DefiLlama address was an unrelated token. |
| 563 | hashlock-u2u-2024-10-amm-contract | 2 | 0/2 | U2U Network (EVM L1) launchpad/market contracts; no deployment address is given in the audit text and no explorer index for the chain was reachable. |
| 564 | hydrex-collaborative | 2 | 0/2 | DefiLlama lists Hydrex Integral/Omni on Base with no address field; HYDX token 0x00000e7efa313F4E11Bfff432471eD9423AC6B30 is a token, not the audited contract. |
| 565 | infinity | 2 | 0/2 | DefiLlama lists INFINIT at 0x61fac5f038515572d6f42d4bcb6b581642753d50, but eth_getCode on Arbitrum returns 0x, so the candidate was rejected rather than recorded. docs.infinit.tech is a JS SPA with no address table. |
| 566 | liquidity management | 2 | 0/2 | Codehawks contest 2025-02-25-liquidity-management. Scope is a GMX-v2-derived perpetual vault (contracts/PerpetualVault.sol, adl/AdlUtils.sol, bank/Bank.sol); the report carries no project identity, URL, chain or deployme |
| 567 | nord | 2 | 0/2 | Cantina 2024-08-06-nord. Report artifacts are Rust engine modules (mod.rs, exploit/exploit.py) with no site, repo, chain or deployment address; identity could not be resolved to an on-chain deployment within budget. |
| 568 | ola-x-november | 2 | 0/2 | Identity unresolved (name collides with Ola Finance and with Chainlink price-feed docs). |
| 569 | pashov-team-2024-03-06-nume-security-review | 2 | 0/2 | Pashov review of nume-p2p-contracts (Polygon zkEVM L3, Diamond pattern). No address in the review; one explorer lookup returned nothing. Polygon zkEVM mainnet has since been sunset, further reducing discoverability. |
| 570 | pashov-team-2024-10-11-stationx-security-review | 2 | 0/2 | Pashov review, Oct 2024. Audited contracts are DAO factory / ERC721 DAO on Base; no deployment address is published in the report extract. |
| 571 | pashov-team-2025-06-28-astrolab-security-review | 2 | 0/2 | Pashov review of Astrolab (yield category). No repository or deployment is linked; the only name-similar contract (AstroLabs 0x8065..., created 2024-12-23) has no deposit/withdraw/sharePrice functions, so it is not attri |
| 572 | poolparty 2025 06 poolparty updates smart contract | 2 | 0/2 | Hashlock 'PoolParty Updates' (2025-06) covers PoolPartyStaking with PartyX and SPLASH tokens. hashlock.com/audits/poolparty is a marketing page with no address. poolparty.fun serves a JS app (Base) that exposes no addres |
| 573 | sanctum sols | 2 | 0/2 | Cantina February-2026 review of Sanctum Sols. learn.sanctum.so/docs/for-developers/deployed-programs publishes Sanctum program IDs (S Controller 5ocnV1qi..., SanctumSpl stake pool SP12tWFx..., value calculators) but no S |
| 574 | sherlock | 2 | 0/2 | SHER token 0x46D2A90153cd8F09464CA3a5605B6BBeC9C2fF01 is a token, not the staking contract. |
| 575 | strateg | 2 | 0/2 | Zenith 2024-06 review of 'strateg'; no website, docs, repo or deployment address surfaced within the search budget. Vault and StrategERC3525 addresses unpublished. |
| 576 | system or codebase. | 2 | 0/2 | BailSec Meuna report; project name is a placeholder ('system or codebase.') and no deployment was resolvable. |
| 577 | tari-base-layer | 2 | 0/2 | Non-EVM base layer (Tari, XTM). 'Address' would be a node/network identifier, not a contract. |
| 578 | xBacked Smart Contracts | 2 | 0/2 | Runtime Verification 2022 audit of xBacked on Algorand (DefiLlama confirms Algorand). xBacked contracts are Algorand application IDs, which the report does not list and xbacked.io/docs.xbacked.io no longer resolve. No ap |
| 579 | xDonations-1 | 2 | 0/2 | xDonations is a small Macro-audited donations contract with no published deployment address or docs. |
| 580 | yearn-balancerlpfactory | 2 | 0/2 | Yearn V3 strategy code; yearn docs list registries/factories but not this strategy deployment. |
| 581 | zerolend | 2 | 0/2 | Docs deployments page confirms ZeroLend on zkSync/Manta/Linea/Blast/Ethereum/Base/X Layer but exposes no veZERO or locker entry. |
| 582 | 05--Heroglyphs | 1 | 1/0 | heroglyphs.com is a client-side app (Tickers section) with no contract listing; Blockscout name search returns only Heroglyph-branded ERC20 tokens, not the Ticker contract. |
| 583 | 08 01 Rolla-FV | 1 | 1/0 | Only a Certora PDF exists; project could not be tied to a live deployment. |
| 584 | 10--Obelisk | 1 | 1/0 | No project identity beyond the yAudit/electisec report; Megapool address not located. |
| 585 | 1INCH CUMULATIVE MERKLE DROP | 1 | 1/0 | MixBytes review of 1inch's cumulative merkle drop. The extract carries no address, github.com/1inch/merkle-drop returns 404 on both branches, and Blockscout indexes no contract named CumulativeMerkleDrop on Ethereum. |
| 586 | 1inch Aqua & Swap-VM | 1 | 1/0 | Aqua/Swap-VM is a 2026 pre-deployment design (DefiLlama has a '1inch Aqua' entry with no chain or address), so there is no live contract to trace. |
| 587 | 1inch-sol-feb-25 | 1 | 1/0 | Solana program id not published in the audited text within budget. |
| 588 | 2020-06-amp | 1 | 1/0 | Project identity unresolved: 'amp' + a wallet popcode underflow does not match the Flexa AMP token, so no address was recorded. |
| 589 | 2021-10-08-centrality-sca-centrality-bridge-oct2021-sca-centrality-bri | 1 | 1/0 | Centrality/CENNZ ecosystem; bridge contracts not identifiable from public sources in timebox. |
| 590 | 2022-01-08-vault-inc-vault | 1 | 1/0 | Vault Inc (2022) deposit/distributeRewards reentrancy; no deployment or chain evidence found. |
| 591 | 2022-05-04-ground-zero-sca-ground-zero-ido-contrac | 1 | 1/0 | 2022 IDO contract audit with no project site or deployment reference found. |
| 592 | 2022-05-14-arkania-protocol-sca-arkania-protocol-e | 1 | 1/0 | Arkania Protocol launchpad/staking; no verified contract address within the timebox. |
| 593 | 2022-07-30-defiai-sca-defiai-farming-jul2022-sca-d | 1 | 1/0 | Second DEFIAI unit (farming, Jul 2022); no address in the SCA artifact and nothing surfaced. |
| 594 | 2022-11-25-marhaba-sca-marhaba-dex-nov2022-sca-mar | 1 | 1/0 | Hacken SCA review of Marhaba DeFi (EVM). MRHB is a BSC token but the audited DEX/Swap address is not published and no verified Swap contract surfaced. |
| 595 | 2022-12-09-fairfi-sca-fairfi-yield-optimizer-dec20 | 1 | 1/0 | FairFi site resolves but publishes no contract address; DefiLlama lists a FairFi entry with no address field. No verifiable deployment found. |
| 596 | 2023-01-11-zkmakers-sca-zkmakers-erc20-staking-jan | 1 | 1/0 | zkSync-era ERC20 staking contract; the batch carries no report URL, and no verified contract matching the ProofVerifier/staking scope surfaced on Ethereum or zkSync. |
| 597 | 2023-02-18-metaspace-sca-metaspace-erc20-nft-staki | 1 | 1/0 | Metaspace ERC20/NFT staking audit; only unrelated MetaSpace tokens appear on Ethereum. Chain and staking contract not identified. |
| 598 | 2023-03-14-libertify-sca-libertify-vault-mar2023-sca-libertify-vault-m | 1 | 1/0 | SCA audit 2023-03-14 of the Libertify vault. The batch entry has no report_url or body and the extracted text names only 'C01 Data Consistency'; no vault address or address book surfaced, so nothing was recorded. |
| 599 | 2023-05-25-qooodo-sca-naplozz-erc20-staking-may202 | 1 | 1/0 | Naplozz ERC20 staking (Qooodo) is a small Hacken-audited project; no deployment address, docs or explorer contract surfaced. |
| 600 | 2023-06-06-diverse-solutions-sca-diverse-solutions | 1 | 1/0 | No identity or deployment verifiable within budget. |
| 601 | 2023-06-22-nf3x-sca-nf3x-airdrop-may2023-sca-nf3x-airdrop-may2023 | 1 | 1/0 | SCA engagement 2023-06-22 (NF3X airdrop, May 2023). Single finding 'Invalid Initialization'; no report body in the corpus extract, no website/GitHub and no address in the batch metadata. Nothing surfaced in one search, s |
| 602 | 2023-07-06-libertify-sca-re-audit-libertify-vault-jul2023-sca-re-audit | 1 | 1/0 | Vault product is behind a login (trust.libertify.com); no public contract address found. |
| 603 | 2023-09-17-autominingtoken-sca-autominingtoken-liquidity-pool-jun2023- | 1 | 1/0 | No deployment information. |
| 604 | 2023-10-14-gemdrop-sca-gemdrop-eip712-oct2023-sca- | 1 | 1/0 | GemDrop EIP-712 audit (2023-10). Token contracts exist but the audited depositor is not among them. |
| 605 | 2023-10-14-gemdrop-sca-gemdrop-eip712-oct2023-sca-gemdrop-eip712-oct20 | 1 | 1/0 | No deployment surfaced. Searches returned no Gemdrop protocol docs, site or explorer contract; the name appears only in the audit title. |
| 606 | 2023-10-17-ripio-sca-lachain-bridge-oct2023-sca-lachain-bridge-oct2023 | 1 | 1/0 | Coinspect audit of the Ripio LaChain bridge; no deployment address, explorer or docs page located in the timebox. |
| 607 | 2023-11-16-nf3x-sca-nf3x-dex-nov2023-sca-nf3x-dex- | 1 | 1/0 | SCA review of the NF3X DEX; no deployment address or live chain found. |
| 608 | 2023-12-08-busker-sca-arcelik-erc721-marketplace-d | 1 | 1/0 | Busker/SCA engagement for an Arcelik ERC721 marketplace (Dec 2023). Batch entry has no report URL or body and no public repo, docs or deployment address for this corporate marketplace was found. |
| 609 | 2024-02-03-eesee-sca-re-audit-eesee-erc20-feb2024- | 1 | 1/0 | eesee is a Blast marketplace/escrow. Only the ESE token (0x908dDb096BFb3AcB19e2280aAD858186ea4935C4, Ethereum) surfaced; the audited receiveAssets() escrow contract was not verifiable on Blast (no working explorer search |
| 610 | 2024-04-16-mantle-op-geth-audit | 1 | 1/0 | Client-level audit (Mantle op-geth). Address tracing not applicable; recorded NOT_FOUND by design rather than guessing a bridge address. |
| 611 | 2024-04-22-dexponent-sca-dexponent-staking-mar2024 | 1 | 1/0 | Dexponent staking (SCA, Mar 2024). The litepaper describes the protocol but publishes no contract addresses; no deployment could be attributed. |
| 612 | 2024-04-29-sigmaprime-sushi-bentobox-strategies-staking-contract-revie | 1 | 1/0 | Sushi BentoBox itself (0xF5BCE5077908a1b7370B9ae04AdC565EBd243750) is a different contract and was not mapped. |
| 613 | 2024-04-29-sigmaprime-sushi-sushi-swap-stable-pool | 1 | 1/0 | Sigma Prime review of Sushi's stable pool (Apr 2024). Sushi deployments are numerous and per-chain; address not resolved. |
| 614 | 2024-04-29-sigmaprime-sushi-sushi-swap-stable-pool-review | 1 | 1/0 | Sushi stable-pool maths review. An explorer-verified StablePoolFactory at 0x8df6...987c exists on Ethereum, but no Sushi-specific source ties it to the audited deployment (source not retrievable, creator unlabelled), so  |
| 615 | 2024-04-30-galileo-protocol-sca-galileo-protocol-m | 1 | 1/0 | No marketplace/escrow deployment verifiable; ERC20 tokens rejected as non-core. |
| 616 | 2024-05-14-longdragon-sca-war-chest-rewardpool-apr2024-sca-war-chest-r | 1 | 1/0 | War Chest RewardPool (Longdragon) is a Hacken-audited contract with no published deployment; searches returned only unrelated LD tokens and generic reward-pool docs. |
| 617 | 2024-05-20-hello-labs-sca-hello-labs-bridge-voting-apr2024-sca-hello-l | 1 | 1/0 | April-2024 SCA review of Hello Labs' Solana<->Ethereum bridge voting/withdrawal. The report carries no deployment address and no verified withdrawFromSolana contract was found. |
| 618 | 2024-05-29-contracts-v1 | 1 | 1/0 | Unit name looks like a repository ('contracts-v1') with no project identity; no address could be derived. |
| 619 | 2024-06-01-octopus-bridge-sca-octopus-bridge-btc-b | 1 | 1/0 | Octopus Bridge BTC contract not located; searches returned only unrelated Octopus items. |
| 620 | 2024-06-11-sigmaprime-sofa-review | 1 | 1/0 | llama_candidate 0x57b96d4af698605563a4653d882635da59bf11af is the RCH token, not the SOFA protocol. The AAVE-backed vault contracts reviewed are not published. |
| 621 | 2024-07-10-base-paper-scissors-sca-base-paper-scis | 1 | 1/0 | Hacken Jun-2024 audit; no contract address published on the audit page. |
| 622 | 2024-09-30-aerobloc-sca-aerobloc-aerobloc-contract | 1 | 1/0 | No public identity for 'Aerobloc'; the batch has no report text or URL. No chain or deployment could be established. |
| 623 | 2024-11-28-hesty-sca-hesty-hesty-contract-oct2024- | 1 | 1/0 | Hesty contract deployment not disclosed. |
| 624 | 2025-01-27-ai-registry-mech-security-audit | 1 | 1/0 | Batch entry carries no report_url and no body, only the title and function name (AI-agent 'mech' registry, Olas-style marketplace). No chain, contract or address is stated and no deployment could be tied to this function |
| 625 | 2025-02-05-lingotoken | 1 | 1/0 | No program id or repo surfaced in two searches; audit text is silent on chain. |
| 626 | 2025-02-15-riskiit-protocol-security-assessment | 1 | 1/0 | No report URL or identity in the batch; 'Riskiit' is not a public protocol name that resolves to a deployment. |
| 627 | 2025-04-04-doefin-sca-doefin-doefin-contracts-sept | 1 | 1/0 | SCA engagement 'doefin contracts' Sep-2024. Batch entry has no report URL, body or source URL; no repo, docs or deployment address for Doefin surfaced. |
| 628 | 2025-06-03-sigmaprime-recall-sigma-prime-recall-la | 1 | 1/0 | Non-EVM actor system; no address to record. |
| 629 | 2025-08-13-cueva-sca-cueva-escrow-jul2025-sca-cuev | 1 | 1/0 | Coinspect SCA of the Cueva escrow contracts (Jul 2025); no public docs, repo or deployment address located. |
| 630 | ABDK CONSULTING VAULT SMART CONTRACT | 1 | 1/0 | Reference/sample contract from an auditor's portfolio; no deployment. |
| 631 | Abstract Account Contract | 1 | 1/0 | Oak Security 2024-12-31 review of the Abstract account contract v0.26.0 (ERC-4337-style authenticator module). The report names no deployed address and no chain, and the Abstract account implementation is deployed per-wa |
| 632 | Aftermath Market Making | 1 | 1/0 | Sui Move market-making modules; the audited package ID was not identified from the OtterSec report. |
| 633 | Ai registry mech | 1 | 1/0 | Cantina Valory Jan-2025 review of the mech/registry contracts; the deployed Mech address could not be verified (Gnosis Blockscout blocked name search). |
| 634 | Akita | 1 | 1/0 | Solana lending program; only the instruction names are known from the report. |
| 635 | Allbridge (bridge-stellar-server, Feb 2023) | 1 | 1/0 | Allbridge Core is live across many chains but the audited component is the Stellar bridge server; no contract address is attributable. NOT_FOUND is about the vulnerable component, not the protocol's token. |
| 636 | Altered Protocol | 1 | 1/0 | Oak Security review dated 2021-08-19 of a rebase-token 'Altered Protocol'. The extract has no chain, repo, website or address, and no explorer index lists a deployment under that name. |
| 637 | Ample Earn | 1 | 1/0 | Ample Earn (strategy allocator) — no public deployment found. |
| 638 | Animoca Core Library - September 26, 2022 | 1 | 1/0 | Solidified review of the Animoca core library. A library has no standalone deployment address. |
| 639 | Animoca Staking Pool | 1 | 1/0 | Oak Security review of an Animoca staking pool. No chain or deployment published. |
| 640 | Archethic AE Bridge | 1 | 1/0 | Archethic is a native L1; AE Bridge contracts are Archethic transaction addresses and none are published in the audit text. |
| 641 | Argent. November 26, 2018. | 1 | 1/0 | Argent v1 wallet infra. Repo checked for address book (DEPLOYMENT.md, deployment/) - none. Argent has since moved to Starknet; the v1 Ethereum factory/module deployment is not published. |
| 642 | Aries Markets | 1 | 1/0 | Aries Markets (OtterSec 2022), Aptos lending. DefiLlama confirms chain only (address null). |
| 643 | Astroport PCL Neutron Duality | 1 | 1/0 | Oak Security 2025-03-17 audit of the Astroport PCL / Duality orderbook integration on Neutron. Neutron contracts are CosmWasm (neutron1... addresses); neither the report nor docs.astroport.fi publishes the SpotOrdersFact |
| 644 | Audius Solana Programs | 1 | 1/0 | Zellic 2022 review of Audius Solana programs; RewardsManager program id unresolved. |
| 645 | Axiom Remote & Broadcast | 1 | 1/0 | Contract is a Gnosis-chain header verifier; Axiom's core AxiomV2Core lives on Ethereum and is not the audited contract. |
| 646 | BCMH | 1 | 1/0 | Blockchain Monster Hunt is a BSC game. Only an unrelated Ethereum ERC-721 item contract (BlockchainMonsterItemBase, 0x6E36...) surfaced; the game contract address was not located. |
| 647 | BIFROST | 1 | 1/0 | The finding concerns the Bifrost bridge server's event-address validation, not a deployed EVM contract; Bifrost is a Polkadot parachain with no EVM address for this component. |
| 648 | BSD DeFi | 1 | 1/0 | PeckShield 2021 BSD DeFi (PolDataMain, POL/PUSD/PNX pools). No live site, docs or deployment address surfaced. |
| 649 | Babylon Genesis Chain | 1 | 1/0 | Babylon Genesis is a Cosmos/Bitcoin-secured chain; the flaw is in chain-level adaptor-signature handling, so there is no EVM contract address. |
| 650 | Bae NFT Lending | 1 | 1/0 | Chain identified from the builder's portfolio page (aegas.io); address not found. |
| 651 | Bahamut April23 | 1 | 1/0 | Bahamut is an EVM L1; the 'activity scores' finding is consensus-node/validator-level, not a deployed contract. Chain recorded, no contract address. |
| 652 | BarnBridge Smart Yield Bonds | 1 | 1/0 | OpenZeppelin 2021 audit of BarnBridge SMART Yield. Blockscout name search returns only per-maturity 'Barnbridge SmartYield Bond Token' tokens (e.g. Dai-09NOV22), not the SmartYield controller/pool that carries the accoun |
| 653 | BattleFly OTC - April 24, 2023 | 1 | 1/0 | docs.battlefly.game/contracts and /references/contracts both 404. BattleFly runs on Arbitrum but no OTC market address surfaced. |
| 654 | Biconomy PasskeyRegistry and Ses sionKeyManager | 1 | 1/0 | Biconomy Nexus account modules are deployed on many chains; the audited PasskeyRegistryModule has no published address in the docs address book. |
| 655 | Bigcoin | 1 | 1/0 | Guardian Audits review (2025-10-29) of Bigcoin; report body withheld in the corpus extract. No website/GitHub/address surfaced; the Ethereum token named 'bitcoin (2015 Wrapper)' at 0xC0BC84e95864BdfDCd1CCFB8A3AA522E79Ca1 |
| 656 | BlastOff March14 | 1 | 1/0 | Zokyo BlastOff March-2024 audit on Blast; no verified Blast explorer API was reachable and the staking contract address was not resolved. |
| 657 | Booster-Protocol | 1 | 1/0 | Repo boosterfarm/boosterProtocol exists but contains no deployed addresses; chain unconfirmed. |
| 658 | Burve (SimplexDiamond) | 1 | 1/0 | Audit of Burve's SimplexDiamond (Berachain). DefiLlama lists Burve on Berachain with no address, and docs.burve.fi (GitBook) has no deployment/address page reachable in two searches. No diamond address recorded rather th |
| 659 | C-Org Audit | 1 | 1/0 | ConsenSys Diligence 2019 audit of Fairmint's C-Org (DAT and FAIR token). The report contains no deployment addresses; Blockscout name search surfaces only Fairmint ERC-20 tokens (e.g. 0x3983C6DA8235F59e16a034EE773e60A69e |
| 660 | CFFv2 | 1 | 1/0 | 'CFFv2' has no identifiable protocol, docs or deployment; searches return only generic reentrancy material. |
| 661 | CSX | 1 | 1/0 | Only the StakedCSX contract name is available; no deployment could be identified. |
| 662 | CYBRO One Click Lending by | 1 | 1/0 | Pessimistic 2024 audit of CYBRO One Click Lending. Deployment page exists but covers a different product line; the lending vault address is missing. |
| 663 | Cairo | 1 | 1/0 | Cairo/StarkEx code audit; no deployment address attributable to the reviewed code. |
| 664 | Catalyst / IPSeed | 1 | 1/0 | Pashov Audit Group review of Catalyst/IPSeed (IPSeed.spawn with a caller-supplied IIPSeedCurve). The report has no deployment addresses and states no chain; no project repo or site publishing an IPSeed address was found. |
| 665 | Cega LP Offramp by | 1 | 1/0 | Cega LP Offramp (Pessimistic 2024). Cega V2 ran on Ethereum/Arbitrum and V1 on Solana; the OfframpEntry contract address was not resolved. |
| 666 | Cetus | 1 | 1/0 | Sui Move package; the report names limit_order::repay_flash_loan but no package id. Sui public JSON-RPC is deprecated and the package id could not be verified. |
| 667 | ChainArQ Feb24 | 1 | 1/0 | Source repo (contracts-evm) contains Terminus.sol / TerminusTlp.sol but no deployment or broadcast addresses; no explorer hit for ChainArQ. |
| 668 | Choise | 1 | 1/0 | Pessimistic 2022 review; no contract address or confirmed chain. |
| 669 | Claim and Rewards Programs | 1 | 1/0 | Zellic review of a multi-VM 'claim and rewards' program set (Cosmos/Move/Solana, Cairo sources). Target module is 'claimable-tokens'; no deployment or program id is published. |
| 670 | Code Inc | 1 | 1/0 | OtterSec 2025 review of a 'code-vm' (in-memory balance VM). No repo, chain or deployment address is published in the report metadata. |
| 671 | Codefi ERC1400 | 1 | 1/0 | Framework audit, no single deployment. |
| 672 | Coinflip | 1 | 1/0 | Pashov team review 2025-02-19 of play-turbo/coinflip-contracts states the project 'plans to deploy on multiple chains'. The GitHub repo path returns 404 (private or renamed) and no deployment/broadcast manifest or live a |
| 673 | Coinflip (pashov review) | 1 | 1/0 | No chain or address found; project label 'Coinflip' collides with unrelated payment/CoinFlip products in search. |
| 674 | Comdex Lend and Liquidation | 1 | 1/0 | Cosmos SDK app-chain (comdex-1). Lend/Liquidation are CosmWasm modules; there is no EVM contract address. Chain recorded, address null. |
| 675 | Comdex Locking and Vesting | 1 | 1/0 | Comdex locking and vesting is a Cosmos SDK module (x/vesting) inside the comdex chain, not a deployable contract; no contract address exists to record. |
| 676 | Convergent | 1 | 1/0 | OtterSec review of Convergent (2024). No deployment surfaced. |
| 677 | Cosmos Labs | 1 | 1/0 | Zenith 2026 review of the Cosmos Labs ics27-gmp Solana program; program id unresolved. |
| 678 | Credit Swap Dec22 ed16f43d95 | 1 | 1/0 | Flipped to profit_confirmed=no: the finding text describes pure griefing/DoS with no attacker gain. |
| 679 | Cross Yield | 1 | 1/0 | SlowMist 2021 review of Cross Yield / HotDrop lottery. No report_addresses, no docs site, and a BscScan/Blockscout name search for HotDrop returned nothing. Likely defunct. |
| 680 | Cryptocurrency Exchange. The objective of the | 1 | 1/0 | Coinspect 2018 review of Lesfex (lesfex.com). The three report addresses are plain accounts, not deployed code; the exchange is defunct. |
| 681 | Curio | 1 | 1/0 | No chain or address surfaced. |
| 682 | Curra Jan4th .pdf | 1 | 1/0 | Only a PDF report title (Curra, Jan 4) is known; no project identity, chain or address surfaced. |
| 683 | DEDAUB.COM CavalRe AMM | 1 | 1/0 | CavalRe's public repo (cavalre-contracts, plus cavalre-multiswap-beta) contains source and docs but no deployment address book; DefiLlama lists CavalRe on Avalanche with a null address. |
| 684 | DEDAUB.COM Lido | 1 | 1/0 | Lido on Avalanche (AvaLido). No verified contract address found within the timebox. |
| 685 | DEDAUB.COM Muffin Protocol | 1 | 1/0 | Dedaub 2022 audit of Muffin Finance. Report body names no address; Blockscout Ethereum name search returns only unrelated 'Muffin' meme tokens. No docs or deployment manifest surfaced. |
| 686 | DEDAUB.COM follows.app | 1 | 1/0 | Solana social app; program id not published in the report. |
| 687 | DEFIAI | 1 | 1/0 | Hacken SCA report (Critical-1). Contract and function are named but the project publishes no deployment address. |
| 688 | Daimon DAO | 1 | 1/0 | Code4rena/Zenith review of Daimon DAO (2026). No chain or address surfaced in search. |
| 689 | DeFireX | 1 | 1/0 | The DefiLlama candidate bsc:0x74b3abb94e9e1ecc25bd77d6872949b4a9b2aacf resolves to a TokenProxy (DFX token) and was rejected as a token. No DeFireX core contract address found. |
| 690 | DeSyn - Restaking | 1 | 1/0 | DeSyn operates across many chains with no single documented restaking deployment; no adapter or explorer entry resolved the audited contract. |
| 691 | Defactor (Pools) Zokyo Nov22 .pdf | 1 | 1/0 | Defactor Pools audit (Zokyo 2023). No pool/factory address published; FACTR token addresses rejected as dependency tokens. |
| 692 | Delphia Token Contracts | 1 | 1/0 | 2021 pre-launch token-sale contracts (bondToMint). No public deployment of the audited Delphia token contracts surfaced and the report gives no address. |
| 693 | Dexdao | 1 | 1/0 | Pessimistic 2023-07-07 report on 'Dexdao' (Launchspace, Uniswap-style LP, references Uniswap tick math). llama_candidates points at DXDao 0xa1d65e8fb6e87b60feccbc582f7f97804b725521, which is the DXD governance token of a |
| 694 | Dharma Audit | 1 | 1/0 | 2018 OpenZeppelin audit of Dharma v1; the protocol has wound down and DebtToken instances are created per loan by the DebtTokenFactory, so there is no canonical deployment address. |
| 695 | DistrictOneAudit | 1 | 1/0 | Three Sigma audit of DistrictOne; no report body in corpus, no project site or repo identified, no address surfaced. |
| 696 | DojoSwap | 1 | 1/0 | Zellic 2024 review of DojoSwap's Injective launchpad (CosmWasm). docs.dojoswap.io did not resolve; DefiLlama lists only the AMM/LSD contracts as inj1... addresses and publishes no launchpad contract. CosmWasm addresses a |
| 697 | Drizzle Finance by | 1 | 1/0 | Pessimistic audit (2024) of Drizzle Finance's CompoundV3Connector. Ethereum name search returns three verified 'CompoundV3Connector' contracts from unrelated integrations and nothing tying them to Drizzle; the report pub |
| 698 | Drop Initia Liquidity Provider | 1 | 1/0 | Oak Security audit 2025-04-17 of Drop's Initia Liquidity Provider v1.0 (Move). The PDF is public in oak-security/audit-reports but publishes no package address, and no Initia module address for the audited liquidity-prov |
| 699 | Dymension Point 0D | 1 | 1/0 | Oak Security review of Dymension (2024). The finding lives in node-side Go code (app/ante/handlers.go), not in a deployed contract, so there is no contract address to record; Dymension mainnet is a Cosmos chain (dymensio |
| 700 | ECDSA Token Distrubutor (SUI) | 1 | 1/0 | CODESPECT review of a Sui Move Distributor<T> template. Sui deployments are package/object IDs; the report publishes none and no package ID could be tied to it. |
| 701 | Eclipse Equinox Lockdrop | 1 | 1/0 | Eclipse is an SVM chain; no lockdrop program ID is published in the audit text and none surfaced. |
| 702 | Eco | 1 | 1/0 | Audit covers BeamNetwork BeamBootstrap/ForwardProxy/Policed contracts. Addresses in the report (0x820b..., 0x820c...) resolve to ERC-820 registry dependencies, not Eco contracts, and were rejected. |
| 703 | Elytra | 1 | 1/0 | No deployment information resolved. |
| 704 | Enclave | 1 | 1/0 | Solana lending program reviewed by Pashov (Oct 2025); no program id published. |
| 705 | FChain | 1 | 1/0 | Two searches surfaced no FCHAIN deployment. Fry Networks' fNODE is Algorand-only and does not match the transferFrom/license finding, so it was rejected. |
| 706 | FFLONK Verifier | 1 | 1/0 | OpenZeppelin review of the zkSync FFLONK verifier (sergeyshemyakov dataset). The report names the verifier contract but ships no address and the batch carries no report_addresses. zkSync docs list system-contract address |
| 707 | Fairblock fairyring | 1 | 1/0 | Oak Security 2023-10-02 audit of the fairyring Cosmos SDK chain. The finding is in chain-level Go modules, not a deployed EVM/CosmWasm contract; fairyring is an appchain and no contract address applies. |
| 708 | Finance Convergence Protocol Smart Contract Security | 1 | 1/0 | Convergence Finance CVG vesting; no verified VestingCvg address found. |
| 709 | Flock - FL Alliance Client - SlowMist | 1 | 1/0 | SlowMist reviewed an off-chain client plus on-chain voting; no deployment address is published in the report or the project docs. |
| 710 | Flooring V3-Staker | 1 | 1/0 | OtterSec audit of Flooring's V3 staker; no deployment address surfaced. |
| 711 | Fluo | 1 | 1/0 | OtterSec 2023 review of Fluo (boosted-share staking with bonusFLUODistributor). No report URL or address book; Blockscout name search returns no Fluo protocol contract (only unrelated FLUO/FLUOGRAM tokens). |
| 712 | Foil Network Seed Contract | 1 | 1/0 | Batch entry has no report URL, body or source URL (Foil Network 'Seed Contract', critical business_logic 'No token transfers'). With no report text and no project identity, neither a chain nor an address could be establi |
| 713 | Forgotten Playland (ToyBox) | 1 | 1/0 | Pashov review of a game-item shop; no public deployments page surfaced. |
| 714 | Fortube Bank 2.0 | 1 | 1/0 | ForTube Bank 2.0; explorer name search returned only ForTube market tokens, not the controller. |
| 715 | Foundation ef kzg | 1 | 1/0 | Review of the Foundation's KZG/EF work on the blst library. This is a library, not a deployed contract: no chain, no address, and no deployment exists to trace. Recorded as NOT_FOUND by nature, not for lack of searching. |
| 716 | Frameit - February 3, 2023 | 1 | 1/0 | Solidified audit 'Frameit [03.02.2022]'. No repo, docs or deployment address surfaced; the report names UniswapV3Oracle but no address. |
| 717 | Fungify Nov23 | 1 | 1/0 | Hexens Nov-2023 review of Fungify. Ethereum name search returns only Fungify token contracts (0x0e4e7F2AecF408AFF4f82f067677050239bdC58A 'Fungify Token', plus Fungify NFT Index/USDC/Ether), which are tokens, not the audi |
| 718 | Futaba | 1 | 1/0 | Futaba ChainlinkLightClient audit; no project site, repo, chain or deployment address surfaced. |
| 719 | GLIF InfinityPool | 1 | 1/0 | InfinityPool is a Filecoin actor; no actor ID is published on the pool page. The GLIF ERC-20 on Filecoin (0x2a0aaf86...) is a token, not the pool. |
| 720 | GMI | 1 | 1/0 | OtterSec audit of GMIndex; no GMIndex contract or deployment reference found on Ethereum. |
| 721 | GTE – Perp | 1 | 1/0 | Zellic 2025 review of GTE Perps (Liquid Labs). The llama candidate 'Gate Perp' is a different protocol and was rejected. GTE perps were audited pre-launch (Code4rena Aug-2025); no deployed clearing-house address was publ |
| 722 | Gamma UniswapV4 LimitOrders | 1 | 1/0 | Guardian Audits 2025-04-14 review, engagement ran before/around Uniswap v4 hook deployment. Blockscout Ethereum name search returns several 'LimitOrderManager' contracts, but none exposes a Gamma/limit-order-hook referen |
| 723 | GammaSwap Vault Security | 1 | 1/0 | Audit covers FundingVault/FundingVault20; no deployment address for those contracts was found (current docs only cover the perps product). |
| 724 | Global Interlink | 1 | 1/0 | Zokyo 2023 review of Global Interlink (GIL) token vesting. The report publishes no address and the project has no reachable docs/deployment page; one search surfaced nothing tying GIL to a chain. NOT_FOUND. |
| 725 | GoMarket May25 | 1 | 1/0 | Sei/CosmWasm Rust codebase (buy_shares.rs, lmsr); no published code id or contract address surfaced. |
| 726 | GovWorld | 1 | 1/0 | GovWorld (BSC lending). BSC explorer API was unavailable and no address was confirmed. |
| 727 | Ground Zero | 1 | 1/0 | No deployment surfaced in budget. |
| 728 | Groupcoin | 1 | 1/0 | Pashov review of a small launchpad; no website, repo or deployment reference, and searches returned only unrelated token results. |
| 729 | Hacken | 1 | 1/0 | Project identity is unresolved (Hacken is the auditing firm, not the protocol). |
| 730 | Helio Money | 1 | 1/0 | SlowMist 2023 report; Helio/Hay is a BNB Chain deployment (CeVault, aBNBc ratio). BscScan blocks unauthenticated search (HTTP 403) and the report publishes no address. Candidates returned by search were checked on chain: |
| 731 | IBC Eureka | 1 | 1/0 | Zellic 2025-03-19 review of IBC Eureka (ibc-go). The finding concerns the Ethereum light-client sync path, but neither the report nor the public ibc-go repo names the deployed Ethereum light-client/ICS20 contract address |
| 732 | Initia | 1 | 1/0 | Initia is a Cosmos appchain; the audited MoveVM verifier is node code, not a deployable contract. The llama candidate "initia:uinit" is a token denom, not a contract. |
| 733 | Instadapp Avocado v3 | 1 | 1/0 | Avocado is a wallet (one proxy per user), not a single protocol deployment. No address book or docs page was reachable, so no representative address is recorded. |
| 734 | Jito Tip Router | 1 | 1/0 | Jito Tip Router is a Solana program (jito-foundation/jito-tip-router). The on-chain program id is injected at build time (declare_id!(env!("TIP_ROUTER_PROGRAM_ID"))) and is not published in the README, docs or repo confi |
| 735 | Kalp-GINI-Vesting | 1 | 1/0 | Audited artefact is Go chaincode (smartcontract.go) for the Kalp permissioned network (Hyperledger Fabric); there is no EVM address to trace. |
| 736 | KiloEx Phase1 | 1 | 1/0 | KiloEx Phase1 (SlowMist, Apr 2025). The only address on KiloEx's contract-address page is the KILO token, which is a dependency, not the vulnerable PriceRouter. |
| 737 | Kim NFT Marketplace | 1 | 1/0 | 2024-11-12 Kim NFT marketplace audit; only an unrelated KIM token on Mode surfaced. No marketplace deployment located. |
| 738 | Kinto Bridger | 1 | 1/0 | Pessimistic 2024 audit of Kinto's Bridger; the PDF was downloaded and text-extracted and contains no 0x address. DefiLlama's kinto-bridge entry points at Arbitrum 0x6ba19ee69d5dde3ab70185c801fa404f66fedb58, but Sourcify  |
| 739 | Kirobo FCT | 1 | 1/0 | Only token contracts surfaced; the audited FCT engine address is not published. |
| 740 | Kyte.One | 1 | 1/0 | No address surfaced; finding body not released. |
| 741 | Legend of Arcadia | 1 | 1/0 | MoveBit 2023 review of Legend of Arcadia's Sui game contracts (github.com/Legend-of-Arcadia/game-contract-sui). The repo root exposes only contracts/ and scripts/ with no Move.toml published-at address at the paths probe |
| 742 | Lido Fixed Income | 1 | 1/0 | Zellic 2024 audit of the LidoVault contract; no chain, repo or deployment reference is given in the report extract. |
| 743 | LightDAO Phase2 | 1 | 1/0 | SlowMist audit of a UniswapV2 pair fork; no project site, chain or pair address surfaced. |
| 744 | Limit Break June12th | 1 | 1/0 | The audit covers the ERC721-C / Creator Token standard libraries, not a single protocol deployment; per-collection deployments cannot be enumerated from the report. |
| 745 | Lindy | 1 | 1/0 | No confirmed chain or deployment. |
| 746 | Lingo Token | 1 | 1/0 | No identity or deployment surfaced from the slug `lingotoken`; NOT_FOUND. |
| 747 | Loopring on May 21st, 2020. | 1 | 1/0 | Loopring's 2020 BaseVault audit. Only the LRC token surfaced, which is not the vault contract; address deliberately left null. |
| 748 | Lopswap by | 1 | 1/0 | Lopswap (Pessimistic, Aug 2025). No deployment address could be attributed; generic searches returned only the audit PDF. |
| 749 | Lossless | 1 | 1/0 | ABDK 2022 audit of the Lossless security/committee contracts. Blockscout returns three separately verified LosslessControllerV2 deployments (0xa0F9..., 0xA436..., 0x9564...) plus LosslessControllerV1, with no way to tell |
| 750 | M*9 | 1 | 1/0 | Chain inferred as Ethereum from M0 docs ('Ethereum is the hub') but the portal address itself was not verified. |
| 751 | MPC Circuit | 1 | 1/0 | Circuit-level audit (Worldcoin SMPC); no on-chain deployment. |
| 752 | MUD | 1 | 1/0 | MUD (latticexyz) is developer infrastructure, not a deployed protocol; the audited Store/World contracts exist only per-application. No chain or address applies. |
| 753 | Mainnet - Sable Finance | 1 | 1/0 | Sable v1 on BSC. Docs expose no address page; the DefiLlama address is the SABLE token. |
| 754 | Majr Dao | 1 | 1/0 | Hacken 2022 Majr Dao review has no deployment section. Ethereum name searches return unrelated Majr NFT contracts (MAJR ID, MajrCanon, MajrContests), not the audited referral/staking code, so they were rejected. |
| 755 | Mantle OP-Geth | 1 | 1/0 | Client/node software audit (OpenZeppelin). Mantle chain recorded; no contract address applicable. |
| 756 | Margined Power | 1 | 1/0 | margined-protocol/power is Rust/CosmWasm and its README says it is to be deployed on Osmosis. No live Osmosis contract address is published in the repo, docs or DefiLlama. |
| 757 | Mars Red Bank Updates | 1 | 1/0 | Neutron deployment address for Red Bank not resolved within budget. |
| 758 | Martian | 1 | 1/0 | Move-language audit; no EVM address to trace. |
| 759 | Match | 1 | 1/0 | SlowMist 2024 Match audit; no auction contract address found. llama_candidates entry had no address. |
| 760 | MilkyWay Staking Updates | 1 | 1/0 | Finding is in Packet Forward Middleware, a Cosmos SDK middleware module compiled into the chain binary; there is no contract address to trace. |
| 761 | Milkyway Celestia Restaking | 1 | 1/0 | Native Cosmos module (milkyway chain). DefiLlama lists the protocol under chain 'Milkyway' with no address; no contract-level deployment exists to trace. |
| 762 | Mina | 1 | 1/0 | Protocol-level (OCaml node) finding; address tracing does not apply. Chain recorded for completeness. |
| 763 | Monad | 1 | 1/0 | Spearbit reviewed the Monad client's staking precompile. This is node/client code, so there is no deployment address; chain recorded as Monad (143). |
| 764 | Moonbirds | 1 | 1/0 | BIRB airdrop distributor is a Solana program; program id unresolved, token mint deliberately not recorded as the target. |
| 765 | Mysten Republic | 1 | 1/0 | Sui Move game/protocol; no package ID or address was recovered from the OtterSec report. |
| 766 | NFT Capsule | 1 | 1/0 | Pashov review of NFT Capsule (2023). Identity beyond the contract name is unavailable. |
| 767 | NFTR Market | 1 | 1/0 | NFTR name registry; audited contract source (NFTRegistry.sol) identified but no deployment address published. |
| 768 | Name of the company | 1 | 1/0 | UniFarm (UFARM) AMMUtility; only the UFARM token surfaced, which is not the audited contract. |
| 769 | Nebra SpecAudit PartI v 1 0 | 1 | 1/0 | Specification audit; no deployment to trace. |
| 770 | Neutron: Duality v0.5.0 + integration of Cosmos SDK | 1 | 1/0 | Duality is a CosmWasm DEX on Neutron; the audited v0.5.0 code is a CosmWasm contract whose bech32 contract address is not published in the report, docs or DefiLlama (DefiLlama lists Duality with a null address). No deplo |
| 771 | NilFoundation BlockchainVerifier v 2 0 | 1 | 1/0 | ABDK 2024 review of a ZK verifier; no deployed verifier address is published in the report, docs or explorer name search. |
| 772 | NovaMarkets | 1 | 1/0 | 2026 Three Sigma report; no deployment information available and no address surfaced. |
| 773 | Nym Mixnet and Vesting | 1 | 1/0 | No contract or program id published; Nym's CosmWasm addresses are not indexed by the EVM explorers used. |
| 774 | OT | 1 | 1/0 | Project identity unresolved - 'OT' is too generic for explorer search; report PDF is the only artifact. |
| 775 | Obelisk | 1 | 1/0 | No reliable identity match; unrelated 'Obelisk' tokens rejected. |
| 776 | Obsidian | 1 | 1/0 | Halborn audit listing shows 'Tradecraft AMM V7 Daml'; no EVM chain or address. |
| 777 | Octopus Network NEAR Smart Contract Security | 1 | 1/0 | NEAR smart-contract audit (Halborn); contract is a NEAR account, not an EVM address, and the audited account id was not resolved. |
| 778 | OjoSmartPendle | 1 | 1/0 | Three Sigma audit (Mar 2025) of Ojo Network's smart-pendle risk engine. The repo github.com/ojo-network/smart-pendle is public and docs.ojolabs.xyz links the audit, but neither publishes a deployment address and docs.ojo |
| 779 | Oku Trade | 1 | 1/0 | Oku's EVM Oku Router (0xb1f3a7B816B0681188F54dFa400991B93ADf00ed on Ethereum/Arbitrum/Base) is a different contract from the audited Solana automation program. |
| 780 | Omo | 1 | 1/0 | No OmoVault deployment found; only an unrelated oVAULT token appeared. |
| 781 | One Planet Smart Contracts | 1 | 1/0 | Oak reviewed the CosmWasm repo one-planet-contract-queuing (src/execute.rs). No chain or deployed contract address is published in the report or repo search. |
| 782 | Onrail | 1 | 1/0 | No public chain or deployment information found. |
| 783 | OpenZeppelin Stack for Zama: Smart Accounts | 1 | 1/0 | OpenZeppelin review of the Zama Stack for Smart Accounts (fhEVM account abstraction framework/SDK). The object is a reusable account implementation, not a protocol deployment; no deployed SmartAccount/factory address is  |
| 784 | OpenZeppelin Uniswap Hooks v1.1.0 RC 1 | 1 | 1/0 | Library release-candidate audit, not a deployed protocol; no address to trace. |
| 785 | Oro Inti | 1 | 1/0 | Audited code is an Anchor program (claim/unstake position accounts); the program ID is not published in the report and no deployment was located. |
| 786 | Osmosis Authentication Abstraction | 1 | 1/0 | Zellic review of Osmosis authentication abstraction (2023). Cosmos module, so there is no contract address to record; chain recorded as Osmosis. |
| 787 | Out | 1 | 1/0 | 'Out' could not be resolved to a protocol; no docs, repo or deployment surfaced, and the title ('esoteric currencies') gives no chain hint. |
| 788 | Paribus Feb27 | 1 | 1/0 | Zokyo Feb-2024 report on Paribus's PNFT (CryptoPunk-backed NFT). CryptoPunks are Ethereum-only, so PNFT is an Ethereum deployment, but neither Blockscout name search (PNFT/PNFTToken) nor web search surfaced the contract, |
| 789 | Paxo Protocol | 1 | 1/0 | PeckShield 2023 review of Paxo, a Compound-fork lending market (CErc20). No report_addresses, no docs, and a BSC Blockscout search for Paxo/CErc20 returned no matching market. Chain unconfirmed. |
| 790 | Penumbra Labs R1CS Implementation | 1 | 1/0 | Penumbra R1CS is a Rust cryptography library; there is no deployed contract address for the audited code. |
| 791 | Picasso Network | 1 | 1/0 | Picasso is a Cosmos SDK chain (Composable's Centauri); the finding concerns a CosmWasm contract's Initialize instruction. No contract address (bech32 or code id) is published in the audit entry or reachable docs, so noth |
| 792 | Plume Smart Wallets | 1 | 1/0 | OtterSec review of Plume smart wallets. Chain identified (Plume mainnet) but the audited wallet implementation address is not published. |
| 793 | Polars July7 | 1 | 1/0 | Likely a 2021 BSC-era farm; identity could not be confirmed. |
| 794 | Poly-notes | 1 | 1/0 | Searches returned only Polymarket, an unrelated project. |
| 795 | Poop | 1 | 1/0 | PeckShield POOP v1.0 review is a meme-token contract review with no deployment address. The token is not listed with an address on DefiLlama and no verified contract name match was found. |
| 796 | Possum Labs | 1 | 1/0 | Possum Labs (Portal fixed-rate-yield protocol) appears defunct; no docs, GitHub or address book reachable. Hacken audit page confirms audit identity only. |
| 797 | Prime DAO by Team Omega | 1 | 1/0 | Team Omega 2021 review of 'Prime DAO' (token buy function with overwritable locks). Ethereum has a separate PrimeDAO project (token 0xE59064a8..., PrimeDAO 0x30C5d40d...) but nothing ties it to this 2021 token-sale code, |
| 798 | Proof Circuit | 1 | 1/0 | Zellic review of a zero-knowledge proof circuit. Circuits are compiled into verifier artifacts, not deployed contracts, so no address applies. |
| 799 | Public - 200Lab NFT and Marketplace | 1 | 1/0 | 200Lab NFT and Marketplace is a training/example audit target; no production deployment address exists in public sources. |
| 800 | Public - Camly Smartcontracts | 1 | 1/0 | Verichains 2023 Camly Smartcontracts review; no address or chain in the report and no verified contract match found. Camly is a consumer-app token project and the audited marketplace/order contract is not identifiable fr |
| 801 | Public - DarkLand Smartcontracts | 1 | 1/0 | No live deployment surfaced within the timebox; report covers Pools.sol staking logic only. |
| 802 | Public - DefiHorse Staking | 1 | 1/0 | Verichains 2022 audit; deployment not published. |
| 803 | Public - EscrowDapp Smartcontracts | 1 | 1/0 | Verichains review of a reference Escrow.sol (buyer/seller/arbiter) for 'EscrowDapp'. It is a public smart-contract sample; no production deployment is identified in the report or on the explorers checked. |
| 804 | Public - Microphone NFT Smartcontracts | 1 | 1/0 | SingSing team BSC NFT game; Verichains reviewed Breeding.sol and LootBox.sol. No verified contract or published address was located. |
| 805 | Public - Mirakle Smartcontracts | 1 | 1/0 | No identity or deployment surfaced in budget. |
| 806 | Public - NF3X Smartcontracts | 1 | 1/0 | No chain or address surfaced; NF3X appears dormant. |
| 807 | Public - NextVisionCapital Smartcontracts | 1 | 1/0 | report_addresses lead rejected: not a contract on Ethereum and no other chain evidence. |
| 808 | Public - PandExchange Smartcontracts | 1 | 1/0 | Verichains audit v1.1 of PandExchange smart contracts. Report is only in the Verichains public-audit-reports repo; no project site, docs or deployment address surfaced. |
| 809 | Public - PolyFlip Smartcontracts | 1 | 1/0 | Chain inferred from public description of PolyFlip as a Polygon casino; no contract address confirmed. |
| 810 | Public - SingSing Backend API | 1 | 1/0 | Off-chain API audit; NOT_FOUND is inherent, not a search failure. |
| 811 | Pyth Express Relay | 1 | 1/0 | Pyth Express Relay (MEV/order-flow auction). Address not resolved. |
| 812 | Qiibee Token | 1 | 1/0 | Token migration contract address not published; historical token address no longer holds code. |
| 813 | Quadrat Booster | 1 | 1/0 | Booster deployment not located. |
| 814 | Quantus Network's Dilithium and HDWallet | 1 | 1/0 | Non-EVM cryptography audit; no deployment address. |
| 815 | Ragnarok's Ronin Zero NFT smart contract | 1 | 1/0 | Audited NFT contract has no published address; the only Ronin hit belongs to a different, later product. |
| 816 | Rari Bridged Token | 1 | 1/0 | Pessimistic 2024 review of the RARI bridged token and its registerTokenOnL2 path on Rari Chain (an Arbitrum Orbit L2). No L1 token, L2 bridged-token or gateway address is published in the report, and the old Ethereum RAR |
| 817 | ReWind | 1 | 1/0 | Pessimistic 2023 report for 'ReWind'. No repo, docs or deployment address surfaced; the report names no contract address. Nothing recorded. |
| 818 | Resonate | 1 | 1/0 | The Resonate repo found is a security-review/Immunefi prep workspace (nexus.scope.md, poc.md) with no deployments. DefiLlama lists Resonate Finance across Optimism/Arbitrum/Ethereum/Polygon but with a null address; no Re |
| 819 | ReyaLabs ReyaNetworkPartI v 1 0 | 1 | 1/0 | Reya Network is a perp DEX L2 (chain id 1729). The public deployments repo is Cannon tooling only (packages/tomls, packages/tests) and contains no literal mainnet addresses; no address surfaced from docs or DefiLlama. |
| 820 | Ripple | 1 | 1/0 | Halborn 2025 audit covers Ripple's lending protocol built on XRPL native transactions (LoanSet/Batch amendments), not EVM contracts. XRPL addresses are r-addresses and the report publishes none. |
| 821 | RiscZero The Signal: Ethereum | 1 | 1/0 | Sigma Prime 2025 assessment of RiscZero 'The Signal: Ethereum'. The report publishes no deployed address and no verified contract named Signal/Attestation could be tied to RISC Zero. |
| 822 | Riskiit | 1 | 1/0 | Cantina NFT/game review; no chain or deployment address stated in the available text. |
| 823 | RociFi SMA public | 1 | 1/0 | Hexens 2022 audit. Only the ROCI token (0xF51092...) is confirmable on Ethereum and was rejected as non-core. |
| 824 | Rolling Dutch Auction Security | 1 | 1/0 | No identity beyond the contract name; nothing to trace. |
| 825 | SDAO | 1 | 1/0 | No report URL or body for this unit; "SDAO" cannot be tied to a specific deployment. |
| 826 | SDAO | 1 | 1/0 | Hacken review of SDAO (Aug 2022). No chain or address in the report extract; not guessed. |
| 827 | SFT (pashov-team-2024-06-23) | 1 | 1/0 | ERC-404-style standard review; no deployed address tied to the audited contracts. |
| 828 | SFT418 | 1 | 1/0 | Pashov Audit Group review of SFT418 (SFT418Core/_claim). The report and the CypherLabz/cyphermate_2024 repo contain only source and PoC addresses (0xABCD, 0x666 etc.), no deployment address and no chain statement. Nothin |
| 829 | Saffron | 1 | 1/0 | Prior batches reached the same conclusion: Saffron publishes no vault deployment address. |
| 830 | Seascape Lighthouse | 1 | 1/0 | Halborn review of the Lighthouse claim contract; no chain or address confirmed for this deployment. |
| 831 | Serious | 1 | 1/0 | Pashov review of serious-core (bonding-curve ERC20 market with Uniswap integration); repo is no longer public and no deployment address was found. |
| 832 | Shayan Eskandari | 1 | 1/0 | Project identity resolved to DeFi Saver, but the audited executor contract address is not published. |
| 833 | Shido May28th | 1 | 1/0 | Chain identified from the project name and the report, but no address evidence. |
| 834 | Shift USDT0 Bridge & Strategies | 1 | 1/0 | MixBytes audit (2026) of Shift's LayerZero USDT0 adapter. No published deployment address found within budget; recorded NOT_FOUND rather than guessing. |
| 835 | Silicon-2 | 1 | 1/0 | Macro audit 'Silicon A-2' (0xmacro.com/library/audits/silicon-2) covers berkeleycompute/pooling src/SiliconEpochPool.sol. The repository tree/README expose no deployment or broadcast manifest and the audit page publishes |
| 836 | Slock.it Incubed3 | 1 | 1/0 | ConsenSys Diligence review of Slock.it Incubed3 (2019). No on-chain deployment attributable to BlockProof. |
| 837 | Soroban Governor | 1 | 1/0 | Soroban (Stellar) smart-contract library audited by OtterSec; deployment is per-consumer, so there is no single protocol address. |
| 838 | Spectral SpecialStaking v 2 0 | 1 | 1/0 | SpecialStaking v2.0 (ABDK 2025) not located. Blockscout name search returns no SpecialStaking contract, and 'Spectra' hits are a different protocol (Spectra Finance). |
| 839 | Stake DAO | 1 | 1/0 | The Stake DAO address book lists hundreds of per-protocol locker/gauge/accumulator contracts; the report names no contract and the finding (missing extra-reward-per-token update on deposit) does not identify which locker |
| 840 | StakeKit | 1 | 1/0 | Three verified AllocatorVaultV1 contracts exist on Ethereum (0xC65151B1..., 0x93421f6F..., 0x8C0f3Af0...) but none could be attributed to StakeKit, so no address is asserted. |
| 841 | Stargaze Infinity Pool | 1 | 1/0 | CosmWasm infinity-swap contract sourced from contracts/infinity-swap. Stargaze pools are per-pool wasm instances and no instance address is published in the report or docs. |
| 842 | Steadefi May15 | 1 | 1/0 | Steadefi is listed by DefiLlama with no protocol address. |
| 843 | Stride | 1 | 1/0 | Cosmos SDK chain module. DefiLlama's Stride entry is an IBC denom on Osmosis, not a contract of the protocol, so it was rejected. |
| 844 | Stride StakeIBC and ICACallbacks Modules | 1 | 1/0 | Stride is a Cosmos SDK chain; StakeIBC and ICACallbacks are Go modules, not deployable contracts. Stride has no EVM deployment, so no contract address exists. |
| 845 | Substance Exchange Exchange V4 Smart Contract Security | 1 | 1/0 | Substance Exchange V4; deployment addresses are not published in docs or report. |
| 846 | Sui Sentinel | 1 | 1/0 | OtterSec 2026 review of Sui Move code; no package id or docs/deployments page surfaced in the two allowed lookups. |
| 847 | Swing Aggregator | 1 | 1/0 | No deployment address found for the audited SwapRouter. |
| 848 | Synonym | 1 | 1/0 | OtterSec review (OS-SNM-ADV-00) of a 'Hub' contract with userActions and per-user vaults. The release names no chain, repo or program id, and synonym.finance/docs.synonym.finance did not resolve. |
| 849 | Tensor tlock | 1 | 1/0 | Tensor NFT lending/lock program; no program ID for tlock published in the Ottersec report or docs. |
| 850 | Terra Liquidity Bootstrapping | 1 | 1/0 | Terra LBP was a Terra (CosmWasm) pool product, not an EVM contract; no canonical pool address is published and the pools were per-launch instances. |
| 851 | Tezos Kernel Scope 1, 2 and 3 | 1 | 1/0 | Spearbit review of the Tezos/Etherlink kernel. The reported defect is in rollup kernel code that runs inside the sequencer, so there is no contract deployment to point at. |
| 852 | The Vault | 1 | 1/0 | Report spans EVM/Solana/Starknet; the finding is a Solana instruction. No program id found. |
| 853 | TrueFi - August 10, 2022 | 1 | 1/0 | TrueFi's live deployments are the legacy loan pools; the audited Helium portfolio appears to be a pre-deployment artifact. |
| 854 | Trufin June7 | 1 | 1/0 | Zokyo audit dated 2023-06-07 of TruFin's Staker.sol ERC4626 vault; truyields.com hosts the audit PDFs (TruMATIC, Trufin 20230309). No deployment address is published on the site or in the PDFs' public pages, and DefiLlam |
| 855 | Trugly contracts v1 | 1 | 1/0 | No mainnet deployment published for the audited MEME404/Trugly contracts. |
| 856 | Turgay Arda Usman | 1 | 1/0 | No project identity beyond the auditor/developer name; nothing to trace. |
| 857 | Typhoon Mixer | 1 | 1/0 | Mixer deployment not officially published; candidate rejected due to conflicting on-chain name. |
| 858 | UFarm | 1 | 1/0 | UFarm.Digital V2 runs on Arbitrum but publishes no deployment table; no verified contract matching the strategy/strategy-manager scope (totalCost) surfaced. |
| 859 | Unchained | 1 | 1/0 | Three Sigma 2026 audit of a gaming protocol; only SessionManager is named and no chain, repo or deployment reference is given. |
| 860 | Unitrade on October 6, 2020 | 1 | 1/0 | Solidified 2020 review of UniTradeOrderBook.sol (finding marked FIXED in the report). The 2020 order-book deployment is not published; only the UniTrade TRADE token 0x6F87D756DAf0503d08Eb8993686c7Fc01Dc44fB1 remains labe |
| 861 | Unlimited Leverage | 1 | 1/0 | Generic product name; no identifiable protocol, chain or deployment could be established from the batch metadata or a search. |
| 862 | UnoRe | 1 | 1/0 | UnoRe (reinsurance DeFi). No verified UnoRe staking contract surfaced; blockscout name search returns unrelated tokens and a BarnBridge staking proxy (SingleAssetStaking), which is a different protocol. |
| 863 | Utility Libraries | 1 | 1/0 | Least Authority 2020 review of client-side utility libraries (JS key generation). No on-chain deployment. |
| 864 | Vetenet | 1 | 1/0 | veTENET-style gauge system (GaugeFactory.createSubGauge). The name suggests Tenet, but neither the report nor a lookup confirmed the chain or a deployment address, so no chain is asserted. |
| 865 | WIZCoin Token Contract | 1 | 1/0 | 2017 ABDK review of a token contract; no deployment or chain evidence. |
| 866 | WOW Max | 1 | 1/0 | Hacken Aug-2023 audit of the WoW Max DEX; the corpus entry has no report URL or body, and no router/factory address is published on the site. |
| 867 | WishWish | 1 | 1/0 | No confirmed chain or deployment. |
| 868 | XION and Burnt Contracts | 1 | 1/0 | CosmWasm contracts on XION; no contract address found. |
| 869 | XPress Protocol | 1 | 1/0 | XPress is an on-chain order-book DEX on Sonic. Its docs list an audit and a contract API but no address table, and DefiLlama records the protocol with a null address. |
| 870 | YA, zokyo | 1 | 1/0 | Zokyo Feb-2023 review filed under project 'YA, zokyo'; the source PDF is the Magic Yearn report (MyStaking._stake reward accrual). No chain or address confirmed. |
| 871 | Yieldmos Outposts Osmosis | 1 | 1/0 | Yieldmos outposts are CosmWasm contracts; no code id or contract address published in docs. |
| 872 | ZAP auditreport April11th | 1 | 1/0 | Zokyo Apr-2024 audit of TokenSaleUSDB.sol / TokenSaleETH.sol; the corpus entry has no report URL or body, and the contract names (USDB/ETH) do not resolve to a published deployment. |
| 873 | ZIGChain Reward Contract | 1 | 1/0 | Oak Security 2025 review of ZIGChain's reward/claim CosmWasm contract. docs.zigchain.com documents the CosmWasm module and whitelisting but publishes no address for the audited zig-claim contract; no zig1... contract add |
| 874 | ZeroPool | 1 | 1/0 | Site and repo describe the protocol but publish no mainnet contract address; no explorer hit for the audited pool. |
| 875 | Zeta Markets | 1 | 1/0 | Solana program; program id not published in the report. |
| 876 | another external | 1 | 1/0 | ConsenSys Diligence 2023-05 review of 'Tidal' (addTidal/withdrawTidal accounting); no deployment address located. |
| 877 | catalyst-generalised-incentives | 1 | 1/0 | GeneralisedIncentives is deployed per-chain via a CREATE2 deployer; no mainnet address is published in the repo within the timebox. |
| 878 | codefunded | 1 | 1/0 | Composable Security Nov-2023 report (2023_11_Codefunded.pdf). No repo, docs or deployment address for Codefunded surfaced; the report section read does not name one. |
| 879 | dForce Lending V2 | 1 | 1/0 | MixBytes 2024 review of dForce Lending V2 (iToken). The audit PDF was downloaded and text-extracted: it contains no 0x address at all. DefiLlama's dForce Lending address 0x431ad2ff...7dbe0 is the DF governance token, and |
| 880 | eGMX | 1 | 1/0 | Guardian Audits 2025 report on eGMX ExitVaultEntryPoint. Two searches plus a GitHub repo search surfaced no eGMX protocol site, docs, repo or deployment; the only 'egmx' GitHub hits are unrelated. No chain or address cou |
| 881 | ether.fi - Prelude V3 | 1 | 1/0 | Prelude V3 is a newer ether.fi component; no live address could be confirmed. |
| 882 | filsnap | 1 | 1/0 | Off-chain wallet snap; NOT_FOUND is inherent, not a search failure. |
| 883 | for MoonBound | 1 | 1/0 | Hexens report describes a MoonBound bonding-curve launch contract but gives no address; no verified MoonBound deployment surfaced on the chains checked. |
| 884 | geodefi | 1 | 1/0 | No Oracle deployment found; the only documented portal address has no bytecode on Ethereum and no other chain could be confirmed. |
| 885 | glif- -july | 1 | 1/0 | GLIF docs return 500 and no LiquidityMineSP address is published; the llama candidate 0xAeD7C2eD… is a Base ICNT vault, unrelated to the Filecoin pool. |
| 886 | liquality | 1 | 1/0 | Cross-chain atomic swap tooling; no on-chain deployment address in the audit. |
| 887 | magic yearn | 1 | 1/0 | Same Zokyo Magic Yearn report as the ya-zokyo unit; staking reward accounting bug, no deployed address found. |
| 888 | neon-spl-governance | 1 | 1/0 | Source repo identified but no program id for the audited addin is published. |
| 889 | octonline | 1 | 1/0 | SCA engagement 'octonline marketplace' (Jan 2023). Batch entry has no report URL or body, and no public repo, docs or deployment address for this marketplace was found. |
| 890 | pashov-solo-2023-12-06-nftcapsule-security-review | 1 | 1/0 | Pashov solo review, 2023-12-06. Neither the pashov/audits repo nor a web search surfaced an 'NFT Capsule' project repo, docs or deployment address. No on-chain identity could be established. |
| 891 | pashov-team-2024-04-19-catalyst-security-review-april | 1 | 1/0 | Pashov review of Catalyst (bridge category, Apr 2024). Report and batch give no deployment reference; catalyst.exchange is a live product but no contracts/addresses page surfaced within the search budget. |
| 892 | pashov-team-2024-05-22-curio-security-review | 1 | 1/0 | No deployment information. |
| 893 | pashov-team-2024-08-03-moarcandy-security-review | 1 | 1/0 | Pashov review of MoarCandy bonding-token factory. No verified factory deployment found. |
| 894 | pashov-team-2024-10-03-apdao | 1 | 1/0 | Pashov Audit Group engagement 2024-10-03 for 'apdao' (NFT auction). Two searches returned only Pashov's general site/repo listing; no APDAO product site, docs, repo or deployment surfaced, so neither chain nor address co |
| 895 | pashov-team-2024-11-29-nexus-security-review | 1 | 1/0 | Pashov report identifies Nexus NativeYield (DepositETH/DepositUSD, BERA gas token on Berachain). The GitHub repo is now 404/private and the report lists only pre-existing token addresses, not a Nexus deployment, so no ad |
| 896 | pashov-team-2024-12-11-ulti-security-review-novemb | 1 | 1/0 | Pashov review of ulti-org/ulti-protocol-contract (ULTI token launch: native-currency deposits, Uniswap pool, referral rewards). The repo is no longer publicly readable (GitHub 404 on the org repo) and no deployment addre |
| 897 | pashov-team-2025-05-10-ripit-security-review | 1 | 1/0 | No project identity resolved beyond the audit title. |
| 898 | pashov-team-2025-06-28-gatekeeper-security-review | 1 | 1/0 | Solana program id not published; no deployment traceable. |
| 899 | pashov-team-2025-10-25-enclave-security-review | 1 | 1/0 | Finding is Solana instruction-introspection logic; no program address recoverable from the batch text. |
| 900 | riskiit protocol security assessment | 1 | 1/0 | Pashov 'Riskiit Protocol' assessment dated 2025-02-15. GitHub has no riskiit protocol repository (only an unrelated user), and no site, docs or explorer match surfaced. Chain and address unresolved. |
| 901 | sigmaprime bullet | 1 | 1/0 | No on-chain program or contract address exists for the audited code; it is an L2 runtime crate. Verified via the Sigma Prime scope section. |
| 902 | sigmaprime-omni-network-sigma-prime-omni-network-omni-portal-security- | 1 | 1/0 | Omni rebranded to Nomina and docs.omni.network no longer resolves. Blockscout name search on Ethereum returns two verified contracts named OmniPortal (0x709e7db90d1960F3B000FEAC67F397a329327E8a with 0 txs, 0xa3324d514708 |
| 903 | skies verse | 1 | 1/0 | Identity confirmed only at the website level. The audited ERC20 staking contract has no published deployment. |
| 904 | sp1 helios audit | 1 | 1/0 | OpenZeppelin SP1 Helios review (2025-05-12) covers the SP1Helios light-client template, including Across Protocol's storage-proof fork. book/deployment.md instructs each operator to deploy SP1Helios on the destination ch |
| 905 | synthetix-bfp-market-carina | 1 | 1/0 | iosiro/Carina 2024 audit of markets/bfp-market in synthetix-v3. The market is deployed through Cannon (cannonfile.toml), not a checked-in address book, and no BFP PerpAccountModule address is published in the repo or doc |
| 906 | team 2024 03 06 tapiocadao | 1 | 1/0 | Tapioca DAO is a multichain deployment (Ethereum, Arbitrum, Optimism); the audited option-broker contract could not be matched to a live address. No address inferred from unrelated Tapioca/OFT tokens. |
| 907 | team 2024 03 06 tapiocadao security review february | 1 | 1/0 | Project rebranded to Alto Money. No public source found that lists the audited GlpStrategy deployment (GLP strategy on Arbitrum); core YieldBox address not independently verifiable. |
| 908 | team 2024 10 11 stationx | 1 | 1/0 | Live product site found, but no verifiable Factory deployment address. |
| 909 | unknown (hf: 2021-07-fei-tribechief) | 1 | 1/0 | Hardhat-fork style entry for Fei Protocol's TribalChief (2021-07). TribalChief is an Ethereum mainnet staking contract, but two searches surfaced only the FEI (0x956f...) and TRIBE (0xc728...) tokens; Blockscout name sea |
| 910 | unknown (hf: 2023-10-30-evm-contracts) | 1 | 1/0 | Unit comes from a Cantina Nov-2023 DFlow report (cdn.cantina.xyz/reports/cantina_dflow_nov2023.pdf) whose corpus metadata records chain 'unknown'. DFlow is primarily a Solana venue and no EVM deployment of DFlowSwap is p |
| 911 | unknown (hf: 2024-04-29-sigmaprime-bls-wallet-review) | 1 | 1/0 | Sigma Prime review of the BLS Wallet (web3well/bls-wallet) contracts. The repo's contracts/deployments path is not present on the default branch and no mainnet bundle-verifier address is published. |
| 912 | unknown (hf: opal-protocol-competition) | 1 | 1/0 | Unknown project identity; nothing verifiable within budget. |
| 913 | unknown (hf: pashov-solo-2023-11-17-bearcave-security-review) | 1 | 1/0 | Project identity resolved to HoneyJar/Bearcave on Berachain; no contract address confirmed. |
| 914 | unknown (hf: pashov-team-2024-05-22-curio-security-review) | 1 | 1/0 | Curio game deployment not located; the name collides with unrelated tokens and no audited contract address surfaced. |
| 915 | unknown (hf: pashov-team-2024-07-15-lucidly-security-review) | 1 | 1/0 | Lucidly Finance (Pashov, Jul 2024), Base yield aggregator. Identity confirmed but deployments not published. |
| 916 | unknown (hf: pashov-team-2024-10-11-groupcoin-security-review) | 1 | 1/0 | No chain, repo or address found; project label is unresolved in the corpus. |
| 917 | unknown (hf: pashov-team-2025-01-25-omo-security-review) | 1 | 1/0 | Pashov Omo review targets OmoVault/DynamicAccount on Hyperliquid EVM (the report references ENTRYPOINT_ADDRESS on 'hyper EVM'). No OmoVault deployment address is published in the review or found on Ethereum. |
| 918 | unknown (hf: pashov-team-2025-03-30-hyperhyper-security-review) | 1 | 1/0 | HyperHyper (Pashov, Mar 2025) on HyperEVM. No address surfaced; not guessed. |
| 919 | veTenet | 1 | 1/0 | veTenet on Tenet chain. Tenet explorer (tenetscan) did not respond during this run; no gauge/clone address confirmed. |
| 920 | wow max DEX (Aug 2023) | 1 | 1/0 | WOWMAX aggregator (Ethereum/Base/BNB per its docs). Docs and site publish no contract addresses; no GitHub deployment book found. |
| 921 | x / 4 | 1 | 1/0 | Unit label 'x' comes from the report filename; the audit PDF is Felix2.pdf. Identity traced to Felix (usefelix.xyz). |
| 922 | xycLoans | 1 | 1/0 | Stellar Soroban deployment; contract ID not published. |
| 923 | zk-token-sdk | 1 | 1/0 | OtterSec 2023 audit of an off-chain Rust SDK; no contract deployment to trace. |
| 924 | zkCross - Partisia Contracts | 1 | 1/0 | Halborn audit of zkCross contracts on Partisia Blockchain (PBC). Partisia contracts use 21-byte addresses and are not published in the report or on an explorer reachable here; zkCross docs do not publish a Partisia deplo |
| 925 | 00bleck | 1 | 0/1 | No '00bleck' or ClaimOperator deployment is attributable on Ethereum; the review appears to cover a project not yet deployed or deployed on another chain. |
| 926 | 04 10 Texture2.0-MR-FV | 1 | 0/1 | Identity unresolved: the Certora review covers a guardian-based price feed called Texture 2.0, but no site, repo or deployment could be attributed; Ethereum 'Texture' hits are unrelated NFT/token projects. |
| 927 | 06--Yearn-BalancerLPFactory | 1 | 0/1 | Yearn is Ethereum-first but the specific BalancerLPFactory deployment address was not published. |
| 928 | 10--DopexV2-CLAMM | 1 | 0/1 | Only the DPX governance token is publicly identifiable; the audited CLAMM was not deployed at review time. |
| 929 | 100x Audit Report | 1 | 0/1 | OrderDispatch is not verified under that name on Ethereum or Optimism. Ethereum 'OrderGateway' contracts (0xabD785dB..., 0x20149E66...) are Solidity 0.5.1 and predate the Feb-2024 audit; the 0.8.30 OrderGateway on Optimi |
| 930 | 12 02 dcSpark Sidechain Bridge-FV | 1 | 0/1 | The reviewed bridge is dcSpark's Milkomeda sidechain component. No address is published and Milkomeda's explorer was not reachable; there is no EVM deployment of this bridge on Ethereum. |
| 931 | 12 11 Glow LRT-MR | 1 | 0/1 | Certora Dec-2024 review of Glow's LRT programs on Solana. Audited Solana program ids are not published in the report extract and no program id could be attributed, so nothing is recorded. |
| 932 | 1Inch Farming | 1 | 0/1 | MixBytes 2022 1inch Farming. 1inch liquidity-mining programme is retired; no address in the record. |
| 933 | 2021-04-24-mogul-sca-mogul-marketplace-nft-apr2021-sca-mogul-marketpla | 1 | 0/1 | No identity or deployment data available in the corpus record. |
| 934 | 2021-06-08-ichi-ichi | 1 | 0/1 | Report body is absent; only the title and exploit path exist. ICHI docs list the ICHI token (0x1111...4d6) and oneToken/AMM factory addresses, but no composite-oracle address. Composite oracles are deployed inside each o |
| 935 | 2022-04-06-pera-finance-sca-pera-finance-erc20-staking-farming-apr2022 | 1 | 0/1 | Pera Finance staking/farming audit (2022-04) with no addresses in the report; no deployment could be confirmed this pass, so no chain is asserted. |
| 936 | 2022-04-14-minterest-sca-minterest-lending-apr2022-sca-minterest-lendi | 1 | 0/1 | SCA Apr-2022 review of Minterest's lending markets (updateBorrowIndexesHistory). Minterest later ran on Mantle and has sunset; the audited Comptroller/MToken addresses are not published, and the only verified Minterest c |
| 937 | 2022-05-01-acta-finance-sca-acta-finance-nft-apr2022-sca-acta-finance- | 1 | 0/1 | SCA Apr-2022 review of Acta Finance's NFT (Collection.sol) on Avalanche. The batch carries no report URL or body, and no docs/deployments page exposed the collection address; only the ACTA token appears on listings, whic |
| 938 | 2022-05-04-ground-zero-sca-ground-zero-ido-contract-may2022-sca-ground | 1 | 0/1 | Ground Zero is an IDO launchpad (it hosted the Dexsport IDO); the Ethereum 'GroundZERO' token 0x33613D7264e183579D3BEa0cE29432C75990d80d surfaced in search is a token, not the audited IDO contract, so it was not recorded |
| 939 | 2022-05-ethereum-evm-anteprotocol | 1 | 0/1 | Ante protocol pools appear dormant/not indexed under the contract name; no docs deployment table was reachable in the timebox. |
| 940 | 2022-06-19-alt-sca-alt-platform-erc1155-jun2022-sca-alt-platform-erc11 | 1 | 0/1 | Insufficient identity to trace; recorded NOT_FOUND rather than guessing an address. |
| 941 | 2022-07-28-web3-bazaar-sca-web3-bazaar-escrow-jul2022-sca-web3-bazaar- | 1 | 0/1 | Web3 Bazaar escrow audit (2022-07); the report lists no deployment addresses and the project has no reachable deployments page, so nothing could be attributed. |
| 942 | 2022-07-30-clabs-sca-clabs-erc20-jul2022-sca-clabs-erc20-jul2022 | 1 | 0/1 | SCA engagement (Jul 2022) with no report URL, body or address. cLabs is Celo's developer but no specific ERC20 deployment is named, so no chain/address is asserted. Nothing recorded. |
| 943 | 2022-08-02-irocket-sca-irocket-erc721-aug2022-sca-irocket-erc721-aug20 | 1 | 0/1 | Metadata-only record (SC Audits, iRocket ERC721, Aug 2022) with no body or URL; no deployment found. |
| 944 | 2022-09-23-nft-market-presethtc-auction-store-nft | 1 | 0/1 | No deployment address is published in the report and the product could not be identified as a live deployment within budget. |
| 945 | 2022-11-09-final-fiat-i-audit-report | 1 | 0/1 | Only the FIAT DAO governance token surfaced; the audited OptimisticOracle deployment was not located. |
| 946 | 2022-11-17-stablezone-sca-wt-worldwide-tech-erc20-vesting-staking-nov2 | 1 | 0/1 | StableZone Nov-2022 review of WT Worldwide Tech's ERC20 vesting/staking contracts. No chain or deployment could be identified from the review metadata or public sources, so nothing is recorded. |
| 947 | 2022-11-debtdao | 1 | 0/1 | LineOfCredit contract not found on Ethereum Blockscout; DebtDAO appears not to have a live deployment. |
| 948 | 2023-01-11-zkmakers-sca-zkmakers-erc20-staking-jan2023-sca-zkmakers-er | 1 | 0/1 | zkSync Era deployment could not be confirmed within budget. |
| 949 | 2023-01-31-presend-sca-presend-affiliate-program-jan2023-sca-presend-a | 1 | 0/1 | SCA engagement name with no report URL, body or address; 'Presend' matches no DefiLlama protocol and no public deployment surfaced. Nothing recorded. |
| 950 | 2023-01-canto-identity | 1 | 0/1 | CidNFT is deployed on Canto (chain id 7700). Canto's explorer (evm.explorer.canto.io) returned 403/Cloudflare and no Blockscout/Routescan instance responded, so the deployment address could not be retrieved. |
| 951 | 2023-03-17-final-uxd-audit-report | 1 | 0/1 | UXD docs contain no deployment addresses; PerpDepository was an Arbitrum-era component and no address is published. Current UXD docs describe only a Solana deployment. |
| 952 | 2023-03-21-quadrata-lending-a3d2d9c8 | 1 | 0/1 | Quadrata is primarily an identity/passport protocol; the audited 'Quadrata Lending' Compound fork has no public deployment address in the report. |
| 953 | 2023-03-22-rumi-finance-sca-quantum-dao-blue-pte-erc20-yield-farming-m | 1 | 0/1 | SCA / Quantum DAO Mar-2023 review of a Rumi ERC-20 yield-farming vault. DefiLlama places Rumi Finance on Arbitrum but lists no address, and Rumi's docs carry no deployments page, so no address is recorded. |
| 954 | 2023-04-02-algoblocks-sca-algoblocks-dex-mar2023-sca-algoblocks-dex-ma | 1 | 0/1 | SCA engagement (Mar 2023) with no report URL/body/address. The DefiLlama 'AlgoBlocks' entry is a BSC protocol and cannot be tied to this engagement; no verified deployment surfaced. Nothing recorded. |
| 955 | 2023-04-04-level-finance-929d1708 | 1 | 0/1 | Project identity confirmed (level.finance, level-fi org); deployment address not resolvable with the permitted lookups. |
| 956 | 2023-04-29-dinowars-sca-dinowars-erc20-vesting-apr | 1 | 0/1 | No identifiable deployment; NOT_FOUND. |
| 957 | 2023-05-24-petaverse-194b7ad8 | 1 | 0/1 | SCA May-2023 review of Petaverse's omnichain NFT (approvals/transfers/burns on non-origin chains). The batch record has no report URL or address; the Ethereum 'Petaverse' (PPT) contract found by name is an ERC-20 unrelat |
| 958 | 2023-05-26-skies-verse-sca-skies-verse-staking-erc | 1 | 0/1 | 2023 SCA review of Skies Verse staking ERC20. |
| 959 | 2023-05-ethereum-evm-franklintempleton-moneymarket-securityreview | 1 | 0/1 | Permissioned Franklin Templeton money-market stack; no public deployment located. |
| 960 | 2023-06-06-diverse-solutions-sca-diverse-solutions-staking-apr2023-sca | 1 | 0/1 | SCA engagement (Apr 2023) with no report URL, body or address and no public deployment tied to 'Diverse Solutions'. Nothing recorded. |
| 961 | 2023-06-llama | 1 | 0/1 | Code4rena Jun-2023 contest on the Llama governance framework (LlamaRelativeQuorum strategy). LlamaCore is deployed per organisation, so the framework has no single canonical deployment and the report names no instance; N |
| 962 | 2023-07-06-bit5-sca-bit5-lending-platform-marketplace-may2023-sca-bit5 | 1 | 0/1 | SC Audits (SCA) review, 2023-07-06. No address in the report text and no public deployment surfaced. |
| 963 | 2023-07-22-govworld-sca-govworld-lending-platform-jul2023-sca-govworld | 1 | 0/1 | BSC lending platform; audit report carries no deployment table. |
| 964 | 2023-08-05-foundry-defi-stablecoin-codehawks-audit-contest | 1 | 0/1 | CodeHawks audit contest of the Cyfrin 'Foundry DeFi Stablecoin' course repository (DSCEngine/DSC). This is teaching code with no production deployment, so NOT_FOUND is structural rather than a search gap. |
| 965 | 2023-08-29-sparkn | 1 | 0/1 | No 'Sparkn' distribution contract found on Ethereum, Optimism, Unichain or Scroll; the SparkNetwork/SparkNFTGateHook hits are unrelated. |
| 966 | 2023-08-goodentry | 1 | 0/1 | Code4rena Aug-2023 contest on GoodEntry's TokenisableRange. GoodEntry's Arbitrum deployment addresses (Geyser, range registry) are not published in docs and could not be attributed through a reachable explorer; the only  |
| 967 | 2023-08-shell | 1 | 0/1 | llama_candidates address 0xe47ba52f326806559c1deC7ddd997F6957d0317D was rejected: its implementation is StandardArbERC20, i.e. the bridged SHELL token, not the Ocean/Cove contract. No Ocean/Cove address could be confirme |
| 968 | 2023-09-ethereum-evm-elixir-securityreview | 1 | 0/1 | 2023 review of an 'Elixir' EVM contract set exposing getVertexBalance (Vertex integration). The batch entry has no report URL and no Elixir deployment could be identified; NOT_FOUND. |
| 969 | 2023-10-04-final-syndr-audit-report | 1 | 0/1 | Previously traced in ST2-079: Syndr is an Arbitrum perp DEX with no published deployment; DefiLlama has no Syndr entry and the docs do not list addresses. |
| 970 | 2023-11-01-ethereum-reserve-dollar-erd-d2c63484 | 1 | 0/1 | No ERD deployment, docs page or GitHub attributable to the project was found; the name resolves only to unrelated tokens on Ethereum. |
| 971 | 2023-11-07-metatime-sca-metatime-layer-2-oct2023-sca-metatime-layer-2- | 1 | 0/1 | Audit of the Metatime L2 validator contract; no public deployment address. |
| 972 | 2023-11-08-blex-io-215a1fca | 1 | 0/1 | Arbitrum perp DEX; no docs/deployments page and no CoreVault address surfaced. |
| 973 | 2023-11-14-final-perennial-v2-update-1-audit-report | 1 | 0/1 | Perennial V2 update audit (2023-11-14). DefiLlama lists Perennial V2 on Arbitrum/'Perennial' but publishes no address, and the batch has no report_addresses. docs.perennial.finance did not resolve and no deployment addre |
| 974 | 2024-02-13-final-100x-audit-report | 1 | 0/1 | 100x (Ciao) perp/withdrawal review, Feb-2024. No protocol identity (site, docs, repo) or chain could be confirmed, so NOT_FOUND. |
| 975 | 2024-02-16-ithaca-finance-8cacdbf3 | 1 | 0/1 | Ithaca Finance (Quantstamp certificate 8cacdbf3). The report is a cross-chain application for ithaca-protocol/ithaca-sc, but the GitHub repo returns 404 and neither the report nor docs publish a mainnet Registry address. |
| 976 | 2024-03-18-final-perpetual-audit-report | 1 | 0/1 | Perp v3 maker contracts identified in source but no deployment address surfaced. |
| 977 | 2024-03-21-coinstir-sca-coinstir-eip712-feb2024-sca-coinstir-eip712-fe | 1 | 0/1 | No public identity, chain or deployment could be tied to this SC Audits record. |
| 978 | 2024-03-31-final-goat-trading-audit-report | 1 | 0/1 | Pashov 2024 audit of Goat Trading (GoatPair). No report URL or deployment manifest; the only Goat Trading contract found by name is the GOAT token 0x6Ae2A128cD07d672164cA9f2712Ea737d198Dd41 (a token, rejected), and no Go |
| 979 | 2024-04-10-impossible-finance-080f5654 | 1 | 0/1 | IFFixedSale giveaway contract; batch carries no report URL and no deployment reference, and no address surfaced within the search budget. |
| 980 | 2024-04-29-sigmaprime-linkpool-linkpool-2-review | 1 | 0/1 | Marked uncertain on profit because the available text describes a staker loss, not a capture. |
| 981 | 2024-05-02-final-uncuts-app-by-rekt-audit-report | 1 | 0/1 | Same codebase as the 'uncuts' unit; no deployed address located. |
| 982 | 2024-05-27-airdao-sca-airdao-bridge-apr2024-sca-airdao-bridge-apr2024 | 1 | 0/1 | Identity known (airdao.io); bridge deployment address missing. |
| 983 | 2024-06-20-subscription-token-protocol-v2-7ef99de3 | 1 | 0/1 | No project identity, website or deployment recovered for the V2 protocol. |
| 984 | 2024-06-20-zero-staking-40ffa176 | 1 | 0/1 | Contest finding '2024-06-20-zero-staking' (reentrancy through the ERC721 receiver hook). The batch has no report URL, chain or deployment; the name collides with several unrelated 'Zero' projects and no contract could be |
| 985 | 2024-06-22-final-symmio-v0-83-update-contest-audit-report | 1 | 0/1 | Multi-chain diamond; chain list from DefiLlama and docs. No core diamond address published. |
| 986 | 2024-06-27-permissionless-multisigner-paymaster | 1 | 0/1 | Audit of a paymaster component of the Permissionless (Pimlico) stack; no deployment address in the report extract. |
| 987 | 2024-07-05-fatty-sca-fatty-presale-smart-contracts-jun2024-sca-fatty-p | 1 | 0/1 | SCA engagement 2024-07-05 on Fatty presale contracts. The batch entry has no report_url, body, or source_url, so there is no contract name beyond the presale buy/cost path and no address list; no published Fatty presale  |
| 988 | 2024-07-10-base-paper-scissors-sca-base-paper-scissors-contract-and-to | 1 | 0/1 | Hacken SCA of the Base game and token, June 2024. |
| 989 | 2024-07-13-final-union-finance-update-2-audit-repo | 1 | 0/1 | Sherlock 2024-06 Union Finance update; the faucet is not part of the mainnet credit protocol. |
| 990 | 2024-07-19-final-allora-audit-report | 1 | 0/1 | Metadata-only batch entry (no report body/source URL). Cosmos appchain: no EVM deployment address exists. |
| 991 | 2024-09-16-cryptex-monorepo | 1 | 0/1 | CTX token 0x321C2fE4446C7c963dc41Dd58879AF648838f98D was rejected as a core mapping (token, not Pocket). |
| 992 | 2024-09-21-final-saffron-lido-vaults-audit-report | 1 | 0/1 | The audit targets Saffron's Lido vault implementation (sherlock-audit/2024-08-saffron-finance). No Saffron Lido vault address is published in the report or repo README, and no address was surfaced, so the finding maps to |
| 993 | 2024-09-25-final-thanos-l2-native-token-bridge-audit-report | 1 | 0/1 | Thanos is an OP Stack L2; the audited bridge is a project-specific modification of the standard bridge, whose proxy address was not resolvable within budget. |
| 994 | 2024-11-01-dria | 1 | 0/1 | Corpus record identifies only project label 'Dria' and a clone-NFT listing finding; no audited artifact or deployment could be tied to it. |
| 995 | 2024-11-15-belong-net-sca-belong-net-evm-oct2024-sca-belong-net-evm-oc | 1 | 0/1 | SCA Nov-2024 review of Belong Net EVM (payee/revenue-split implementation). Belong's documentation covers API access only and publishes no contract-address table; the audited payee implementation address was not found, s |
| 996 | 2024-11-17-final-vvv-launchpad-investments-token-d | 1 | 0/1 | The finding is in VVVVCTokenDistribution::claim. Only the VVV token (0xacfE6019Ed1A7Dc6f7B508C02d1b04ec88cC21bf, Base) is publicly identifiable; no VVVVCTokenDistribution deployment address was found, and the token is no |
| 997 | 2024-11-28-hesty-sca-hesty-hesty-contract-oct2024-sca-hesty-hesty-cont | 1 | 0/1 | Hacken report for Hesty (Base, Nov 2024) lists the contract set but publishes no addresses, and the Hacken site is Cloudflare-gated; no verified Hesty deployment surfaced. |
| 998 | 2024-12-06-prospective-world-sca-prospective-world-pros-venture-m-nft- | 1 | 0/1 | SCA engagement (Oct 2024) with no report URL, body or address. The title describes a loop/gas problem, so profit is marked uncertain rather than yes. Nothing recorded. |
| 999 | 2025-01-02-gamic-sca-gamic-gamic-airdrop-dec2024-sca-gamic-gamic-airdr | 1 | 0/1 | Gamic airdrop audit (2024-12) with no addresses and no reachable deployment page this pass; no chain or address is asserted. |
| 1000 | 2025-01-27-zkvm-security-review-openvm-competition | 1 | 0/1 | No deployment exists for a zkVM circuit; nothing to map. |
| 1001 | 2025-01-next-generation | 1 | 0/1 | No identity or deployment surfaced for this audit; address intentionally left null. |
| 1002 | 2025-02-24-uniswap-hooks-library-milestone-1-audit | 1 | 0/1 | The audited artifact is a Solidity hooks library, not a deployed protocol, so there is no single deployment address to record. |
| 1003 | 2025-02-25-liquidity-management | 1 | 0/1 | Batch item has no project identity beyond the audit slug; no chain or deployment could be established. |
| 1004 | 2025-03-03-colorpool-chromia | 1 | 0/1 | ColorPool is a Chromia dapp (DEX); Chromia contracts are identified by blockchain RID + dapp account rather than an EVM address, and the audit entry has no body or deployment data. The DefiLlama adapter only carries the  |
| 1005 | 2025-03-06-vedelegate-vet-sca-vedelegate-vet-contracts-feb2025-sca-ved | 1 | 0/1 | SCA Feb-2025 review of veDelegate (VeChain). Contracts are VeChain Thor deployments with 0x-style 20-byte addresses; the audited ERC-6551 account implementation address is not published in the report and no VeChain explo |
| 1006 | 2025-03-12-fireblocks-upgradeable-tokens-audit-erc721f | 1 | 0/1 | Nothing on-chain corresponds to this review: ERC721F is Fireblocks' token template audited as source. Ethereum 'ERC721F' hits are an unrelated test token (0xa8eb4d2E...). |
| 1007 | 2025-03-14-final-crestal-network-audit-report | 1 | 0/1 | Crestal Network omni-contracts audit; no live BlueprintV5 address located within the search budget. |
| 1008 | 2025-04-cabal-liquid-staking-token | 1 | 0/1 | Code4rena 2025-04 Cabal Liquid Staking Token audit. Initia Move modules are addressed per-chain and no deployed module address was attributable within the timebox. |
| 1009 | 2025-05-07-aquarius | 1 | 0/1 | 2025 audit of Aquarius's boost/reward-share accounting. The boost feature and DefiLlama's 'Aquarius Stellar' entry point to the Stellar Soroban AMM, but the Soroban contract ID (C...) is published neither in the extract  |
| 1010 | 2025-08-24-foresight-contracts | 1 | 0/1 | Audit filename is the only identifier; no repo, chain or deployment was attributable. |
| 1011 | 2025-08-29-somnia-sca-somnia-somnia-contracts-aug2025-sca-somnia-somni | 1 | 0/1 | Somnia L1 (EVM, chain id 5031); deployment address not published. |
| 1012 | 2025-09-18-luckify-sca-luckify-token-aug2025-sca-luckify-token-aug2025 | 1 | 0/1 | SCA Aug-2025 review of the Luckify token's randomness fulfilment. Name search on Ethereum returns only an unrelated 'Luckify Presale' token; no Luckify VRF consumer, chain or address could be confirmed. |
| 1013 | 2025-10-31-dirol-sca-dirol-dirol-agr-oct2025-sca-dirol-dirol-agr-oct20 | 1 | 0/1 | Dirol deployment not located; no docs, site or explorer contract surfaced. |
| 1014 | 2025-10-sequence | 1 | 0/1 | Smart-wallet module library; per-chain deployments exist but none is tied to the audited revision in the record. |
| 1015 | A41 - SuperNova CosmWasm Smart Contract | 1 | 0/1 | Halborn reviewed a CosmWasm contract (A41 SuperNova); the report states no chain and no contract address, and CosmWasm instances are instantiated per deployment. No address could be attributed. |
| 1016 | AAG Ventures | 1 | 0/1 | Identity limited to the audit-id prefix and the report name. No chain or address can be substantiated after the rebrand to Saakuru Labs; left NOT_FOUND rather than attaching an unverified AAG token. |
| 1017 | ACHIP & ACHAIR GUILD VENTURES PTE. LTD. | 1 | 0/1 | No address. |
| 1018 | ACO Protocol | 1 | 0/1 | EVM Solidity project (Auctus); chain and deployment address unverified. |
| 1019 | AI Arena | 1 | 0/1 | An Ethereum contract named AIArena (0xbd313400eBFf664d730852822e548ab5E09dfe59) exists but its source has no redeemMintPass/FighterFarm, so it was not recorded as the audited contract. |
| 1020 | AIRDAO | 1 | 0/1 | Only the AMB token (0xf4fB9BF10E489EA3Edb03E094939341399587b0C) surfaced; the lock/staking contract named in the finding is not published in docs or explorer search within budget. |
| 1021 | ALTR | 1 | 0/1 | No deployment or documentation surfaced; finding text unavailable. |
| 1022 | AR Data Tech Snap | 1 | 0/1 | Off-chain artifact; address tracing not applicable. |
| 1023 | AZTEC (2019 TOB audit) | 1 | 0/1 | No address attributable to the audited 2019 code; later Aztec deployments (Aztec Connect rollup, 2022) are a different codebase. |
| 1024 | Aave Aptos V3.0.2 Core | 1 | 0/1 | Non-EVM deployment (Aptos). No package address located within the time box. |
| 1025 | Aave Aptos V3.1-3.3 Core Upgrades | 1 | 0/1 | Aave V3.1-3.3 on Aptos (Move). Package address not published; Aptos addresses are 32-byte, not EVM. |
| 1026 | Aave CPM Price Provider | 1 | 0/1 | One identity search plus one repo search; no address surfaced. Not worth further time inside the batch timebox — the module was a 2020 experiment and its ABI/address is not in today's Aave documentation. |
| 1027 | Abracadabra MultiRewards | 1 | 0/1 | Guardian Audits' Feb-2024 MultiRewards review. MultiRewards is deployed per staking pool and the report names no pool; Abracadabra's docs address page did not yield a MultiRewards instance. Only the SPELL token is public |
| 1028 | Abranft | 1 | 0/1 | Bare metadata entry (uid 2022-04-abranft_H-05) with no report URL, body, website or repo. |
| 1029 | Abster Freefall | 1 | 0/1 | Project appears to be a small game; identity unresolved within the timebox. |
| 1030 | Acala | 1 | 0/1 | Incentive contract is a parachain module; no address resolvable without the specific pallet/account. |
| 1031 | AccountRecoveryModule | 1 | 0/1 | Zellic review of Biconomy's AccountRecoveryModule. Biconomy docs paths tried did not resolve and no module address is given in the report text. |
| 1032 | Aegis DFF | 1 | 0/1 | Multi-chain (EVM/Solana/Starknet) audit with no address. Not mapped to Aegis YUSD/Markets to avoid a wrong attribution. |
| 1033 | Aftermath | 1 | 0/1 | Sui Move protocol (AMM/perps). Sui packages are object ids, not EVM addresses; the docs landing page exposed no package id and the OtterSec report gives none. |
| 1034 | Aftermath Finance | 1 | 0/1 | OtterSec 2023 review of Aftermath Finance on Sui. Sui package IDs are not published in the report and there is no EVM deployment, so NOT_FOUND. |
| 1035 | Aftermath Perpetuals Oracle | 1 | 0/1 | OtterSec review of Aftermath's Sui perpetuals oracle. Sui Move packages are object-addressed and the package id is not published in the extract or site reached, so no address is recorded. |
| 1036 | Algorand Name Service | 1 | 0/1 | Non-EVM (Algorand) project; no app ID recoverable. |
| 1037 | AllScale | 1 | 0/1 | BlockSec AllScale EIP-7702 contracts review. No public deployment traceable from the audit text. |
| 1038 | Allora Network (allora) | 1 | 0/1 | Chain resolved from cosmos/chain-registry allora/chain.json (allora-mainnet-1, cosmos-sdk v0.50.11). Finding comes from the 2024-07-19 Allora audit report; there is no contract address to trace because LibP2PKey registra |
| 1039 | Alpaca Delta | 1 | 0/1 | Alpaca Finance DeltaNeutralVault (BlockSec 2022). The docs and DefiLlama adapter do not publish the vault address; only the ALPACA token/manager are listed. |
| 1040 | Alpen | 1 | 0/1 | No attributable contract address. |
| 1041 | Amphor | 1 | 0/1 | DefiLlama lists Amphor on Ethereum with a null address. docs.amphor.io did not resolve and no contract address appeared in search results. The similarly named 'Amphora'/AmphorMultiTokenMerkleClaim contracts on Ethereum b |
| 1042 | Andromeda | 1 | 0/1 | Sherlock 2024 review of Andromeda Validator Staking ADO and Vesting ADO. Deployment is CosmWasm (andromeda1.../cosmos1... addresses) and no instance address is published in the report, so no EVM-style address is recorded |
| 1043 | Andromeda (Validator Staking ADO / Vesting ADO) | 1 | 0/1 | CosmWasm deployment; no EVM address applies. Nothing recorded rather than inventing a bech32 contract address. |
| 1044 | Animoca - July 17, 2021 | 1 | 0/1 | Animoca child-token contracts; no address or confirmed chain. |
| 1045 | Animoca Core Library Extension - Oct 18, 2023 | 1 | 0/1 | The report is a library audit for Publisher NFT Season 2 contracts; no public deployment address was identified. |
| 1046 | Aperture 2 | 1 | 0/1 | The audited EthereumManager contract is not identifiable among Aperture's current deployments. |
| 1047 | Aperture Finance - September 24, 2022 | 1 | 0/1 | Aperture Finance docs list current ApertureSwap and Automan deployments (Manta Pacific/Ethereum/Arbitrum) but not the audited HomoraPDNVault; no address for the named contract. |
| 1048 | Apollo Osmosis Fixed Width | 1 | 0/1 | Osmosis CosmWasm vault; repo github.com/apollodao/apollo-vaults exists but no deployed bech32 address surfaced. |
| 1049 | Aragon Generic Money | 1 | 0/1 | Spearbit review (Nov 2025) of Aragon's new Generic Money vault contracts; no deployment address published in the report or in Aragon docs reached within the timebox. |
| 1050 | Aragon Katana | 1 | 0/1 | Chain identified as Katana from Aragon's katana-governance repo/blog; no contract address surfaced. |
| 1051 | Arcane (0x0 wallet) | 1 | 0/1 | 0x0/Arcane is a privacy wallet on 0x0 Exchange; docs.0x0.ai describes an Arcane Contract without listing addresses, and the llms.txt index carried no 0x addresses. |
| 1052 | Aria IPRWA | 1 | 0/1 | No address found for IPRWAStaking in the timebox. |
| 1053 | Arkania | 1 | 0/1 | Hacken 2022 audit of Arkania; the report names no deployment and no Arkania contract could be tied to the finding. Nothing recorded. |
| 1054 | Arken Swap | 1 | 0/1 | BlockSec 2023 Arken v1.0. Arken Finance is a BSC/multi-chain aggregator; no verified ArkenDexV4 deployment was found in the budget. |
| 1055 | Astera | 1 | 0/1 | Aave fork with minipools; chain hints Base/Linea, but no deployment address found. The llama_candidate 'Asteria Finance' on Scroll is a different project and was rejected. |
| 1056 | Astroport Core Updates | 1 | 0/1 | Per-pool wasm contract; no specific pair named in the finding. |
| 1057 | Astroport Governance Updates | 1 | 0/1 | Non-EVM; contract is a CosmWasm module. No address recorded. |
| 1058 | Atlendis Labs Loan Products | 1 | 0/1 | Trail of Bits 2023 review of Atlendis loan products. Atlendis V1/V2 ran on Polygon/Mode; per-pool addresses are not listed in DefiLlama or the docs reached. |
| 1059 | Avix Presale & Vesting | 1 | 0/1 | Solana Anchor presale; program id unresolved. |
| 1060 | Awaken Swap | 1 | 0/1 | Zellic review of Awaken Swap on aelf. aelf contracts are not 0x-addressable in the EVM sense and the audited addresses are not published in the report extract or site, so no address is recorded. |
| 1061 | BSV Blockchain TS-SDK | 1 | 0/1 | Library audit (Trail of Bits 2025); no on-chain deployment by design. |
| 1062 | BSX Exchange | 1 | 0/1 | Chain from DeFiLlama; address not found. |
| 1063 | Base Paper Scissors | 1 | 0/1 | No deployment address located for BlockPaperScissors on Base. |
| 1064 | Baseline MM Looping 2 | 1 | 0/1 | Baseline docs site is a JS app with no contracts/deployments page; no deployment address surfaced. |
| 1065 | Belong | 1 | 0/1 | No deployment found. |
| 1066 | BetX | 1 | 0/1 | Solidified review of BetX (Jan 2019). 2019-era dApp, no verifiable current deployment. |
| 1067 | Bictory Finance | 1 | 0/1 | Solana program ID not published in the audited material available here. |
| 1068 | Bigshort | 1 | 0/1 | BlockSec 'bigshort launchpad contracts' audit (2026). No chain or deployment address identified; the project does not resolve on the explorers checked. |
| 1069 | BitVault | 1 | 0/1 | No verified deployment of MultiTokenWrapper found. Ethereum search returns only unrelated 'Bitvault' ERC-20s (0x6987e983..., 0x234FF4e7...). Client told the auditor the wrapper is not in use. |
| 1070 | Bitlayer Bridge Phase 2 | 1 | 0/1 | SlowMist 2024 review of the Bitlayer Bridge (Phase 2). Report text contains no contract address and the bridge contracts were not located on a public explorer within budget. |
| 1071 | Black Tie Asset Hub (Black Tie 2025-03) | 1 | 0/1 | Identity resolved from the Hashlock audit page (hashlock.com/audits/black-tie, site link btassethub.digital) and the report PDF (hashlock.com/wp-content/uploads/2025/04/Black-Tie-Asset-Hub-Smart-Contract-Audit-Report-Fin |
| 1072 | BlockSwap | 1 | 0/1 | Halborn 2021 review of BlockSwap smart contracts. No chain, site or repository could be tied to the audited deposit/withdraw code, so NOT_FOUND. |
| 1073 | Bond Options (Teller) | 1 | 0/1 | Teller protocol Bond Options module; address unresolved rather than guessed. |
| 1074 | Bool Network | 1 | 0/1 | Bool Network's Messenger is deployed on several chains; docs are GitBook with no address registry surfaced, and the one BSC candidate found by search (0x739b...) could not be tied to Bool's Messenger. |
| 1075 | Brahma Protected MoonShots | 1 | 0/1 | Brahma docs expose no deployment table; contracts named 'Brahma' on Ethereum could not be confirmed as the Protected Moonshots Vault. |
| 1076 | Broadcaster Provers | 1 | 0/1 | Audit of ZKsync interop provers (ERC-7888). No deployment address in the report or reachable sources. |
| 1077 | BullvBear | 1 | 0/1 | BullvBear (BvbProtocol, bull/bear binary options on NFTs) was audited by Sherlock on 2022-12-12. No live deployment, website or repository surfaced; the report's addresses are test fixtures, so nothing is recorded. |
| 1078 | BullvBear | 1 | 0/1 | The only Ethereum contract matching the 'BullvBear' name is a TaxableTeamToken memecoin (0x2ABc704a...), unrelated to the protocol; no Bull/Bear options deployment is attributable. |
| 1079 | BuyBurner | 1 | 0/1 | Pashov review dated 2024-12-14. No deployment or repo surfaced in two searches; the project appears to be an unlaunched or privately deployed token. |
| 1080 | C2X | 1 | 0/1 | Oak Security's C2X review targets CosmWasm contracts (the report notes a legacy CW20 base) with no chain or address. C2X's game launcher is CosmWasm, so no EVM address applies; no instance could be attributed. |
| 1081 | CAMINO NETWORK | 1 | 0/1 | Infrastructure finding; no deployable contract address. |
| 1082 | CBI/JUKU | 1 | 0/1 | No token address found. |
| 1083 | CLABS | 1 | 0/1 | Hacken 2022 CLABS (cLabs/Celo identity escrow). No address in the record. |
| 1084 | CONSENSYS DILIGENCE | 1 | 0/1 | EternalHeroes/SkyWeaver contracts are on Polygon; Polygon explorers were not reachable from this environment and no EternalHeroesFactory appears on Ethereum or Optimism. |
| 1085 | CW20 Blocklist | 1 | 0/1 | Oak Security reviewed a generic cw20-blocklist CosmWasm module; the report gives no chain and no instantiated contract, and such modules are embedded per-token, so no deployment could be attributed. |
| 1086 | CallistoVault | 1 | 0/1 | No chain or deployment identifiable from the report text; name search on Ethereum found no match. |
| 1087 | Camp Network Origin platform (IpNFT, Marketplace, DisputeModule) | 1 | 0/1 | Camp Network Origin platform review (IpNFT, Marketplace, DisputeModule). The batch record has no report URL or address; Camp's explorer and docs deployment pages were not reachable in this pass, so no address is recorded |
| 1088 | Canopy program | 1 | 0/1 | CODESPECT Jan-2026 review of the Canopy Solana program (deposit instruction, token-account validation). The program ID is not in the extract and no Canopy program could be confirmed on Solana. DefiLlama's Canopy is a Mov |
| 1089 | Canto Dex Oracle contest | 1 | 0/1 | Canto chain (7700); DEX oracle deployment address not published. |
| 1090 | Canto Identity Protocol contest | 1 | 0/1 | Canto mainnet (chain id 7700) deployment exists in principle, but neither docs.cantoidentity.build nor the contest repo publishes addresses and the Canto explorer name search returned nothing within budget; recorded NOT_ |
| 1091 | Canto Invitational | 1 | 0/1 | Code4rena 2024-01 Canto (Canto Lending Market). Canto L1 halted in 2024 and its explorer/API was not reachable from this environment; no address is given in the report text, so nothing is recorded. |
| 1092 | Cega SFN | 1 | 0/1 | OtterSec review of Cega SFN (Solana). docs.cega.fi did not resolve, no report_addresses, and no program ID surfaced in search results. DefiLlama lists Cega V1/V2 with null addresses. |
| 1093 | Celestia Q2 2025 | 1 | 0/1 | CIP-31 audit (Informal Systems), chain-level finding only. |
| 1094 | ChainPro | 1 | 0/1 | No deployment information in the report; no project contract surfaced. |
| 1095 | Chromia Postchain (EIF bridge) | 1 | 0/1 | Repo identity is certain (function withdrawBySnapshot only exists in postchain-eif), but the project publishes no mainnet deployment address. Chromia's docs sitemap exposes no bridge address page; leaving address null ra |
| 1096 | Citadel-1 | 1 | 0/1 | Identified only as a Base NFT/auction game from report text; no contract address or docs found. |
| 1097 | Citrex | 1 | 0/1 | Zenith/Code4rena 2025 report targets OrderDispatch.sol and Ciao.sol; DefiLlama lists 'Citrex Markets' on Sei but publishes no address. citrex.io/docs.citrex.io do not resolve and no Sei explorer name search returned a ve |
| 1098 | ClickPesa Oracle Aggregator Stellar | 1 | 0/1 | Non-EVM (Soroban); deployment id unresolved. |
| 1099 | Codex CDEX (Codex on Althash LLC) | 1 | 0/1 | Identity limited to the audit-id prefix 'codex cdex codex on althash llc' and the report name 'Codex Staking May 2022'. No reachable project site or address book; left as NOT_FOUND rather than guessing an HTMLCoin/Althas |
| 1100 | Colexion | 1 | 0/1 | One explorer name search; no marketplace contract address published. The audited scope (Colexion ERC721, Dec 2021) is a marketplace, not the collection tokens found. |
| 1101 | Comet | 1 | 0/1 | CosmWasm pool contract with no chain/code-id in the report; EVM address tracing not applicable. Fantom Comet Finance candidate rejected as a different protocol. |
| 1102 | Computable | 1 | 0/1 | Nothing resolvable: no report URL, no repo, no protocol site. Recorded NOT_FOUND rather than guessing an address. If the parent has the Trail of Bits 2019-07 report text, the contract name/address may be recoverable from |
| 1103 | Cook Index | 1 | 0/1 | SlowMist 2021 Cook Index. The COOK token is the only confirmed Cook address and does not host the audited slippage logic, so it was not recorded as a trace. |
| 1104 | Cornerstone | 1 | 0/1 | NEAR NFT-auction contract (ft_on_transfer). corn.near exists but holds no contract code; no Cornerstone auction account found. |
| 1105 | Cultured February | 1 | 0/1 | Zellic's February 2025 review (target VaultUtils.sol, network EVM). The extract gives no project site, repo or deployment, so no address was traced. |
| 1106 | DEFI MONEY - FEE MODULE | 1 | 0/1 | Bailsec audit of a fee module; no project site, docs or explorer entry resolved the deployment within the time box. |
| 1107 | DODO v3 | 1 | 0/1 | DODO v3 deployment table is JS-rendered on docs.dodoex.io and no D3Vault/D3Maker/DODO V3 contract name resolves on Ethereum Blockscout. DefiLlama's DODO address 0x43Dfc415... is the DODO token and was rejected. |
| 1108 | DOP | 1 | 0/1 | Data Ownership Protocol identified; the audited DOP token/fund contract address was not confirmable, so no token address was guessed. |
| 1109 | DPNMDEFI | 1 | 0/1 | No identity or deployment found. |
| 1110 | DVX | 1 | 0/1 | Body not in corpus (empty body_path). |
| 1111 | DXdao dxGovernance Audit | 1 | 0/1 | Ethereum Blockscout search for dxGovernance/DXdao returns DXdao and DXD tokens plus reputation tokens, but no governance module; the audited contract cannot be pinned to an address. |
| 1112 | Dabba Network | 1 | 0/1 | DePIN WiFi marketplace on Solana; no program ID published for the audited singleton/bootstrap. |
| 1113 | Dapper Labs Dapper Smart Contract Wallet | 1 | 0/1 | Sigma Prime 2019 review of the Dapper smart-contract wallet on Flow. The report names no account address and Dapper's Flow account/contract address for the wallet is not published in any reachable doc; nothing recorded. |
| 1114 | Dapper Smart Contract Wallet | 1 | 0/1 | The reviewed wallet is Dapper's Ethereum smart-contract wallet (Sigma Prime review v2). Contracts compile/deploy per user via WalletFactory; no factory address surfaced in the repo README or sources page reached. |
| 1115 | DeFis-Network Swap cn 1 0 | 1 | 0/1 | 2020 project; no live deployment source found in the timebox. |
| 1116 | DeSyn ETH Flashloan Leverage Staking | 1 | 0/1 | DeSyn docs describe the SDT model but publish no contract addresses; DeFiLlama entries cover other DeSyn products (basis trading, safe, liquid strategy) with no core address. |
| 1117 | Decent | 1 | 0/1 | Six 'Decent Eth' (DcntEth) ERC-20s exist on Ethereum, all with dust supply and one holder (test deployments); none could be confirmed as the audited DcntEth router contract, so no address is recorded. |
| 1118 | Dedcat (2025-11 Dedcat Smart Contract) | 1 | 0/1 | Hashlock audit identity confirmed only. No deployment address, chain or docs page could be surfaced; NOT_FOUND rather than guessing a BSC/Base meme-token address. |
| 1119 | Defactor Buyback | 1 | 0/1 | Zokyo review of Defactor Buyback (Nov 2023). No buyback deployment address found. |
| 1120 | Dega ISPO | 1 | 0/1 | Dega ran ISPOs on Cardano, Ethereum and MELD. The finding involves a stETH rebase, so an Ethereum-side staking/reward contract is implied, but no address is published; the DEGA token (0x97aeE01ed2aabAd9F54692f94461AE761D |
| 1121 | DelNorte | 1 | 0/1 | DelNorte tokens exist on Ethereum, but the audited cross-chain treasury (ElasticTreasurySpoke/PeerTreasury) deployments were not located. |
| 1122 | Denis Miličević | 1 | 0/1 | Solo audit entry named after the auditor; the underlying protocol (LeverageRouter) is not identified in the batch metadata. |
| 1123 | Dexynth | 1 | 0/1 | Verichains review of Dexynth (2023). No deployment surface found; project appears unlaunched or defunct. |
| 1124 | Divicoin Token Contract | 1 | 0/1 | Legacy 2017 token; no live deployment located. |
| 1125 | Djed | 1 | 0/1 | Chain is Milkomeda-C1 (DefiLlama), but the explorer was offline during the run. |
| 1126 | Double-1 | 1 | 0/1 | Chain confirmed by DefiLlama (Arbitrum, $414 TVL). No address publication found; address null. |
| 1127 | Duality: Dex and Incentives modules | 1 | 0/1 | Informal Systems review; full body unavailable (publisher_notice). |
| 1128 | Dumont | 1 | 0/1 | MONT rewards game; chain and address not established. |
| 1129 | Dumont (team 2024 09 16 dumont) | 1 | 0/1 | Only the audit report is public. With the project repo private and no site or deployment manifest, no chain or address can be substantiated; left NOT_FOUND rather than guessing a Base/Mont token. |
| 1130 | ERC-20 | 1 | 0/1 | KOK token audit (iosiro, 2020). The report page contains no contract address and no explorer hit was confirmed. |
| 1131 | EVEREST GOLD | 1 | 0/1 | 2020 Verichains review of a MultiOwner wallet; no deployment address or chain published. |
| 1132 | EXA Finance Smart Contracts | 1 | 0/1 | Runtime Verification audit of the Algorand 'Baskets' TEAL contract; no EVM deployment exists. |
| 1133 | Eco PhaseI v 1 0 | 1 | 0/1 | Eco's 2022 contract suite could not be tied to a current deployment; no chain or address recorded rather than guessing. |
| 1134 | Element Finance Contract | 1 | 0/1 | Runtime Verification's 2021 review of Element Finance contracts. Element deploys tranche/principal-token contracts through factories per pool and the report extract names no instance; the ELFI token was deliberately not  |
| 1135 | Elixir | 1 | 0/1 | Elixir's sdeUSD is a Move package (Sui); no package ID in the report and Sui has no public name-search API, so the address is genuinely unavailable. |
| 1136 | Entropy/Rust Cryptography | 1 | 0/1 | Library audit; address tracing not applicable. |
| 1137 | Ern | 1 | 0/1 | No address. |
| 1138 | EthSign Launchpad | 1 | 0/1 | OtterSec 2024 review of EthSign Launchpad, the TokenTable token-distribution product. TokenTable deploys per-project instances; the launchpad implementation address is not published on docs.tokentable.xyz (its deployment |
| 1139 | EthereumOctant v2 | 1 | 0/1 | Octant v2 (Golem) uses Yearn-style TokenizedStrategy vaults; docs describe the flow but not deployment addresses. No address found within search budget. |
| 1140 | Etherfuse Stablebond | 1 | 0/1 | Etherfuse Stablebond is a Solana Anchor program; the report text does not contain the program id and no program address surfaced within budget. |
| 1141 | Ethos Network Financial Contracts | 1 | 0/1 | Ethos financial contracts on Base; no public deployment table found. |
| 1142 | Eywa CLP | 1 | 0/1 | MixBytes Aug-2024 review of Eywa's CrossCurve CLP contracts. Name search returns only EYWA ERC-20 tokens; the CLP pool and cross-chain adapter addresses are not in the extract, and Eywa's docs root has no deployments pag |
| 1143 | FCHAIN Validator and Staking | 1 | 0/1 | OpenZeppelin audited 0xFFoundation/fchain-contracts (StakeManager.sol, ValidatorRegistry.sol, Avalanche ICM) in Mar-2025. The report gives no deployment address and the repo is not publicly readable (GitHub API 404). |
| 1144 | FChain Validator | 1 | 0/1 | Identity unresolved; no deployment data. |
| 1145 | FOMOSolana | 1 | 0/1 | Solana game/NFT program per OtterSec classification; address not disclosed. |
| 1146 | Fabric Crowdfinancing | 1 | 0/1 | Small 2023 crowdfinancing audit; chain and deployment not public. |
| 1147 | Fair Funding by Alchemix & Unstoppable | 1 | 0/1 | The Sherlock report only carries Alchemix mainnet dependency addresses in its PoC setup (alchemist 0x062Bf7..., whitelist 0xA3dfCc..., yvWETH 0xa258C4...), which are not Fair Funding deployments and were rejected. No Fai |
| 1148 | Fee Abstraction Module by Notional | 1 | 0/1 | Osmosis module; no deployable address. |
| 1149 | Feeder Lending | 1 | 0/1 | No identity beyond the audit. Address not recoverable within the timebox. |
| 1150 | Fields of Mars | 1 | 0/1 | Terra-native CosmWasm project; no contract address published in the repository. |
| 1151 | Final Fiat | 1 | 0/1 | No identity evidence at all (no report_urls, no addresses in the audit text); nothing to trace. |
| 1152 | Float Capital contest | 1 | 0/1 | 2021 Code4rena contest; repo states deployment intent for Polygon. No live address found. |
| 1153 | Flux Protocol | 1 | 0/1 | Identity ambiguity with Flux Finance (a Compound fork) was avoided; neither the oracle aggregator nor its deployment could be verified on-chain. |
| 1154 | FlyFoundation | 1 | 0/1 | FlyPad/FLY on BSC; only token-level hits surfaced and no FlyFoundation vault/launch contract address was confirmed. |
| 1155 | Foil Vault | 1 | 0/1 | Guardian Audits 2025-01-13 report names Vault.sol, TradeModule.sol, LiquidityModule.sol and ConfiguratonModule but gives no website, chain or address; no public deployment surfaced. |
| 1156 | Folks Finance Capital Market Protocol v2 | 1 | 0/1 | Folks Finance v2 is an Algorand application suite; the DefiLlama Avalanche address belongs to the separate xChain product and was not used. |
| 1157 | Foresight | 1 | 0/1 | Cantina report on a prediction-market protocol; no deployment address in the extracted text and no docs site identified. |
| 1158 | Fragmint | 1 | 0/1 | Omega Audits' 2022 review of Fragmint, an NFT fractionalisation/auction protocol. The batch record has no report URL or site and no deployment was found; NOT_FOUND. |
| 1159 | G21 Capital Marketing | 1 | 0/1 | No report URL, body or source address in the batch; the project name matches no DefiLlama protocol and no public deployment. Nothing recorded rather than guessing. |
| 1160 | Gacha | 1 | 0/1 | No address recorded; deployment is on Abstract and addresses are not published. |
| 1161 | Gamma Position Managers | 1 | 0/1 | Gamma runs many single-sided Hypervisor/position-manager instances across ~35 chains, each per pool. Dozens of 'Hypervisor' contracts exist on Ethereum; none is identifiable as the July-2025 audited position manager from |
| 1162 | Genius Contracts | 1 | 0/1 | Code4rena 'Genius Contracts' competition covers Genius' cross-chain action/solver code (genius-actions, SolanaSolver). The project is multi-chain (Ethereum/BSC/Polygon per DefiLlama) but the audited action-contract addre |
| 1163 | Genius Foundation | 1 | 0/1 | No deployment address located. |
| 1164 | GinzaGaming Forwarders | 1 | 0/1 | Guardian Audits review of Ginza Gaming's ERC-2771-style forwarders; no public deployment address surfaced. |
| 1165 | Giza Pendle | 1 | 0/1 | Giza is an agent framework; the audited slippage check runs in off-chain transaction-building code. |
| 1166 | Gnosis Hashi | 1 | 0/1 | Hashi is Gnosis's message-bridge aggregation layer, deployed per chain. The former docs page now 404s and the Gnosis Blockscout instance is Cloudflare-gated; no address could be sourced within budget. |
| 1167 | Goat Trading | 1 | 0/1 | Sherlock 2024-03 contest; deploy script targets Ethereum mainnet (WETH) with Base/Arbitrum/BSC planned, but no deployed factory/router/pair address is published in the repo or report. |
| 1168 | Growth Labs GSquared | 1 | 0/1 | Dataset prefix 'ethereum evm gsquared' resolves to Growth Labs GSquared (Trail of Bits, 2022-10/11). Multi-chain, migration-related scope with no attributable deployed contract. |
| 1169 | HLOS | 1 | 0/1 | Could not resolve the project identity. No address recorded. |
| 1170 | HYTOPIA wallet | 1 | 0/1 | Audit is of the HYTOPIA wallet implementation (deploy-then-initialize pattern); no address published. |
| 1171 | Habittrade | 1 | 0/1 | Blocksec audit of HabitTrade's Stove Protocol (private repo). Stove docs publish no contract addresses and the chain was not confirmed within budget. |
| 1172 | Hadron Labs | 1 | 0/1 | No address recorded; identity ambiguity prevented a safe match. |
| 1173 | Halo | 1 | 0/1 | Only a social post confirms Base deployment; no address. |
| 1174 | HaloTrade | 1 | 0/1 | BlockSec Rust audit (Jun-2023) of the CosmWasm halo-pair contract; chain identified as Aura via the DefiLlama adapter, address not located. |
| 1175 | Haven1 Dec31 | 1 | 0/1 | Zokyo's Dec-2024 review of Haven1's H1NativeApplicationUpgradeable/H1DevelopedApplication multicall. Haven1 is a separate L1; its explorer and RPC endpoints returned Cloudflare errors (1016/530) during the batch, so no c |
| 1176 | Haven1 Feb25th | 1 | 0/1 | Haven1 is an EVM L1; the oracle-refresh finding targets a protocol deployed on it. No oracle contract address surfaced. |
| 1177 | Hesty | 1 | 0/1 | Real-estate investment platform on Base (EURC denominated). Repo HestyOfficial/hesty-contract contains TokenFactory/HestyRouter/HestyAccessControl but no address book or broadcast files. |
| 1178 | HighStreetMarket ProductToken | 1 | 0/1 | The repo contains ProductTokenHighBase.sol, but the publicly indexed instance 0xC89097B2aEe0820E3E3015E6cae3C89Cd1D3BC4f has no code on Ethereum, BSC or Polygon (eth_getCode returned empty on all three), and no other dep |
| 1179 | Holdefi Audit | 1 | 0/1 | Repository migrations exist but no deployed address is recorded there. |
| 1180 | Horizen | 1 | 0/1 | Coinspect 2021 source-code audit of the Horizen node. The finding is in main.cpp block timestamp validation, so there is no contract deployment to trace. |
| 1181 | HydraDX | 1 | 0/1 | Address tracing does not apply: the audited StableSwap logic is a Substrate pallet (extrinsic buy), not a deployed contract. |
| 1182 | Hypercube Protocol | 1 | 0/1 | Zellic's Hypercube review covers a Rust proving/verification stack (Basefold, rusted_evaluations, Buffer) - no Solidity/CosmWasm deployment or chain is referenced, so there is no on-chain address to trace. |
| 1183 | Hyperdrive | 1 | 0/1 | The Obsidian May-2025 review targets Hyperdrive on Solana (report metadata chains: ['Solana']); the two report 'addresses' are storage-slot constants, not accounts. The EVM 'Hyperdrive' in DefiLlama is a different protoc |
| 1184 | IBC-Go GMP Module and Attestations Light Client | 1 | 0/1 | Zellic review of the IBC-Go GMP module and attestations light client. This is chain-module code, so address tracing does not apply. |
| 1185 | Ideologi | 1 | 0/1 | No deployment information available for this Hacken-audited project. |
| 1186 | Ika | 1 | 0/1 | OtterSec 2025 review of Ika, a Sui Move MPC network. Contracts are Move packages addressed by 0x package ids; neither the report nor the repo README publishes the staking package id, so no address is recorded. |
| 1187 | Ikigai Studios Limited Oct15 | 1 | 0/1 | Zokyo 2025-10 review of Ikigai Studios rank/vesting contracts; no chain or address in the report record and no verified Ikigai rank contract found in Ethereum search. |
| 1188 | Iloop-contract | 1 | 0/1 | Solana program id not resolvable through the EVM explorer tooling used for this batch. |
| 1189 | Immutable - April 20, 2021 | 1 | 0/1 | Audit is of the Guild of Guardians game contracts (Dice.sol), not a public DeFi deployment. |
| 1190 | Increment | 1 | 0/1 | DefiLlama lists 'Increment Protocol' on zkSync Era with no address. Blockscout zkSync name search returned only an unverified contract named 'Increment' and unrelated airdrop tokens; nothing ties a StakedToken deployment |
| 1191 | Increment Finance (team 2024 03 05 increment) | 1 | 0/1 | Chain attribution (zkSync Era, id 324) comes from DefiLlama protocol metadata (api.llama.fi/protocol/increment-protocol). The repo is named 'peripheral-contracts' but no public Increment Finance GitHub org or address man |
| 1192 | Increment Finance: Increment Protocol | 1 | 0/1 | zkSync Era deployment; address not published. |
| 1193 | Index Fun Order Book | 1 | 0/1 | Contest-stage code; no live deployment identified within the search budget. |
| 1194 | Initia (Move / usernames module) | 1 | 0/1 | Chain inferred from the audited MoveVM/Initia L1 scope. No deployment address published; NOT_FOUND. |
| 1195 | InterBTC Parachain | 1 | 0/1 | Polkadot/Interlay parachain audit; EVM address not applicable. |
| 1196 | Inverter-1 | 1 | 0/1 | Audited code lives in InverterNetwork/contracts. Docs list no address table; module instances are deployed per workflow. |
| 1197 | Ironblocks Onchain Firewall | 1 | 0/1 | Identity from the ironblocks GitHub org (onchain-firewall, firewall-consumer, hello-firewall-foundry). The audited artifact is a policy template, not a single deployed contract; nothing recorded rather than guessing an a |
| 1198 | Ironblocks Onchain Firewall | 1 | 0/1 | OpenZeppelin audit of Ironblocks' policy contracts. The product is a hosted firewall; addresses are client-specific and not public. |
| 1199 | Itos | 1 | 0/1 | Small Pashov-reviewed RFQ protocol; no deployment address published in the report or discoverable on Ethereum explorers. |
| 1200 | Ivy Cash - August 29, 2021 | 1 | 0/1 | Solidified 2021 audit of an early paymaster/relayer; project appears defunct and has no discoverable deployment. |
| 1201 | JanisDex | 1 | 0/1 | UniswapV2 fork; pair addresses unresolved. |
| 1202 | JuicyFi | 1 | 0/1 | No identity or deployment found within the time box; the audit name alone does not resolve to a live chain or address. |
| 1203 | JustYours Oct25 | 1 | 0/1 | Zokyo Oct-2021 token-only review of JustYours' mint/access control. The report names no chain or address and the project has no current docs or explorer presence that could be attributed, so nothing is recorded. |
| 1204 | Kalmar | 1 | 0/1 | PeckShield review of Kalmar bond (2022). kalmar.io returned an empty placeholder; no verified BSC deployment found. |
| 1205 | KaoyaSwap | 1 | 0/1 | PeckShield 2022 review of KaoyaSwap (BSC). BscScan is Cloudflare-gated without an API key and the project's interface repository only contains forked mainnet token constants, so no BSC address could be evidenced. |
| 1206 | Kelp Delta | 1 | 0/1 | Kelp Delta = Kelp DAO / Harmonix Finance delta-neutral restaking vault on Base (report header: 'Report for Harmonix Finance'). Chain confirmed by the Solidity path; vault address not published, so address is null. |
| 1207 | Keyring Unwind | 1 | 0/1 | Chains from DefiLlama (Ethereum, Avalanche, Euler governor link). No address book in Keyring docs. |
| 1208 | Kingdomly Staking | 1 | 0/1 | Hashlock review of KingdomlyStaking; no deployment table or explorer hit for the staking contract surfaced. |
| 1209 | Knox Finance | 1 | 0/1 | No Knox Finance deployment is attributable; Ethereum 'Knox' hits are unrelated tokens (KnoxNet, KnoxsterChain, Fort Knox). |
| 1210 | Kraken Wallet In-App Browser | 1 | 0/1 | Trail of Bits review of the Kraken Wallet mobile in-app browser — a client-side component with no on-chain deployment. |
| 1211 | Kuiper (Code4rena 2021-12 'defiProtocol' contest) | 1 | 0/1 | Identity from the local Code4rena report (sponsor Kuiper, slug 2021-12-defiprotocol). No website or repo could be confirmed; project appears defunct and pre-deployment addresses were never published. |
| 1212 | Kuiper contest | 1 | 0/1 | Code4rena 2021-09 contest for 'DeFi Protocol' (Kuiper), an EVM/Solana NFT-index protocol. The contest repo has no deployment manifest; the verified Ethereum contract named 'Kuiper' (0x6dA5...) does not contain settleAuct |
| 1213 | Kuna Labs | 1 | 0/1 | OtterSec engagement OS-KUL-ADV-00 (2025-06-20); chain and deployment unresolved within the timebox. |
| 1214 | LEGENDS NEVER DIE | 1 | 0/1 | PeckShield's 2021 review of the Legends Never Die BSC game (_claimWeekly). The extract carries no contract address and no address book or explorer match was found. |
| 1215 | LIDO KSM | 1 | 0/1 | MixBytes Lido KSM audit; no deployment address in the batch metadata and the Kusama-side deployment was not resolved. |
| 1216 | LSD Network - Stakehouse | 1 | 0/1 | SyndicateRewardsProcessor has no verified deployment under that name on Ethereum Blockscout; Stakehouse-branded contracts exist but the audited processor was not matched. |
| 1217 | Levva Protocol | 1 | 0/1 | Marginly/Levva deployment JSONs hold configuration, not live pool addresses. |
| 1218 | Libertum Bonding | 1 | 0/1 | Hashlock review of a bonding-curve token that Libertum documents as not yet deployed. |
| 1219 | Linea ENS | 1 | 0/1 | Two-chain design (Linea registry + Ethereum L1 resolver/verifier) confirmed from github.com/Consensys/linea-ens; no published deployment addresses for either side. |
| 1220 | LineaBank | 1 | 0/1 | PeckShield 2023 review of LineaBank (Linea lending fork) including a SaleLabOverflowFarm contract. No published address and no verifiable explorer result, so nothing is recorded rather than guessing. |
| 1221 | Linum Labs - July 15, 2021 | 1 | 0/1 | Mito NFT project. Name collides with several unrelated Mito/Mitosis tokens on Ethereum; no NFT.sol deployment can be attributed. |
| 1222 | LionDEX | 1 | 0/1 | Arbitrum deployment; no verified contract lookup available (Arbiscan API key not available). |
| 1223 | LiquidOps Pool | 1 | 0/1 | LiquidOps is an AO/Arweave lending protocol; finding sits in Lua process code (interest.lua), so there is no EVM address to trace. Project identity from docs.liquidops.io and github.com/useLiquidOps. |
| 1224 | Liquidity Staking | 1 | 0/1 | Non-EVM; no address applicable. |
| 1225 | Lombard Finance (Lending Platform, Dec 2022) | 1 | 0/1 | No chain, docs or address book for the audited 2022 lending platform could be identified. Live Lombard Finance (LBTC) addresses were deliberately not recorded because they belong to a different project. |
| 1226 | Lombard Solana Integration | 1 | 0/1 | OpenZeppelin 2025 review of Lombard's Solana integration; the audited artifact is a Solana program and its program id is not present in the report text or the docs pages reached. |
| 1227 | Loop Vaults | 1 | 0/1 | Pashov review of LoopVaults (Apr-May 2025). The report extract names totalAssets/_vestingInterest but no project site, repo or deployment page; the vault address was not identified. |
| 1228 | LoopVaults | 1 | 0/1 | No report_url or body in the corpus entry. |
| 1229 | Lorenzo OTF contract | 1 | 0/1 | Lorenzo's docs describe the OTF (on-chain traded fund) vault but publish no deployment address, and the Cantina report dates from 2025 with an unnamed instance. Lorenzo's tokens are on BNB Chain/Ethereum per DefiLlama, s |
| 1230 | LottoPGF | 1 | 0/1 | Code4rena/Guardian review of LottoPGF's Lootery. The site says lottery factories are deployed on Ethereum L2s (two chains) but publishes no factory or Lootery address, and no explorer search attributed one, so nothing is |
| 1231 | Lumis LumisContracts v 1 1 | 1 | 0/1 | Lumis is an Euler-based ALM on Base; report references Base 41 times. Specific ALM address not located. |
| 1232 | Lumiterra | 1 | 0/1 | Game/economy docs publish token addresses only (e.g. LUDAMOON); the HashCore sale contract address is not published and no explorer hit surfaced. |
| 1233 | Lyra | 1 | 0/1 | Sherlock's Jan-2023 Lyra review targets the Lyra V2 LiquidityPool (Optimism/Arbitrum). Lyra has since rebranded to Derive and the old docs redirect to derive.xyz, whose contract page describes the perps exchange rather t |
| 1234 | MAIV Dec2 | 1 | 0/1 | No address. |
| 1235 | MAJR INC | 1 | 0/1 | MAJR INC review. The batch record has no report URL and no site, repo or explorer entry for MAJR was identified; chain unknown. |
| 1236 | MDK | 1 | 0/1 | MDK (White Noise) is a Nostr/MLS messaging protocol reviewed by Least Authority; no smart contract is involved and the finding is in KeyPackage handling. |
| 1237 | MaGaugeV2Upgradeable && ChronosMarketplace | 1 | 0/1 | Chronos (Arbitrum) NFT marketplace and MaGaugeV2; no marketplace address in public docs. |
| 1238 | Mage Finance | 1 | 0/1 | BlockSec review of Mage Finance on Merlin (body withheld in corpus). No address in the report; DefiLlama lists the protocol on Merlin without a contract address. |
| 1239 | MagicSea | 1 | 0/1 | Chain confirmed via DeFiLlama/explorer (IOTA EVM, 8822); contract address not confirmed. |
| 1240 | Magma | 1 | 0/1 | Sui Move package/object IDs are not published in the audited material available here. |
| 1241 | Maia | 1 | 0/1 | Maia DAO (Metis/Arbitrum). docs.maiadao.io returned 403 and the Arbitrum explorer is Cloudflare-blocked; RootBridgeAgent address not confirmed. |
| 1242 | Malt | 1 | 0/1 | No chain confirmed for the audited deployment; no address attributable. |
| 1243 | Malt Protocol - Versus contest | 1 | 0/1 | Code4rena Feb-2023 Malt versus contest (livePrice / defaultIncentive). Malt is a 2021-2022 Ethereum stablecoin project; no current deployment or address book was found and Blockscout name search returns only unrelated 'M |
| 1244 | Marco Polo DEX | 1 | 0/1 | OtterSec review of Marco Polo DEX (2022). No address in the report text and no public address book surfaced. |
| 1245 | Mars Rover | 1 | 0/1 | Cosmos/CosmWasm deployment; address format is not EVM and was not published in the audit. |
| 1246 | Mars Rover Updates | 1 | 0/1 | Mars v2 is CosmWasm (Rust): the finding cites contracts/credit-manager/src/health.rs. CosmWasm contracts are instantiated per chain with bech32 addresses and the credit-manager instance is not published in the extract, s |
| 1247 | Mars v2 on Neutron | 1 | 0/1 | Mars v2 on Neutron is a CosmWasm deployment; no contract address was published in the material reachable here. |
| 1248 | Mayan Sui | 1 | 0/1 | OtterSec review of Mayan's Sui Move contracts. No Sui package id appears in the extract; Mayan's EVM and Solana deployments are different codebases and were not substituted. |
| 1249 | Melonport. January 9, 2019. | 1 | 0/1 | The 2019 Melonport v1 fund contracts predate the Enzyme rewrite; no 2019-era MelonFund deployment is verified or linked from the report, and current Enzyme addresses are a different protocol generation. |
| 1250 | Membrane | 1 | 0/1 | CosmWasm protocol on Osmosis (report references cw-utils and Osmosis 11 times). No EVM deployment; no osmo1 contract address surfaced. |
| 1251 | MetaMask/Partner Snaps - StarknetSnap | 1 | 0/1 | Off-chain wallet snap; address tracing does not apply. Finding is a UI/signing-preview injection, still profit-relevant. |
| 1252 | MetaPool - Staking Pools Aurora | 1 | 0/1 | Aurora (EVM, chain id 1313161554) deployment not located; explorer search returned no MetaPool contract. |
| 1253 | MightyNetERC1155Claimer | 1 | 0/1 | Zellic 2023 report states the reviewed MightyNetERC1155Claimer code was not deployed to Ethereum mainnet at assessment time; no later deployment surfaced. |
| 1254 | Minimax Finance | 1 | 0/1 | No identity or deployment surfaced from DefiLlama/CoinGecko or the gated Hacken page; recorded NOT_FOUND rather than guessing a BSC token address. |
| 1255 | Minterest Zokyo 14thMarch | 1 | 0/1 | Only the MTI/'minty' token and deployer surfaced on Mantle; the audited swap/pool contract address was not found within the timebox. NOT_FOUND rather than mapping the token. |
| 1256 | Mintify | 1 | 0/1 | Hexens review of Mintify staking (Mar 2025). No staking deployment resolvable from reachable sources. |
| 1257 | Mirror Decentralized | 1 | 0/1 | Terra app is largely deprecated; DefiLlama's Mirror 'address' is the MIR ERC-20 (0x09a3ecaf...), not the collateral oracle, so it was rejected. |
| 1258 | Mitosis - (September | 1 | 0/1 | ReclaimQueue is a contract on Mitosis L1; the explorer API did not return a match for ReclaimQueue and no docs deployment table was found. |
| 1259 | Modular Smart Contract Account (MSCA) | 1 | 0/1 | No address: the audit concerns account-abstraction module design rather than one deployment. |
| 1260 | Monday.trade | 1 | 0/1 | Monday Trade runs on Monad (docs.monday.trade). No deployment address published in reachable docs. |
| 1261 | MovEx | 1 | 0/1 | Audit by MoveBit for a Move-based AMM; Stage 2 EVM address tracing does not apply. Recorded as NOT_FOUND rather than guessing a package id. |
| 1262 | MoviePass Exchange | 1 | 0/1 | Certora audit is of Move-language contracts; no public deployment address surfaced in the timebox. The Ethereum MOVIE token (0x7a54Fae94B6960D9f7316612EEC179078e911769) exists but is not attributable to the audited excha |
| 1263 | Mute Switch - Versus contest | 1 | 0/1 | Chain from Mute's zkSync Era deployment; the Switch bond contracts may never have shipped, and no address is published. |
| 1264 | Mutuum Finance | 1 | 0/1 | Halborn audit of contracts ahead of the V1 launch on Ethereum; no deployed lending-market address is public. |
| 1265 | MyCowrie | 1 | 0/1 | No identity signal in the corpus entry (no report_urls, no body_path) and no reachable deployment. Nothing to trace. |
| 1266 | Myso v2 | 1 | 0/1 | MYSO v2 zero-liquidation loans; deployed on Arbitrum, Mantle, Ethereum, Telos per DefiLlama. |
| 1267 | N1xyz nord | 1 | 0/1 | N1 is a new L1 with no public Blockscout/Etherscan coverage reachable here; the Nord bridge/withdrawal-root contracts could not be located. |
| 1268 | N4T | 1 | 0/1 | No report URL/body in the corpus and no deployment page; left null rather than guessing a chain. |
| 1269 | NOAH-DAO | 1 | 0/1 | BlockSec 2023 review (noah v1.0). The report does not publish addresses and no NOAH DAO bribe contract could be tied to it. Nothing recorded. |
| 1270 | Namada Ethereum Bridge | 1 | 0/1 | Oak Security Mar-2023 review of the Namada Ethereum Bridge. The report and the Namada specs describe the vault/contract design but publish no deployed address, and the bridge launched after the review. |
| 1271 | Nemeos | 1 | 0/1 | No identity or address. |
| 1272 | Neptune Protocol | 1 | 0/1 | DefiLlama's Neptune entries (Neptune Finance on Injective, Neptune Protocol on Eclipse) are different products and were not used. |
| 1273 | Neutron Independent Chain | 1 | 0/1 | Neutron is a Cosmos SDK chain; the audited staking logic is a native module, so no contract address exists. |
| 1274 | Ninja | 1 | 0/1 | Oak Security report classifies the target as Cosmos; no chain id, program or contract address is published, so nothing can be traced. |
| 1275 | Ninja Yield protocol | 1 | 0/1 | Pashov audit (2022) of a Solana-style vault ('NinjaYielder'); report names no deployment and the audited code appears never to have shipped. No website, docs or GitHub address book surfaced, and no contract with this sha |
| 1276 | Nocturne | 1 | 0/1 | Nocturne wound down in 2024; no protocol contract address is published in the repository. |
| 1277 | Nocturne Snap | 1 | 0/1 | Off-chain artifact (snap RPC method); address tracing is not applicable, recorded NOT_FOUND. |
| 1278 | Non-Fungible | 1 | 0/1 | Code4rena 2022-11 engagement; no deployment information available. |
| 1279 | Noya | 1 | 0/1 | No deployment found. |
| 1280 | Nunchi | 1 | 0/1 | Guardian Audits Oct-2025 review of Nunchi vaults/strategies. The report describes a pre-deployment codebase and publishes no address; the only 0x string in the report series (0x0868A6...) has no code on Ethereum. Nothing |
| 1281 | ONCHAINID | 1 | 0/1 | Per-identity proxy architecture means a single protocol address does not exist; the audited implementation address was not confirmed. |
| 1282 | OObleck | 1 | 0/1 | Corpus record has no report URL, body text or chain; only the finding title referencing ClaimOperator and ERC-6551 TBA validation. Nothing to trace against. |
| 1283 | OPINION | 1 | 0/1 | OPINION is a BNB Chain prediction market. The only confirmed address is the OPN token (0x7977BF3e7e0c954D12cdcA3E013ADAf57E0B06E0, BSC); the order-book/exchange contract that holds maker funds is not published, and the t |
| 1284 | OPRF Noir Circuits | 1 | 0/1 | Circuit-level audit; address tracing not applicable. |
| 1285 | ORACLE DAO | 1 | 0/1 | Decurity's 2022 review of ORACLE DAO (staking access control). No project site, docs or explorer entry attributable to this DAO was identified, and the report extract gives no chain or address; NOT_FOUND. |
| 1286 | Octopus Network | 1 | 0/1 | Octopus Network (now Omnity). NEAR account oct-convertor.near does not exist on mainnet (RPC UNKNOWN_ACCOUNT). |
| 1287 | Odx Contracts | 1 | 0/1 | Cantina April 2025 review. No protocol identity beyond contract file names; ODX ticker search on Ethereum returned unrelated tokens. |
| 1288 | Ohm | 1 | 0/1 | Source contract is public but no Olympus YieldStreamer deployment address was found. |
| 1289 | Onchain Labs Router | 1 | 0/1 | Batch entry carries no report link or chain; nothing to trace. |
| 1290 | Ondo August10 | 1 | 0/1 | Ondo v1 (legacy) contracts from the August 2020 review are unresolved; current Ondo deployments are a different codebase and were not substituted. |
| 1291 | Opal Protocol | 1 | 0/1 | No identity or deployment found. |
| 1292 | Optimisim Interop Proofs | 1 | 0/1 | Cantina's 2025 review of the OP Stack interop proofs (CrossL2Inbox / Superchain interop). At review time this was pre-deployment code for the interop devnet; the batch carries no addresses and the OP Mainnet address tabl |
| 1293 | Oracly | 1 | 0/1 | Name search returned only unrelated oracle contracts; the fuzzland report does not carry an address and no docs/deployment page was found in the timebox. |
| 1294 | Orderly Solana Vault Contract | 1 | 0/1 | Repo Anchor.toml publishes only localnet/devnet program ids (solana-vault = 9shwxWDUNhtwkHocsUAmrNAQfBH2DHh4njdAEdHZZkF2 on localnet); no mainnet program id is published. |
| 1295 | Origin Protocol - December 17, 2020 | 1 | 0/1 | Origin is on Ethereum, but the 2020 staking contract (preApprovedStake) is not present under that name in Ethereum Blockscout and no deployment page was reachable. |
| 1296 | Oro | 1 | 0/1 | Solana-native; program id not located. |
| 1297 | Osmosis Transmuter v3 | 1 | 0/1 | Osmosis app-chain CosmWasm contract; address would be a bech32 contract, not an EVM address, so recorded as NOT_FOUND. |
| 1298 | OverHere | 1 | 0/1 | Only the audit PDF identifies the project. No verified contract, repo or deployment page found. |
| 1299 | P2P.org Staking Fee Distributor Diff | 1 | 0/1 | Institutional staking fee distributor; deployments are client-specific and not published. |
| 1300 | Particle | 1 | 0/1 | Particle NFT-lending protocol; distinct from Particle LAMM/DUO on Blast, which were not used. |
| 1301 | Party Protocol | 1 | 0/1 | docs.party.app no longer resolves. Ethereum Blockscout lists several verified CrowdfundFactory contracts, but none could be tied to PartyDAO, so no address is attributed rather than guessing. |
| 1302 | Patchwork-2 | 1 | 0/1 | Macro audit 2023-12-19 of the Patchwork NFT-fragment protocol (PatchworkProtocol / PatchworkFragmentSingle). Report has no addresses and no repo link. An Ethereum name search returns only an unrelated 'MNTGE Patchwork Li |
| 1303 | PenguinGotchi | 1 | 0/1 | Shieldify 2025 review of PenguinGotchi. No site, repository or deployment address is published, and no matching game contract is indexed on Ethereum. |
| 1304 | Perennial V2 | 1 | 0/1 | Perennial V2 update-4 audit. No report link or deployment surface reachable; factory-deployed markets are not enumerable without docs. |
| 1305 | PieDAO Vested Token Migration and Crust | 1 | 0/1 | No address. |
| 1306 | Pillar | 1 | 0/1 | Pillar later moved to Zilliqa/account-abstraction; the 2020 Ethereum Gateway deployment was not locatable in the timebox. |
| 1307 | Pleasr Album | 1 | 0/1 | PleasrDAO's album sale. The PDF names only a Token contract with purchaseWithUSDC/onlyLive; no repository, docs or deployment link, and no Pleasr album contract is verified on Ethereum Blockscout. |
| 1308 | Plexus Nov24 | 1 | 0/1 | Zokyo review of Plexus (Nov 2023). No address in the report text; only the PLX token (0x60b9c9C167bA57cc376b0FaafC68Df5C9882328e, Ethereum) surfaces via DefiLlama and is a token, not the airdrop contract. |
| 1309 | Plume (smart wallets) | 1 | 0/1 | Identity resolved to the Plume Network smart-wallet contracts (WalletFactory, SmartWallet, SignedOperations). The audited code is in the public repo, but no deployed WalletFactory/SmartWallet address could be sourced: th |
| 1310 | Pluz Protocol | 1 | 0/1 | No identity beyond the audit; no address in the report. |
| 1311 | Polygon Yield Exposed Token | 1 | 0/1 | Sigma Prime report covers the vault-bridge 'yield exposed token' on Katana (Polygon's L2, chain id 747474). No token/vault address surfaced and Katana explorers are not searchable from this environment. |
| 1312 | Polygun | 1 | 0/1 | Promo double-payment is a backend idempotency bug in a custodial Telegram bot; no deployment address exists to trace. DefiLlama lists Polygon but gives no address. |
| 1313 | Polyhedra zk light client on LayerZero | 1 | 0/1 | LayerZero DVN/oracle contract; address unresolved. |
| 1314 | Pontem CLMM | 1 | 0/1 | OtterSec review of Pontem CLMM (2023). Aptos Move deployment; pontem.network does not publish the CLMM package address. |
| 1315 | Pool Fans-1 | 1 | 0/1 | No identity or deployment found. |
| 1316 | PoolParty (dApp) | 1 | 0/1 | No verified PoolPartyStaking contract on Ethereum, Optimism, Unichain or Scroll; the 'PoolParty' hits are unrelated ERC-20s and PartyToken (0x0fE0...) belongs to a different project. |
| 1317 | PowerBomb | 1 | 0/1 | One identity search; no live address for the Anchor-facing contract. Protocol site and repo no longer resolve. |
| 1318 | Prodigy | 1 | 0/1 | Only address in the report (0xf5bbe9558f4bf37f1eb82fb2cedb1c775fa56832, Base Goerli) is the Base Pyth UpdatePriceFeeds contract, not Prodigy. Vault deployment on Base not located. |
| 1319 | Proof of Neutrality | 1 | 0/1 | Runtime Verification 2023 review of the Proof of Neutrality Network (Blockswap). The four components (Payout Pool, etc.) are described but no live contract address is given, and Ethereum name search returns no PayoutPool |
| 1320 | Prospective world | 1 | 0/1 | NFT drop project with no attributable site, repository or deployment; no matching contract on the reachable explorers. |
| 1321 | Public - Breederdao Staking v2 | 1 | 0/1 | Blockscout Ethereum search found BreederDAO / Staked BreederDAO / Escrowed BreederDAO tokens, but no BreederTimeLockPool. The TimeLockPool contracts on Ethereum use compiler 0.4.24 and are not this 0.8-era staking pool. |
| 1322 | Public - Briky Land | 1 | 0/1 | Verichains 2024 review of Briky Land's Collection.sol (fractional real-estate NFT). Briky Capital is a BNB Chain project (BNB Chain announcement, DappBay listing), but neither the GitBook nor any reachable explorer entry |
| 1323 | Public - CyberEight Smartcontracts | 1 | 0/1 | Verichains audit of CyberEight GachaContract; EVM but chain and address are not published in the report. |
| 1324 | Public - Datagram Contract Hub | 1 | 0/1 | Datagram (DePIN) contract hub audit; no chain or address in the report, and name search produced only unrelated CrossChainBridge deployments. |
| 1325 | Public - Dot Arcade Token and Vesting | 1 | 0/1 | Verichains 2022 review of Dot Arcade's ADT token and vesting. The GitHub repo is public but carries no deployed address, and no live ADTVesting deployment surfaced. |
| 1326 | Public - FCO ETH | 1 | 0/1 | Verichains 'FCO Polygon v1.2' audit. 'FCO' has no discoverable public deployment page; no address could be attributed without guessing. |
| 1327 | Public - FCO TRON | 1 | 0/1 | TronScan TRC20 search for FCO returns no matching contract, and the Verichains report publishes no deployment address; chain recorded from the report title only. |
| 1328 | Public - House of Kibaa NFT Sale Smartcontracts | 1 | 0/1 | Verichains 2022 review of House of Kibaa NFT sale contracts. No address in the report record. |
| 1329 | Public - IStep Token | 1 | 0/1 | Verichains 2022 audit of the IStep token. The released body describes a restrictive check (DoSed user withdrawal), not a value-extraction bug, so profit is flipped to no. No deployment address published and no IStep cont |
| 1330 | Public - Kroma Spectrum | 1 | 0/1 | Chain identified from Kroma's own launch material; no SpectrumCore address found. |
| 1331 | Public - LOOPStarter Smartcontract | 1 | 0/1 | Verichains 2022 review of the LOOPStarter launchpad. |
| 1332 | Public - OP3N smartcontracts | 1 | 0/1 | Verichains Jan-2022 review of OP3N's Solidity contracts (NFTPackageTrade). The record has no chain, address or repo, and OP3N's public sites do not publish contract addresses, so nothing was attributed. |
| 1333 | Public - SenSwap | 1 | 0/1 | Verichains SenSwap audit on Solana; program id not present in the batch metadata and no verified program was resolved. |
| 1334 | Public - TheParallel | 1 | 0/1 | Polygon-era NFT/launch project; no live deployment reference. |
| 1335 | Public - UTXO Global Wallet Extension | 1 | 0/1 | The audited artifact is a browser extension (JavaScript), not a deployed contract. No on-chain address exists for the vulnerable component. |
| 1336 | Pyth Governance | 1 | 0/1 | OtterSec review of Pyth Governance (2022). No program id in the report text, and the governance program id could not be confirmed from Pyth docs within the timebox. |
| 1337 | Quail Contracts | 1 | 0/1 | Cantina solo audit (Mar 2024) of QuailFinance.sol; no repo, docs or explorer contract attributable to the project within the timebox. |
| 1338 | RAMS | 1 | 0/1 | RAMX is an EOSIO (C++) contract, not an EVM deployment; no traceable on-chain account was published in the report. |
| 1339 | REPORT FOR NIMBUS | 1 | 0/1 | Hexens 2021-12-16 report on Nimbus; body text withheld by publisher (publisher_notice). No chain, website or address in the report record. |
| 1340 | REPORT FOR SYNCDAO | 1 | 0/1 | Hexens 2022 review; the report names IStrategy/YearnStrategy but no deployment addresses, and no SyncDAO contract address is published. Nothing recorded. |
| 1341 | REPORT FOR TRUPENNY TOKEN | 1 | 0/1 | Hexens Jan-2022 review of the Trupenny token. The extract gives no chain or address. Name search finds an Ethereum contract 'Trupenny' (0xADB7d68bc6A86ab7b65d1632d9cb22213Ac7862b, TRU, 1 holder, 0.1 supply) that is plaus |
| 1342 | RabbitHole (quest-protocol) | 1 | 0/1 | RabbitHole quest-protocol audit (2023-01). The report entry has no body or address list; RabbitHole's QuestFactory/RabbitHoleReceipt/RabbitHoleTickets addresses are not published in the material reachable here, and no ve |
| 1343 | Raiinmaker Oct5 | 1 | 0/1 | Zokyo Oct-2021 review of Raiinmaker's CoiinMinter.sol. No deployment address in the report and no COIIN minter contract located on a public explorer. Nothing recorded. |
| 1344 | Rain Coin | 1 | 0/1 | Only the audit PDF (blocksec_raincoin_wrain) is known; no verified wRAIN deployment. |
| 1345 | Rally Foundation | 1 | 0/1 | Ambiguous name match; no address recorded rather than guessing. |
| 1346 | Random Earth Smart Contracts | 1 | 0/1 | Oak Security Dec-2021 review of Random Earth's Terra marketplace. Deployment is CosmWasm on Terra and no contract address is available in the report or in EVM explorer search, so NOT_FOUND. |
| 1347 | Reach | 1 | 0/1 | No project documentation, repository or deployment could be attributed to this 'Reach' audit; the name collides with several unrelated tokens and no matching contract was found on the reachable explorers. |
| 1348 | Recall | 1 | 0/1 | No deployment address found in the report; Recall uses a bucket/actor L1 model, so no explorer mapping was attempted. |
| 1349 | RedStone Oracles | 1 | 0/1 | Move payload library; no package id found within the timebox. |
| 1350 | Regnum Aurum veRAAC | 1 | 0/1 | The audited repo (RegnumAurumAcquisitionCorp/contracts) is private (404 this pass) and the 2026 review is of a pre-deployment codebase. RAAC itself is live on Ethereum (Blockscout shows RAAC Peg Stability Module sUSDS),  |
| 1351 | Research Portfolio | 1 | 0/1 | Composable Security 2023-09 review of Research Portfolio (ResearchTokenFactory); report names contracts only, with no chain or deployment address. |
| 1352 | Rigor Protocol (Code4rena 2022-08) | 1 | 0/1 | No website/GitHub/deployment surfaced; Code4rena scope only. |
| 1353 | Riley Holterhus, Lead Security Researcher | 1 | 0/1 | Metadata-only finding. Unresolvable within the timebox. |
| 1354 | Rip It (team 2025 04 25 ripit) | 1 | 0/1 | Project identity is certain from the audit report (rip.fun trading-card platform), but deployment tracing is blocked: repo private, site bot-walled, no published chain. NOT_FOUND rather than guessing Base/Abstract. |
| 1355 | Risk Harbor | 1 | 0/1 | Protocol appears sunset; no deployment address surfaced. |
| 1356 | Rolla Finance | 1 | 0/1 | Identity from code-423n4/2022-03-rolla (Rolla Finance options protocol). No live deployment could be located within the timebox. |
| 1357 | Round 2 | 1 | 0/1 | Sigma Prime review of Layr Labs / EigenLayer Sidecar Rewards v2.2 Round 2. No address in the report text and no public address book surfaced; deployment chain presumed Ethereum/EigenLayer but not confirmed. |
| 1358 | Royco Day | 1 | 0/1 | Identity ambiguous (Royco 'Day' vs the public royco-dawn repo); no address evidence, so left NOT_FOUND rather than guessing. |
| 1359 | SCOREPLAY | 1 | 0/1 | Prediction-market protocol, likely Base/Sophon; address not located. |
| 1360 | SNX | 1 | 0/1 | The MixBytes report path is Yearn Finance/SNX: an audited Yearn strategy for SNX, not a Synthetix core deployment. The specific strategy vault address is not named in the report extract. |
| 1361 | SOLANA: PRIVATE CHANNELS RE | 1 | 0/1 | Private Channels audit on Solana; no program id or public deployment information surfaced. |
| 1362 | SSO Account OIDC Recovery for SSOAccount | 1 | 0/1 | Wallet/account audit (audit_type: wallet_or_account). No deployment address is published. |
| 1363 | SafeGram | 1 | 0/1 | Obscure 2022 BEP20 token; no public deployment record found within the timebox. |
| 1364 | Saffron Finance | 1 | 0/1 | Audit is the Sherlock 'Saffron Lido Vaults' review; only the SFI token 0xb753428af26E81097e7fD17f40c88aaA3E04902c surfaced. Contracts named SaffronLido* on Ethereum are unrelated (e.g. SaffronLidoDrainer_FullAuto), so no |
| 1365 | Saffron Orca (team 2026 03 06 saffron) | 1 | 0/1 | Chain identified from the report body: Solana-based fixed-income vault program (Anchor). Saffron's live EVM docs (docs.saffron.finance/saffron-vaults/smart-contracts) cover a separate fixed-yield product on Ethereum/Arbi |
| 1366 | Sapien | 1 | 0/1 | The 2025 Sapien audit concerns a rewards/staking system that was not locatable on explorers; the old SapienNetwork presale repo deploys via migrations with no fixed addresses. |
| 1367 | SatLayer LST | 1 | 0/1 | Audited code is the CosmWasm LST staking hub deployed on Babylon, not an EVM contract. No published hub contract address found; SatLayer's EVM-side tokens (e.g. SLAY 0x51477A3002ee04B7542aDfe63ccdb50c00Ee5147 on Ethereum |
| 1368 | Satori Sports Satori Sports Token Royalties | 1 | 0/1 | Satori Sports NFT royalty contracts (Royalties, Token1155, TokenCollectibles721) have no published deployment address. |
| 1369 | Satoshi-Account | 1 | 0/1 | BlockSec Rust review 'satashi_account' (csna_verify_deposit). The PDF is image-only (no extractable text) and publishes no chain or address; no deployment is attributable. |
| 1370 | Satoshi-Bridge and | 1 | 0/1 | BlockSec Dec-2024 review of a Rust bitcoin bridge. The audited code (assert_one_yocto, account_id, BtcInputSignature, UtxoAdded) is a NEAR contract, but the report publishes no contract account id and no EVM/Near address |
| 1371 | Savea-1 | 1 | 0/1 | Macro 2024 review of Savea's Management contract. No addresses in the report and no Savea deployment page reachable (savea.finance does not resolve). Nothing recorded. |
| 1372 | Scroll zkTrie | 1 | 0/1 | The Trail of Bits review covers Scroll's zkTrie Go library and circuit/verifier stack, not a deployed contract: zkTrie proofs are verified in the prover/circuits and by the relayer, and the report names no contract or ch |
| 1373 | Seascape MSCP Token & Vesting | 1 | 0/1 | Halborn review of Seascape MSCP token and vesting (2021). No MSCP or vesting deployment located. |
| 1374 | Security Audit - Pye Fi | 1 | 0/1 | Pye is a Solana stake-account protocol; audited program id is not public. |
| 1375 | Security Technology for Smart Contracts Mushrooms Finance - Helvella F | 1 | 0/1 | Mushrooms Finance operated multi-chain vaults; Helvella Field vault/strategy address not recoverable in the timebox. |
| 1376 | Seismic Finance | 1 | 0/1 | Chain attribution (Blast) comes from DefiLlama protocol metadata (api.llama.fi/protocol/seismic). No website, docs or repo surfaced; the chain being defunct rules out address verification. |
| 1377 | Session Token | 1 | 0/1 | Zellic review of Session Token (2024). No deployed token contract could be attributed (Session is primarily an Oxen-based messenger). |
| 1378 | Settlement contracts | 1 | 0/1 | Cantina Apr-2025 review of t3rn 'Settlement contracts'. The t3rn/l2-settlements-contracts repo (escrowGMP, remoteOrder, claimerGMPV2) publishes no deployment addresses and the PDF contains none; DefiLlama's t3rn address  |
| 1379 | Sheepcoin | 1 | 0/1 | SHEEP on BNB (0xA182c1E29aB35947387E1eCFEAA7f939B36b88DF) surfaced but could not be tied to the audited SheepDog contract; rejected rather than guessed. |
| 1380 | SickleBridge StrategiesUpdate2 | 1 | 0/1 | Electisec 2026 review of Sickle Bridge Strategies Update 2. The bridge receiver/CCIP route contracts were not found at a published address; no address was asserted. |
| 1381 | Side Protocol | 1 | 0/1 | Non-EVM Cosmos chain; header validation lives in node code, so there is no deployment address to trace. |
| 1382 | Sifchain Peggy | 1 | 0/1 | Cosmos chain + Ethereum bridge contracts; Sifchain's docs explain the symbol whitelist mitigation but publish no addresses. |
| 1383 | Skillet / Kettle | 1 | 0/1 | OtterSec review of Kettle NFT lending (2023). Contract named in the report (Kettle.sol) but no deployment could be attributed. |
| 1384 | Slash Payment Aug23(Web3 Payment Platform)( ) upd | 1 | 0/1 | Identity unresolved beyond the report title. |
| 1385 | SnagMarketHybridV2 | 1 | 0/1 | Audit of Snag Solutions' marketplace contract; no deployment address located. |
| 1386 | SoSoValueLabs | 1 | 0/1 | SoSoValue SSI index product. Only the protocol token address is public. |
| 1387 | Sofa Automator(Oct | 1 | 0/1 | Zenith 2024 review of the SOFA Automator (mintProducts front-run). SOFA's docs page carries no contract table and the repo README no deployments. DefiLlama's SOFA.org address 0x57b96d4a... resolves to an unrelated 'RCH'  |
| 1388 | Sofiane Akermoun | 1 | 0/1 | Unit is named after the reviewer (Sofiane Akermoun); the finding is the AirDAO lock-cancellation reentrancy. No report URL, website deployment page or address is attached, and one search returned nothing usable. AirDAO's |
| 1389 | Solana EDDSA Token Distributor | 1 | 0/1 | TokenTable (Solana EDDSA distributor); program address not published. |
| 1390 | Solana Foundation Keystorecrate(pay) | 1 | 0/1 | Library/CLI audit (Cantina, Solana Foundation). No on-chain address by nature; recorded NOT_FOUND rather than inventing a program id. |
| 1391 | Sonic Airdrop | 1 | 0/1 | 2025-06-24 Sonic Airdrop contracts review. No contract address in the record; the claim portal is off-chain. |
| 1392 | Soroban-based automated market maker (AMM) protocol on Stellar | 1 | 0/1 | Stellar/Soroban deployment: addresses are contract IDs, not EVM hex; none found in the audit text or normalfinance repo within the search budget. |
| 1393 | Souls Club Wheel | 1 | 0/1 | No identity or address. |
| 1394 | Source Code - Soroban Tricorn Bridge v240725 | 1 | 0/1 | Stellar Soroban Rust bridge; contract IDs are not EVM addresses and none was published in the report metadata. |
| 1395 | Spectral | 1 | 0/1 | Zenith Apr-2025 review of Spectral's tax-token swap path. No address or chain appears in the extract. The Ethereum/Base 'Spectral' tokens returned by name search are not demonstrably the audited tax token, and 'Spectra'  |
| 1396 | Spicenet | 1 | 0/1 | Spicenet security review (withdrawal confirmation / chain_hash). The batch record has no report URL; Spicenet is a Cosmos-SDK style chain and no bech32 contract or EVM address was published, so nothing is recorded. |
| 1397 | Spicenet | 1 | 0/1 | Official docs repo is pepper-research/docs. Audit scope is Rust modules of a Sovereign SDK chain; no EVM/Solidity deployment exists. |
| 1398 | Spline Audit | 1 | 0/1 | Starknet protocol; fee-accrual finding. Address not located. |
| 1399 | Sprinter: Stash Contracts | 1 | 0/1 | Likely pre- or early-deployment; no address. |
| 1400 | Stacking Salmon | 1 | 0/1 | Berachain (chain id 80094) per the finding body; address not retrievable. |
| 1401 | StakeUp Protocol | 1 | 0/1 | No identity or deployment found. |
| 1402 | Stapleswap Omnipool EMA Oracle Circuit Breaker | 1 | 0/1 | Audit is of the HydraDX Substrate omnipool/stableswap runtime (code4rena 2024-02-hydradx); no EVM deployment address exists for the audited pallet. |
| 1403 | Starknet Perpetual | 1 | 0/1 | Chain is Starknet (Cairo/Scarb repo), but no deployed contract address is published; NOT_FOUND. |
| 1404 | Starter June26th | 1 | 0/1 | Starter launchpad staking docs describe pools but publish no contract addresses; chain not confirmed from the report. |
| 1405 | Steakhouse Leveraged Lending ERC4626 Yield Vault | 1 | 0/1 | Audit predates/does not name a live vault deployment; no contracts page found. |
| 1406 | Stoneii | 1 | 0/1 | Stoneii DeFi audit (KYCSoulBound.mintSBT). The batch record has no report URL and no site, repo or explorer entry attributable to Stoneii was found; the similarly named HashKey KYC adapter contracts are unrelated. |
| 1407 | Streaming Protocol contest | 1 | 0/1 | Contest codebase only (code-423n4/2021-11-streaming-findings). No project site or deployment could be attributed; Ethereum 'Streaming' hits are unrelated tokens. |
| 1408 | StylusPort Internal Review | 1 | 0/1 | Internal review; no live deployment identified. |
| 1409 | SubDao | 1 | 0/1 | No deployment address found; the audited contracts appear to be a pre-deployment review. |
| 1410 | Sui Move Application | 1 | 0/1 | Sui Move package; package ID not published. |
| 1411 | Summa-Vb | 1 | 0/1 | yAudit review of the Summa custody/inclusion-proof verifier; no production deployment address published (repo is the deliverable). |
| 1412 | SuperEarn: Crosschain | 1 | 0/1 | Cantina 2025 review of SuperEarn's crosschain contracts. DefiLlama lists SuperEarn only as a Klaytn deployment with no address, and the report publishes no chain or address for the crosschain version. Nothing recorded. |
| 1413 | Superposition | 1 | 0/1 | Move-based DEX; package address unresolved. |
| 1414 | Supplier Server Magic Protocol | 1 | 0/1 | Coinspect Magic Protocol supplier-server assessment; no chain or deployment address in the batch metadata and the protocol is not identifiable. |
| 1415 | Swaap Labs Pools | 1 | 0/1 | Swaap v1 pools are on Polygon; polygon.blockscout.com is Cloudflare-blocked and no deployment list was reachable. |
| 1416 | Swell ETH Staking Deposit Bot | 1 | 0/1 | CODESPECT review of Swell's ETH staking deposit bot (2026). The audited component is an off-chain bot, so there is no unique on-chain address. |
| 1417 | Syndr | 1 | 0/1 | Sherlock 2023 review of Syndr's key register/revoke (perps DEX on Arbitrum). No deployment address is published in the report extract or docs, and the project docs domain did not resolve during the batch. |
| 1418 | Tadle | 1 | 0/1 | Tadle identity resolved (tadle.com, points/pre-market marketplace; Cyfrin contest repo). No chain or deployment address could be sourced: the market-evm repository referenced by the audit README no longer exists and the  |
| 1419 | Tally Collaborative | 1 | 0/1 | Project identity uncertain (Tally governance vs a separate 'Tally Collaborative'); no address surfaced. |
| 1420 | Tally contest | 1 | 0/1 | Code4rena 2021-10 Tally contest (Swap.fillZrxQuote). 'Tally' contracts on Ethereum are governance/token contracts that cannot be tied to the audited Swap contract; no deployment address surfaced. |
| 1421 | TangleSwap Investment Hub | 1 | 0/1 | PostAuctionLauncher on ShimmerEVM; no contract address surfaced for the Investment Hub deployment. |
| 1422 | Taraxa Ficus Root Bridge | 1 | 0/1 | Taraxa-native (EVM-compatible) bridge; no address published. |
| 1423 | Taraxa Ficus Root Bridge Smart Contracts | 1 | 0/1 | Taraxa L1 bridge; the audited PillarBlock/finalization contracts are on the Taraxa chain and no address was located. |
| 1424 | TempleDAO-Origami | 1 | 0/1 | Origami v1 GMX/GLP vaults are on Arbitrum, but no vault address is published in the docs or repo README. The report's 0xB95DB5B1... is GMX's glpRewardRouter, a dependency, and was rejected. |
| 1425 | Tentou | 1 | 0/1 | No deployment address found. |
| 1426 | TermiX bsc-mcp Wallet us | 1 | 0/1 | Wallet-app audit (SlowMist); no protocol contract address. |
| 1427 | Terplayer BeraBTC Vault Token (BVT) Staking and Distribution | 1 | 0/1 | Berachain-based BVT staking product; neither the report nor a project page lists contract addresses, and no attributable deployment surfaced. |
| 1428 | Terrace Fi | 1 | 0/1 | Sherlock 2024-06 Terrace. Router/paymaster contracts not deployed publicly at a discoverable address. |
| 1429 | Thanos L2 Native Token Bridge | 1 | 0/1 | Tokamak Thanos OP-Stack L2; L1/L2 bridge contract addresses were not located within budget. |
| 1430 | Thorchain | 1 | 0/1 | Code4rena 2024-06 THORChain findings. THORChain is a Cosmos app-chain: vaults are protocol-level accounts rather than a deployed contract, so there is no contract address to record. The finding text is the warden submiss |
| 1431 | ThreeS | 1 | 0/1 | Non-EVM Chromia dapp; no address in report. |
| 1432 | Timewave Covenants | 1 | 0/1 | Finding drains NTRN, so the chain is Neutron (neutron-1); no address was obtained and none was guessed. |
| 1433 | Tinlake Contracts + Actions | 1 | 0/1 | Centrifuge Tinlake is deployed per pool on Ethereum mainnet. The audit covers shared Solidity contracts (centrifuge/tinlake repo) so no one address maps; docs page blocked by Cloudflare, chain confirmed by docs search sn |
| 1434 | Tokamak Network | 1 | 0/1 | Tokamak docs contract page is JS-rendered and yielded no addresses. |
| 1435 | Tokenmill V2 | 1 | 0/1 | No address recorded. DefiLlama lists the project with no address on either chain. |
| 1436 | Tokens Farm Zokyo january 11 | 1 | 0/1 | Zokyo 2023 (Jan 11) audit of TokensFarm, same farm-as-a-service template as the Sep 2022 report. Each farm is a separate TokensFarm deployment and no official farm registry/address was published; the service concluded in |
| 1437 | Tokensoft | 1 | 0/1 | No address. |
| 1438 | Torque Labs | 1 | 0/1 | Solana program ids are not enumerable by name through the EVM explorers used here; no docs deployment table found. |
| 1439 | TraitForge | 1 | 0/1 | Code4rena 2024-07 TraitForge. No live deployment located; the audited repo and docs are the only identities found. |
| 1440 | Transfer | 1 | 0/1 | Non-EVM (XRPL) protocol-level review; no address to trace. |
| 1441 | Treasures | 1 | 0/1 | Project identity uncertain; no address. |
| 1442 | Tribe Turbo contest | 1 | 0/1 | Code4rena 2022-02 Tribe Turbo. No live deployment located; the audited repo is the only identity. |
| 1443 | TrustSwap - LockToken - Update | 1 | 0/1 | Audit is of LockToken.sol (collectUniswapV3LPFees). No TrustSwap LockToken deployment address surfaced; only the TRUSTSWAP token appears on Ethereum Blockscout. |
| 1444 | Umee | 1 | 0/1 | Cosmos module; no contract address applies. |
| 1445 | Uncuts | 1 | 0/1 | Duplicate of the Uncuts unit; no address. |
| 1446 | Uniswap Hooks Library Milestone 1 | 1 | 0/1 | Library audit, not a deployed protocol; no address to trace. |
| 1447 | Unstoppable | 1 | 0/1 | No report_url in the corpus entry; identity from the Sherlock contest repo. |
| 1448 | Upshift Solana ERC4626 | 1 | 0/1 | OtterSec review of the Solana ERC4626 vault program; audit text names no program ID. |
| 1449 | VTVL | 1 | 0/1 | No chain/deployment identifiable; VTVL token-vesting product appears not to have a public address book. |
| 1450 | Valantis Overseer | 1 | 0/1 | Valantis deploys on Hyperliquid EVM, whose explorer API was not reachable; no Overseer contract is verified on Ethereum (the 'Overseer' hits there are unrelated tokens). |
| 1451 | Valorem Options | 1 | 0/1 | Valorem options is deployed on Arbitrum per DefiLlama; the settlement engine address was not retrievable. |
| 1452 | Vanir | 1 | 0/1 | Guardian Audits Feb-2025 review of Vanir's liquidation logic. No deployment address appears in the report and no project site, docs page or explorer entry could be attributed, so nothing is recorded. |
| 1453 | Vaultka | 1 | 0/1 | Audit is a Solana-program review; the Arbitrum vault deployment does not contain the audited code path. |
| 1454 | Venom Bridge | 1 | 0/1 | Chain set from DefiLlama (Venom, Ethereum, BSC, Polygon, Avalanche, Fantom). No address book found in docs. |
| 1455 | Vortex - September 02 2021 | 1 | 0/1 | Solidified 2021-09-02 Vortex staking review. Project identity not resolvable from the record. |
| 1456 | Watches | 1 | 0/1 | OSEC report 'Double Claiming Of USDC Funds'; no project identity or deployment surfaced from the batch metadata. |
| 1457 | Windranger | 1 | 0/1 | BlockSec review v1.2 (2022) of Windranger. No address in the report text and no public deployment surfaced. |
| 1458 | Wonderland Prophet | 1 | 0/1 | Report covers a NoResolution dispute pledge flow, but no chain, repo or deployment page was available in the timebox. |
| 1459 | Worm | 1 | 0/1 | Hashlock audit (2025-11) of Worm; no chain or contract could be tied to the project within the timebox. |
| 1460 | XRPL Permission Delegation | 1 | 0/1 | Cantina review of an XRPL protocol amendment (RIPP-11). Ledger-native feature, so address tracing does not apply; recorded as NOT_FOUND by design. |
| 1461 | YearnstYFI-YBC | 1 | 0/1 | Yearn stYFI vote-bucket controller (YBC). |
| 1462 | Yiedl Drift Delegator Bot | 1 | 0/1 | Non-EVM (Solana). No address. |
| 1463 | Yield Protocol | 1 | 0/1 | Yield Protocol v2 ran on Ethereum and Arbitrum; the protocol has wound down and its deployment docs are no longer reachable. |
| 1464 | Yield micro contest #1 | 1 | 0/1 | Code4rena 2021-08 Yield (micro contest). Protocol is wound down; no address in the record. |
| 1465 | Yieldly.Finance Polygon NFT Marketplace | 1 | 0/1 | Yieldly's Polygon NFT marketplace contracts are not published and Polygon explorer search by name is unavailable without a key. |
| 1466 | ZK Prover | 1 | 0/1 | Least Authority audit of a proving library (Tools for Humanity / World). No deployment address exists to trace. |
| 1467 | Zama Confidential Vesting Wallet and Voting | 1 | 0/1 | EVM/fhEVM template code; the audit is of a template repository, not a live deployment. |
| 1468 | Zap Protocol | 1 | 0/1 | Sherlock 2024 review; no project site, docs or deployment could be attributed (the name collides with several unrelated 'Zap' products). |
| 1469 | Zap Protocol | 1 | 0/1 | Only the contract name (Vesting.sol) is known; project identity and chain could not be resolved. |
| 1470 | Zap Seasons | 1 | 0/1 | Guardian Audits Zap Seasons (2024-12) has no deployment information; no Zap contracts were discoverable on Ethereum explorers. |
| 1471 | Zap node sale | 1 | 0/1 | Guardian Audits review (Oct 2024) of the Zap node sale and ZapRewards; no public deployment address surfaced. |
| 1472 | Zeitgeist Combinatorial Betting | 1 | 0/1 | Zeitgeist is a Substrate parachain on Polkadot; the audited combinatorial-betting code is a Rust pallet with no EVM contract address. |
| 1473 | Zendoo Proof Verifier Cryptography | 1 | 0/1 | Zendoo is Horizen's Rust proof-verification library for sidechain certificates; batch_verify_proofs is library code with no EVM contract deployment. |
| 1474 | Zora | 1 | 0/1 | Finding body was not present in the corpus (empty body_path); title/entry-point only. |
| 1475 | ZyfiPermissionless multi signer paymaster | 1 | 0/1 | Zyfi's docs list ERC20 and sponsored paymasters on zkSync Era but no addresses. zkSync Blockscout search for 'Zyfi' returns only a memecoin ('Zyfi Explorer', 0x25d6b0c1...), not a paymaster. |
| 1476 | abranft | 1 | 0/1 | Code4rena 2022-04 AbraNFT repo documents only Ropsten testnet deployments (BentoBox 0x9a56..., NFTPair master 0x3a34...) and says one NFTPair is a BentoBox master contract cloned per lending market, so there is no single |
| 1477 | acala | 1 | 0/1 | Code4rena review (Mar 2024) of the Acala Substrate runtime. Deployment is the Acala parachain runtime, addressed by chain rather than a contract address. |
| 1478 | adil chain 2025 10 adil chain smart contract | 1 | 0/1 | AdilChain is a hybrid PoS EVM L1. The Hashlock audit PDF has no addresses and the explorer exposes no verified Exchange contract, so no deployment could be traced. |
| 1479 | afiVault | 1 | 0/1 | Quantstamp AFI Vault report; corpus entry has no report URL, body, website or repo, and the certificate page is JS-only with no address in the served HTML. |
| 1480 | alphahomorav2 alpha | 1 | 0/1 | Alpha Homora V2 is leveraged farming on Ethereum plus Fantom/BSC/Avalanche/Optimism (DefiLlama). The audited Jan-2021 'alpha' deployment is not published in the repo (AlphaFinanceLab/alpha-homora-v2-contract ships deploy |
| 1481 | alphahomorav2-alpha | 1 | 0/1 | Alpha Homora V2; version-to-deployment mapping unresolved. |
| 1482 | altr b6241933 | 1 | 0/1 | Quantstamp review of Altr Lending (Oct 2023). The audited code matches lucidao-developer/altr-lending-smart-contracts (Lending.sol, IPriceIndex.sol), but the repo publishes no deployment and no chain; the separate Altr M |
| 1483 | atoshi atoshi chain 20260710 | 1 | 0/1 | BlockSec 2026 review of the Atoshi chain (infrastructure). The finding lives in the chain's Go x/tokenomics module, so there is no contract address to trace. |
| 1484 | aurora labs limited | 1 | 0/1 | Hacken audit of the Aurora staking/rewards contract (Jun 2022). Neither the report page nor Aurora's docs expose a deployment address, so the contract could not be traced. Aurora is NEAR's EVM chain, but no verified chai |
| 1485 | autofarm | 1 | 0/1 | Autofarm runs many per-vault strategies; without a named strategy or a keyed BSC explorer, no single address is defensible. |
| 1486 | balloon 2025 09 balloon depositvault smart contract | 1 | 0/1 | Hashlock's 2nd Balloon audit report (2025-09) records Network: ETHEREUM and project BalloonTech (balloontech.ai), scope DepositVault.sol/deposit/withdraw/redeem. The report contains no 0x address; balloontech.ai, app.bal |
| 1487 | belong net | 1 | 0/1 | December-2022 SCA review of Belong's ERC721 (belong.net, event/hospitality NFT platform). The live site and docs publish no contract-address list, and earlier batches (ST2-081, ST2-094) also found no deployment; nothing  |
| 1488 | black tie | 1 | 0/1 | Black Tie Asset Hub appears to be a permissioned RWA platform; the Hashlock report (Apr 2025) names UserManager/AuthorityManager/Token but no addresses. Same protocol as project 26. |
| 1489 | coded estate | 1 | 0/1 | No chain was confirmable from the report metadata (chains: unknown), so no address is claimed. |
| 1490 | cyan-5ef87add | 1 | 0/1 | CyanPrivateSales deployment not located. |
| 1491 | defi app security audit competition | 1 | 0/1 | Unit carries no report URL and no chain. defi.app is an all-in-one SuperApp; no deployed claim/Merkle distributor address is published on its site, so nothing is asserted. |
| 1492 | dopex-v2-automator | 1 | 0/1 | Electisec's 2023 review of the Dopex V2 automator. docs.dopex.io no longer serves documentation and the automator's address is not in the report extract; no deployment located. |
| 1493 | ethereum evm bacon labs | 1 | 0/1 | One search and a GitHub repo scan found only Bacon-labs/website (no addresses). No address recorded rather than guessing. |
| 1494 | ethereum evm primitive securityreview | 1 | 0/1 | The audit target is EVM primitive behaviour; there is no project deployment. No address was invented. |
| 1495 | final-apebond-collaborative-audit-report-1751030104 | 1 | 0/1 | Solana collaborative audit of a pre-launch program; no on-chain program ID surfaced in the report or the Sherlock repo snapshot. Deliberately not mapped to ApeBond's EVM deployments. |
| 1496 | final-sentiment-audit-report | 1 | 0/1 | Sentiment is an Arbitrum lending protocol; per-asset LToken addresses were not resolvable within budget. |
| 1497 | final-smilee-finance-audit-report | 1 | 0/1 | Smilee deploys on Arbitrum and Berachain; neither explorer API was reachable and no FinanceIGDelta/Smilee vault is verified on Ethereum, Optimism, Unichain or Scroll. |
| 1498 | firestarter firestarter | 1 | 0/1 | Firestarter IDO platform (Oct-2021 review). Ethereum Blockscout search returns only unrelated FireStarter-branded memecoins; no Presale/Whitelist deployment is attributable. |
| 1499 | for Train Protocol | 1 | 0/1 | No address. |
| 1500 | for Zealous Swap | 1 | 0/1 | Kaspa-based DEX; no EVM contract address applies and no on-chain pool address was published. |
| 1501 | franklintempleton-benjicontracts-securityreview | 1 | 0/1 | Trail of Bits 2025-02 review of Franklin Templeton Benji contracts; report text withheld and the tokenized-MMF deployment is permissioned. No public contract address surfaced. |
| 1502 | hashlock-00bleck-2025-10-00bleck-smart-contract-audit-report | 1 | 0/1 | Contract name implies Berachain (ERC-6551 account), but no chain/address evidence was obtained, so both are left null. |
| 1503 | hashlock-aqualis-2024-12-aqualis-code-review-smart-contract | 1 | 0/1 | Hashlock Aqualis review (Dec 2024). Aqualis is listed on DappBay for BNB Chain; the only token surfaced (AQL on Ethereum) is not the audited SavingsPool contract. |
| 1504 | hashlock-aqualis-2024-12-aqualis-code-review-smart-contract-audit-repo | 1 | 0/1 | Hashlock Dec-2024 review of Aqualis' stablecoin vault (AqualisSP). The project has no discoverable site/docs and no explorer entry for AqualisSP; only unrelated AQLS memecoins exist on Ethereum, so nothing is recorded. |
| 1505 | hashlock-black-tie-2025-03-black-tie-asset-hub-smart-contract-audit-re | 1 | 0/1 | Duplicate protocol of project 'black tie'. Hashlock report is public but contains no contract addresses. |
| 1506 | hashlock-db-cherry-2025-05-db-cherry-smart-contract-audit-report | 1 | 0/1 | Hashlock May-2025 review of DB Cherry's SmartWallet (ERC-4337 validateUserOp). The batch record carries no report URL, chain or address, and no DB Cherry deployment could be located in this pass. |
| 1507 | hashlock-dvx-2024-06-dvx-smart-contract-audit-repo | 1 | 0/1 | Hashlock audit (2024-06) of a 'DVX' perp/account codebase. The batch entry has no report URL or body, only the finding title, and no chain or deployment address is given. No DVX deployment matching Account.sol/adapters c |
| 1508 | hashlock-emergence-art-2025-10-emergence-art-smart-contract-audit-repo | 1 | 0/1 | Hashlock Oct-2025 audit of 'Emergence'; project identity could not be resolved to a live deployment. |
| 1509 | hashlock-imf-international-meme-fund-2024-06-imf-s | 1 | 0/1 | No verified PepeMoneyOracle, MemeFund or related IMF contract found on Ethereum; the report gives no repository or deployment address. |
| 1510 | hashlock-mortgagefi-2024-08-mortgagefi-smart-contract-audit-report | 1 | 0/1 | Hashlock 2024-08 review of MortgageFi. DefiLlama lists the protocol on Base and Arbitrum, but neither the report record nor the app bundle exposed a contract address. |
| 1511 | hashlock-pandapump-2025-01-pandapump-smart-contract-audit-report | 1 | 0/1 | Not to be confused with PandaSwap (BSC 0x47DcC83a...), a different project; that address was not used. |
| 1512 | hashlock-tenexium-2025-10-tenexium-smart-contract-audit-report | 1 | 0/1 | Hashlock review of Tenexium, a spot-margin protocol in the Bittensor ecosystem (subnet 67). The audit page and site name no deployment address and the chain is not confirmed, so nothing is recorded. |
| 1513 | iRocket | 1 | 0/1 | Identity unresolved; no deployment found. |
| 1514 | ibc-solidity | 1 | 0/1 | Library code (yui-ibc-solidity); no single deployment. |
| 1515 | iq ai | 1 | 0/1 | Code4rena January-2025 IQ AI contest (AgentFactory deploys Agent + AIToken + TokenGovernor + LiquidityManager per agent). The audit README states the deployment chain is Fraxtal, but no AgentFactory/TokenGovernor address |
| 1516 | irocket | 1 | 0/1 | Hacken/SCA ERC-721 audit dated 2022-08-02. The project appears to be a one-off NFT collection with no published deployment; no chain or address could be verified. |
| 1517 | joyn | 1 | 0/1 | Code4rena 2022-03 Joyn repository (core-contracts, royalty-vault, splits) contains no committed deployment output: core-contracts/scripts/deploy.js derives CoreCollection/CoreMembership/CoreFactory addresses at runtime a |
| 1518 | kingdomly 2025 01 kingdomly 3rd smart contract audit report | 1 | 0/1 | Kingdomly is an NFT marketplace/launchpad supporting many chains (docs list Ethereum, Arbitrum, Berachain, Base, HyperEVM, Sophon, Mitosis); the audited KingdomlyStaking address is not published and the staking front end |
| 1519 | liquid-bitcoin-lombard-finance | 1 | 0/1 | The Ackee review targets Lombard's Solana program (the finding names initialize on lbtc_config). The Solana program id is not published in the report or in the docs reached. The Ethereum LBTC ERC20 and the BARD token are |
| 1520 | liskv4.0-securityreview | 1 | 0/1 | The review covers the Lisk v4.0 SDK (message recovery module), i.e. client/framework code, not a deployed contract. Lisk later relaunched as an OP-Stack L2; no address corresponds to the audited module. |
| 1521 | lorenzo otf contract | 1 | 0/1 | Report identified (Cantina, Lorenzo OTF contract) but no deployment address in report, repo tree, or DefiLlama listings. |
| 1522 | malt | 1 | 0/1 | Malt has no published deployment address; prior Stage 2 batch ST2-079 also recorded NOT_FOUND. |
| 1523 | meta soccer | 1 | 0/1 | Identity is a 2021-12 SCA review of a Meta Soccer NFT voucher sale. One search plus BSC/Ethereum explorer names produced no attributable contract. |
| 1524 | multichain-account | 1 | 0/1 | NEAR/Rhea multichain account. Contract account not located. |
| 1525 | mute | 1 | 0/1 | Chain is zkSync Era (324) from the project's history; Mute.io has wound down. No MuteBond address is published anywhere reachable, so the finding stays unmapped. |
| 1526 | nearx | 1 | 0/1 | BlockSec 2022 review of NearX (Rust, NEAR liquid staking, v3.0). NEAR contracts live at named accounts (foo.near) and no account name is published in the report extract; no name was guessed. |
| 1527 | nft security review sheepcoin protocol audit | 1 | 0/1 | NFT Security Review February-2025 of Sheepcoin's SheepDog contract. A BSC contract at 0xA182c1E29aB35947387E1eCFEAA7f939B36b88DF answers name()='SheepDog' and symbol()='SHEEP', but Sourcify verifies its source as HolyTri |
| 1528 | odx contracts | 1 | 0/1 | Cantina Managed review of odx-contracts at commit e3f2850b (Apr-May 2025). Report PDF: https://cdn.cantina.xyz/reports/cantina_odx_april2025.pdf. No public chain or contract address is disclosed. |
| 1529 | openzeppelin uniswap hooks v1 1 0 rc 1 audit | 1 | 0/1 | OpenZeppelin 'Uniswap Hooks v1.1.0-rc.1' audit (2025-07-16). The scope is the OpenZeppelin/uniswap-hooks Solidity library (src/general/LiquidityPenaltyHook.sol), distributed as a package; there is no first-party deployed |
| 1530 | pandapump 2025 01 pandapump smart contract | 1 | 0/1 | Nothing surfaced; likely a small/defunct BSC-style launchpad. |
| 1531 | particle 3cd57a7b | 1 | 0/1 | Could not identify which 'Particle' project the review covers (Particle Network, Charged Particles and others share the name). No address recorded. |
| 1532 | pashov-solo-2023-11-17-bearcave-second-security-review | 1 | 0/1 | Metadata-only finding (body withheld). No address evidence available. |
| 1533 | pashov-solo-2023-11-17-mugen-security-review | 1 | 0/1 | Pashov solo review of 'Mugen'; ArbitrumSwaps has no verified deployment and the project identity is not resolvable from the batch metadata. |
| 1534 | pashov-solo-2023-11-17-ninjayielder-security-review | 1 | 0/1 | Review repo hash links to 0xTK421/ninja-core-contracts, which is no longer public (404 this pass), and the review was pre-deployment; no chain or address appears in the report. |
| 1535 | pashov-team-2024-03-29-forgottenplayland-security-review | 1 | 0/1 | Forgotten Playland (Beam) ToyBox sale; no contract address found. |
| 1536 | pashov-team-2024-12-14-buyburner-security-review | 1 | 0/1 | Pashov Dec-2024 review; the batch carries no report URL or body. Name-similar BuyBurn token on Ethereum left as an unconfirmed lead rather than a traced address. |
| 1537 | pashov-team-2024-12-19-stardusts-security-review | 1 | 0/1 | Bonding-curve review with no report URL in the batch and no identifiable 'Stardust' deployment; nothing to trace. |
| 1538 | pashov-team-2025-02-05-coinflip-security-review | 1 | 0/1 | No chain or deployment identifier recoverable from the report; left NOT_FOUND rather than guessing from explorer name collisions. |
| 1539 | pashov-team-2025-04-25-ripit-security-review | 1 | 0/1 | Pashov 2025 review of RipIt. No report URL, body or deployed address in the batch, and no RipIt deployment could be tied to the finding. Nothing recorded. |
| 1540 | pashov-team-2025-05-24-itos-security-review | 1 | 0/1 | Scope repo itos-finance/ItosCommons is a Solidity utilities library with no deployment/address files; no chain or address published. |
| 1541 | pashov-team-2025-08-27-funnel-security-review | 1 | 0/1 | Pashov Aug-2025 review; the SwapX router referenced is Sonic-native, so the chain is inferred as Sonic. No report URL, body or deployment address in the batch and no Funnel contract surfaced. Nothing recorded. |
| 1542 | powerloom l2 695c4ca5 | 1 | 0/1 | Quantstamp 'Powerloom L2' review (certificate 695c4ca5) covers hardhat/contracts/SnapshotterState.sol on the project's own 'Prost Chain'. The docs state the protocol-state contract lives on that EVM chain and deliberatel |
| 1543 | propto 2025 03 propto penetration test | 1 | 0/1 | Hashlock 'Propto' penetration test (2025-03) reads as a Web2 application assessment: the finding is path traversal in a compliance/ route. No website, docs, repo, chain or contract address surfaced, so there is no deploy |
| 1544 | rush-trading-jan-25( ) 1002 | 1 | 0/1 | No address. |
| 1545 | shark race | 1 | 0/1 | Project appears defunct: no website/docs/GitHub surfaced and no live BEP20 market found for the audited token. |
| 1546 | sigmaprime dxdao erc20 guild | 1 | 0/1 | Identity from the Sigma Prime public-audits README (DXdao, ERC20Guild, report PDF) and dxdocs. The audited artifact is the ERC20Guild implementation repo, not a named live deployment; Etherscan/Blockscout name searches f |
| 1547 | sigmaprime-bullet-review | 1 | 0/1 | No chain or address identified for Bullet. |
| 1548 | sigmaprime-omni-network-sigma-prime-omni-solvernet-security-assessment | 1 | 0/1 | Omni Network (now Nomina) SolverNet review. The inbox is deployed per chain via script; no address table was found, so no address was asserted. |
| 1549 | sigmaprime-satori-sports-satori-sports-token-royalties-review | 1 | 0/1 | No reliable identity resolution within the timebox; skipped rather than guess at a Satori-branded token on an unrelated chain. |
| 1550 | smart-contract-audit-for-clave-wallet | 1 | 0/1 | Clave is on zkSync Era and each account is a per-user proxy; the zkSync Blockscout search returned only ClaveNameService tokens and no ClaveAccount/Proxy/Factory implementation under the audited name. |
| 1551 | solo 2023 11 17 ninjayielder | 1 | 0/1 | Pashov solo review 2023-11-17 of NinjaYielder; the referenced repo 0xTK421/ninja-core-contracts (commit 9e9367120d45fdd6144328964fabb8f57610661c) now returns 404 and the account lists no ninja repository, so neither the  |
| 1552 | spline audit | 1 | 0/1 | Unresolvable identity; nothing to map. |
| 1553 | spool-arbitrum- -april | 1 | 0/1 | Spool's docs domain (docs.spool.fi) no longer resolves; the Arbitrum explorer is Cloudflare-blocked from this environment; Ethereum Blockscout search returns only SPOOL/Spool Finance tokens and SpoolDao, no controller or |
| 1554 | sprinter remote collateral contracts | 1 | 0/1 | Only identity could be confirmed: sprinter.tech (onchain credit engine, $400M+ issued claim) and DefiLlama chain = Base. The 2026-03 audit report and its contract scope are not published where reachable; recorded NOT_FOU |
| 1555 | stablezone | 1 | 0/1 | SCA November-2022 review of 'WT Worldwide Tech ERC20 vesting/staking'. No report URL, website, repository or explorer match surfaced for StableZone/WT Worldwide Tech, so neither chain nor address could be established. |
| 1556 | stoneii 2026 03 stoneii updates smart contract | 1 | 0/1 | Hashlock March-2026 review of a StoneII update (PrivateEquityToken dividend accounting). The unit has no report URL or contract address; Hashlock's audit index has no reachable StoneII page with deployment data, and no s |
| 1557 | sythentix-kwenta-snx-conversion | 1 | 0/1 | Only the KWENTA token (Optimism 0x920Cf626a271321C151D027030D5d08aF699456b) surfaced, which is not the conversion contract. |
| 1558 | team 2024 10 03 apdao | 1 | 0/1 | apDAO / Apiology DAO (Pashov, 2024-10-03). Report references ApiologyDAOAuctionHouse, Treasury and StationX factory; the scope repo is gone and no apDAO/Apiology contracts were found on Ethereum, Optimism or Base explore |
| 1559 | team 2024 11 29 nexus | 1 | 0/1 | Nexus (Pashov, 2024-11-29) - 'NativeYield' cross-chain yield vault, Berachain deployment inferred from report (BERA gas token). Repo deleted; Berachain explorer not machine-searchable within budget, so no address. |
| 1560 | team 2025 01 18 gigaverse | 1 | 0/1 | Docs (docs.gigaverse.io/llms.txt) state the game is live on Abstract (chain 2741) and the Links & Contracts page gives only a contract discovery endpoint, https://gigaverse.io/api/contracts, which now returns HTTP 410 'T |
| 1561 | team 2025 01 25 omo | 1 | 0/1 | Pashov Omo review (2025-01-25) scopes AgentSetter, OmoRouter, OmoVault, OmoVaultFactory, OmoOracle, DynamicAccount, DynamicAccountFactory and OmoAgent, and mentions 'hyper EVM' in the EntryPoint finding. The audited repo |
| 1562 | team 2025 01 27 gacha | 1 | 0/1 | Audit report read; no deployment information in it, repo unavailable. |
| 1563 | team 2025 02 05 coinflip | 1 | 0/1 | Coinflip (Pashov, 2025-02-05). Scope covers Flip game, Staking and PythRandomnessProvider contracts; repo is gone and no Coinflip/Flip game deployment of this project was identifiable on the explorers checked. |
| 1564 | teneo 2024 06 teneo smart contract audit | 1 | 0/1 | Hashlock report name only; no repo/address book. Teneo ProtocolAI org has SDK repos only. |
| 1565 | tengoku-senso-5361cc88 | 1 | 0/1 | EVM audit with no published deployment; explorer name matches (TENGOKU SPACE) were not verifiable and were rejected. |
| 1566 | tessera | 1 | 0/1 | Identity limited to the Code4rena '2022-12-tessera' contest (NFT marketplace, OptimisticListingSeaport + GroupBuy). No website/docs were reachable/verifiable, and the project appears to have wound down; no deployment add |
| 1567 | the next world | 1 | 0/1 | SCA May-2022 review of a GameFi project called 'the next world'. No website, docs, repo or explorer match surfaced; thenextworld.io is an unrelated technology-news site. Chain and deployment unknown, so nothing is record |
| 1568 | u2u 2024 10 amm contract 2 | 1 | 0/1 | Scope repo identified (unicornultrafoundation/u2u-marketplace-erc-contracts, launchpad/contracts/U2UPremintBase.sol), but no deployment address is published. |
| 1569 | u2u 2024 11 staking 4 | 1 | 0/1 | U2U Network (chain id 39, confirmed from the staking app bundle at staking.u2u.xyz). The audited IncentivePool is part of U2U's staking suite, but no address is published in the report, docs (docs.u2u.xyz / docs.uniultra |
| 1570 | unibot diamond protocol uni | 1 | 0/1 | Identity unresolved beyond the Quantstamp review name; the audited code appears private and no chain/deployment could be evidenced. |
| 1571 | verwa | 1 | 0/1 | veRWA is a Canto (chain id 7700) ve-tokenomics PoC. Chain evidenced by the Code4rena README award note; no address recorded because none could be verified. |
| 1572 | vynksafe-sca-vynksafe-bep20-staking-may2022-sca-vynksafe-bep20-staking | 1 | 0/1 | Small BSC staking project; no deployment reference in the report text available. |
| 1573 | yAcademy Yearn BalancerLpFactory | 1 | 0/1 | Fellowship/educational review of a prototype; no live deployment identified. |
| 1574 | yAcademy joint strategy | 1 | 0/1 | SolidexJoint (Fantom) address not located. |
| 1575 | zaros part 1 | 1 | 0/1 | CodeHawks/Cyfrin 2024-07 Zaros Part 1 review; audited contracts were deployed on Arbitrum but no address is published in the audit repo or report extract. |
| 1576 | zkBob | 1 | 0/1 | zkBob pools run on Polygon and Optimism; the audited liquidation bot is an operator-side contract with no published address. |
| 1577 | zkMakers | 1 | 0/1 | Repo identity confirmed, but deployment environment is only Ropsten test migrations; audit scope is an ERC20 staking contract that is not in the public repo tree. No chain or address can be substantiated. |

## 4. Profit refuted — DoS / griefing only

These were Stage 1 profit-plausible but the Stage 2 read found no attacker gain. They are recorded so they are not re-chased as drains.

| Finding UID | Project | Title | Reason |
|---|---|---|---|
| `2022-07-juicebox::2022-07-juicebox_H-02` | Juicebox | Token Change Can Be Frontrun, Blocking Token | The finding describes front-running a token change to block it (griefing/DoS); no attacker payout is described. |
| `2024-12-06-prospective-world-sca-prospective-world-pros-venture-m-nft-oct2024-sca-prospective-world-pros-venture-m-nft-oct2024::problematic-triple-loop-in-nft-minting-process` | prospective world | Problematic Triple Loop in NFT Minting Process | The triple nested loop is a gas/iteration cost in the mint path; the text describes a minting liveness problem, not a way for the caller to extract funds. |
| `2024-06-vultisig::2024-06-vultisig_H-01` | vultisig | Most users won’t be able to claim their share of Uniswap fees | Users cannot claim their fee share and the value is stranded in the pool; the text describes a claim denial with no attacker payout. |
| `finding:976251d1636a465b80cf854a901ab723b8afa1467636955d53739b84152997f4` | Astaria | AstariaRouter.liquidate(...) can be called multiple times for an expired lien/stack | Repeated liquidate() calls overwrite auction parameters and can keep stacking auctions (never-ending liquidation), a griefing/DoS path; the report shows no atta |
| `finding:7750b6af33ba114e755f8abb625985e230322a2f56059ff5c13db8a2e2feeb6f` | Astaria | Lack of access control in PublicVault.sol#transferWithdrawReserve let user call trans- ferWithdrawRe | Repeated transferWithdrawReserve calls only decrement the in-memory withdrawReserve when the withdraw proxy is unset, blocking/locking withdrawals; no attacker  |
| `finding:742c4d18769b128e523b73046864eb0cc656836c02ad1464b220c835a2202d85` | Sushi Trident contest phase 1 | Flash swap call back prior to transferring tokens in `indexPool` | The flash-swap callback runs before the token transfer, so the callback cannot receive the tokens and flashSwap is simply broken; no attacker gain. |
| `finding:5224f52c851ced0d7b74b5e7722b209f4e5628e1d9464c7b49f6936b19ade569` | Usual Money | Incorrect accounting of accumulatedReward after transfer | The recipient accumulatedReward is increased by the pre-tax amount, so the recipient loses rewards; the bug harms users and gives no attacker gain. |
| `finding:0fca7d1392bd0de7bdfe38a86f3a69b264b5d6162e85a5064790407c491b5f62` | GMX Crosschain V2.2 1 | Incorrect Message Decoding Leads | The Stargate compose message is decoded in the wrong format, so lzCompose fails and the user loses the already-delivered funds; no attacker gain. |
| `finding:cd8f5a1033775c99045034abdf422432c1f4240bb967b90a871b776ea2824170` | Olympus | Adversary can stake LP directly for the vault then withdraw to break lp accounting in BLVaultManager | Duplicate of the LP-accounting break: users are trapped, attacker gains nothing. |
| `finding:7fea4cf0d6986e165c6e5d7bedbd1d766382ad92d9618e36c264ced6bdd619b5` | Olympus | Adversary can stake LP directly for the vault then withdraw to break lp accounting in BLVaultManager | Staking LP directly for a vault breaks LP accounting and traps other users' withdrawals - griefing/DoS, no attacker payout. |
| `finding:e87f83278f99201a529517cd01eb40a1ba0cdeaca7bf0aea6b12e4727b8b59ab` | Teller | CollateralManager#commitCollateral can be called by anyone | Anyone can commit a malicious token to any bid - griefing of bids, no value moves to the attacker. |
| `finding:f60baebc6f4b15e07a2643b5803eff3afafce5dd112ef676b033fdddf8cf122b` | Tokemak | Incorrect number of shares minted as fee | fee shares are mis-minted to the protocol fee sink; the stated impact is loss of fee, with no external attacker gain |
| `finding:6c6f03e69f75b9df3a10410e92d42d2c485e29995b1fcfcc1c3aa234b43a44ea` | USSD - Autonomous Secure Dollar | `USSDRebalancer.sol#SellUSSDBuyCollateral` the check of whether collateral is DAI is wrong | the bad DAI check makes SellUSSDBuyCollateral revert; the impact is a rebalancer DoS, not attacker gain |
| `finding:70764f82e1e185dab3b97bad2749b1c8a3423a781f393616226151bf0e089c75` | Chakra | Malicious actors can manipulate the `cross_chain_callback` callback | missing from_chain in the signed message lets an attacker force the tx into Failed; griefing/DoS with no attacker gain |
| `finding:00b1f4fa305d273c8b12f9aa9b98046d8b6e6db46fe9b7d62319e8766e0ce6df` | Chakra | Handler's `receive_cross_chain_callback()` will always set the `tx_status` to `SETTLED` on source ch | source chain burns tokens and marks SETTLED even when the destination failed; value is destroyed, not captured |
| `finding:173b8ef03879a9b8856a9dcd69045f35142640cae72019fd4fe6706e8582377e` | Etherspot Credible Account Module | Missing Session Key Uniqueness Validation in `ResourceLock` due to Key Data Overwrite | reused session keys overwrite sessionData and orphan lockedTokens; the stated impact is accounting corruption/DoS |
| `finding:0d938f2e0380319c9302a8596b66de97a3264827eb17984f099852706e44d73c` | Fastlane Atlas | Borrow()s after validateBalances() | borrow() remains callable after validateBalances, so the solver is griefed with a bill it cannot control; no attacker gain |
| `finding:31ab8df81aaaaa02640db9160ca43db8b7c7ed322500a62810e3a337e9942240` | Fastlane Atlas | userOp validation is skipped in simulation mode for smart contract user accounts | userOp validation is skipped only in simulation mode, which has no on-chain effect |
| `finding:bfc6d21c8f65544d36de9780edc9bac03143d1a92a0da7642c77fb9985470b7a` | Frankencoin | buyExpiredCollateral Can Disincentivize Challenging | buyExpiredCollateral removes the challenger's reward; the stated impact is a disincentive to challenge, not attacker gain |
| `finding:285b0c86f33f13943275924325a80adc4877b9104724709147134cf41c82b1b7` | NearOinDao | inject_reward lacks access control | inject_reward only adds balance to the reward pool; it is a donation/griefing primitive with no attacker gain |
| `finding:d80d4acca15655a70ad37896c85ee3fd7a1d9e9656ab97a6aa2fe9beb68bac61` | NearOinDao | inject_sp_reward lacks access control | inject_sp_reward only increases the recorded stable-pool reward; no value is captured by the caller |
| `finding:5f425cc15e27fc31b0c8cee580be4435eb2d65f1a74a39335b6a74d010d8d462` | Poolshark Cover | amountOutDeltaMax Double Counted In Section2 | amountOutDeltaMax is removed twice, perturbing accounting and locking the position; the stated impact is a lock, not a payout |
| `finding:26b9a32c321ccf53121fcae8671bd9028814e50d65cff27828483bd20e526ed2` | Symbiotic RelayContracts AI | State Inconsistency from Unauthenticated Key Setters | Only corrupts key metadata and lookups; griefing/DoS of the key registry with no attacker value gain. |
| `finding:d3fc2f50faf8ac2c37c9fc41f2ff5d10815d2548a87c44bf56100aeb2a021abd` | Tigris Trade contest | Incorrect calculation of new price while adding position | The wrong addToPosition price makes the user lose part of their funds/profit; no attacker gain. |
| `finding:6d82ca5c7419fc5d1d8ec2bf1e5f1e074393700c971b2ee88f331d213b1b54a4` | v2 Contracts | Uninitialised AccessControl In TermDiamond | Missing AccessControl init breaks role checks and causes functionality failures (DoS); no attacker value path is described. |
| `finding:57d2faf9fb23726a8b940e2cc8795c63990d559da1e878197c0d28c38c32c632` | Goat Tech | Malicious poolowner can withdraw earnings without affecting trust score | Attack only lets a pool owner withdraw their own earnings via a second 99%-owner pool; the gain is their own funds and a cosmetic trust score, not external valu |
| `finding:cf28af4763177df8bac60f434c93924e3b712bf7a4d8de7b773405f286099bbd` | INIT Capital Invitational | Liquidations can be prevented by frontrunning and liquidating 1 debt (or more) due to wrong assumpti | Front-running a liquidation with a 1-wei self-liquidation makes the later liquidation revert; impact is blocked liquidation, no attacker value. |
| `finding:74f0dc6740b0018ccf03c610d33b04fe66395ff9497ff97ac372c8717807141a` | InsureDAO contest | backdoor in `withdrawRedundant` | withdrawRedundant is onlyOwner; the 'backdoor' is an admin rug vector, not an unprivileged profit path. |
| `finding:394890d7d7a7df636311f1bd44a2fadb1adbea54c224832de6a3ecb94e7d10cd` | SingularityAudit | In StakingAssetManager::lockERC20() the resulting note is created with asset instead of zkToken | lockERC20 builds the note with asset instead of zkToken; the note cannot be unlocked, so funds are locked rather than stolen. |
| `finding:32fb0e5d6ca3687efe41ebbdc2b737e91cf52779d0c3048a8cf98d2c215f3b8c` | YIELD | auth collision possible | Auth is keyed on 4-byte selectors; exploiting a collision requires a malicious module to be approved through governance. |
| `finding:2693f89d8a1bfe04fcc5216df830a36681ec1126e03e4f8fd5d3d654da133ec5` | 02 12 Whetstone Doppler-MR | In UniswapV2Migrator.migrate(): misconfiguration of recipient to msg.sender in addLiquidityETH call | The liquidity recipient is the Airlock (msg.sender) instead of the token timelock, so value is locked in Airlock rather than captured by an external actor. |
| `finding:7ad442e26ec6fbc84ec8626d72b819872262098428d0eda42accd5da138380a3` | 02 12 Whetstone Doppler-MR | Anyone can call beforeInitialize() directly | An arbitrary poolKey breaks the migration flow and leaves funds stuck; the report describes a lock/DoS, not an attacker payout. |
| `finding:e4bb76df27b52e9d0a1b055e6a538613239761ac4e48e0ed75154d885f6a548b` | 2024-07-loopfi | `decreaseLever` uses incorrect position address when withdrawing | decreaseLever always reverts for Position4626 vaults because it withdraws from the wrong position address; the impact is a DoS with no value transfer. |
| `finding:c32c68fef99edc5d4da398b04edc2c6430958dbb1fa0f7ec4356e9339e5e9e3b` | Instadapp Fluid | Incorrect work of UniV3CheckFallbackCLRSOracle in the first mode | In the first mode the function never returns the computed rate and always reverts on the delta check, a denial of service rather than a value path. |
| `finding:846ec5311a03ef20f0743062aa1ec1d165f5e05bfed86b47e6a31bc36902f2a1` | MYX Finance | Incorrect getPriceNoOlderThan age | getPriceNoOlderThan with age 0 makes the Pyth read revert on L2, a denial of service rather than an attacker gain. |
| `finding:b2a7441bbcc4d624f79cbdebc0308118116bac9cfbc57860466b141b882ae327` | Biconomy Hyphen 2.0 contest | `LiquidityProviders.sol` The share price of the LP can be manipulated and making future liquidityPro | Title and body describe LP share-price manipulation that blocks later LPs from removeLiquidity - griefing/DoS with no attacker payout stated. |
| `finding:33efb198ba5c727ab942d4ac1e8138b1e712be4065f383f71d50599a0b3d1728` | Ink Protocol | Slashes or other reduction of assets in the Anchor strategy could block drawing a winner while causi | Clear DoS/griefing: a shortfall blocks drawing a winner and triggers a bank run; no attacker gain is described. |
| `finding:ca6cdecf7635ef3e3e892be31fe8e5eabb96567f5e85630d432eefb76e5ed3c2` | Connext NXTP — Noncustodial Xchain Transfer Protoc | Router - spawns unauthenticated admin API endpoint listening on all interfaces | Unauthenticated admin API on the router is an operational/DoS exposure with no direct attacker gain. |
| `finding:36c7a108189c3d33ecf7660443ed5b8033ce4588209f4a34a08ec963a82c255c` | Monerium (Wake Arena AI review) | sellGem allows no-op when caller equals recipient (msg.sender == usr) High impact finding | sellGem becomes a no-op when caller==recipient: no token movement, only a false Swapped event - no attacker gain, so not profit. |
| `finding:7a9d178dd45e3df4157f9c876948c21e5a69a47e01b06d55f2cbe1ef4c9db153` | Karak | Code should use state root to validate withdraw credentials | Report states the effect is that no validator can be added to the system: a functional/DoS break with no attacker gain path. |
| `finding:10c7f4acc753d13a4ee7df1e63b2e8639657ebc57e46b38595b2fc2151f79e8e` | Ellipsis Labs | SDK Transaction Spoofing | Body states the impact is a denial-of-service condition for SDK users caused by parsing failed transactions' logs; no attacker payout. |
| `finding:e52b7d69c5f9dc62965ed6956f8b8be146d239d11f58a6b34db710ba408fd4c8` | Sunnyside Labs PrivacyBoost | Tree Number Range Misconstraint Causes | The finding is 'Tree Number Range Misconstraint Causes Permanent Protocol Halt After 16 Rollovers' - a liveness failure with no attacker gain, so it is DoS not  |
| `finding:995fd9e1318d2e12e9e56618ee12732cd64430294e7bae4a8abf37d0849e420e` | Credit Swap Dec22 ed16f43d95 | Attacker Can Grief Liquidations And Repayments | Anyone can front-run liquidate()/repay() with a 1-wei debt-token transfer so the vault balance no longer equals debtAmount and the call reverts. The attacker ga |
| `finding:c35314f0dcc09622ed4d1f0a3f62d07563de7866c18bb0403af17170c2df7bfb` | Public - IStep Token | Invalid unlocked balance check in transferFrom | The strict '>' check blocks transferring the last unlocked token, i.e. a user-facing restriction/DoS with no attacker gain (report text confirms). |

## 5. Earlier campaign findings (already traced)

The pre-Stage-1 campaign produced the following live/dust and gated addresses. They are repeated here, verbatim from `research/EXTRACTABLE_VALUE_MASTER.md`, so this file is the single Stage 2 hand-off. Values are point-in-time and were measured before this pass; re-read the chain before relying on them. Full dossiers and per-finding evidence: `research/EXTRACTABLE_VALUE_MASTER.md` §2–§3.

### 5.1 Master ranking — net-positive findings

| # | Target | Chain | Bug / source | Who can take it | Gross | Net | Status | Confidence |
|---:|---|---|---|---|---:|---:|---|---|
| 1 | **StationX** | Linea | Pashov C-03 native-fee drain via local ERC721 buy | **fresh unprivileged EOA** | **$121.14** | **+$119.28** | **LIVE, confirmed twice** | High |
| 2 | **X7Finance X7Pioneer** | Ethereum | `claimRewards([])` re-counts ETH delta; NFT #300 only | holder of NFT #300 | $48.30 | **+$47.80** | HOLDER-GATED, live | High |
| 3 | **HeavensGate HATE** | Ethereum | Stale 2,197-epoch rebase backlog + 0.5% mint loop | **fresh unprivileged EOA** | $29.54 ceiling | **+$20.01** best tx | **LIVE** | High |
| 4 | **Gensyn Delphi DPM** | Gensyn 685689 | Terminal-marginal-price liquidation on FAILED/EXPIRED | fresh EOA **after** market fails/expires | $143.88 payout | **+$11.85** conditional | CONDITIONAL after 2027-01-02 | Medium |
| 5 | **INUKO Bond** | BSC | `LpToToken` balanceOf/reserves mismatch | fresh EOA **after** 10-year lock | $19.96 | +$8.55 | LOCKED 10 years | High |
| 6 | **OverNight USD+** | Avalanche | Permissionless `payout()` NAV rebase, capped premium | fresh unprivileged EOA | $7.49 | +$7.48 | BELOW_THRESHOLD, one-shot | High |
| 7 | **PegaBall** | Ethereum | `buyGamesFrom` pays vendor/referrer from proxy balance | fresh unprivileged EOA | $8.35 | +$5.92 | BELOW_THRESHOLD | High |
| 8 | **Renzo ezETH** | Ethereum | Secondary-market discount vs 14-day redemption | fresh EOA with capital | $24.66 spread | +$2.49 | ARBITRAGE, 14-day cooldown | Medium |
| 9 | **SinstakeZombie** | BSC | Unbacked dividend drip | fresh unprivileged EOA | $0.86 | +$0.81 | BELOW_THRESHOLD | High |
| 10 | **Dumbo** | BSC | Permissionless distributor epochs | fresh unprivileged EOA | $0.99 | +$0.79 | BELOW_THRESHOLD | High |
| 11 | **SCROLL** | Ethereum | Unchecked balance underflow | fresh unprivileged EOA | $0.59 | +$0.54 | BELOW_THRESHOLD | High |
| 12 | **DeezNutz DN404** | Ethereum | Self-transfer `rOwned` overwrite | fresh unprivileged EOA | $2.88 | −$0.17 at 0.0508 gwei; **+$0.53 at 0.0392 gwei** | GAS-DEPENDENT | High |
| 13 | **Limit Break V2** | Polygon | ERC-2771 forwarder offset bypass | fresh unprivileged EOA | $0.5207 | +$0.4686 | BELOW_THRESHOLD | High |

### 5.2 Gated / latent value — not currently extractable

| Target | Chain | Value | Gate / why not extractable now | Evidence |
|---|---|---:|---|---|
| **V4 Router (z0r0z)** | Ethereum + 5 chains | $0 today; live critical | The audited Critical payer-check bypass is **live** on `0x00000000000044a361Ae3cAc094c9D1b14Eece97`, but the only real-token allowance with balance is 5 USDT, and USDT settlement reverts on the non-standard ERC20 return. DRAINED. | `HUNT-069.md` |
| **Morpho Blue** | Ethereum | $33.21 to an existing supplier; fresh EOA $0 | Bad-debt socialization bug live (`Morpho.sol:392`), but the only dust market (`0x0ff9c1…d789`) has zero liquidity and two 1-wei positions; the 85.09% supplier can shift $33.21 by withdrawing before socialization. | `HUNT-072.md` |
| **Ostium** | Arbitrum | 9,169.62 USDC legacy discounts | 963 legacy `LockedDepositNft` holders; new discount-deposit creation removed. Only legacy holders can act. | `HUNT-033.md` |
| **Radiant dLP** | Base | $15,539 AUM; bug live | Initial-donation bug live on `0x8A76639FE8e390Ed16eA88f87BEB46d6A5328254`, but supply is 5.3M shares; zeroing a $10 deposit would need ~$53M of donation. | `HUNT-029.md` |
| **Gamma GMX vaults** | Arbitrum | $115 at risk ($124 total) | `run`/`runNextAction`/`cancelFlow` are keeper-only (`NotAKeeper`); the funded vault is in an open 1x position. | `HUNT-008.md` |
| **Exactly Protocol** | Optimism / Ethereum / Base | $2.80M OP / $0.15M ETH / $12.1M Base TVL | Rounding/donation bug live, but every live market is seeded with 5 USD of dead shares; smallest supply 974,959 wei; `enableMarket` is admin-only. A new market seeded without dead shares reopens it. | `HUNT-067.md` |
| **Omo** | Base | $3.36 max | H-02 `transferFrom` live, but the sole holder has zero router allowance; H-01 reverts `NotWhitelisted`; two vaults hold 4,448 sats cbBTC. | `HUNT-014.md` |
| **ArkProject NFT Bridge** | Ethereum | 888 EveraiDuo (~$11,464) | Genuine Starknet L2→L1 message consumption + whitelist; all five validated highs are DoS/design, not drains. | `HUNT-010.md` |
| **TesseraSwap** | Base | $818,972 treasury | Callback repays at the engine quote, not the amount received; engine bid must exceed best ask + ~5 bp. 251/251 samples were negative. | `h2-tesseraswap.md` |
| **SKY** | BSC | $122,280 pair | Token acquisition blocked; 35% sell tax; V2 buys revert `Transaction Closed`; net −$3,482. | `sky-final.md` |
| **PMMSKYDAO** | BSC | $0.37 | Pool emptied during research; `releaseToken` key-gated. | `pmmskydao-final.md` |
| **GoldPesa GPX hook** | Base | $71,258 | Rebalance price gate closed; opening costs $123,168.72 > the LP. | `goldpesa-verify.md` |
| **Likwid C4–C6** | BSC | $31.08 / $20.29 / $11.07 gross | 16.777215× `minBorrowLevel`; net negative at all sizes. | `likwid-extract.md` |
| **BTCPay Server ≤2.4.1** | Bitcoin/Litecoin | Unquantified | Vendor-confirmed actively exploited; no server probed; no public balance. | `btcpay-deep.md` |

The remaining earlier-campaign rows (gross-positive but net-negative, stale/changed, and patched/not-deployed) are in `EXTRACTABLE_VALUE_MASTER.md` §4–§6. They are not re-traced here.

## 6. Caveats and Stage 3 hand-off

- **Address existence is not exploitability.** A FOUND row means the contract is deployed; it does not mean the vulnerable path is reachable or unpatched. Stage 3 must check the live bytecode and state.
- **Proxy/implementation.** Where a proxy was recorded, the implementation may differ from the audited commit. Stage 3 should resolve the current implementation and compare it to the report.
- **Representative instances.** Multi-instance protocols (per-pool, per-market, per-DAO, per-user clones) are recorded at the factory/core or a representative instance. `stage2_targets.csv` lists the exact address used for each finding.
- **NOT_FOUND is not proof of absence.** Explorer APIs were Cloudflare/key-gated for several chains during this pass, and several projects publish no address. A NOT_FOUND row is a lead for a second pass, not a conclusion.
- **Report status is the publisher's assertion.** No fix status was verified here.
- **No transactions, no keys, no audits.** All work was read-only public research.

## 7. Files

- `stage2/index/stage2_master.csv` — finding-level: finding_uid, project, chain, contract, address, trace_status, profit_confirmed, reason, source_url.
- `stage2/index/stage2_targets.csv` — target-level: project, chain, contract, address, finding count, severity, finding_uid list.
- `stage2/index/stage2_summary.json` — counts and per-chain distribution.
- `stage2/results/ST2-*.json` and `ST2U-*.json` — per-batch agent output with evidence URLs.
- `stage2/batches/` and `stage2/batches_unknown/` — exact batch inputs.

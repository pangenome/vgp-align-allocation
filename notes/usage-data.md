# Usage data — refreshed 2026-07-30

Source: "User and Job Data ACCESS Allocation Request 2026"
(fileId `1pIzOoQuWFqtbwYtih9eYbuMVWV98z4Nhr6vQ2w5y9ho`, owner ncoraor@gmail.com,
**updated 2026-07-29**). Parsed dumps in `notes/data/`.

**The earlier blocker is resolved.** Both the compute and user/job series now run
through **June 2026**, covering nine months of the current (2025/26) allocation
period. Nothing needs to come from XDMoD.

## Allocation-year convention

Allocation years run **Oct 1 – Sep 30**. The workbook's `xracNN sum` rows are
offset by one from its pivot column labels — verified against the `SUM()`
formulas in `notes/data/wb2026-formulas.txt`:

| Sum row | Pivot column | Months | Status |
| --- | --- | --- | --- |
| `xrac24 sum` | 2025 XRAC | Oct 2024 – Sep 2025 | complete, 12 mo |
| `xrac25 sum` | 2026 XRAC | Oct 2025 – Jun 2026 | **partial, 9 mo** |

Everything below labels periods by explicit date range to avoid this trap.

## Compute utilization (core-hours per month)

| Resource | Oct 23–Sep 24 | Oct 24–Sep 25 | **Oct 25–Jun 26 (9 mo)** |
| --- | --- | --- | --- |
| Galaxy Dedicated | 130,396 | 165,608 | 126,795 |
| Frontera (non-ACCESS) | 1,167 | 2,174 | 0 |
| Jetstream2 | 203,268 | 359,042 | **626,661** |
| Jetstream2 GPU | 425 | 1,285 | 903 |
| Bridges-2 | 117,276 | 128,633 | 73,268 |
| Expanse | 224,939 | 141,545 | 88,326 |
| Anvil | 0 | 171,587 | 46,835 |
| Stampede3 | 133,650 | 42,064 | **700** |
| Rockfish | 93,414 | 0 | 0 |
| **Total ACCESS** | 772,971 | 844,155 | **836,693** |
| **Total (all)** | 904,534 | 1,011,937 | 963,487 |
| Dedicated/ACCESS ratio | 0.856 | 0.836 | 0.868 |

Period sums for Oct 2025 – Jun 2026: ACCESS 7,530,233 core-hours; all sources
8,671,386. For the complete prior year: ACCESS 10,129,862; all 12,143,249.

### The story these numbers tell

**Total ACCESS consumption is essentially flat** (844,155 → 836,693 core-hours
per month) while the *distribution* shifted hard. Jetstream2 grew **75%** and now
carries roughly three quarters of all our ACCESS compute, up from about two
fifths. Every HPC line fell: Bridges-2 −43%, Expanse −38%, Anvil −73%,
Stampede3 −98%.

This is a coherent and defensible narrative — TPV routing has consolidated work
onto the cloud-style resource that best matches Galaxy's bursty, short-job,
interactive-latency workload. But it must be *stated*, because the raw table
otherwise reads as five resources in simultaneous decline.

Note the Anvil figure supersedes the earlier read. Last cycle's partial data
showed Anvil ramping steeply (835,549 core-hours in June 2025 alone); across the
full year it averaged 171,587/mo, and it has since fallen to 46,835/mo. The
"Anvil is exploding" framing in the earlier draft was an artifact of a partial
year and must not go into the proposal.

## Requested amounts vs. annualized current usage

| Resource | Requested 2026/27 | Annualized current usage | Ratio |
| --- | --- | --- | --- |
| Jetstream2 CPU | 5,000,000 | ~7,520,000 | **1.5× over request** |
| Jetstream2 GPU | 100,000 | ~10,800 | 0.11× |
| Bridges-2 RM | 2,500,000 | ~879,000 | 0.35× |
| Expanse CPU | 2,000,000 | ~1,060,000 | 0.53× |
| Anvil CPU | 3,000,000 | ~562,000 | 0.19× |
| Stampede3 | 250,000 node-h | ~8,400 core-h | ≪0.1× |

**Caveat before acting on this table:** core-hours are not necessarily SUs.
Charging multipliers differ per resource, and Stampede3 bills node-hours against
core-hour tracking. Confirm against each resource's charging policy. The
directional signal is nonetheless unambiguous.

## User and job statistics

Series runs through June 2026.

| Period | Jobs | New registrations | Mean active users/mo |
| --- | --- | --- | --- |
| Oct 2022 – Sep 2023 | 6,159,432 | 42,691 | 7,023 |
| Oct 2023 – Sep 2024 | 7,649,740 | 48,539 | 7,888 |
| Oct 2024 – Sep 2025 | 9,416,835 | 60,534 | 9,073 |
| **Oct 2025 – Jun 2026 (9 mo)** | **6,744,172** | **54,455** | **9,322** |

**Registrations are accelerating**: 54,455 in nine months annualizes to ~72,600,
a **20% increase** over the prior full year. Total registered users reach
**479,604** by June 2026 (running sum of the monthly series).

Records worth citing:

- **October 2025: 1,010,496 jobs** — all-time monthly record.
- **May 2026: 1,000,040 jobs** — second month ever over one million.
- **November 2025: 11,109 active users** — all-time record.

Job volume for the partial year annualizes to ~8.99M, slightly below the prior
year's 9.42M, while active users and registrations both rose.

## Still stale in the workbook — do not reuse

- `Other Stuff`: tool count still reads **2008**. Use the live API.
- `Job Counts`: still ends June 2022.
- `Cores vs. Runtime`: still references Stampede 2 and Jetstream m1 flavors.
- Total-registered-users snapshot table still stops at June 2023 (304,030); the
  479,604 figure above is derived from the monthly series instead.
- Still absent entirely: **Jetstream2 Large Memory** (the single largest line in
  the request at 12M SU, with no usage tracking anywhere), PSC Ocean, Ranch,
  Corral, Delta/DeltaAI, all storage in TB, and all awarded amounts.

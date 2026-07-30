# Usage data — what exists, what is missing

Extracted from the three Drive workbooks (`User and Job Data ACCESS Allocation
Request 2024 / 2025 / 2026`), all owned by ncoraor@gmail.com.

## The blocker

**There is no resource-usage data for the current allocation period.**

The 2025/26 allocation period runs **Oct 1, 2025 – Sep 30, 2026**. The
`CPU Hours` tab in every workbook — including the one named "2026 (for interim
data)" — stops at **June 2025**. The 2026 workbook is a copy of the 2025
workbook; the two are identical except for the `Users and Jobs` tab.

So the Progress Report for this renewal currently has **zero** compute-hour data
covering the period it is supposed to report on. **This must be pulled from
XDMoD (<https://xdmod.access-ci.org>) before submission.** It is the one thing
that cannot be drafted around.

User and job counts are in better shape but still short: they run through
**January 2026** and need extending to June 2026.

## Allocation-year convention — easy to get wrong

ACCESS allocation years run **Oct 1 – Sep 30**. The workbook names them by
*ending* year (`xrac24` = Oct 2023–Sep 2024). The proposals name them by
*span* ("2025/26 allocation" = Oct 2025–Sep 2026). Past progress report tables
label columns by *starting* year.

Three conventions, one dataset. Verified against the sheet's `SUM()` formulas:

| Workbook row | Months covered |
| --- | --- |
| xrac21 | 2020-10 → 2021-09 |
| xrac22 | 2021-10 → 2022-09 |
| xrac23 | 2022-10 → 2023-09 |
| xrac24 | 2023-10 → 2024-09 |
| xrac25 | 2024-10 → **2025-06 (partial, 9 mo)** |

The "2024" column in the 2025 Progress Report is workbook `xrac25`, i.e. Oct
2024–Jun 2025. Label columns explicitly by date range in the 2026 report rather
than by a bare year.

## Compute utilization, monthly averages (core-hours/month)

From the workbook pivot. Columns are labeled by the workbook's ending-year
convention.

| Resource | 2022 XRAC | 2023 XRAC | 2024 XRAC | 2025 XRAC (9 mo) |
| --- | --- | --- | --- | --- |
| Galaxy Dedicated | 163,940 | 137,257 | 130,396 | 179,968 |
| Frontera (non-ACCESS) | 11,316 | 0 | 1,167 | 2,899 |
| Jetstream (v1) | 198,445 | 0 | 0 | 0 |
| Jetstream2 | 10,164 | 103,715 | 203,268 | 318,555 |
| Jetstream2 GPU | — | — | 425 | 1,255 |
| Bridges-2 | 94,488 | 74,739 | 117,276 | 171,510 |
| Expanse | 0 | 4,593 | 224,939 | 158,848 |
| Anvil | — | — | 0 | 197,602 |
| Stampede 2/3 | 138,099 | 335,309 | 133,650 | 56,085 |
| Rockfish | — | 5,229 | 93,414 | 0 |
| **Total ACCESS** | 441,196 | 470,130 | 772,971 | **903,854** |
| **Total (all)** | 616,453 | 607,387 | 904,534 | **1,086,721** |

Note these differ from the figures printed in the 2024 and 2025 Progress
Reports for the same years. Those reports computed averages over partial years
(data through June at time of writing); the workbook has since been completed
with the remaining months, changing the denominators. **Pick one basis and say
which** — a reviewer comparing the 2025 and 2026 reports will otherwise see the
same year reported with two different numbers.

Straight-lining the partial 2025 XRAC year to 12 months gives ~10.85M ACCESS
core-hours, **+17% over the completed 2024 XRAC year (9,275,653)**.

## Per-resource signals worth acting on

- **Anvil ramped hard.** Zero in 2024 XRAC, 197,602 hrs/mo in 2025 XRAC, and
  **835,549 core-hours in June 2025 alone**. Fastest-growing line in the request.
- **Jetstream2 up 57%** (203,268 → 318,555 hrs/mo).
- **Bridges-2 up 46%** (117,276 → 171,510 hrs/mo).
- **Expanse down 29%** (224,939 → 158,848 hrs/mo).
- **Stampede3 down 58%** (133,650 → 56,085 hrs/mo). This is the exposed line.
- **Bridges-2, Stampede3, and Rockfish all report exactly 0 for both May and
  June 2025.** This is ambiguous and important: it reads as either allocation
  exhaustion or expiry, not as low demand. **Determine which before writing the
  Progress Report** — if those allocations were exhausted, the Stampede3 story
  flips from underutilization to saturation, which is a completely different
  argument. Do not assert either without checking.
- Rockfish and Stampede2 and Jetstream v1 are fully retired from our usage.

## User and job statistics

Authoritative series is the **2025 workbook** (refreshed 2026-02-12), running
through **January 2026**. The 2026 workbook disagrees with it on two overlapping
months (Jul/Aug 2025 job and active-user counts) and is the older refresh — use
the 2025 workbook.

| Period | Jobs | New registrations | Mean active users/mo |
| --- | --- | --- | --- |
| AY2023 (2022-10→2023-09) | 6,159,432 | 42,691 | 7,023 |
| AY2024 (2023-10→2024-09) | 7,649,740 | 48,539 | 7,888 |
| AY2025 (2024-10→2025-09) | 9,416,802 | 60,534 | 9,073 |
| AY2026 partial (2025-10→2026-01) | 3,038,717 | 23,350 | 9,488 |

Records worth citing in the Progress Report:

- **October 2025: 1,010,496 jobs — the all-time monthly record.**
- **November 2025: 11,108 active users — the all-time monthly record.**
- Total registered users **≈448,500 as of Jan 31, 2026** (derived as a running
  sum of monthly registrations; validated against the sheet's own snapshot
  series to within 0.04%). The sheet's explicit total-users snapshots stop at
  June 2023 (304,030) and were never updated.

Growth is real and continuing: AY2025 job count is **+23% over AY2024**, and the
partial AY2026 is tracking above AY2025 on active users.

"Active user" is defined in the sheet as a registered user who submitted at
least one job in the given month.

## What the workbooks do NOT contain

Do not expect to source these from Drive — they are absent entirely:

- **Any awarded/allocated amounts.** These are usage-only ledgers, so burn-down
  against award cannot be computed from them. Get awarded totals from the ACCESS
  allocations portal.
- Any storage figures (Ranch, Ocean, Corral, Jetstream2 storage) in TB.
- PSC Ocean, Ranch, Corral, Delta, and Jetstream2 **Large Memory** usage — note
  that JS2 Large Memory is the single largest line in the 2025 request (12M SU)
  and has no usage tracking in these sheets at all.
- Workflow counts, history counts, dataset counts (the 2025 Progress Report
  quoted these, so they came from elsewhere — likely the Looker dashboard).
- User country counts (`Other Stuff` tab says "will have to wait for DB").

## Stale tabs — do not reuse

- `Other Stuff`: tool count reads **2008**, identical across all three
  workbooks and clearly never updated. The 2025 Progress Report claims 6,900
  tools installed. Use the live API (`curl usegalaxy.org/api/tools | jq ...`),
  not this cell.
- `Job Counts`: ends June 2022, with 12 blank months after it.
- `Cores vs. Runtime`: still references Stampede 2 and Jetstream m1 flavors.
- `IGNORE Active monthly users`: explicitly superseded.

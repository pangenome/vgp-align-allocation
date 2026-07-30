# Per-resource request history

Amounts as *requested* in each year's Main document (not necessarily as awarded).

| Resource | 2023 | 2024 | 2025 | 2026 (draft) |
| --- | --- | --- | --- | --- |
| IU Jetstream2 CPU | 3M SU | 5M SU | 4M SU | TBD |
| IU Jetstream2 Large Memory | — | 4M SU | 12M SU | TBD |
| IU Jetstream2 GPU | 200K SU | 200K SU | 200K SU | TBD |
| IU Jetstream2 Storage | — | 200 TB | 200 TB | TBD |
| PSC Bridges-2 RM | 1M SU | 1.5M SU | 1.5M SU | TBD |
| PSC Bridges-2 EM | — | 100K SU | 100K SU | TBD |
| PSC Ocean | — | 20 TB | 20 TB | TBD |
| SDSC Expanse CPU | 1M SU | 1.5M SU | 1.5M SU | TBD |
| SDSC Expanse GPU | — | — | 100K SU | TBD |
| SDSC Expanse Storage | — | 20 TB | 20 TB | TBD |
| Purdue Anvil CPU | — | 1.5M SU | 1.5M SU | TBD |
| NCSA Delta GPU | — | — | 100K SU | TBD |
| TACC Stampede | 1M SU (S3)* | 500K SU (S3)* | 500K SU (S3) | TBD |
| TACC Ranch | 4 PB | 4 PB | 4 PB | TBD |
| JHU Rockfish | 1M SU* | — | — | — |

\* The 2023 and 2024 Main documents contradict themselves on these lines — the
summary and the body give different systems and different amounts. See
[prior-cycle-issues.md](prior-cycle-issues.md). Values above are from the
section 1 summary, which is what was actually requested.

Mid-cycle supplements were also awarded in the 2023/24 period and are not in the
table above: Jetstream2 (+2.5M CPU, +2.5M Large Memory), Ranch (+3 PB), and a
second Jetstream2 High Memory (+1M) / Bridges-2 EM (+200K) request. The 2024
request folded all of this into the base ask, which is why several lines appear
to jump.

## Observations worth using in the renewal

- **Jetstream2 Large Memory tripled** between the 2024 and 2025 requests (4M → 12M SU).
  The 2025 Progress Report notes "the complete exhaustion of our allocation on
  Jetstream 2 Large Memory," so this line has demonstrated saturation — the
  strongest possible argument for holding or increasing it.
- **Jetstream2 CPU dipped** 5M → 4M in 2025. If 2025/26 usage again ran hot,
  justify a return upward; if not, holding flat is the honest ask.
- **GPU lines expanded** in 2025 (added Expanse GPU and Delta GPU alongside
  Jetstream2 GPU), driven by KegAlign and the whole-genome-alignment effort.
  With alignment in production during 2025/26 this is where growth is most
  defensible — assuming the resources still exist (see resource-landscape.md).
- **Ranch has been flat at 4 PB since 2023**, always justified as "transitioning
  to tiered storage and decreasing our current Corral footprint." Three years on,
  that transition should either be reported as complete or the justification
  should be rewritten. A reviewer checking prior reports will notice the
  identical sentence.
- **Stampede jumped 10K → 500K** with the S2→S3 transition and has been flat
  since. 2025 actual usage was low (56,085 hours in 2024 per the progress
  report table), so this line is the most likely target for reviewer criticism
  about underutilization.
- Rockfish (JHU) appeared in 2023 only, then dropped.

## Utilization vs. request — the weak spot

From the 2025 Progress Report, compute hours by resource:

| Resource | 2021 | 2022 | 2023 | 2024 |
| --- | --- | --- | --- | --- |
| Galaxy Dedicated | 163,940 | 137,257 | 130,396 | 179,968 |
| Frontera (non-ACCESS) | 11,316 | 0 | 1,167 | 2,899 |
| Jetstream 1/2 | 208,609 | 103,715 | 203,268 | 319,809 |
| Bridges-2 | 94,488 | 74,739 | 142,718 | 171,510 |
| Expanse | N/A | 4,593 | 283,321 | 158,848 |
| Stampede 2/3 | 138,099 | 335,309 | 71,553 | 56,085 |
| Rockfish | N/A | 5,229 | 124,551 | N/A |
| Anvil | N/A | N/A | N/A | 197,602 |
| **Total** | 616,453 | 663,846 | 928,162 | 1,086,721 |
| **Total ACCESS** | 441,196 | 523,586 | 807,874 | 903,854 |
| **Percent ACCESS** | 73% | 79% | 87% | 83% |

Note these are *hours*, not SUs, and the Jetstream2/Galaxy Dedicated figures come
from Galaxy's internal accounting, which the report itself flags as an
undercount relative to the Slurm accounting used for the other systems.

The 2026 Progress Report must extend this table through the 2025/26 period and,
per the stated ACCESS requirement, explain any resource that was underutilized.

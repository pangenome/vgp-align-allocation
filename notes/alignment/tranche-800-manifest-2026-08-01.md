# Frozen clade-balanced tranche manifest — 2026-08-01

This manifest adds **800** current NCBI complete or chromosome-level assemblies to the 581-assembly pilot. The resulting catalogue contains **1,381 assemblies**, with **1,568,800 new ordered pairs** and **1,905,780 total ordered pairs.

The TSV manifest is `notes/alignment/data/tranche-800-2026-08-01.tsv`.

## Selection rule

Candidates are ordered greedily by new class, order, family, genus, then species. Assembly quality breaks ties but never overrides taxonomic novelty. Paired GCA/GCF records count as one biological assembly.

## Coverage

| Rank | Pilot matched to NCBI | After tranche | Added |
| --- | ---: | ---: | ---: |
| Class | 9 | 9 | 0 |
| Order | 137 | 156 | 19 |
| Family | 317 | 517 | 200 |
| Genus | 483 | 1,262 | 779 |
| Species | 566 | 1,366 | 800 |

## Tranche composition

- Complete genomes: 39
- Chromosome-level assemblies: 761
- Pilot accessions matched to the current Vertebrata report: 568 of 581
- Unmatched pilot records or deliberate outgroups: 13

The unmatched records are listed in the JSON audit artifact and are retained in the pilot. Most are non-vertebrate chordate or deuterostome outgroups rather than missing vertebrate candidates.

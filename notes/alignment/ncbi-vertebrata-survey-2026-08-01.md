# NCBI Vertebrata assembly survey — 2026-08-01

NCBI Datasets v18.34.0, taxon 7742 (Vertebrata). The raw report contains 15,382 accession records because many biological assemblies have both GenBank (`GCA_`) and RefSeq (`GCF_`) accessions. We count current `GCA_` records to avoid treating a paired RefSeq accession as another assembly.

| Measure | Count |
| --- | ---: |
| Raw GCA/GCF accession records | 15,382 |
| Current biological assemblies | **14,247** |
| Assemblies with a current RefSeq counterpart | 898 |
| Species represented | **6,358** |
| Phase 1 complete/chromosome assemblies | **4,467** |
| Species represented in Phase 1 | **1,896** |

## Assembly level

| Level | All current assemblies | Best assembly per species |
| --- | ---: | ---: |
| Complete Genome | 85 | 54 |
| Chromosome | 4,382 | 1,842 |
| Scaffold | 8,077 | 4,127 |
| Contig | 1,703 | 335 |

## Planning scenarios

The compute columns use the measured FastGA cost of 0.263 node-hours per ordered pair. Storage uses the draft's measured 31.1 MB of working data per pair and must be reconciled with the smaller compressed public release.

| Scenario | N | Ordered pairs | New pairs beyond 581* | Node-h +20% | Working TB/set |
| --- | ---: | ---: | ---: | ---: | ---: |
| All current assemblies, paired RefSeq records deduplicated | 14,247 | 202,962,762 | 202,625,782 | 63,948,697 | 6,312 |
| All chromosome-level and complete assemblies | 4,467 | 19,949,622 | 19,612,642 | 6,189,750 | 620 |
| One best current assembly per represented species, all levels | 6,358 | 40,417,806 | 40,080,826 | 12,649,509 | 1,257 |
| One best assembly per species, scaffold or better | 6,023 | 36,270,506 | 35,933,526 | 11,340,621 | 1,128 |
| One best assembly per species, chromosome or complete | 1,896 | 3,592,920 | 3,255,940 | 1,027,575 | 112 |

\* Assumes all 581 completed pilot assemblies are members of the selected set. Verify this against the pilot accession manifest before using the incremental figure.

## Selected staged inclusion rule

Phase 1 includes all 4,467 complete and chromosome-level assemblies. Within that set, execution order maximizes taxonomic novelty at class, order, family, genus, and species levels before adding redundant assemblies from already dense clades. Later scaffold and contig candidates must pass explicit usability checks and follow the same clade-balanced ordering.

## Species by NCBI class

| Class | Species |
| --- | ---: |
| Actinopteri | 2,448 |
| Aves | 1,996 |
| Mammalia | 1,091 |
| Lepidosauria | 401 |
| Amphibia | 259 |
| Chondrichthyes | 73 |
| Unclassified | 72 |
| Hyperoartia | 11 |
| Myxini | 4 |
| Cladistia | 3 |

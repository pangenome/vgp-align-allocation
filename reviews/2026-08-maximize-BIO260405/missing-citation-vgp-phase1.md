# Missing citation — VGP Phase I preprint (Formenti et al. 2026)

Discovered after submission. Should have been in the References document and in
the Main Document's background/support narrative. Do not invent figures from it;
pull values from the preprint itself when reconciling.

## Citation

> Formenti G, Absolon DE, Abueg LAL, Ackerman F, Al-Ajli FO, Aleixo A, Antunes A,
> … Cao S, … Garrison E, … Guarracino A, … Jarvis ED, Vertebrate Genomes Project
> Consortium Phase I. The Vertebrate Genomes Project Phase I: a global reference
> genome resource. bioRxiv. 2026. doi:10.64898/2026.06.24.732306.

- Posted 2026-06-26 (before our 2026-07-31 / 2026-08-01 submission).
- Preprint; not yet peer-reviewed. cite as preprint.
- Relevant authors from our team: Shuo Cao, Erik Garrison, Andrea Guarracino.

## Why it matters for BIO260405

1. **It supplies the biological imperative reviewer #1 asked for.** Its abstract
   names concrete impacts: reconstructing the last common ancestor of all
   vertebrates 500 Mya, modes of sex-chromosome evolution, clade-specific
   three-dimensional genome architecture, methylated epigenetic landscapes,
   gene/pseudogene evolution, immune loci, cancer-associated genes, and IUCN
   Red List extinction-risk work.
2. **It gives the VGP Phase I baseline we build on.** It reports completion of
   Phase I with a defined species count and a comparative-analysis subset of
   579 species — the set our alignment expands from.
3. **It establishes published, co-authored context for the pilot.** Our
   581-assembly all-to-all alignment underpins the Phase I comparative analysis;
   we are consortium authors. This refutes "no publications or grants associated
   with the work."

## How it maps onto the reviews

| Reviewer point | How the preprint answers it |
| --- | --- |
| #1 "unclear the biological imperative or impacts" | The preprint's impact list is the rationale; restate it ahead of our methods. |
| #1 / #2 "no publications/grants associated with the work" | Preprint is a co-authored, citable product of the same consortium and dataset. |
| #1 "why all 4,467 NCBI chromosome-level assemblies" | Position our expansion as extending a published Phase I backbone beyond VGP into the full public catalogue. |
| #2 "no relevant manuscripts… at peer-review outlets" | A Phase I preprint exists; state its status plainly and note any plans for peer review. |

## Verified from the full PDF (2026-10-05)

- **Preprint's own numbers:** "~95% of vertebrate orders", **816 species**,
  **1.6 trillion bp**; data-freeze subset **579 species**; all-vs-all of that
  freeze using `wfmash` and `FastGA`, **336,980 pairwise alignment files in PAF
  format per method** (Supplementary Table 11, row 17), indexed with `impg`.
  Use these, not aggregator variants (815, ~97%).
- **Pilot passage** (section "Initial phylogeny and whole-genome alignments"):
  *"We also performed an all-vs-all alignment of the 579 species data freeze,
  using wfmash and FastGA, generating 336,980 pairwise alignment files in PAF
  format per method (Supplementary Table 11, row 17). Each alignment was
  indexed using impg…"*
- **Count reconciliation:** 336,980 = 581 × 580. 581 assemblies = 579-species
  data freeze (566 vertebrate species + 13 outgroup species) + 2 additional
  haplotypes (human GRCh38, mouse GRCm39). Matches our manifest (566 matched
  species, 568 Vertebrata, 13 outgroups).
- **Grant link in acknowledgements:** *"E.G., P.S., S.C. acknowledge funding
  from NIH R01HG013017 and U01HG013760."*

## Remaining TODOs

- [ ] Update `references.md` and the Main Document; keep Vancouver numbering
      consistent.
- [ ] Confirm the 581 = 579 + 2-haplotype arithmetic against Supplementary
      Table 11 in the submission PDF.

## Action

Add as a numbered reference, lead the background section with its impact
statement, state our team's authorship, and reconcile the counts before the
renewal submission.

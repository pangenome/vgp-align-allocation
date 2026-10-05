# Abstract

Comparative genomics across the vertebrate tree usually reduces many genomes
to alignments against one reference or to a multiple alignment directed by a
phylogenetic guide tree. Both choices impose prior structure on the result. We
are building a reference-free alternative: a direct all-to-all whole-genome
alignment that supports locus-level studies of conservation, structural change,
and phylogenetic conflict.

The first stage is complete. We aligned 568 Vertebrate Genomes Project (VGP)-
derived vertebrate assemblies and 13 phylogenetic outgroups in both directions
— 581 assemblies and 336,980 ordered pairs — on TACC Stampede3. The
campaign spanned portions of two annual allocations, with approximately 94%
effective utilization in the reconstructed job records. We released an interactive heatmap of pairwise similarity and
coverage, and we are publishing the underlying PAF files through GenomeArk.
This completed atlas establishes feasibility and a measured cost basis.

We now propose to expand beyond the VGP-derived pilot. A reproducible NCBI
survey on 2026-08-01 identified 14,247 current vertebrate assemblies
representing 6,358 species across complete-genome, chromosome, scaffold, and
contig assembly levels. We will use this inventory to define a dated catalogue,
compute only ordered pairs involving newly admitted assemblies, and publish the
manifest and derived alignments.

We will analyze the alignment network with `impg`, not by materializing a
whole-genome pangenome graph. `impg` treats pairwise alignments as an implicit
pangenome graph and projects a selected region through direct and transitive
homologies. We have already used it for ape incomplete-lineage-sorting windows
and VGP BUSCO gene analyses. The expanded project will use the same indexed,
regional model to measure conservation and phylogenetic conflict across the
vertebrate tree.

The 4,467 current complete and chromosome-level assemblies, representing 1,896
species, define our multi-allocation first phase. We request 1,000,000
Stampede3 SUs for its next clade-balanced tranche. At the measured FastGA rate
and the highest standard CPU charge, this award supports approximately 800 new
assemblies and advances the catalogue from 581 to approximately 1,381. We prioritize assemblies that add an unrepresented
class, order, family, genus, or species before additional assemblies from
densely sampled clades. Later awards will complete the chromosome-level set
and admit usable scaffold- and contig-level assemblies.


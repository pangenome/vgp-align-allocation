# **1. Resource utilization statistics**

Because the current allocation period has not ended, we will consider average compute hours per month to evaluate compute usage for the Galaxy Gateway, through the end of June 2024:

|  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: |
|   | \*\*2021\*\* | \*\*2022\*\* | \*\*2023\*\* | \*\*2024\*\* |
| Galaxy Dedicated | 163,940 | 137,257 | 130.396 | 179,968 |
| Frontera (non-ACCESS) | 11,316 | 0 | 1,167 | 2,899 |
| Jetstream 1/2 | 208,609 | 103,715 | 203,268 | 319,809 |
| Bridges-2 | 94,488 | 74,739 | 142,718 | 171,510 |
| Expanse | N/A | 4,593 | 283,321 | 158,848 |
| Stampede 2/3 | 138,099 | 335,309 | 71,553 | 56,085 |
| Rockfish | N/A | 5,229 | 124,551 | N/A |
| Anvil | N/A | N/A | N/A | 197,602 |
| Total | 616,453 | 663,846 | 928,162 | 1,086,721 |
| Total ACCESS | 441,196 | 523,586 | 807,874 | 903,854 |
| \*\*Percent ACCESS\*\* | \*\*73%\*\* | \*\*79%\*\* | \*\*87%\*\* | \*\*83%\*\* |

The Galaxy Dedicated and Jetstream 2 compute hour calculations were performed using Galaxy’s internal accounting and is an undercalculation compared to the other resources, which used the more accurate Slurm accounting database. However, the complete exhaustion of our allocation on Jetstream 2 Large Memory corroborates this increase in resource utilization.

|  |
| :-: |
|   |
| \*\*Figure 1\*\*. Galaxy Gateway compute utilization (per month) by resource. |

In this allocation period, we requested time on three resources that are similar in configuration: Bridges-2, Expanse, and Anvil. This decision was made after we successfully exhausted our Bridges-2, Expanse, and Anvil allocations in previous years, had successfully shifted more of our workload to shared node allocations, and demonstrated an ability to efficiently balance workloads across multiple resources. In addition, adjustments to our scheduling policy resulted in a more efficient usage of Stampede3, which allocates full nodes to jobs.

Galaxy stores 5.8 TB of genomic and other bioinformatics reference data in CVMFS (<https://cernvm.cern.ch/fs/>), a global read-only filesystem designed for software and data distribution. Because this filesystem is not mounted on HPC systems, this limited our ability to send certain types of jobs to those systems. During the 2022-2023 allocation period, we successfully deployed the cvmfsexec package (<https://github.com/cvmfs/cvmfsexec>) to provide this data on HPC systems as it is on our dedicated resources and Jetstream 2. Combined with Apptainer (<https://apptainer.org/>), we have been able to produce a compute environment on unprivileged, shared HPC systems that exactly mirrors the environment on our dedicated cluster and cloud instances on Jetstream 2. During the 2023-2024 period, we refined this environment to eliminate sources of job failures and it has been in production use throughout the 2024-2025 allocation period.

Leveraging this work, we have been able to make more efficient use of all resources supporting the Galaxy Gateway, including dedicated resources.

# **2. User statistics**

Between June 2024 and June 2025 new user registration remained consistently high (Fig. 2). The number of new accounts created each month ranged from 2,882 in June 2024 to a peak of over 6,000 in November 2024. From October 2024 through the spring of 2025, monthly registrations remained above 4,000. These numbers point to persistent interest from researchers and educators. By June 2025, the total number of registered users had reached 412,379, with an average of nearly 4,000 new users joining each month.

Engagement, defined as submitting at least one computational job, showed that a large portion of new users went beyond simple exploration. 32.8 percent of new users each month remained active for more than one day. This pattern suggests that nearly one-third of newly registered users became meaningfully involved in scientific work soon after joining. When including all users—new and returning—an average of 16.8 percent of the monthly active community were newcomers who engaged with the platform beyond a single session. About 4,004 users each month returned to use the platform on multiple days.

Computational throughput over this period was considerable. Nearly 69 million jobs were executed, with monthly volumes ranging from around 522,000 in June 2024 to over one million in February and March of 2025. The average was 682,000 jobs per month. 

Job failure rates remained low (Job failures are primarily caused by corrupt or wrong data uploaded by users. They are rarely caused by problems with Galaxy infrastructure). On average, \~70,000 jobs failed each month (10.3%). Jobs submitted by new users accounted for \~ 14,800 failures per month, or 8.8%. This slightly lower error rate among newer users may reflect the effectiveness of default tool settings, introductory documentation, and training materials. 

More than 45% of all jobs each month came from users who had been active prior to that month. The remainder was split between new users who used the platform only once and those who returned. The returning group—new users who engaged for more than one day— accounted for a large share of job activity. Those who interacted with the platform only on their registration day contributed significantly less to overall system load. These patterns indicate that the majority of Galaxy’s computational capacity is consumed by a stable user base and by newly registered users who quickly transition into regular users.

Over this thirteen-month span, users created more than 11.1 million histories (Galaxy’s terms for users’ workspaces) and generated a total of 128.4 million datasets. Automation and reproducibility are increasingly important in research, and the Galaxy platform supports both through its workflow features. In total, \>492,000 workflows were created, and \>868,000 workflow executions occurred during the period. 

As of June 2025, 6,900 distinct tools had been installed on [usegalaxy.org](http://usegalaxy.org). This toolset allows users from many disciplines—genomics, transcriptomics, epigenomics, proteomics, and beyond—to carry out their work in a single unified platform.

|  |
| :-: |
|  |
| \*\*Figure 2.\*\* New user registration and engagement data. |

# **3. Impact: Publications enabled by the service**

The service provided by us is well established and popular. As a result it is often taken for granted and not cited properly. For the list of publications resulting from the use of Galaxy by the scientific community see the document **“Addressing Reviewers Comments”** (for full, but still incomplete, list see <https://www.zotero.org/groups/1732893/galaxy/items/L5WWHAIU/library>). **Note that we could not fit all publications into the required 3 pages\!**

  
  
  
  
  
  
  
  
  
  
**  
**

### **This list shows publications resulting from the use of Galaxy by the scientific community in 2025. To fit within the required 3 pages this list is limited to 65 most recent publications. The total number of publications for 2024 and 2025 is 183 and 322, respectively.** 

  

1.  Aciole Barbosa,D. *et al.* (2025) *De novo* assembly and annotation of the pantranscriptome of *Astyanax lacustris* on the liver and pituitary-gonadal axis. *Marine Genomics*, **81**, 101190.
2.  Aciole Barbosa,D. *et al.* (2025) De Novo Assembly and Annotation of the Pantranscriptome of Astyanax Lacustris on the Liver and Pituitary-Gonadal Axis.
3.  Al-Jawabreh,H. and Thesis,M. (2025) Molecular Epidemiology: Prevalence of Human Cutaneous Leishmaniasis in Palestine in the Period between 2016 and 2024 Using Next Generation Sequencing.
4.  Almeida,C. and Marques,A. (2025) Giant mitogenomes in Rhynchospora are a result of nuclear gene and retrotransposon insertions in intergenic spaces. *Annals of Botany*, mcaf098.
5.  Almiñana Brines,C. *et al.* (2025) P-346 Endometriosis-associated infertility changes the microRNA profile of cumulus cells with a notably pronounced effect on oocytes that failed fertilisation. *Human Reproduction*, **40**, deaf097.653.
6.  Altaf,M.T. *et al.* (2025) Unveiling Genetic Basis Associated With Manganese Content in Turkish Common Bean (Phaseolus vulgaris L.) Germplasm Through a Genome-Wide Association Study. *Plant Breeding*, **144**, 285–309.
7.  Anwar,S. *et al.* (2025) The Complete Mitochondrial Genome Assembly of Bali Cattle (Bos Javanicus) Using Oxford Nanopore Long-Read Sequencing Technology.
8.  A. Pletsch,E. *et al.* (2025) A type 4 resistant potato starch alters the cecal microbiome, gene expression and resistance to colitis in mice fed a Western diet based on NHANES data. *Food & Function*.
9.  Aruwa,C.E. and Sabiu,S. (2025) Staphylococcus Aureus AgrA Modulators from South African Antimicrobial Plants. *Chemistry & Biodiversity*, **n/a**, e202403220.
10. Asadi,S. *et al.* (2025) Exploring effector candidates in Rhynchosporium commune: insights into their expression dynamics during barley infection. *Scientific Reports*, **15**, 17667.
11. Baei,B. *et al.* (2025) Pharmacophore modeling and QSAR analysis of anti-HBV flavonols. *PLOS ONE*, **20**, e0316765.
12. Banar,M. *et al.* (2025) A novel broad-spectrum bacteriophage cocktail against methicillin-resistant Staphylococcus aureus: Isolation, characterization, and therapeutic potential in a mastitis mouse model. *PLOS ONE*, **20**, e0316157.
13. Barragán-Rosillo,A.C. *et al.* (2025) The role of DNA content in shaping chromatin architecture and gene expression. *The Plant Journal*, **121**, e70116.
14. Barroso,M.do V. *et al.* (2025) Genomic insights into a colonization-infection progression by a carbapenemase-producing *Klebsiella quasipneumoniae* K1 serotype. *Journal of Global Antimicrobial Resistance*, **44**, 12–14.
15. Benatto Perino,E.H. *et al.* (2025) The suberin transporter StABCG1 is required for barrier formation in potato leaves. *Scientific Reports*, **15**, 7930.
16. Berns,H. *et al.* (2025) A homozygous human WNT11 variant is associated with laterality, heart and renal defects. *Disease Models & Mechanisms*, dmm.052211.
17. Bessette,E. *et al.* (2025) Integrated Morphological and Genome Redescription of Leidyana Gryllorum in Acheta Domesticus: Uncovering Gregarine Diversity in Gryllidae.
18. Bhuiyan,T. *et al.* (2025) TAF2 condensation in nuclear speckles links basal transcription factor TFIID to RNA splicing factors. *Cell Reports*, **44**.
19. Black,K.A. *et al.* (2025) Resolution of a T1-Like Bacteriophage Outbreak by Receptor Engineering. *Molecular Biotechnology*.
20. Boondech,A. *et al.* (2025) Complete genome and comparative analysis of Xanthomonas oryzae pv. oryzae isolated fro  
21. m northern Thailand. *Access Microbiology*, **7**, 000986.v4.
22. Boulogne,I. *et al.* (2025) Meta-analysis of RNA-Seq datasets allows a better understanding of P. tricornutum cellular biology, a requirement to improve the production of Biologics. *Scientific Reports*, **15**, 3603.
23. Bright,A.R. *et al.* (2025) Temporal control of progenitor competence shapes maturation in GABAergic neuron development in mice. *Nature Neuroscience*, 1–13.
24. Brimson,C.A. *et al.* (2025) Collective oscillatory signaling in Dictyostelium discoideum acts as a developmental timer initiated by weak coupling of a noisy pulsatile signal. *Developmental Cell*, **60**, 918–933.e4.
25. Casella,V. *et al.* (2025) Novel Insights into the Nobilamide Family from a Deep-Sea Bacillus: Chemical Diversity, Biosynthesis and Antimicrobial Activity Towards Multidrug-Resistant Bacteria. *Marine Drugs*, **23**, 41.
26. Cen,W. *et al.* (2025) Morpho-Molecular Discordance and Cryptic Diversity in Jumping Bristletails: A Mitogenomic Analysis of Pedetontus silvestrii (Insecta: Archaeognatha: Machilidae). *Insects*, **16**, 452.
27. Chen,T. *et al.* (2025) Developing *Bacillus subtilis* as cell factory for the production of the natural biocontrol compound pulcherrimin. *Bioresource Technology*, 132433.
28. Chen,Y. *et al.* (2025) Terrestrial Adaptation in Chelonoidis vicina as Revealed Based on Analysis of the Complete Mitochondrial Genome. *Genes*, **16**, 173.
29. Chiappa,G. (2025) Evolutionary biology of Raphitoma Bellardi, 1847 (Neogastropoda, Conoidea).
30. Contreras,P. *et al.* (2025) *De novo* transcriptome assembly and functional annotation supports potential biotechnological applications for the non-model thraustochytrid *Ulkenia visurgensis* Lng2. *Gene*, **958**, 149492.
31. Córdova Bastidas,D.A. (2025) Comparación genómica de especies de klebsiella secuenciadas en Ecuador: resistencia y diversidad.
32. Costa,R.A. *et al.* (2025) Olfactory specialization in the Senegalese sole (*Solea senegalensis*): CO2 acidified water triggers nostril-specific immune processes. *Comparative Biochemistry and Physiology Part A: Molecular & Integrative Physiology*, 111820.
33. Cruz-Ojeda,P.de la *et al.* (2025) In silico analysis of lncRNA-miRNA-mRNA signatures related to Sorafenib effectiveness in liver cancer cells. *World Journal of Gastroenterology*, **31**.
34. Cunha,P.C. *et al.* (2025) Characterization of Newly Isolated Rosenblumvirus Phage Infecting Staphylococcus aureus from Different Sources. *Microorganisms*, **13**, 664.
35. Carvalho,C.V. de *et al.* (2025) First report of Moraxella oculi in Brazil in an infectious bovine keratoconjunctivitis outbreak. *Veterinary Research Communications*, **49**, 143.
36. Denis,J. *et al.* (2025) Identification of Toxoplasma gondii antigenic proteins using an in vivo approach and in silico investigation of their polymorphism. *Microbiology Spectrum*, **0**, e02040–24.
37. Devasahayam,B. (2025) Microbial confrontations trigger broad array synthesis of human-toxic secondary metabolites.
38. Do,K. *et al.* (2025) A Clinical Metaproteomics Workflow Implemented within Galaxy Bioinformatics Platform to Analyze Host-Microbiome Interactions Underlying Human Disease. *Journal of Visualized Experiments (JoVE)*, e67581.
39. Doyle,T.D. *et al.* (2025) Multiple factors contribute to female dominance in migratory bioflows. *Open Biology*, **15**, 240235.
40. Duffy,D.J. *et al.* (2025) Rapid pan-biodiversity lifeform and genomic diversity detection from shotgun sequencing of air eDNA.
41. Dwiyanti,F.G. *et al.* (2025) Whole Genome Sequencing of Neolamarckia macrophylla (Roxb.) Bosser and Neolamarckia cadamba (Roxb.) Bosser from Indonesia: A vital resource for completing chloroplast genomes and mining microsatellite markers. *Frontiers in Plant Science*, **16**.
42. Ertürkmen,P. (2025) Microbiota Composition of Buffalo Colostrum and Characterization of Potential Probiotic Bacteria With High Exopolysaccharide Production and Cholesterol Assimilation Capacity. *Journal of Food Quality*, **2025**, 4406517.
43. Espadinha,D. *et al.* (2025) Case–Control Study of Factors Associated with Hemolytic Uremic Syndrome among Shiga Toxin–Producing Escherichia coli Patients, Ireland, 2017–2020. *Emerging Infectious Diseases*, **31**, 728–740.
44. Falconieri,A. *et al.* (2025) The Extremely Low Mechanical Force Generated by Nano-Pulling Induces Global Changes in the Microtubule Network, Nuclear Morphology, and Chromatin Transcription in Neurons. *Small*, **n/a**, 2503011.
45. Farmiloe,G. *et al.* (2025) Transcriptomic profiling of unmethylated full mutation carriers implicates TET3 in FMR1 CGG repeat expansion methylation dynamics in fragile X syndrome. *Journal of Neurodevelopmental Disorders*, **17**, 22.
46. FRACCALVIERI,R.O.S.A. (2025) Isolamento di batteri appartenenti alla famiglia delle Enterobatteriacee resistenti agli antibiotici in alimenti di origine animale e vegetale: analisi genomica e implicazioni per la sicurezza alimentare.
47. Fraccalvieri,R. *et al.* (2025) Isolation and Characterization of Colistin-Resistant Enterobacteriaceae from Foods in Two Italian Regions in the South of Italy. *Microorganisms*, **13**, 163.
48. Freedman,A. *et al.* (2025) Plasmid and chromosomal sequences of Pantoea agglomerans isolated from air in Fort Collins, Colorado. *Microbiology Resource Announcements*, **0**, e00341–25.
49. Fuchs,J. *et al.* (2025) varVAMP: degenerate primer design for tiled full genome sequencing and qPCR. *Nature Communications*, **16**, 5067.
50. Fullstone,T.L. *et al.* (2025) Identification of FLYWCH1 as a regulator of platinum-resistance in epithelial ovarian cancer. *NAR Cancer*, **7**, zcaf012.
51. Gadkar,V.J. *et al.* (2025) RLB-MALBAC: a rapid, non-transposase method for synthesizing unbiased sequencing libraries from low amount of genomic DNA for Nanopore sequencing. *BMC Methods*, **2**, 4.
52. Galvis,J. *et al.* (2025) Using DIMet for Differential Analysis of Labeled Metabolomics Data: A Step-by-step Guide Showcasing the Glioblastoma Metabolism. *Bio-protocol*, **15**, e5168.
53. Garcia-Jimenez,P. and Robaina,R.R. (2025) Exploring transposons in macroalgae: LTR elements and neighboring genes in red seaweeds. *Frontiers in Marine Science*, **12**.
54. Garcia,I.R. and Larcombe,L.D. (2025) Exploring the Perturbation of Biological Processes Caused by Gene Upregulation Using Knock-In Transfection, Transcriptomics, and Bioinformatics Analysis. In, Moll,J. and Carotta,S. (eds), *Target Identification and Validation in Drug Discovery: Methods and Protocols*. Springer US, New York, NY, pp. 121–136.
55. Gather,F. *et al.* (2025) The lincRNA Pantr1 is a FOXG1 target gene conferring site-specific chromatin binding of FOXG1. *Nucleic Acids Research*, **53**, gkaf539.
56. Goclowski,C.L. *et al.* (2025) Galaxy as a gateway to bioinformatics: Multi-Interface Galaxy Hands-on Training Suite (MIGHTS) for scRNA-seq. *GigaScience*, **14**, giae107.
57. Gomes,S.M. *et al.* (2025) Unlocking the Potential of Medicago truncatula A17 Cell Suspension Cultures for Bioproduction of Astaxanthin and Canthaxanthin. *Biotechnology and Bioengineering*, **n/a**.
58. González-Vinceiro,L. *et al.* (2025) PLAMseq enables the proteo-genomic characterization of chromatin-associated proteins and protein interactions in a single experimental workflow.
59. Goshi,N. *et al.* (2025) Direct effects of prolonged TNF-α and IL-6 exposure on neural activity in human iPSC-derived neuron-astrocyte co-cultures. *Frontiers in Cellular Neuroscience*.
60. GREY,F. *et al.* (2025) African swine fever viral infections.
61. Gruber,P. *et al.* (2025) Complete genome sequence of Planococcus koreensis isolated from soil in Fort Collins, Colorado. *Microbiology Resource Announcements*, **0**, e00193–25.
62. Haidar,H. *et al.* (2025) Neural function of Netrin-1 in precancerous lesions of the pancreas.
63. Hamar,R. and Varga,M. (2025) The zebrafish (Danio rerio) snoRNAome. *NAR Genomics and Bioinformatics*, **7**, lqaf013.
64. Harahap-Carrillo,I.S. *et al.* (2025) Chronic, Low-Dose Methamphetamine Reveals Sexual Dimorphism of Memory Performance, Histopathology, and Gene Expression Affected by HIV-1 Tat Protein in a Transgenic Model of NeuroHIV. *Viruses*, **17**, 361.
65. Hashimoto,T. *et al.* (2025) The oncoprotein DEK controls growth-regulated gene expression by enhancing the DNA-binding activity of basic leucine zipper transcription factors. *The FEBS Journal*.
66. Haufschild,T. *et al.* (2025) Novel tools for genomic modification and heterologous gene expression in the phylum Planctomycetota. *Applied Microbiology and Biotechnology*, **109**, 79.
67. He,J. *et al.* (2025) Depletion of P2X4 receptor alleviates prostate cancer bone metastasis through reduced cancer cell invasiveness and enhanced cell adhesion activities. *Purinergic Signalling*.
68. Heise,C.M. *et al.* (2025) Evidence for a CO2-concentrating mechanism in the model streptophyte green alga Chara braunii. *New Phytologist*, **n/a**.
69. Henriques,L.R. *et al.* (2025) Revealing the hidden diversity of Chlorella heliozoae-infecting giant viruses. *npj Viruses*, **3**, 1–11.
70. Hermawaty,D. *et al.* (2025) De novo transcriptome assembly and analysis during agarwood induction in Gyrinops versteegii Gilg. seedling. *Scientific Reports*, **15**, 2977.
71. Honecker,B. *et al.* (2025) Entamoeba histolytica extracellular vesicles drive pro-inflammatory monocyte signaling. *PLOS Neglected Tropical Diseases*, **19**, e0012997.
72. Huang,Y.-T. *et al.* (2025) Rising threat of metallo-β-lactamase-producing *Klebsiella oxytoca* complex in Taiwan, 2013-2022. *International Journal of Antimicrobial Agents*, 107515.
73. Hurtado,A. *et al.* (2025) A One Health approach for the genomic characterization of antibiotic-resistant Campylobacter isolates using Nanopore whole-genome sequencing. *Frontiers in Microbiology*, **16**.
74. Inäbnit,T. *et al.* (2025) Mitochondrial Genomes of Three Melampus Species (Ellobiidae; Gastropoda). *Ecology and Evolution*, **15**, e71282.
75. Ishtiaq,B. *et al.* (2025) Discovering promising drug candidates for Parkinson’s disease: integrating miRNA and DEG analysis with molecular dynamics and MMPBSA. *Journal of Computer-Aided Molecular Design*, **39**, 8.
76. Jepsen,V.H. (2025) Linker histone variant H1-0 dysregulation in ETV6::RUNX1+ preleukemia and B cell acute lymphoblastic leukemia.
77. Ji,J.-H. *et al.* (2025) Unusual Genetic Diversity Within Thereuopoda clunifera (Wood, 1862) (Chilopoda: Scutigeromorpha) Revealed by Phylogeny and Divergence Times Using Mitochondrial Genomes. *Insects*, **16**, 486.
78. Jönsson,A. *et al.* (2025) Enhanced biocompatibility of 3D printed resin parts via wet autoclave postprocessing: implications for stem cell organ-on-a-chip culture. *Materials Advances*.
79. Joshi,P. *et al.* (2025) Insights into urinary catheter colonisation and polymicrobial biofilms of Candida- bacteria under flow condition. *Scientific Reports*, **15**, 15375.
80. Joshi,S. and Srivastava,R. (2025) Theoretical studies on safety and efficacy of 16 small-molecule MC4R antagonists as therapeutics for obesity. *Journal of Proteins and Proteomics*.
81. Kabir,T. *et al.* (2025) Genome characterization, pathogenicity, and evaluation of therapeutics of Klebsiella aerogenes in Bombyx larvae infection model. *BMC Microbiology*, **25**, 209.
82. Kandinov,I. *et al.* (2025) Molecular epidemiology of Neisseria gonorrhoeae isolates in Russia, 2015–2023: current trends and forecasting. *Frontiers in Cellular and Infection Microbiology*, **15**.
83. Kashani,N. *et al.* (2025) *In silico* drug repurposing for potential HPV-induced skin wart treatment − A comparative transcriptome analysis. *Journal of Genetic Engineering and Biotechnology*, **23**, 100485.
84. Kim,N.M. *et al.* (2025) Nucleotide-level characterization and improvement of l-arabinose- and l-rhamnose-inducible systems in E. coli using a high-throughput approach. *Nucleic Acids Research*, **53**, gkaf224.
85. Kiser,H. *et al.* (2025) Comparative mitochondrial and phylomitogenomic analyses support the existence of a cryptic species complex in *Gonodactylaceus falcatus* (Stomatopoda: Gonodactyloidea). *Gene Reports*, **40**, 102248.
86. Kongsomboonchoke,P. *et al.* (2025) Rapid formulation of a genetically diverse phage cocktail targeting uropathogenic Escherichia coli infections using the UTI89 model. *Scientific Reports*, **15**, 12832.
87. Konkol,M. *et al.* (2025) Encouraging reusability of computational research through Data-to-Knowledge Packages - A hydrological use case. *Open Research Europe*, **5**, 123.
88. Kruszewski,M. *et al.* (2025) Sensitization of Non-M3 Acute Myeloid Leukemia Blasts to All-Trans Retinoic Acid by the LSD1 Inhibitor Tranylcypromine: TRANSATRA Phase I Study. *European Journal of Haematology*, **n/a**.
89. Kumari,L.S. *et al.* (2025) Rapid whole genome sequencing for AMR surveillance in low- and middle-income countries: Oxford Nanopore Technology reveals multidrug-resistant Enterobacter cloacae complex from dairy farms in Sri Lanka. *BMC Veterinary Research*, **21**, 351.
90. Kunz,L. *et al.* (2025) Avirulence depletion assay: Combining R gene-mediated selection with bulk sequencing for rapid avirulence gene identification in wheat powdery mildew. *PLOS Pathogens*, **21**, e1012799.
91. Lacchini,E. *et al.* (2025) Engineering Gypsophila elegans hairy root cultures to produce endosomal escape-enhancing saponins. *Plant Biotechnology Journal*, **n/a**.
92. Lacerda,J.T. *et al.* (2025) The effect of thermal stress on the X-organ/sinus gland proteome of the estuarine blue crab *Callinectes sapidus* during the intermolt and premolt stages. *Journal of Proteomics*, **313**, 105382.
93. Lanave,G. *et al.* (2025) Discovery of a human parvovirus B19 analog (Erythroparvovirus) in cats. *Scientific Reports*, **15**, 9650.
94. Lapadula,W.J. *et al.* (2025) Characterization of Ribosome inactivating protein genes and their transcripts in *Trialeurodes vaporariorum*. *Gene*, **948**, 149356.
95. Lee,F.C.H. *et al.* (2025) Little influence of DNA quality on the direct sequencing output of non-human primates’ faecal samples. *Journal of Virological Methods*, **332**, 115074.
96. Lengyel,M. *et al.* (2025) Zymogen granule protein 16B (ZG16B) is a druggable epigenetic target to modulate the mammary extracellular matrix. *Cancer Science*, **116**, 81–94.
97. Lenz,J. *et al.* (2025) Hangover regulates gene expression by limiting NSL-mediated H4K16 acetylation.
98. Li,Y. *et al.* (2025) Functional characterization of *Camptotheca acuminata* 7-deoxyloganetic acid synthases and 7-deoxyloganetic acid glucosyltransferases involved in camptothecin biosynthesis. *Plant Physiology and Biochemistry*, **218**, 109305.
99. Liao,J. *et al.* (2025) In-depth analysis of the first complete mitochondrial genome of the rare shrimp Alpheus euphrosyne, with comparative phylogenetic genomics insights into the Alpheus species. *Molecular Biology Reports*, **52**, 579.
100. Lin,Y.-T. *et al.* (2025) Integrative morphological, mitogenomic and phylogenetic analyses reveal new vent-dwelling scallop species. *Invertebrate Systematics*, **39**, NULL–NULL.
101. The complete mitochondrial genome of Crocidura rapax Allen, 1923 and its phylogenetic analyses (2025) *Mitochondrial DNA Part B*, **10**, 288–291.
102. Luo,T. *et al.* (2025) Comparative Mitochondrial Genomic and Phylogenetic Study of Eight Species of the Family Lonchodidae (Phasmatodea: Euphasmatodea). *Genes*, **16**, 565.
103. Mandal,A. *et al.* (2025) Dataset of benthic foraminiferal community structure from sediment eDNA of Sundarbans mangrove ecosystem. *Data in Brief*, 111554.
104. Mapunda,L.A. *et al.* (2025) Coxsackievirus A24: A Causative Agent of Acute Haemorrhagic Conjunctivitis Outbreak in Dar es Salaam, Tanzania, between January and February 2024.
105. Maridueña-Zavala,M.G. *et al.* (2025) Babaco Mosaic Virus (BabMV) Induces Genome-Wide Transcriptomic Reprogramming in Carica papaya. *Physiologia Plantarum*, **177**, e70270.
106. Mitra,S. *et al.* (2025) Diversity of mobile genetic elements in carbapenem-resistant Enterobacterales isolated from the intensive care units of a tertiary care hospital in Northeast India. *Frontiers in Microbiology*, **16**.
107. Mohebbi,A. *et al.* (2025) Computer-aided drug repurposing & discovery for Hepatitis B capsid protein. *In Silico Pharmacology*, **13**, 35.
108. Nazari,M. *et al.* (2025) Comprehensive analysis of Slc15a3 and Myo1f gene expression in renal carcinoma: Insights from RNA-seq data and validation via qRT-PCR. *Human Gene*, 201422.
109. Negrete-Méndez,H. *et al.* (2025) A Lambda-evo (λevo) phage platform for Zika virus EDIII protein display. *Applied Microbiology and Biotechnology*, **109**, 8.
110. Hidalga,A. Nieva de la *et al.* (2025) Facilitating Reproducibility in Catalysis Research with Managed Workflows and RO-Crates: A Galaxy Case Study. *ChemCatChem*, **n/a**, e202401676.
111. Clostridium tetani bacteraemia in the plague area in France: Two cases (2025) *Current Research in Microbial Sciences*, **8**, 100339.
112. Exome sequencing: a tool for the diagnosis of hereditary retinal dystrophies in Mexican patients (2025) *Scilit*.
113. Nortje,N.Q. *et al.* (2025) Molecular modelling and experimental validation of mangiferin and its related compounds as quorum sensing modulators of Pseudomonas aeruginosa. *Archives of Microbiology*, **207**, 53.
114. Omenge,K. *et al.* (2025) SEOR2 in Arabidopsis mediates Ca2+ dependent defense against phytoplasmas and reduction of plant growth. *Scientific Reports*, **15**, 17829.
115. Paiva,A.M.O. *et al.* (2025) The l,d-transpeptidation pathway is inhibited by antibiotics of the β-lactam class in Clostridioides difficile. *iScience*, **28**.
116. Panagiotopoulou,D. *et al.* (2025) The Quorum Sensing Regulated sRNA Lrs1 Is Involved in the Adaptation to Low Iron in Pseudomonas aeruginosa. *Environmental Microbiology Reports*, **17**, e70090.
117. Patil,K.B. (2025) Investigating the molecular mechanisms involved in the developmental assembly of the mushroom body calyx in \\textlessem\\textgreaterDrosophila melanogaster\\textless/em\\textgreater.
118. Perez,J.M. *et al.* (2025) Investigating proteogenomic divergence in patient-derived xenograft models of ovarian cancer. *Scientific Reports*, **15**, 813.
119. Petroll,R. *et al.* (2025) Enhanced sensitivity of TAPscan v4 enables comprehensive analysis of streptophyte transcription factor evolution. *The Plant Journal*, **121**, e17184.
120. Phumthanakorn,N. and Thanasak,J. (2025) Prevalence and Antimicrobial Resistance of Methicillin-Resistant and Methicillin-Susceptible Staphylococcus in Small- to Medium-Scale and Large-Scale Dairy Farms in Thailand. *Translational Animal Science*, txaf081.
121. Pishan,M. *et al.* (2025) The Role of Rhodococcus Opacus R7 Laccase-Like Multicopper Oxidase (Lmco1) Enzyme In Biodegradation of Polyethylene Polymer.
122. Pitt,A. *et al.* (2025) Aquirufa esocilacus sp. nov., Aquirufa originis sp. nov., Aquirufa avitistagni, and Aquirufa echingensis sp. nov. discovered in small freshwater habitats in Austria during a citizen science project. *Archives of Microbiology*, **207**, 71.
123. Pitt,A. *et al.* (2025) Biodiversity of strains belonging to the freshwater genus Aquirufa in a riparian forest restoration area in Salzburg, Austria, with a focus on the description of Aquirufa salirivi sp. nov. and Aquirufa novilacunae sp. nov. *International Microbiology*.
124. Ranganathan,R. *et al.* (2025) Targets of the transcription factor Six1 identify previously unreported candidate deafness genes. *Development*, **152**, dev204533.
125. Ranta,K. *et al.* (2025) Isolation and characterization of fMGyn-Pae01, a phiKZ-like jumbo phage infecting Pseudomonas aeruginosa. *Virology Journal*, **22**, 55.
126. Rashid,M.H. *et al.* (2025) Shotgun metagenomic composition, microbial interactions and functional insights into the uterine microbiome of postpartum dairy cows with clinical and subclinical endometritis. *Scientific Reports*, **15**, 18274.
127. Raymond,J.H. *et al.* (2025) Targeting GRPR for sex hormone-dependent cancer after loss of E-cadherin. *Nature*, 1–9.
128. redonion (2025) Clinical validation of 13-gene DNA methylation analysis in oral brushing samples for detection of oral carcinoma: An Italian multicenter study. *TomaLab*.
129. Rehm,T.M. *et al.* (2025) A splice donor in E6 influences keratinocyte immortalization by beta-HPV49. *Journal of Virology*, **0**, e01640–24.
130. Ritson,M. *et al.* (2025) Repeated Low-Level Inflammatory Challenge Leads to Alterations in the TNF-CXCL10 Signalling Pathway in Mouse Cerebral Endothelial Cells In Vitro. *Journal of Neurochemistry*, **169**, e70130.
131. Ruider,I. *et al.* (2025) Accelerated maturation of branched organoids confined in collagen droplets.
132. Salem,S. *et al.* (2025) Comparative genomics of Acinetobacter baumannii from Egyptian healthcare settings reveals high-risk clones and resistance gene mobilization. *BMC Infectious Diseases*, **25**, 803.
133. Santos,A.F.B. *et al.* (2025) Wastewater Metavirome Diversity: Exploring Replicate Inconsistencies and Bioinformatic Tool Disparities. *International Journal of Environmental Research and Public Health*, **22**, 707.
134. Seah,M.K.Y. *et al.* (2025) Maternal PRDM10 activates essential genes for oocyte-to-embryo transition. *Nature Communications*, **16**, 1939.
135. Semail,N. *et al.* (2025) Genomic dataset of eighteen *Burkholderia pseudomallei* strains isolated from clinical and environmental settings in Malaysia. *Current Research in Microbial Sciences*, **8**, 100397.
136. Sharma,S. *et al.* (2025) The cytokinesis associated proteins CITK and ASPM-1 regulate neuronal microtubule dynamics and polarity in C. elegans.
137. Sherwood,O.L. *et al.* (2025) Transcriptional signatures associated with waterlogging stress responses and aerenchyma formation in barley root tissue. *Annals of Botany*, mcaf104.
138. Shiekh Suliman,N. *et al.* (2025) Taxonomic refinement of Bacillus thuringiensis. *Frontiers in Microbiology*, **16**.
139. Inspired by molecular dynamic simulation, exploring chemical constituents of alcoholic extract of Garuga pinnata computationally as inhibitors of GluN2B-containing NMDA receptors (2025) *Journal of Biomolecular Structure and Dynamics*, **0**, 1–15.
140. Silva,P.O. *et al.* (2025) Exploring the genomic diversity and breeding applications of the Solanum sessiliflorum transcriptome via phylogenetic analysis. *Crop Science*, **65**, e70036.
141. Simonis,A. *et al.* (2025) Persistent epigenetic memory of SARS-CoV-2 mRNA vaccination in monocyte-derived macrophages. *Molecular Systems Biology*, 1–20.
142. Sliti,A. *et al.* (2025) Whole Genome Sequencing and *In Silico* Analysis of the Safety and Probiotic Features of *Lacticaseibacillus paracasei* FMT2 Isolated from Fecal Microbiota Transplantation (FMT) Capsules. *Microbial Pathogenesis*, 107405.
143. Soumia,P.S. *et al.* (2025) Unravelling the complete mitochondrial genomes of Thrips tabaci Lindeman and Thrips parvispinus Karny (Thysanoptera: Thripidae) and their phylogenetic implications. *Frontiers in Insect Science*, **5**.
144. Souza,L.H.B. *et al.* (2025) New Insights into the Sex Chromosome Evolution of the Common Barker Frog Species Complex (Anura, Leptodactylidae) Inferred from Its Satellite DNA Content. *Biomolecules*, **15**, 876.
145. Sterling,M.J. *et al.* (2025) A revision of the hitherto neglected genus Topiris Walker, 1863 (Lepidoptera, Xyloryctidae) with taxonomic notes on the genus Athrypsiastis Meyrick, 1910. *ZooKeys*, **1229**, 297–368.
146. Strateva,T.V. *et al.* (2025) First Detection and Genomic Characterization of Linezolid-Resistant Enterococcus faecalis Clinical Isolates in Bulgaria. *Microorganisms*, **13**, 195.
147. Strepis,N. *et al.* (2025) BenchAMRking: a Galaxy-based platform for illustrating the major issues associated with current antimicrobial resistance (AMR) gene prediction workflows. *BMC Genomics*, **26**, 27.
148. Su,J. *et al.* (2025) C13-Deacylase from Nocardioides albus Resp. Streptomyces sp., Catalyzing Side Chain Hydrolysis on the Taxane Core. *ChemCatChem*, **n/a**, e00567.
149. Suresh,R. *et al.* (2025) Comparative genomics reveals genetic diversity and differential metabolic potentials of the species of Arachnia and suggests reclassification of Arachnia propionica E10012 (=NBRC\_14587) as novel species. *Archives of Microbiology*, **207**, 93.
150. Sweatman,E. *et al.* (2025) SETD1A-dependent EME1 transcription drives PARPi sensitivity in HR deficient tumour cells. *British Journal of Cancer*, 1–13.
151. Talubo,N.D.D. *et al.* (2025) QSAR-Based Drug Repurposing and RNA-Seq Metabolic Networks Highlight Treatment Opportunities for Hepatocellular Carcinoma Through Pyrimidine Starvation. *Cancers*, **17**, 903.
152. Tamang,J.P. *et al.* (2025) Analysis of meta-transcriptomics and identification of genes linked to bioactive peptides and vitamins in Indonesian *tempe*. *Food Research International*, **202**, 115757.
153. Tang,W. *et al.* (2025) Denser Mitogenomic Sampling for Exploring the Phylogeny of Tellinoidea (Mollusca: Bivalvia). *Diversity*, **17**, 303.
154. Tascini,C. *et al.* (2025) OXA-carbapenemases and mutations within PBPs in ST2 carbapenem-resistant *A. baumannii*: evaluating the efficacy of cefiderocol and ampicillin-sulbactam combination therapy. *Journal of Global Antimicrobial Resistance*.
155. Teng,Y.-H. *et al.* (2025) TGF-β signaling redirects Sox11 gene regulatory activity to promote partial EMT and collective invasion of oncogenically transformed intestinal organoids. *Oncogenesis*, **14**, 1–14.
156. Thompson,R.M. *et al.* (2025) From pollution to reforestation: the hidden microbiome of Alnus glutinosa nodules over 30 years. *Scientific Reports*, **15**, 23373.
157. Trifonova,A. *et al.* (2025) Expansion of SARS-CoV-2 mutations in patient with B-cell lymphoma and rare combination of ACE2, TLR4, DDX58 and IFIH1 variations: A retrospective analysis of the virus-host interplay. *Clinical Immunology Communications*, **7**, 47–54.
158. Tsangaras,K. *et al.* (2025) Crossing Wallace’s line: an evolutionarily young gibbon ape leukemia virus like endogenous retrovirus identified from the Philippine flying lemur (Cynocephalus volans). *Scientific Reports*, **15**, 9790.
159. Uluar,O. *et al.* (2025) Mitogenomics of Psorodonotus ebneri Brunner von Wattenwyl, 1861 (Orthoptera: Tettigoniidae): Selection profile and patterns of intraspecific and interspecific divergence. *Hacettepe Journal of Biology and Chemistry*, **53**, 81–96.
160. Valer,J.A. *et al.* (2025) PI3Kα inhibition blocks osteochondroprogenitor specification and the hyper-inflammatory response to prevent heterotopic ossification. *eLife*, **12**, RP91779.
161. Varga,Z. *et al.* (2025) Transposon insertion causes *ctnnb2* transcript instability that results in the maternal effect zebrafish *ichabod* (*ich*) mutation. *Biochimica et Biophysica Acta (BBA) - Gene Regulatory Mechanisms*, **1868**, 195104.
162. Velasquez,R. *et al.* (2025) An emerging Platynota sp. (Lepidoptera: Tortricidae) infesting blueberry (Vaccinium corymbosum) in the central coast of Peru. *Frontiers in Insect Science*, **5**.
163. Vidal-Quist,J.C. *et al.* (2025) Stage-specific transcriptomic analysis reveals insights into the development, reproduction and biological function of allergens in the European house dust mite Dermatophagoides pteronyssinus. *BMC Genomics*, **26**, 527.
164. Vila-Luna,S.E. *et al.* (2025) The draft genome of ‘Candidatus Phytoplasma palmae’ strain LY-C2, the phytoplasma associated with coconut lethal yellowing disease, reveals insights into its biological characteristics. *World Journal of Microbiology and Biotechnology*, **41**, 242.
165. Virgili,R. *et al.* (2025) Paedomorphic adaptations in a new Heterostigma species: a novel strategy for ascidians to live in soft-bottom habitats. *Invertebrate Systematics*, **39**, NULL–NULL.
166. Ehr,A. von *et al.* (2025) Experimental evidence on colchicine’s mode of action in human carotid artery plaques. *Atherosclerosis*, **406**, 119239.
167. Wahlberg,E. (2025) Genome Skimming of Thysanoptera (Arthropoda, Insecta) and Its Taxonomic and Systematic Applications. *Diversity*, **17**, 226.
168. Wambreuse,N. *et al.* (2025) Morpho-functional characterisation of cœlomocytes in the aquacultivated sea cucumber *Holothuria scabra*: From cell diversity to transcriptomic immune response. *Fish & Shellfish Immunology*, **158**, 110144.
169. Wasfy,R.M. *et al.* (2025) First Evidence of Candidate Phyla Radiation in Chronic Hepatitis B Virus-Infected Patients: A Case-Control Metagenomic Study.
170. Wicaksono,A. *et al.* (2025) Hairpin in a haystack: In silico identification and characterization of plant-conserved microRNA in Rafflesiaceae. *Open Life Sciences*, **20**.
171. Winkler,M.A. and Pan,A.A. (2025) Molecular and Genetic Analysis of the Increased Number of Genes for Trypanosoma cruzi Microtubule Associated Proteins in the Class Kinetoplastida. *Pathogens*, **14**, 476.
172. Wolf,J. *et al.* (2025) A proteotranscriptomic approach to dissect the molecular landscape of human retinoblastoma. *Frontiers in Oncology*, **15**, 1571702.
173. Wu,S. *et al.* (2025) An Atlas of Thyroid Hormone Responsive Genes in Adult Mouse Hypothalamus. *Endocrinology*, **166**, bqaf084.
174. Wu,Q. *et al.* (2025) Comparative Genomic and Mitochondrial Phylogenetic Relationships of Ovulidae (Mollusca: Gastropoda) Along the Chinese Coast. *Ecology and Evolution*, **15**, e71224.
175. Wu,X. *et al.* (2025) Differential Mitochondrial Genome Expression of Four Skink Species Under High-Temperature Stress and Selection Pressure Analyses in Scincidae. *Animals*, **15**, 999.
176. Wu,J. *et al.* (2025) Genome analysis of colistin-resistant Salmonella isolates from human sources in Guizhou of southwestern China, 2019–2023. *Frontiers in Microbiology*, **16**.
177. Yang,Y.-B. *et al.* (2025) The complete mitochondrial genome of the snapping shrimp, Alpheus brevicristatus De Haan, 1844 (Crustacea, Decapoda, Alpheidae). *Mitochondrial DNA Part B*, **10**, 554–557.
178. Yao,J. *et al.* (2025) Genome and transcriptome analysis of the lignite-degrading *Trichoderma* cf. *simile* WF8 strain highlights potential degradation mechanisms. *International Biodeterioration & Biodegradation*, **198**, 105997.
179. Yerlikaya,B.A. *et al.* (2025) Enhanced drought and salt stress tolerance in Arabidopsis via ectopic expression of the PvMLP19 gene. *Plant Cell Reports*, **44**, 130.
180. Yu,Y.-H. *et al.* (2025) Pseudomonas Species Isolated From Lotus Nodules Are Genetically Diverse and Promote Plant Growth. *Environmental Microbiology*, **27**, e70066.
181. Zakir,M. *et al.* (2025) Cohesive data analysis for the identification of prognostic hub genes and significant pathways associated with HER2 + and TN breast cancer types. *Scientific Reports*, **15**, 23675.
182. Zhang,X. *et al.* (2025) IRF4 expression by NK precursors predetermines exhaustion of NK cells during tumor metastasis. *Nature Immunology*, **26**, 1062–1073.
183. Zubaer,A. (2025) Genome mining of Leptographium wingfieldii, an invasive species in Canadian forests, and related taxa in the order Ophiostomatales for the characterization of secondary metabolites and ribozymes.

### **2024**

1.  鲍泽华 *et al.* (2024) 一种大规模并行dna序列编辑方法及应用.
2.  AbuSaleh,L. *et al.* (2024) Genetic Polymorphisms of Angiotensin-Converting Enzyme 1 (ACE1) and ACE2 Associated With Severe Acute Respiratory Syndrome COVID-19 in the Palestinian Population. *Cureus*, **16**.
3.  Aerts,T. *et al.* (2024) Altered socio-affective communication and amygdala development in mice with protocadherin10-deficient interneurons. *Open Biology*, **14**, 240113.
4.  Aguirre Pranzoni,C. *et al.* (2024) Biofoams with untapped enzymatic potential produced from beer bagasse by indigenous fungal strains. *Bioresource Technology*, **406**, 131037.
5.  Aguirre Pranzoni,C. *et al.* (2024) Biofoams with Untapped Enzymatic Potential Produced from Beer Bagasse by Indigenous Fungal Strains.
6.  Akpinar,Z. and Karaoglu,H. (2024) Characterization of a highly thermostable recombinant xylanase from *Anoxybacillu*s *ayderensis*. *Protein Expression and Purification*, **219**, 106478.
7.  Alawi,M. *et al.* (2024) Private and well drinking water are reservoirs for antimicrobial resistant bacteria. *npj Antimicrobials and Resistance*, **2**, 1–16.
8.  Albrecht,C. *et al.* (2024) Amplicon-Based Bisulfite Conversion-NGS DNA Methylation Analysis Protocol. In, Jeltsch,A. and Rots,M.G. (eds), *Epigenome Editing: Methods and Protocols*. Springer US, New York, NY, pp. 405–418.
9.  Ali,M.A. *et al.* (2024) Bioinformatics and Computational Biology. In, Ijaz,S. *et al.* (eds), *Trends in Plant Biotechnology*. Springer Nature, Singapore, pp. 281–334.
10. AlJindan,R. *et al.* (2024) Phenomics and genomic features of *Enterococcus avium* IRMC1622a isolated from a clinical sample of hospitalized patient. *Journal of Infection and Public Health*.
11. Andriyanov,P.A. *et al.* (2024) Genomic analysis of multidrug-resistant Delftia tsuruhatensis isolated from raw bovine milk. *Frontiers in Microbiology*, **14**.
12. Arai,H. *et al.* (2024) Two male-killing Wolbachia from Drosophila birauraia that are closely related but distinct in genome structure. *Royal Society Open Science*, **11**, 231502.
13. Argenta,N. *et al.* (2024) American lobster (Homarus americanus) hepatopancreas transcriptome reveals the significance of chitin-related genes during impoundment shell disease. *FACETS*, **9**, 1–10.
14. Aribisala,J.O. *et al.* (2024) In silico exploration of phenolics as modulators of penicillin binding protein (PBP) 2× of Streptococcus pneumoniae. *Scientific Reports*, **14**, 8788.
15. Arlat,A. *et al.* (2024) Generation of functionally active resident macrophages from adipose tissue by 3D cultures. *Frontiers in Immunology*, **15**.
16. Arnold,N.D. (2024) Unlocking a Potent Chitin Saccharification System in a Novel Bacterium Through Omics and Bioinformatics.
17. Arshad,A. *et al.* (2024) Comparative study of chloroplast genomes across seven Salacca species. *Biodiversitas Journal of Biological Diversity*, **25**.
18. Asiri,A. (2024) In-Silico Perspectives on the Potential Therapeutic Aids of Hesperetin Derivatives for Lung Cancer. *Advancements in Life Sciences*, **11**, 878–886.
19. Atac,D. *et al.* (2024) Identification and Characterization of ATOH7-Regulated Target Genes and Pathways in Human Neuroretinal Development. *Cells*, **13**, 1142.
20. Bahrami,B. *et al.* (2024) Integrated analysis of transcriptome and epigenome reveals ENSR00000272060 as a potential biomarker in gastric cancer. *Epigenomics*, **16**, 159–173.
21. Balcke,G.U. *et al.* (2024) Coordinated metabolic adaptation of Arabidopsis thaliana to high light. *The Plant Journal*, **120**, 387–405.
22. Barreira,E.M.da C. (2024) Predictability of genomic evolution of populations with contrasting initial history.
23. Bastide,H. *et al.* (2024) The genome of the blind bee louse fly reveals deep convergences with its social host and illuminates Drosophila origins. *Current Biology*.
24. Bawin,T. *et al.* (2024) Cuscuta campestris fine-tunes gene expression during haustoriogenesis as an adaptation to different hosts. *Plant Physiology*, **194**, 258–273.
25. Becker,A.-L. *et al.* (2024) Correlation of Immunomodulatory Cytokines with Tumor Volume and Cerebrospinal Fluid in Vestibular Schwannoma Patients. *Cancers*, **16**, 3002.
26. Beerling,D.J. *et al.* (2024) Enhanced weathering in the US Corn Belt delivers carbon removal with agronomic benefits. *Proceedings of the National Academy of Sciences*, **121**, e2319436121.
27. Berlanga,M. *et al.* (2024) Biodiversity and poten al func onality of biofilmsediment biotope in La Muerte lagoon, Monegros desert, Spain. *Frontiers in Ecology and Evolution*, **12**.
28. Besson,B. *et al.* (2024) Pan-flavivirus analysis reveals sfRNA-independent, 3′ UTR-biased siRNA production from an insect-specific flavivirus. *Journal of Virology*, **0**, e01215–24.
29. Bianconi,I. *et al.* (2024) Characterization of Verona Integron-Encoded Metallo-β-Lactamase-Type Carbapenemase-Producing Escherichia coli Isolates Collected over a 16-Year Period in Bolzano (Northern Italy). *Microbial Drug Resistance*, **30**, 91–100.
30. Bianconi,I. *et al.* (2024) Disseminated Echovirus 11 infection in a newborn in the Province of Bolzano, Italy. *Infection*.
31. Bihani,S. *et al.* (2024) Metaproteomics for Coinfections in the Upper Respiratory Tract: The Case of COVID-19. In, Salerno,C. (ed), *Metaproteomics: Methods and Protocols*. Springer US, New York, NY, pp. 165–185.
32. Bloor,S. *et al.* (2024) RNA binding by Periphilin plays an essential role in initiating silencing by the HUSH complex. *Nucleic Acids Research*, gkae1165.
33. Bode,C. *et al.* (2024) Catecholamine treatment induces reversible heart injury and cardiomyocyte gene expression. *Intensive Care Medicine Experimental*, **12**, 48.
34. Bode,C. *et al.* (2024) Dynamics of cardiomyocyte gene expression and reversibility of catecholamine-induced heart injury.
35. Boeckman,J. *et al.* (2024) Phage DNA Extraction, Genome Assembly, and Genome Closure. In, Tumban,E. (ed), *Bacteriophages: Methods and Protocols*, Methods in Molecular Biology. Springer US, New York, NY, pp. 125–144.
36. Bogguri,C. *et al.* (2024) Biphasic response of human iPSC-derived neural network activity following exposure to a sarin-surrogate nerve agent. *Frontiers in Cellular Neuroscience*, **18**.
37. Boneva,S.K. *et al.* (2024) The multifaceted role of vitreous hyalocytes: Orchestrating inflammation, angiomodulation and erythrophagocytosis in proliferative diabetic retinopathy. *Journal of Neuroinflammation*, **21**, 297.
38. Boyer,T. and Neronov,A. (2024) Pulsar timing array constraints on the cosmological magnetic field from quark confinement epoch.
39. Brink,A.van den (2024) Identification of the Expression Patterns of Fatty Acid Oxidation Genes in a Heterogenic Cardiomyopathy Patient Cohort.
40. Camacho-Beltrán,E. *et al.* (2024) Complete genome sequence of the Microbacterium enclense bacteriophage phiMiGM15. *Microbiology Resource Announcements*, **0**, e00302–24.
41. Candeliere,F. *et al.* (2024) Genomic and functional analysis of the mucinolytic species Clostridium celatum, Clostridium tertium, and Paraclostridium bifermentans. *Frontiers in Microbiology*, **15**.
42. Capitani,V. *et al.* (2024) In vivo evolution to hypermucoviscosity and ceftazidime/avibactam resistance in a liver abscess caused by Klebsiella pneumoniae sequence type 512. *mSphere*, **9**, e00423–24.
43. Carval,T. *et al.* (2024) Pangeo environment in Galaxy Earth System supported by Fair-Ease Copernicus Meetings.
44. Carvalho,J.V.R.P. *et al.* (2024) Genomics and evolutionary analysis of Chlorella variabilis-infecting viruses demarcate criteria for defining species of giant viruses. *Journal of Virology*, **0**, e00361–24.
45. Casal,J.J. *et al.* (2024) Plant Thermosensors.
46. Castellana,S. *et al.* (2024) Pannonibacter anstelovis sp. nov. Isolated from Two Cases of Bloodstream Infections in Paediatric Patients. *Microorganisms*, **12**, 799.
47. Castillo-Villamizar,G.A. *et al.* (2024) Unveiling soil bacterial ecosystems in andean citrus orchards of Santander, Colombia. *Frontiers in Ecology and Evolution*, **12**.
48. Ceylan,F. *et al.* (2024) Whole-genome resequencing identifies exonic single-nucleotide variations in terpenoid biosynthesis genes of the medicinal and aromatic plant common sage (Salvia officinalis L.). *Genetic Resources and Crop Evolution*.
49. Chatti,K. *et al.* (2024) Genome-Wide Analysis of the Common Fig (Ficus carica L.) R2R3-MYB Genes Reveals Their Structure, Evolution, and Roles in Fruit Color Variation. *Biochemical Genetics*.
50. Chen,X. *et al.* (2024) Canonical androgen response element motifs are tumor suppressive regulatory elements in the prostate. *Nature Communications*, **15**, 10675.
51. Chetverikov,P.E. *et al.* (2024) Molecular Phylogenetics and Light Microscopy Reveal “True” and “False” Calacarines and Novel Genital Structures in Gall Mites (Acariformes, Eriophyoidea). *Forests*, **15**, 329.
52. Chiappa,G. *et al.* (2024) Potential Ancestral Conoidean Toxins in the Venom Cocktail of the Carnivorous Snail Raphitoma purpurea (Montagu, 1803) (Neogastropoda: Raphitomidae). *Toxins*, **16**, 348.
53. Choudalakis,M. *et al.* (2024) RepEnTools: an automated repeat enrichment analysis package for ChIP-seq data reveals hUHRF1 Tandem-Tudor domain enrichment in young repeats. *Mobile DNA*, **15**, 6.
54. Cosenza-Contreras,M. *et al.* (2024) Proteometabolomics of initial and recurrent glioblastoma highlights an increased immune cell signature with altered lipid metabolism. *Neuro-Oncology*, **26**, 488–502.
55. Costa,R.A. *et al.* (2024) The Unique Specialization of Olfaction in the Senegalese Sole (Solea Senegalensis). Smelling in Co2 Acidified Water Triggers Nostril Specific Immune Processes.
56. Crespo,R. *et al.* (2024) PCID2 dysregulates transcription and viral RNA processing to promote HIV-1 latency. *iScience*, **27**, 109152.
57. Croney,K. (2024) Revealing Binding and Unbinding Pathways of Small Molecules and Peptides to Enzymes with Enhanced Sampling Methods. *WWU Graduate School Collection*.
58. Darino,M. *et al.* (2024) Identification and functional characterisation of a locus for target site integration in Fusarium graminearum. *Fungal Biology and Biotechnology*, **11**, 2.
59. Azevedo,B.L. de *et al.* (2024) The genomic and phylogenetic analysis of Marseillevirus cajuinensis raises questions about the evolution of Marseilleviridae lineages and their taxonomical organization. *Journal of Virology*, **0**, e00513–24.
60. Melo,S.M.F. de *et al.* (2024) The mitochondrial genome sequence of Syagrus coronata (Mart.) Becc. (Arecaceae) is characterized by gene insertion within intergenic spaces. *Tree Genetics & Genomes*, **20**, 10.
61. De Oliveira,I.B. *et al.* (2024) Apoplastomes of contrasting cacao genotypes to witches’ broom disease reveals differential accumulation of PR proteins. *Frontiers in Plant Science*, **15**.
62. Souza,F.D. de *et al.* (2024) Mitochondrial genome of Hancornia speciosa gomes: intergenic regions containing retrotransposons and predicted genes. *Molecular Biology Reports*, **51**, 132.
63. Souza,Y.P.A. de *et al.* (2024) The seeds of Plantago lanceolata comprise a stable core microbiome along a plant richness gradient. *Environmental Microbiome*, **19**, 11.
64. Dederichs,T.-S. *et al.* (2024) Nonpreferential but Detrimental Accumulation of Macrophages With Clonal Hematopoiesis-Driver Mutations in Cardiovascular Tissues—Brief Report. *Arteriosclerosis, Thrombosis, and Vascular Biology*, **44**, 690–697.
65. Dehghanian,F. *et al.* (2024) ZFP982 confers mouse embryonic stem cell characteristics by regulating expression of *Nanog*, *Zfp42,* and *Dppa3*. *Biochimica et Biophysica Acta (BBA) - Molecular Cell Research*, **1871**, 119686.
66. Delandre,O. *et al.* (2024) Long-Read Sequencing and De Novo Genome Assembly Pipeline of Two Plasmodium falciparum Clones (Pf3D7, PfW2) Using Only the PromethION Sequencer from Oxford Nanopore Technologies without Whole-Genome Amplification. *Biology*, **13**, 89.
67. Deng,L. *et al.* (2024) Atlas of cardiac endothelial cell enhancer elements linking the mineralocorticoid receptor to pathological gene expression. *Science Advances*, **10**, eadj5101.
68. Deng,L. *et al.* (2024) Massively parallel CRISPR-assisted homologous recombination enables saturation editing of full-length endogenous genes in yeast. *Science Advances*, **10**, eadj9382.
69. Depari,E.K. *et al.* (2024) Long-read datasets of Kayu Bawang (*Azadirachta excelsa* (Jack) Jacobs) from 3 different identified seed stands in Bengkulu (Sumatra), Indonesia and its phylogenetic relationships.
70. de Souza,Y.P.A. *et al.* (2024) The effect of successive summer drought periods on bacterial diversity along a plant species richness gradient. *FEMS Microbiology Ecology*, **100**, fiae096.
71. Diz-Küçükkaya,R. *et al.* (2024) JAK2V617F Mutation in Endothelial Cells of Patients with Atherosclerotic Carotid Disease. *Turkish Journal of Haematology: Official Journal of Turkish Society of Haematology*, **41**, 167–174.
72. Donátová,K. *et al.* (2024) Changes in the Expression of Proteins Associated with Neurodegeneration in the Brains of Mice after Infection with Influenza A Virus with Wild Type and Truncated NS1. *International Journal of Molecular Sciences*, **25**, 2460.
73. Dossmann,L. *et al.* (2024) Specific DNMT3C flanking sequence preferences facilitate methylation of young murine retrotransposons. *Communications Biology*, **7**, 1–12.
74. Duque-Afonso,J. *et al.* (2024) Identification of epigenetic modifiers essential for growth and survival of AML1/ETO-positive leukemia. *International Journal of Cancer*, **155**, 2068–2079.
75. Edet,O.U. *et al.* (2024) Genomic analysis of a spontaneous unifoliate mutant reveals gene candidates associated with compound leaf development in Vigna unguiculata \[L\] Walp. *Scientific Reports*, **14**, 10654.
76. Eggenhofer,F. and Siederdissen,C. Höner zu (2024) Evolutionary Structure Conservation and Covariance Scores. In, Lorenz,R. (ed), *RNA Folding: Methods and Protocols*. Springer US, New York, NY, pp. 255–284.
77. Ehle,C. *et al.* (2024) Downregulation of HNF4A enables transcriptomic reprogramming during the hepatic acute-phase response. *Communications Biology*, **7**, 1–14.
78. Epihov,D.Z. *et al.* (2024) Iron Chelation in Soil: Scalable Biotechnology for Accelerating Carbon Dioxide Removal by Enhanced Rock Weathering. *Environmental Science & Technology*, **58**, 11970–11987.
79. Ercole,T.G. *et al.* (2024) Unveiling Agricultural Biotechnological Prospects: The Draft Genome Sequence of Stenotrophomonas geniculata LGMB417. *Current Microbiology*, **81**, 247.
80. Erkelenz,S. *et al.* (2024) Rbm3 deficiency leads to transcriptome-wide splicing alterations. *RNA Biology*, **21**, 1–13.
81. Fabian-Morales,G.E. *et al.* (2024) Identification of Pathogenic Copy Number Variants in Mexican Patients With Inherited Retinal Dystrophies Applying an Exome Sequencing Data-Based Read-Depth Approach. *Molecular Genetics & Genomic Medicine*, **12**, e70019.
82. Faulstich,N.G. *et al.* (2024) Evidence for phosphate-dependent control of symbiont cell division in the model anemone *Exaiptasia diaphana*. *mBio*, e01059–24.
83. Fernandes,D.R. (2024) LAMA2-CMD: establishment of a new gene therapy strategy using an in vitro model.
84. Ferreira,M.M. *et al.* (2024) TcSERPIN, an inhibitor that interacts with cocoa defense proteins and has biotechnological potential against human pathogens. *Frontiers in Plant Science*, **15**.
85. Fischer,J. *et al.* (2024) Expanding the Scope of Adenoviral Vectors by Utilizing Novel Tools for Recombination and Vector Rescue. *Viruses*, **16**, 658.
86. Flores Orozco,D. (2024) Evaluation of the long-term effects of anaerobic digestion on bovine manure resistomes and mobilomes and the molecular and microbial mechanisms involved.
87. Fonseca,J.S.da (2024) Mineração genômica e identificação de moléculas com potencial biotecnológico da microbiota amazônica.
88. Galià-Camps,C. *et al.* (2024) Jumping through hoops: Structural rearrangements and accelerated mutation rates on Dendrodorididae (Mollusca: Nudibranchia) mitogenomes rumble their evolution. *Molecular Phylogenetics and Evolution*, **201**, 108218.
89. Galvis,J. *et al.* (2024) DIMet: An open-source tool for Differential analysis of targeted Isotope-labeled Metabolomics data. *Bioinformatics (Oxford, England)*, btae282.
90. Gao,C. *et al.* (2024) Land use intensity differently affects soil microbial functional communities in arable fields. *Applied Soil Ecology*, **204**, 105723.
91. Garcia-Fernandez,A. *et al.* (2024) Antibiotic resistance, plasmids, and virulence-associated markers in human strains of Campylobacter jejuni and Campylobacter coli isolated in Italy. *Frontiers in Microbiology*, **14**.
92. Gavalda-Garcia,J. *et al.* (2024) bio2Byte Tools deployment as a Python package and Galaxy tool to predict protein biophysical properties.
93. Ghosh,A. *et al.* (2024) Mitogenomics providing new insights into the phylogenetic structure of subfamily Panchaetothripinae (Thripidae: Terebrantia). *Genetica*, **153**, 3.
94. Ghosh,A. *et al.* (2024) Suppressive cancer nonstop extension mutations increase C-terminal hydrophobicity and disrupt evolutionarily conserved amino acid patterns. *Nature Communications*, **15**, 9209.
95. Giroud,S. *et al.* (2024) Torpor and Hibernation: Metabolic and Physiological Paradigms Frontiers Media SA.
96. Giufrè,M. *et al.* (2024) Detection of KPC-216, a Novel KPC-3 Variant, in a Clinical Isolate of Klebsiella pneumoniae ST101 Co-Resistant to Ceftazidime-Avibactam and Cefiderocol. *Antibiotics*, **13**, 507.
97. Glærum,I.L. *et al.* (2024) Postnatal persistence of hippocampal Cajal-Retzius cells has a crucial role in the establishment of the hippocampal circuit. *Development*, **151**, dev202236.
98. Godbole,S. *et al.* (2024) Multiomic profiling of medulloblastoma reveals subtype-specific targetable alterations at the proteome and N-glycan level. *Nature Communications*, **15**, 6237.
99. Goglio,A. *et al.* (2024) The performance of biochar waste-derived electrodes in different bio-electrochemical applications. *Journal of Power Sources*, **625**, 235623.
100. Gress,C. *et al.* (2024) Prostaglandin D2 receptor 2 downstream signaling and modulation of type 2 innate lymphoid cells from patients with asthma. *PLOS ONE*, **19**, e0307750.
101. Gress,C. *et al.* (2024) Transcriptomic characterization of the human segmental endotoxin challenge model. *Scientific Reports*, **14**, 1721.
102. Grève,P. *et al.* (2024) Three feminizing Wolbachia strains in a single host species: comparative genomics paves the way for identifying sex reversal factors. *Frontiers in Microbiology*, **15**.
103. Gu,Y. *et al.* (2024) ProSwats: A Proxy-based Scientific Workflow Retrieval Approach by Bridging the Gap between Textual and Structural Semantics. In, *2024 IEEE International Conference on Web Services (ICWS)*., pp. 932–943.
104. Guo,Z.-Q. *et al.* (2024) Mitogenome-Based Phylogeny with Divergence Time Estimates Revealed the Presence of Cryptic Species within Heptageniidae (Insecta, Ephemeroptera). *Insects*, **15**, 745.
105. Häkkänen,T. *et al.* (2024) Molecular characteristics of *Cryptosporidium* spp. in human cases in five Finnish hospital districts during 2021: first findings of *Cryptosporidium mortiferum* (*Cryptosporidium* chipmunk genotype I) in Finland. *International Journal for Parasitology*, **54**, 225–231.
106. Hamdi,J. *et al.* (2024) Wall-Associated Kinase (WAK) and WAK-like Kinase Gene Family in Sugar Beet: Genome-Wide Characterization and In Silico Expression Analysis in Response to Beet Cyst Nematode (Heterodera schachtii Schmidt) Infection. *Journal of Plant Growth Regulation*.
107. Hashempour,A. *et al.* (2024) Reverse vaccinology approaches to design a potent multiepitope vaccine against the HIV whole genome: immunoinformatic, bioinformatics, and molecular dynamics approaches. *BMC Infectious Diseases*, **24**, 873.
108. He,Y. *et al.* (2024) A novel deep-benthic sea cucumber species of Benthodytes (Holothuroidea, Elasipodida, Psychropotidae) and its comprehensive mitochondrial genome sequencing and evolutionary analysis. *BMC Genomics*, **25**, 689.
109. Hecht,H. *et al.* (2024) Quantum chemistry based prediction of electron ionization mass spectra for environmental chemicals.
110. Heine,S. *et al.* (2024) Activation of the aryl hydrocarbon receptor improves allergen-specific immunotherapy of murine allergic airway inflammation: a novel adjuvant option? *Frontiers in Immunology*, **15**.
111. Herwibawa,B. *et al.* (2024) Association of a Specific OsCULLIN3c Haplotype with Salt Stress Responses in Local Thai Rice. *International Journal of Molecular Sciences*, **25**, 1040.
112. Hoffmann,U.A. *et al.* (2024) The role of the 5’ sensing function of ribonuclease E in cyanobacteria. *RNA Biology*.
113. Homchan,S. *et al.* (2024) A reproducible workflow for assembling the mitochondrial genome of Acheta domesticus (Orthoptera: Gryllidae). *Ecology and Evolution*, **14**, e11696.
114. Hossain,M.S. *et al.* (2024) Evaluation of novel pyridoxal isonicotinoyl hydrazone (PIH) derivatives as potential anti-tuberculosis agents: An in silico investigation. *International Journal of Quantum Chemistry*, **124**, e27381.
115. Hosseini,S.M. *et al.* (2024) Astrocytes originated from neural stem cells drive the regenerative remodeling of pathologic CSPGs in spinal cord injury. *Stem Cell Reports*, **0**.
116. Hosseinzadeh,S. and Hasanpur,K. (2024) Whole genome discovery of regulatory genes responsible for the response of chicken to heat stress. *Scientific Reports*, **14**, 6544.
117. Huang,H.-H. *et al.* (2024) Rs1347093 regulates microRNA-216/-217 expression and is associated with pancreatic cancer risk. *Pancreatology*.
118. Humphrey,S. *et al.* (2024) Genomic characterization of prophage elements in Clostridium clostridioforme: an understudied component of the intestinal microbiome. *Microbiology*, **170**, 001486.
119. Hwang,H.M. *et al.* (2024) Reduction of APOE accounts for neurobehavioral deficits in fetal alcohol spectrum disorders. *Molecular Psychiatry*, 1–17.
120. Imre,L. *et al.* (2024) Epigenetic modulation via the C-terminal tail of H2A.Z. *Nature Communications*, **15**, 9171.
121. Ipoutcha,T. *et al.* (2024) A synthetic biology approach to assemble and reboot clinically relevant Pseudomonas aeruginosa tailed phages. *Microbiology Spectrum*, **12**, e02897–23.
122. Ishola,O.A. *et al.* (2024) Comparative Metagenomic Analysis of Bacteriophages and Prophages in Gnotobiotic Mouse Models. *Microorganisms*, **12**, 255.
123. Jain,K. and Yadav,R. (2024) Human Metagenome Analysis with COVID-19 Infectious Disease. *Current Trends in Biotechnology and Pharmacy*, **18**, 1616–1628.
124. Jia,C. *et al.* (2024) *Salmonella* phylogenomics. In, Mokrousov,I. and Shitikov,E. (eds), *Phylogenomics*. Academic Press, pp. 267–281.
125. Joshi,S. and Srivastava,R. (2024) Physicochemical properties and biological efficacy of 30 DYRK2 Inhibitors for the treatment of prostate cancer. *Vietnam Journal of Chemistry*, **n/a**.
126. Joshi,S. and Srivastava,R. (2024) Tracing the pathways and mechanisms involved in medicinal uses of flaxseed with computational methods and bioinformatics tools. *Frontiers in Chemistry*, **11**.
127. Jovović,L. *et al.* (2024) De novo transcriptomes of cave and surface isopod crustaceans: insights from 11 species across three suborders. *Scientific Data*, **11**, 595.
128. Junge,M. *et al.* (2024) ATP-Gated P2X7-Ion Channel on Kidney-Resident Natural Killer T Cells and Memory T Cells in Intrarenal Inflammation. *Journal of the American Society of Nephrology*, 10.1681/ASN.0000000564.
129. Kaari,M. *et al.* (2024) Integrated genomic and functional analysis of *Streptomyces* sp. UP1A-1 for bacterial wilt control and solanaceae yield increase. *Gene Reports*, **37**, 102012.
130. Kahraman-Ilıkkan,Ö. (2024) Comparative genomics of four lactic acid bacteria identified with Vitek MS (MALDI-TOF) and whole-genome sequencing. *Molecular Genetics and Genomics*, **299**, 31.
131. Kalnytska,O. *et al.* (2024) SORCS2 activity in pancreatic α-cells safeguards insulin granule formation and release from glucose-stressed β-cells. *iScience*, **27**, 108725.
132. Kamajian,M. *et al.* (2024) Identification of effector candidates in *Bipolaris sorokiniana* and their expression profile analysis during pathogen-wheat interactions. *Physiological and Molecular Plant Pathology*, **133**, 102343.
133. Kandinov,I. *et al.* (2024) Mini-Multilocus Sequence Typing Scheme for the Global Population of Neisseria gonorrhoeae. *International Journal of Molecular Sciences*, **25**, 5781.
134. Karim,T. *et al.* (2024) In Silico Prediction of Antibacterial Activity of Quinolone Derivatives. *ChemistrySelect*, **9**, e202402780.
135. Kifle,B.A. *et al.* (2024) Shotgun metagenomic insights into secondary metabolite biosynthetic gene clusters reveal taxonomic and functional profiles of microbiomes in natural farmland soil. *Scientific Reports*, **14**, 15096.
136. Köhler,A.R. (2024) Novel approaches to investigate the cellular effects of epigenome modifications.
137. Kojima,Y. *et al.* (2024) Cytochrome P450 2J2 is required for the natural compound austocystin D to elicit cancer cell toxicity. *Cancer Science*.
138. Kostrykin,L. *et al.* (2024) Enhancing the image analysis community in Galaxy.
139. Kostrykin,L. and Rohr,K. (2024) Robust Graph Pruning for Efficient Segmentation and Cluster Splitting of Cell Nuclei Using Deformable Shape Models. In, *2024 IEEE International Symposium on Biomedical Imaging (ISBI)*., pp. 1–4.
140. Krämer,M. *et al.* (2024) Cyclic electron flow compensates loss of PGDH3 and concomitant stromal NADH reduction. *Scientific Reports*, **14**, 29274.
141. Kristen,M. and Helm,M. (2024) Method for the accurate quantification of non-coding rnas in minute quantities.
142. Kruk,M.E. *et al.* (2024) An integrated metaproteomics workflow for studying host-microbe dynamics in bronchoalveolar lavage samples applied to cystic fibrosis disease. *mSystems*, **0**, e00929–23.
143. Kruse,P. *et al.* (2024) Synaptopodin Regulates Denervation-Induced Plasticity at Hippocampal Mossy Fiber Synapses. *Cells*, **13**, 114.
144. Kumar,G. and Bhadury,P. (2024) Dataset of metagenomic profiles of human gut microbiome from frozen fecal samples sequenced using Illumina and ONT chemistries. *Data in Brief*, **57**, 110961.
145. Kumawat,K.L. *et al.* (2024) Association of Reproductive Phenology with Air Temperature in Almond (Prunus dulcis \[Mill.\] D.A. Webb) Cultivars Under Northwestern Himalayan Conditions. *Applied Fruit Science*, **66**, 581–588.
146. Lapp,T. *et al.* (2024) Transcriptional profiling specifies the pathogen-specific human host response to infectious keratitis. *Frontiers in Cellular and Infection Microbiology*, **13**.
147. Larivière,D. *et al.* (2024) Scalable, accessible and reproducible reference genome assembly and evaluation in Galaxy. *Nature Biotechnology*, 1–4.
148. Lasolle,H. *et al.* (2024) Dual targeting of MAPK and PI3K pathways unlocks redifferentiation of Braf-mutated thyroid cancer organoids. *Oncogene*, **43**, 155–170.
149. Laurette,P. *et al.* (2024) In Vivo Silencing of Regulatory Elements Using a Single AAV-CRISPRi Vector. *Circulation Research*, **134**, 223–225.
150. Leavitt,R.J. *et al.* (2024) Acute Hypoxia Does Not Alter Tumor Sensitivity to FLASH Radiation Therapy. *International Journal of Radiation Oncology\*Biology\*Physics*.
151. Lenz,M. *et al.* (2024) Transcriptomic and de novo proteomic analyses of organotypic entorhino-hippocampal tissue cultures reveal changes in metabolic and signaling regulators in TTX-induced synaptic plasticity. *Molecular Brain*, **17**, 78.
152. Li,Q. *et al.* (2024) tRNA regulation and amino acid usage bias reflect a coordinated metabolic adaptation in *Plasmodium falciparum*. *iScience*, 111167.
153. Liang,P. *et al.* (2024) Characterization of the angiomodulatory effects of Interleukin 11 cis- and trans-signaling in the retina. *Journal of Neuroinflammation*, **21**, 230.
154. Liang,Z. *et al.* (2024) PICKLE-mediated nucleosome condensing drives H3K27me3 spreading for the inheritance of Polycomb memory during differentiation. *Molecular Cell*, **84**, 3438–3454.e8.
155. Lin,B. *et al.* (2024) Characteristics and phylogenetic implications of the mitochondrial genome of a rare species, *Libellula melli*. *Gene Reports*, **36**, 101986.
156. Link,T. (2024) Characterization and habitat adaptation of \\textlessem\\textgreaterTetragenococcus halophilus\\textless/em\\textgreater and \\textlessem\\textgreaterDebaryomyces hansenii\\textless/em\\textgreater from a lupine seasoning sauce fermentation.
157. López,M.-E. *et al.* (2024) Epigenomic and transcriptomic persistence of heat stress memory in strawberry (Fragaria vesca). *BMC Plant Biology*, **24**, 405.
158. Luenstedt,J. *et al.* (2024) Partial hepatectomy accelerates colorectal metastasis by priming an inflammatory premetastatic niche in the liver. *Frontiers in Immunology*, **15**.
159. Mack-Bowles,B. (2024) Mechanisms of Mycophenolic Acid-Induced Gastrointestinal Toxicity and Potential Therapeutic Interventions in Primary Mouse Colonic Organoids.
160. Maffei,E. *et al.* (2024) Complete genome sequence of Pseudomonas aeruginosa phage Knedl. *Microbiology Resource Announcements*, **13**, e01174–23.
161. Maldonado-Pava,J. *et al.* (2024) Exploring the biotechnological potential of novel soil-derived Klebsiella sp. and Chryseobacterium sp. strains using phytate as sole carbon source. *Frontiers in Bioengineering and Biotechnology*, **12**.
162. Marco,K. *et al.* (2024) DORQ-seq: high-throughput quantification of femtomol tRNA pools by combination of cDNA hybridization and Deep sequencing. *Nucleic Acids Research*, gkae765.
163. Marimón,J.M. *et al.* (2024) Pertussis Outbreak During 2023 in Gipuzkoa, North Spain. *Vaccines*, **12**, 1192.
164. Martineau,M. *et al.* (2024) Unravelling the main genomic features of Mycoplasma equirhinis. *BMC Genomics*, **25**, 886.
165. Martinez-Delgado,B. *et al.* (2024) Ehmt2 Loss-of-Function Alterations Cause a Kleefstra-Like Syndrome.
166. Martins,S.G. *et al.* (2024) Laminin-α2 chain deficiency in skeletal muscle causes dysregulation of multiple cellular mechanisms. *Life Science Alliance*, **7**.
167. Matsuura-Suzuki,E. *et al.* (2024) miRNA-mediated gene silencing in Drosophila larval development involves GW182-dependent and independent mechanisms. *The EMBO Journal*, 1–19.
168. McCluskey,K. *et al.* (2024) Predicting the Identities of su(met-2) and met-3 in Neurospora crassa by Genome Resequencing. *Fungal Genetics Reports*, **67**.
169. McVey,D.G. *et al.* (2024) Genetic influence on vascular smooth muscle cell apoptosis. *Cell Death & Disease*, **15**, 1–12.
170. Meem,M.H. *et al.* (2024) Exploring the anticancer and antibacterial potential of naphthoquinone derivatives: a comprehensive computational investigation. *Frontiers in Chemistry*, **12**.
171. Mérida-Cerro,J.A. *et al.* (2024) Rat1 promotes premature transcription termination at R-loops. *Nucleic Acids Research*, **52**, 3623–3635.
172. Merz,M. *et al.* (2024) Characterization of the major autolysin (AtlC) of Staphylococcus carnosus. *BMC Microbiology*, **24**, 77.
173. Midtbø,H.M.D. *et al.* (2024) Cell death induced by *Lepeophtheirus salmonis* labial gland protein 3 in salmonid fish leukocytes: A mechanism for disabling host immune responses. *Fish & Shellfish Immunology*, **154**, 109992.
174. Minisy,F.M. *et al.* (2024) Transcription Factor 23 is an Essential Determinant of Murine Term Parturition. *Molecular and Cellular Biology*, **44**, 316–333.
175. Miranda,S. *et al.* (2024) Assessment and Partial Characterization of Candidate Genes in Dihydrochalcone and Arbutin Biosynthesis in an Apple–Pear Hybrid by De Novo Transcriptome Assembly. *Journal of Agricultural and Food Chemistry*.
176. Molina Valencia,E.S. (2024) Anotación genómica de genes expresados en la biosíntesis de compuestos fenólicos en pitahaya (Hylocereus spp.) expuesta a condiciones de estrés.
177. Molla,A.A. *et al.* (2024) Harnessing Lignocellulolytic and Electrogenic Potential: Insights from Shewanella oneidensis MR-1 and Cellulomonas Strains on Lignocellulosic Biomass. *Journal of The Electrochemical Society*, **171**, 095501.
178. Moraga-Fernández,A. *et al.* (2024) Impact of vaccination with the *Anaplasma phagocytophilum* MSP4 chimeric antigen on gene expression in the rabbit host. *Research in Veterinary Science*, **178**, 105370.
179. Moris,V.C. *et al.* (2024) Ionizing radiation responses appear incidental to desiccation responses in the bdelloid rotifer Adineta vaga. *BMC Biology*, **22**, 11.
180. Mostafa,K. *et al.* (2024) Genome-wide analysis of PvMADS in common bean and functional characterization of PvMADS31 in Arabidopsis thaliana as a player in abiotic stress responses. *The Plant Genome*, **17**, e20432.
181. Müller,T. *et al.* (2024) CheRRI—Accurate classification of the biological relevance of putative RNA–RNA interaction sites. *GigaScience*, **13**, giae022.
182. Naorem,R.S. *et al.* (2024) Immunoinformatics Design of a Multiepitope Vaccine (MEV) Targeting Streptococcus mutans: A Novel Computational Approach. *Pathogens*, **13**, 916.
183. Nayak,R. and Mallick,B. (2024) BMS345541 is predicted as a repurposed drug for the treatment of TMZ-resistant Glioblastoma using target gene expression and virtual drug screening. *Cancer Genetics*, **288-289**, 20–31.
184. Nguionza,A.-E. (2024) Development and Validation of Nanopore Sequencing Targeting the L1 Gene for High-Risk HPV Genotyping /.
185. Nguyen,D.H. *et al.* (2024) Genomic characterization and identification of candidate genes for putative podophyllotoxin biosynthesis pathway in Penicillium herquei HGN12.1C. *Microbial Biotechnology*, **17**, e70007.
186. Nicholson,T.L. *et al.* (2024) The contribution of BvgR, RisA, and RisS to global gene regulation, intracellular cyclic-di-GMP levels, motility, and biofilm formation in Bordetella bronchiseptica. *Frontiers in Microbiology*, **15**.
187. Nilsson,A. (2024) Benchmarking Bioinformatics Workflows using Bibliographic Networks : Exploring Co-Usage Information in Software Co-Citation Graphs.
188. Amazonian Bacteria from River Sediments as a Biocontrol Solution against Ralstonia solanacearum (2024).
189. Bioinformatic challenge on prostate cancer and urinary microbiome. \\textbar EBSCOhost (2024).
190. Candidatus Methanosphaera massiliense sp. nov., a methanogenic archaeal species found in a human fecal sample and prevalent in pigs and red kangaroos \\textbar Microbiology Spectrum (2024).
191. Draft genome sequence of Streptomyces poriferorum RTGN2, a bacterial endophyte isolated from Alnus glutinosa root nodules \\textbar Microbiology Resource Announcements (2024).
192. The Effect of Methamphetamine on NeuroHIV, Alzheimer’s Disease, and Alzheimer’s Disease Related Dementias - ProQuest (2024).
193. Effect of Anti‐S100A4 Monoclonal Antibody Treatment on Experimental Skin Fibrosis and Systemic Sclerosis–Specific Transcriptional Signatures in Human Skin - Trinh‐Minh - 2024 - Arthritis & Rheumatology - Wiley Online Library (2024).
194. Insights Into the Evolution of Chromatin Architecture Generated by Inversion Breakpoints in \\textlessem\\textgreaterDrosophila pseudoobscura\\textless/em\\textgreater - ProQuest (2024).
195. Nutrients \\textbar Free Full-Text \\textbar A 14-Day Double-Blind, Randomized, Controlled Crossover Intervention Study with Anti-Bacterial Benzyl Isothiocyanate from Nasturtium (Tropaeolum majus) on Human Gut Microbiome and Host Defense (2024).
196. A practical guide to bioimaging research data management in core facilities - Schmidt - 2024 - Journal of Microscopy - Wiley Online Library (2024).
197. Repositório Institucional da UnB: Estudo sobre bactérias degradadoras de polietileno : descrição de uma potencial nova espécie bacteriana e caracterização de uma enzima peroxirredoxina (2024).
198. Whole-genome long-read sequencing to unveil Enterococcus antimicrobial resistance in dairy cattle farms exposed a widespread occurrence of Enterococcus lactis \\textbar Microbiology Spectrum (2024).
199. Nógell,A. (2024) Structure and function of the ribosomal intergenic DNA.
200. Nugroho,A. *et al.* (2024) Transcriptome dataset of gall-rust infected Sengon (*Falcataria falcata*) seedlings using long-read PCR-cDNA sequencing. *Data in Brief*, **52**, 109919.
201. Nwankwo,C.C. *et al.* (2024) Metagenomic Study of Bacteria Diversity and Functional Profile in Bulk and Rhizosphere Soils of Fusarium-Wilt Infected Plantain (Musa paradisiaca). *Journal of Advances in Microbiology*, **24**, 77–93.
202. Oakes,B.J. *et al.* (2024) Building Domain-Specific Machine Learning Workflows: A Conceptual Framework for the State of the Practice. *ACM Transactions on Software Engineering and Methodology*, **33**, 91:1–91:50.
203. Ocejo,M. *et al.* (2024) Whole-genome long-read sequencing to unveil Enterococcus antimicrobial resistance in dairy cattle farms exposed a widespread occurrence of Enterococcus lactis. *Microbiology Spectrum*, **12**, e03672–23.
204. Ogunnupebi,T.A. *et al.* (2024) In silico studies of benzothiazole derivatives as potential inhibitors of Anopheles funestus and Anopheles gambiae trehalase. *Frontiers in Bioinformatics*, **4**.
205. Oliveira,T.T. *et al.* (2024) Integrated analysis of RNA-seq datasets reveals novel targets and regulators of COVID-19 severity. *Life Science Alliance*, **7**.
206. Olszak-Przybyś,H. and Korbecka-Glinka,G. (2024) The Diversity of Seed-Borne Fungi Associated with Soybean Grown in Southern Poland. *Pathogens*, **13**, 769.
207. ORTEGA RAMÍREZ,J.A.Z.M.Í.N.A.L.E.J.A.N.D.R.A. (2024) MOLECULAR CHARACTERIZATION OF PLASMIDS CARRYING AMPC Β-LACTAMASES (AMPCs) AND EXTENDED-SPECTRUM Β-LACTAMASE (ESBLs) GENES USING HYBRID GENOME ASSEMBLY ANALYSIS.
208. Ostenfeld,L.J. *et al.* (2024) A hybrid receptor binding protein enables phage F341 infection of Campylobacter by binding to flagella and lipooligosaccharides. *Frontiers in Microbiology*, **15**.
209. Ou,S. *et al.* (2024) Differences in activity and stability drive transposable element variation in tropical and temperate maize. *Genome Research*, **34**, 1140–1153.
210. Oyedara,O.O. *et al.* (2024) Bacterial Communities, Pathogens, Resistomes, and Mobilomes Associated with a Wastewater Treatment Plant in Mexico: A Metagenomics Approach. *International Journal of Environmental Research*, **19**, 47.
211. Pachanon,R. *et al.* (2024) Genomic characterization of carbapenem and colistin-resistant Klebsiella pneumoniae isolates from humans and dogs. *Frontiers in Veterinary Science*, **11**.
212. Palacios-Rodriguez,A.P. *et al.* (2024) Antimicrobial Activity of Bacillus amyloliquefaciens BS4 against Gram-Negative Pathogenic Bacteria. *Antibiotics*, **13**, 304.
213. Pazoki,N. *et al.* (2024) Elucidating the impact of Y chromosome microdeletions and altered gene expression on male fertility in assisted reproduction. *Human Molecular Genetics*, ddae086.
214. Peresh,Y.-Y. *et al.* (2024) Carbon nanodots as photosensitizer in photodynamic inactivation of *Rickettsia slovaca*. *Photodiagnosis and Photodynamic Therapy*, 104402.
215. Pérez-Sisqués,L. *et al.* (2024) The Intellectual Disability Risk Gene Kdm5b Regulates Long-Term Memory Consolidation in the Hippocampus. *Journal of Neuroscience*, **44**.
216. Pfäffle,S.P. *et al.* (2024) A 14-Day Double-Blind, Randomized, Controlled Crossover Intervention Study with Anti-Bacterial Benzyl Isothiocyanate from Nasturtium (Tropaeolum majus) on Human Gut Microbiome and Host Defense. *Nutrients*, **16**, 373.
217. Pham,V.-C. *et al.* (2024) Epigenetic regulation by polycomb repressive complex 1 promotes cerebral cavernous malformations. *EMBO Molecular Medicine*, 1–29.
218. Pick,K. *et al.* (2024) Complete genome sequence of Escherichia coli MP1. *Microbiology Resource Announcements*, **0**, e01216–23.
219. Pietroforte,S. *et al.* (2024) Meiotic maturation failure in primary ovarian insufficiency: insights from a bovine model. *Journal of Assisted Reproduction and Genetics*, **41**, 2011–2020.
220. Pilliol,V. *et al.* (2024) Methanobrevibacter massiliense and Pyramidobacter piscolens Co-Culture Illustrates Transkingdom Symbiosis. *Microorganisms*, **12**, 215.
221. Pinto,D. *et al.* (2024) Rescue of Mycobacterium bovis DNA Obtained from Cultured Samples during Official Surveillance of Animal TB: Key Steps for Robust Whole Genome Sequence Data Generation. *International Journal of Molecular Sciences*, **25**, 3869.
222. Pirnay,J.-P. *et al.* (2024) Personalized bacteriophage therapy outcomes for 100 consecutive cases: a multicentre, multinational, retrospective observational study. *Nature Microbiology*, **9**, 1434–1453.
223. Pranomphon,T. *et al.* (2024) Oviduct epithelial spheroids during in vitro culture of bovine embryos mitigate oxidative stress, improve blastocyst quality and change the embryonic transcriptome. *Biological Research*, **57**, 73.
224. Punyawatthananukool,S. *et al.* (2024) Prostaglandin E2-EP2/EP4 signaling induces immunosuppression in human cancer by impairing bioenergetics and ribosome biogenesis in immune cells. *Nature Communications*, **15**, 9464.
225. Pustam,A. *et al.* (2024) Whole genome sequencing reveals complex resistome features of *Klebsiella pneumoniae* isolated from patients at major hospitals in Trinidad, West Indies. *Journal of Global Antimicrobial Resistance*.
226. Pyles,R.B. *et al.* (2024) The altered TBI fecal microbiome is stable and functionally distinct. *Frontiers in Molecular Neuroscience*, **17**.
227. Pyöriä,L. *et al.* (2024) Intra-host genomic diversity and integration landscape of human tissue-resident DNA virome. *Nucleic Acids Research*, gkae871.
228. Qiu,X. *et al.* (2024) SmCYP71D373 of *Salvia miltiorrhiza* catalyzes the methyl oxidation reaction of tanshinone IIA-19 position. *Industrial Crops and Products*, **212**, 118323.
229. Rabbås,H.B. (2024) Surveillance and detection of multidrug resistant bacterial strains and blaOXA genes in aquatic environments in Ås and Nordre Follo municipalities.
230. Rahman,N. *et al.* (2024) Mobilisation and analyses of publicly available SARS-CoV-2 data for pandemic responses. *Microbial Genomics*, **10**, 001188.
231. Ramos,B. and Cunha,M.V. (2024) The mobilome of *Staphylococcus aureus* from wild ungulates reveals epidemiological links at the animal-human interface. *Environmental Pollution*, 124241.
232. Rapp,J. *et al.* (2024) Oncostatin M Reduces Pathological Neovascularization in the Retina Through Müller Cell Activation. *Investigative Ophthalmology & Visual Science*, **65**, 22.
233. Raubenolt,B. and Blankenberg,D. (2024) Generalized open-source workflows for atomistic molecular dynamics simulations of viral helicases. *GigaScience*, **13**, giae026.
234. Ravindran,S. and Rau,C.D. (2024) The multifaceted role of mitochondria in cardiac function: insights and approaches. *Cell Communication and Signaling*, **22**, 525.
235. Rebollo,R. *et al.* (2024) Identification and quantification of transposable element transcripts using Long-Read RNA-seq in Drosophila germline tissues. *Peer Community Journal*, **4**.
236. Richter,S. *et al.* (2024) Genome sequence of a European Diplocarpon coronariae strain and in silico structure of the mating-type locus. *Frontiers in Plant Science*, **15**.
237. Richter,L. *et al.* (2024) Genomic Evaluation of Multidrug-Resistant Extended-Spectrum β-Lactamase (ESBL)-Producing Escherichia coli from Irrigation Water and Fresh Produce in South Africa: A Cross-Sectional Analysis. *Environmental Science & Technology*, **58**, 14421–14438.
238. Robson,J.K. *et al.* (2024) Environmental regulation of male fertility is mediated through Arabidopsis transcription factors bHLH89, 91, and 10. *Journal of Experimental Botany*, **75**, 1934–1947.
239. Rodrigues Alves Barbosa,V. (2024) Phenotypic variability in C. elegans natural isolates reveals plasticity of gene essentiality for mat-1 and cgh-1.
240. Rodríguez-Alarcón,C.A. *et al.* (2024) MICROBIAL DIVERSITY OF CULICOIDES REEVESI FROM CHIHUAHUA, MEXICO: A METAGENOMIC ANALYSIS OF RRNA 16S.
241. Royaux,C. *et al.* (2024) Genetic variability of New Caledonian Boeckella De Guerne & Richard, 1889 (Copepoda: Calanoida), with the description of a new species. *Journal of Crustacean Biology*, **44**, ruae001.
242. Rukminiati,Y. *et al.* (2024) First Indonesian report of WGS-based MTBC L3 discovery. *BMC Research Notes*, **17**, 176.
243. Russo,D.A. *et al.* (2024) EXCRETE workflow enables deep proteomics of the microbial extracellular environment. *Communications Biology*, **7**, 1–13.
244. Sabala,R.F. *et al.* (2024) Carbapenem and colistin-resistant hypervirulent *Klebsiella pneumoniae*: An emerging threat transcending the egyptian food chain. *Journal of Infection and Public Health*, **17**, 1037–1046.
245. Saddiqa,A. *et al.* (2024) On discovery of novel hub genes for ER+ and TN breast cancer types through RNA seq data analyses and classification models. *Scientific Reports*, **14**, 20840.
246. Sageman-Furnas,K. *et al.* (2024) Detailing Early Shoot Growth Arrest in Kro-0 x BG-5 Hybrids of Arabidopsis thaliana. *Plant and Cell Physiology*, **65**, 420–427.
247. Salapa,H.E. *et al.* (2024) hnRNP A1 dysfunction alters RNA splicing and drives neurodegeneration in multiple sclerosis (MS). *Nature Communications*, **15**, 356.
248. Salerno,C. (2024) Metaproteomics: Methods and Protocols Springer Nature.
249. Sánchez-León,I. (2024) Heterorresistencia a colistina en aislados clínicos de Klebsiella pneumoniae con fenotipo de resistencia silvestre o productores de la carbapenemasa OXA-48.
250. Sarkar,P. *et al.* (2024) Insights on the comparative affinity of ribonucleic acids with plant-based beta carboline alkaloid, harmine: Spectroscopic, calorimetric and computational evaluation. *Heliyon*, **0**.
251. Sarkar,S. *et al.* (2024) JunB is required for CD8+ T cell responses to acute infections. *International Immunology*, dxae063.
252. Schäfer,R.A. (2024) Algorithms for the global mapping of RNA-RNA interactomes.
253. Schäfer,L. *et al.* (2024) A practical guide and Galaxy workflow to avoid inter-plasmidic repeat collapse and false gene loss in Unicycler’s hybrid assemblies. *Microbial Genomics*, **10**, 001173.
254. Schene,I.F. *et al.* (2024) Misidentification of neural cell identity in liver-derived organoid systems. *Stem Cell Reports*, **19**, 315–316.
255. Schmidt,C. *et al.* (2024) A practical guide to bioimaging research data management in core facilities. *Journal of Microscopy*, **294**, 350–371.
256. Schröder,C.M. *et al.* (2024) EOMES establishes mesoderm and endoderm differentiation potential through SWI/SNF-mediated global enhancer remodeling. *Developmental Cell*, **0**.
257. Schult,P. *et al.* (2024) Viral hijacking of hnRNPH1 unveils a G-quadruplex-driven mechanism of stress control. *Cell Host & Microbe*.
258. Sethi,R. *et al.* (2024) ezSingleCell: an integrated one-stop single-cell and spatial omics analysis platform for bench scientists. *Nature Communications*, **15**, 5600.
259. Shaikh,M.A. *et al.* (2024) StCDF1: A ‘jack of all trades’ clock output with a central role in regulating potato nitrate reduction activity. *New Phytologist*, **n/a**.
260. Shipman,A. and Tian,M. (2024) Combined Use of Phenotype-Based and Genome-Informed Approaches Identified a Unique Fusarium oxysporum f. sp. cubense Isolate in Hawaii. *Phytopathology®*, **114**, 1305–1319.
261. Silar,P. and Lalanne,C. (2024) Fungani, a Blast-Based Program for Analyzing Average Nucleotide Identity (Ani) between Two Fungal Genomes, Enables Easy Fungal Species Delimitation.
262. Silva,F.J. *et al.* (2024) Comparative Transcriptomics of Fat Bodies between Symbiotic and Quasi-Aposymbiotic Adult Females of Blattella germanica with Emphasis on the Metabolic Integration with Its Endosymbiont Blattabacterium and Its Immune System. *International Journal of Molecular Sciences*, **25**, 4228.
263. Sime,A.M. *et al.* (2024) Microbial carbohydrate active enzyme (CAZyme) genes and diversity from Menagesha Suba natural forest soils of Ethiopia as revealed by shotgun metagenomic sequencing. *BMC Microbiology*, **24**, 285.
264. Singh,P. *et al.* (2024) Biophysical and structural characterization of tetramethrin serum protein complex and its toxicological implications. *Journal of Molecular Recognition*, **n/a**, e3076.
265. Singh,S. *et al.* (2024) Hemoglobin Targeting Potential of Aminocarb Pesticide: Investigation into Dynamics, Conformational Stability, and Energetics in Solvent Environment. *Biochemical and Biophysical Research Communications*, 150896.
266. Skalon,E.K. *et al.* (2024) Expression of Transposable Elements throughout the Fasciola hepatica Trematode Life Cycle. *Non-Coding RNA*, **10**, 39.
267. Soggia,G. *et al.* (2024) Bioelectrochemical protein production valorizing NH3-rich pig manure-derived wastewater and CO2 from anaerobic digestion. *Renewable Energy*, 120761.
268. Soleau,N. *et al.* (2024) First Isolation of the Heteropathotype Shiga Toxin-Producing and Extra-Intestinal Pathogenic (STEC-ExPEC) E. coli O80:H2 in French Healthy Cattle: Genomic Characterization and Phylogenetic Position. *International Journal of Molecular Sciences*, **25**, 5428.
269. Souza,D. and Alves,Y.P. (2024) The effect of increasing plant species richness on soil and seed microbiome and its importance to stress response.
270. Søyland,E.Ø. (2024) Mapping the presence of antibiotic resistant bacteria in water habitats in Gjesdal, Moss, and Våler municipality.
271. Spanò,R. *et al.* (2024) Overview of transcriptome changes and phenomic profile of sanitized artichoke vis-à-vis non-sanitized plants. *Plant Biology*, **26**, 715–726.
272. Spanò,R. *et al.* (2024) Spotlight on Secondary Metabolites Produced by an Early-Flowering Apulian Artichoke Ecotype Sanitized from Virus Infection by Meristem-Tip-Culture and Thermotherapy. *Antioxidants*, **13**, 852.
273. Stillger,M.N. *et al.* (2024) Neoadjuvant chemo- or chemo-radiation-therapy of pancreatic ductal adenocarcinoma differentially shift ECM composition, complement activation, energy metabolism and ribosomal proteins of the residual tumor mass. *International Journal of Cancer*, **154**, 2162–2175.
274. Stojkovic,L. *et al.* (2024) Targeted RNAseq Revealed the Gene Expression Signature of Ferroptosis-Related Processes Associated with Disease Severity in Patients with Multiple Sclerosis. *International Journal of Molecular Sciences*, **25**, 3016.
275. Strateva,T. and Peykov,S. (2024) First detection of a cefiderocol-resistant and extensively drug-resistant Acinetobacter baumannii clinical isolate in Bulgaria. *Acta Microbiologica et Immunologica Hungarica*, **-1**.
276. Strateva,T. *et al.* (2024) Genomic Insights into Vietnamese Extended-Spectrum β-Lactamase-9-Producing Extensively Drug-Resistant Pseudomonas aeruginosa Isolates Belonging to the High-Risk Clone ST357 Obtained from Bulgarian Intensive Care Unit Patients. *Pathogens*, **13**, 719.
277. Tapia,S. *et al.* (2024) Nanopore sequencing of IPNV vp2 gene in Peruvian Andean trout (Oncorhynchus mykiss) cultures. *Microbiology Resource Announcements*, **0**, e00190–24.
278. Tensen,L. and Camacho,G. (2024) Dark Mystery Solved: A Captive Black Leopard from South Africa is of Asian Descent. *African Journal of Wildlife Research*, **54**.
279. Tetzlaff,S. *et al.* (2024) Small RNAs from mitochondrial genome recombination sites are incorporated into T. gondii mitoribosomes. *eLife*, **13**, e95407.
280. Thangameeran,S.I.M. *et al.* (2024) Examining Transcriptomic Alterations in Rat Models of Intracerebral Hemorrhage and Severe Intracerebral Hemorrhage. *Biomolecules*, **14**, 678.
281. Thompson,R.M. *et al.* (2024) Draft genome sequences of two Micromonospora strains isolated from the root nodules of Alnus glutinosa. *Microbiology Resource Announcements*, **13**, e01131–23.
282. Thompson,R.M. *et al.* (2024) Draft genome sequences of five Mycobacterium strains, isolated from Alnus glutinosa root nodules. *Microbiology Resource Announcements*, **13**, e01132–23.
283. Thongbunrod,N. and Chaiprasert,P. (2024) Potential of enriched and stabilized anaerobic lignocellulolytic fungi coexisting with bacteria and methanogens for enhanced methane production from rice straw. *Biomass Conversion and Biorefinery*, **14**, 8229–8250.
284. Tiwari,V. *et al.* (2024) Innate immune training restores pro-reparative myeloid functions to promote remyelination in the aged central nervous system. *Immunity*, **57**, 2173–2190.e8.
285. Toth,R. *et al.* (2024) Divergence within the Taxon ‘Candidatus Phytoplasma asteris’ Confirmed by Comparative Genome Analysis of Carrot Strains. *Microorganisms*, **12**, 1016.
286. Tóth,K. *et al.* (2024) Genomic Epidemiology of C2/H30Rx and C1-M27 Subclades of Escherichia coli ST131 Isolates from Clinical Blood Samples in Hungary. *Antibiotics*, **13**, 363.
287. Trinh-Minh,T. *et al.* (2024) Effect of Anti-S100A4 Monoclonal Antibody Treatment on Experimental Skin Fibrosis and Systemic Sclerosis–Specific Transcriptional Signatures in Human Skin. *Arthritis and Rheumatology*, **76**, 783–795.
288. Ummethum,H. (2024) Proximity labeling as a tool to study transcription-replication interference.
289. Umpeleva,T. *et al.* (2024) Identification of genetic determinants of bedaquiline resistance in Mycobacterium tuberculosis in Ural region, Russia. *Microbiology Spectrum*, **12**, e03749–23.
290. Uncu,A.T. *et al.* (2024) Whole-genome sequencing and identification of antimicrobial peptide coding genes in parsley (Petroselinum crispum), an important culinary and medicinal Apiaceae species. *Functional & Integrative Genomics*, **24**, 142.
291. Urrutia-Angulo,L. *et al.* (2024) Unravelling the complexity of bovine milk microbiome: insights into mastitis through enterotyping using full-length 16S-metabarcoding. *Animal Microbiome*, **6**, 58.
292. Vallecillo-García,P. *et al.* (2024) Mesenchymal Osr1+ cells regulate embryonic lymphatic vessel formation. *Development*, **151**, dev202747.
293. Varshney,D. *et al.* (2024) MAdLand computational resources for the Plant community., pp. 10–11.
294. Vecchi,M. and Stec,D. (2024) Mitogenome of a new Ramazzottius species (Tardigrada: Eutardigrada: Ramazzottiidae) discovered in rock pools along with its temperature and desiccation-related proteins repertoire. *Organisms Diversity & Evolution*.
295. Vieira Da Cruz,A. *et al.* (2024) Pyridylpiperazine efflux pump inhibitor boosts in vivo antibiotic efficacy against K. pneumoniae. *EMBO Molecular Medicine*, **16**, 93–111.
296. Vieira,T. *et al.* (2024) Polymyxin Resistance in Salmonella: Exploring Mutations and Genetic Determinants of Non-Human Isolates. *Antibiotics*, **13**, 110.
297. Volkova,P. *et al.* (2024) Multi-omics responses of barley seedlings to low and high linear energy transfer irradiation. *Environmental and Experimental Botany*, **218**, 105600.
298. Vozenin,M.-C. *et al.* (2024) More May Not be Better: Enhanced Spacecraft Shielding May Exacerbate Cognitive Decrements by Increasing Pion Exposures during Deep Space Exploration. *Radiation Research*, **201**, 93–103.
299. Wang,E. (2024) Application of CUT\&Tag to the mapping and analysis of VEZF1 binding sites in K562 cells.
300. Wang,Y.-H. *et al.* (2024) The Genome of Arsenophonus sp. and Its Potential Contribution in the Corn Planthopper, Peregrinus maidis. *Insects*, **15**, 113.
301. Wang,L. *et al.* (2024) Growth, Enzymatic, and Transcriptomic Analysis of xyr1 Deletion Reveals a Major Regulator of Plant Biomass-Degrading Enzymes in Trichoderma harzianum. *Biomolecules*, **14**, 148.
302. Waterhouse,R.M. *et al.* (2024) The ELIXIR Biodiversity Community: Understanding short- and long-term changes in biodiversity. *F1000Research*, **12**, ELIXIR–499.
303. Watson,S. *et al.* (2024) Modification of Seurat v4 for the Development of a Phase Assignment Tool Able to Distinguish between G2 and Mitotic Cells. *International Journal of Molecular Sciences*, **25**, 4589.
304. Weise,M. and Rauber,A. (2024) Trusted Research Environments: Analysis of Characteristics and Data Availability. *International Journal of Digital Curation*, **18**.
305. Wennmann,J.T. *et al.* (2024) Distribution and genetic diversity of Bombyx mori nucleopolyhedrovirus in mass-reared silkworms in Thailand. *Journal of Invertebrate Pathology*, 108221.
306. Wicaksono,A. and Buaboocha,T. (2024) Genome-wide identification of CAMTA genes and their expression dependence on light and calcium signaling during seedling growth and development in mung bean. *BMC Genomics*, **25**, 992.
307. Wight,J. *et al.* (2024) Anthropogenic contamination sources drive differences in antimicrobial-resistant Escherichia coli in three urban lakes. *Applied and Environmental Microbiology*, **90**, e01809–23.
308. Willnow,P. and Teleman,A.A. (2024) Nuclear position and local acetyl-CoA production regulate chromatin state. *Nature*, 1–9.
309. Wirth,L. *et al.* (2024) Gene expression networks in endothelial cellsfrom failing human hearts. *American Journal of Physiology-Heart and Circulatory Physiology*.
310. Wurzbacher,C.E. *et al.* (2024) Planctoellipticum variicoloris gen. nov., sp. nov., a novel member of the family Planctomycetaceae isolated from wastewater of the aeration lagoon of a sugar processing plant in Northern Germany. *Scientific Reports*, **14**, 5741.
311. Yong,H.-S. *et al.* (2024) Complete mitochondrial genomes of Bactrocera (Bulladacus) cinnabaria and B. (Bactrocera) propinqua (Diptera: Tephritidae) and their phylogenetic relationships with other congeners. *Arthropod Systematics & Phylogeny*, **82**, 515–526.
312. Yu,K. *et al.* (2024) The USP12/46 deubiquitinases protect integrins from ESCRT-mediated lysosomal degradation. *EMBO reports*, 1–32.
313. Zafar,Z. *et al.* (2024) Identification of the odorant binding proteins of Western Flower Thrips (Frankliniella occidentalis), characterization and binding analysis of FoccOBP3 with molecular modelling, molecular dynamics simulations and a confirmatory field trial. *Journal of Biomolecular Structure and Dynamics*, **0**, 1–16.
314. Zaman,B. *et al.* (2024) Tolperisone hydrochloride improves motor functions in Parkinson’s disease via MMP-9 inhibition and by downregulating p38 MAPK and ERK1/2 signaling cascade. *Biomedicine & Pharmacotherapy*, **174**, 116438.
315. Zehr,J.D. *et al.* (2024) Positive selection, genetic recombination, and intra-host evolution in novel equine coronavirus genomes and other members of the Embecovirus subgenus. *Microbiology Spectrum*, **0**, e00867–24.
316. Zhan,L. *et al.* (2024) Comparison of Mitochondrial Genome Expression Differences among Four Skink Species Distributed at Different Latitudes under Low-Temperature Stress. *International Journal of Molecular Sciences*, **25**, 10637.
317. Zhang,G. *et al.* (2024) Complete Mitochondrial Genomes of Nedyopus patrioticus: New Insights into the Color Polymorphism of Millipedes. *Current Issues in Molecular Biology*, **46**, 2514–2527.
318. Zhang,N. *et al.* (2024) Deciphering the molecular logic of WOX5 function in the root stem cell organizer. *The EMBO Journal*, 1–23.
319. Zhang,G. *et al.* (2024) The First Complete Mitochondrial Genome of the Genus Litostrophus: Insights into the Rearrangement and Evolution of Mitochondrial Genomes in Diplopoda. *Genes*, **15**, 254.
320. Zhao,M. *et al.* (2024) Nodulating Aeschynomene indica without Nod Factor Synthesis Genes: In Silico Analysis of Evolutionary Relationship. *Agronomy*, **14**, 1295.
321. Zhao,R. *et al.* (2024) An RRM domain protein SOE suppresses transgene silencing in rice. *New Phytologist*, **n/a**.
322. Zhu,T. *et al.* (2024) The BAS chromatin remodeler determines brassinosteroid-induced transcriptional activation and plant growth in Arabidopsis. *Developmental Cell*, **59**, 924–939.e6.

  
  
  
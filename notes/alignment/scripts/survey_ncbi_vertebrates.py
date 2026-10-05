#!/usr/bin/env python3
"""Summarize current NCBI Vertebrata assemblies and derive planning scenarios.

Inputs are JSON Lines reports produced by NCBI Datasets v18.34.0:

  datasets summary genome taxon 7742 --as-json-lines --limit all
  datasets summary taxonomy taxon --inputfile TAXIDS --as-json-lines --limit all

A biological assembly may have both GCA_ (GenBank) and GCF_ (RefSeq) records.
For assembly counts this script retains current GCA_ records, which gives one
record per biological assembly without counting the paired RefSeq record twice.
"""

import argparse
import collections
import json
from pathlib import Path

LEVEL_ORDER = {
    "Contig": 0,
    "Scaffold": 1,
    "Chromosome": 2,
    "Complete Genome": 3,
}
LEVELS = ["Complete Genome", "Chromosome", "Scaffold", "Contig"]
PILOT_N = 581
NODE_HOURS_PER_PAIR = 0.263
MB_PER_WORKING_PAIR = 31.1


def load_jsonl(path):
    with open(path, encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def fmt_int(value):
    return f"{value:,}"


def scenario(name, n):
    pairs = n * (n - 1)
    if n >= PILOT_N:
        m = n - PILOT_N
        incremental = m * (2 * PILOT_N + m - 1)
    else:
        incremental = None
    node_hours = incremental * NODE_HOURS_PER_PAIR if incremental is not None else None
    node_hours_contingency = node_hours * 1.2 if node_hours is not None else None
    tb_per_set = pairs * MB_PER_WORKING_PAIR / 1_000_000
    return {
        "name": name,
        "assemblies": n,
        "ordered_pairs": pairs,
        "incremental_pairs_if_pilot_subset": incremental,
        "incremental_node_hours": node_hours,
        "incremental_node_hours_plus_20_percent": node_hours_contingency,
        "working_tb_per_set": tb_per_set,
        "working_tb_five_sets": tb_per_set * 5,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--genomes", required=True)
    parser.add_argument("--taxonomy", required=True)
    parser.add_argument("--json-output", required=True)
    parser.add_argument("--markdown-output", required=True)
    args = parser.parse_args()

    reports = load_jsonl(args.genomes)
    taxonomy_reports = load_jsonl(args.taxonomy)
    taxonomy = {r["taxonomy"]["tax_id"]: r["taxonomy"] for r in taxonomy_reports}

    # One current GenBank record per biological assembly. Paired GCF records are
    # alternate database accessions for the same assembly and are not additional
    # sequence inputs.
    assemblies = [
        r for r in reports
        if r.get("source_database") == "SOURCE_DATABASE_GENBANK"
        and r.get("assembly_info", {}).get("assembly_status") == "current"
    ]

    level_counts = collections.Counter(
        r.get("assembly_info", {}).get("assembly_level", "Unknown") for r in assemblies
    )

    def species_id(row):
        tax_id = row["organism"]["tax_id"]
        classification = taxonomy.get(tax_id, {}).get("classification", {})
        return classification.get("species", {}).get("id", tax_id)

    by_species = collections.defaultdict(list)
    for row in assemblies:
        by_species[species_id(row)].append(row)

    best_by_species = {
        sid: max(
            rows,
            key=lambda r: (
                LEVEL_ORDER.get(r.get("assembly_info", {}).get("assembly_level"), -1),
                bool(r.get("paired_accession")),
                r.get("assembly_stats", {}).get("scaffold_n50", 0) or 0,
                r.get("assembly_stats", {}).get("contig_n50", 0) or 0,
                r.get("assembly_info", {}).get("release_date", ""),
            ),
        )
        for sid, rows in by_species.items()
    }
    best_level_counts = collections.Counter(
        r.get("assembly_info", {}).get("assembly_level", "Unknown")
        for r in best_by_species.values()
    )

    current_refseq_roots = {
        r["accession"][4:].split(".")[0]
        for r in reports
        if r.get("source_database") == "SOURCE_DATABASE_REFSEQ"
        and r.get("assembly_info", {}).get("assembly_status") == "current"
    }

    class_counts = collections.Counter()
    for sid in by_species:
        t = taxonomy.get(sid)
        if t is None:
            # sid may be a species ancestor rather than an input taxon. Find an
            # input taxon's classification carrying that species id.
            input_taxid = by_species[sid][0]["organism"]["tax_id"]
            t = taxonomy.get(input_taxid, {})
        class_name = t.get("classification", {}).get("class", {}).get("name", "Unclassified")
        class_counts[class_name] += 1

    all_species_n = len(by_species)
    scaffold_or_better_n = sum(
        1 for r in best_by_species.values()
        if LEVEL_ORDER.get(r.get("assembly_info", {}).get("assembly_level"), -1) >= LEVEL_ORDER["Scaffold"]
    )
    chromosome_or_better_n = sum(
        1 for r in best_by_species.values()
        if LEVEL_ORDER.get(r.get("assembly_info", {}).get("assembly_level"), -1) >= LEVEL_ORDER["Chromosome"]
    )

    chromosome_assemblies_n = sum(level_counts[level] for level in ("Complete Genome", "Chromosome"))

    scenarios = [
        scenario("All current assemblies, paired RefSeq records deduplicated", len(assemblies)),
        scenario("All chromosome-level and complete assemblies", chromosome_assemblies_n),
        scenario("One best current assembly per represented species, all levels", all_species_n),
        scenario("One best assembly per species, scaffold or better", scaffold_or_better_n),
        scenario("One best assembly per species, chromosome or complete", chromosome_or_better_n),
    ]

    result = {
        "survey_date": "2026-08-01",
        "taxonomy": {"name": "Vertebrata", "tax_id": 7742},
        "ncbi_datasets_version": "18.34.0",
        "raw_accession_records": len(reports),
        "current_biological_assemblies": len(assemblies),
        "current_refseq_counterparts": len(current_refseq_roots),
        "represented_species": all_species_n,
        "phase_1_complete_or_chromosome_assemblies": chromosome_assemblies_n,
        "phase_1_represented_species": chromosome_or_better_n,
        "assembly_levels": dict(level_counts),
        "best_assembly_level_per_species": dict(best_level_counts),
        "species_by_class": dict(class_counts.most_common()),
        "phase_1_rule": "All current complete and chromosome-level biological assemblies.",
        "tranche_order": (
            "Maximize taxonomic novelty at class, order, family, genus, and species levels, "
            "then rank RefSeq status, scaffold N50, contig N50, and release date."
        ),
        "scenarios": scenarios,
        "caveat": (
            "Incremental calculations assume all 581 completed pilot assemblies occur in "
            "the selected NCBI set. Verify by accession against the pilot manifest."
        ),
    }

    Path(args.json_output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# NCBI Vertebrata assembly survey — 2026-08-01",
        "",
        "NCBI Datasets v18.34.0, taxon 7742 (Vertebrata). The raw report contains "
        f"{fmt_int(len(reports))} accession records because many biological assemblies have both "
        "GenBank (`GCA_`) and RefSeq (`GCF_`) accessions. We count current `GCA_` records to "
        "avoid treating a paired RefSeq accession as another assembly.",
        "",
        "| Measure | Count |",
        "| --- | ---: |",
        f"| Raw GCA/GCF accession records | {fmt_int(len(reports))} |",
        f"| Current biological assemblies | **{fmt_int(len(assemblies))}** |",
        f"| Assemblies with a current RefSeq counterpart | {fmt_int(len(current_refseq_roots))} |",
        f"| Species represented | **{fmt_int(all_species_n)}** |",
        f"| Phase 1 complete/chromosome assemblies | **{fmt_int(chromosome_assemblies_n)}** |",
        f"| Species represented in Phase 1 | **{fmt_int(chromosome_or_better_n)}** |",
        "",
        "## Assembly level",
        "",
        "| Level | All current assemblies | Best assembly per species |",
        "| --- | ---: | ---: |",
    ]
    for level in LEVELS:
        lines.append(
            f"| {level} | {fmt_int(level_counts[level])} | {fmt_int(best_level_counts[level])} |"
        )
    lines.extend([
        "",
        "## Planning scenarios",
        "",
        "The compute columns use the measured FastGA cost of 0.263 node-hours per ordered "
        "pair. Storage uses the draft's measured 31.1 MB of working data per pair and must "
        "be reconciled with the smaller compressed public release.",
        "",
        "| Scenario | N | Ordered pairs | New pairs beyond 581* | Node-h +20% | Working TB/set |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ])
    for s in scenarios:
        lines.append(
            f"| {s['name']} | {fmt_int(s['assemblies'])} | {fmt_int(s['ordered_pairs'])} | "
            f"{fmt_int(s['incremental_pairs_if_pilot_subset'])} | "
            f"{fmt_int(round(s['incremental_node_hours_plus_20_percent']))} | "
            f"{s['working_tb_per_set']:,.0f} |"
        )
    lines.extend([
        "",
        "\\* Assumes all 581 completed pilot assemblies are members of the selected set. "
        "Verify this against the pilot accession manifest before using the incremental figure.",
        "",
        "## Selected staged inclusion rule",
        "",
        "Phase 1 includes all 4,467 complete and chromosome-level assemblies. Within that set, "
        "execution order maximizes taxonomic novelty at class, order, family, genus, and species "
        "levels before adding redundant assemblies from already dense clades. Later scaffold and "
        "contig candidates must pass explicit usability checks and follow the same clade-balanced "
        "ordering.",
        "",
        "## Species by NCBI class",
        "",
        "| Class | Species |",
        "| --- | ---: |",
    ])
    for name, count in class_counts.most_common():
        lines.append(f"| {name} | {fmt_int(count)} |")
    lines.append("")
    Path(args.markdown_output).write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

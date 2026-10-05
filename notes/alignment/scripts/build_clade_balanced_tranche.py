#!/usr/bin/env python3
"""Freeze a clade-balanced NCBI vertebrate assembly tranche.

Phase 1 candidates are current GenBank biological assemblies at chromosome or
complete-genome level. Paired GCF records are database counterparts, not
additional assemblies. Candidates already present in the 581-assembly pilot
are excluded by accession root. The greedy order maximizes taxonomic novelty
lexicographically at class, order, family, genus, then species. Quality breaks
ties without overriding cladal breadth.
"""

import argparse
import collections
import csv
import json
from pathlib import Path

RANKS = ("class", "order", "family", "genus", "species")
LEVEL_SCORE = {"Chromosome": 1, "Complete Genome": 2}


def load_jsonl(path):
    with open(path, encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def root(accession):
    return accession.split(".")[0]


def classification(taxonomy, tax_id):
    c = taxonomy.get(tax_id, {}).get("classification", {})
    return {rank: c.get(rank, {}) for rank in RANKS}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--genomes", required=True)
    parser.add_argument("--taxonomy", required=True)
    parser.add_argument("--pilot-catalog", required=True)
    parser.add_argument("--size", type=int, default=800)
    parser.add_argument("--tsv-output", required=True)
    parser.add_argument("--json-output", required=True)
    parser.add_argument("--markdown-output", required=True)
    args = parser.parse_args()

    reports = load_jsonl(args.genomes)
    taxonomy = {
        row["taxonomy"]["tax_id"]: row["taxonomy"]
        for row in load_jsonl(args.taxonomy)
    }
    pilot = json.load(open(args.pilot_catalog, encoding="utf-8"))["records"]

    current_gca = [
        row for row in reports
        if row.get("source_database") == "SOURCE_DATABASE_GENBANK"
        and row.get("assembly_info", {}).get("assembly_status") == "current"
    ]
    by_accession = {row["accession"]: row for row in reports}
    by_root = {root(row["accession"]): row for row in current_gca}
    by_name = {
        row["organism"]["organism_name"].casefold(): row for row in current_gca
    }

    pilot_rows = []
    unmatched_pilot = []
    for record in pilot:
        accession = record["accessions"]["primary"]
        row = (
            by_accession.get(accession)
            or by_root.get(root(accession))
            or by_name.get(record["scientificName"].casefold())
        )
        if row is None:
            unmatched_pilot.append({
                "accession": accession,
                "scientific_name": record["scientificName"],
                "clade": record.get("clade"),
            })
        else:
            pilot_rows.append(row)

    pilot_roots = {root(record["accessions"]["primary"]) for record in pilot}
    candidates = [
        row for row in current_gca
        if row.get("assembly_info", {}).get("assembly_level") in LEVEL_SCORE
        and root(row["accession"]) not in pilot_roots
    ]

    represented = {rank: set() for rank in RANKS}
    for row in pilot_rows:
        for rank, value in classification(taxonomy, row["organism"]["tax_id"]).items():
            if value.get("id") is not None:
                represented[rank].add(value["id"])
    coverage_before = {rank: len(ids) for rank, ids in represented.items()}

    selected = []
    remaining = list(candidates)
    for ordinal in range(1, min(args.size, len(remaining)) + 1):
        def score(row):
            cls = classification(taxonomy, row["organism"]["tax_id"])
            novelty = tuple(
                int(value.get("id") is not None and value["id"] not in represented[rank])
                for rank, value in cls.items()
            )
            stats = row.get("assembly_stats", {})
            info = row.get("assembly_info", {})
            return (
                *novelty,
                LEVEL_SCORE.get(info.get("assembly_level"), 0),
                int(bool(row.get("paired_accession"))),
                stats.get("scaffold_n50", 0) or 0,
                stats.get("contig_n50", 0) or 0,
                info.get("release_date", ""),
                row["accession"],
            )

        chosen = max(remaining, key=score)
        remaining.remove(chosen)
        cls = classification(taxonomy, chosen["organism"]["tax_id"])
        novelty = [
            rank for rank, value in cls.items()
            if value.get("id") is not None and value["id"] not in represented[rank]
        ]
        reason = novelty[0] if novelty else "additional_assembly"
        for rank, value in cls.items():
            if value.get("id") is not None:
                represented[rank].add(value["id"])
        selected.append((ordinal, reason, chosen, cls))

    coverage_after = {rank: len(ids) for rank, ids in represented.items()}
    level_counts = collections.Counter(
        row["assembly_info"]["assembly_level"] for _, _, row, _ in selected
    )
    reason_counts = collections.Counter(reason for _, reason, _, _ in selected)

    fields = [
        "tranche_order", "selection_reason", "accession", "paired_refseq",
        "scientific_name", "tax_id", "assembly_level", "assembly_name",
        "release_date", "total_sequence_length", "scaffold_n50", "contig_n50",
        *RANKS,
    ]
    with open(args.tsv_output, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for ordinal, reason, row, cls in selected:
            info = row["assembly_info"]
            stats = row.get("assembly_stats", {})
            writer.writerow({
                "tranche_order": ordinal,
                "selection_reason": reason,
                "accession": row["accession"],
                "paired_refseq": row.get("paired_accession", ""),
                "scientific_name": row["organism"]["organism_name"],
                "tax_id": row["organism"]["tax_id"],
                "assembly_level": info.get("assembly_level", ""),
                "assembly_name": info.get("assembly_name", ""),
                "release_date": info.get("release_date", ""),
                "total_sequence_length": stats.get("total_sequence_length", ""),
                "scaffold_n50": stats.get("scaffold_n50", ""),
                "contig_n50": stats.get("contig_n50", ""),
                **{rank: cls[rank].get("name", "") for rank in RANKS},
            })

    n0 = len(pilot)
    k = len(selected)
    n = n0 + k
    new_pairs = k * (2 * n0 + k - 1)
    result = {
        "generated_date": "2026-08-01",
        "pilot_assemblies": n0,
        "pilot_matched_to_ncbi_vertebrata_report": len(pilot_rows),
        "pilot_unmatched_or_outgroups": unmatched_pilot,
        "phase_1_candidates_excluding_pilot_roots": len(candidates),
        "tranche_size": k,
        "catalogue_after_tranche": n,
        "new_ordered_pairs": new_pairs,
        "total_ordered_pairs_after_tranche": n * (n - 1),
        "selection_rule": (
            "Greedy lexicographic novelty at class, order, family, genus, species; "
            "then complete over chromosome, paired RefSeq, scaffold N50, contig N50, "
            "release date, accession."
        ),
        "coverage_before": coverage_before,
        "coverage_after": coverage_after,
        "assembly_levels": dict(level_counts),
        "selection_reasons": dict(reason_counts),
        "manifest": str(args.tsv_output),
    }
    Path(args.json_output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Frozen clade-balanced tranche manifest — 2026-08-01",
        "",
        f"This manifest adds **{k:,}** current NCBI complete or chromosome-level assemblies "
        f"to the {n0}-assembly pilot. The resulting catalogue contains **{n:,} assemblies**, "
        f"with **{new_pairs:,} new ordered pairs** and **{n * (n - 1):,} total ordered pairs.",
        "",
        "The TSV manifest is `notes/alignment/data/tranche-800-2026-08-01.tsv`.",
        "",
        "## Selection rule",
        "",
        "Candidates are ordered greedily by new class, order, family, genus, then species. "
        "Assembly quality breaks ties but never overrides taxonomic novelty. Paired GCA/GCF "
        "records count as one biological assembly.",
        "",
        "## Coverage",
        "",
        "| Rank | Pilot matched to NCBI | After tranche | Added |",
        "| --- | ---: | ---: | ---: |",
    ]
    for rank in RANKS:
        lines.append(
            f"| {rank.title()} | {coverage_before[rank]:,} | {coverage_after[rank]:,} | "
            f"{coverage_after[rank] - coverage_before[rank]:,} |"
        )
    lines.extend([
        "",
        "## Tranche composition",
        "",
        f"- Complete genomes: {level_counts['Complete Genome']:,}",
        f"- Chromosome-level assemblies: {level_counts['Chromosome']:,}",
        f"- Pilot accessions matched to the current Vertebrata report: {len(pilot_rows):,} of {n0:,}",
        f"- Unmatched pilot records or deliberate outgroups: {len(unmatched_pilot):,}",
        "",
        "The unmatched records are listed in the JSON audit artifact and are retained in the "
        "pilot. Most are non-vertebrate chordate or deuterostome outgroups rather than missing "
        "vertebrate candidates.",
        "",
    ])
    Path(args.markdown_output).write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

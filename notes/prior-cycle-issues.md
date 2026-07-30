# Defects in prior submissions — do not repeat

Found while archiving the Drive folder. These are real errors in documents that
were actually submitted, and a reviewer comparing years would catch them.

## Internal contradictions between the summary and the body

Both the 2023 and 2024 Main documents contradict themselves on the amounts
requested:

- **2024 Main**: the section 1 summary requests **Stampede3: 500,000 node-hours**,
  while section 4's narrative still carries the stale sentence *"Stampede 2:
  10,000 SUs (node-hours) ... This is no change from the amount of our previous
  year's request."* Different system, different number, in the same document.
- **2023 Main**: same class of error for Rockfish — **1,000,000 SU** in the
  summary, **500,000 SU** in the body.

The summary bullet list and the per-resource justification section are edited
independently year to year, and the body sentences get carried forward without
being reconciled. **Before submitting 2026: diff the summary table against the
section 4 justifications line by line.**

## Justification text carried forward past its expiry

The Ranch request has been 4 PB every year since 2023, justified each time with
the identical sentence: *"for transitioning to tiered storage and decreasing our
current Corral footprint."* If that transition is complete, say so and rewrite
the justification. If it is not, after three years the report needs to explain
why.

Similarly, several Jetstream2 CPU justifications repeat *"We have developed a
system to scale out Jetstream-2 usage for workshops that will result in an
increase in usage during the next year"* — this sentence appears in 2023, 2024,
and 2025 unchanged.

## Progress report page limit

The 2025 Progress Report contains ~500 lines of publication list and states
outright *"Note that we could not fit all publications into the required 3
pages!"* The limit is 3 pages. Move lists to the References document, which has
no page limit.

## Archive folder naming does not match document self-titling

- `archive/galaxy/2023/*` — documents are internally titled **"2022/23 allocation"**
- `archive/galaxy/2024/*` — internally titled **"2024/25 allocation"**
- `archive/galaxy/2025/*` — internally titled **"2025/26 allocation"**
- `archive/galaxy/supplements/*` — internally titled **"2023/24 allocation"**

Folder names follow the Drive file names ("Main 2023"), which for the 2023 cycle
disagree with the document's own title. The 2023 document title was probably
never updated. Left as-is because `archive/` is a verbatim record, but be aware
when citing prior years.

## The public VGP page is stale and reviewers may check it

The 2025 Main document claims 348 assemblies as of July 2025 and cites
<https://galaxyproject.org/projects/vgp> as the source. That page currently
reads *"Last updated January, 2025 with 315 assemblies of 188 species."*

A reviewer following the citation finds a smaller, older number than the one in
the proposal. **Update the public page before submitting**, or cite something
that actually carries the current figure. Note also that the page counts
assemblies *and* species separately (some species appear twice because two
haplotype assemblies exist) — the proposal should be explicit about which it
means.

## Typos in prior submissions

- 2025 Main §3.2 links to `https://galayxproject.org/projects/vgp` — "galayx"
  is transposed. Corrected in the 2026 draft.
- 2025 Main Table heading is labeled "Table 3" but is the first and only table;
  §2.2 text refers to it as "Table 1".
- 2025 Main §2.2 refers to the tools repository as `/iuc`; the actual repo is
  `/tools-iuc`. Corrected in the 2026 draft.

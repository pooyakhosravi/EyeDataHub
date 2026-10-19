# Fundus source-evidence proposal (2026-10-19)

Status: **candidate evidence only, pending maintainer discussion**. These are
not registered records, supported loaders, or additions to the frozen v0.7.0
scientific snapshot. This document proposes three standalone entries for a
future release without hosting any third-party images or annotations.

## Duplicate check and scope

Compared canonical names, aliases, official sources and publication identifiers
against the 451-record `hub/catalog.json` at commit
`65104e4028a22e355f7d2cfc4d6919487fb4036b`. Searches for TJDR, INSPIRE and
IIIT DR Eye Tracking did not identify standalone counterparts. GitHub issue
and PR searches likewise found no matching proposal during this check.
Name absence is not proof of non-overlapping cohorts; provenance relationships
still need maintainer review. No new cohort-independence claim is made.

CONTRIBUTING.md requests an issue before implementation. Attempting to create
the upstream issue returned HTTP 403 from the integration; issues are disabled
in the contributor fork. This proposal therefore deliberately stops short of
runtime registration. Please advise whether these entries are in scope and
whether to split them into individual implementation PRs.

## TJDR

- Proposed slug: `tjdr`.
- Full name: TJDR: A High-Quality Diabetic Retinopathy Pixel-Level Annotation Dataset.
- Official metadata, count, modality, tasks and citation evidence:
  <https://github.com/NekoPii/TJDR>.
- Source-reported count/unit: **561 color fundus images**. Use the original
  count, not a count after local deduplication.
- Task: diabetic-retinopathy lesion segmentation. Source annotation categories:
  microaneurysms, hemorrhages, hard exudates and soft exudates.
- Splits: the provider documents training/testing; split sizes and fixed image
  dimensions are not established by this landing-page review.
- Publication: Mao J, Ma X, Bi Y, Zhang R. *TJDR: A High-Quality Diabetic
  Retinopathy Pixel-Level Annotation Dataset*. arXiv:2312.15389 (2023),
  <https://arxiv.org/abs/2312.15389>. The provider also requests citation of its
  2024 IEEE Transactions on Big Data article; verify its identifier separately.
- Dataset DOI: not established. Do not substitute the article identifier.
- Access: the author repository links OneDrive and Google Drive. Only the
  landing page was reviewed; transfer and authentication requirements are
  **unverified**, not anonymous by assumption.
- Dataset-file license: **Unknown**. The repository displays Apache-2.0, but
  its applicability to the externally hosted clinical image files remains
  unconfirmed. Preserve that distinction rather than inheriting a code license.
- Proposed implementation: metadata-only, manual guidance, no parser and no
  automatic download until source terms and route behavior are clarified.

## INSPIRE-AVR

- Proposed slug: `inspire_avr`.
- Full name: INSPIRE-AVR, Iowa Normative Set for Processing Images of the REtina.
- Official metadata, count, modality, task, access and terms evidence:
  <https://eye.medicine.uiowa.edu/inspire-datasets>.
- Source-reported count/unit: **40 color fundus images** with an
  arteriolar-to-venular width-ratio reference standard averaged from two experts'
  assessments using IVAN.
- Task: measurement/regression. Do **not** claim pixel-level segmentation masks
  on the basis of this provider page.
- Publication: Niemeijer et al. *Automated Measurement of the
  Arteriolar-To-Venular Width Ratio in Digital Color Fundus Photographs*.
  IEEE Transactions on Medical Imaging (2011).
  Associated-publication DOI: <https://doi.org/10.1109/TMI.2011.2159619>.
- Dataset DOI: not established. Splits, fixed dimensions: not established here.
- Access: guided/manual provider request form; no form submitted and no
  agreement accepted. Account, approval and DUA flags remain unknown until
  independently verified. No transfer was tested.
- Dataset-file terms: research/education use is stated, with source restrictions
  on redistribution and commercial use. Exact relevant excerpt:
  “Copying, redistribution, and any commercial use is prohibited.”
  Provider acquisition and citation are also required. Proposed family:
  `research-only`; scope: dataset files. No redistribution mirror proposed.
- Proposed implementation: manual instructions and explicit stub loader.

## IIIT DR Eye Tracking

- Proposed slug: `iiit_dr_eye_tracking`.
- Human-readable name: IIIT DR Eye Tracking — Scan, dwell, decide.
- Official metadata, count, modalities, task, access and citation evidence:
  <https://cvit.iiit.ac.in/projects/mip/DR_Eye_Tracking/Home.php>.
- Source-reported count/unit: **40 fundus stimulus images**, viewed by
  **56 participants**. These are distinct quantities, not 56 images or
  2,240 independent images.
- Modalities: fundus and eye tracking. Task: gaze analysis during DR assessment.
  Do not assert delivered per-image classification labels from study design
  alone; their encoding requires archive inspection.
- Publication: Rangrej SB, Sivaswamy J, Srivastava P. *Scan, dwell, decide:
  strategies for detecting abnormalities in diabetic retinopathy*. PLOS ONE
  (2018). Associated-publication DOI:
  <https://doi.org/10.1371/journal.pone.0207086>.
- Dataset DOI, official splits, fixed image dimensions: not established here.
- Access: the provider page links a DR Eye Tracking archive. Transfer and
  access requirements were not tested; report them as unverified.
- Dataset-file license: **Unknown**; no explicit data-file license was found
  on the landing page. Do not inherit the publication license.
- Distinctness: do not conflate this study with the catalog's other glaucoma
  or DR eye-movement studies solely because both contain fundus/gaze data.
- Proposed implementation: metadata-only, manual guidance and explicit stub.

## Follow-up and validation

Before runtime registration: resolve the issue-first discussion, record
tri-state access flags, preserve source terms, review cohort relationships,
add classes to appropriate modules, register them, add offline preflight and
failure-behavior tests, update the runtime count, and decide with maintainers
which generated surfaces belong to a future release. Preserve frozen release
artifacts and never label these proposals as accepted entries.

This proposal changes documentation only. Unmodified upstream baseline tests
in the contributor's environment returned 179 passed and 3 failed: two optional
credential env-file loading cases and one temporary-filesystem space preflight.
These are baseline/environment observations, not a passing implementation
claim. No dataset transfer was performed.

AI assistance: prepared with OpenAI Codex. Public-source evidence and unknowns
are provided for human verification; maintainer acceptance is not assumed.

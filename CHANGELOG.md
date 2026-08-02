# Changelog

All notable changes to EyeDataHub are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2026-08-01

### Added

- Added 135 source-checked Dryad records after a reproducible review of 722
  unique official API results, bringing the catalog to 386 records.
- Added the complete Dryad decision ledger, catalog-ready source records,
  taxonomy and quantity checks, and authenticated API validation metadata.
- Added source-reported quantities for 55 Dryad records, including the two
  previously cataloged Dryad resources inspected at file level.
- Added 11 source-supported relationship assertions, including documented
  cohort overlap among four Moorfields neovascular AMD records and a Dryad
  derivative of DRIVE.

### Changed

- Updated the catalog cutoff to 1 August 2026 and the package version to 0.4.0.
- Recomputed current totals as 300 records with resolved primary quantities,
  364 quantity statements, and 142 directed relationship assertions involving
  94 records.
- Classified Dryad, Figshare, Hugging Face, Kaggle, Mendeley Data, PhysioNet,
  and Zenodo as platform-credential routes; source-hosted links, Google Drive,
  and GitHub remain routes without platform credentials.
- Updated the practical route partition to 33 routes without platform
  credentials, 293 platform-credential routes, and 60 manual procedures.
- Collapsed reciprocal symmetric relationship assertions for website display
  while preserving all directed assertions in the machine-readable graph.
- Revised the Scientific Data manuscript and supplement around catalog breadth,
  quantities, relationships, source-stated terms, and reproducible discovery.

### Security

- Dryad tokens and client credentials are used only at run time and are never
  written to public logs. Downloaded third-party files were removed after the
  dated inspection.

## [0.3.0] - 2026-08-01

### Added

- Added a source-reported quantity model and dated review covering all 251
  records, with 245 resolved primary quantities, 305 evidence rows, and exact
  units kept separate.
- Added clickable relationship tags and filters to the website explorer and
  record pages.
- Added a catalog-wide, source-supported relationship graph with 131 directed
  assertions involving 91 records, plus one review row for every catalog
  record and separate unresolved and rejected-candidate logs.
- Added controlled relationship types for derivation, subsets, versions,
  mirrors, collection components, extensions, replacements, and documented
  cohort overlap.
- Added a 251-row acquisition-verification ledger with separate controlled
  vocabularies for acquisition method and strongest verification evidence.
- Added machine-readable acquisition summaries by backend, access route,
  method, and evidence level, plus retained initial failure outcomes and a
  resource-level citation file.
- Added record-level acquisition and loader reliability tests and a redacted
  evidence package for the Scientific Data submission.

### Changed

- Corrected the current RAO and Retinal Corrugations deposits to version 2 and
  reconciled their identifiers, quantities, and source citations.
- Classified official platform authentication responses as credential or
  client requirements rather than dataset download failures, and removed
  signed redirect query strings and credential values from public artifacts.
- Corrected source-supported metadata for FairVLMed, CORN Pro, MuReD, Ophora,
  and X-PCR, and replaced unsupported name-based overlap claims with reviewed
  relationship assertions.
- Improved resumable transfers, retry behavior, archive extraction safety,
  platform error handling, and dataset-specific completion checks.
- Reclassified HYAMD as controlled or manual access after source
  reconciliation, giving 170 anonymous and 28 controlled or manual routes.
- Revised the manuscript evidence taxonomy so completed transfers, existing
  local holdings, file listings, route confirmations, and unresolved loader
  failures are reported separately.

## [0.2.2] - 2026-07-25

### Added

- Added the current combined CORN corneal-confocal collection record from
  Zenodo, with its restricted request route, dataset DOI, source terms, and
  explicit overlap relationships to the existing CORN component records.

### Changed

- Expanded component-modality tags for resources that contain more than one
  data type, including OCT-plus-fundus and imaging-plus-tabular resources.
- Updated the website explorer to filter and display all contained modalities
  and to calculate every displayed count from the generated catalog payload.
- Updated catalog exports, documentation, and tests for 251 records and 27
  controlled or manual routes.

## [0.2.1] - 2026-07-25

### Changed

- Removed three records whose official acquisition routes were unavailable;
  the current catalog contains 250 records across 18 primary categories.
- Expanded multimodal records into multi-valued component-modality tags so
  resources containing fundus, OCT, text, tabular, or other data are returned
  by every relevant modality search.
- Updated catalog exports, documentation, and tests to use the revised catalog
  and overlapping modality counts.
- Replaced the unverified MIGS article-only entry with its official Zenodo
  record, dataset DOI, CC BY 4.0 terms, reported video count, and tested file
  listing.

## [0.2.0] - 2026-07-21

### Added

- Granular access-friction, availability, acquisition-support, source-term
  scope, typed-identifier, modality, relationship, field-provenance, and
  verification metadata.
- Side-effect-free `search`, `show`, `cite`, and `preflight` workflows.
- Explicit `download` behavior with manual-route blocking, structured exit
  statuses, official-source transfer, and local provenance manifests.
- Added catalog, access-verification, acquisition-validation, loader-support,
  curation, completeness, and conformance outputs.
- Manually specified expected-search fixtures and acquisition/failure-mode
  tests.

### Changed

- Repositioned the public product as a command-line dataset access tool backed
  by a versioned catalog snapshot; the internal `REGISTRY` name remains for
  compatibility.
- Separated source-stated terms from acquisition friction and automation
  support; unknown values are no longer treated as unrestricted.
- Expanded the bounded snapshot to 253 records across 18 primary categories.
- Corrected multiple official routes and platform identifiers after live
  source checks.
- Updated documentation, contribution workflow, tests, and release metadata.

### Safety

- Search and inspection remain read-only; transfer requires an explicit user
  command.
- EyeDataHub does not accept click-through terms or agreements, automate
  controlled routes, or record credentials in provenance logs.

## [0.1.0] - 2026-07-04

### Added

- Initial public catalog of 188 ophthalmic and eye-related datasets.
- License-family normalization for commercial-OK, non-commercial,
  research-only, and unknown source terms.
- Access backends for direct HTTP, Kaggle, Hugging Face, Zenodo, Mendeley
  Data, Figshare, Google Drive, PhysioNet, Synapse, GitHub, and manual/gated
  sources.
- `eyehub list`, `eyehub show`, and `eyehub download` commands.
- Python API through `eyedatahub.datasets.registry.REGISTRY`.
- Read-only MCP server at `python -m eyedatahub.agent.mcp_server`.

# EyeDataHub catalog snapshot

This documentation describes the 0.5.0 catalog release.

The catalog contains 479 manually source-checked ophthalmology data
resources across 18 primary navigation categories. This is a bounded,
date-stamped catalog, not a complete census and not a collection of 479
independent cohorts. EyeDataHub does not host or redistribute the indexed
third-party datasets.

## Catalog summary

| Metric | Count |
|---|---:|
| Catalog records | 479 |
| Primary categories | 18 |
| No-account source links | 46 |
| Self-service authenticated routes | 384 |
| Self-service click-through routes | 11 |
| Controlled or manual routes | 30 |
| Author-contact routes | 8 |
| Routes without platform credentials | 33 |
| Platform API or client routes | 375 |
| Manual, controlled, institutional, or author-contact procedures | 71 |
| Records with a resolved primary source-reported quantity | 328 |
| Source-supported directed relationship assertions | 153 |
| Records participating in documented relationships | 100 |

Access requirements, download implementation, source review, and source-stated
terms are independent dimensions. A self-service route does not establish
permission for a proposed reuse. Relationship counts are directed assertions,
not counts of independent cohorts.

The descriptive source-term groups are:

- `standard-no-nc`: source terms without an explicit noncommercial clause;
- `non-commercial`: a recorded noncommercial clause;
- `research-only`: research, challenge, or similarly restricted source text;
- `unknown`: the source evidence is insufficient.

These labels are screening metadata, not legal advice. Terms scope is recorded
separately because a publication, code, website, metadata index, and dataset
files can have different terms.

## Query and inspect

```bash
# Read-only discovery and inspection
eyehub search --modality oct
eyehub search --access anonymous_direct --json
eyehub show airogs --json
eyehub cite airogs --type dataset --format bibtex

# Source terms, access requirements, loader status, and intended action
eyehub preflight airogs --json
eyehub download airogs --data-dir ./data --dry-run --json
```

## Explicit acquisition

```bash
# Transfer begins only through this explicit non-dry-run command
eyehub download <resource> --data-dir ./data
```

EyeDataHub never accepts click-through terms, licenses, or data-use agreements
for a user. Manual and controlled routes return official instructions without
imitating a successful download. Successful supported transfers create a local
provenance manifest with the catalog release, source route, source-stated
terms, authentication category without secrets, acquired files, sizes, local
checksums, citations, warnings, and completion scope.

## Catalog exports

Complete machine-readable catalog exports are provided in `hub/catalog.json`,
`hub/catalog.csv`, and `website/static/datasets.json`. The files
`hub/open_licence_catalogue.json`, `hub/metadata.json`, and `hub/metadata.csv`
are legacy compatibility artifacts and must not be used as the
complete-catalog denominator. Run `python hub/export_catalog.py` to
regenerate the complete exports and `python -m pytest -q` to validate the
catalog and command-line behavior.

Each complete-catalog record includes `reported_quantities`: an ordered list
of source-linked count objects with `count`, `unit`, `scope`, `evidence_url`,
`evidence_basis`, `primary`, `exactness`, `review_date`, and `notes`. The
backward-compatible `num_samples` and `item_count_unit` fields match the one
primary quantity when a primary quantity is resolved. Units are controlled
vocabulary values; totals are reported only within the same unit and must not
be interpreted as independent cohort totals.

The live Python implementation retains
`eyedatahub.datasets.registry.REGISTRY` as an internal compatibility name.

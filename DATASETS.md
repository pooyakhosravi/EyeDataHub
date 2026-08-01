# EyeDataHub catalog snapshot

This documentation describes the 0.3.0 catalog release.

The catalog contains 251 manually source-checked ophthalmology data
resources across 18 primary navigation categories. This is a bounded,
date-stamped catalog, not a complete census and not a collection of 251
independent cohorts. EyeDataHub does not host or redistribute the indexed
third-party datasets.

## Catalog summary

| Metric | Count |
|---|---:|
| Catalog records | 251 |
| Primary categories | 18 |
| Anonymous direct routes | 170 |
| Self-service authenticated routes | 34 |
| Self-service click-through routes | 11 |
| Controlled or manual routes | 28 |
| Author-contact routes | 8 |
| Complete current-deposit transfers through EyeDataHub | 47 |
| Representative pre-existing holdings | 5 |
| Listing-only strongest evidence | 4 |
| Route-only strongest evidence | 195 |
| Cumulative metadata or listing confirmations | 14 |
| Unresolved automated listing failures | 2 |

Access friction, acquisition implementation, verification evidence, and
source-stated terms are independent dimensions. The strongest evidence levels
above are mutually exclusive; the cumulative listing count overlaps eight
complete transfers and two representative holdings. A self-service route does
not establish permission for a proposed reuse, and a route confirmation is not
a file transfer.

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
contain the 137-record enriched EyeDataHub-Open subset and must not be used as
the complete-catalog denominator. Run `python hub/export_catalog.py` to
regenerate the complete exports and `python -m pytest -q` to validate the
catalog and command-line behavior.

The live Python implementation retains
`eyedatahub.datasets.registry.REGISTRY` as an internal compatibility name.

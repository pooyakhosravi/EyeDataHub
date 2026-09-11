# EyeDataHub

EyeDataHub is a versioned, community-extensible, source-terms- and access-aware
command-line tool backed by a manually curated ophthalmology dataset snapshot.
It helps users find, inspect, cite, preflight, and acquire supported resources
from their official sources.

EyeDataHub does **not** host or redistribute the indexed third-party datasets.
It does not accept source terms for users or determine legal permission,
ethical acceptability, data quality, clinical validity, or scientific
suitability.

[![License: MIT](https://img.shields.io/badge/code-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)
[![Catalog](https://img.shields.io/badge/catalog-451%20current%20records-brightgreen.svg)](DATASETS.md)
[![Tests](https://img.shields.io/badge/tests-146%20passing-brightgreen.svg)](tests)

## One-minute overview

The development branch supports initial dataset publication dates, sourced
date entries, chronological search, and website year filters. Unknown dates
remain explicit. See [publication dates](docs/PUBLICATION_DATES.md) for the
field definitions, search examples, and how to contribute missing dates.

Release 0.7.0 contains 451 manually source-checked records across
18 primary categories, representing 446 narrowly defined dataset families. At the
catalog cutoff on 2 August 2026:

- 33 use source-hosted file, Google Drive, or GitHub routes;
- 350 use repository or challenge-platform APIs or clients;
- 68 use manual, controlled, institutional, or author-contact procedures.

These practical groups are mutually exclusive. Separately, the catalog records
the source interaction visible to a user:

- 47 used a source link requiring neither an account nor manual approval;
- 356 required immediate self-service authentication;
- 11 required user click-through;
- 29 required controlled or manual access;
- 8 required author contact.

Backend and user-facing access requirements are intentionally separate. A
publicly viewable repository record may use an API or client route without
requiring an authenticated user account.

The 451-record working catalog was reviewed for documented reuse, derivation,
subset, version, mirror, component, and cohort-overlap relationships. The reviewed
graph contains 145 directed assertions involving 96 records. Thirty-three
records have documented derivation from another catalog resource, including 16
of the 17 annotation layers; three records are separately indexed components.
The current-version review preserves two earlier releases and two unmodified
repository copies as links rather than catalog records. The complete
record matrix, edge evidence, unresolved upstream resources, and rejected
false-positive links are in `hub/audit/resource_relationship_*_2026-08-02.*`;
the role, family, and current-version decisions are in
`hub/audit/resource_identity_*_2026-08-02.*`.

A separate source review resolved a primary reported quantity for 324 records
and retained 396 quantity-evidence rows. Totals are reported only within exact
units because related resources can overlap and different modalities use
different counting units. The record, evidence, unit-summary, and unresolved
files are in `hub/audit/resource_quantity_*_2026-08-02.*`.

The repository searches returned 18,737 records across Dryad, Mendeley Data,
Kaggle, Figshare, and Hugging Face. Human/model-use screening, duplicate
reconciliation, and source review identified 288 eligible repository records;
163 catalog records came from the other documented search routes. Within the
145 Dryad-backed candidates reviewed specifically for reusable model inputs or
targets, 82 were retained and 63 were excluded. The exclusions remain visible
in the dated screening ledger, including 58 nonhuman records and two
analysis-only deposits.

The corresponding Mendeley review examined 141 records after official deposit
inspection. It retained 116 resources and excluded 25: 20 did not meet the
model-use boundary, and five records with uncertain value were removed at the
author's direction.

The complete machine-readable exports are `hub/catalog.json` and
`hub/catalog.csv`. Legacy `hub/metadata.*` and
`hub/open_licence_catalogue.json` files are compatibility artifacts, not
complete-catalog exports, and are not used for current manuscript counts.

## Install

Install release 0.7.0 from [PyPI](https://pypi.org/project/eyedatahub/):

```bash
python -m pip install "eyedatahub==0.7.0"
```

EyeDataHub is tested on Python 3.10 through 3.14.

To install the same release directly from its Git tag:

```bash
python -m pip install "git+https://github.com/pooyakhosravi/EyeDataHub.git@v0.7.0"
```

For development:

```bash
git clone https://github.com/pooyakhosravi/EyeDataHub.git
cd EyeDataHub
python -m pip install -e .
```

Optional platform clients are available through `.[kaggle]`,
`.[huggingface]`, `.[synapse]`, or `.[full]`.

## Safe command-line workflow

```bash
# Read-only discovery
eyehub search --modality oct --access anonymous_direct
eyehub search --task segmentation --source-terms standard-no-nc --json

# Read-only record and citation inspection
eyehub show fives --json
eyehub cite fives --type dataset --format bibtex

# Read-only acquisition preflight
eyehub download fives --data-dir ./data --dry-run --json

# Explicit transfer from the represented official source
eyehub download fives --data-dir ./data --json
```

Search, `show`, `cite`, Python queries, JSON, JSON-LD, and the optional MCP
server are read-only. Only an explicit non-dry-run `download` command may start
transfer. Manual, controlled, author-contact, unavailable, and unsupported
routes return structured status and instructions instead of imitating success.

## What source-terms-aware means

Before acquisition, EyeDataHub displays:

- the raw source-stated terms and evidence URL;
- whether the terms appear to apply to data, metadata, code, a publication,
  challenge participation, mixed components, or an unknown scope;
- registration, authentication, token, click-through, manual approval,
  agreement, author-contact, and institutional restrictions;
- route-verification date and loader test scope;
- warnings for unknown, research-only, noncommercial, no-derivatives, or mixed
  terms.

The tool blocks manual authorization routes, never accepts agreements, and
writes a provenance manifest after successful transfer. This behavior is not
legal advice. The descriptive `standard-no-nc` filter means only that the
normalized source label contains no explicit noncommercial clause; it does not
establish permission for a proposed use.

## Python

```python
from pathlib import Path

from eyedatahub.acquisition import acquire_dataset, preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

dataset = REGISTRY.get_dataset("ophthalwechat")
data_dir = Path("./data")

plan = preflight_dataset(dataset, data_dir)       # read-only
result = acquire_dataset(dataset, data_dir)       # explicit transfer request
print(result.status, result.manifest_path)
```

`REGISTRY` is the retained internal Python class name. Public-facing release
artifacts use *catalog* and *snapshot* because EyeDataHub is not a data
repository.

## Credentials and security

Copy [.env.example](.env.example) to a private `.env` file or use each
platform's supported credential mechanism. EyeDataHub records only an
authentication category or credential presence, never credential values.
`.env` and acquired data directories must not be committed.

Supported backends include official Figshare, Zenodo, Mendeley Data, Dryad,
Kaggle, Hugging Face, PhysioNet, Dataverse, Synapse, GitHub, Google Drive, and
source-hosted file links. Support varies by record and is exposed through
`acquisition_support` and `loader_test_scope`.

## Release record

The 0.7.0 release contains the catalog, schema, source-review logs, resource
citations, documentation, regeneration scripts, and release checksums, but no
indexed third-party dataset files. The Git tag and attached scientific archive
identify the same immutable catalog state. The version-specific scientific
archive is available at [doi:10.5281/zenodo.21798623](https://doi.org/10.5281/zenodo.21798623).

See [CONTRIBUTING.md](CONTRIBUTING.md) for reviewed additions and
[CLAUDE.md](CLAUDE.md) for the canonical agent guide.

## Citation and licences

Use [CITATION.cff](CITATION.cff) for the software citation and cite each
acquired dataset from its official source. EyeDataHub code is MIT licensed;
the catalog metadata are CC BY 4.0. Third-party data remain under their
source-specific terms and access controls.

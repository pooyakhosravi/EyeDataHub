# EyeDataHub

EyeDataHub is a versioned, community-extensible, license- and access-aware
command-line tool backed by a manually curated ophthalmology dataset snapshot.
It helps users find, inspect, cite, preflight, and acquire supported resources
from their official sources.

EyeDataHub does **not** host or redistribute the indexed third-party datasets.
It does not accept source terms for users or determine legal permission,
ethical acceptability, data quality, clinical validity, or scientific
suitability.

[![License: MIT](https://img.shields.io/badge/code-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)
[![Catalog](https://img.shields.io/badge/catalog-251%20records-brightgreen.svg)](DATASETS.md)
[![Tests](https://img.shields.io/badge/tests-46%20passing-brightgreen.svg)](tests)

## One-minute overview

The current catalog contains 251 manually source-checked records across 18
primary categories. At the final catalog update on 25 July 2026:

- 171 routes were anonymous direct;
- 34 required immediate self-service authentication;
- 11 required user click-through;
- 27 required controlled or manual access;
- 8 required author contact.

Acquisition support is separate from access: one official deposit completed an
end-to-end transfer test, 13 routes passed partial API or file-listing checks,
and all other loader states are labelled by their actual test scope.

## Install

PyPI: [pypi.org/project/eyedatahub](https://pypi.org/project/eyedatahub/)

```bash
python -m pip install "eyedatahub==0.2.2"
```

EyeDataHub is tested on Python 3.10 through 3.14.

To install the same release directly from its Git tag:

```bash
python -m pip install "git+https://github.com/pooyakhosravi/EyeDataHub.git@v0.2.2"
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

## What “license-aware” means

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
direct-file routes. Support varies by record and is exposed through
`acquisition_support` and `loader_test_scope`.

## Release record

The release DOI is
[doi:10.5281/zenodo.21614657](https://doi.org/10.5281/zenodo.21614657).
The Zenodo record contains a README that directs users to this repository;
software and catalog files are distributed from GitHub.

See [CONTRIBUTING.md](CONTRIBUTING.md) for reviewed additions and
[CLAUDE.md](CLAUDE.md) for the canonical agent guide.

## Citation and licences

Use [CITATION.cff](CITATION.cff) for the software citation and cite each
acquired dataset from its official source. EyeDataHub code is MIT licensed;
the catalog metadata are CC BY 4.0. Third-party data remain under their
source-specific terms and access controls.

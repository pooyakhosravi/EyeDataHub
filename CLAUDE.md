# CLAUDE.md — canonical agent guide

## Product boundary

EyeDataHub is a versioned, community-extensible, license- and access-aware
command-line tool backed by a manually curated ophthalmology dataset snapshot.
Release 0.7.0 contains 451 current records across 18 primary categories,
representing 446 narrowly defined dataset families.

The scientific output is the date-stamped metadata and availability snapshot. The
practical output is the `eyehub` command line for discovery, citation,
preflight, and supported official-source acquisition. Reviewed pull requests
feed later releases; they do not mutate the analyzed snapshot.

EyeDataHub does not host or redistribute indexed third-party datasets and does
not determine legal permission, ethics, quality, clinical validity, or
scientific suitability. Use *catalog*, *snapshot*, *access tool*, or
*acquisition layer* in public prose. `REGISTRY` remains an internal class name.

## Repository map

```text
eyedatahub/
  acquisition.py          preflight, blocking, explicit transfer, manifests
  catalog.py              deterministic serialization, search, citations
  cli.py                  search/show/cite/preflight/download commands
  core/metadata.py        access, automation, terms scope, typed identifiers
  datasets/               dataset records and loader backends
  agent/mcp_server.py     optional read-only stdio JSON-RPC interface
hub/audit/                URL, access, and acquisition validation
tests/                    deterministic unit, command, and expected-result tests
```

Use `eyedatahub` for Python imports and `eyehub` for command examples.

## Public workflow

```bash
eyehub search --modality oct --access anonymous_direct --json
eyehub show <record> --json
eyehub cite <record> --type dataset --format bibtex
eyehub download <record> --data-dir <directory> --dry-run --json
eyehub download <record> --data-dir <directory> --json
```

Search, show, cite, Python, JSON, JSON-LD, and MCP operations are read-only.
Only an explicit non-dry-run download command may invoke a loader.

## Metadata discipline

Keep these dimensions independent:

- `access_friction`: anonymous, self-service, controlled, author-contact,
  secure/model-to-data, unavailable, or unverified.
- `acquisition_support`: complete, partial, implemented, platform-supported,
  guided, blocked, unsupported, or unavailable.
- `source_terms`, `license_family`, `terms_scope`, and evidence URL.

Access flags are true, false, or unknown. Never silently turn missing values
into false. Preserve raw source terms. A publication, site, or code licence is
not a dataset licence. Dataset DOI, dataset accession, repository identifier,
article DOI, software DOI, and challenge identifier are separate fields.

`standard-no-nc` is a descriptive normalized-label group, not a permission
finding. The legacy `commercial-ok` and `open` aliases may remain only for
backward compatibility; do not use them in new public claims.

## Acquisition rules

- Preflight must display terms, evidence, scope, access requirements, route
  date, loader state, and warnings.
- Never accept click-through terms, licences, or agreements for a user.
- Block controlled, manual, author-contact, secure, unavailable, and
  unsupported routes.
- Never print credential values.
- Successful transfers create `eyedatahub-acquisition-manifest.json`.
- Do not call a landing-page or file-listing check a complete download.
- Do not bulk-download during exploration.

## Adding or correcting records

Follow `CONTRIBUTING.md` and `.github/PULL_REQUEST_TEMPLATE.md`. Require an
official source and field-level evidence for terms, scope, access, identifiers,
count/unit, modality, task, citation, loader behavior, and relationships.
Retain unavailable records with dated status when historically useful; do not
silently delete them.

## Required checks

```bash
python -m pip install -e .
python -m pytest -q
eyehub --help
eyehub --version
eyehub search --modality oct --json
eyehub show fives --json
eyehub download corn_pro --dry-run --json
```

Live network checks are explicit and are not part of every pull request:

```bash
python -m hub.audit.verify_urls
python hub/audit/validate_acquisition.py --out <path>
```

Never expose secrets or claim current external state from a stale log.

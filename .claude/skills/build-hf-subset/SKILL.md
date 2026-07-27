---
name: build-hf-subset
description: Prepare a metadata-only Hugging Face catalog view or, only with independently documented authorization, a user-owned data subset outside EyeDataHub.
---

# Skill: Hugging Face catalog view

EyeDataHub does not host or redistribute indexed third-party datasets. The
default workflow publishes metadata and official-source links only.

## Metadata-only workflow

1. Select records with `eyehub search --json`.
2. Inspect every candidate with `eyehub show` and `eyehub preflight`.
3. Export record identifiers, official URLs, raw source terms, evidence, terms
   scope, access requirements, citations, verification dates, and EyeDataHub
   version. Do not include source data files.
4. Generate a dataset card that states that the catalog view does not grant
   permission and that acquisition remains at the official host.
5. Dry-run and review the exact files before a user-authorized upload.

## Data-file workflow: hard gate

Do not copy or upload third-party files based only on an EyeDataHub normalized
term or access route. Proceed only when the user supplies independently
reviewed, component-specific authorization for redistribution and explicitly
authorizes the external upload. Preserve source provenance, terms, required
attribution, versions, checksums, and restrictions. Exclude any record with
unknown scope, unknown terms, manual/controlled access, author contact,
non-redistribution language, or unresolved conflict.

The resulting user-owned artifact is outside the EyeDataHub release and must
not be described as an official EyeDataHub mirror.

## Safety

- Never upload credentials, restricted URLs, agreements, or private data.
- Never bulk-download the catalog.
- Never accept click-through terms or agreements for a user.
- Never treat availability as permission.
- Stop when authorization or source scope is unclear.

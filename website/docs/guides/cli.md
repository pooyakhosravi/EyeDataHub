---
id: cli
title: "Command-line guide"
sidebar_label: Command line
description: "Search, inspect, cite, preflight, and acquire supported ophthalmology datasets with eyehub."
---

# Command-line guide

`eyehub` queries a versioned catalog and, after explicit preflight, can transfer
supported resources from official hosts. EyeDataHub does not host third-party
data or determine legal permission or scientific suitability.

## Search without side effects

```bash
eyehub search
eyehub search --modality oct
eyehub search --task segmentation --task classification --json
eyehub search --access anonymous_direct --json
eyehub search --source-terms research-only --json
eyehub search --acquisition-support end_to_end_tested --json
```

Contained modalities are multi-valued, so a multimodal resource can be found
through each represented modality. JSON results are deterministically ordered.

## Inspect and cite one record

```bash
eyehub show airogs
eyehub show airogs --json
eyehub cite airogs --type dataset --format bibtex
eyehub cite airogs --type article --format json
eyehub cite airogs --type software --format plain
```

Dataset, associated-publication, and software identifiers are separate. An
empty typed identifier remains empty rather than being guessed from another
object's DOI.

## Preflight

```bash
eyehub preflight airogs --json
eyehub download airogs --data-dir ./data --dry-run --json
```

Preflight reports raw source-stated terms, their evidence URL and apparent
scope, authentication/registration/click-through/manual requirements, the
current route check, loader support, warnings, and the action the software
would take. Dry run starts no transfer and creates no destination directory.

## Explicit acquisition

```bash
eyehub download <resource> --data-dir ./data
```

Only this explicit non-dry-run command may start a transfer. Supported routes
use the official host and write a local provenance manifest. Controlled,
manual, author-contact, unavailable, and unsupported routes return a structured
status and official instructions instead of imitating a successful download.
EyeDataHub never accepts source terms, click-throughs, licences, or data-use
agreements for a user.

Platform credentials are supplied through the platform's documented client or
environment/configuration mechanism. Credentials are not printed or stored in
manifests or validation logs. See `SECURITY.md` before testing an authenticated
route.

## Reproducibility checks

```bash
eyehub --help
eyehub --version
python -m pytest -q
```

The test suite validates catalog behavior and deterministic command output.
Live network checks are separate because external state changes.

---
id: python
title: "Python API Guide"
sidebar_label: Python API
description: "Use EyeDataHub from notebooks, scripts, and training pipelines."
---

# Python API Guide

Use the Python API when you need structured metadata in notebooks, training
scripts, validation manifests, or internal dataset audits.

## Query The Catalog

```python
import eyedatahub as edh

print(len(edh.REGISTRY.list_datasets()))
ds = edh.REGISTRY.get_dataset("airogs")
print(ds.info.full_name)
print(ds.info.license_family)
```

## Filter Datasets

```python
import eyedatahub as edh

oct_datasets = [
    ds for ds in edh.REGISTRY.list_datasets()
    if ds.info.modality == "oct"
]

standard_labels_without_explicit_nc = {
    "cc0", "cc-by", "cc-by-sa", "mit", "apache", "odc-by"
}
source_term_candidates = [
    ds for ds in edh.REGISTRY.list_datasets()
    if ds.info.license_family in standard_labels_without_explicit_nc
]
```

This descriptive grouping is not a permission finding. Check the exact current
source terms, evidence URL, and scope before deciding whether a proposed use is
allowed.

## Preflight And Explicit Acquisition

```python
from pathlib import Path
import eyedatahub as edh
from eyedatahub.acquisition import acquire_dataset, preflight_dataset

data_dir = Path("~/.eyedatahub/data").expanduser()
ds = edh.REGISTRY.get_dataset("ophthalwechat")

plan = preflight_dataset(ds, data_dir)  # read-only
print(plan["source_terms"])
print(plan["terms_evidence_url"])
print(plan["access_requirements"])

if plan["automation_allowed"]:
    result = acquire_dataset(ds, data_dir)  # explicit transfer request
    print(result.status, result.manifest_path)
else:
    print(plan["status"], plan["blocked_reason"])
```

Manual, controlled, author-contact, unavailable, and unsupported routes return
a structured blocked status rather than bypassing source controls. EyeDataHub
does not accept click-through terms or agreements for the user.

## Build A Manifest

```python
import json
import eyedatahub as edh

manifest = []
for ds in edh.REGISTRY.list_datasets():
    i = ds.info
    manifest.append({
        "name": i.name,
        "full_name": i.full_name,
        "modality": i.modality,
        "tasks": i.tasks,
        "license_family": i.license_family,
        "download_type": i.download_type,
        "url": i.download_url,
    })

with open("eyedatahub_manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)
```

## Practical Caveats

- Source-term values are catalog classifications, not legal advice.
- Sample counts are source-reported units and may refer to images, videos,
  reports, records, or visual-field tests depending on the source.
- Patient-level counts, duplicate-image detection, and label harmonization are
  not inferred unless source documentation provides them.

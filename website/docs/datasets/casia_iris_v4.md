---
id: casia_iris_v4
title: "CASIA-IrisV4 Iris Image Database"
sidebar_label: casia_iris_v4
description: "Six near-infrared or synthetic iris subsets spanning close-range, lamp variation, twins, distance, large-scale, and synthetic recognition."
tags: ["iris_biometrics", "cc0", "manual", "biometric_recognition", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CASIA-IrisV4 Iris Image Database

Six near-infrared or synthetic iris subsets spanning close-range, lamp variation, twins, distance, large-scale, and synthetic recognition.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `casia_iris_v4` |
| **Full name** | CASIA-IrisV4 Iris Image Database |
| **Primary category** | `iris_biometrics` |
| **Contained modalities** | iris_biometrics |
| **Tasks** | biometric_recognition, classification |
| **Samples** | 54,601 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.86 GB |
| **Source-stated terms** | Public domain; source access terms apply |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The project documentation mirror reports 54,601 images from more than 1,800 genuine and 1,000 virtual subjects, with possible subject overlap across four subsets, and describes the release as public domain. The linked download service may require login.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download casia_iris_v4 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download casia_iris_v4 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('casia_iris_v4')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [hycasia.github.io/dataset](https://hycasia.github.io/dataset/casia-irisv4/)

**Source-term evidence:** [hycasia.github.io/dataset](https://hycasia.github.io/dataset/casia-irisv4/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{casia_iris_v4,
  title  = { CASIA-IrisV4 Iris Image Database },
  note   = { Chinese Academy of Sciences Institute of Automation. CASIA Iris Image Database Version 4.0. Dataset documentation },
  url    = { https://hycasia.github.io/dataset/casia-irisv4/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Chinese Academy of Sciences Institute of Automation. CASIA Iris Image Database Version 4.0. Dataset documentation.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Public domain; source access terms apply
- **Normalized category:** `cc0`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [nd_iris_0405](./nd_iris_0405.md): ND-IRIS-0405 Iris Image Dataset (64,980 records, `research-only`)
- [ubiris_v2](./ubiris_v2.md): UBIRIS.v2 Noisy Visible-Wavelength Iris Database (11,102 records, `unknown`)

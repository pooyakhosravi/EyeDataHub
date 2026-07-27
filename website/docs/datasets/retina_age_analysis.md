---
id: retina_age_analysis
title: "Retina Age Analysis"
sidebar_label: retina_age_analysis
description: "Fundus images and age labels for retinal age prediction and regression."
tags: ["fundus", "mit", "huggingface", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Retina Age Analysis

Fundus images and age labels for retinal age prediction and regression.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `retina_age_analysis` |
| **Full name** | Retina Age Analysis |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | regression |
| **Samples** | 9,857 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | MIT |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Provenance should be verified before clinical use.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download retina_age_analysis --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download retina_age_analysis --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('retina_age_analysis')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/ramankamran/retina-age-analysis)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/ramankamran/retina-age-analysis)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{retina_age_analysis,
  title  = { Retina Age Analysis },
  note   = { ramankamran/retina-age-analysis. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/ramankamran/retina-age-analysis },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
ramankamran/retina-age-analysis. Hugging Face dataset, accessed 2026-07.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** MIT
- **Normalized category:** `mit`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)

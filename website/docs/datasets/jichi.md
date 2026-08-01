---
id: jichi
title: "Jichi Medical University Diabetic Retinopathy Dataset"
sidebar_label: jichi
description: "9,939 color fundus images from Japanese patients with DR grading labels (Davis grading scale)."
tags: ["fundus", "cc-by", "figshare", "grading", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Jichi Medical University Diabetic Retinopathy Dataset

9,939 color fundus images from Japanese patients with DR grading labels (Davis grading scale).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `jichi` |
| **Full name** | Jichi Medical University Diabetic Retinopathy Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Samples** | 9,939 |
| **Classes** | 4 (Not reported) |
| **Splits** | all |
| **Size** | 10.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download jichi --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download jichi --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('jichi')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.4879853](https://doi.org/10.6084/m9.figshare.4879853)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.4879853](https://doi.org/10.6084/m9.figshare.4879853)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{jichi,
  title  = { Jichi Medical University Diabetic Retinopathy Dataset },
  note   = { Takahashi et al., 'Applying artificial intelligence to disease staging: Deep learning for improved staging of diabetic retinopathy', PLOS ONE 2017. Article: https://pmc.ncbi.nlm.nih.gov/articles/PMC5480986/ },
  year   = { 2017 },
  url    = { https://doi.org/10.6084/m9.figshare.4879853 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Takahashi et al., 'Applying artificial intelligence to disease staging: Deep learning for improved staging of diabetic retinopathy', PLOS ONE 2017. Article: https://pmc.ncbi.nlm.nih.gov/articles/PMC5480986/
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

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

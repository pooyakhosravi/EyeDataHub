---
id: real_fundus
title: "Real Fundus Clinical Image Restoration Benchmark"
sidebar_label: real_fundus
description: "One hundred twenty paired low quality and high quality clinical fundus photographs of the same eyes at 2560 by 2560 pixels for image restoration and enhancement research."
tags: ["fundus", "unknown", "manual", "restoration"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Real Fundus Clinical Image Restoration Benchmark

One hundred twenty paired low quality and high quality clinical fundus photographs of the same eyes at 2560 by 2560 pixels for image restoration and enhancement research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `real_fundus` |
| **Full name** | Real Fundus Clinical Image Restoration Benchmark |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | restoration |
| **Samples** | 120 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.02 GB |
| **Source-stated terms** | Unknown; no dataset license declared in the repository |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The public GitHub release contains the image archive. The paper describes a random 81/9/30 experimental split, but the release does not define distributed train, validation, and test partitions. No license file or dataset use terms were found.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download real_fundus --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download real_fundus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('real_fundus')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/dengzhuo-AI](https://github.com/dengzhuo-AI/Real-Fundus/releases/tag/v.1.0.0)

**Source-term evidence:** [github.com/dengzhuo-AI](https://github.com/dengzhuo-AI/Real-Fundus/releases/tag/v.1.0.0)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{real_fundus,
  title  = { Real Fundus Clinical Image Restoration Benchmark },
  note   = { Deng Z, Cai Y, Chen L, et al. RFormer: Transformer-based generative adversarial network for real fundus image restoration on a new clinical benchmark. IEEE J Biomed Health Inform. 2022;26:4645-4655. doi:10.1109/JBHI.2022.3187103 },
  year   = { 2022 },
  url    = { https://github.com/dengzhuo-AI/Real-Fundus/releases/tag/v.1.0.0 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Deng Z, Cai Y, Chen L, et al. RFormer: Transformer-based generative adversarial network for real fundus image restoration on a new clinical benchmark. IEEE J Biomed Health Inform. 2022;26:4645-4655. doi:10.1109/JBHI.2022.3187103
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; no dataset license declared in the repository
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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

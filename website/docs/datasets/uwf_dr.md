---
id: uwf_dr
title: "UWF DR Reasoning Dataset"
sidebar_label: uwf_dr
description: "Ultra-widefield fundus photographs for diabetic retinopathy grading (5-level ICDR scale). Released alongside the Reasoning-Enhanced VLM paper for interpretable UWF DR detection. Related to the UWF4DR "
tags: ["uwf_fundus", "research-only", "gdrive", "grading", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# UWF DR Reasoning Dataset

Ultra-widefield fundus photographs for diabetic retinopathy grading (5-level ICDR scale). Released alongside the Reasoning-Enhanced VLM paper for interpretable UWF DR detection. Related to the UWF4DR 2024 MICCAI challenge (~495 images across image quality and DR grading tasks).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `uwf_dr` |
| **Full name** | UWF DR Reasoning Dataset |
| **Primary category** | `uwf_fundus` |
| **Contained modalities** | uwf_fundus |
| **Tasks** | grading, classification |
| **Samples** | 495 |
| **Classes** | 5 (No DR, Mild DR, Moderate DR, Severe DR, Proliferative DR) |
| **Splits** | train, val, test |
| **Size** | 2.0 GB |
| **Source-stated terms** | Research only — see paper terms |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download uwf_dr --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download uwf_dr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('uwf_dr')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/drive](https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu)

**Source-term evidence:** [drive.google.com/drive](https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('uwf_dr')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{uwf_dr,
  title  = { UWF DR Reasoning Dataset },
  note   = { Reasoning-Enhanced Vision-Language Model for Interpretable Diabetic Retinopathy Detection in Ultra-Wide-Field Fundus Images. OMIA 2025 (MICCAI Workshop), Springer. DOI: 10.1007/978-3-032-10351-2_12 },
  year   = { 2025 },
  url    = { https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Reasoning-Enhanced Vision-Language Model for Interpretable Diabetic Retinopathy Detection in Ultra-Wide-Field Fundus Images. OMIA 2025 (MICCAI Workshop), Springer. DOI: 10.1007/978-3-032-10351-2_12
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only — see paper terms
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 records, `cc-by`)
- [tsukazaki_uwf](./tsukazaki_uwf.md): Tsukazaki Hospital UWF Fundus Dataset (13,047 records, `research-only`)
- [birdshot_wide](./birdshot_wide.md): Birdshot-WIDE Widefield Fundus Dataset (6,352 records, `cc-by`)
- [deepdrid](./deepdrid.md): DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset (2,256 records, `cc-by-sa`)
- [uwf_tumor](./uwf_tumor.md): UWF Fundus Intraocular Tumor Dataset (2,031 records, `cc-by`)
- [uwf_dr_peng](./uwf_dr_peng.md): UWF Fundus DR Dataset (Peng et al., 2026) (1,630 records, `cc-by`)
- [uwf_zhejiang](./uwf_zhejiang.md): Open UWF Fundus Dataset with Disease + Quality Labels (700 records, `cc-by`)

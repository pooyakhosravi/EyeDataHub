---
id: octid
title: "OCTID: OCT Image Database"
sidebar_label: octid
description: "500 OCT images: NORMAL (206), AMD (50), CSC (128), DR (59), MH (57). High-resolution B-scans for 5-class classification."
tags: ["oct", "cc0", "manual", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCTID: OCT Image Database

500 OCT images: NORMAL (206), AMD (50), CSC (128), DR (59), MH (57). High-resolution B-scans for 5-class classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `octid` |
| **Full name** | OCTID: OCT Image Database |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Samples** | 500 |
| **Classes** | 5 (NORMAL, AMD, CSC, DR, MH) |
| **Splits** | all |
| **Size** | 0.3 GB |
| **Source-stated terms** | CC0 1.0 Universal |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Freely available from Borealis Data Repository. No account required.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download octid --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download octid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('octid')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [borealisdata.ca/dataverse](https://borealisdata.ca/dataverse/OCTID)

**Source-term evidence:** [borealisdata.ca/dataverse](https://borealisdata.ca/dataverse/OCTID)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('octid')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{octid,
  title  = { OCTID: OCT Image Database },
  note   = { Gholami et al., 'OCTID: Optical Coherence Tomography Image Database', Elsevier 2020 },
  year   = { 2020 },
  url    = { https://borealisdata.ca/dataverse/OCTID },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Gholami et al., 'OCTID: Optical Coherence Tomography Image Database', Elsevier 2020.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0 Universal
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 records, `cc-by`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 records, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 records, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)

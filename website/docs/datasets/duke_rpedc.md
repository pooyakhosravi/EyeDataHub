---
id: duke_rpedc
title: "Duke RPE-Drusen Complex OCT Dataset"
sidebar_label: duke_rpedc
description: "OCT data from 384 subjects, including 269 with AMD and 115 normal subjects, with 38,400 B-scans and derived total retina and RPE-drusen complex thickness measurements."
tags: ["oct", "research-only", "manual", "segmentation", "classification", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Duke RPE-Drusen Complex OCT Dataset

OCT data from 384 subjects, including 269 with AMD and 115 normal subjects, with 38,400 B-scans and derived total retina and RPE-drusen complex thickness measurements.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `duke_rpedc` |
| **Full name** | Duke RPE-Drusen Complex OCT Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, classification, measurement |
| **Samples** | 384 |
| **Classes** | 2 (normal, amd) |
| **Splits** | all |
| **Size** | 20.0 GB |
| **Source-stated terms** | Research only: research and educational use; commercialization and redistribution prohibited |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> The source describes more than 20 GB of subject data, segmentation boundaries, and thickness maps.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download duke_rpedc --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download duke_rpedc --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('duke_rpedc')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [people.duke.edu/~sf59](https://people.duke.edu/~sf59/RPEDC_Ophth_2013_dataset.htm)

**Source-term evidence:** [people.duke.edu/~sf59](https://people.duke.edu/~sf59/RPEDC_Ophth_2013_dataset.htm)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('duke_rpedc')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{duke_rpedc,
  title  = { Duke RPE-Drusen Complex OCT Dataset },
  note   = { Farsiu S, Chiu SJ, O'Connell RV, et al. Quantitative classification of eyes with and without intermediate age-related macular degeneration using optical coherence tomography. Ophthalmology. 2014;121:162-172. doi:10.1016/j.ophtha.2013.07.013 },
  year   = { 2014 },
  url    = { https://people.duke.edu/~sf59/RPEDC_Ophth_2013_dataset.htm },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Farsiu S, Chiu SJ, O'Connell RV, et al. Quantitative classification of eyes with and without intermediate age-related macular degeneration using optical coherence tomography. Ophthalmology. 2014;121:162-172. doi:10.1016/j.ophtha.2013.07.013
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only: research and educational use; commercialization and redistribution prohibited
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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

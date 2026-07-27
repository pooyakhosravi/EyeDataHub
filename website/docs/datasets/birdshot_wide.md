---
id: birdshot_wide
title: "Birdshot-WIDE Widefield Fundus Dataset"
sidebar_label: birdshot_wide
description: "Longitudinal widefield fundus photographs from birdshot chorioretinitis eyes and age- and sex-matched controls."
tags: ["uwf_fundus", "cc-by", "manual", "classification", "progression_analysis", "quality_assessment"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Birdshot-WIDE Widefield Fundus Dataset

Longitudinal widefield fundus photographs from birdshot chorioretinitis eyes and age- and sex-matched controls.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `birdshot_wide` |
| **Full name** | Birdshot-WIDE Widefield Fundus Dataset |
| **Primary category** | `uwf_fundus` |
| **Contained modalities** | uwf_fundus |
| **Tasks** | classification, progression_analysis, quality_assessment |
| **Samples** | 6,352 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Restricted Zenodo record requiring an access request. The source reports 5,042 images from 742 affected eyes and 1,310 images from 742 matched control eyes; the birdshot cohort has a median 4.31-year follow-up. CC BY 4.0 does not remove the access agreement.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download birdshot_wide --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('birdshot_wide')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5281/zenodo.19474623](https://doi.org/10.5281/zenodo.19474623)

**Source-term evidence:** [https://doi.org/10.5281/zenodo.19474623](https://doi.org/10.5281/zenodo.19474623)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{birdshot_wide,
  title  = { Birdshot-WIDE Widefield Fundus Dataset },
  note   = { Foulonneau T, Memmi C, Monnet D, Brezin AP, Vienne-Jumeau A. A Dataset of Widefield Fundus Images From Patients With Birdshot Chorioretinitis and Matched Control. Scientific Data. 2026. doi:10.1038/s41597-026-07494-8 },
  year   = { 2026 },
  url    = { https://doi.org/10.5281/zenodo.19474623 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Foulonneau T, Memmi C, Monnet D, Brezin AP, Vienne-Jumeau A. A Dataset of Widefield Fundus Images From Patients With Birdshot Chorioretinitis and Matched Control. Scientific Data. 2026. doi:10.1038/s41597-026-07494-8
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

- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 records, `cc-by`)
- [tsukazaki_uwf](./tsukazaki_uwf.md): Tsukazaki Hospital UWF Fundus Dataset (13,047 records, `research-only`)
- [deepdrid](./deepdrid.md): DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset (2,256 records, `cc-by-sa`)
- [uwf_tumor](./uwf_tumor.md): UWF Fundus Intraocular Tumor Dataset (2,031 records, `cc-by`)
- [uwf_dr_peng](./uwf_dr_peng.md): UWF Fundus DR Dataset (Peng et al., 2026) (1,630 records, `cc-by`)
- [uwf_zhejiang](./uwf_zhejiang.md): Open UWF Fundus Dataset with Disease + Quality Labels (700 records, `cc-by`)
- [uwf_dr](./uwf_dr.md): UWF DR Reasoning Dataset (495 records, `research-only`)

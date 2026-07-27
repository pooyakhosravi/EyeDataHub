---
id: dryad_retinal_vein_cannulation
title: "Autonomous Retinal Vein Cannulation Data and Code"
sidebar_label: dryad_retinal_vein_cannulation
description: "Surgical-microscope and intraoperative-OCT data for autonomous robotic retinal-vein cannulation in ex vivo porcine eyes."
tags: ["multimodal", "surgical_video", "oct", "cc0", "dryad", "classification", "navigation", "surgical_workflow"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Autonomous Retinal Vein Cannulation Data and Code

Surgical-microscope and intraoperative-OCT data for autonomous robotic retinal-vein cannulation in ex vivo porcine eyes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_retinal_vein_cannulation` |
| **Full name** | Autonomous Retinal Vein Cannulation Data and Code |
| **Primary category** | `multimodal` |
| **Contained modalities** | surgical_video, oct |
| **Tasks** | classification, navigation, surgical_workflow |
| **Samples** | 26 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 7.511 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Experiments used 20 static and six motion-simulated ex vivo porcine eyes. The large release contains model-training data and code.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_retinal_vein_cannulation --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dryad_retinal_vein_cannulation --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_retinal_vein_cannulation')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.3ffbg79zd](https://doi.org/10.5061/dryad.3ffbg79zd)

**Source-term evidence:** [https://doi.org/10.5061/dryad.3ffbg79zd](https://doi.org/10.5061/dryad.3ffbg79zd)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_retinal_vein_cannulation,
  title  = { Autonomous Retinal Vein Cannulation Data and Code },
  note   = { Zhang P, Gehlbach P, Taylor R, Iordachita I, Kobilarov M. Data and code from: Deep learning-based autonomous retinal vein cannulation in ex vivo porcine eyes. Dryad. 2025. doi:10.5061/dryad.3ffbg79zd },
  year   = { 2025 },
  url    = { https://doi.org/10.5061/dryad.3ffbg79zd },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Zhang P, Gehlbach P, Taylor R, Iordachita I, Kobilarov M. Data and code from: Deep learning-based autonomous retinal vein cannulation in ex vivo porcine eyes. Dryad. 2025. doi:10.5061/dryad.3ffbg79zd
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [dryad_subretinal_robot](./dryad_subretinal_robot.md): Head-Mounted Robot Subretinal Injection Dataset (count not reported records, `cc0`)
- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 records, `cc-by`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (160,185 records, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 records, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)

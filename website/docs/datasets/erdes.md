---
id: erdes
title: "ERDES: Ocular Ultrasound Video Benchmark (Retinal Detachment + Macula)"
sidebar_label: erdes
description: "5,381 B-scan ocular ultrasound video clips with retinal-detachment presence and macula-on/off status labels. Total runtime approximately 5 hours 10 minutes. Only public ocular ultrasound video benchma"
tags: ["multimodal", "ocular_ultrasound", "unknown", "manual", "classification", "resource-role-current-dataset", "dataset-family-erdes"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ERDES: Ocular Ultrasound Video Benchmark (Retinal Detachment + Macula)

5,381 B-scan ocular ultrasound video clips with retinal-detachment presence and macula-on/off status labels. Total runtime approximately 5 hours 10 minutes. Only public ocular ultrasound video benchmark.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `erdes` |
| **Full name** | ERDES: Ocular Ultrasound Video Benchmark (Retinal Detachment + Macula) |
| **First published** | 2025-07-31 |
| **Publication date precision** | day |
| **Publication date evidence** | [github.com/OSUPCVLab](https://github.com/OSUPCVLab/ERDES) |
| **Publication date source field** | Official GitHub README: News |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `erdes` |
| **Contained modalities** | ocular_ultrasound |
| **Tasks** | classification |
| **Primary reported quantity** | 5,381 video clips |
| **Classes** | 3 (no_rd, rd_macula_on, rd_macula_off) |
| **Splits** | train, val, test |
| **Size** | 5.0 GB |
| **Source-stated terms** | Unknown — needs check (open-access project site) |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 5,381 | `video_clips` | Ocular-ultrasound B-scan clips | `associated_publication` | [arxiv.org/abs](https://arxiv.org/abs/2503.04525) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Adds ocular ultrasound video — modality EyeDataHub otherwise lacks. Project page at github/arxiv referenced. Access verified via project site.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download erdes --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download erdes --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('erdes')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [arxiv.org/abs](https://arxiv.org/abs/2503.04525)

**Source-term evidence:** [arxiv.org/abs](https://arxiv.org/abs/2503.04525)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{erdes,
  title  = { ERDES: Ocular Ultrasound Video Benchmark (Retinal Detachment + Macula) },
  note   = { Ozkut Y, Navard P, Adhikari S, et al., 'ERDES: A benchmark video dataset for retinal detachment and macular status classification in ocular ultrasound', arXiv 2503.04525, 2025 },
  year   = { 2025 },
  url    = { https://arxiv.org/abs/2503.04525 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ozkut Y, Navard P, Adhikari S, et al., 'ERDES: A benchmark video dataset for retinal detachment and macular status classification in ocular ultrasound', arXiv 2503.04525, 2025.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown — needs check (open-access project site)
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (600 question answer pairs, `cc-by`)
- [dryad_preeclampsia_ocular_octa](./dryad_preeclampsia_ocular_octa.md): Plane wave ultrasound and OCT angiography of the eye in preeclampsia (Not reported, `cc0`)
- [dryad_rop_plane_wave_doppler](./dryad_rop_plane_wave_doppler.md): ROP Plane-Wave Doppler Dataset (Not reported, `cc0`)
- [mendeley_development_deep_learning_based_system_optic](./mendeley_development_deep_learning_based_system_optic.md): Dataset for - Development of a Deep Learning-based system for Optic Nerve characterization in Transorbital Ultrasound Images on a multicenter dataset (Not reported, `cc-by`)

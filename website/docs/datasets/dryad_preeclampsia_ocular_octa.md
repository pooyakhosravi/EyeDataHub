---
id: dryad_preeclampsia_ocular_octa
title: "Plane wave ultrasound and OCT angiography of the eye in preeclampsia"
sidebar_label: dryad_preeclampsia_ocular_octa
description: "The defined plane-wave ultrasound/OCTA data file and README directly support human ocular vascular measurement."
tags: ["octa", "ocular_ultrasound", "tabular", "cc0", "dryad", "vessel_analysis", "resource-role-current-dataset", "dataset-family-dryad-preeclampsia-ocular-octa"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Plane wave ultrasound and OCT angiography of the eye in preeclampsia

The defined plane-wave ultrasound/OCTA data file and README directly support human ocular vascular measurement.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_preeclampsia_ocular_octa` |
| **Full name** | Plane wave ultrasound and OCT angiography of the eye in preeclampsia |
| **Primary category** | `octa` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_preeclampsia_ocular_octa` |
| **Contained modalities** | octa, ocular_ultrasound, tabular |
| **Tasks** | vessel_analysis |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000308996 GB |
| **Source-stated terms** | https://spdx.org/licenses/CC0-1.0.html |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-08-01) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope: core_add. Named file-level object: PE_ran.sav plus README. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_preeclampsia_ocular_octa --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_preeclampsia_ocular_octa --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_preeclampsia_ocular_octa')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.j0zpc86kg](https://doi.org/10.5061/dryad.j0zpc86kg)

**Source-term evidence:** [https://doi.org/10.5061/dryad.j0zpc86kg](https://doi.org/10.5061/dryad.j0zpc86kg)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_preeclampsia_ocular_octa,
  title  = { Plane wave ultrasound and OCT angiography of the eye in preeclampsia },
  note   = { Plane wave ultrasound and OCT angiography of the eye in preeclampsia. Dryad Dataset. doi:10.5061/dryad.j0zpc86kg },
  url    = { https://doi.org/10.5061/dryad.j0zpc86kg },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Plane wave ultrasound and OCT angiography of the eye in preeclampsia. Dryad Dataset. doi:10.5061/dryad.j0zpc86kg.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** https://spdx.org/licenses/CC0-1.0.html
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 longitudinal samples, `cc-by`)
- [dryad_rop_plane_wave_doppler](./dryad_rop_plane_wave_doppler.md): ROP Plane-Wave Doppler Dataset (Not reported, `cc0`)
- [mendeley_development_deep_learning_based_system_optic](./mendeley_development_deep_learning_based_system_optic.md): Dataset for - Development of a Deep Learning-based system for Optic Nerve characterization in Transorbital Ultrasound Images on a multicenter dataset (Not reported, `cc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [octa_macula_coronal](./octa_macula_coronal.md): OCTA Macula Coronal Views (82,560 images, `cc-by`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)

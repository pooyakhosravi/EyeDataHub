---
id: mendeley_digital_holograms_rbcs_glaucoma_patients_healthy
title: "Digital holograms of RBCs from the glaucoma patients and healthy controls"
sidebar_label: mendeley_digital_holograms_rbcs_glaucoma_patients_healthy
description: "Observation-level human or human-derived measurements/signals. from Red blood cells from glaucoma patients and healthy controls."
tags: ["cell_microscopy", "tabular", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-digital-holograms-rbcs-glaucoma-patients-healthy"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Digital holograms of RBCs from the glaucoma patients and healthy controls

Observation-level human or human-derived measurements/signals. from Red blood cells from glaucoma patients and healthy controls.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_digital_holograms_rbcs_glaucoma_patients_healthy` |
| **Full name** | Digital holograms of RBCs from the glaucoma patients and healthy controls |
| **First published** | 2025-04-08 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/tryd7r3wct/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `cell_microscopy` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_digital_holograms_rbcs_glaucoma_patients_healthy` |
| **Contained modalities** | cell_microscopy, tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Red blood cells from glaucoma patients and healthy controls. Source-review finding: Digital and background holograms recorded with CMOS camera.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_digital_holograms_rbcs_glaucoma_patients_healthy --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_digital_holograms_rbcs_glaucoma_patients_healthy --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_digital_holograms_rbcs_glaucoma_patients_healthy')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/tryd7r3wct/3)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/tryd7r3wct)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_digital_holograms_rbcs_glaucoma_patients_healthy,
  title  = { Digital holograms of RBCs from the glaucoma patients and healthy controls },
  note   = { Digital holograms of RBCs from the glaucoma patients and healthy controls. Mendeley Data, V3. doi:10.17632/tryd7r3wct.3 },
  url    = { https://data.mendeley.com/datasets/tryd7r3wct/3 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Digital holograms of RBCs from the glaucoma patients and healthy controls. Mendeley Data, V3. doi:10.17632/tryd7r3wct.3.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [mendeley_ocular_sebaceous_neoplasms](./mendeley_ocular_sebaceous_neoplasms.md): Ocular sebaceous neoplasms (Not reported, `cc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)

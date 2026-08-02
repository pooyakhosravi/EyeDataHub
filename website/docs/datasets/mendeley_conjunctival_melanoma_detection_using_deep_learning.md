---
id: mendeley_conjunctival_melanoma_detection_using_deep_learning
title: "Conjunctival melanoma detection using deep learning in smartphone images"
sidebar_label: mendeley_conjunctival_melanoma_detection_using_deep_learning
description: "Human/derived image or image-annotation observations. from Human ocular anterior-segment images gathered from public web sources; source-level provenance remains limited."
tags: ["tabular", "cc-by-nc", "mendeley", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Conjunctival melanoma detection using deep learning in smartphone images

Human/derived image or image-annotation observations. from Human ocular anterior-segment images gathered from public web sources; source-level provenance remains limited.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_conjunctival_melanoma_detection_using_deep_learning` |
| **Full name** | Conjunctival melanoma detection using deep learning in smartphone images |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | segmentation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY-NC 3.0 |
| **Normalized terms** | `cc-by-nc` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
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

> Human provenance: Human ocular anterior-segment images gathered from public web sources; source-level provenance remains limited. Source-review finding: Indexed record describes manually clinician-classified smartphone ocular images.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_conjunctival_melanoma_detection_using_deep_learning --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_conjunctival_melanoma_detection_using_deep_learning --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_conjunctival_melanoma_detection_using_deep_learning')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/t75wjsw6bw/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/t75wjsw6bw)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_conjunctival_melanoma_detection_using_deep_learning,
  title  = { Conjunctival melanoma detection using deep learning in smartphone images },
  note   = { Conjunctival melanoma detection using deep learning in smartphone images. Mendeley Data, V2. doi:10.17632/t75wjsw6bw.2 },
  url    = { https://data.mendeley.com/datasets/t75wjsw6bw/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Conjunctival melanoma detection using deep learning in smartphone images. Mendeley Data, V2. doi:10.17632/t75wjsw6bw.2.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC 3.0
- **Normalized category:** `cc-by-nc`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)

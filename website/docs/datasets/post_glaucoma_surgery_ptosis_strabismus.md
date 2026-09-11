---
id: post_glaucoma_surgery_ptosis_strabismus
title: "Post-Glaucoma-Surgery Ptosis and Strabismus Dataset"
sidebar_label: post_glaucoma_surgery_ptosis_strabismus
description: "De-identified human glaucoma-surgery clinical records with postoperative ptosis and strabismus outcomes."
tags: ["tabular", "cc-by", "figshare", "classification", "measurement", "resource-role-current-dataset", "dataset-family-post-glaucoma-surgery-ptosis-strabismus"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Post-Glaucoma-Surgery Ptosis and Strabismus Dataset

De-identified human glaucoma-surgery clinical records with postoperative ptosis and strabismus outcomes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `post_glaucoma_surgery_ptosis_strabismus` |
| **Full name** | Post-Glaucoma-Surgery Ptosis and Strabismus Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `post_glaucoma_surgery_ptosis_strabismus` |
| **Contained modalities** | tabular |
| **Tasks** | classification, measurement |
| **Primary reported quantity** | 705 records |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 705 | `records` | Source reports 705 glaucoma-surgery clinical records. Source-stated quantity; repository file count is separate. | `official_source_description` | [https://doi.org/10.1371/journal.pone.0335074.s001](https://doi.org/10.1371/journal.pone.0335074.s001) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download post_glaucoma_surgery_ptosis_strabismus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download post_glaucoma_surgery_ptosis_strabismus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('post_glaucoma_surgery_ptosis_strabismus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.1371/journal.pone.0335074.s001](https://doi.org/10.1371/journal.pone.0335074.s001)

**Source-term evidence:** [https://doi.org/10.1371/journal.pone.0335074.s001](https://doi.org/10.1371/journal.pone.0335074.s001)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{post_glaucoma_surgery_ptosis_strabismus,
  title  = { Post-Glaucoma-Surgery Ptosis and Strabismus Dataset },
  note   = { Repository dataset record. 10.1371/journal.pone.0335074.s001 },
  url    = { https://doi.org/10.1371/journal.pone.0335074.s001 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.1371/journal.pone.0335074.s001.
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

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)

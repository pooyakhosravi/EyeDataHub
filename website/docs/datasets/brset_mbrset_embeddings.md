---
id: brset_mbrset_embeddings
title: "Embedding-Based Representations for BRSET and mBRSET"
sidebar_label: brset_mbrset_embeddings
description: "Precomputed image embeddings for BRSET and mBRSET to support efficient ophthalmic AI research without raw-image redistribution."
tags: ["tabular", "unknown", "physionet", "classification", "retrieval", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Embedding-Based Representations for BRSET and mBRSET

Precomputed image embeddings for BRSET and mBRSET to support efficient ophthalmic AI research without raw-image redistribution.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `brset_mbrset_embeddings` |
| **Full name** | Embedding-Based Representations for BRSET and mBRSET |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | classification, retrieval |
| **Primary reported quantity** | 53,188 embedding vectors |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | PhysioNet credentialed access terms |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 53,188 | `embedding_vectors` | Rows across six model-specific CSV files Two BRSET files contain 16,266 rows each and four mBRSET files contain 5,164 rows each. | `derived_from_reported_components` | [physionet.org/content](https://physionet.org/content/embedding-brset-mbrset/1.0.0/) |
| Additional | 21,430 | `images` | Distinct parent images represented by at least one embedding This is 16,266 BRSET plus 5,164 mBRSET images; it is not a new image cohort. | `derived_from_reported_components` | [physionet.org/content](https://physionet.org/content/embedding-brset-mbrset/1.0.0/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative representation layer for existing BRSET/mBRSET cohorts.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [brset](./brset.md): The PhysioNet record supplies precomputed representations for BRSET images. ([evidence](https://physionet.org/content/embedding-brset-mbrset/1.0.0/))
- This record is `derived from` [mbrset](./mbrset.md): The PhysioNet record supplies precomputed representations for mBRSET images. ([evidence](https://physionet.org/content/embedding-brset-mbrset/1.0.0/))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download brset_mbrset_embeddings --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('brset_mbrset_embeddings')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [physionet.org/content](https://physionet.org/content/embedding-brset-mbrset/1.0.0/)

**Source-term evidence:** [physionet.org/content](https://physionet.org/content/embedding-brset-mbrset/1.0.0/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{brset_mbrset_embeddings,
  title  = { Embedding-Based Representations for BRSET and mBRSET },
  note   = { Embedding-Based Representations for BRSET and mBRSET. PhysioNet, 2026 },
  year   = { 2026 },
  url    = { https://physionet.org/content/embedding-brset-mbrset/1.0.0/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Embedding-Based Representations for BRSET and mBRSET. PhysioNet, 2026.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** PhysioNet credentialed access terms
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [dryad_canine_pra_cea_genotypes](./dryad_canine_pra_cea_genotypes.md): Canine PRA and CEA Genotype Dataset (86,667 records, `cc0`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)

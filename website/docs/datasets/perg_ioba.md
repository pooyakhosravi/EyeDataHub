---
id: perg_ioba
title: "PERG-IOBA Ocular Electrophysiology Dataset"
sidebar_label: perg_ioba
description: "Transient pattern electroretinogram responses from 304 subjects in 336 records with clinical metadata."
tags: ["electrophysiology", "tabular", "odc-by", "physionet", "classification", "regression", "resource-role-current-dataset", "dataset-family-perg-ioba"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# PERG-IOBA Ocular Electrophysiology Dataset

Transient pattern electroretinogram responses from 304 subjects in 336 records with clinical metadata.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `perg_ioba` |
| **Full name** | PERG-IOBA Ocular Electrophysiology Dataset |
| **Primary category** | `electrophysiology` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `perg_ioba` |
| **Contained modalities** | electrophysiology, tabular |
| **Tasks** | classification, regression |
| **Primary reported quantity** | 1,354 signals |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | ODC-BY 1.0 (Open Data Commons Attribution) |
| **Normalized terms** | `odc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `transfer_tested_partial` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,354 | `signals` | Transient pattern electroretinogram responses | `official_source_description` | [physionet.org/content](https://physionet.org/content/perg-ioba-dataset/1.0.0/) |
| Additional | 304 | `participants` | Participants represented in 336 records | `official_source_description` | [physionet.org/content](https://physionet.org/content/perg-ioba-dataset/1.0.0/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download perg_ioba --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download perg_ioba --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('perg_ioba')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [physionet.org/content](https://physionet.org/content/perg-ioba-dataset/1.0.0/)

**Source-term evidence:** [physionet.org/content](https://physionet.org/content/perg-ioba-dataset/1.0.0/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{perg_ioba,
  title  = { PERG-IOBA Ocular Electrophysiology Dataset },
  note   = { The PERG-IOBA Dataset. PhysioNet, 2024. doi:10.13026/d24m-w054 },
  year   = { 2024 },
  url    = { https://physionet.org/content/perg-ioba-dataset/1.0.0/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
The PERG-IOBA Dataset. PhysioNet, 2024. doi:10.13026/d24m-w054
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** ODC-BY 1.0 (Open Data Commons Attribution)
- **Normalized category:** `odc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)

---
id: oculoscope
title: "OculoScope: Fairer AI in Ophthalmology Dataset"
sidebar_label: oculoscope
description: "16,530 ultra-widefield fundus images from 8,405+ patients (age 0–90) annotated for 38 ophthalmic diseases and 67 fundus features. Released alongside the FairerOPTH study on sexism and ageism in ophtha"
tags: ["uwf_fundus", "tabular", "cc-by", "figshare", "classification", "multilabel", "resource-role-current-dataset", "dataset-family-oculoscope"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OculoScope: Fairer AI in Ophthalmology Dataset

16,530 ultra-widefield fundus images from 8,405+ patients (age 0–90) annotated for 38 ophthalmic diseases and 67 fundus features. Released alongside the FairerOPTH study on sexism and ageism in ophthalmic AI (Nature Communications 2024).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `oculoscope` |
| **Full name** | OculoScope: Fairer AI in Ophthalmology Dataset |
| **First published** | 2023-12-03 |
| **Publication date precision** | day |
| **Publication date evidence** | [zenodo.org/api](https://zenodo.org/api/records/10403889) |
| **Publication date source field** | metadata.publication_date (author Zenodo dataset record) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `uwf_fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `oculoscope` |
| **Contained modalities** | uwf_fundus, tabular |
| **Tasks** | classification, multilabel |
| **Primary reported quantity** | 16,530 images |
| **Classes** | 38 (Not reported) |
| **Splits** | train, test |
| **Size** | 20.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 16,530 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [Figshare private-share page](https://figshare.com/s/926c2c2ef9e77ab5eb9d) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Also annotates 67 fine-grained fundus features in addition to 38 disease-level labels. Full class list in dataset CSV.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oculoscope --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download oculoscope --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oculoscope')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [Figshare private-share page](https://figshare.com/s/926c2c2ef9e77ab5eb9d)

**Source-term evidence:** [Figshare private-share page](https://figshare.com/s/926c2c2ef9e77ab5eb9d)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('oculoscope')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{oculoscope,
  title  = { OculoScope: Fairer AI in Ophthalmology Dataset },
  note   = { FairerOPTH Study — OculoScope Dataset. Nature Communications 2024. https://www.nature.com/articles/s41467-024-48972-0 — Data: https://figshare.com/s/926c2c2ef9e77ab5eb9d },
  year   = { 2024 },
  url    = { https://figshare.com/s/926c2c2ef9e77ab5eb9d },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
FairerOPTH Study — OculoScope Dataset. Nature Communications 2024. https://www.nature.com/articles/s41467-024-48972-0 — Data: https://figshare.com/s/926c2c2ef9e77ab5eb9d
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
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [tsukazaki_uwf](./tsukazaki_uwf.md): Tsukazaki Hospital UWF Fundus Dataset (13,047 images, `research-only`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)

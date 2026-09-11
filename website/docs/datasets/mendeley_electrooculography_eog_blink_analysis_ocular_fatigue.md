---
id: mendeley_electrooculography_eog_blink_analysis_ocular_fatigue
title: "Electrooculography (EOG) Dataset for Blink Analysis and Ocular Fatigue Detection"
sidebar_label: mendeley_electrooculography_eog_blink_analysis_ocular_fatigue
description: "Observation-level human or human-derived measurements/signals. from Four human participants."
tags: ["electrophysiology", "tabular", "cc-by", "mendeley", "classification", "resource-role-current-dataset", "dataset-family-mendeley-electrooculography-eog-blink-analysis-ocular-fatigue"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Electrooculography (EOG) Dataset for Blink Analysis and Ocular Fatigue Detection

Observation-level human or human-derived measurements/signals. from Four human participants.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_electrooculography_eog_blink_analysis_ocular_fatigue` |
| **Full name** | Electrooculography (EOG) Dataset for Blink Analysis and Ocular Fatigue Detection |
| **Publication date** | 2026-06-13 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w7hm97cts5/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `electrophysiology` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_electrooculography_eog_blink_analysis_ocular_fatigue` |
| **Contained modalities** | electrophysiology, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | 4 participants |
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

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 4 | `participants` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w7hm97cts5) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Four human participants. Source-review finding: Vertical BIOPAC EOG recordings at 1000 Hz during baseline/fixation tasks.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_electrooculography_eog_blink_analysis_ocular_fatigue --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_electrooculography_eog_blink_analysis_ocular_fatigue --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_electrooculography_eog_blink_analysis_ocular_fatigue')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w7hm97cts5/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w7hm97cts5)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_electrooculography_eog_blink_analysis_ocular_fatigue,
  title  = { Electrooculography (EOG) Dataset for Blink Analysis and Ocular Fatigue Detection },
  note   = { Electrooculography (EOG) Dataset for Blink Analysis and Ocular Fatigue Detection. Mendeley Data, V2. doi:10.17632/w7hm97cts5.2 },
  url    = { https://data.mendeley.com/datasets/w7hm97cts5/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Electrooculography (EOG) Dataset for Blink Analysis and Ocular Fatigue Detection. Mendeley Data, V2. doi:10.17632/w7hm97cts5.2.
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

- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [perg_ioba](./perg_ioba.md): PERG-IOBA Ocular Electrophysiology Dataset (1,354 signals, `odc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)

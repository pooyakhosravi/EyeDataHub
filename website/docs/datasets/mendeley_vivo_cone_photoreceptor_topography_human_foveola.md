---
id: mendeley_vivo_cone_photoreceptor_topography_human_foveola
title: "In-vivo cone photoreceptor topography of the human foveola"
sidebar_label: mendeley_vivo_cone_photoreceptor_topography_human_foveola
description: "Retinal-image montages, cone annotation maps, and participant-level supporting measurements from In-vivo human foveolar imaging; individual-participant MATLAB files are stated."
tags: ["adaptive_optics", "tabular", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-vivo-cone-photoreceptor-topography-human-foveola"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# In-vivo cone photoreceptor topography of the human foveola

Retinal-image montages, cone annotation maps, and participant-level supporting measurements from In-vivo human foveolar imaging; individual-participant MATLAB files are stated.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_vivo_cone_photoreceptor_topography_human_foveola` |
| **Full name** | In-vivo cone photoreceptor topography of the human foveola |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `adaptive_optics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_vivo_cone_photoreceptor_topography_human_foveola` |
| **Contained modalities** | adaptive_optics, tabular |
| **Tasks** | segmentation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `mixed_components` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: In-vivo human foveolar imaging; individual-participant MATLAB files are stated. Source-review finding: Source description lists retinal image montages, cone annotation maps, supporting data, and individual-participant MATLAB files readable by ConeMapper. Potential overlap with related foveola studies was not resolved; no record-to-record edge is encoded.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_vivo_cone_photoreceptor_topography_human_foveola --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_vivo_cone_photoreceptor_topography_human_foveola --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_vivo_cone_photoreceptor_topography_human_foveola')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/m5nkpb8phv/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/m5nkpb8phv)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_vivo_cone_photoreceptor_topography_human_foveola,
  title  = { In-vivo cone photoreceptor topography of the human foveola },
  note   = { In-vivo cone photoreceptor topography of the human foveola. Mendeley Data, V1. doi:10.17632/m5nkpb8phv.1 },
  url    = { https://data.mendeley.com/datasets/m5nkpb8phv/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
In-vivo cone photoreceptor topography of the human foveola. Mendeley Data, V1. doi:10.17632/m5nkpb8phv.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `mixed_components`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [dryad_human_foveal_cones](./dryad_human_foveal_cones.md): Human foveal cone photoreceptor topography and its dependence on eye length (28 eyes, `cc0`)
- [mendeley_sub_cone_visual_resolution_by_active](./mendeley_sub_cone_visual_resolution_by_active.md): Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola (16 participants, `cc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)

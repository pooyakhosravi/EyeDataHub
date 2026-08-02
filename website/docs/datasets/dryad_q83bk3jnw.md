---
id: dryad_q83bk3jnw
title: "Disease parameters following ocular herpes simplex virus type 1 infection are similar in male and female BALB/C mice"
sidebar_label: dryad_q83bk3jnw
description: "Official Dryad deposit of source-described tabular ophthalmic data for the associated study."
tags: ["tabular", "cc0", "dryad", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Disease parameters following ocular herpes simplex virus type 1 infection are similar in male and female BALB/C mice

Official Dryad deposit of source-described tabular ophthalmic data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_q83bk3jnw` |
| **Full name** | Disease parameters following ocular herpes simplex virus type 1 infection are similar in male and female BALB/C mice |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.004541161 GB |
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

> Scope screen: adjacent_add. Current Dryad v4 file listing: 7 files, 4541161 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_q83bk3jnw --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_q83bk3jnw --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_q83bk3jnw')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.q83bk3jnw](https://doi.org/10.5061/dryad.q83bk3jnw)

**Source-term evidence:** [https://doi.org/10.5061/dryad.q83bk3jnw](https://doi.org/10.5061/dryad.q83bk3jnw)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_q83bk3jnw,
  title  = { Disease parameters following ocular herpes simplex virus type 1 infection are similar in male and female BALB/C mice },
  note   = { Brandt Curtis, Kolb Aaron, Ferguson Sarah, Larsen Inna. Disease parameters following ocular herpes simplex virus type 1 infection are similar in male and female BALB/C mice. Dryad. 2023. doi:10.5061/dryad.q83bk3jnw },
  year   = { 2023 },
  url    = { https://doi.org/10.5061/dryad.q83bk3jnw },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Brandt Curtis, Kolb Aaron, Ferguson Sarah, Larsen Inna. Disease parameters following ocular herpes simplex virus type 1 infection are similar in male and female BALB/C mice. Dryad. 2023. doi:10.5061/dryad.q83bk3jnw
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

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [dryad_canine_pra_cea_genotypes](./dryad_canine_pra_cea_genotypes.md): Canine PRA and CEA Genotype Dataset (86,667 records, `cc0`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)

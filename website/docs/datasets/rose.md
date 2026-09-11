---
id: rose
title: "ROSE: Retinal OCT-Angiography Vessel Segmentation"
sidebar_label: rose
description: "229 OCTA images (ROSE-1 + ROSE-2) with pixel-level retinal vessel segmentation ground truth."
tags: ["octa", "cc-by", "zenodo", "segmentation", "resource-role-current-dataset", "dataset-family-rose"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ROSE: Retinal OCT-Angiography Vessel Segmentation

229 OCTA images (ROSE-1 + ROSE-2) with pixel-level retinal vessel segmentation ground truth.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rose` |
| **Full name** | ROSE: Retinal OCT-Angiography Vessel Segmentation |
| **Publication date** | 2021-03-02 |
| **Date basis** | Associated publication |
| **Publication date precision** | day |
| **Publication date evidence** | [pubmed.ncbi.nlm.nih.gov/33284751](https://pubmed.ncbi.nlm.nih.gov/33284751/) |
| **Publication date source field** | epubdate (PubMed-indexed publisher e-publication date) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | PubMed reports electronic publication on 2 March 2021. Crossref records DOI registration on 7 December 2020. |
| **Primary category** | `octa` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `rose` |
| **Contained modalities** | octa |
| **Tasks** | segmentation |
| **Primary reported quantity** | 229 images |
| **Classes** | 2 (background, vessel) |
| **Splits** | train, test |
| **Size** | 0.8 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 229 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/doi](https://zenodo.org/doi/10.5281/zenodo.12775880) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Zenodo mirror (2024) publishes ROSE-1 + ROSE-2 under CC BY 4.0 — upgraded from the previous form-gated academic-only distribution on imed.nimte.ac.cn. EyeDataHub auto-downloads from Zenodo record 12775880.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download rose --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rose')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/doi](https://zenodo.org/doi/10.5281/zenodo.12775880)

**Source-term evidence:** [zenodo.org/doi](https://zenodo.org/doi/10.5281/zenodo.12775880)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rose,
  title  = { ROSE: Retinal OCT-Angiography Vessel Segmentation },
  note   = { Ma et al., 'ROSE: A Retinal OCT-Angiography Vessel Segmentation Dataset and New Model', IEEE TMI 2021. Zenodo mirror: doi:10.5281/zenodo.12775880 (CC BY 4.0) },
  year   = { 2021 },
  url    = { https://zenodo.org/doi/10.5281/zenodo.12775880 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ma et al., 'ROSE: A Retinal OCT-Angiography Vessel Segmentation Dataset and New Model', IEEE TMI 2021. Zenodo mirror: doi:10.5281/zenodo.12775880 (CC BY 4.0).
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

- [octa_macula_coronal](./octa_macula_coronal.md): OCTA Macula Coronal Views (82,560 images, `cc-by`)
- [octa_500](./octa_500.md): OCTA-500: Large-scale OCTA Multi-task Benchmark (500 participants, `research-only`)
- [aroma_octa](./aroma_octa.md): AROMA Retinal OCTA Artifact Dataset (281 images, `cc-by`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 longitudinal samples, `cc-by`)
- [drac22](./drac22.md): DRAC 2022: Diabetic Retinopathy Analysis Challenge (174 images, `cc-by`)
- [ut_fsocta](./ut_fsocta.md): UTHealth Fundus and Synthetic OCTA Dataset (112 participants, `unknown`)
- [dryad_preeclampsia_ocular_octa](./dryad_preeclampsia_ocular_octa.md): Plane wave ultrasound and OCT angiography of the eye in preeclampsia (Not reported, `cc0`)
- [retinal_oct_octa_two_subjects_processed](./retinal_oct_octa_two_subjects_processed.md): Processed Retinal OCT and OCTA Two-Subject Dataset (Not reported, `cc-by`)

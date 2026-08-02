---
id: soul_octa
title: "SOUL: OCTA Human-Machine Collaborative Annotation Dataset"
sidebar_label: soul_octa
description: "Longitudinal OCT angiography projection maps with vessel labels, clinical text, and treatment/follow-up groupings."
tags: ["octa", "text", "tabular", "cc-by", "figshare", "segmentation", "classification", "progression_analysis"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SOUL: OCTA Human-Machine Collaborative Annotation Dataset

Longitudinal OCT angiography projection maps with vessel labels, clinical text, and treatment/follow-up groupings.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `soul_octa` |
| **Full name** | SOUL: OCTA Human-Machine Collaborative Annotation Dataset |
| **Primary category** | `octa` |
| **Contained modalities** | octa, text, tabular |
| **Tasks** | segmentation, classification, progression_analysis |
| **Primary reported quantity** | 178 longitudinal samples |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.113 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 178 | `longitudinal_samples` | Six source-reported longitudinal subsets The current archive contains 2,046 JPG assets including raw images and corresponding labels; these are not 2,046 independent samples. | `official_source_description` | [https://doi.org/10.6084/m9.figshare.24893358.v3](https://doi.org/10.6084/m9.figshare.24893358.v3) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The six source-reported longitudinal subsets total 178 samples. The release includes raw images, vessel annotations, and clinical text.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download soul_octa --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download soul_octa --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('soul_octa')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.24893358.v3](https://doi.org/10.6084/m9.figshare.24893358.v3)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.24893358.v3](https://doi.org/10.6084/m9.figshare.24893358.v3)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{soul_octa,
  title  = { SOUL: OCTA Human-Machine Collaborative Annotation Dataset },
  note   = { Xue J, Feng Z, Zeng L, et al. Soul: An OCTA dataset based on Human Machine Collaborative Annotation Framework. Scientific Data. 2024;11. doi:10.1038/s41597-024-03665-7 },
  year   = { 2024 },
  url    = { https://doi.org/10.6084/m9.figshare.24893358.v3 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Xue J, Feng Z, Zeng L, et al. Soul: An OCTA dataset based on Human Machine Collaborative Annotation Framework. Scientific Data. 2024;11. doi:10.1038/s41597-024-03665-7
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
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [ophtho_readability](./ophtho_readability.md): Language and Readability Barriers in Ophthalmology Dataset (139 documents, `cc-by`)
- [dryad_preeclampsia_ocular_octa](./dryad_preeclampsia_ocular_octa.md): Plane wave ultrasound and OCT angiography of the eye in preeclampsia (Not reported, `cc0`)
- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 text items, `unknown`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [fundus_105k](./fundus_105k.md): Fundus-105K Text Dataset (105,000 text items, `unknown`)

---
id: fundus_report_dataset
title: "Fundus Report Dataset"
sidebar_label: fundus_report_dataset
description: "Fundus/UWF image-report dataset derived from DeepDRiD and OUWFD-style resources for report-generation research."
tags: ["multimodal", "fundus", "uwf_fundus", "text", "cc-by", "huggingface", "report_generation", "text_generation", "resource-role-annotation-layer", "dataset-family-fundus-report-dataset", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fundus Report Dataset

Fundus/UWF image-report dataset derived from DeepDRiD and OUWFD-style resources for report-generation research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fundus_report_dataset` |
| **Full name** | Fundus Report Dataset |
| **First published** | 2026 |
| **Publication date precision** | year |
| **Publication date evidence** | [api.datacite.org/dois](https://api.datacite.org/dois/10.57967/hf/9303) |
| **Publication date source field** | data.attributes.publicationYear |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `multimodal` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `fundus_report_dataset` |
| **Contained modalities** | fundus, uwf_fundus, text |
| **Tasks** | report_generation, text_generation |
| **Primary reported quantity** | 422 image report pairs |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 422 | `image_report_pairs` | Fundus or UWF image-report rows | `official_source_description` | [huggingface.co/datasets](https://huggingface.co/datasets/zzzzineun/fundus-report-dataset) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative report-generation view; verify source image terms row by row.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [deepdrid](./deepdrid.md): The dataset card reports 203 source images from DeepDRiD and 219 from OUWFD. ([evidence](https://huggingface.co/datasets/zzzzineun/fundus-report-dataset))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fundus_report_dataset --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fundus_report_dataset --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fundus_report_dataset')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/zzzzineun/fundus-report-dataset)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/zzzzineun/fundus-report-dataset)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fundus_report_dataset,
  title  = { Fundus Report Dataset },
  note   = { zzzzineun/fundus-report-dataset. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/zzzzineun/fundus-report-dataset },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
zzzzineun/fundus-report-dataset. Hugging Face dataset, accessed 2026-07.
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

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 images, `research-only`)
- [dme_vqa](./dme_vqa.md): Diabetic Macular Edema Visual Question Answering Dataset (13,470 question answer pairs, `cc-by`)

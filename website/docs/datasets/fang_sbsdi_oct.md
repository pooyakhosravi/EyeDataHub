---
id: fang_sbsdi_oct
title: "Duke Fang SBSDI Retinal OCT Dataset"
sidebar_label: fang_sbsdi_oct
description: "Paired low signal and high signal retinal OCT data used to study sparse acquisition, denoising, interpolation, and reconstruction in normal and non-neovascular AMD eyes."
tags: ["oct", "research-only", "manual", "reconstruction", "denoising"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Duke Fang SBSDI Retinal OCT Dataset

Paired low signal and high signal retinal OCT data used to study sparse acquisition, denoising, interpolation, and reconstruction in normal and non-neovascular AMD eyes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fang_sbsdi_oct` |
| **Full name** | Duke Fang SBSDI Retinal OCT Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | reconstruction, denoising |
| **Primary reported quantity** | 41 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.45 GB |
| **Source-stated terms** | Research only: academic research use |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 41 | `participants` | Human participants described by the associated paper The archive also contains software and mouse imaging data; a file-level image count is not asserted. | `associated_publication` | [https://doi.org/10.1109/TMI.2013.2271904](https://doi.org/10.1109/TMI.2013.2271904) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The count records the 41 human participants described in the paper, not the number of files. The archive is organized by experiment rather than an official train and test split and also includes software and mouse imaging data.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fang_sbsdi_oct --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fang_sbsdi_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fang_sbsdi_oct')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Fang_TMI_2013.htm)

**Source-term evidence:** [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Fang_TMI_2013.htm)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fang_sbsdi_oct,
  title  = { Duke Fang SBSDI Retinal OCT Dataset },
  note   = { Fang L, Li S, McNabb RP, et al. Fast acquisition and reconstruction of optical coherence tomography images via sparse representation. IEEE Trans Med Imaging. 2013;32:2034-2049. doi:10.1109/TMI.2013.2271904 },
  year   = { 2013 },
  url    = { https://people.duke.edu/~sf59/Fang_TMI_2013.htm },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fang L, Li S, McNabb RP, et al. Fast acquisition and reconstruction of optical coherence tomography images via sparse representation. IEEE Trans Med Imaging. 2013;32:2034-2049. doi:10.1109/TMI.2013.2271904
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only: academic research use
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)

---
id: dataset-exploration
title: "Dataset Exploration Guide"
sidebar_label: Dataset Exploration
description: "Practical search and qualification guidance for ophthalmology datasets."
---

# Dataset Exploration Guide

This guide is for humans and software clients looking for ophthalmology datasets to add
to EyeDataHub. It is organized as a practical search map rather than a catalog
snapshot. Use it to broaden candidate discovery, structure notes, and decide
whether a resource is distinct and sufficiently evidenced for catalog review.

Before adding metadata, check the current catalog:

```bash
eyehub search --json
eyehub show <name> --json
```

Do not infer missing licenses, sample counts, demographics, or access terms.
When source material is ambiguous, preserve the ambiguity in notes and mark the
license family as `unknown` until verified.

## Exploration Workflow

1. Define the anatomical scope, modality, and task.
2. Search with several synonym groups, including disease names, device names,
   annotation types, and repository platforms.
3. Record the primary source URL, data paper, challenge page, access platform,
   license text, and citation before interpreting the dataset.
4. Compare candidate names, sources, publications, sample counts, and images
   against the existing catalog.
5. Decide whether the candidate is a new dataset, a subset, a mirror, a
   benchmark split, a derived annotation set, or a duplicate.
6. Add only source-supported metadata.

## Anatomical Search Map

Use anatomical terms to avoid overfitting searches to a single disease or
modality.

| Anatomical focus | Common data targets | Useful search terms |
|---|---|---|
| Retina, posterior pole | Color fundus images, ultra-widefield images, OCT, OCTA, vessel masks, lesion labels | retina dataset, retinal image dataset, fundus dataset, posterior pole, diabetic retinopathy images, retinal vessel segmentation |
| Macula | OCT B-scans, OCT volumes, fundus photographs, OCTA maps, edema labels, AMD grades | macular OCT dataset, age-related macular degeneration dataset, diabetic macular edema, macula segmentation, retinal fluid segmentation |
| Optic disc and nerve fiber layer | Fundus optic disc crops, cup-disc masks, OCT RNFL scans, visual fields | glaucoma dataset, optic disc segmentation, optic cup segmentation, RNFL OCT dataset, visual field dataset |
| Choroid | Enhanced-depth OCT, OCTA, ICGA, choroidal thickness maps | choroid OCT dataset, choroidal segmentation, pachychoroid dataset, indocyanine green angiography dataset |
| Retinal vasculature | Fundus vessel masks, fluorescein angiography, OCTA capillary plexus maps | retinal vessel dataset, vessel segmentation, artery vein classification, OCTA dataset, fluorescein angiography dataset |
| Anterior chamber and angle | AS-OCT, UBM, slit-lamp gonioscopy, angle closure labels | anterior segment OCT dataset, anterior chamber angle dataset, gonioscopy dataset, ultrasound biomicroscopy eye dataset |
| Cornea | Slit-lamp images, specular microscopy, confocal microscopy, topography, tomography | corneal dataset, keratoconus dataset, specular microscopy dataset, corneal endothelium dataset, corneal topography dataset |
| Lens and cataract | Slit-lamp images, retroillumination, fundus quality labels, cataract grades | cataract dataset, lens opacity dataset, slit lamp cataract images, cataract grading dataset |
| Conjunctiva and sclera | External eye photographs, slit-lamp images, redness and lesion labels | conjunctiva dataset, ocular surface dataset, sclera segmentation, eye redness dataset, pterygium dataset |
| Eyelid, periocular, orbit | External photographs, periocular biometrics, ptosis labels, thyroid eye disease images | eyelid dataset, periocular dataset, ptosis dataset, orbital disease dataset, thyroid eye disease image dataset |
| Eye movements and gaze | Eye tracking streams, video, fixation and saccade labels, gaze estimation | eye tracking dataset, gaze estimation dataset, fixation dataset, saccade dataset, ocular motility dataset |
| Functional vision | Visual fields, electrophysiology, acuity, contrast sensitivity, clinical tabular data | visual field dataset, perimetry dataset, ERG dataset, visual acuity dataset, ophthalmology tabular dataset |

## Modality And Device Search Map

Search by both modality and device because many dataset pages use vendor or
instrument language rather than clinical anatomy.

| Modality or device class | Common fields to verify | Useful search terms |
|---|---|---|
| Color fundus photography | Field of view, mydriatic status, camera model, laterality, grading scale | color fundus dataset, retinal fundus images, CFP dataset, mydriatic fundus, nonmydriatic fundus |
| Ultra-widefield fundus imaging | Device, field of view, peripheral lesion labels, montage or raw image status | ultra-widefield retinal dataset, UWF fundus dataset, Optos dataset, peripheral retina dataset |
| OCT B-scan and volume | Vendor, scan protocol, voxel spacing if available, disease labels, layer or fluid masks | OCT dataset, spectral domain OCT, swept source OCT, retinal OCT volume, OCT segmentation dataset |
| OCT angiography | Plexus segmentation, scan size, projection artifact handling, flow metrics | OCTA dataset, optical coherence tomography angiography, capillary plexus dataset, FAZ segmentation |
| Fundus fluorescein angiography | Phase timing, leakage labels, vessel or lesion annotations, video vs still frames | fluorescein angiography dataset, FFA dataset, retinal angiography images, leakage segmentation |
| Indocyanine green angiography | Phase timing, choroidal disease labels, still frames vs sequence | ICGA dataset, indocyanine green angiography dataset, choroidal angiography |
| Slit-lamp photography | Illumination type, magnification, eye region, diagnosis labels | slit lamp image dataset, anterior segment image dataset, ocular surface image dataset |
| Anterior segment OCT | Angle metrics, corneal scans, lens or iris visibility, acquisition protocol | AS-OCT dataset, anterior segment OCT images, angle closure OCT dataset |
| Specular or confocal microscopy | Cell density labels, endothelial masks, magnification, device model | specular microscopy dataset, corneal endothelial cell dataset, confocal microscopy cornea dataset |
| Topography and tomography | Map type, raw measurements vs rendered maps, keratoconus labels, device model | corneal topography dataset, Pentacam dataset, Scheimpflug dataset, keratoconus tomography |
| Ultrasound and UBM | Probe type, B-scan vs UBM, lesion labels, measurement annotations | ocular ultrasound dataset, eye B-scan ultrasound dataset, UBM dataset |
| Visual fields and perimetry | Program type, reliability indices, pointwise thresholds, glaucoma labels | Humphrey visual field dataset, perimetry dataset, visual field progression dataset |
| External eye photography and video | Capture device, pose, illumination, laterality, privacy handling | external eye image dataset, eye photo dataset, periocular image dataset, mobile eye dataset |
| Eye tracking and gaze sensors | Sampling rate, calibration method, screen task, event labels | eye tracking dataset, gaze dataset, fixation saccade dataset, pupillometry dataset |
| Clinical tabular, EHR, and multimodal cohorts | Linked imaging, visit structure, de-identification, variable dictionary | ophthalmology EHR dataset, multimodal ophthalmology dataset, retinal imaging clinical dataset |

## Task Search Map

Task terms are often the fastest way to find annotated datasets. Combine them
with anatomical and modality terms.

| Task family | Typical annotations | Search terms |
|---|---|---|
| Disease classification | Image-level diagnosis, referable disease labels, severity grades | classification, diagnosis, screening, grading, referable, disease detection |
| Lesion detection | Bounding boxes, points, pixel masks, image-level lesion presence | lesion detection, microaneurysm detection, exudate detection, hemorrhage detection |
| Segmentation | Pixel masks, layer boundaries, cup-disc masks, vessel maps, fluid masks | segmentation, semantic segmentation, instance segmentation, boundary annotation |
| Grading and staging | Ordinal disease severity, clinical scales, consensus grades | severity grading, staging, diabetic retinopathy grade, cataract grade, glaucoma grade |
| Measurement and biomarker extraction | Thickness, cup-to-disc ratio, FAZ area, vessel caliber, cell density | biomarker dataset, thickness measurement, cup disc ratio, FAZ area, endothelial cell density |
| Registration and longitudinal analysis | Paired visits, image pairs, aligned modalities, progression labels | longitudinal, progression, registration, follow-up, time series |
| Image quality and artifact detection | Quality scores, gradability labels, artifact categories | image quality dataset, gradability, artifact detection, ungradable fundus |
| Domain adaptation and generalization | Multi-center, multi-device, geography, demographic metadata | multi-center, cross-device, domain adaptation, external validation |
| Multimodal learning | Linked fundus, OCT, visual field, tabular, text, or genetics | multimodal ophthalmology dataset, fundus OCT dataset, imaging clinical dataset |
| Report generation and language | Reports, captions, clinical notes, structured findings | ophthalmology report dataset, retinal report generation, image captioning eye dataset |

## Common Dataset Types

Distinguish the dataset type before deciding how to register it.

| Dataset type | Register as | Notes |
|---|---|---|
| Primary public dataset | New dataset if not already covered | Prefer the official source page, data paper, and original citation. |
| Challenge dataset | Dataset or benchmark, depending on source structure | Record challenge access terms, train/test visibility, and whether labels are public. |
| Hospital or screening cohort | Dataset if data are accessible or clearly documented | Capture institution, country, cohort criteria, and access restrictions. |
| Data paper archive | Dataset if files are deposited and reusable terms are available | Use repository metadata and the paper for sample counts and methods. |
| Annotation extension | Separate dataset only if annotations are independently published and useful | Link to the base dataset and describe what annotation layer is new. |
| Curated subset | Usually not a new dataset unless separately released with stable access and citation | Note selection criteria and parent dataset relationship. |
| Mirror or rehost | Usually not a new dataset | Prefer the original source unless the mirror has distinct terms or stable derived content. |
| Composite benchmark | Register carefully as composite or derived | Identify every parent dataset and avoid double-counting images. |
| Synthetic dataset | Dataset if source generation method, files, and license are clear | Mark synthetic status and avoid presenting it as patient-derived data. |
| Teaching atlas or image gallery | Usually exclude unless downloadable and licensed for dataset use | Many atlases are useful references but not reusable datasets. |

## Qualification Criteria

Use these checks before proposing a dataset entry.

| Criterion | Accept when | Reject or defer when |
|---|---|---|
| Public source | There is a stable source page, repository, DOI, challenge page, or institutional page | Only a secondary blog, copied archive, or broken link is available |
| Access path | Files are downloadable, gated with documented terms, or manually requestable | The dataset is only mentioned in a paper with no data access path |
| License or terms | License, terms of use, challenge rules, or data-use agreement are visible | Terms are absent, contradictory, or copied from an unofficial mirror |
| Ophthalmic relevance | The dataset contains eye, ocular, visual function, or ophthalmic clinical data | Eye content is incidental or not separable from a broader non-eye dataset |
| Metadata sufficiency | Source supports modality, task, sample unit, rough scale, and access notes | Basic identity, modality, or source provenance cannot be verified |
| Citation path | There is a paper, DOI, repository citation, or source-recommended citation | No stable citation or attribution path exists |
| Ethical and privacy status | Source describes de-identification, consent, review, or public release basis when relevant | Identifiable patient media are exposed without clear release basis |
| Catalog fit | It adds a new source, modality, task, annotation layer, or access route | It is only a duplicate mirror or undocumented repost |

Minimum useful notes for a candidate:

- Dataset name and known aliases
- Primary URL and backup URL if relevant
- Citation or DOI
- Modality and anatomical scope
- Task and annotation type
- Sample unit: images, eyes, patients, visits, videos, volumes, or records
- Access type: direct, platform, gated, challenge, manual, or unavailable
- License or terms text exactly as stated by the source
- Relationship to existing catalog entries

## Duplicate And Composite Detection Criteria

Many ophthalmology datasets appear under multiple names, mirrors, challenge
pages, papers, Kaggle uploads, Hugging Face repos, and institutional pages.
Check for duplication before adding a new entry.

Signals that two candidates are probably the same dataset:

- Same acronym, expanded name, or distinctive dataset title.
- Same DOI, arXiv paper, challenge page, repository record, or citation.
- Same authors, institution, recruitment site, and collection period.
- Same sample counts, class distributions, image dimensions, or train/test
  split sizes.
- Same file names, folder layout, checksums, or archive names.
- Same images visible in thumbnails, papers, README examples, or challenge
  documentation.
- Same license text and access instructions copied across mirrors.
- A source page explicitly says it mirrors, republishes, or converts another
  dataset.

Signals that a candidate may be a derived or composite dataset rather than a
duplicate:

- It adds new labels, masks, grades, reports, quality scores, or splits to an
  existing image set.
- It merges multiple named datasets into a benchmark, often with harmonized
  labels or resized images.
- It converts formats, crops regions, normalizes images, or packages a model
  training subset from one or more parent datasets.
- It includes both original files and generated or synthetic augmentations.
- It cites parent datasets but publishes a new stable archive and citation.

Suggested handling:

- Prefer the original dataset as the primary catalog entry when mirrors do
  not add distinct annotations, access terms, or citation value.
- Register a derived annotation set only when the added annotation layer is
  independently accessible, citable, and useful.
- For composites, record parent datasets in notes and avoid implying that all
  samples are newly collected.
- For challenge splits, distinguish training data, validation labels, hidden
  test sets, and leaderboard-only evaluation.
- When unsure, leave a duplicate-risk note for human review instead of adding
  a confident new entry.

## Catalog Overlap Notes

The current catalog intentionally keeps some derivative resources when they
add a useful task, annotation layer, benchmark split, or machine-readable
representation. These records should not be interpreted as independent
patient cohorts unless their notes say so.

High-confidence duplicate, subset, or derivative relationships:

| Catalog entries | Relationship | Handling |
|---|---|---|
| `bidr`, `dr_arranged`, `eyepacs` | `bidr` and `dr_arranged` are EyePACS-based reposts/subsets. | Keep for reproducibility and access history; do not count as independent cohorts. |
| `aod`, `odir2019` | AOD is an augmented ODIR-5K derivative. | Keep as an augmentation/preprocessing resource. |
| `aptos_arcade_onh_masks`, `aptos2019` | APTOS-derived vascular arcade and optic nerve head masks. | Keep as an annotation layer. |
| `maples_dr`, `messidor1`/`messidor2` | MAPLES-DR re-annotates MESSIDOR images with biomarker masks. | Keep as an annotation layer; verify exact source release when using image-level splits. |
| `riga`, `riga_plus`, `messidor1`/`messidor2` | RIGA includes a MESSIDOR sub-archive; RIGA+ is a domain-adaptation derivative. | Keep but flag partial overlap. |
| `dme_vqa`, `dme_vqa_logical`, `idrid`, `e_ophtha` | VQA layers derived from existing fundus datasets; logical variant extends DME VQA. | Keep as language/VQA task resources, not new image cohorts. |
| `retinal_vessel_robustness`, `rite`, `stare`, `chase_db1` | Robustness/artery-vein resources derive from common vessel datasets; RITE is DRIVE-based. | Keep task-specific annotation/benchmark records; track parent datasets. |
| `cataract101_extended_labels`, `cataract_101` | Label extension for Cataract-101 videos. | Keep as a label layer. |
| `rfmid2`, `rfmid` | Versioned auxiliary RFMiD release. | Keep as an extension, not a duplicate. |
| `brset_mbrset_embeddings`, `brset`, `mbrset` | Embedding representation derived from BRSET/MBRSET. | Keep as a representation layer. |
| `fairvlmed`, `harvard_fairvision` | Text/NPZ view of the Harvard FairVision cohort. | Keep as a derived multimodal view. |
| `stage_task1`, `stage_task2`, `stage_task3` | Same challenge collection exposed as separate task records. | Keep task records; avoid adding sample counts together. |

Composite or broad derived corpora that need especially careful citation:

- `amdnet23`: compiled from ODIR, DR_200, Fundus Dataset, RFMiD, HRF, and
  ARIA.
- `rao_fundus`: web/public data plus RFMiD and JSIEC.
- `fundus_domain_generalization`: benchmark assembled from existing
  glaucoma/fundus segmentation datasets.
- `smdg`: aggregate glaucoma benchmark spanning many public sources.
- `hassan_composite_retina`, `multieye`, `mm_retinal_reason`,
  `eyecare_100k`, `x_pcr`, `fundus_report_dataset`,
  `intraretinal_cystoid_fluid`, `lmod_cataract_1k`,
  `lmod_cataract_1k_cot`, and `ocular_chat_vqa`: retain only as
  task-specific derived/composite resources and verify parent-source terms.

High-risk overlap clusters for future audit:

- `mured` versus `rfmid` and `odir2019`: similar multi-disease fundus scope,
  but local metadata do not prove reuse. Compare upstream papers, filenames,
  and hashes before flagging.
- `messidor1`, `messidor2`, `riga`, `riga_plus`, and `maples_dr`: high-risk
  MESSIDOR overlap cluster.
- `stare`, `chase_db1`, `rite`, and `retinal_vessel_robustness`: vessel
  segmentation overlap cluster. Add canonical DRIVE relationship handling if
  DRIVE is later reintroduced.

## Search Workflow Record

The July 2026 follow-up search used the catalog plus PubMed, Consensus, web
search, and platform pages. The intent was not to exhaust every possible
archive again, but to stress-test the guide and identify high-confidence
additions missed by the current catalog.

Search channels used:

- Consensus query: `ophthalmology public dataset fundus OCT slit lamp cornea
  dataset year:2020-2026`.
- PubMed/web queries: `SLID slit-lamp image dataset anatomical segmentation
  lesion detection GitHub`, `ScLNet cornea scleral lens OCT layers
  segmentation dataset public`, `retinal branching angle detection dataset`,
  `FPRM retina psychological assessment dataset`, and related exact-title
  queries.
- Platform/web queries: `ScLNet cornea scleral lens OCT dataset GitHub data
  download`, `OCT and eye fundus dataset diabetic macular edema diabetic
  retinopathy GitHub`, `RETA retinal vascular tree analysis Figshare`,
  `MSHF fundus image quality assessment Figshare`, `OphthalVQA Figshare`,
  `OphthalWeChat Figshare`, and exact repository-title searches.
- Platform API and source-page checks: GitHub repository contents and license
  metadata, Zenodo record metadata, Figshare DOI landing pages, PubMed/PMC data
  availability statements, and DOI-backed Synapse landing pages.
- Local catalog checks: `eyehub search --json`, direct metadata
  keyword scans for `slid`, `slit`, `sclnet`, `scleral`, `mured`, `rfmid`,
  `odir`, `aptos`, `dme_vqa`, `riga`, `messidor`, `stare`, `chase`, `reta`,
  `mshf`, `ophthal`, `rbad`, `eed`, and `fprm`.

Candidate outcomes from this pass:

| Candidate | Evidence | Catalog action |
|---|---|---|
| SLID slit-lamp dataset | PubMed/Consensus and GitHub availability were found, but `slid` is already registered. | No new entry. |
| ScLNet cornea with scleral-lens OCT | PubMed/Consensus describes a public dataset, but the visible GitHub repository exposed code and two example images rather than the full dataset archive during review. | Defer until a stable full-data access route is verified. |
| SLIT-Net microbial keratitis slit-lamp data | GitHub README points to a Duke Box dataset download. | Candidate for future verification; check license/access terms before adding. |
| OCT and Eye Fundus Dataset for DME and DR | GitHub repository exposes fundus and OCT image folders plus CSV labels, with 1,548 fundus images and 1,113 OCT images. No repository license was declared. | Added as `oct_fundus_dme_dr_mexico` with `Unknown` license caveat. |
| RBAD retinal branching-angle detection | Public GitHub repository exposes a small benchmark and non-commercial academic license terms. | Added as `rbad`; reuse is marked research-only/non-commercial. |
| EED-Astig | Zenodo record describes pediatric external-eye photographs, corneal masks, keypoints, and tabular parameters under a data-use agreement. | Added as `eed_astig`; access remains manual/DUA. |
| FPRM multimodal eye imaging and psychological assessment | Scientific Data/PubMed record and Synapse DOI document fundus photographs, multispectral/functional retinal imaging, videos, labels, and psychological assessments under a DUA. | Added as `fprm_retina`; access remains manual/DUA. |
| RETA retinal vascular-tree benchmark | Figshare DOI and data paper describe IDRiD-derived images with vessel, artery/vein, bifurcation, tree, and abnormality annotations under CC BY 4.0. | Added as `reta_benchmark`; notes mark it as an IDRiD-derived annotation benchmark. |
| MSHF fundus image-quality assessment | Figshare DOI identifies a multi-source heterogeneous fundus image-quality dataset under CC BY 4.0. | Added as `mshf`; notes flag multi-source composition. |
| OphthalVQA | Figshare DOI provides a VQA benchmark dataset under CC BY 4.0. | Added as `ophthalvqa`; notes recommend provenance and leakage checks before validation. |
| OphthalWeChat | Figshare DOI exposes WeChat article and image-link metadata, not redistributed image files, with non-commercial linked-content restrictions. | Added as `ophthalwechat`; modality is text/index metadata and license is non-commercial. |

## Search Query Patterns

Start broad, then constrain by anatomy, modality, task, and source type.

```text
"ophthalmology dataset" +"fundus"
+"retinal image dataset" +"segmentation"
+"OCT dataset" +"macular" +"fluid"
+"glaucoma dataset" +"optic disc" +"visual field"
+"corneal dataset" +"keratoconus" +"topography"
+"slit lamp dataset" +"cataract grading"
+"OCTA dataset" +"FAZ segmentation"
+"fluorescein angiography dataset" +"retina"
+"eye tracking dataset" +"gaze estimation"
+"ophthalmology EHR dataset" +"imaging"
```

Repository-specific patterns:

```text
site:physionet.org ophthalmology dataset
site:zenodo.org retina dataset
site:figshare.com ophthalmology dataset
site:mendeley.com "retinal" "dataset"
site:kaggle.com "fundus" "dataset"
site:huggingface.co/datasets ophthalmology
site:grand-challenge.org retina challenge
site:codalab.lisn.upsaclay.fr ophthalmology challenge
site:synapse.org retina dataset
site:github.com "ophthalmology dataset"
```

Paper-oriented patterns:

```text
"a dataset for" ophthalmology images
"publicly available" "retinal" "dataset"
"benchmark dataset" "fundus"
"data descriptor" ophthalmology
"Scientific Data" ophthalmology dataset
"segmentation dataset" "optical coherence tomography"
```

Access and license patterns:

```text
"ophthalmology dataset" "license"
"retinal dataset" "CC BY"
"fundus dataset" "data use agreement"
"OCT dataset" "challenge rules"
"eye dataset" "terms of use"
```

## Agent Notes

When an agent explores candidates, produce evidence rather than conclusions.
A useful handoff note includes:

- Source URL and date accessed.
- Exact source language for license or terms.
- Evidence for sample counts and annotation types.
- Known aliases and mirror URLs.
- Duplicate or composite concerns.
- Proposed catalog action: add, defer, exclude, merge with existing entry, or
  request human review.

Do not download large archives during discovery. Do not bypass forms, logins,
challenge registrations, data-use agreements, or institutional access controls.

## PR Handoff For New Datasets

If a candidate passes qualification and is not already represented in the
catalog, prepare a focused PR rather than mixing it with unrelated cleanup.
For agent-driven changes, use `.claude/skills/add-dataset/SKILL.md` and the
agent-fillable PR template in that skill directory.

Required PR evidence:

- Primary source URL, access route, and date accessed.
- Exact license or terms text. If absent, set `license="Unknown"` and explain
  the missing source terms in `notes`.
- Citation, DOI, PubMed ID, or repository-recommended citation.
- Modality, anatomical scope, task, sample unit, and source-reported count.
- Duplicate/composite assessment with parent datasets named explicitly.
- Files changed, generated docs status, and smoke-test output.

Do not open an add-dataset PR when the only evidence is a paper abstract, a
model-code repository without data, a mirror with unclear provenance, or a
dataset whose license conflicts with the original source.

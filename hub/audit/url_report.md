# EyeDataHub URL Audit Report

- **Total datasets checked**: 251
- **Broken URLs**: 3
- **Generated at**: 2026-07-26T05:38:02.388526+00:00
- **EyeDataHub version**: 0.2.2
- **Git commit**: 9eb179cb47ed3f443c04b97523e9008b470f521a
- **Git dirty**: True
- **Timeout / concurrency**: 30 s / 8

## Status distribution

| Status | Count |
| --- | ---:|
| ok | 171 |
| no_bot_allowed | 67 |
| forbidden | 10 |
| ssl_error | 3 |

## Status definitions

| Status | Definition |
| --- | --- |
| `ok` | HTTP 2xx response after redirects; technical reachability only. |
| `forbidden` | HTTP 403 response; often bot-blocked, browser-gated, or manually accessible. |
| `no_bot_allowed` | Mendeley Data or Zenodo returned HTTP 403 to automated probes even though manually checked source links were healthy; this reflects bot blocking, not a dead link. |
| `auth_required` | HTTP 401 or known access-controlled host requiring authentication. |
| `not_found` | HTTP 404 response; source-page review or replacement URL required. |
| `connect_error` | Connection failure during automated request. |
| `ssl_error` | TLS/SSL validation failure during automated request. |
| `timeout` | No response within configured timeout. |
| `server_error` | HTTP 5xx response from source host. |
| `http_*` | Other non-success HTTP response requiring source-page review. |
| `no_url` | No URL recorded in the catalog record. |

## Broken / unreachable

| Dataset | Status | URL |
| --- | --- | --- |
| `stare` | `ssl_error` | [cecas.clemson.edu/~ahoover](https://cecas.clemson.edu/~ahoover/stare/) |
| `drions_db` | `ssl_error` | [ia.uned.es/~ejcarmona](https://www.ia.uned.es/~ejcarmona/DRIONS-DB.html) |
| `fire` | `ssl_error` | [projects.ics.forth.gr/cvrl](https://projects.ics.forth.gr/cvrl/fire/) |

## All findings

| Dataset | Backend | Status | HTTP | Source URL |
| --- | --- | --- | ---:| --- |
| `aroma_octa` | `zenodo` | `forbidden` | 403 | [https://doi.org/10.5281/zenodo.18258095](https://doi.org/10.5281/zenodo.18258095) |
| `birdshot_wide` | `manual` | `forbidden` | 403 | [https://doi.org/10.5281/zenodo.19474623](https://doi.org/10.5281/zenodo.19474623) |
| `eed_astig` | `manual` | `forbidden` | 403 | [https://doi.org/10.5281/zenodo.18976824](https://doi.org/10.5281/zenodo.18976824) |
| `gaze360` | `manual` | `forbidden` | 403 | [gaze360.csail.mit.edu](https://gaze360.csail.mit.edu/) |
| `goblet_cell_segmentation` | `zenodo` | `forbidden` | 403 | [https://doi.org/10.5281/zenodo.18642562](https://doi.org/10.5281/zenodo.18642562) |
| `ichallenge_amd` | `manual` | `forbidden` | 403 | [amd.grand-challenge.org/download](https://amd.grand-challenge.org/download/) |
| `maetschke_glaucoma_oct` | `zenodo` | `forbidden` | 403 | [https://doi.org/10.5281/zenodo.1481223](https://doi.org/10.5281/zenodo.1481223) |
| `periorbital_segmentation` | `zenodo` | `forbidden` | 403 | [https://doi.org/10.5281/zenodo.13916845](https://doi.org/10.5281/zenodo.13916845) |
| `riga` | `direct` | `forbidden` | 403 | [deepblue.lib.umich.edu/data](https://deepblue.lib.umich.edu/data/concern/data_sets/3b591905z) |
| `syn_oct` | `zenodo` | `forbidden` | 403 | [https://doi.org/10.5281/zenodo.17151869](https://doi.org/10.5281/zenodo.17151869) |
| `afio_fundus_vessels` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3csr652p9y/2) |
| `airogs` | `direct` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/5793241) |
| `amdnet23` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yj35kjgrv3/1) |
| `anterior_segment_smile` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/vkdxsnhkrm/1) |
| `aptos_arcade_onh_masks` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/20711325) |
| `bajwa_multi_eye` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/rgwpd4m785/3) |
| `bmrd` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/959whsbc6v/1) |
| `cataract101_extended_labels` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/4984167) |
| `chronic_corneal_disorders` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mcwv6thk8m/1) |
| `corn1500` | `manual` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/5880419) |
| `corn_collection` | `manual` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/19689814) |
| `corn_pro` | `manual` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/14263883) |
| `corneal_curvature_fundus` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bc2jfr7dv9/1) |
| `corneal_epithelium_confocal` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/n3gky25brh/2) |
| `corneal_parameters_kc` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3nz4fkwn3y/1) |
| `corneal_tomography_iol` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/wddj7bh9p9/1) |
| `cornorb` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/20542091) |
| `csc_fundus_segmentation` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/4k64fwnp4k/5) |
| `data_oct_fundus_glaucoma` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/2rnnz5nz74/2) |
| `deepdrid` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/8248825) |
| `dme_vqa` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/6784358) |
| `dme_vqa_logical` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/7777849) |
| `drac22` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/10280359) |
| `external_eye_blepharitis` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bp37vw4z8d/1) |
| `eye_conjunctiva_segmentation` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yxwjgcndg2/1) |
| `eye_disease_image_mendeley` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/s9bfhswzjb/1) |
| `eyecatcher_visual_field` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/swsfj47cxw/2) |
| `fimd` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jkzsh6pcv4/1) |
| `fociset_pamm` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mkwxn7rjpm/2) |
| `fundus_domain_generalization` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/8009107) |
| `ghana_eye_screening` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mfv6sb5wyc/4) |
| `glaucoma_eye_movements` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/7761477) |
| `hassan_composite_retina` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/trghs22fpg/4) |
| `hrf_seg_plus` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/16744782) |
| `irfdrd` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/12552326) |
| `jrc_multimodal_vessels` | `manual` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/17874693) |
| `jsiec` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/record](https://zenodo.org/record/3477553) |
| `justraigs` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/10035093) |
| `leops_erg` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w3yx7hdds7/1) |
| `mario` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/15270469) |
| `migs_video` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/19438128) |
| `msila_fundus_dr` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/19169587) |
| `mured` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/pc4mb3h8hz/1) |
| `myopic_regression_fundus` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/k34rvfw3dg/2) |
| `nehut` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/8kt969dhx6/2) |
| `octa_macula_coronal` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/p5h7x55zw7/1) |
| `octave` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/14580071) |
| `octdl` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/sncdhf53xc/4) |
| `olives` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/7105232) |
| `ophtho_readability` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/16592100) |
| `papila` | `direct` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/6379970) |
| `paraguay_dr` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/record](https://zenodo.org/record/4647952) |
| `popeye_nir` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/18430187) |
| `rao_fundus` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/5428684j44/1) |
| `retinal_corrugations_oct` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bzsc7gd9p3/1) |
| `retinal_vessel_robustness` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/12659652) |
| `rfmid2` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/7505822) |
| `riga_plus` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/6325549) |
| `rop_synthetic_mendeley` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/fscyyhg6vt/1) |
| `rose` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/doi](https://zenodo.org/doi/10.5281/zenodo.12775880) |
| `sics155` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/19482928) |
| `superccm_fineset` | `manual` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/17051148) |
| `thyroid_ophthalmopathy_external` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/z7ys7r4bdn/2) |
| `trend2_fundus` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/7678656) |
| `trend_fundus` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/4521044) |
| `ut_fsocta` | `zenodo` | `no_bot_allowed` | 403 | [zenodo.org/records](https://zenodo.org/records/6476639) |
| `uveitis_smote` | `mendeley` | `no_bot_allowed` | 403 | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/n9zp473wfw/2) |
| `acrima` | `figshare` | `ok` | 202 | [figshare.com/s](https://figshare.com/s/c2d31f850af14c5b5232) |
| `adam_challenge` | `gdrive` | `ok` | 200 | [drive.google.com/file](https://drive.google.com/file/d/1Uz5x0aqXb0aecjzNWQ4522oCxaRDZxBt/view) |
| `agar300` | `manual` | `ok` | 200 | [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/diabetic-retinopathy-fundus-image-datasetagar300) |
| `age_challenge` | `gdrive` | `ok` | 200 | [drive.google.com/file](https://drive.google.com/file/d/1Qlkqj74SW8DJRKdYL_-ApC_0H5Z7uyvr/view) |
| `amd_dme_3d_oct` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.30582035.v1](https://doi.org/10.6084/m9.figshare.30582035.v1) |
| `amd_sd` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/gaoweihao/amd-sd) |
| `angioreport` | `manual` | `ok` | 200 | [tianchi.aliyun.com/dataset](https://tianchi.aliyun.com/dataset/170128) |
| `aod` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases) |
| `aptos2019` | `kaggle` | `ok` | 200 | [kaggle.com/c](https://www.kaggle.com/c/aptos2019-blindness-detection) |
| `aroi` | `gdrive` | `ok` | 200 | [drive.google.com/file](https://drive.google.com/file/d/10Ys4xsw81evjHewZEvqHy4Kri0my8C2S/view) |
| `as_oct_keratitis` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.c.7036994.v1](https://doi.org/10.6084/m9.figshare.c.7036994.v1) |
| `beh` | `gdrive` | `ok` | 200 | [drive.google.com/file](https://drive.google.com/file/d/1YdZm-sioiAbTdBRy4oej1q6tZL8Baft7) |
| `belo` | `manual` | `ok` | 200 | [belo-dataset.vercel.app](https://belo-dataset.vercel.app/) |
| `bidr` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy) |
| `brset` | `physionet` | `ok` | 200 | [physionet.org/content](https://physionet.org/content/brazilian-ophthalmological/1.0.1/) |
| `brset_mbrset_embeddings` | `physionet` | `ok` | 200 | [physionet.org/content](https://physionet.org/content/embedding-brset-mbrset/1.0.0/) |
| `cadis` | `manual` | `ok` | 200 | [cataracts-semantic-segmentation2020.grand-challenge.org](https://cataracts-semantic-segmentation2020.grand-challenge.org/) |
| `casia_iris_v4` | `manual` | `ok` | 200 | [hycasia.github.io/dataset](https://hycasia.github.io/dataset/casia-irisv4/) |
| `cataract` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/jr2ngb/cataractdataset) |
| `cataract1k` | `manual` | `ok` | 200 | [synapse.org](https://www.synapse.org/#!Synapse:syn53404917) |
| `cataract_101` | `manual` | `ok` | 200 | [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/cat-101/) |
| `cataract_lmm` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/mjahmadi/Cataract-LMM) |
| `cataracts2017` | `manual` | `ok` | 200 | [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/cataracts) |
| `cavri` | `manual` | `ok` | 200 | [dsp.put.poznan.pl/cavri_database-191](https://dsp.put.poznan.pl/cavri_database-191/) |
| `chaksu` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.20123135](https://doi.org/10.6084/m9.figshare.20123135) |
| `chase_db1` | `manual` | `ok` | 200 | [researchinnovation.kingston.ac.uk/en](https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/) |
| `coph100` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.27061084.v1](https://doi.org/10.6084/m9.figshare.27061084.v1) |
| `csdi` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/RainyNight/CSDI) |
| `ddr` | `gdrive` | `ok` | 200 | [drive.google.com/drive](https://drive.google.com/drive/folders/1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC) |
| `deepeyenet` | `manual` | `ok` | 200 | [github.com/Jhhuangkay](https://github.com/Jhhuangkay/DeepOpht-Medical-Report-Generation-for-Retinal-Images-via-Deep-Models-and-Visual-Explanation) |
| `dr_arranged` | `manual` | `ok` | 200 | [tianchi.aliyun.com/dataset](https://tianchi.aliyun.com/dataset/93926) |
| `dridb` | `manual` | `ok` | 200 | [ipg.fer.hr/ipg](https://ipg.fer.hr/ipg/resources/image_database) |
| `drishti_gs` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation) |
| `drive` | `manual` | `ok` | 200 | [drive.grand-challenge.org/DRIVE](https://drive.grand-challenge.org/DRIVE/) |
| `drtid` | `manual` | `ok` | 200 | [github.com/FDU-VTS](https://github.com/FDU-VTS/DRTiD) |
| `dryad_aoslo_rpe` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.b41j15h](https://doi.org/10.5061/dryad.b41j15h) |
| `dryad_cornea_oct_pentacam` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.tht76hf0c](https://doi.org/10.5061/dryad.tht76hf0c) |
| `dryad_functional_oct_alzheimer` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| `dryad_gcc_glaucoma` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.xwdbrv1tn](https://doi.org/10.5061/dryad.xwdbrv1tn) |
| `dryad_glaucoma_rnfl_vf` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.q6ft5](https://doi.org/10.5061/dryad.q6ft5) |
| `dryad_namd_oct_quant` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.2rbnzs7m4](https://doi.org/10.5061/dryad.2rbnzs7m4) |
| `dryad_namd_visual_prediction` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.573n5tb5d](https://doi.org/10.5061/dryad.573n5tb5d) |
| `dryad_retinal_vein_cannulation` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.3ffbg79zd](https://doi.org/10.5061/dryad.3ffbg79zd) |
| `dryad_subretinal_robot` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.w0vt4b91w](https://doi.org/10.5061/dryad.w0vt4b91w) |
| `dryad_uveal_melanoma_coog2` | `dryad` | `ok` | 200 | [https://doi.org/10.5061/dryad.n8pk0p340](https://doi.org/10.5061/dryad.n8pk0p340) |
| `duke_amd_chiu` | `manual` | `ok` | 200 | [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Chiu_IOVS_2011_dataset.htm) |
| `duke_chiu_boe` | `direct` | `ok` | 200 | [people.duke.edu/~sf59](http://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm) |
| `duke_rpedc` | `manual` | `ok` | 200 | [people.duke.edu/~sf59](https://people.duke.edu/~sf59/RPEDC_Ophth_2013_dataset.htm) |
| `e_ophtha` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma) |
| `erdes` | `manual` | `ok` | 200 | [arxiv.org/abs](https://arxiv.org/abs/2503.04525) |
| `eth_xgaze` | `manual` | `ok` | 200 | [ait.ethz.ch/xgaze](https://ait.ethz.ch/xgaze) |
| `eyecare_100k` | `huggingface` | `ok` | 200 | [github.com/DCDmllm](https://github.com/DCDmllm/EyecareGPT) |
| `eyepacs` | `kaggle` | `ok` | 200 | [kaggle.com/c](https://www.kaggle.com/c/diabetic-retinopathy-detection) |
| `eyeq` | `github` | `ok` | 200 | [github.com/HzFu](https://github.com/HzFu/EyeQ) |
| `fairvlmed` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/harvardairobotics/FairVLMed) |
| `fang_sbsdi_oct` | `manual` | `ok` | 200 | [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Fang_TMI_2013.htm) |
| `farfum_rop` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.c.6721269](https://doi.org/10.6084/m9.figshare.c.6721269) |
| `ffa_ir` | `physionet` | `ok` | 200 | [https://doi.org/10.13026/k5rp-9h43](https://doi.org/10.13026/k5rp-9h43) |
| `fiqs` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.28129847.v1](https://doi.org/10.6084/m9.figshare.28129847.v1) |
| `fives` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.19688169](https://doi.org/10.6084/m9.figshare.19688169) |
| `fovea` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.28329338](https://doi.org/10.6084/m9.figshare.28329338) |
| `fprm_retina` | `manual` | `ok` | 200 | [https://doi.org/10.7303/syn61672643](https://doi.org/10.7303/syn61672643) |
| `fundus_105k` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/PJMixers-Dev/Fundus-105K) |
| `fundus_avseg` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.27938034](https://doi.org/10.6084/m9.figshare.27938034) |
| `fundus_cc_2_5m` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/PJMixers-Dev/Fundus-CC-2.5M) |
| `fundus_report_dataset` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/zzzzineun/fundus-report-dataset) |
| `g1020` | `kaggle` | `ok` | 200 | [arxiv.org/abs](https://arxiv.org/abs/2006.09158) |
| `gamma` | `gdrive` | `ok` | 200 | [drive.google.com/file](https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view) |
| `gaze_capture` | `manual` | `ok` | 200 | [gazecapture.csail.mit.edu/dataset.php](https://gazecapture.csail.mit.edu/dataset.php) |
| `goals` | `gdrive` | `ok` | 200 | [aistudio.baidu.com/competition](https://aistudio.baidu.com/competition/detail/783/0/introduction) |
| `grape` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.c.6406319](https://doi.org/10.6084/m9.figshare.c.6406319) |
| `harvard_fairvision` | `manual` | `ok` | 200 | [ophai.hms.harvard.edu/datasets](https://ophai.hms.harvard.edu/datasets/harvard-fairvision30k) |
| `harvard_gdp` | `gdrive` | `ok` | 200 | [drive.google.com/drive](https://drive.google.com/drive/folders/1JMi_HCql113uc9X0DOaMkNfEWfxaDlEz) |
| `harvard_glaucoma` | `direct` | `ok` | 202 | [https://doi.org/10.7910/DVN/1YRRAC](https://doi.org/10.7910/DVN/1YRRAC) |
| `hei_med` | `github` | `ok` | 200 | [github.com/lgiancaUTH](https://github.com/lgiancaUTH/HEI-MED) |
| `hpmi` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.24800232](https://doi.org/10.6084/m9.figshare.24800232) |
| `hrf` | `manual` | `ok` | 200 | [www5.cs.fau.de/research](https://www5.cs.fau.de/research/data/fundus-images/) |
| `hyamd` | `physionet` | `ok` | 200 | [https://doi.org/10.13026/f0dn-8q46](https://doi.org/10.13026/f0dn-8q46) |
| `hygd` | `physionet` | `ok` | 200 | [https://doi.org/10.13026/pdxv-m215](https://doi.org/10.13026/pdxv-m215) |
| `ichallenge_oct` | `manual` | `ok` | 200 | [hdmilab.cn/ichallenge](http://hdmilab.cn/ichallenge) |
| `idrid` | `manual` | `ok` | 200 | [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid) |
| `insegcat` | `manual` | `ok` | 200 | [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/InSegCat/) |
| `intraretinal_cystoid_fluid` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid) |
| `jichi` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.4879853](https://doi.org/10.6084/m9.figshare.4879853) |
| `keratoconus_detection_kaggle` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/elmehdi12/keratoconus-detection) |
| `kermany_oct` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/paultimothymooney/kermany2018) |
| `lag` | `manual` | `ok` | 200 | [github.com/smilell](https://github.com/smilell/AG-CNN) |
| `lmod_cataract_1k` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K) |
| `lmod_cataract_1k_cot` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot) |
| `lmod_plus` | `manual` | `ok` | 200 | [kfzyqin.github.io/lmod_plus](https://kfzyqin.github.io/lmod_plus/) |
| `lpw` | `manual` | `ok` | 200 | [mpi-inf.mpg.de/de](https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw/) |
| `maples_dr` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.24328660](https://doi.org/10.6084/m9.figshare.24328660) |
| `mbrset` | `physionet` | `ok` | 200 | [physionet.org/content](https://physionet.org/content/mbrset/1.0/) |
| `mcoa` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.28123088.v1](https://doi.org/10.6084/m9.figshare.28123088.v1) |
| `messidor2` | `manual` | `ok` | 200 | [adcis.net/en](https://www.adcis.net/en/third-party/messidor2/) |
| `mfiddr` | `manual` | `ok` | 200 | [github.com/mfiddr](https://github.com/mfiddr/MFIDDR) |
| `mgd1k` | `github` | `ok` | 200 | [mgd1k.github.io/index.html](https://mgd1k.github.io/index.html) |
| `mm_retinal_reason` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason) |
| `mmrdr` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.29423747](https://doi.org/10.6084/m9.figshare.29423747) |
| `mpii_gaze` | `manual` | `ok` | 200 | [mpi-inf.mpg.de/de](https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild) |
| `mshf` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.21507564](https://doi.org/10.6084/m9.figshare.21507564) |
| `multieye` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/Luxuriant16/MultiEYE) |
| `nd_iris_0405` | `manual` | `ok` | 200 | [tsapps.nist.gov/BDbC](https://tsapps.nist.gov/BDbC/Search/Details/371) |
| `ochid` | `manual` | `ok` | 200 | [imed.nimte.ac.cn/OCHID.html](https://imed.nimte.ac.cn/OCHID.html) |
| `oct5k` | `direct` | `ok` | 202 | [https://doi.org/10.5522/04/22128671](https://doi.org/10.5522/04/22128671) |
| `oct_c8` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/obulisainaren/retinal-oct-c8) |
| `oct_cirrus` | `manual` | `ok` | 200 | [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Srinivasan_BOE_2014_dataset.htm) |
| `oct_fundus_dme_dr_mexico` | `github` | `ok` | 200 | [github.com/Traslational-Visual-Health-Laboratory](https://github.com/Traslational-Visual-Health-Laboratory/OCT-AND-EYE-FUNDUS-DATASET) |
| `oct_macular_hole_postsurgery` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/mathieugodbout/oct-postsurgery-visual-improvement) |
| `oct_ms_jhu` | `direct` | `ok` | 200 | [iacl.ece.jhu.edu/~aaron](https://iacl.ece.jhu.edu/~aaron/data/OCT_Manual_Delineations-2018_June_29_b.zip) |
| `octa_500` | `manual` | `ok` | 200 | [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/octa-500) |
| `octid` | `manual` | `ok` | 200 | [borealisdata.ca/dataverse](https://borealisdata.ca/dataverse/OCTID) |
| `ocular_chat_vqa` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/ncbi/OcularChat-VQA) |
| `oculoscope` | `figshare` | `ok` | 202 | [figshare.com/s](https://figshare.com/s/926c2c2ef9e77ab5eb9d) |
| `odir2019` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k) |
| `oimhs` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.23508453](https://doi.org/10.6084/m9.figshare.23508453) |
| `ophnet2024` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/xioamiyh/OphNet2024) |
| `ophora` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/General-Medical-AI/Ophora-160K) |
| `ophthalmology_eqa_v3` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-EQA-v3) |
| `ophthalmology_mcqa_v3` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-MCQA-v3) |
| `ophthalmology_pubmed_corpus` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-PubMed-Corpus) |
| `ophthalvqa` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.25624917](https://doi.org/10.6084/m9.figshare.25624917) |
| `ophthalwechat` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.29064149](https://doi.org/10.6084/m9.figshare.29064149) |
| `paired_retina` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/smartretina2025/paired_retina) |
| `palm` | `gdrive` | `ok` | 200 | [drive.google.com/file](https://drive.google.com/file/d/14XWD6kX0dVRfAyEc7FkZGKZibWEkvnyv/view) |
| `perg_ioba` | `physionet` | `ok` | 200 | [physionet.org/content](https://physionet.org/content/perg-ioba-dataset/1.0.0/) |
| `prime_fp20` | `manual` | `ok` | 200 | [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/prime-fp20-ultra-widefield-fundus-photography-vessel-segmentation-dataset) |
| `rasti_oct` | `manual` | `ok` | 200 | [drive.google.com/file](https://drive.google.com/file/d/1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu) |
| `ravir` | `gdrive` | `ok` | 200 | [ravir.grand-challenge.org/data](https://ravir.grand-challenge.org/data/) |
| `rbad` | `github` | `ok` | 200 | [github.com/Retinal-Research](https://github.com/Retinal-Research/RBAD) |
| `real_fundus` | `manual` | `ok` | 200 | [github.com/dengzhuo-AI](https://github.com/dengzhuo-AI/Real-Fundus/releases/tag/v.1.0.0) |
| `refuge1_multirater` | `gdrive` | `ok` | 200 | [drive.google.com/file](https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view) |
| `refuge2` | `gdrive` | `ok` | 200 | [drive.google.com/file](https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view) |
| `refuge2018` | `manual` | `ok` | 200 | [refuge.grand-challenge.org](https://refuge.grand-challenge.org/) |
| `reta_benchmark` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.16960855](https://doi.org/10.6084/m9.figshare.16960855) |
| `retina_age_analysis` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/ramankamran/retina-age-analysis) |
| `retinal_dr_longitudinal` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/usama10/retinal-dr-longitudinal) |
| `retouch` | `manual` | `ok` | 200 | [retouch.grand-challenge.org](https://retouch.grand-challenge.org/) |
| `rfmid` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification) |
| `rimone_dl` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/orvile/rim-one-retinal-dataset-for-assessing-glaucoma) |
| `rite` | `manual` | `ok` | 200 | [eye.medicine.uiowa.edu/rite-dataset](https://eye.medicine.uiowa.edu/rite-dataset) |
| `roc` | `manual` | `ok` | 200 | [webeye.ophth.uiowa.edu/ROC](http://webeye.ophth.uiowa.edu/ROC/) |
| `rocc` | `manual` | `ok` | 200 | [rocc.grand-challenge.org](https://rocc.grand-challenge.org/) |
| `rop_ostrava` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/jananowakova/retinal-image-dataset-of-infants-and-rop) |
| `rop_uwf_intelligent` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.25514449](https://doi.org/10.6084/m9.figshare.25514449) |
| `ru_medical_texts_ophthalmology` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/cheshrcat/ru-medical-texts-ophtalmology) |
| `rvo_me` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.29804435.v1](https://doi.org/10.6084/m9.figshare.29804435.v1) |
| `slid` | `direct` | `ok` | 200 | [github.com/xumingyu-hub](https://github.com/xumingyu-hub/SLID) |
| `smdg` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset) |
| `soul_octa` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.24893358.v3](https://doi.org/10.6084/m9.figshare.24893358.v3) |
| `stage_task1` | `manual` | `ok` | 200 | [aistudio.baidu.com/aistudio](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets) |
| `stage_task2` | `manual` | `ok` | 200 | [aistudio.baidu.com/aistudio](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets) |
| `stage_task3` | `manual` | `ok` | 200 | [aistudio.baidu.com/aistudio](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets) |
| `sustech_sysu` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.12570770](https://doi.org/10.6084/m9.figshare.12570770) |
| `tear_meniscus` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.28650536.v2](https://doi.org/10.6084/m9.figshare.28650536.v2) |
| `teyed` | `manual` | `ok` | 200 | [arxiv.org/abs](https://arxiv.org/abs/2102.02115) |
| `thoct1800` | `github` | `ok` | 200 | [github.com/SJD095](https://github.com/SJD095/OCT-Segmentation) |
| `tian_oct` | `direct` | `ok` | 200 | [https://doi.org/10.1371/journal.pone.0133908.s002](https://doi.org/10.1371/journal.pone.0133908.s002) |
| `tom500` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.27133389.v1](https://doi.org/10.6084/m9.figshare.27133389.v1) |
| `toxofundus` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset) |
| `tsukazaki_uwf` | `github` | `ok` | 200 | [github.com/DateCazuki](https://github.com/DateCazuki/Fundus_Diagnosis) |
| `ubiris_v2` | `manual` | `ok` | 200 | [iris.di.ubi.pt/index.html](https://iris.di.ubi.pt/index.html) |
| `umn_parhi_oct` | `direct` | `ok` | 200 | [people.ece.umn.edu/users](http://people.ece.umn.edu/users/parhi/.DATA/OCT/DME/UMNDataset.mat) |
| `uwf_dr` | `gdrive` | `ok` | 200 | [drive.google.com/drive](https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu) |
| `uwf_dr_peng` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.31259494](https://doi.org/10.6084/m9.figshare.31259494) |
| `uwf_tumor` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.27986258](https://doi.org/10.6084/m9.figshare.27986258) |
| `uwf_zhejiang` | `figshare` | `ok` | 202 | [https://doi.org/10.6084/m9.figshare.26936446](https://doi.org/10.6084/m9.figshare.26936446) |
| `uwhvf` | `direct` | `ok` | 200 | [github.com/uw-biomedical-ml](https://github.com/uw-biomedical-ml/uwhvf/archive/refs/heads/master.zip) |
| `vietai_retinal_disease` | `kaggle` | `ok` | 200 | [kaggle.com/competitions](https://www.kaggle.com/competitions/vietai-advance-retinal-disease-detection-2020/data) |
| `visual_field_testing_experiment` | `kaggle` | `ok` | 200 | [kaggle.com/datasets](https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment) |
| `x_pcr` | `huggingface` | `ok` | 200 | [huggingface.co/datasets](https://huggingface.co/datasets/Fantasy666/X-PCR) |
| `drions_db` | `direct` | `ssl_error` | — | [ia.uned.es/~ejcarmona](https://www.ia.uned.es/~ejcarmona/DRIONS-DB.html) |
| `fire` | `direct` | `ssl_error` | — | [projects.ics.forth.gr/cvrl](https://projects.ics.forth.gr/cvrl/fire/) |
| `stare` | `direct` | `ssl_error` | — | [cecas.clemson.edu/~ahoover](https://cecas.clemson.edu/~ahoover/stare/) |

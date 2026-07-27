# Fundus and OCT literature refresh, 21 July 2026

This update followed recent fundus and OCT review searches. Candidate records
were compared with the live catalog and checked against an official dataset
page, repository record, or competition page. A resource was added only when
its identity, access route, source terms, and basic size or cohort description
could be recorded without relying on an undocumented mirror.

## Added resources

| Slug | Source | Access and terms |
| --- | --- | --- |
| `agar300` | IEEE DataPort, DOI `10.21227/fsnq-tn19` | Manual account route, CC BY 4.0 |
| `drive` | [DRIVE at Grand Challenge](https://drive.grand-challenge.org/DRIVE/) | Manual route, no named license on the official page |
| `hei_med` | [Official GitHub repository](https://github.com/lgiancaUTH/HEI-MED) | GitHub route, noncommercial research use |
| `dridb` | [University of Zagreb page](https://ipg.fer.hr/ipg/resources/image_database) | Email request, research and educational use |
| `eyeq` | [Official GitHub repository](https://github.com/HzFu/EyeQ) | Label terms are unclear; code is CC BY-NC-SA 4.0; EyePACS images obtained separately |
| `real_fundus` | [Official GitHub release](https://github.com/dengzhuo-AI/Real-Fundus/releases/tag/v.1.0.0) | Public release, no named dataset license |
| `fiqs` | Figshare, DOI `10.6084/m9.figshare.28129847.v1` | Figshare route, CC BY 4.0 |
| `octa_macula_coronal` | Mendeley Data, DOI `10.17632/p5h7x55zw7.1` | Mendeley route, CC BY 4.0 |
| `fang_sbsdi_oct` | [Official Duke page](https://people.duke.edu/~sf59/Fang_TMI_2013.htm) | Manual route, academic research use |
| `duke_amd_chiu` | [Official Duke page](https://people.duke.edu/~sf59/Chiu_IOVS_2011_dataset.htm) | Manual route, no named license on the page |
| `maetschke_glaucoma_oct` | Zenodo, DOI `10.5281/zenodo.1481223` | Zenodo route, CC BY-NC 4.0 |
| `ochid` | [Official project page](https://imed.nimte.ac.cn/OCHID.html) | Email request, academic research use |
| `thoct1800` | [Official GitHub repository](https://github.com/SJD095/OCT-Segmentation) | GitHub route, research and educational use |
| `vietai_retinal_disease` | [Official Kaggle competition](https://www.kaggle.com/competitions/vietai-advance-retinal-disease-detection-2020/data) | Kaggle competition rules |

## Corrected existing records

- `oct_cirrus` now points to the official Duke Srinivasan dataset rather than
  Zenodo record 1481223, which contains the Maetschke glaucoma data.
- `duke_rpedc` now describes the 384 subject RPE and drusen-complex resource
  reported by Farsiu et al.
- `jsiec` now records 1,000 images and Zenodo's `other-open` rights statement.
- `nehut` now uses the source classes Normal, Drusen, and CNV.

## Candidates not added

The update did not add DIARETDB0 or DIARETDB1, DR-HAGIS, OPTIMA Cyst,
Project MACULA, the UCI paired OCT and fundus record, the Yoo OCT collection,
the rare OCT collection, single case image deposits, or derivative Kaggle
packages. Their current route was unavailable, closed, incomplete, unofficial,
or did not establish a distinct reusable resource with clear provenance.

The automated URL check reached all 14 new source pages or received the
expected repository bot response. Registry validation and the full test suite
were run after the additions.

# EyeDataHub Hub Utilities

Utilities for building public catalog artifacts from the live EyeDataHub
registry.

## What Lives Here

| Path | Purpose |
|---|---|
| `audit/` | URL audit runner and JSON/Markdown reports. |
| `docs/` | Docusaurus and `llms-full.txt` generators. |
| `stats/` | Catalog statistics and figure-data scripts. |
| `open_catalogue.py` | Filter the registry to open-license datasets. |
| `enrich_metadata.py` | Maintain geography/scanner/demographic metadata snapshots. |
| `preprocess.py` | Optional harmonization pipeline for redistributable datasets. |
| `build_hf_dataset.py` | Optional Hugging Face dataset publisher for an EyeDataHub-Open mirror. |
| `label_schema.json` | Experimental cross-dataset label schema for redistributable subsets. |

## Common Commands

```bash
python -m hub.docs.generate_dataset_pages --out website/docs
python -m hub.docs.generate_llms_full
python -m hub.audit.verify_urls --out hub/audit/url_report.json --md hub/audit/url_report.md
python -m hub.stats.run_all --metadata hub/metadata.json --out reports/figures/auto
```

The live Python registry is authoritative. Do not add datasets to `hub/`
metadata snapshots without also adding them to `eyedatahub/datasets/` and
`eyedatahub/datasets/registry.py`.

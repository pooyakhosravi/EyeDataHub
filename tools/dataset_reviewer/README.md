# EyeDataHub internal dataset reviewer

This local-only review desk presents one current catalog record at a time and
saves subjective inclusion decisions separately from the public catalog.

## Start

From PowerShell at the repository root:

```powershell
.\tools\dataset_reviewer\start_review.ps1
```

Or run:

```powershell
python tools/dataset_reviewer/server.py --open
```

The server listens only on `127.0.0.1` by default. Stop it with `Ctrl+C`.

## Review workflow

- Apply the model-data boundary consistently. Retain deposits containing data
  that can serve as model inputs, targets, or linked covariates, including
  images, videos, raw signals, omics, gene expression, visual fields,
  refraction, biometry, and spatial or topographic maps. A table can qualify
  when the measurement is inherently tabular or when it accompanies a primary
  modality.
- Exclude article-result tables, aggregate statistical outputs, and tables that
  contain only derived OCT, OCTA, or retinal-layer measurements when the source
  images or volumes are absent. Mark uncertain participant-level clinical
  tables as Needs review rather than excluding them automatically.
- Apply any number of review tags.
- Optionally assign a usefulness score from 1 to 5.
- Choose Include, Needs review, Exclude, or Duplicate/version.
- Add notes describing what should be checked later.
- Use keys 1 through 4 for decisions, J/K or arrow keys to navigate, O to open
  the represented dataset source, and P to open the associated publication.

Every edit is saved atomically to:

```text
data/internal_dataset_review_decisions.json
```

That local decision file and its backup are ignored by Git. The interface can
also export a complete CSV or JSON review snapshot. The CSV contains all
catalog records, including those not yet reviewed, so it can be filtered and
reconciled later.

The reviewer reads `hub/catalog.json` each time it starts. It does not modify
the catalog or download any third-party data.

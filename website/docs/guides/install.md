---
id: install
title: "Install EyeDataHub"
sidebar_label: Install
description: "Install EyeDataHub and verify the command-line tool and Python package."
---

# Install EyeDataHub

EyeDataHub is a Python package with a command-line entry point named `eyehub`.

## Requirements

- Python 3.10 through 3.14
- Optional platform credentials for gated hosts such as Kaggle, PhysioNet, or
  Hugging Face
- Enough local disk for datasets you intentionally download

## From PyPI

```bash
python -m pip install --upgrade pip
python -m pip install "eyedatahub==0.2.2"
```

## From GitHub

```bash
python -m pip install --upgrade pip
python -m pip install "git+https://github.com/pooyakhosravi/EyeDataHub.git@v0.2.2"
```

## Editable Developer Install

```bash
git clone https://github.com/pooyakhosravi/EyeDataHub.git
cd EyeDataHub
python -m pip install -e .
pytest -q
```

## Verify The Install

```bash
eyehub --version
eyehub search --json
eyehub show airogs --json
eyehub download airogs --dry-run --json
```

The current installation should report 251 catalog records. The catalog
includes self-service, controlled, and author-contact routes; it is
not a claim that every resource is open or downloadable.

## Credentials

EyeDataHub does not bypass upstream access controls. Store local credentials in
a `.env` file at the repository root, or set them in your shell. Never commit
that file or include secrets in command output, issues, validation logs, or
provenance manifests.

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Uncomment and fill only the variables you need:

| Backend | Variables |
|---|---|
| Kaggle | `KAGGLE_USERNAME`, `KAGGLE_KEY` |
| Hugging Face | `HF_TOKEN` or `HUGGING_FACE_HUB_TOKEN` |
| Zenodo | `ZENODO_TOKEN` |
| Figshare | `FIGSHARE_TOKEN` |
| Mendeley Data | `MENDELEY_TOKEN` |
| Dataverse | `DATAVERSE_TOKEN` |
| PhysioNet | `PHYSIONET_USERNAME`, `PHYSIONET_PASSWORD` |
| Synapse | `SYNAPSE_AUTH_TOKEN`, or `SYNAPSE_USERNAME` and `SYNAPSE_PASSWORD` |

Shell variables take precedence over `.env` values. To use a credentials file
outside the repository, set `EYEDATAHUB_ENV_FILE` before running EyeDataHub:

```bash
export EYEDATAHUB_ENV_FILE="$HOME/.config/eyedatahub/private.env"
```

```powershell
$env:EYEDATAHUB_ENV_FILE = "$HOME\.config\eyedatahub\private.env"
```

Manual, challenge-gated, author-contact, and data-use-agreement routes print
official instructions and return a structured blocked status instead of
attempting unauthorized transfer. EyeDataHub never accepts terms for a user.

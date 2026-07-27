"""
Enrich open_licence_catalogue.json with scanner, geography, and demographic metadata.

This script merges:
  1. The registry-generated catalogue (from open_catalogue.py)
  2. The curated metadata overlay (METADATA_OVERLAY below)

Run:
    python hub/open_catalogue.py          # regenerate base catalogue
    python hub/enrich_metadata.py         # merge + write metadata.json / metadata.csv
"""
from __future__ import annotations

import json
import pandas as pd
from pathlib import Path


# ---------------------------------------------------------------------------
# Curated metadata overlay
# Each key is the dataset 'name' from the registry.
# Sources: dataset papers, data descriptor articles, challenge websites.
# ---------------------------------------------------------------------------

METADATA_OVERLAY: dict[str, dict] = {

    # ── Fundus vessels ──────────────────────────────────────────────────────
    "chase_db1": {
        "geography": "United Kingdom (Kingston, England)",
        "scanner_device": "Nikon D3, 30° FOV (handheld fundus camera); NM-200D",
        "demographics": {
            "age_range": "9–11 years (schoolchildren)",
            "sex_distribution": "mixed",
            "ethnicity": "multi-ethnic UK schoolchildren",
            "num_patients": 28,
        },
    },
    "hrf": {
        "geography": "Germany (Erlangen, FAU)",
        "scanner_device": "Canon CR-1 Mark II (45° FOV, 3504×2336 px)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "not reported",
            "num_patients": 45,
        },
    },
    "fives": {
        "geography": "China (Beijing Tongren Hospital)",
        "scanner_device": "Canon CX-1, 30° digital non-mydriatic fundus camera",
        "demographics": {
            "age_range": "18–90 years",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": 800,
        },
    },

    # ── Glaucoma ────────────────────────────────────────────────────────────
    "airogs": {
        "geography": "Netherlands (Rotterdam Eye Hospital + 5 regional centres)",
        "scanner_device": "Various non-mydriatic fundus cameras (mixed fleet)",
        "demographics": {
            "age_range": "18+ years (screening population)",
            "sex_distribution": "~50% female",
            "ethnicity": "Dutch (multi-ethnic screening)",
            "num_patients": 88 + 14000,  # approx from paper
        },
    },
    "acrima": {
        "geography": "Spain (Madrid — Hospital Clínico San Carlos; processed at Universitat Politècnica de València)",
        "scanner_device": "Topcon TRC-NW8 (45° non-mydriatic)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Spanish",
            "num_patients": 705,
        },
    },
    "g1020": {
        "geography": "Pakistan (Islamabad)",
        "scanner_device": "Nikon and Topcon fundus cameras (details in paper)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "South Asian (Pakistani)",
            "num_patients": 1020,
        },
    },
    "harvard_glaucoma": {
        "geography": "USA (Harvard/Massachusetts Eye and Ear)",
        "scanner_device": "Various (Zeiss Clarus, Optos, Topcon — mixed fleet)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "not reported",
            "num_patients": 1000,
        },
    },
    "origa": {
        "geography": "Singapore (National University of Singapore Eye Centre)",
        "scanner_device": "Canon CR-1 Mark II (45° non-mydriatic)",
        "demographics": {
            "age_range": "40+ years (population study)",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese Singaporean",
            "num_patients": 650,
        },
    },
    "papila": {
        "geography": "Spain (Alcorcón, Murcia — two ophthalmology departments)",
        "scanner_device": "Topcon TRC-NW8 (45° non-mydriatic)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Spanish",
            "num_patients": 488,
        },
    },
    "rimone_dl": {
        "geography": "Spain (Canary Islands, Huelva, Alicante — three hospitals)",
        "scanner_device": "Nikon D3, Canon EOS (various)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Spanish",
            "num_patients": 485,
        },
    },

    # ── DR grading / lesion ──────────────────────────────────────────────────
    "idrid": {
        "geography": "India (Nanded, Maharashtra — Shri Ganesha Vinayak Eye Institute)",
        "scanner_device": "Kowa VX-10α (50° digital non-mydriatic, 4752×3168 px)",
        "demographics": {
            "age_range": "not reported (diabetic patients)",
            "sex_distribution": "not reported",
            "ethnicity": "South Asian (Indian)",
            "num_patients": 516,
        },
    },
    "ddr": {
        "geography": "China (multi-center, Tianjin/Jinan hospitals)",
        "scanner_device": "Canon CR-2 and Topcon NW400 (non-mydriatic)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": 12522,
        },
    },
    "maples_dr": {
        "geography": "Canada (Montréal — Hôpital Maisonneuve-Rosemont + Université de Montréal)",
        "scanner_device": "Topcon NW400 and Topcon TRC-NW8 (45° non-mydriatic)",
        "demographics": {
            "age_range": "18+ years (diabetic patients)",
            "sex_distribution": "not reported",
            "ethnicity": "mixed (Montréal population)",
            "num_patients": 198,
        },
    },
    "deepdrid": {
        "geography": "China (multi-centre — Shenzhen, Guangzhou, Chengdu)",
        "scanner_device": "Zeiss Visucam 500, Topcon TRC-50DX (dual-view 45°); Optos 200Tx (UWF subset)",
        "demographics": {
            "age_range": "20–90 years (diabetic patients)",
            "sex_distribution": "~50% female",
            "ethnicity": "Chinese",
            "num_patients": 1600,
        },
    },
    "drac22": {
        "geography": "China (multi-center)",
        "scanner_device": "Optovue AngioVue (OCTA, 3×3 mm and 6×6 mm scans)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": 174,
        },
    },
    "mmrdr": {
        "geography": "China (multi-modal, centres not detailed in descriptor)",
        "scanner_device": "Fundus: various; OCT: Zeiss Cirrus; UWF: Optos (mixed)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": None,
        },
    },

    # ── Fundus multi-disease / misc ──────────────────────────────────────────
    "jsiec": {
        "geography": "China (Shantou, Guangdong — Joint Shantou International Eye Center, Shantou University)",
        "scanner_device": "Canon CX-1 (45° non-mydriatic)",
        "demographics": {
            "age_range": "6–90 years",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": 10000,
        },
    },
    "rfmid": {
        "geography": "India (Pune — Nanded and Icare Eye Institute)",
        "scanner_device": "Topcon TRC-50DX (45°) and Kowa VX-10α",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "South Asian (Indian)",
            "num_patients": 3200,
        },
    },
    "odir2019": {
        "geography": "China (multi-centre — ODIR Challenge 2019)",
        "scanner_device": "Various (fundus cameras not specified uniformly)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": 8000,
        },
    },
    "toxofundus": {
        "geography": "Brazil (São Paulo — Federal University of São Paulo / UNIFESP)",
        "scanner_device": "Topcon TRC-50DX and Zeiss Visucam Pro NM",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Brazilian",
            "num_patients": 412,
        },
    },
    "farfum_rop": {
        "geography": "Iran (Tehran — multi-centre NICU)",
        "scanner_device": "RetCam (wide-field neonatal fundus camera)",
        "demographics": {
            "age_range": "Neonatal/premature infants (gestational 24–36 weeks)",
            "sex_distribution": "not reported",
            "ethnicity": "Iranian",
            "num_patients": 1533,
        },
    },

    # ── OCT classification ────────────────────────────────────────────────────
    "kermany_oct": {
        "geography": "USA (UC San Diego + China — Shenzhen Aier Eye Hospital)",
        "scanner_device": "Heidelberg Spectralis OCT",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "mixed (US + Chinese)",
            "num_patients": None,
        },
    },
    "octid": {
        "geography": "Canada (Edmonton, Alberta — University of Alberta)",
        "scanner_device": "Heidelberg Spectralis OCT (512×496 px B-scans)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "not reported",
            "num_patients": 206,
        },
    },
    "oct_cirrus": {
        "geography": "USA (Durham, NC — Duke University Eye Center)",
        "scanner_device": "Zeiss Cirrus HD-OCT (1000×100×1024 volumes)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "not reported",
            "num_patients": None,
        },
    },
    "octdl": {
        "geography": "Germany (multiple ophthalmology clinics)",
        "scanner_device": "Heidelberg Spectralis OCT",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "German",
            "num_patients": 2000,
        },
    },
    "nehut": {
        "geography": "USA (San Antonio, TX — UT Health San Antonio)",
        "scanner_device": "Zeiss Cirrus HD-OCT",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "not reported",
            "num_patients": None,
        },
    },
    "olives": {
        "geography": "USA (Atlanta, GA — Emory Eye Center / Georgia Tech)",
        "scanner_device": "Heidelberg Spectralis OCT",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "not reported",
            "num_patients": 96,
        },
    },

    # ── OCT segmentation ──────────────────────────────────────────────────────
    "oimhs": {
        "geography": "China (Beijing — multiple hospitals)",
        "scanner_device": "Zeiss Cirrus HD-OCT 5000 and Heidelberg Spectralis",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": None,
        },
    },
    "octave": {
        "geography": "Not specified (multi-center, details in paper)",
        "scanner_device": "Zeiss Cirrus HD-OCT (1024×200×1024 volumes)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "not reported",
            "num_patients": None,
        },
    },
    "goals": {
        "geography": "China (Hangzhou — Zhejiang University Second Affiliated Hospital)",
        "scanner_device": "Optovue Avanti RTVue XR OCTA (6×6 mm)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": 300,
        },
    },
    "tian_oct": {
        "geography": "USA (Iowa City, IA — University of Iowa)",
        "scanner_device": "Zeiss Cirrus HD-OCT (200 B-scans per volume)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "not reported",
            "num_patients": 10,
        },
    },

    # ── UWF fundus ────────────────────────────────────────────────────────────
    "oculoscope": {
        "geography": "United Kingdom (London — Moorfields Eye Hospital NHS)",
        "scanner_device": "Various (Optos, Zeiss Clarus, Canon CR-2 — mixed fleet)",
        "demographics": {
            "age_range": "18+ years",
            "sex_distribution": "~50% female",
            "ethnicity": "multi-ethnic (South Asian, Black, White, other)",
            "num_patients": 16530,
        },
    },
    "uwf_tumor": {
        "geography": "China (Beijing — Peking Union Medical College Hospital)",
        "scanner_device": "Optos P200Tx Panoramic Ophthalmoscope (200° UWF)",
        "demographics": {
            "age_range": "not reported",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": 2031,
        },
    },

    # ── Visual field ─────────────────────────────────────────────────────────
    "uwhvf": {
        "geography": "USA (Seattle, WA — University of Washington)",
        "scanner_device": "Humphrey Field Analyzer (HFA) 24-2 SITA Standard/Fast",
        "demographics": {
            "age_range": "18–90+ years",
            "sex_distribution": "not reported",
            "ethnicity": "not reported",
            "num_patients": None,
        },
    },

    # ── Multimodal ────────────────────────────────────────────────────────────
    "grape": {
        "geography": "China (Guangzhou — Zhongshan Ophthalmic Center, Sun Yat-sen University)",
        "scanner_device": "Heidelberg Spectralis OCT + Optos UWF + Zeiss HFA (multi-modal)",
        "demographics": {
            "age_range": "40+ years (glaucoma follow-up)",
            "sex_distribution": "not reported",
            "ethnicity": "Chinese",
            "num_patients": 1115,
        },
    },
}


# ---------------------------------------------------------------------------
# Merge and write
# ---------------------------------------------------------------------------

def enrich(
    catalogue_path: Path | None = None,
    out_json: Path | None = None,
    out_csv: Path | None = None,
) -> list[dict]:

    hub_dir = Path(__file__).parent
    if catalogue_path is None:
        catalogue_path = hub_dir / "open_licence_catalogue.json"

    if not catalogue_path.exists():
        # Generate it on the fly
        from hub.open_catalogue import build_catalogue
        records = build_catalogue(catalogue_path)
    else:
        records = json.loads(catalogue_path.read_text(encoding="utf-8"))

    enriched = []
    for rec in records:
        name = rec["name"]
        overlay = METADATA_OVERLAY.get(name, {})
        merged = {**rec}
        if "geography" in overlay:
            merged["geography"] = overlay["geography"]
        if "scanner_device" in overlay:
            merged["scanner_device"] = overlay["scanner_device"]
        if "demographics" in overlay:
            merged["demographics"] = overlay["demographics"]
        enriched.append(merged)

    if out_json is None:
        out_json = hub_dir / "metadata.json"
    if out_csv is None:
        out_csv = hub_dir / "metadata.csv"

    out_json.write_text(
        json.dumps(enriched, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Wrote {len(enriched)} entries -> {out_json}")

    # Flatten for CSV
    rows = []
    for e in enriched:
        demo = e.get("demographics") or {}
        rows.append({
            "name":              e["name"],
            "full_name":         e["full_name"],
            "modality":          e["modality"],
            "tasks":             "|".join(e.get("tasks", [])),
            "num_samples":       e.get("num_samples"),
            "size_gb":           e.get("size_gb"),
            "license":           e.get("license"),
            "license_family":    e.get("license_family"),
            "download_type":     e.get("download_type"),
            "download_url":      e.get("download_url"),
            "geography":         e.get("geography"),
            "scanner_device":    e.get("scanner_device"),
            "age_range":         demo.get("age_range"),
            "sex_distribution":  demo.get("sex_distribution"),
            "ethnicity":         demo.get("ethnicity"),
            "num_patients":      demo.get("num_patients"),
        })

    df = pd.DataFrame(rows)
    df.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"Wrote CSV -> {out_csv}")
    return enriched


if __name__ == "__main__":
    enrich()

# Dataset publication dates

`DatasetInfo.publication_date` records the initial public release of the
represented dataset. It is separate from the associated article date, the
latest version date, the catalog cutoff, and the date of metadata review.
"Public release" includes resources that require an account or access approval.

## Fields

Every Python record and JSON/CSV export exposes these optional fields:

| Field | Value when known |
|---|---|
| `publication_date` | ISO `YYYY-MM-DD`, `YYYY-MM`, or `YYYY` |
| `publication_date_precision` | `day`, `month`, or `year`, matching the date |
| `publication_date_source_url` | Public official page or API URL supporting the date |
| `publication_date_source_field` | Exact upstream field or named release announcement |
| `publication_date_scope` | `initial_public_release` |
| `publication_date_reviewed_on` | Date the evidence was checked, `YYYY-MM-DD` |
| `publication_date_notes` | Optional explanation of versions, mirrors, or ambiguity |

Unknown dates and their evidence fields are `None` in Python, `null` in JSON,
and empty cells in CSV. A year-only date stays year-only; do not add January 1.
The website and CLI display the date as supplied and link its evidence.

## Find and review a date

1. Inspect the official source's History, Posted, First online, or Publication
   date. On a versioned repository, inspect the earliest public version.
2. Check whether that deposit is a later archive or mirror of an older release.
   Use the original resource's release evidence where available. If the evidence
   establishes only a later upload date, leave the initial date unknown.
3. For a separately indexed derivative or annotation layer, use that product's
   own release date, not its parent dataset's date. A collection's date cannot
   be inferred from the oldest component.
4. Record the source URL, field name, precision, and review date. Never substitute
   article publication, private repository creation, modification, or data
   collection dates. Conflicting dates need an explanatory note and resolution
   before they are added.

Use permanent public evidence links, never credentials, signed download URLs,
or local paths. A source's planned release date needs confirmation that the
release occurred before it is used as an actual publication date.

Sourced entries are in
[`eyedatahub/core/publication_dates.json`](../eyedatahub/core/publication_dates.json),
keyed by existing record ID. This file ships inside the Python package, so
metadata lookup works offline. It fills the first-class `DatasetInfo` fields
only when the dataset class supplies none of them. A class may instead set
the fields explicitly; explicit values take precedence and must include evidence.

For example, a reviewed entry can use this shape (values below are placeholders,
not evidence for a real record):

```json
{
  "example_record": {
    "publication_date": "2024-06",
    "publication_date_precision": "month",
    "publication_date_source_url": "https://example.org/dataset/history",
    "publication_date_source_field": "First online",
    "publication_date_scope": "initial_public_release",
    "publication_date_reviewed_on": "2026-09-11",
    "publication_date_notes": "Source reports the month, not the day."
  }
}
```

Source checks and reasons for withholding dates are in
`hub/audit/publication_dates_*.json`. The initial and remaining review batches
together cover every catalog record. Supporting second-pass files document
additional checks; they do not represent additional catalog records.
These files are review records, not runtime inputs. The packaged metadata is
the source of truth for the interfaces and exports. Dates remain unknown when
the checked sources do not establish the initial public release.

## Search and sort

```bash
eyehub search --published-from 2020 --published-through 2024 --sort publication-date
eyehub search --publication-date-status known --sort publication-date-desc --json
eyehub search --publication-date-status unknown --json
eyehub show brset --json
```

`published-from` and `published-through` are inclusive. The CLI and Python
accept year, month, or day bounds. Partial dates match when their possible
interval overlaps the requested range: a `2020` record can match a June 2020
query, but still displays `2020`. Both chronological sorts put unknown dates
last and use the earliest possible date for ordering; ties use the record ID.
Unknown dates do not match a date range. The default remains alphabetical.

```python
from eyedatahub.catalog import search_datasets
from eyedatahub.datasets.registry import REGISTRY

records = search_datasets(
    REGISTRY.list_datasets(),
    published_from="2020",
    published_through="2024",
    publication_date_status="known",
    sort="publication-date-desc",
)
print(records[0].info.publication_date)
```

The website offers inclusive year bounds, known/unknown filtering, and oldest
or newest sorting. Other search filters can be combined with date filters.
Date lookup, filtering, and sorting never initiate dataset downloads.

## Contributing the remaining dates

Choose existing records with unknown dates, document the official evidence,
and add entries to the packaged JSON. Do not change catalog membership or
count earlier versions again. Leave uncertain dates unknown and record why.

Regenerate exports and dataset documentation, then run:

```bash
python -m hub.export_catalog
python -m hub.docs.generate_dataset_pages --out website/docs
python -m hub.docs.generate_llms_full
python -m pytest -q
cd website
npm test
npm run build
```

Tests check calendar validity, precision and evidence, offline metadata exposure,
date filtering, sorting, and agreement between exported and website values.
A coverage test requires a sourced date or a documented source check for every
catalog record, with no duplicate assignments across the review batches.

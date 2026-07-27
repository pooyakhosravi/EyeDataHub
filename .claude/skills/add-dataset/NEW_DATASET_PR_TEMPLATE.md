# New Dataset PR Template

Use this template when an agent or contributor opens a PR adding a dataset to
EyeDataHub. Keep unknowns explicit. Do not delete license or provenance
sections.

## Summary

- Dataset slug:
- Full dataset name:
- One-sentence purpose:
- Closes issue:

## Source And Provenance

| Field | Value |
|---|---|
| Official source URL |  |
| Dataset DOI / record URL |  |
| Publication / citation |  |
| Source host |  |
| Original dataset, mirror, derivative, or composite? |  |
| Known upstream datasets or overlaps |  |
| Access route | open / account / challenge / DUA / manual / other |

## Registry Metadata

| Field | Value |
|---|---|
| `name` |  |
| `full_name` |  |
| `description` |  |
| `modality` |  |
| `tasks` |  |
| `num_samples` |  |
| `splits` |  |
| `classes` / `num_classes` |  |
| `image_size` |  |
| `download_type` |  |
| `download_url` |  |
| `size_gb` |  |
| `tags` |  |
| `notes` |  |

## License Verification

- Exact license text from source:
- License-family classification:
- Where the license was found:
- Mirror/source license conflicts:
- Commercial-use interpretation:
- Caveats for reviewers:

## Implementation

- Dataset module edited:
- New class name:
- Registry import added in `eyedatahub/datasets/registry.py`:
- Registry instantiation section:
- Loader status:
  - [ ] Full `download()` implementation
  - [ ] Full `load()` parser
  - [ ] Download-only implementation
  - [ ] Manual/gated instructions
  - [ ] Metadata-only stub with explicit notes
- New credentials or `.env` variables required:
- Generated docs/catalog files updated:

## Validation

Paste commands and relevant output.

```bash
python -m pytest -q
python -m eyedatahub.cli show <slug> --json
python -m eyedatahub.cli list datasets --license-type <license_family>
python -m hub.docs.generate_dataset_pages --out website/docs
python -m hub.docs.generate_llms_full
```

## Reviewer Notes

- Open questions:
- Known limitations:
- Follow-up work:
- Human review needed for:

## Checklist

- [ ] I checked for duplicate slugs and duplicate datasets.
- [ ] I used the official source URL, not only a mirror.
- [ ] I copied the exact license text from the source.
- [ ] I documented access restrictions and manual steps.
- [ ] I added the class to an appropriate `eyedatahub/datasets/*.py` module.
- [ ] I registered the dataset in `eyedatahub/datasets/registry.py`.
- [ ] I updated `tests/test_smoke.py` if the dataset count changed.
- [ ] I regenerated docs/catalog snapshots when applicable.
- [ ] I did not bypass upstream access controls.
- [ ] I disclosed AI assistance when applicable.

<!-- Thanks for contributing. Fill in the sections that apply. -->

## Summary

<!-- One or two sentences describing the change. -->

Closes #<issue>

## New Dataset Checklist

If this PR adds a dataset, complete this checklist. For agent-assisted dataset
PRs, paste the filled template from
`.claude/skills/add-dataset/NEW_DATASET_PR_TEMPLATE.md` below this section or
link to it in the PR description.

- [ ] I checked existing issues and `eyehub search --json` for duplicate slugs, mirrors, derivatives, versions, and overlapping cohorts.
- [ ] I recorded the canonical name, official source, preferred route, and field-level evidence URLs.
- [ ] I copied the exact source-stated terms and recorded whether they apply to dataset files, metadata, code, a publication, challenge participation, mixed components, or an unknown scope.
- [ ] I recorded one access-friction category and the registration, authentication, API-token, click-through, manual-approval, data-use-agreement, author-contact, payment, and geographic/institutional restriction fields using true, false, or unknown.
- [ ] I separated dataset DOI/accession/repository identifier, associated-publication DOI, software DOI, and challenge identifier.
- [ ] I recorded one primary navigation category, every contained modality, tasks, source-reported count and unit, and the corresponding evidence.
- [ ] I documented typed mirror, derivation, version, supplement, supersession, and known cohort-overlap relationships.
- [ ] I recorded the verification date, level, result, loader or guided instructions, test scope, and known limitations.
- [ ] I added or updated a `DatasetInfo` class in the appropriate `eyedatahub/datasets/*.py` module.
- [ ] I registered the dataset in `eyedatahub/datasets/registry.py`.
- [ ] I updated `tests/test_smoke.py::EXPECTED_DATASET_COUNT` if the dataset count changed.
- [ ] I regenerated dataset docs/catalog snapshots when applicable.
- [ ] I added or updated tests, including preflight and failure behavior for a loader change.
- [ ] I did not bypass upstream access controls.
- [ ] I did not infer dataset-file terms from a website, publication, or code license.

## Validation

Paste relevant command output or explain why a command does not apply.

```bash
python -m pytest -q
python -m eyedatahub.cli show <slug> --json
python -m eyedatahub.cli search --modality <modality> --json
python -m eyedatahub.cli preflight <slug> --json
```

## Reviewer Notes

<!-- Known limitations, license caveats, manual review needed, or follow-up work. -->

## AI-Assisted Contribution

- [ ] No AI assistance used
- [ ] AI-assisted; model/tool: __________________

AI assistance is welcome when disclosed. Maintainers remain responsible for
every inclusion, source, terms, access, code, and interpretation decision; no
record is accepted solely from an AI system's output.

---
name: license-filter
description: Screen EyeDataHub records by source-stated terms and access conditions without making a legal permission determination.
---

# Skill: source-term and access screening

Use EyeDataHub metadata to narrow records for human review. Never answer that a
dataset is lawful, safe, approved, or commercially usable. EyeDataHub records
source documentation and operational conditions; it does not determine
permission.

## Required inputs

1. Intended activity and whether it includes redistribution, modification,
   model-weight release, commercial use, sensitive-data handling, or clinical
   use.
2. Modality and task filters.
3. Tolerance for registration, authentication, click-through, manual approval,
   author contact, payment, and unknown terms.
4. Whether counsel, an institutional data office, or an ethics body must review
   the source.

## Workflow

1. Search independently by modality/task, source-term category, access
   friction, availability, and acquisition support.

   ```bash
   eyehub search --modality <modality> --task <task> --json
   eyehub search --source-terms <category> --json
   eyehub search --access <access_friction> --json
   ```

2. Inspect each candidate rather than aggregating terms into one verdict.

   ```bash
   eyehub show <record> --json
   eyehub preflight <record> --json
   ```

3. Report the raw source-stated terms, evidence URL, apparent scope, normalized
   category, access requirements, route-check date, loader-test scope, and all
   unknowns.

4. If terms may apply to code, metadata, a publication, or challenge
   participation instead of dataset files, say so. Do not inherit them.

5. Recommend review of the current official source and the appropriate human or
   institutional authority. Do not infer a legal result from CC, MIT, Apache,
   research-only, unknown, or any normalized group.

## Output

Use columns such as `record`, `raw source terms`, `terms scope`, `evidence`,
`access friction`, `automation/test scope`, `unknowns`, and `review needed`.
Do not use an “OK for use?” column.

Always state: “This is descriptive source and access metadata, not legal
advice or a permission determination. Review the current official source and
obtain any required institutional or legal approval.”

## Refuse

- Converting `standard-no-nc` or a legacy `commercial-ok` alias into permission.
- Treating an unknown as unrestricted.
- Treating a self-service route as reuse authorization.
- Treating a code, paper, website, mirror, or platform licence as the
  dataset-file licence.
- Bypassing authentication, click-through, payment, author contact, manual
  approval, data-use agreements, geography, or institutional controls.

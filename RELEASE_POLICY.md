# Release policy

EyeDataHub uses immutable versioned releases. The software version, catalog
snapshot, validation logs, generated figures/tables, Git tag, and archived DOI
must identify the same state. Existing tags and DOI deposits are never moved or
silently replaced; corrections and additions enter a later release and are
recorded in `CHANGELOG.md`.

Before a release, maintainers:

1. review source evidence, source-term scope, access requirements, typed
   identifiers, relationships, and unknown values;
2. run the unit/command tests and a clean installation;
3. date-stamp per-record source and route checks and acquisition-test evidence;
4. regenerate the catalog snapshots, schema, completeness results, figures,
   tables, manifest, and checksums;
5. confirm the CLI examples and JSON failure outputs;
6. create an annotated Git tag and archive that exact tag;
7. verify the public code release and DOI archive without author credentials.

Scheduled URL or platform checks may update the living project, but do not
change a frozen release. Failed routes are retained with their dated status
rather than deleted. The archive contains metadata and software evidence only;
it never redistributes the indexed third-party datasets.

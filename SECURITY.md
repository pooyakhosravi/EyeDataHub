# Security and credential handling

Report a suspected vulnerability privately through GitHub's security advisory
workflow for this repository. Do not include credentials, tokens, protected
URLs, or third-party data in a public issue.

EyeDataHub reads platform credentials only through the platform's supported
client or documented environment/configuration mechanism. Credentials must be
provided by the user; the software does not embed them in catalog records,
command output, validation logs, or provenance manifests. Search, show, cite,
preflight, JSON, Python, and MCP operations are read-only. Transfer starts only
after an explicit non-dry-run `eyehub download` command.

The tool never accepts click-through terms, licenses, or data-use agreements on
a user's behalf. Controlled and manual routes are blocked from automation and
return official instructions. Users should inspect the source host, applicable
terms, destination path, available disk space, and any institutional security
requirements before transferring data.

Validation artifacts intentionally contain no secrets and no indexed
third-party dataset files. Locally downloaded data remain outside the project
repository and under the source host's controls and terms.

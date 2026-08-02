import React from 'react';

import useBaseUrl from '@docusaurus/useBaseUrl';
import catalogPayload from '@site/static/datasets.json';

const STANDARD_NO_NC = new Set(['cc0', 'cc-by', 'cc-by-sa', 'mit', 'apache', 'odc-by']);
const QUICK_START_COMMANDS = [
  'pip install "eyedatahub==0.5.0"',
  'eyehub search --access anonymous_direct --json',
  'eyehub show airogs --json',
  'eyehub download airogs --dry-run --json',
];

function formatNumber(value) {
  if (value === null || value === undefined) return '-';
  return Number(value).toLocaleString();
}

function formatPrimaryQuantity(row) {
  if (row.samples === null || row.samples === undefined) return 'Not reported';
  const unit = row.item_count_unit && row.item_count_unit !== 'unknown'
    ? row.item_count_unit.replace(/_/g, ' ')
    : 'unit not resolved';
  return `${formatNumber(row.samples)} ${unit}`;
}

function titleCase(value) {
  return String(value || '')
    .replace(/_/g, ' ')
    .replace(/\b\w/g, (m) => m.toUpperCase());
}

function reuseBucket(row) {
  if (STANDARD_NO_NC.has(row.license_family)) return 'standard-no-nc';
  if (String(row.license_family).includes('nc')) return 'non-commercial';
  if (row.license_family === 'research-only') return 'research-only';
  return 'unknown';
}

function CopyIcon() {
  return (
    <svg className="edh-copy-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <rect x="9" y="9" width="11" height="11" rx="2" />
      <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
    </svg>
  );
}

function CopyButton({ copied, disabled = false, label, onClick, tooltip = 'Copy' }) {
  return (
    <button
      type="button"
      className={`edh-icon-copy${copied ? ' is-copied' : ''}`}
      disabled={disabled}
      onClick={onClick}
      aria-label={copied ? `${label}. Copied to clipboard.` : label}
      data-tooltip={copied ? 'Copied' : tooltip}
      title={label}
    >
      <CopyIcon />
      <span className="edh-sr-only">{label}</span>
    </button>
  );
}

export default function DatasetDashboard() {
  const baseUrl = useBaseUrl('/');
  const withBase = React.useCallback((path) => `${baseUrl.replace(/\/$/, '')}${path}`, [baseUrl]);

  const payload = catalogPayload;
  const [query, setQuery] = React.useState('');
  const [modality, setModality] = React.useState('all');
  const [license, setLicense] = React.useState('all');
  const [backend, setBackend] = React.useState('all');
  const [reuse, setReuse] = React.useState('all');
  const [relationshipType, setRelationshipType] = React.useState('all');
  const [sort, setSort] = React.useState('name');
  const [copiedToken, setCopiedToken] = React.useState(null);
  const [selectedNames, setSelectedNames] = React.useState([]);

  const copyText = React.useCallback((text, token, promptLabel = 'Copy text') => {
    const done = () => {
      setCopiedToken(token);
      window.setTimeout(() => setCopiedToken((current) => (current === token ? null : current)), 2500);
    };

    if (navigator.clipboard?.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(() => {
        window.prompt(promptLabel, text);
      });
      return;
    }

    window.prompt(promptLabel, text);
  }, []);

  const toggleDataset = React.useCallback((name, checked) => {
    setSelectedNames((current) => {
      if (checked) return current.includes(name) ? current : [...current, name];
      return current.filter((item) => item !== name);
    });
  }, []);

  const rows = payload?.datasets || [];
  const facets = payload?.facets || {};
  const summary = payload?.summary || {};
  const rowsByName = React.useMemo(() => new Map(rows.map((row) => [row.name, row])), [rows]);

  const filtered = React.useMemo(() => {
    const q = query.trim().toLowerCase();
    const result = rows.filter((row) => {
      const haystack = [
        row.name,
        row.full_name,
        row.description,
        row.primary_category,
        ...(row.modalities || []),
        row.license_family,
        row.download_type,
        row.loader_status,
        ...(row.tasks || []),
        ...((row.relationships || []).flatMap((relationship) => [
          relationship.relationship_type,
          relationship.target_name,
          relationship.target_full_name,
        ])),
      ].join(' ').toLowerCase();
      return (
        (!q || haystack.includes(q)) &&
        (modality === 'all' || (row.modalities || []).includes(modality)) &&
        (license === 'all' || row.license_family === license) &&
        (backend === 'all' || row.download_type === backend) &&
        (reuse === 'all' || reuseBucket(row) === reuse) &&
        (relationshipType === 'all' || (row.relationships || []).some(
          (relationship) => relationship.relationship_type === relationshipType,
        ))
      );
    });

    result.sort((a, b) => {
      if (sort === 'name') return a.name.localeCompare(b.name);
      if (sort === 'modality') {
        return (a.modalities || []).join(',').localeCompare((b.modalities || []).join(','))
          || a.name.localeCompare(b.name);
      }
      if (sort === 'license') return a.license_family.localeCompare(b.license_family) || a.name.localeCompare(b.name);
      return (b.samples || 0) - (a.samples || 0) || a.name.localeCompare(b.name);
    });
    return result;
  }, [rows, query, modality, license, backend, reuse, relationshipType, sort]);

  const visibleRows = React.useMemo(() => filtered.slice(0, 120), [filtered]);
  const selectedRows = React.useMemo(
    () => selectedNames.map((name) => rowsByName.get(name)).filter(Boolean),
    [rowsByName, selectedNames],
  );
  const selectedDownloadCommand = selectedNames.length
    ? `eyehub download --datasets ${selectedNames.join(',')}`
    : 'eyehub download --datasets';

  return (
    <div className="edh-dashboard">
      <section className="edh-hero">
        <div>
          <p className="edh-kicker">Source-aware ophthalmic data access</p>
          <h1>
            Find ophthalmology datasets, inspect access requirements, and preflight supported transfers.
          </h1>
          <p>
            EyeDataHub combines a date-stamped, manually source-checked snapshot of{' '}
            {formatNumber(summary.datasets)} resources across{' '}
            {formatNumber(summary.primary_categories)} primary categories with a
            command-line access layer. It records source
            terms, access friction, automation support, citations, and dated
            verification without hosting third-party datasets.
          </p>
          <div className="edh-actions">
            <a className="button button--primary" href={withBase('/guides/install')}>
              Install
            </a>
            <a className="button button--secondary" href={withBase('/datasets')}>
              Browse datasets
            </a>
            <a className="button button--secondary" href={withBase('/guides/agentic')}>
              Plan with an LLM agent
            </a>
            <a className="button button--secondary" href="https://doi.org/10.5281/zenodo.21614657">
              Cite release
            </a>
          </div>
        </div>
        <div className="edh-code-panel" aria-label="Quick start">
          <div className="edh-code-title">Quick start</div>
          <div className="edh-command-list">
            {QUICK_START_COMMANDS.map((command, index) => (
              <div className="edh-command-row" key={command}>
                <code title={command}>{command}</code>
                <CopyButton
                  copied={copiedToken === `quick-${index}`}
                  label={`Copy quick-start command: ${command}`}
                  tooltip="Copy command"
                  onClick={() => copyText(command, `quick-${index}`, 'Copy command')}
                />
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="edh-metrics" aria-label="Catalog summary">
        <div><strong>{formatNumber(summary.datasets)}</strong><span>catalog records</span></div>
        <div><strong>{formatNumber(summary.anonymous_routes)}</strong><span>anonymous routes</span></div>
        <div><strong>{formatNumber(summary.authenticated_or_clickthrough_routes)}</strong><span>signed-in or click-through routes</span></div>
        <div><strong>{formatNumber(summary.controlled_routes)}</strong><span>controlled or manual routes</span></div>
        <div><strong>{formatNumber(summary.author_contact_routes)}</strong><span>author-contact routes</span></div>
        <div><strong>{formatNumber(summary.transfer_tested_routes)}</strong><span>complete or partial transfer tests</span></div>
        <div><strong>{formatNumber(summary.documented_relationship_edges)}</strong><span>source-backed relationships</span></div>
      </section>

      <section className="edh-workflows">
        <div>
          <h2>Explore From The CLI</h2>
          <p>Search, inspect, filter by license, copy citations, and follow recorded access routes.</p>
          <a href={withBase('/guides/cli')}>CLI guide</a>
        </div>
        <div>
          <h2>Use One Metadata Layer</h2>
          <p>Read the same versioned metadata in notebooks, tests, training scripts, and cohort manifests.</p>
          <a href={withBase('/guides/python')}>Python guide</a>
        </div>
        <div>
          <h2>Use Optional Machine Interfaces</h2>
          <p>Read the same catalog through deterministic JSON, JSON-LD, Python, or the optional read-only MCP interface.</p>
          <a href={withBase('/guides/agentic')}>Machine-interface guide</a>
        </div>
      </section>

      <section className="edh-agent-story" aria-labelledby="agent-story-title">
        <div className="edh-agent-story-copy">
          <p className="edh-kicker">Explicit acquisition by design</p>
          <h2 id="agent-story-title">Inspect source terms and access requirements before transfer.</h2>
          <p>
            Search and inspection are read-only. A separate preflight reports
            the represented route, source-stated terms, evidence, credentials,
            manual requirements, and loader status. Transfer begins only after
            an explicit user-issued acquisition command.
          </p>
          <a href={withBase('/guides/cli')}>See the command-line workflow</a>
        </div>
        <ol className="edh-agent-flow">
          <li><span>1</span><div><strong>Search</strong><p>Filter the date-stamped catalog by modality, task, access, terms, or automation status.</p></div></li>
          <li><span>2</span><div><strong>Inspect</strong><p>Review source evidence, identifiers, access state, and citation guidance.</p></div></li>
          <li><span>3</span><div><strong>Preflight</strong><p>Check credentials, recorded conditions, disk space, and loader behavior without transfer.</p></div></li>
          <li><span>4</span><div><strong>Acquire</strong><p>Issue an explicit command when the official route is supported.</p></div></li>
          <li><span>5</span><div><strong>Record</strong><p>Retain the generated provenance manifest with local files and citations.</p></div></li>
        </ol>
        <p className="edh-agent-boundary">
          EyeDataHub never accepts terms for a user and does not determine legal
          permission, scientific suitability, clinical validity, or ethical acceptability.
        </p>
      </section>

      <section className="edh-explorer" id="dataset-explorer">
        <div className="edh-section-head">
          <div>
            <h2>Dataset Explorer</h2>
            <p>{formatNumber(filtered.length)} of {formatNumber(rows.length)} datasets match the current filters.</p>
          </div>
          <a href={withBase('/url-audit')}>Latest URL audit</a>
        </div>

        <div className="edh-filters">
          <label>
            <span>Search</span>
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="fundus, OCT, glaucoma, VQA..."
            />
          </label>
          <label>
            <span>Modality</span>
            <select value={modality} onChange={(e) => setModality(e.target.value)}>
              <option value="all">All modalities</option>
              {Object.keys(facets.modality || {}).map((key) => (
                <option key={key} value={key}>{titleCase(key)} ({facets.modality[key]})</option>
              ))}
            </select>
          </label>
          <label>
            <span>License</span>
            <select value={license} onChange={(e) => setLicense(e.target.value)}>
              <option value="all">All license families</option>
              {Object.keys(facets.license_family || {}).map((key) => (
                <option key={key} value={key}>{key} ({facets.license_family[key]})</option>
              ))}
            </select>
          </label>
          <label>
            <span>Access</span>
            <select value={backend} onChange={(e) => setBackend(e.target.value)}>
              <option value="all">All access backends</option>
              {Object.keys(facets.download_type || {}).map((key) => (
                <option key={key} value={key}>{titleCase(key)} ({facets.download_type[key]})</option>
              ))}
            </select>
          </label>
          <label>
            <span>Reuse</span>
            <select value={reuse} onChange={(e) => setReuse(e.target.value)}>
              <option value="all">Any reuse category</option>
              <option value="standard-no-nc">No explicit noncommercial clause</option>
              <option value="non-commercial">Noncommercial</option>
              <option value="research-only">Research only</option>
              <option value="unknown">Unknown / verify</option>
            </select>
          </label>
          <label>
            <span>Relationship</span>
            <select value={relationshipType} onChange={(e) => setRelationshipType(e.target.value)}>
              <option value="all">All relationships</option>
              {Object.keys(facets.relationship_type || {}).map((key) => (
                <option key={key} value={key}>
                  {titleCase(key)} ({facets.relationship_type[key]})
                </option>
              ))}
            </select>
          </label>
          <label>
            <span>Sort</span>
            <select value={sort} onChange={(e) => setSort(e.target.value)}>
              <option value="samples">Numeric quantity (mixed units)</option>
              <option value="name">Name</option>
              <option value="modality">Modality</option>
              <option value="license">License</option>
            </select>
          </label>
        </div>

        <section className="edh-selected" aria-label="Selected datasets">
          <div className="edh-selected-head">
            <div>
              <h3>Selected Access Command</h3>
              <p>{formatNumber(selectedRows.length)} datasets selected for review</p>
            </div>
            <div className="edh-selected-actions">
              <button
                type="button"
                onClick={() => {
                  const names = visibleRows.map((row) => row.name);
                  setSelectedNames((current) => Array.from(new Set([...current, ...names])));
                }}
              >
                Select visible
              </button>
              <button type="button" onClick={() => setSelectedNames([])} disabled={!selectedRows.length}>
                Clear
              </button>
            </div>
          </div>

          <div className="edh-command-row edh-download-command">
            <code title={selectedDownloadCommand}>{selectedDownloadCommand}</code>
            <CopyButton
              copied={copiedToken === 'download-command'}
              disabled={!selectedRows.length}
              label="Copy selected dataset download command"
              tooltip="Copy command"
              onClick={() => copyText(selectedDownloadCommand, 'download-command', 'Copy command')}
            />
          </div>
          <p className="edh-command-note">
            Review every source and its current terms before running this
            command. Some routes require an account, agreement, or manual
            approval.
          </p>

          {selectedRows.length ? (
            <div className="edh-selected-table-wrap">
              <table className="edh-selected-table">
                <thead>
                  <tr>
                    <th>Dataset</th>
                    <th>Access</th>
                    <th>Source</th>
                    <th>Remove</th>
                  </tr>
                </thead>
                <tbody>
                  {selectedRows.map((row) => (
                    <tr key={row.name}>
                      <td>
                        <strong>{row.name}</strong>
                        <CopyButton
                          copied={copiedToken === `selected-name-${row.name}`}
                          label={`Copy dataset name: ${row.name}`}
                          tooltip="Copy dataset name"
                          onClick={() => copyText(row.name, `selected-name-${row.name}`, 'Copy dataset name')}
                        />
                      </td>
                      <td>{titleCase(row.download_type)}</td>
                      <td>
                        {row.download_url ? (
                          <CopyButton
                            copied={copiedToken === `selected-url-${row.name}`}
                            label={`Copy source URL for ${row.name}`}
                            tooltip="Copy URL"
                            onClick={() => copyText(row.download_url, `selected-url-${row.name}`, 'Copy source URL')}
                          />
                        ) : (
                          <span>-</span>
                        )}
                      </td>
                      <td>
                        <button type="button" className="edh-text-button" onClick={() => toggleDataset(row.name, false)}>
                          Remove
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : null}
        </section>

        <div className="edh-table-wrap" role="region" aria-label="Dataset results" tabIndex="0">
          <table className="edh-dataset-table">
            <thead>
              <tr>
                <th>Select</th>
                <th>Dataset</th>
                <th>Modality</th>
                <th>Tasks</th>
                <th>Primary quantity</th>
                <th>License</th>
                <th>Access</th>
                <th>Loader</th>
                <th>Relationships</th>
                <th>Links</th>
              </tr>
            </thead>
            <tbody>
              {visibleRows.map((row) => (
                <tr key={row.name}>
                  <td>
                    <input
                      type="checkbox"
                      checked={selectedNames.includes(row.name)}
                      onChange={(event) => toggleDataset(row.name, event.target.checked)}
                      aria-label={`Select ${row.name}`}
                    />
                  </td>
                  <td>
                    <div className="edh-dataset-name">
                      <a href={withBase(row.doc_path)}><strong>{row.name}</strong></a>
                      <CopyButton
                        copied={copiedToken === `name-${row.name}`}
                        label={`Copy dataset name: ${row.name}`}
                        tooltip="Copy dataset name"
                        onClick={() => copyText(row.name, `name-${row.name}`, 'Copy dataset name')}
                      />
                    </div>
                    <span>{row.full_name}</span>
                  </td>
                  <td>
                    <div className="edh-modality-tags">
                      {(row.modalities || []).map((value) => (
                        <span key={value}>{titleCase(value)}</span>
                      ))}
                    </div>
                  </td>
                  <td>{(row.tasks || []).slice(0, 3).map((task) => <em key={task}>{task}</em>)}</td>
                  <td>{formatPrimaryQuantity(row)}</td>
                  <td><code>{row.license_family}</code></td>
                  <td>{titleCase(row.download_type)}</td>
                  <td>{row.loader_status === 'implemented' ? 'Included' : 'Metadata only'}</td>
                  <td>
                    {(row.relationships || []).length ? (
                      <div className="edh-relationship-tags">
                        {row.relationships.slice(0, 4).map((relationship) => (
                          <a
                            className="edh-relationship-tag"
                            href={withBase(relationship.target_doc_path)}
                            key={`${relationship.direction}-${relationship.relationship_type}-${relationship.target_name}`}
                            title={relationship.evidence_summary}
                          >
                            {titleCase(relationship.relationship_type)}
                            {' '}{relationship.direction === 'outgoing' ? '->' : '<-'}{' '}
                            {relationship.target_name}
                          </a>
                        ))}
                        {row.relationships.length > 4 ? (
                          <a
                            className="edh-relationship-tag"
                            href={withBase(row.doc_path)}
                            title="Open the record page to view every documented relationship"
                          >
                            +{row.relationships.length - 4} more
                          </a>
                        ) : null}
                      </div>
                    ) : <span>-</span>}
                  </td>
                  <td>
                    <a href={withBase(row.doc_path)}>Docs</a>
                    {row.download_url ? <a href={row.download_url}>Source</a> : null}
                    {row.download_url ? (
                      <CopyButton
                        copied={copiedToken === `url-${row.name}`}
                        label={`Copy source URL for ${row.name}`}
                        tooltip="Copy URL"
                        onClick={() => copyText(row.download_url, `url-${row.name}`, 'Copy source URL')}
                      />
                    ) : null}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        {filtered.length > 120 ? (
          <p className="edh-table-note">Showing the first 120 matches. Narrow the filters to inspect the remaining entries.</p>
        ) : null}
      </section>
    </div>
  );
}

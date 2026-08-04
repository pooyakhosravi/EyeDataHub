const BASE_TAGS = [
  { id: 'strong_dataset', label: 'Strong dataset', tone: 'positive' },
  { id: 'not_good', label: 'Dataset not good', tone: 'negative' },
  { id: 'not_human', label: 'Not human', tone: 'negative' },
  { id: 'no_reusable_data', label: 'No reusable data', tone: 'negative' },
  { id: 'analysis_tables_only', label: 'Analysis tables only', tone: 'negative' },
  { id: 'paper_support_tables_only', label: 'Paper support tables only', tone: 'negative' },
  { id: 'derived_measurements_without_source_data', label: 'Derived measures, no source data', tone: 'negative' },
  { id: 'not_relevant', label: 'Not relevant', tone: 'negative' },
  { id: 'duplicate', label: 'Duplicate', tone: 'caution' },
  { id: 'superseded_version', label: 'Superseded version', tone: 'caution' },
  { id: 'derived_or_annotation_only', label: 'Derived/annotation only', tone: 'caution' },
  { id: 'images_missing_from_deposit', label: 'Images missing from deposit', tone: 'caution' },
  { id: 'access_problem', label: 'Access problem', tone: 'caution' },
  { id: 'metadata_problem', label: 'Metadata problem', tone: 'caution' },
  { id: 'human_status_unclear', label: 'Human status unclear', tone: 'caution' },
  { id: 'quantity_unclear', label: 'Quantity unclear', tone: 'caution' },
  { id: 'paper_source_mismatch', label: 'Paper/source mismatch', tone: 'caution' },
  { id: 'inherently_tabular_useful', label: 'Inherently tabular and useful', tone: 'positive' },
  { id: 'primary_images_or_signals_present', label: 'Primary images/signals present', tone: 'positive' },
];

const DECISION_LABELS = {
  include: 'Include',
  needs_review: 'Needs review',
  exclude: 'Exclude',
  duplicate_or_version: 'Duplicate/version',
};

const state = {
  catalog: null,
  records: [],
  recordsById: new Map(),
  reviews: {},
  customTags: [],
  filtered: [],
  currentId: null,
  pendingSaves: 0,
  noteTimers: new Map(),
};

const elements = {};

function byId(id) {
  return document.getElementById(id);
}

function recordId(record) {
  return String(record?.record_id || record?.name || '');
}

function titleCase(value) {
  return String(value || '')
    .replace(/_/g, ' ')
    .replace(/\b\w/g, (character) => character.toUpperCase());
}

function formatNumber(value) {
  if (value === null || value === undefined || value === '') return 'Not reported';
  const number = Number(value);
  return Number.isFinite(number) ? number.toLocaleString() : String(value);
}

function listText(values, empty = 'Not recorded') {
  return Array.isArray(values) && values.length
    ? values.map((value) => titleCase(value)).join(', ')
    : empty;
}

function createElement(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined && text !== null) node.textContent = text;
  return node;
}

function safeExternalUrl(value) {
  if (!value) return '';
  try {
    const url = new URL(String(value));
    return ['http:', 'https:'].includes(url.protocol) ? url.href : '';
  } catch {
    return '';
  }
}

function sourceUrl(record) {
  return [
    record.preferred_route_url,
    record.source_landing_page_url,
    record.canonical_resolver_url,
    record.download_url,
  ].map(safeExternalUrl).find(Boolean) || '';
}

function extractDoi(text) {
  const match = String(text || '').match(/10\.\d{4,9}\/[\-._;()/:A-Z0-9]+/i);
  return match ? match[0].replace(/[.,;)]*$/, '') : '';
}

function publicationUrl(record) {
  const explicitDoi = String(record.associated_publication_doi || '')
    .replace(/^https?:\/\/(dx\.)?doi\.org\//i, '')
    .trim();
  if (explicitDoi) return `https://doi.org/${explicitDoi}`;

  const citationDoi = extractDoi(record.citation);
  if (citationDoi) return `https://doi.org/${citationDoi}`;

  const evidence = safeExternalUrl(record.citation_evidence_url);
  const sourceUrls = new Set([
    safeExternalUrl(record.preferred_route_url),
    safeExternalUrl(record.source_landing_page_url),
    safeExternalUrl(record.download_url),
  ]);
  if (evidence && !sourceUrls.has(evidence)) return evidence;

  const citationUrls = String(record.citation || '').match(/https?:\/\/[^\s<>"']+/g) || [];
  return citationUrls.map((url) => safeExternalUrl(url.replace(/[.,;)]*$/, '')))
    .find((url) => url && !sourceUrls.has(url)) || '';
}

function scholarUrl(record) {
  const query = record.citation || record.full_name || record.canonical_name || record.name;
  return `https://scholar.google.com/scholar?q=${encodeURIComponent(query)}`;
}

function emptyReview() {
  return { decision: '', score: null, tags: [], notes: '' };
}

function reviewFor(id) {
  const existing = state.reviews[id];
  return existing
    ? {
        decision: existing.decision || '',
        score: existing.score ?? null,
        tags: Array.isArray(existing.tags) ? [...existing.tags] : [],
        notes: existing.notes || '',
        reviewed_at: existing.reviewed_at || '',
      }
    : emptyReview();
}

function isReviewed(review) {
  return Boolean(review?.decision);
}

async function apiJson(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
  });
  if (!response.ok) {
    let message = `Request failed (${response.status})`;
    try {
      const payload = await response.json();
      if (payload.error) message = payload.error;
    } catch {
      // Keep the status-based message.
    }
    throw new Error(message);
  }
  return response.json();
}

function setSaveState(mode, text) {
  elements.saveState.className = `save-state${mode ? ` ${mode}` : ''}`;
  elements.saveState.textContent = text;
}

function showToast(message, type = '') {
  elements.toast.textContent = message;
  elements.toast.className = `toast visible${type ? ` ${type}` : ''}`;
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => {
    elements.toast.className = 'toast';
  }, 2600);
}

async function persistReview(id, review) {
  state.pendingSaves += 1;
  setSaveState('saving', 'Saving...');
  try {
    const payload = await apiJson(`/api/reviews/${encodeURIComponent(id)}`, {
      method: 'POST',
      body: JSON.stringify(review),
    });
    if (payload.review) state.reviews[id] = payload.review;
    else delete state.reviews[id];
  } catch (error) {
    setSaveState('error', 'Save failed');
    showToast(`Could not save: ${error.message}`, 'error');
    throw error;
  } finally {
    state.pendingSaves -= 1;
    if (state.pendingSaves === 0 && !elements.saveState.classList.contains('error')) {
      setSaveState('', 'Saved locally');
    }
  }
}

function saveReview(id, patch, options = {}) {
  if (!id) return;
  const existing = reviewFor(id);
  const updated = { ...existing, ...patch };
  if (patch.tags) updated.tags = [...patch.tags];
  state.reviews[id] = updated;

  const nextId = options.advance ? nextQueueId(id) : null;
  renderProgress();
  applyFilters({ keepCurrent: true });
  if (options.advance && nextId) selectRecord(nextId, { scrollQueue: true });
  else renderCurrentReview();

  persistReview(id, updated).catch(() => {});
}

function scheduleNoteSave(id, notes) {
  const review = reviewFor(id);
  review.notes = notes;
  state.reviews[id] = review;
  elements.notesCount.textContent = `${notes.length.toLocaleString()} characters`;

  const priorTimer = state.noteTimers.get(id);
  if (priorTimer) window.clearTimeout(priorTimer);
  const timer = window.setTimeout(() => {
    state.noteTimers.delete(id);
    persistReview(id, reviewFor(id)).catch(() => {});
  }, 550);
  state.noteTimers.set(id, timer);
}

function flushNotes(id) {
  const timer = state.noteTimers.get(id);
  if (!timer) return;
  window.clearTimeout(timer);
  state.noteTimers.delete(id);
  persistReview(id, reviewFor(id)).catch(() => {});
}

function uniqueValues(selector) {
  const values = new Set();
  state.records.forEach((record) => {
    const selected = selector(record);
    (Array.isArray(selected) ? selected : [selected]).filter(Boolean).forEach((value) => values.add(value));
  });
  return [...values].sort((a, b) => String(a).localeCompare(String(b)));
}

function fillSelect(select, values, label) {
  values.forEach((value) => {
    const count = state.records.filter((record) => {
      const selected = label.selector(record);
      return Array.isArray(selected) ? selected.includes(value) : selected === value;
    }).length;
    const option = document.createElement('option');
    option.value = value;
    option.textContent = `${titleCase(value)} (${count})`;
    select.append(option);
  });
}

function initializeFilters() {
  const roles = uniqueValues((record) => record.resource_role);
  const modalities = uniqueValues((record) => record.modalities || []);
  const sources = uniqueValues((record) => record.download_type);
  const scopeClasses = uniqueValues((record) => record.internal_model_data_screen?.classification);
  fillSelect(elements.roleFilter, roles, { selector: (record) => record.resource_role });
  fillSelect(elements.modalityFilter, modalities, { selector: (record) => record.modalities || [] });
  fillSelect(elements.sourceFilter, sources, { selector: (record) => record.download_type });
  fillSelect(elements.scopeFilter, scopeClasses, { selector: (record) => record.internal_model_data_screen?.classification });
}

function recordHaystack(record) {
  return [
    record.name,
    record.record_id,
    record.full_name,
    record.canonical_name,
    record.description,
    record.dataset_family_id,
    record.primary_category,
    record.download_type,
    record.resource_role,
    ...(record.modalities || []),
    ...(record.tasks || []),
    ...(record.tags || []),
    record.internal_model_data_screen?.classification,
    record.internal_model_data_screen?.suggested_action,
    record.internal_model_data_screen?.rationale,
    record.internal_model_data_screen?.source_evidence,
  ].join(' ').toLowerCase();
}

function applyFilters(options = {}) {
  const query = elements.searchInput.value.trim().toLowerCase();
  const status = elements.statusFilter.value;
  const role = elements.roleFilter.value;
  const modality = elements.modalityFilter.value;
  const source = elements.sourceFilter.value;
  const scope = elements.scopeFilter.value;

  state.filtered = state.records.filter((record) => {
    const id = recordId(record);
    const review = reviewFor(id);
    return (
      (!query || recordHaystack(record).includes(query))
      && (status === 'all' || status === 'unreviewed' || review.decision === status)
      && (role === 'all' || record.resource_role === role)
      && (modality === 'all' || (record.modalities || []).includes(modality))
      && (source === 'all' || record.download_type === source)
      && (scope === 'all' || record.internal_model_data_screen?.classification === scope)
    );
  });

  state.filtered.sort((a, b) => {
    if (status === 'unreviewed') {
      const aReviewed = isReviewed(reviewFor(recordId(a)));
      const bReviewed = isReviewed(reviewFor(recordId(b)));
      if (aReviewed !== bReviewed) return aReviewed ? 1 : -1;
    }
    return String(a.full_name || a.name).localeCompare(String(b.full_name || b.name));
  });

  if (!options.keepCurrent || !state.filtered.some((record) => recordId(record) === state.currentId)) {
    state.currentId = state.filtered[0] ? recordId(state.filtered[0]) : null;
  }
  renderQueue(Boolean(options.scrollQueue));
  renderRecord();
}

function renderProgress() {
  const decisions = { include: 0, needs_review: 0, exclude: 0, duplicate_or_version: 0 };
  state.records.forEach((record) => {
    const decision = reviewFor(recordId(record)).decision;
    if (decisions[decision] !== undefined) decisions[decision] += 1;
  });
  const reviewed = Object.values(decisions).reduce((sum, count) => sum + count, 0);
  const percent = state.records.length ? Math.round((reviewed / state.records.length) * 100) : 0;
  elements.progressCount.textContent = `${reviewed.toLocaleString()} of ${state.records.length.toLocaleString()}`;
  elements.progressPercent.textContent = `${percent}%`;
  elements.progressBar.style.width = `${percent}%`;
  elements.decisionCounts.replaceChildren(
    createElement('span', '', `${decisions.include} include`),
    createElement('span', '', `${decisions.needs_review} review`),
    createElement('span', '', `${decisions.exclude} exclude`),
    createElement('span', '', `${decisions.duplicate_or_version} duplicate/version`),
  );
}

function renderQueue(scrollCurrent = false) {
  elements.queueSummary.textContent = `${state.filtered.length.toLocaleString()} matching records`;
  const fragment = document.createDocumentFragment();
  if (!state.filtered.length) {
    fragment.append(createElement('div', 'empty-queue', 'No records match these filters.'));
  } else {
    state.filtered.forEach((record) => {
      const id = recordId(record);
      const review = reviewFor(id);
      const button = createElement('button', `queue-item${id === state.currentId ? ' active' : ''}`);
      button.type = 'button';
      button.dataset.recordId = id;
      button.setAttribute('role', 'option');
      button.setAttribute('aria-selected', id === state.currentId ? 'true' : 'false');
      button.title = record.full_name || record.canonical_name || id;
      button.addEventListener('click', () => selectRecord(id));

      button.append(createElement('span', `status-dot ${review.decision || 'unreviewed'}`));
      const copy = createElement('span');
      copy.append(
        createElement('span', 'queue-name', record.full_name || record.canonical_name || id),
        createElement('span', 'queue-meta', `${titleCase(record.resource_role)} | ${listText(record.modalities)}`),
      );
      button.append(copy, createElement('span', 'queue-score', review.score || ''));
      fragment.append(button);
    });
  }
  elements.recordList.replaceChildren(fragment);
  if (scrollCurrent) {
    window.requestAnimationFrame(() => {
      elements.recordList.querySelector('.queue-item.active')?.scrollIntoView({ block: 'nearest' });
    });
  }
}

function setLink(element, url, enabledLabel, disabledLabel) {
  const safe = safeExternalUrl(url);
  element.textContent = safe ? enabledLabel : disabledLabel;
  element.classList.toggle('disabled', !safe);
  if (safe) {
    element.href = safe;
    element.removeAttribute('aria-disabled');
  } else {
    element.removeAttribute('href');
    element.setAttribute('aria-disabled', 'true');
  }
}

function appendBadge(container, label, role = '') {
  container.append(createElement('span', `badge${role ? ` ${role}` : ''}`, label));
}

function accessRequirements(record) {
  const requirements = [];
  if (record.requires_registration === true) requirements.push('registration');
  if (record.requires_authentication === true) requirements.push('authentication');
  if (record.requires_api_token === true) requirements.push('API token');
  if (record.requires_clickthrough === true) requirements.push('click-through');
  if (record.requires_manual_approval === true) requirements.push('manual approval');
  if (record.requires_data_use_agreement === true) requirements.push('data-use agreement');
  if (record.requires_author_contact === true) requirements.push('author contact');
  if (record.requires_payment === true) requirements.push('payment');
  return requirements.length ? requirements.join(', ') : 'No affirmative requirement flags';
}

function addEvidenceTerm(container, label, value, url = '') {
  const wrapper = createElement('div');
  wrapper.append(createElement('dt', '', label));
  const definition = createElement('dd');
  const safe = safeExternalUrl(url);
  if (safe) {
    const link = createElement('a', '', value || 'View evidence');
    link.href = safe;
    link.target = '_blank';
    link.rel = 'noopener';
    definition.append(link);
  } else {
    definition.textContent = value || 'Not recorded';
  }
  wrapper.append(definition);
  container.append(wrapper);
}

function renderQuantities(record) {
  const quantities = Array.isArray(record.reported_quantities) ? record.reported_quantities : [];
  elements.quantitySection.hidden = quantities.length === 0;
  const fragment = document.createDocumentFragment();
  quantities.forEach((quantity) => {
    const row = createElement('div', 'quantity-row');
    const main = createElement('div', 'quantity-main');
    main.append(createElement('strong', '', `${formatNumber(quantity.count)} ${titleCase(quantity.unit || 'units')}`));
    const evidenceUrl = safeExternalUrl(quantity.evidence_url);
    if (evidenceUrl) {
      const link = createElement('a', 'mini-link', 'Check evidence');
      link.href = evidenceUrl;
      link.target = '_blank';
      link.rel = 'noopener';
      main.append(link);
    }
    const details = [
      quantity.scope,
      quantity.evidence_basis ? `Basis: ${titleCase(quantity.evidence_basis)}` : '',
      quantity.exactness ? `Exactness: ${titleCase(quantity.exactness)}` : '',
      quantity.review_date ? `Reviewed: ${quantity.review_date}` : '',
    ].filter(Boolean).join(' | ');
    row.append(main, createElement('p', 'quantity-meta', details));
    fragment.append(row);
  });
  elements.quantityList.replaceChildren(fragment);
}

function relationshipType(relationship) {
  return relationship.type || relationship.relationship_type || 'related_to';
}

function relationshipTarget(relationship) {
  return relationship.target || relationship.target_name || '';
}

function renderRelationships(record) {
  const relationships = Array.isArray(record.relationships) ? record.relationships : [];
  const alternates = Array.isArray(record.alternate_sources) ? record.alternate_sources : [];
  elements.relationshipSection.hidden = relationships.length === 0 && alternates.length === 0;
  const fragment = document.createDocumentFragment();

  relationships.forEach((relationship) => {
    const row = createElement('div', 'relationship-row');
    const main = createElement('div', 'relationship-main');
    const target = relationshipTarget(relationship);
    main.append(createElement('strong', '', `${titleCase(relationshipType(relationship))}: ${target || 'Unnamed record'}`));
    if (target && state.recordsById.has(target)) {
      const button = createElement('button', 'related-record-button', 'Review linked record');
      button.type = 'button';
      button.addEventListener('click', () => {
        clearFilters(false);
        selectRecord(target, { scrollQueue: true });
      });
      main.append(button);
    } else if (safeExternalUrl(relationship.evidence_url)) {
      const link = createElement('a', 'mini-link', 'Check evidence');
      link.href = safeExternalUrl(relationship.evidence_url);
      link.target = '_blank';
      link.rel = 'noopener';
      main.append(link);
    }
    const meta = [relationship.direction, relationship.evidence_summary].filter(Boolean).join(' | ');
    row.append(main, createElement('p', 'relationship-meta', meta || 'Relationship recorded in the catalog.'));
    fragment.append(row);
  });

  alternates.forEach((alternate) => {
    const row = createElement('div', 'alternate-row');
    const main = createElement('div', 'relationship-main');
    main.append(createElement('strong', '', `Alternate ${titleCase(alternate.role || 'source')}: ${titleCase(alternate.platform || 'source')}`));
    const url = safeExternalUrl(alternate.url);
    if (url) {
      const link = createElement('a', 'mini-link', 'Open alternate');
      link.href = url;
      link.target = '_blank';
      link.rel = 'noopener';
      main.append(link);
    }
    const meta = [alternate.identifier, alternate.version, alternate.notes].filter(Boolean).join(' | ');
    row.append(main, createElement('p', 'relationship-meta', meta || 'Alternate source recorded in the catalog.'));
    fragment.append(row);
  });

  elements.relationshipList.replaceChildren(fragment);
}

function renderRecord() {
  const record = state.recordsById.get(state.currentId);
  const currentIndex = state.filtered.findIndex((item) => recordId(item) === state.currentId);
  elements.recordPosition.textContent = record
    ? `Record ${(currentIndex + 1).toLocaleString()} of ${state.filtered.length.toLocaleString()}`
    : 'No matching record';
  elements.previousRecord.disabled = !record || state.filtered.length < 2;
  elements.nextRecord.disabled = !record || state.filtered.length < 2;
  elements.recordCard.hidden = !record;
  if (!record) return;

  const id = recordId(record);
  const review = reviewFor(id);
  elements.recordTitle.textContent = record.full_name || record.canonical_name || id;
  elements.recordId.textContent = `${id} | family: ${record.dataset_family_id || 'not assigned'}`;
  elements.recordDescription.textContent = record.description || 'No description recorded.';
  elements.recordBadges.replaceChildren();
  appendBadge(elements.recordBadges, titleCase(record.resource_role || 'unclassified'), 'role');
  appendBadge(elements.recordBadges, titleCase(record.primary_category || 'uncategorized'));
  (record.modalities || []).forEach((modality) => appendBadge(elements.recordBadges, titleCase(modality)));
  (record.tasks || []).slice(0, 4).forEach((task) => appendBadge(elements.recordBadges, titleCase(task)));

  elements.currentVerdict.className = `current-verdict${review.decision ? ` ${review.decision}` : ''}`;
  elements.currentVerdict.textContent = review.decision ? DECISION_LABELS[review.decision] : 'Unreviewed';

  const dataset = sourceUrl(record);
  const paper = publicationUrl(record);
  setLink(elements.datasetLink, dataset, 'Open dataset source', 'Dataset source unavailable');
  setLink(elements.paperLink, paper, 'Open associated paper', 'Direct paper link unavailable');
  setLink(elements.scholarLink, scholarUrl(record), 'Search paper', 'Paper search unavailable');
  elements.openBoth.disabled = !dataset && !paper;
  elements.openBoth.onclick = () => {
    if (dataset) window.open(dataset, '_blank', 'noopener');
    window.setTimeout(() => window.open(paper || scholarUrl(record), '_blank', 'noopener'), 80);
  };

  elements.lastChecked.textContent = record.source_check_date || record.route_last_checked
    ? `Source checked ${record.source_check_date || record.route_last_checked}`
    : 'Source check date not recorded';

  elements.evidenceGrid.replaceChildren();
  addEvidenceTerm(elements.evidenceGrid, 'Resource role', titleCase(record.resource_role), '');
  addEvidenceTerm(elements.evidenceGrid, 'Dataset family', record.dataset_family_id || 'Not assigned', '');
  addEvidenceTerm(elements.evidenceGrid, 'Primary quantity', `${formatNumber(record.num_samples)} ${titleCase(record.item_count_unit || 'units')}`, record.item_count_evidence_url);
  addEvidenceTerm(elements.evidenceGrid, 'Modalities', listText(record.modalities), record.modality_evidence_url);
  addEvidenceTerm(elements.evidenceGrid, 'Tasks', listText(record.tasks), record.task_evidence_url);
  addEvidenceTerm(elements.evidenceGrid, 'Source/backend', titleCase(record.download_type || record.loader_backend), dataset);
  addEvidenceTerm(elements.evidenceGrid, 'Access route', titleCase(record.access_friction), '');
  addEvidenceTerm(elements.evidenceGrid, 'Requirements', accessRequirements(record), '');
  addEvidenceTerm(elements.evidenceGrid, 'Source-stated terms', record.source_terms || record.license || 'Not recorded', record.terms_evidence_url);
  addEvidenceTerm(elements.evidenceGrid, 'Terms scope', titleCase(record.terms_scope), '');
  addEvidenceTerm(elements.evidenceGrid, 'Availability', titleCase(record.availability_status), '');
  addEvidenceTerm(elements.evidenceGrid, 'Version/identifier', record.resource_version || record.dataset_doi || record.dataset_accession || record.repository_record_id || 'Not recorded', record.canonical_resolver_url);
  if (record.internal_model_data_screen) {
    const screen = record.internal_model_data_screen;
    addEvidenceTerm(elements.evidenceGrid, 'Model-data screen', titleCase(screen.classification), '');
    addEvidenceTerm(elements.evidenceGrid, 'Suggested action', titleCase(screen.suggested_action), '');
    addEvidenceTerm(elements.evidenceGrid, 'Screen rationale', screen.rationale, '');
    addEvidenceTerm(elements.evidenceGrid, 'File/source evidence', screen.source_evidence, '');
    if (screen.suggested_modalities?.length) {
      addEvidenceTerm(elements.evidenceGrid, 'Suggested modalities', listText(screen.suggested_modalities), '');
    }
  }

  renderQuantities(record);
  renderRelationships(record);
  elements.recordCitation.textContent = record.citation || 'No citation recorded.';
  elements.catalogNotes.textContent = record.notes || '';
  elements.catalogNotesBlock.hidden = !record.notes;
  elements.rawRecord.textContent = JSON.stringify(record, null, 2);
  renderCurrentReview();
  history.replaceState(null, '', `#record=${encodeURIComponent(id)}`);
}

function allTagDefinitions(review) {
  const known = [...BASE_TAGS];
  const knownIds = new Set(known.map((tag) => tag.id));
  state.customTags.forEach((tag) => {
    if (!knownIds.has(tag)) {
      known.push({ id: tag, label: titleCase(tag), tone: 'custom' });
      knownIds.add(tag);
    }
  });
  (review.tags || []).forEach((tag) => {
    if (!knownIds.has(tag)) known.push({ id: tag, label: titleCase(tag), tone: 'custom' });
  });
  return known;
}

function renderCurrentReview() {
  if (!state.currentId) return;
  const review = reviewFor(state.currentId);
  elements.scoreButtons.querySelectorAll('[data-score]').forEach((button) => {
    const active = Number(button.dataset.score) === review.score;
    button.classList.toggle('active', active);
    button.setAttribute('aria-checked', active ? 'true' : 'false');
  });

  const tagFragment = document.createDocumentFragment();
  allTagDefinitions(review).forEach((tag) => {
    const active = review.tags.includes(tag.id);
    const button = createElement('button', `tag-button ${tag.tone}${active ? ' active' : ''}`, tag.label);
    button.type = 'button';
    button.dataset.tag = tag.id;
    button.setAttribute('aria-pressed', active ? 'true' : 'false');
    button.addEventListener('click', () => toggleTag(tag.id));
    tagFragment.append(button);
  });
  elements.tagButtons.replaceChildren(tagFragment);

  if (document.activeElement !== elements.reviewNotes) {
    elements.reviewNotes.value = review.notes;
  }
  elements.notesCount.textContent = `${review.notes.length.toLocaleString()} characters`;
  elements.decisionButtons.forEach((button) => {
    button.classList.toggle('active', button.dataset.decision === review.decision);
    button.setAttribute('aria-pressed', button.dataset.decision === review.decision ? 'true' : 'false');
  });
}

function selectRecord(id, options = {}) {
  if (!state.recordsById.has(id)) return;
  if (state.currentId && state.currentId !== id) flushNotes(state.currentId);
  state.currentId = id;
  renderQueue(Boolean(options.scrollQueue));
  renderRecord();
  document.querySelector('.record-panel')?.scrollIntoView({ block: 'start' });
}

function nextQueueId(id, delta = 1) {
  if (!state.filtered.length) return null;
  const index = Math.max(0, state.filtered.findIndex((record) => recordId(record) === id));
  return recordId(state.filtered[(index + delta + state.filtered.length) % state.filtered.length]);
}

function moveRecord(delta) {
  const id = nextQueueId(state.currentId, delta);
  if (id) selectRecord(id, { scrollQueue: true });
}

function toggleTag(tag) {
  if (!state.currentId) return;
  const review = reviewFor(state.currentId);
  const tags = review.tags.includes(tag)
    ? review.tags.filter((current) => current !== tag)
    : [...review.tags, tag];
  saveReview(state.currentId, { tags });
}

async function addCustomTag(rawTag) {
  const tag = String(rawTag || '').trim().replace(/\s+/g, '_').toLowerCase().slice(0, 80);
  if (!tag) return;
  if (!state.customTags.includes(tag) && !BASE_TAGS.some((item) => item.id === tag)) {
    state.customTags.push(tag);
    try {
      const payload = await apiJson('/api/settings/tags', {
        method: 'POST',
        body: JSON.stringify({ custom_tags: state.customTags }),
      });
      state.customTags = payload.custom_tags;
    } catch (error) {
      showToast(`Could not save custom tag: ${error.message}`, 'error');
      return;
    }
  }
  const review = reviewFor(state.currentId);
  if (!review.tags.includes(tag)) saveReview(state.currentId, { tags: [...review.tags, tag] });
}

function clearCurrentReview() {
  if (!state.currentId) return;
  const id = state.currentId;
  state.reviews[id] = emptyReview();
  elements.reviewNotes.value = '';
  renderProgress();
  applyFilters({ keepCurrent: true });
  persistReview(id, emptyReview()).catch(() => {});
  showToast('Record reset to unreviewed.');
}

function clearFilters(render = true) {
  elements.searchInput.value = '';
  elements.statusFilter.value = 'unreviewed';
  elements.roleFilter.value = 'all';
  elements.modalityFilter.value = 'all';
  elements.sourceFilter.value = 'all';
  elements.scopeFilter.value = 'all';
  if (render) applyFilters();
}

function bindEvents() {
  [elements.searchInput, elements.statusFilter, elements.roleFilter, elements.modalityFilter, elements.sourceFilter, elements.scopeFilter]
    .forEach((element) => element.addEventListener('input', () => applyFilters()));
  elements.clearFilters.addEventListener('click', () => clearFilters());
  elements.previousRecord.addEventListener('click', () => moveRecord(-1));
  elements.nextRecord.addEventListener('click', () => moveRecord(1));
  elements.scoreButtons.querySelectorAll('[data-score]').forEach((button) => {
    button.addEventListener('click', () => saveReview(state.currentId, { score: Number(button.dataset.score) }));
  });
  elements.clearScore.addEventListener('click', () => saveReview(state.currentId, { score: null }));
  elements.reviewNotes.addEventListener('input', (event) => {
    if (state.currentId) scheduleNoteSave(state.currentId, event.target.value);
  });
  elements.decisionButtons.forEach((button) => {
    button.addEventListener('click', () => saveReview(
      state.currentId,
      { decision: button.dataset.decision },
      { advance: elements.autoAdvance.checked },
    ));
  });
  elements.clearReview.addEventListener('click', clearCurrentReview);
  elements.customTagForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const value = elements.customTagInput.value;
    elements.customTagInput.value = '';
    addCustomTag(value);
  });
  elements.keyboardHelp.addEventListener('click', () => elements.shortcutDialog.showModal());

  document.addEventListener('keydown', (event) => {
    const target = event.target;
    if (target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target instanceof HTMLSelectElement) return;
    if (elements.shortcutDialog.open && event.key !== 'Escape') return;
    const key = event.key.toLowerCase();
    if (key === '?' && !elements.shortcutDialog.open) {
      event.preventDefault();
      elements.shortcutDialog.showModal();
    } else if (key === '/' && !elements.shortcutDialog.open) {
      event.preventDefault();
      elements.searchInput.focus();
    } else if (key === 'j' || event.key === 'ArrowRight') {
      event.preventDefault();
      moveRecord(1);
    } else if (key === 'k' || event.key === 'ArrowLeft') {
      event.preventDefault();
      moveRecord(-1);
    } else if (['1', '2', '3', '4'].includes(key)) {
      const decisions = ['include', 'needs_review', 'exclude', 'duplicate_or_version'];
      event.preventDefault();
      saveReview(state.currentId, { decision: decisions[Number(key) - 1] }, { advance: elements.autoAdvance.checked });
    } else if (key === 'o') {
      const record = state.recordsById.get(state.currentId);
      const url = sourceUrl(record || {});
      if (url) window.open(url, '_blank', 'noopener');
    } else if (key === 'p') {
      const record = state.recordsById.get(state.currentId);
      const url = publicationUrl(record || {}) || scholarUrl(record || {});
      if (url) window.open(url, '_blank', 'noopener');
    }
  });

  window.addEventListener('beforeunload', () => {
    if (state.currentId) flushNotes(state.currentId);
  });
}

function cacheElements() {
  const ids = [
    'loading', 'app', 'save-state', 'progress-count', 'progress-percent', 'progress-bar',
    'decision-counts', 'search-input', 'status-filter', 'role-filter', 'modality-filter',
    'source-filter', 'scope-filter', 'clear-filters', 'queue-summary', 'record-list', 'previous-record',
    'next-record', 'record-position', 'record-card', 'record-badges', 'record-title',
    'record-id', 'current-verdict', 'record-description', 'dataset-link', 'paper-link',
    'scholar-link', 'open-both', 'last-checked', 'evidence-grid', 'quantity-section',
    'quantity-list', 'relationship-section', 'relationship-list', 'record-citation',
    'catalog-notes-block', 'catalog-notes', 'raw-record', 'keyboard-help', 'clear-score',
    'score-buttons', 'tag-buttons', 'custom-tag-form', 'custom-tag-input', 'review-notes',
    'notes-count', 'auto-advance', 'clear-review', 'shortcut-dialog', 'toast',
  ];
  ids.forEach((id) => {
    const key = id.replace(/-([a-z])/g, (_, letter) => letter.toUpperCase());
    elements[key] = byId(id);
  });
  elements.decisionButtons = [...document.querySelectorAll('[data-decision]')];
}

async function initialize() {
  cacheElements();
  bindEvents();
  try {
    const [catalog, reviews] = await Promise.all([
      apiJson('/api/catalog'),
      apiJson('/api/reviews'),
    ]);
    state.catalog = catalog;
    state.records = [...catalog.records].sort((a, b) =>
      String(a.full_name || a.name).localeCompare(String(b.full_name || b.name))
    );
    state.recordsById = new Map(state.records.map((record) => [recordId(record), record]));
    state.reviews = reviews.reviews || {};
    state.customTags = reviews.custom_tags || [];

    initializeFilters();
    const requestedId = decodeURIComponent(location.hash.replace(/^#record=/, ''));
    state.currentId = state.recordsById.has(requestedId) ? requestedId : recordId(state.records[0]);
    renderProgress();
    applyFilters({ keepCurrent: true, scrollQueue: true });
    elements.loading.hidden = true;
    elements.app.hidden = false;
  } catch (error) {
    elements.loading.innerHTML = '';
    const title = createElement('h1', '', 'The review desk could not start');
    const message = createElement('p', '', error.message);
    const hint = createElement('p', '', 'Keep the local Python review server running, then reload this page.');
    elements.loading.append(title, message, hint);
  }
}

initialize();

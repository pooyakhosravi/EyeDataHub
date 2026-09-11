import {comparePublicationDates} from './publicationDates.mjs';

export const SORT_COLUMNS = [
  {key: 'name', label: 'Dataset'},
  {key: 'modality', label: 'Modality'},
  {key: 'publication-date', label: 'Publication date'},
  {key: 'tasks', label: 'Tasks'},
  {key: 'samples', label: 'Primary quantity'},
  {key: 'license', label: 'License'},
  {key: 'access', label: 'Access'},
  {key: 'loader', label: 'Loader'},
  {key: 'relationships', label: 'Relationships'},
];

export function sortValue(key, descending = false) {
  if (key === 'samples') return descending ? 'samples' : 'samples-asc';
  return descending ? `${key}-desc` : key;
}

export function sortDirection(value, key) {
  if (value === sortValue(key)) return 'ascending';
  if (value === sortValue(key, true)) return 'descending';
  return 'none';
}

export function nextSort(value, key) {
  return sortValue(key, sortDirection(value, key) === 'ascending');
}

const listText = (values) => [...(values || [])].sort().join(', ');
const textValue = (row, key) => ({
  name: row.name,
  modality: listText(row.modalities),
  tasks: listText(row.tasks),
  license: row.license_family,
  access: row.download_type,
  loader: row.loader_status === 'implemented' ? 'Included' : 'Metadata only',
}[key] || '');

export function compareTableRows(a, b, value) {
  const column = SORT_COLUMNS.find(({key}) => sortDirection(value, key) !== 'none');
  const key = column?.key || 'name';
  const descending = sortDirection(value, key) === 'descending';
  if (key === 'publication-date') return comparePublicationDates(a, b, descending);
  let result;
  if (key === 'samples') {
    const av = Number.isFinite(a.samples) ? a.samples : null;
    const bv = Number.isFinite(b.samples) ? b.samples : null;
    if (av === null || bv === null) {
      if (av !== null) return -1;
      if (bv !== null) return 1;
      return a.name.localeCompare(b.name);
    }
    result = av - bv;
  } else if (key === 'relationships') {
    result = (a.relationships || []).length - (b.relationships || []).length;
  } else {
    result = textValue(a, key).localeCompare(textValue(b, key));
  }
  return (descending ? -result : result) || a.name.localeCompare(b.name);
}

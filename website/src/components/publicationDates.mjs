// Date-only comparisons avoid browser timezone shifts. Partial dates stay partial.
export function publicationDateBasis(scope) {
  return {
    initial_public_release: 'Initial dataset release',
    repository_deposit: 'Repository deposit',
    associated_publication: 'Associated publication',
  }[scope] || 'Unknown';
}

export function publicationYear(value) {
  if (!/^\d{4}(?:-\d{2}){0,2}$/.test(value || '')) return null;
  return Number(value.slice(0, 4));
}

export function validYearRange(from, through) {
  const valid = (v) => v === '' || (/^\d{4}$/.test(v) && Number(v) >= 1);
  return valid(from) && valid(through) && (!from || !through || Number(from) <= Number(through));
}

export function matchesPublicationDate(row, from = '', through = '', status = 'any') {
  if (!validYearRange(from, through)) return false;
  const year = publicationYear(row.publication_date);
  if (status === 'known' && year === null) return false;
  if (status === 'unknown' && year !== null) return false;
  if (from || through) {
    if (year === null) return false;
    if ((from && year < Number(from)) || (through && year > Number(through))) return false;
  }
  return true;
}

export function comparePublicationDates(a, b, descending = false) {
  const av = a.publication_date;
  const bv = b.publication_date;
  if (!av || !bv) {
    if (av) return -1;
    if (bv) return 1;
    return a.name.localeCompare(b.name);
  }
  // Bounds used only for ordering, never displayed as a more precise date.
  const start = (v) => v.length === 4 ? `${v}-01-01` : v.length === 7 ? `${v}-01` : v;
  const result = start(av).localeCompare(start(bv));
  return (descending ? -result : result) || a.name.localeCompare(b.name);
}

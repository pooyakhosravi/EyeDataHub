import test from 'node:test';
import assert from 'node:assert/strict';
import {SORT_COLUMNS, sortValue, sortDirection, nextSort, compareTableRows} from '../src/components/tableSort.mjs';

test('headers and dropdown share ascending and descending values for every column', () => {
  for (const {key} of SORT_COLUMNS) {
    const asc = sortValue(key);
    const desc = sortValue(key, true);
    assert.equal(sortDirection(asc, key), 'ascending');
    assert.equal(sortDirection(desc, key), 'descending');
    assert.equal(nextSort(asc, key), desc);
    assert.equal(nextSort(desc, key), asc);
    assert.equal(sortDirection('invalid', key), 'none');
  }
});

test('every displayed data column sorts in both directions', () => {
  const a = {name: 'a', modalities: ['Fundus'], tasks: ['Classification'], publication_date: '2020', samples: 1, license_family: 'cc-by', download_type: 'Figshare', loader_status: 'implemented', relationships: []};
  const b = {name: 'b', modalities: ['OCT'], tasks: ['Segmentation'], publication_date: '2021-02', samples: 2, license_family: 'research-only', download_type: 'Manual', loader_status: 'metadata_only', relationships: [{}]};
  for (const {key} of SORT_COLUMNS) {
    assert.ok(compareTableRows(a, b, sortValue(key)) < 0, key);
    assert.ok(compareTableRows(a, b, sortValue(key, true)) > 0, key);
  }
});

test('unknown quantities and dates stay last in either direction and zero is valid', () => {
  const rows = [{name: 'unknown'}, {name: 'zero', samples: 0, publication_date: '2020'}, {name: 'many', samples: 5, publication_date: '2021'}];
  for (const key of ['samples', 'publication-date']) {
    assert.deepEqual([...rows].sort((a, b) => compareTableRows(a, b, sortValue(key))).map(r => r.name), ['zero', 'many', 'unknown']);
    assert.deepEqual([...rows].sort((a, b) => compareTableRows(a, b, sortValue(key, true))).map(r => r.name), ['many', 'zero', 'unknown']);
  }
});

test('multi-valued fields are compared consistently without changing their order', () => {
  const a = {name: 'a', modalities: ['OCT', 'Fundus']};
  const b = {name: 'b', modalities: ['Fundus', 'OCT']};
  assert.ok(compareTableRows(a, b, 'modality-desc') < 0);
  assert.deepEqual(a.modalities, ['OCT', 'Fundus']);
  assert.ok(compareTableRows(a, b, 'invalid') < 0);
});

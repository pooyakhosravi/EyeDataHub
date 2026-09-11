import test from 'node:test';
import assert from 'node:assert/strict';
import {comparePublicationDates, matchesPublicationDate, publicationDateBasis, validYearRange} from '../src/components/publicationDates.mjs';

test('labels the source basis of each selected date', () => {
  assert.equal(publicationDateBasis('initial_public_release'), 'Initial dataset release');
  assert.equal(publicationDateBasis('repository_deposit'), 'Repository deposit');
  assert.equal(publicationDateBasis('associated_publication'), 'Associated publication');
  assert.equal(publicationDateBasis(null), 'Unknown');
});

const rows = [
  {name: 'unknown', publication_date: null},
  {name: 'year', publication_date: '2020'},
  {name: 'month', publication_date: '2020-06'},
  {name: 'day', publication_date: '2020-06-15'},
  {name: 'early', publication_date: '2019-12-31'},
];

test('sorts partial dates without changing stored values; unknown last both ways', () => {
  assert.deepEqual([...rows].sort(comparePublicationDates).map(r => r.name), ['early', 'year', 'month', 'day', 'unknown']);
  assert.deepEqual([...rows].sort((a, b) => comparePublicationDates(a, b, true)).map(r => r.name), ['day', 'month', 'year', 'early', 'unknown']);
  assert.equal(rows[1].publication_date, '2020');
  assert.ok(comparePublicationDates({name: 'a', publication_date: '2020'}, {name: 'b', publication_date: '2020-01-01'}) < 0);
});

test('year filters are inclusive and exclude unknown dates', () => {
  assert.deepEqual(rows.filter(r => matchesPublicationDate(r, '2020', '2020')).map(r => r.name), ['year', 'month', 'day']);
  assert.deepEqual(rows.filter(r => matchesPublicationDate(r, '', '', 'unknown')).map(r => r.name), ['unknown']);
  assert.equal(rows.filter(r => matchesPublicationDate(r, '', '', 'known')).length, 4);
  assert.equal(matchesPublicationDate(rows[0], '2020', '', 'unknown'), false);
});

test('invalid and reversed ranges do not silently match records', () => {
  for (const [from, through] of [['2021', '2020'], ['abc', ''], ['0000', ''], ['20', ''], ['', '2020-01']]) {
    assert.equal(validYearRange(from, through), false);
    assert.equal(matchesPublicationDate(rows[1], from, through), false);
  }
  assert.equal(validYearRange('', ''), true);
});

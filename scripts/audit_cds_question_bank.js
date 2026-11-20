#!/usr/bin/env node
/* Read-only CDS question-bank audit: exact and normalized-text duplicates. */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const dataDir = path.join(root, 'data');
const files = fs.readdirSync(dataDir)
  .filter((name) => name.endsWith('.json') && /cds/i.test(name))
  .map((name) => path.join(dataDir, name));

function normalise(text) {
  return String(text || '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function tokens(text) {
  return new Set(normalise(text).split(' ').filter((word) => word.length > 2));
}

function similarity(a, b) {
  const left = tokens(a), right = tokens(b);
  const intersection = [...left].filter((word) => right.has(word)).length;
  const union = new Set([...left, ...right]).size;
  return union ? intersection / union : 0;
}

const questions = [];
const unreadableFiles = [];
for (const file of files) {
  let data;
  try { data = JSON.parse(fs.readFileSync(file, 'utf8')); } catch (error) { unreadableFiles.push({ file: path.basename(file), error: error.message }); continue; }
  for (const section of data.sections || []) {
    for (const question of section.questions || []) {
      questions.push({ file: path.basename(file), id: question.id, q: question.q });
    }
  }
}

const ids = new Map();
const text = new Map();
const missingIds = [];
for (const question of questions) {
  if (!question.id) {
    missingIds.push(question);
  } else {
    const idList = ids.get(question.id) || [];
    idList.push(question);
    ids.set(question.id, idList);
  }
  const key = normalise(question.q);
  if (key) {
    const textList = text.get(key) || [];
    textList.push(question);
    text.set(key, textList);
  }
}

const duplicates = (index) => [...index.values()].filter((items) => items.length > 1);
const nearDuplicates = [];
for (let i = 0; i < questions.length; i++) for (let j = i + 1; j < questions.length; j++) {
  if (normalise(questions[i].q) === normalise(questions[j].q)) continue;
  const score = similarity(questions[i].q, questions[j].q);
  if (score >= 0.82) nearDuplicates.push({ score: Number(score.toFixed(3)), left: questions[i], right: questions[j] });
}
const report = {
  files: files.map((file) => path.basename(file)),
  questionCount: questions.length,
  validUniqueIds: [...ids.values()].filter((items) => items.length === 1).length,
  missingIds: missingIds.length,
  reusedIds: duplicates(ids),
  duplicateIds: duplicates(ids),
  exactOrNormalisedTextDuplicates: duplicates(text),
  nearDuplicateCandidates: nearDuplicates,
  semanticDuplicateReview: 'NOT_PERFORMED: automated token overlap is a candidate filter, not a semantic verdict.',
  mathematicalStructureReview: 'NOT_PERFORMED: requires subject-aware review; no mathematical CDS set is currently included.',
  unreadableFiles,
};
console.log(JSON.stringify(report, null, 2));
if (report.reusedIds.length || report.exactOrNormalisedTextDuplicates.length || report.nearDuplicateCandidates.length) process.exitCode = 1;

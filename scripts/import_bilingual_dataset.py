#!/usr/bin/env python3
"""Audit and safely import authorized bilingual question data."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PREFIXES = ("upsi-", "alp-")
FAMILIES = {"upsi-": "UP SI", "alp-": "Railway"}
LANGUAGES = ("hi", "en")
PROVENANCE_FIELDS = (
    "sourceType",
    "sourceName",
    "sourceReference",
    "exam",
    "year",
    "shift",
)
QUESTION_LANGUAGE_FIELDS = frozenset({"q", "options"})
VALID_TRANSLATION_STATUSES = {
    "complete",
    "needs-review",
    "unmatched",
    "rejected",
}
PLACEHOLDER_VALUES = {"todo", "undefined", "null", "translation pending"}
PLACEHOLDER_PATTERN = re.compile(r"\[translate\]", re.IGNORECASE)


class ImportDataError(Exception):
    """Raised when an import or source file cannot be safely processed."""


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ImportDataError(f"Could not read JSON from {path}: {error}") from error


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _language_of(text: str) -> str:
    devanagari = sum("\u0900" <= char <= "\u097f" for char in text)
    latin = sum(len(word) for word in re.findall(r"[A-Za-z]+", text))
    has_english_word = re.search(r"[A-Za-z]{2,}", text) is not None
    if devanagari and devanagari >= latin:
        return "hi"
    if has_english_word:
        return "en"
    if devanagari:
        return "hi"
    return "neutral"


def _text_language(value: Any) -> str:
    if isinstance(value, dict):
        hi = _nonempty_text(value.get("hi"))
        en = _nonempty_text(value.get("en"))
        if hi and en:
            return "both"
        if hi:
            return "hi"
        if en:
            return "en"
        return "unknown"
    if isinstance(value, str) and value.strip():
        return _language_of(value)
    return "unknown"


def _valid_bilingual_value(value: Any) -> bool:
    return isinstance(value, dict) and all(
        _nonempty_text(value.get(language)) for language in LANGUAGES
    )


def _is_bilingual_record(question: Any) -> bool:
    return (
        isinstance(question, dict)
        and _valid_bilingual_value(question.get("q"))
        and isinstance(question.get("options"), list)
        and bool(question["options"])
        and all(_valid_bilingual_value(option) for option in question["options"])
    )


def _question_shape_errors(question: Any) -> list[str]:
    if not isinstance(question, dict):
        return ["question record is not an object"]

    q_value = question.get("q")
    if isinstance(q_value, str):
        if not q_value.strip():
            return ["question text is empty"]
    elif isinstance(q_value, dict):
        if not _valid_bilingual_value(q_value):
            return ["question hi/en fields must be non-empty strings"]
    else:
        return ["question text must be a string or hi/en object"]

    options = question.get("options")
    if not isinstance(options, list) or not options:
        return ["options must be a non-empty array"]
    for index, option in enumerate(options, start=1):
        if isinstance(option, str):
            if not option.strip():
                return [f"option {index} is empty"]
        elif isinstance(option, dict):
            if not _valid_bilingual_value(option):
                return [f"option {index} hi/en fields must be non-empty strings"]
        else:
            return [f"option {index} must be a string or hi/en object"]

    if "answer" not in question:
        return ["answer field is missing"]
    answer = question["answer"]
    if answer is not None and (
        type(answer) is not int or answer < 0 or answer >= len(options)
    ):
        return ["answer is not null or a valid zero-based option index"]

    status = question.get("translationStatus")
    if status is not None and (
        not isinstance(status, str) or status not in VALID_TRANSLATION_STATUSES
    ):
        return [f"unknown translationStatus: {status!r}"]
    if status == "complete" and not _is_bilingual_record(question):
        return ["translationStatus is complete but the question/options are not bilingual"]
    return []


def _target_file_paths(root: Path) -> list[Path]:
    data_dir = root / "data"
    return sorted(
        path
        for prefix in PREFIXES
        for path in data_dir.glob(f"{prefix}*.json")
    )


def _registry_by_file(root: Path) -> tuple[dict[str, dict[str, Any]], list[str]]:
    registry_path = root / "data" / "papers.json"
    registry = _read_json(registry_path)
    if not isinstance(registry, list):
        raise ImportDataError("data/papers.json must contain an array")

    by_file: dict[str, dict[str, Any]] = {}
    issues: list[str] = []
    seen_ids: set[str] = set()
    for entry in registry:
        if not isinstance(entry, dict):
            issues.append("papers.json contains a non-object paper entry")
            continue
        file_name = entry.get("file")
        paper_id = entry.get("id")
        if not isinstance(file_name, str):
            continue
        if not Path(file_name).name.startswith(PREFIXES):
            continue
        if file_name in by_file:
            issues.append(f"duplicate registry file entry: {file_name}")
        by_file[file_name] = entry
        if isinstance(paper_id, str):
            if paper_id in seen_ids:
                issues.append(f"duplicate registry paper ID: {paper_id}")
            seen_ids.add(paper_id)
    return by_file, issues


def _record_fingerprint(
    paper_id: str,
    section_index: int,
    section_name: str,
    question_number: int,
    question: dict[str, Any],
) -> str:
    metadata = {
        key: value
        for key, value in question.items()
        if key not in QUESTION_LANGUAGE_FIELDS
    }
    identity = {
        "paperId": paper_id,
        "sectionIndex": section_index,
        "sectionName": section_name,
        "questionNumber": question_number,
        "question": question.get("q"),
        "options": question.get("options"),
        "metadata": metadata,
    }
    payload = json.dumps(
        identity, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _iter_questions(paper_id: str, paper: dict[str, Any]):
    sections = paper.get("sections")
    if not isinstance(sections, list):
        return
    for section_index, section in enumerate(sections):
        if not isinstance(section, dict):
            continue
        section_name = section.get("name")
        questions = section.get("questions")
        if not isinstance(section_name, str) or not isinstance(questions, list):
            continue
        for question_number, question in enumerate(questions, start=1):
            if not isinstance(question, dict):
                continue
            yield {
                "paperId": paper_id,
                "sectionIndex": section_index,
                "sectionName": section_name,
                "questionNumber": question_number,
                "question": question,
            }


def audit_dataset(root: Path = ROOT, include_inventory: bool = True) -> dict[str, Any]:
    registry, registry_issues = _registry_by_file(root)
    files = _target_file_paths(root)
    actual_files = {f"data/{path.name}" for path in files}
    for registry_file in registry:
        if registry_file not in actual_files:
            registry_issues.append(f"registered target paper file is missing: {registry_file}")

    summary: dict[str, dict[str, int]] = {
        family: {
            "files": 0,
            "total": 0,
            "bilingual": 0,
            "hindi_only": 0,
            "english_only": 0,
            "language_neutral": 0,
            "invalid": 0,
        }
        for family in FAMILIES.values()
    }
    inventory: list[dict[str, Any]] = []
    seen_paper_ids: set[str] = set()
    question_ids: set[tuple[str, str]] = set()
    duplicate_question_ids: list[dict[str, str]] = []
    file_issues: list[str] = []
    loaded: dict[str, tuple[Path, dict[str, Any]]] = {}

    for path in files:
        family = FAMILIES[next(prefix for prefix in PREFIXES if path.name.startswith(prefix))]
        family_summary = summary[family]
        family_summary["files"] += 1
        try:
            paper = _read_json(path)
        except ImportDataError as error:
            file_issues.append(str(error))
            continue

        if not isinstance(paper, dict):
            file_issues.append(f"{path}: paper root must be an object")
            continue
        paper_id = paper.get("id")
        if not isinstance(paper_id, str) or not paper_id:
            file_issues.append(f"{path}: paper ID is missing")
            continue
        if paper_id in seen_paper_ids:
            file_issues.append(f"{path}: duplicate paper ID {paper_id!r}")
        seen_paper_ids.add(paper_id)
        loaded[paper_id] = (path, paper)

        registry_entry = registry.get(f"data/{path.name}")
        if registry_entry is None:
            file_issues.append(f"{path}: paper is not registered in data/papers.json")
        elif registry_entry.get("id") != paper_id:
            file_issues.append(
                f"{path}: registry ID {registry_entry.get('id')!r} does not match {paper_id!r}"
            )

        sections = paper.get("sections")
        if not isinstance(sections, list):
            file_issues.append(f"{path}: sections must be an array")
            continue
        for section_index, section in enumerate(sections):
            section_name = section.get("name") if isinstance(section, dict) else None
            questions = section.get("questions") if isinstance(section, dict) else None
            if not isinstance(section_name, str) or not isinstance(questions, list):
                file_issues.append(f"{path}: section {section_index + 1} is malformed")
                continue
            for question_number, question in enumerate(questions, start=1):
                family_summary["total"] += 1
                errors = _question_shape_errors(question)
                if errors:
                    family_summary["invalid"] += 1
                    language = "unknown"
                    status = "invalid"
                    question_object = question if isinstance(question, dict) else {}
                else:
                    question_object = question
                    is_bilingual = _is_bilingual_record(question_object)
                    language = "both" if is_bilingual else _text_language(question_object["q"])
                    if is_bilingual:
                        family_summary["bilingual"] += 1
                        status = "complete"
                    elif language == "hi":
                        family_summary["hindi_only"] += 1
                        status = question_object.get("translationStatus", "missing")
                    elif language == "en":
                        family_summary["english_only"] += 1
                        status = question_object.get("translationStatus", "missing")
                    elif language == "neutral":
                        family_summary["language_neutral"] += 1
                        status = question_object.get("translationStatus", "missing")
                    else:
                        family_summary["invalid"] += 1
                        status = "invalid"
                        errors = ["question text has no recognizable language"]

                question_id = question_object.get("id")
                if isinstance(question_id, str):
                    key = (paper_id, question_id)
                    if key in question_ids:
                        duplicate_question_ids.append(
                            {"paperId": paper_id, "questionId": question_id}
                        )
                    question_ids.add(key)

                if include_inventory:
                    options = question_object.get("options", [])
                    option_languages = [
                        _text_language(option) for option in options
                    ] if isinstance(options, list) else []
                    paper_meta = registry_entry or {}
                    inventory.append(
                        {
                            "filename": path.name,
                            "paperId": paper_id,
                            "exam": question_object.get("exam", paper_meta.get("exam")),
                            "year": question_object.get("year", paper_meta.get("year")),
                            "shift": question_object.get("shift", paper_meta.get("shift")),
                            "section": section_name,
                            "sectionIndex": section_index,
                            "questionNumber": question_number,
                            "questionId": question_id,
                            "sourceType": question_object.get("sourceType"),
                            "sourceName": question_object.get("sourceName"),
                            "sourceReference": question_object.get("sourceReference"),
                            "questionLanguage": language,
                            "optionLanguages": option_languages,
                            "translationStatus": status,
                            "invalidReasons": errors,
                        }
                    )

    report: dict[str, Any] = {
        "up_si": summary["UP SI"],
        "railway": summary["Railway"],
        "total": {
            key: sum(group[key] for group in summary.values())
            for key in (
                "files",
                "total",
                "bilingual",
                "hindi_only",
                "english_only",
                "language_neutral",
                "invalid",
            )
        },
        "registry": {
            "targetEntries": len(registry),
            "actualFiles": len(files),
            "issues": registry_issues + file_issues,
            "duplicateQuestionIds": duplicate_question_ids,
        },
        "inventory": inventory,
    }
    return report


def _source_language_hint(value: Any) -> str:
    if isinstance(value, str):
        return _language_of(value)
    if _valid_bilingual_value(value):
        return "both"
    return "unknown"


def create_template(root: Path = ROOT) -> dict[str, Any]:
    papers: list[dict[str, Any]] = []
    for path in _target_file_paths(root):
        paper = _read_json(path)
        if not isinstance(paper, dict) or not isinstance(paper.get("id"), str):
            raise ImportDataError(f"{path}: cannot create template for malformed paper")
        sections: list[dict[str, Any]] = []
        for section_index, section in enumerate(paper.get("sections", [])):
            if not isinstance(section, dict) or not isinstance(section.get("questions"), list):
                raise ImportDataError(f"{path}: malformed section {section_index + 1}")
            questions: list[dict[str, Any]] = []
            for question_number, question in enumerate(section["questions"], start=1):
                if not isinstance(question, dict):
                    raise ImportDataError(
                        f"{path}: malformed question {section_index + 1}/{question_number}"
                    )
                record: dict[str, Any] = {
                    "questionNumber": question_number,
                    "fingerprint": _record_fingerprint(
                        paper["id"],
                        section_index,
                        section["name"],
                        question_number,
                        question,
                    ),
                    "sourceLanguage": _source_language_hint(question.get("q")),
                    "optionSourceLanguages": [
                        _source_language_hint(option)
                        for option in question.get("options", [])
                    ],
                    "translationStatus": "needs-review",
                    "q": {"hi": "", "en": ""},
                    "options": [
                        {"hi": "", "en": ""}
                        for _ in question.get("options", [])
                    ],
                    "answer": question.get("answer"),
                }
                if isinstance(question.get("id"), str):
                    record["questionId"] = question["id"]
                for field in PROVENANCE_FIELDS:
                    record[field] = question.get(field)
                questions.append(record)
            sections.append(
                {
                    "sectionIndex": section_index,
                    "sectionName": section["name"],
                    "questions": questions,
                }
            )
        papers.append({"paperId": paper["id"], "sections": sections})
    return {"schemaVersion": 1, "papers": papers}


def _source_records(source: Any) -> tuple[list[dict[str, Any]], list[str]]:
    if not isinstance(source, dict) or source.get("schemaVersion") != 1:
        raise ImportDataError("source must be an object with schemaVersion: 1")
    papers = source.get("papers")
    if not isinstance(papers, list):
        raise ImportDataError("source.papers must be an array")

    records: list[dict[str, Any]] = []
    errors: list[str] = []
    seen_papers: set[str] = set()
    for paper_index, paper in enumerate(papers):
        if not isinstance(paper, dict):
            errors.append(f"source paper {paper_index + 1} is not an object")
            continue
        paper_id = paper.get("paperId")
        if not isinstance(paper_id, str) or not paper_id:
            errors.append(f"source paper {paper_index + 1} has no paperId")
            continue
        if paper_id in seen_papers:
            errors.append(f"duplicate source paper ID: {paper_id}")
        seen_papers.add(paper_id)
        sections = paper.get("sections")
        if not isinstance(sections, list):
            errors.append(f"{paper_id}: sections must be an array")
            continue
        for section_index, section in enumerate(sections):
            if not isinstance(section, dict):
                errors.append(f"{paper_id}: section {section_index + 1} is not an object")
                continue
            questions = section.get("questions")
            if not isinstance(questions, list):
                errors.append(f"{paper_id}: section {section_index + 1} questions must be an array")
                continue
            for position, record in enumerate(questions, start=1):
                records.append(
                    {
                        "paperId": paper_id,
                        "sectionIndex": section.get("sectionIndex", section_index),
                        "sectionName": section.get("sectionName", section.get("name")),
                        "position": position,
                        "record": record,
                    }
                )
    return records, errors


def _source_original_question(record: dict[str, Any]) -> Any:
    if "originalQuestion" in record:
        return record["originalQuestion"]
    q_value = record.get("q")
    if isinstance(q_value, dict):
        return q_value.get("hi") or q_value.get("en")
    return None


def _resolve_record(
    item: dict[str, Any],
    paper_records: list[dict[str, Any]],
    by_location: dict[tuple[str, int, int], dict[str, Any]],
    by_question_id: dict[tuple[str, str], list[dict[str, Any]]],
    by_fingerprint: dict[tuple[str, str], list[dict[str, Any]]],
) -> tuple[dict[str, Any] | None, str]:
    record = item["record"]
    if not isinstance(record, dict):
        return None, "source question record is not an object"
    paper_id = item["paperId"]
    question_id = record.get("questionId")
    if question_id is not None:
        if not isinstance(question_id, str) or not question_id:
            return None, "questionId must be a non-empty string"
        matches = by_question_id.get((paper_id, question_id), [])
        if len(matches) == 1:
            return matches[0], "questionId"
        return None, f"questionId {question_id!r} did not identify one canonical record"

    question_number = record.get("questionNumber")
    section_name = item.get("sectionName")
    section_index = item.get("sectionIndex")
    if type(question_number) is int and question_number > 0 and isinstance(section_name, str):
        if section_index is not None and (
            type(section_index) is not int or section_index < 0
        ):
            return None, "sectionIndex must be a non-negative integer"
        candidate = (
            by_location.get((paper_id, section_index, question_number))
            if section_index is not None
            else None
        )
        if candidate is None and section_index is None:
            named = [
                candidate
                for candidate in paper_records
                if candidate["sectionName"] == section_name
                and candidate["questionNumber"] == question_number
            ]
            if len(named) == 1:
                candidate = named[0]
            elif len(named) > 1:
                return None, "section name is ambiguous without sectionIndex"
        if candidate is None:
            return None, "paperId/section/questionNumber did not match a canonical record"
        if candidate["sectionName"] != section_name:
            return None, "section name does not match the canonical record"
        return candidate, "location"

    original_question = _source_original_question(record)
    if isinstance(original_question, str) and original_question:
        matches = [
            candidate
            for candidate in paper_records
            if _question_has_exact_text(candidate["question"].get("q"), original_question)
        ]
        if len(matches) == 1:
            return matches[0], "exact original question"
        if len(matches) > 1:
            fingerprint = record.get("fingerprint")
            if isinstance(fingerprint, str):
                by_hash = [
                    candidate
                    for candidate in matches
                    if candidate["fingerprint"] == fingerprint
                ]
                if len(by_hash) == 1:
                    return by_hash[0], "fingerprint"
            return None, "exact original question is not unique"

    fingerprint = record.get("fingerprint")
    if isinstance(fingerprint, str):
        matches = by_fingerprint.get((paper_id, fingerprint), [])
        if len(matches) == 1:
            return matches[0], "fingerprint"
        if len(matches) > 1:
            return None, "fingerprint is not unique"
    return None, "no stable ID, location, exact question, or unique fingerprint matched"


def _question_has_exact_text(value: Any, text: str) -> bool:
    if isinstance(value, str):
        return value == text
    if isinstance(value, dict):
        return any(value.get(language) == text for language in LANGUAGES)
    return False


def _placeholder(value: str) -> bool:
    normalized = value.strip().casefold()
    return (
        normalized in PLACEHOLDER_VALUES
        or PLACEHOLDER_PATTERN.search(value) is not None
    )


def _identity_errors(
    canonical: dict[str, Any],
    source: dict[str, Any],
    ref: dict[str, Any],
) -> tuple[list[str], int, int, int]:
    errors: list[str] = []
    missing_hindi = 0
    missing_english = 0
    provenance_mismatch = 0

    q_value = source.get("q")
    if not isinstance(q_value, dict):
        return ["q must be an object with hi and en fields"], 1, 1, 0
    for language in LANGUAGES:
        if not _nonempty_text(q_value.get(language)):
            errors.append(f"q.{language} is missing or empty")
            if language == "hi":
                missing_hindi += 1
            else:
                missing_english += 1
        elif _placeholder(q_value[language]):
            errors.append(f"q.{language} contains placeholder text")

    old_question = canonical.get("q")
    if isinstance(old_question, str):
        source_language = source.get("sourceLanguage")
        if source_language not in {"hi", "en", "neutral"}:
            source_language = _language_of(old_question)
        if source_language in {"hi", "en"}:
            if q_value.get(source_language) != old_question:
                errors.append(
                    f"original question text is not preserved exactly in q.{source_language}"
                )
        elif old_question not in (q_value.get("hi"), q_value.get("en")):
            errors.append("original question text is not preserved exactly")
    elif isinstance(old_question, dict):
        for language in LANGUAGES:
            old_text = old_question.get(language)
            if _nonempty_text(old_text) and q_value.get(language) != old_text:
                errors.append(f"existing q.{language} text would be changed")
    else:
        errors.append("canonical question has an unsupported q value")

    if "originalQuestion" in source:
        original_question = source["originalQuestion"]
        if isinstance(old_question, str):
            original_question_matches = original_question == old_question
        elif isinstance(old_question, dict):
            original_question_matches = any(
                original_question == old_question.get(language)
                for language in LANGUAGES
            )
        else:
            original_question_matches = False
        if not original_question_matches:
            errors.append("originalQuestion identity text does not match the canonical record")

    old_options = canonical.get("options")
    new_options = source.get("options")
    if not isinstance(old_options, list) or not isinstance(new_options, list):
        errors.append("options must be arrays")
        return errors, missing_hindi, missing_english, 0
    if len(new_options) != len(old_options):
        errors.append(
            f"option count mismatch: expected {len(old_options)}, received {len(new_options)}"
        )
        return errors, missing_hindi, missing_english, 0

    source_option_languages = source.get("optionSourceLanguages")
    if not isinstance(source_option_languages, list):
        source_option_languages = []
    for index, (old_option, new_option) in enumerate(zip(old_options, new_options), start=1):
        if not isinstance(new_option, dict):
            errors.append(f"option {index} must be an object with hi and en fields")
            missing_hindi += 1
            missing_english += 1
            continue
        for language in LANGUAGES:
            if not _nonempty_text(new_option.get(language)):
                errors.append(f"option {index} {language} text is missing or empty")
                if language == "hi":
                    missing_hindi += 1
                else:
                    missing_english += 1
            elif _placeholder(new_option[language]):
                errors.append(f"option {index} {language} contains placeholder text")

        if isinstance(old_option, str):
            expected_language = (
                source_option_languages[index - 1]
                if index - 1 < len(source_option_languages)
                else _language_of(old_option)
            )
            if expected_language in {"hi", "en"}:
                if new_option.get(expected_language) != old_option:
                    errors.append(
                        f"original option {index} is not preserved exactly in {expected_language}"
                    )
            elif old_option not in (new_option.get("hi"), new_option.get("en")):
                errors.append(f"original option {index} is not preserved exactly")
        elif isinstance(old_option, dict):
            for language in LANGUAGES:
                old_text = old_option.get(language)
                if _nonempty_text(old_text) and new_option.get(language) != old_text:
                    errors.append(f"existing option {index} {language} text would be changed")
        else:
            errors.append(f"canonical option {index} has an unsupported value")

    if "originalOptions" in source and source["originalOptions"] != old_options:
        errors.append("originalOptions identity does not match canonical option order")

    if "answer" not in source or source.get("answer") != canonical.get("answer"):
        errors.append("answer mismatch")

    for field in PROVENANCE_FIELDS:
        if field in canonical:
            if field not in source or source.get(field) != canonical[field]:
                provenance_mismatch += 1
        elif source.get(field) is not None:
            provenance_mismatch += 1
    if provenance_mismatch:
        errors.append("sourceType/sourceName/sourceReference/exam/year/shift mismatch")

    source_fingerprint = source.get("fingerprint")
    expected_fingerprint = ref.get("fingerprint")
    if source_fingerprint is not None and source_fingerprint != expected_fingerprint:
        errors.append("record fingerprint does not match the canonical question")

    return errors, missing_hindi, missing_english, provenance_mismatch


def _review_identity_errors(
    canonical: dict[str, Any],
    source: dict[str, Any],
    ref: dict[str, Any],
) -> tuple[list[str], int]:
    errors: list[str] = []
    if "answer" not in source or source.get("answer") != canonical.get("answer"):
        errors.append("answer mismatch")

    provenance_mismatch = sum(
        field not in source or source.get(field) != canonical.get(field)
        for field in PROVENANCE_FIELDS
        if field in canonical
    )
    provenance_mismatch += sum(
        field not in canonical and source.get(field) is not None
        for field in PROVENANCE_FIELDS
    )
    if provenance_mismatch:
        errors.append("sourceType/sourceName/sourceReference/exam/year/shift mismatch")

    source_fingerprint = source.get("fingerprint")
    if source_fingerprint is not None and source_fingerprint != ref.get("fingerprint"):
        errors.append("record fingerprint does not match the canonical question")
    return errors, provenance_mismatch


def _preserves_original_value(old: Any, new: Any) -> bool:
    if old == new:
        return True
    if isinstance(old, str):
        return isinstance(new, dict) and old in (new.get("hi"), new.get("en"))
    if isinstance(old, dict):
        return isinstance(new, dict) and all(
            not _nonempty_text(old.get(language))
            or new.get(language) == old.get(language)
            for language in LANGUAGES
        )
    return old == new


def _verify_integrity(
    before: dict[str, dict[str, Any]],
    after: dict[str, dict[str, Any]],
) -> dict[str, bool]:
    result = {
        "paperCountPreserved": len(before) == len(after),
        "paperIdsPreserved": list(before) == list(after),
        "sectionOrderPreserved": True,
        "questionCountPreserved": True,
        "questionOrderPreserved": True,
        "optionCountPreserved": True,
        "optionOrderPreserved": True,
        "answersPreserved": True,
        "provenancePreserved": True,
        "metadataPreserved": True,
    }
    if not result["paperIdsPreserved"]:
        return {key: False for key in result}

    for paper_id in before:
        old_paper = before[paper_id]
        new_paper = after[paper_id]
        old_sections = old_paper.get("sections", [])
        new_sections = new_paper.get("sections", [])
        if len(old_sections) != len(new_sections):
            result["sectionOrderPreserved"] = False
            result["questionCountPreserved"] = False
            continue
        for old_section, new_section in zip(old_sections, new_sections):
            if old_section.get("name") != new_section.get("name"):
                result["sectionOrderPreserved"] = False
            old_questions = old_section.get("questions", [])
            new_questions = new_section.get("questions", [])
            if len(old_questions) != len(new_questions):
                result["questionCountPreserved"] = False
                continue
            for old_question, new_question in zip(old_questions, new_questions):
                if not _preserves_original_value(old_question.get("q"), new_question.get("q")):
                    result["questionOrderPreserved"] = False
                old_options = old_question.get("options", [])
                new_options = new_question.get("options", [])
                if len(old_options) != len(new_options):
                    result["optionCountPreserved"] = False
                elif not all(
                    _preserves_original_value(old_option, new_option)
                    for old_option, new_option in zip(old_options, new_options)
                ):
                    result["optionOrderPreserved"] = False
                if old_question.get("answer") != new_question.get("answer"):
                    result["answersPreserved"] = False
                if any(
                    old_question.get(field) != new_question.get(field)
                    for field in PROVENANCE_FIELDS
                ):
                    result["provenancePreserved"] = False
                old_other = {
                    key: value
                    for key, value in old_question.items()
                    if key not in QUESTION_LANGUAGE_FIELDS
                }
                new_other = {
                    key: value
                    for key, value in new_question.items()
                    if key not in QUESTION_LANGUAGE_FIELDS
                }
                if old_other != new_other:
                    result["metadataPreserved"] = False
    return result


def _stage_and_replace(files: dict[Path, dict[str, Any]]) -> None:
    staged: dict[Path, Path] = {}
    originals = {path: path.read_bytes() for path in files}
    replaced: list[Path] = []
    try:
        for path, data in files.items():
            descriptor, temp_name = tempfile.mkstemp(
                prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
            )
            temp_path = Path(temp_name)
            staged[path] = temp_path
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                json.dump(data, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
        for path, temp_path in staged.items():
            os.replace(temp_path, path)
            replaced.append(path)
    except OSError:
        for path in replaced:
            descriptor, temp_name = tempfile.mkstemp(
                prefix=f".{path.name}.rollback.", suffix=".tmp", dir=path.parent
            )
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(originals[path])
            os.replace(temp_name, path)
        raise
    finally:
        for temp_path in staged.values():
            if temp_path.exists():
                temp_path.unlink()


def _validate_source_structure(
    source: Any,
    papers: dict[str, dict[str, Any]],
) -> list[str]:
    if not isinstance(source, dict) or not isinstance(source.get("papers"), list):
        return []

    errors: list[str] = []
    for source_paper in source["papers"]:
        if not isinstance(source_paper, dict):
            continue
        paper_id = source_paper.get("paperId")
        canonical = papers.get(paper_id) if isinstance(paper_id, str) else None
        if canonical is None:
            continue

        source_sections = source_paper.get("sections")
        canonical_sections = canonical.get("sections")
        if not isinstance(source_sections, list) or not isinstance(canonical_sections, list):
            errors.append(f"{paper_id}: source and canonical sections must be arrays")
            continue
        if len(source_sections) != len(canonical_sections):
            errors.append(
                f"{paper_id}: section count mismatch: expected {len(canonical_sections)}, "
                f"received {len(source_sections)}"
            )

        for section_index, source_section in enumerate(source_sections):
            if not isinstance(source_section, dict):
                errors.append(f"{paper_id}: section {section_index + 1} is not an object")
                continue
            source_section_index = source_section.get("sectionIndex", section_index)
            if type(source_section_index) is not int or source_section_index != section_index:
                errors.append(
                    f"{paper_id}: section order mismatch at section {section_index + 1}"
                )
            if section_index >= len(canonical_sections):
                continue

            canonical_section = canonical_sections[section_index]
            expected_name = canonical_section.get("name")
            source_name = source_section.get("sectionName", source_section.get("name"))
            if source_name != expected_name:
                errors.append(f"{paper_id}: section {section_index + 1} name/order mismatch")

            source_questions = source_section.get("questions")
            canonical_questions = canonical_section.get("questions")
            if not isinstance(source_questions, list) or not isinstance(canonical_questions, list):
                errors.append(
                    f"{paper_id}: questions in section {section_index + 1} must be arrays"
                )
                continue
            if len(source_questions) != len(canonical_questions):
                errors.append(
                    f"{paper_id}: question count mismatch in section {section_index + 1}: "
                    f"expected {len(canonical_questions)}, received {len(source_questions)}"
                )
            for position, source_record in enumerate(source_questions, start=1):
                if not isinstance(source_record, dict):
                    continue
                if (
                    "questionNumber" in source_record
                    and (
                        type(source_record["questionNumber"]) is not int
                        or source_record["questionNumber"] != position
                    )
                ):
                    errors.append(
                        f"{paper_id}: question order mismatch in section {section_index + 1} "
                        f"at position {position}"
                    )
                if position > len(canonical_questions):
                    continue
                expected_id = canonical_questions[position - 1].get("id")
                source_id = source_record.get("questionId")
                if source_id is not None and expected_id is not None and source_id != expected_id:
                    errors.append(
                        f"{paper_id}: question ID/order mismatch in section "
                        f"{section_index + 1} at position {position}"
                    )
    return errors


def import_dataset(
    root: Path,
    source: Any,
    apply: bool = False,
) -> dict[str, Any]:
    audit = audit_dataset(root, include_inventory=False)
    if audit["registry"]["issues"]:
        raise ImportDataError(
            "Existing data registry is inconsistent: "
            + "; ".join(audit["registry"]["issues"])
        )
    if audit["total"]["invalid"]:
        raise ImportDataError(
            f"Existing target dataset has {audit['total']['invalid']} invalid records; "
            "repair or review them before importing"
        )

    papers: dict[str, dict[str, Any]] = {}
    paths: dict[str, Path] = {}
    for path in _target_file_paths(root):
        paper = _read_json(path)
        paper_id = paper.get("id")
        if not isinstance(paper_id, str) or paper_id in papers:
            raise ImportDataError(f"{path}: missing or duplicate paper ID")
        papers[paper_id] = paper
        paths[paper_id] = path

    target_records: list[dict[str, Any]] = []
    by_location: dict[tuple[str, int, int], dict[str, Any]] = {}
    by_question_id: dict[tuple[str, str], list[dict[str, Any]]] = {}
    by_fingerprint: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for paper_id, paper in papers.items():
        for ref in _iter_questions(paper_id, paper):
            question = ref["question"]
            ref["fingerprint"] = _record_fingerprint(
                paper_id,
                ref["sectionIndex"],
                ref["sectionName"],
                ref["questionNumber"],
                question,
            )
            key = (paper_id, ref["sectionIndex"], ref["questionNumber"])
            by_location[key] = ref
            question_id = question.get("id")
            if isinstance(question_id, str):
                by_question_id.setdefault((paper_id, question_id), []).append(ref)
            by_fingerprint.setdefault((paper_id, ref["fingerprint"]), []).append(ref)
            target_records.append(ref)

    source_records, source_errors = _source_records(source)
    structure_errors = _validate_source_structure(source, papers)
    all_source_errors = source_errors + structure_errors
    report: dict[str, Any] = {
        "total_source_records": len(source_records),
        "matched": 0,
        "imported": 0,
        "would_import": 0,
        "already_bilingual": 0,
        "unmatched": 0,
        "rejected": 0,
        "needs_review": 0,
        "missing_hindi": 0,
        "missing_english": 0,
        "option_count_mismatch": 0,
        "answer_mismatch": 0,
        "provenance_mismatch": 0,
        "duplicates": 0,
        "errors": [
            {"status": "rejected", "reason": error}
            for error in all_source_errors
        ],
        "data_audit": {
            "up_si": audit["up_si"],
            "railway": audit["railway"],
            "total": audit["total"],
        },
    }
    report["rejected"] += len(all_source_errors)
    report["duplicates"] += sum(
        "duplicate" in error.casefold() for error in source_errors
    )

    target_by_paper: dict[str, list[dict[str, Any]]] = {}
    for ref in target_records:
        target_by_paper.setdefault(ref["paperId"], []).append(ref)

    matched_targets: set[tuple[str, int, int]] = set()
    updates: dict[tuple[str, int, int], dict[str, Any]] = {}
    simulated = copy.deepcopy(papers)

    for item in source_records:
        paper_id = item["paperId"]
        source_record = item["record"]
        if not isinstance(source_record, dict):
            report["rejected"] += 1
            report["errors"].append(
                {
                    "paperId": paper_id,
                    "sectionName": item.get("sectionName"),
                    "questionNumber": item.get("position"),
                    "status": "rejected",
                    "reason": "source question record is not an object",
                }
            )
            continue
        paper_refs = target_by_paper.get(paper_id, [])
        resolved, method = _resolve_record(
            item,
            paper_refs,
            by_location,
            by_question_id,
            by_fingerprint,
        )
        if resolved is None:
            report["unmatched"] += 1
            report["errors"].append(
                {
                    "paperId": paper_id,
                    "sectionName": item.get("sectionName"),
                    "questionNumber": (
                        source_record.get("questionNumber")
                        if isinstance(source_record, dict)
                        else None
                    ),
                    "status": "unmatched",
                    "reason": method,
                }
            )
            continue

        ref_key = (paper_id, resolved["sectionIndex"], resolved["questionNumber"])
        if ref_key in matched_targets:
            report["duplicates"] += 1
            report["rejected"] += 1
            report["errors"].append(
                {
                    "paperId": paper_id,
                    "sectionName": resolved["sectionName"],
                    "questionNumber": resolved["questionNumber"],
                    "status": "rejected",
                    "reason": "duplicate source record for the same canonical question",
                }
            )
            continue
        matched_targets.add(ref_key)
        report["matched"] += 1

        target_question = resolved["question"]
        status = source_record.get("translationStatus", "complete")
        if not isinstance(status, str) or status not in VALID_TRANSLATION_STATUSES:
            report["rejected"] += 1
            report["errors"].append(
                {
                    "paperId": paper_id,
                    "sectionName": resolved["sectionName"],
                    "questionNumber": resolved["questionNumber"],
                    "status": "rejected",
                    "reason": f"unknown translationStatus {status!r}",
                }
            )
            continue
        if status == "unmatched":
            report["unmatched"] += 1
            report["errors"].append(
                {
                    "paperId": paper_id,
                    "sectionName": resolved["sectionName"],
                    "questionNumber": resolved["questionNumber"],
                    "status": "unmatched",
                    "reason": "source explicitly marks this record unmatched",
                }
            )
            continue
        if status == "rejected":
            report["rejected"] += 1
            report["errors"].append(
                {
                    "paperId": paper_id,
                    "sectionName": resolved["sectionName"],
                    "questionNumber": resolved["questionNumber"],
                    "status": "rejected",
                    "reason": "source explicitly marks this record rejected",
                }
            )
            continue

        if _is_bilingual_record(target_question):
            if status == "complete":
                errors, missing_hi, missing_en, provenance_mismatch = _identity_errors(
                    target_question, source_record, resolved
                )
                report["missing_hindi"] += missing_hi
                report["missing_english"] += missing_en
                report["provenance_mismatch"] += bool(provenance_mismatch)
            else:
                errors, provenance_mismatch = _review_identity_errors(
                    target_question, source_record, resolved
                )
                source_options = source_record.get("options")
                if not isinstance(source_options, list):
                    errors.append("options must be an array")
                    report["option_count_mismatch"] += 1
                elif len(source_options) != len(target_question.get("options", [])):
                    errors.append(
                        f"option count mismatch: expected {len(target_question.get('options', []))}, "
                        f"received {len(source_options)}"
                    )
                    report["option_count_mismatch"] += 1
                report["answer_mismatch"] += any("answer mismatch" in error for error in errors)
                report["provenance_mismatch"] += bool(provenance_mismatch)
            if errors:
                report["rejected"] += 1
                report["errors"].append(
                    {
                        "paperId": paper_id,
                        "sectionName": resolved["sectionName"],
                        "questionNumber": resolved["questionNumber"],
                        "status": "rejected",
                        "reason": "; ".join(errors),
                    }
                )
                continue
            report["already_bilingual"] += 1
            continue

        if status == "needs-review":
            report["needs_review"] += 1
            review_errors = []
            source_question = source_record.get("q")
            if isinstance(source_question, dict):
                report["missing_hindi"] += not _nonempty_text(source_question.get("hi"))
                report["missing_english"] += not _nonempty_text(source_question.get("en"))
            else:
                report["missing_hindi"] += 1
                report["missing_english"] += 1
                review_errors.append("q must be an object with hi and en fields")
            source_options = source_record.get("options")
            if not isinstance(source_options, list):
                review_errors.append("options must be an array")
                report["option_count_mismatch"] += 1
            else:
                if len(source_options) != len(target_question.get("options", [])):
                    review_errors.append(
                        f"option count mismatch: expected {len(target_question.get('options', []))}, "
                        f"received {len(source_options)}"
                    )
                    report["option_count_mismatch"] += 1
                for option in source_options:
                    if isinstance(option, dict):
                        report["missing_hindi"] += not _nonempty_text(option.get("hi"))
                        report["missing_english"] += not _nonempty_text(option.get("en"))
                    else:
                        report["missing_hindi"] += 1
                        report["missing_english"] += 1
            identity_errors, provenance_mismatch = _review_identity_errors(
                target_question, source_record, resolved
            )
            review_errors.extend(identity_errors)
            report["answer_mismatch"] += any(
                "answer mismatch" in error for error in identity_errors
            )
            report["provenance_mismatch"] += bool(provenance_mismatch)
            if review_errors:
                report["rejected"] += 1
                report["errors"].append(
                    {
                        "paperId": paper_id,
                        "sectionName": resolved["sectionName"],
                        "questionNumber": resolved["questionNumber"],
                        "status": "rejected",
                        "reason": "; ".join(review_errors),
                    }
                )
            continue

        errors, missing_hi, missing_en, provenance_mismatch = _identity_errors(
            target_question, source_record, resolved
        )
        report["missing_hindi"] += missing_hi
        report["missing_english"] += missing_en
        report["provenance_mismatch"] += bool(provenance_mismatch)
        if any("option count mismatch" in error for error in errors):
            report["option_count_mismatch"] += 1
        if any("answer mismatch" in error for error in errors):
            report["answer_mismatch"] += 1
        if errors:
            report["rejected"] += 1
            report["errors"].append(
                {
                    "paperId": paper_id,
                    "sectionName": resolved["sectionName"],
                    "questionNumber": resolved["questionNumber"],
                    "status": "rejected",
                    "reason": "; ".join(errors),
                }
            )
            continue

        update = copy.deepcopy(target_question)
        update["q"] = {
            "hi": source_record["q"]["hi"],
            "en": source_record["q"]["en"],
        }
        update["options"] = [
            {"hi": option["hi"], "en": option["en"]}
            for option in source_record["options"]
        ]
        ref_section = simulated[paper_id]["sections"][resolved["sectionIndex"]]
        ref_section["questions"][resolved["questionNumber"] - 1] = update
        updates[ref_key] = update

    missing_targets = len(target_records) - len(matched_targets)
    if missing_targets > 0:
        report["unmatched"] += missing_targets
        report["errors"].append(
            {
                "status": "unmatched",
                "reason": f"{missing_targets} canonical questions were absent from the source",
            }
        )

    integrity = _verify_integrity(papers, simulated)
    report["integrity"] = integrity
    report["would_import"] = len(updates)
    can_apply = (
        not all_source_errors
        and report["unmatched"] == 0
        and report["rejected"] == 0
        and report["duplicates"] == 0
        and all(integrity.values())
    )
    report["applied"] = False
    if apply and can_apply and updates:
        changed_paper_ids = {paper_id for paper_id, _, _ in updates}
        _stage_and_replace(
            {paths[paper_id]: simulated[paper_id] for paper_id in changed_paper_ids}
        )
        report["imported"] = len(updates)
        report["applied"] = True
        after = audit_dataset(root, include_inventory=False)
        report["data_audit_after"] = {
            "up_si": after["up_si"],
            "railway": after["railway"],
            "total": after["total"],
        }
    report["status"] = (
        "PASS"
        if can_apply and report["needs_review"] == 0
        else "PASS WITH REVIEW"
        if can_apply
        else "FAIL"
    )
    return report


def _print_audit(report: dict[str, Any]) -> None:
    print("EXISTING DATA AUDIT")
    for label, key in (("UP SI", "up_si"), ("RAILWAY", "railway")):
        values = report[key]
        print(
            f"{label}: files={values['files']} total={values['total']} "
            f"bilingual={values['bilingual']} Hindi-only={values['hindi_only']} "
            f"English-only={values['english_only']} language-neutral={values['language_neutral']} "
            f"invalid={values['invalid']}"
        )
    print(f"TOTAL: {report['total']['total']}")
    issues = report["registry"]["issues"]
    print(f"papers.json registry: {'PASS' if not issues else 'FAIL'}")
    for issue in issues:
        print(f"  - {issue}")
    if report["registry"]["duplicateQuestionIds"]:
        print(f"Duplicate question IDs: {report['registry']['duplicateQuestionIds']}")


def _print_import(report: dict[str, Any], applied: bool) -> None:
    print("IMPORT VALIDATION REPORT")
    print(f"TOTAL SOURCE RECORDS: {report['total_source_records']}")
    for field, label in (
        ("matched", "MATCHED"),
        ("imported", "IMPORTED"),
        ("would_import", "WOULD IMPORT"),
        ("already_bilingual", "ALREADY BILINGUAL"),
        ("unmatched", "UNMATCHED"),
        ("rejected", "REJECTED"),
        ("missing_hindi", "MISSING HINDI"),
        ("missing_english", "MISSING ENGLISH"),
        ("option_count_mismatch", "OPTION COUNT MISMATCH"),
        ("answer_mismatch", "ANSWER MISMATCH"),
        ("provenance_mismatch", "PROVENANCE MISMATCH"),
        ("duplicates", "DUPLICATES"),
        ("needs_review", "NEEDS REVIEW"),
    ):
        print(f"{label}: {report[field]}")
    print(f"APPLIED: {'yes' if applied and report['applied'] else 'no'}")
    print(f"STATUS: {report['status']}")
    for issue in report["errors"]:
        print(f"  - {json.dumps(issue, ensure_ascii=False)}")


def _write_report(report: dict[str, Any], path: Path | None) -> None:
    if path:
        _write_json(path, report)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="project root")
    subparsers = parser.add_subparsers(dest="command", required=True)

    audit_parser = subparsers.add_parser("audit", help="audit all existing UP SI and ALP files")
    audit_parser.add_argument("--inventory", type=Path, help="write metadata-only inventory JSON")
    audit_parser.add_argument("--json", action="store_true", help="print machine-readable audit JSON")

    template_parser = subparsers.add_parser(
        "template", help="create a blank authorized-translation template without question text"
    )
    template_parser.add_argument("--output", type=Path, required=True)
    template_parser.add_argument("--force", action="store_true")

    import_parser = subparsers.add_parser(
        "import", help="validate an authorized bilingual dataset; writes only with --apply"
    )
    import_parser.add_argument("source", type=Path)
    import_parser.add_argument("--apply", action="store_true")
    import_parser.add_argument("--report", type=Path)
    import_parser.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    try:
        if args.command == "audit":
            report = audit_dataset(args.root, include_inventory=bool(args.inventory))
            if args.inventory:
                _write_json(args.inventory, {"records": report["inventory"]})
            if args.json:
                print(json.dumps(report, ensure_ascii=False, indent=2))
            else:
                _print_audit(report)
            return 1 if report["registry"]["issues"] or report["total"]["invalid"] else 0

        if args.command == "template":
            if args.output.exists() and not args.force:
                raise ImportDataError(
                    f"{args.output} already exists; pass --force to replace it"
                )
            template = create_template(args.root)
            _write_json(args.output, template)
            print(f"Wrote blank bilingual template: {args.output}")
            return 0

        source = _read_json(args.source)
        report = import_dataset(args.root, source, apply=args.apply)
        _write_report(report, args.report)
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            _print_import(report, args.apply)
        return 0 if report["status"] != "FAIL" else 1
    except ImportDataError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"ERROR: file operation failed: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

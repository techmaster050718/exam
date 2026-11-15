import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.import_bilingual_dataset import (
    audit_dataset,
    create_template,
    import_dataset,
)


class BilingualImporterTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        data_dir = self.root / "data"
        data_dir.mkdir()
        self.paper_path = data_dir / "upsi-test-paper.json"
        self.paper = {
            "id": "test-paper",
            "sections": [
                {
                    "name": "Section A",
                    "questions": [
                        {
                            "id": "stable-question-1",
                            "q": "Original question?",
                            "options": ["Original option A", "Original option B"],
                            "answer": 1,
                            "exam": "Test exam",
                            "year": 2024,
                            "shift": "Shift 1",
                            "sourceType": "official",
                            "sourceName": "Test source",
                            "sourceReference": "Page 1",
                            "customMetadata": {"preserve": True},
                        }
                    ],
                }
            ],
        }
        self.paper_path.write_text(json.dumps(self.paper), encoding="utf-8")
        (data_dir / "papers.json").write_text(
            json.dumps([{"id": "test-paper", "file": "data/upsi-test-paper.json"}]),
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def complete_template(self):
        source = create_template(self.root)
        record = source["papers"][0]["sections"][0]["questions"][0]
        record["translationStatus"] = "complete"
        record["q"] = {"hi": "मूल प्रश्न?", "en": "Original question?"}
        record["options"] = [
            {"hi": "मूल विकल्प A", "en": "Original option A"},
            {"hi": "मूल विकल्प B", "en": "Original option B"},
        ]
        return source, record

    def test_template_is_blank_and_import_changes_only_language_fields(self):
        template = create_template(self.root)
        record = template["papers"][0]["sections"][0]["questions"][0]
        self.assertEqual(record["q"], {"hi": "", "en": ""})
        self.assertEqual(record["options"], [{"hi": "", "en": ""}] * 2)

        source, _ = self.complete_template()
        before_bytes = self.paper_path.read_bytes()
        dry_run = import_dataset(self.root, source)
        self.assertEqual(self.paper_path.read_bytes(), before_bytes)
        self.assertEqual(dry_run["would_import"], 1)
        self.assertTrue(all(dry_run["integrity"].values()))

        applied = import_dataset(self.root, source, apply=True)
        self.assertTrue(applied["applied"])
        self.assertEqual(applied["imported"], 1)
        result = json.loads(self.paper_path.read_text(encoding="utf-8"))
        question = result["sections"][0]["questions"][0]
        self.assertEqual(question["q"], source["papers"][0]["sections"][0]["questions"][0]["q"])
        self.assertEqual(
            question["options"],
            source["papers"][0]["sections"][0]["questions"][0]["options"],
        )
        for field in ("answer", "exam", "year", "shift", "sourceType", "sourceName",
                      "sourceReference", "id", "customMetadata"):
            self.assertEqual(question[field], self.paper["sections"][0]["questions"][0][field])
        self.assertNotIn("translationStatus", question)
        self.assertEqual(audit_dataset(self.root)["total"]["bilingual"], 1)

    def test_rejects_option_answer_and_provenance_mismatches(self):
        mutations = (
            ("option_count_mismatch", lambda record: record.update(options=record["options"][:1])),
            ("answer_mismatch", lambda record: record.update(answer=0)),
            ("provenance_mismatch", lambda record: record.update(sourceName="Changed source")),
        )
        for field, mutate in mutations:
            with self.subTest(field=field):
                source, record = self.complete_template()
                mutate(record)
                report = import_dataset(self.root, source)
                self.assertEqual(report[field], 1)
                self.assertEqual(report["rejected"], 1)
                self.assertFalse(report["applied"])

    def test_rejects_missing_language_and_reordered_source_records(self):
        source, record = self.complete_template()
        record["q"]["hi"] = ""
        report = import_dataset(self.root, source)
        self.assertEqual(report["missing_hindi"], 1)
        self.assertEqual(report["rejected"], 1)

        source, record = self.complete_template()
        record["questionNumber"] = 2
        report = import_dataset(self.root, source)
        self.assertGreater(report["rejected"], 0)
        self.assertTrue(
            any("question order mismatch" in error.get("reason", "") for error in report["errors"])
        )
        self.assertFalse(report["applied"])

    def test_rejects_reordered_options_and_unmatched_paper_identity(self):
        source, record = self.complete_template()
        record["options"].reverse()
        report = import_dataset(self.root, source)
        self.assertEqual(report["rejected"], 1)
        self.assertFalse(report["applied"])

        source, _ = self.complete_template()
        source["papers"][0]["paperId"] = "different-paper"
        report = import_dataset(self.root, source)
        self.assertEqual(report["unmatched"], 2)
        self.assertTrue(
            any(error.get("status") == "unmatched" for error in report["errors"])
        )

    def test_duplicate_source_record_is_reported_and_blocks_apply(self):
        source, _ = self.complete_template()
        record = source["papers"][0]["sections"][0]["questions"][0]
        source["papers"][0]["sections"][0]["questions"].append(copy.deepcopy(record))
        report = import_dataset(self.root, source, apply=True)
        self.assertEqual(report["duplicates"], 1)
        self.assertGreater(report["rejected"], 0)
        self.assertFalse(report["applied"])

    def test_needs_review_still_validates_answer_and_provenance(self):
        source = create_template(self.root)
        record = source["papers"][0]["sections"][0]["questions"][0]
        record["answer"] = 0
        record["sourceName"] = "Changed source"
        report = import_dataset(self.root, source)
        self.assertEqual(report["answer_mismatch"], 1)
        self.assertEqual(report["provenance_mismatch"], 1)
        self.assertEqual(report["rejected"], 1)

    def test_non_object_source_record_is_rejected(self):
        source = create_template(self.root)
        source["papers"][0]["sections"][0]["questions"][0] = ["not", "an", "object"]
        report = import_dataset(self.root, source)
        self.assertEqual(report["rejected"], 1)
        self.assertEqual(report["unmatched"], 1)
        self.assertTrue(
            any(error.get("reason") == "source question record is not an object"
                for error in report["errors"])
        )

    def test_language_neutral_records_are_not_reported_as_invalid(self):
        paper = copy.deepcopy(self.paper)
        question = paper["sections"][0]["questions"][0]
        question["q"] = "x + 7 = 15, x = ?"
        question["options"] = ["3", "4"]
        self.paper_path.write_text(json.dumps(paper), encoding="utf-8")
        report = audit_dataset(self.root)
        self.assertEqual(report["up_si"]["language_neutral"], 1)
        self.assertEqual(report["up_si"]["invalid"], 0)

    def test_existing_bilingual_alp_records_are_regression_fixtures(self):
        root = Path(__file__).resolve().parents[1]
        source = create_template(root)
        for paper in source["papers"]:
            canonical_path = root / "data" / f"{paper['paperId']}.json"
            canonical = json.loads(canonical_path.read_text(encoding="utf-8"))
            for section, canonical_section in zip(paper["sections"], canonical["sections"]):
                for record, question in zip(section["questions"], canonical_section["questions"]):
                    if not isinstance(question.get("q"), dict):
                        continue
                    record["translationStatus"] = "complete"
                    record["q"] = copy.deepcopy(question["q"])
                    record["options"] = copy.deepcopy(question["options"])

        report = import_dataset(root, source)
        self.assertEqual(report["already_bilingual"], 17)
        self.assertEqual(report["needs_review"], 3718)
        self.assertEqual(report["would_import"], 0)
        self.assertTrue(all(report["integrity"].values()))


if __name__ == "__main__":
    unittest.main()

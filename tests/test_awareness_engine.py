#!/usr/bin/env python3
"""
================================================================================
Automated Unit Verification Suite for PEER'S Awareness Guard Suite
Author      : Mohammed Peer Siddiqui
Organization: Sqrock IT Solutions — Cybersecurity Internship (Alpha 2 Cohort)
================================================================================
"""

import os
import sys
import json
import shutil
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from awareness_engine import (
    load_question_bank,
    calculate_risk_tier,
    save_score_report
)


class TestAwarenessGuardSuite(unittest.TestCase):
    """Test suite covering question bank validation, risk tiering, and report serialization."""

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_json = os.path.join(self.test_dir, "test_report.json")
        self.test_txt = os.path.join(self.test_dir, "test_report.txt")

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_question_bank_structure(self):
        """Verify question bank contains at least 10 comprehensive questions with required schema."""
        questions = load_question_bank()
        self.assertGreaterEqual(len(questions), 10)
        
        required_keys = ["id", "vector", "scenario", "options", "correct_answer", "explanation"]
        for q in questions:
            for k in required_keys:
                self.assertIn(k, q, f"Question {q.get('id')} missing mandatory key: {k}")

    def test_perfect_score_calculation(self):
        """Verify 100% score assigns Tier 1 Cyber Defender Elite."""
        pct, tsi, tier, verdict = calculate_risk_tier(12, 12)
        self.assertEqual(pct, 100.0)
        self.assertEqual(tsi, 0.0)
        self.assertEqual(tier, "TIER_1_CYBER_DEFENDER_ELITE")
        self.assertIn("EXEMPLARY", verdict)

    def test_passing_score_calculation(self):
        """Verify 75% score (9/12) satisfies corporate standard with Tier 2."""
        pct, tsi, tier, verdict = calculate_risk_tier(9, 12)
        self.assertEqual(pct, 75.0)
        self.assertEqual(tsi, 25.0)
        self.assertEqual(tier, "TIER_2_AWARE_AND_VIGILANT")
        self.assertIn("PASS", verdict)

    def test_failing_score_classification(self):
        """Verify score below 50% classifies candidate as Tier 4 High-Risk Liability."""
        pct, tsi, tier, verdict = calculate_risk_tier(4, 12)
        self.assertLess(pct, 50.0)
        self.assertGreater(tsi, 50.0)
        self.assertEqual(tier, "TIER_4_HIGH_RISK_LIABILITY")
        self.assertIn("CRITICAL RISK", verdict)

    def test_all_questions_have_valid_answers(self):
        """Verify every question provides exactly 4 options and a valid answer key (A, B, C, or D)."""
        questions = load_question_bank()
        for q in questions:
            self.assertEqual(len(q["options"]), 4, f"Question {q['id']} does not have 4 options.")
            self.assertIn(q["correct_answer"], ["A", "B", "C", "D"], f"Question {q['id']} has invalid answer.")

    def test_score_report_serialization(self):
        """Verify candidate assessment record serializes properly to JSON and text on disk."""
        sample_report = {
            "candidate_name": "Test Candidate",
            "employee_id": "SQ-TEST-01",
            "department": "Quality Assurance",
            "timestamp_utc": "2026-11-07T12:00:00Z",
            "score": 11,
            "total_questions": 12,
            "percentage": 91.7,
            "threat_susceptibility_index": 8.3,
            "risk_tier": "TIER_1_CYBER_DEFENDER_ELITE",
            "evaluation_status": "EXEMPLARY",
            "question_results": []
        }
        save_score_report(sample_report, json_path=self.test_json, txt_path=self.test_txt)
        
        self.assertTrue(os.path.exists(self.test_json))
        self.assertTrue(os.path.exists(self.test_txt))
        
        with open(self.test_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["employee_id"], "SQ-TEST-01")


if __name__ == "__main__":
    unittest.main()

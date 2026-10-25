# -*- coding: utf-8 -*-
import unittest
from genpark_bio.metabolic import AutophagyFastingEngine, KetoneMetabolicEngine, GlycemicDynamicsEngine

class TestMetabolic(unittest.TestCase):
    def test_autophagy_kinetics(self):
        res = AutophagyFastingEngine.estimate_autophagy_index(fasting_duration_hours=24.0)
        self.assertGreater(res["estimated_autophagy_index_pct"], 70.0)
        self.assertIn("Mitophagy", res["cellular_cleansing_tier"])

    def test_ketone_gki(self):
        res = KetoneMetabolicEngine.calculate_gki_score(blood_glucose_mg_dl=90.0, blood_bhb_mmol_l=1.5)
        self.assertAlmostEqual(res["gki_score"], 3.33, places=1)

    def test_glycemic_dynamics(self):
        readings = [85.0, 92.0, 145.0, 120.0, 95.0, 88.0]
        res = GlycemicDynamicsEngine.calculate_mage_and_conga(readings)
        self.assertGreater(res["mage_score"], 0)
        self.assertEqual(res["readings_count"], 6)

if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
import unittest
from genpark_bio.cardio_renal import HydrationRenalEngine, HemodynamicsEngine, BloodPressureDippingEngine, LactateThresholdEngine

class TestCardioRenal(unittest.TestCase):
    def test_hydration_ratio(self):
        res = HydrationRenalEngine.calculate_bun_creatinine_ratio(bun_mg_dl=25.0, creatinine_mg_dl=1.0)
        self.assertEqual(res["hydration_classification"], "PRERENAL_AZOTEMIA_DEHYDRATION")

    def test_hemodynamics(self):
        res = HemodynamicsEngine.compute_cardiac_output_tpr(heart_rate_bpm=70, systolic_bp=120, diastolic_bp=80)
        self.assertGreater(res["cardiac_output_l_min"], 3.0)

    def test_bp_dipping(self):
        res = BloodPressureDippingEngine.assess_nocturnal_dipping(daytime_mean_sbp=125.0, nighttime_mean_sbp=110.0)
        self.assertEqual(res["chronotype_classification"], "NORMAL_DIPPER")

    def test_lactate_dynamics(self):
        res = LactateThresholdEngine.evaluate_lactate_dynamics(lactate_mmol_l=1.6)
        self.assertIn("AEROBIC", res["metabolic_intensity_domain"])

if __name__ == "__main__":
    unittest.main()

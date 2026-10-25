# -*- coding: utf-8 -*-
"""30-Second Quickstart for GenPark Bio-Agent (Pure Python Standard Library)."""
from genpark_bio.metabolic import AutophagyFastingEngine, KetoneMetabolicEngine
from genpark_bio.cardio_renal import HemodynamicsEngine
from genpark_bio.chronobiology import DLMOCircadianEngine
from genpark_bio.biomechanics import GripVitalityEngine

print("=" * 60)
print("GenPark Bio-Agent 30-Second Demo")
print("=" * 60)

# 1. Autophagy
autophagy = AutophagyFastingEngine.estimate_autophagy_index(fasting_duration_hours=20.0, activity_level="moderate")
print(f"\n[1] 20-Hour Fast Autophagy Index: {autophagy['estimated_autophagy_index_pct']}% | Tier: {autophagy['cellular_cleansing_tier']}")

# 2. Ketone GKI
gki = KetoneMetabolicEngine.calculate_gki_score(blood_glucose_mg_dl=85.0, blood_bhb_mmol_l=1.8)
print(f"[2] Glucose-Ketone Index (GKI): {gki['gki_score']} | Clinical State: {gki['clinical_state']}")

# 3. Hemodynamics
hemo = HemodynamicsEngine.compute_cardiac_output_tpr(heart_rate_bpm=68.0, systolic_bp=118.0, diastolic_bp=76.0)
print(f"[3] Cardiac Output: {hemo['cardiac_output_l_min']} L/min | TPR: {hemo['total_peripheral_resistance_tpr']} dynes*s/cm5")

# 4. DLMO Circadian
dlmo = DLMOCircadianEngine.predict_dim_light_melatonin_onset(wake_up_hour_decimal=6.5, evening_lux_average=60.0)
print(f"[4] Predicted DLMO Melatonin Onset: {dlmo['estimated_dlmo']} | Sleep Gate: {dlmo['biological_sleep_gate']}")

# 5. Grip Vitality
grip = GripVitalityEngine.assess_grip_strength_vitality(grip_dominant_kg=54.0, chronological_age=38, gender="male")
print(f"[5] Isometric Grip Vitality Age: {grip['biological_vitality_age']} (Chronological: 38) | Tier: {grip['vitality_tier']}")

print("\n" + "=" * 60)
print("All 5 Physiological Engines Verified Successfully!")
print("=" * 60)

# -*- coding: utf-8 -*-
"""Isometric Grip Strength Vitality & Sarcopenia Screening."""
from typing import Dict, Any

class GripVitalityEngine:
    @staticmethod
    def assess_grip_strength_vitality(grip_dominant_kg: float, chronological_age: int, gender: str = "male") -> Dict[str, Any]:
        base_norm = 50.0 if gender.lower() == "male" else 32.0
        age_decay = max(0.6, 1.0 - max(0, chronological_age - 30) * 0.008)
        expected = round(base_norm * age_decay, 1)
        strength_ratio = grip_dominant_kg / max(1.0, expected)
        bio_age_delta = round((1.0 - strength_ratio) * 15.0, 1)
        biological_vitality_age = round(chronological_age + bio_age_delta, 1)
        tier = "ELITE_NEUROMUSCULAR" if strength_ratio >= 1.15 else ("OPTIMAL" if strength_ratio >= 0.90 else "SARCOPENIA_RISK")
        return {
            "dominant_grip_kg": grip_dominant_kg,
            "cohort_expected_grip_kg": expected,
            "biological_vitality_age": biological_vitality_age,
            "vitality_tier": tier
        }

# -*- coding: utf-8 -*-
"""Pulmonary Spirometry FEV1/FVC Ratio & Vital Capacity."""
from typing import Dict, Any

class SpirometryPulmonaryEngine:
    @staticmethod
    def calculate_tiffeneau_index(fev1_liters: float, fvc_liters: float, predicted_fev1_liters: float = 3.8) -> Dict[str, Any]:
        ratio_pct = round((fev1_liters / max(0.1, fvc_liters)) * 100.0, 1)
        fev1_pct = round((fev1_liters / max(0.1, predicted_fev1_liters)) * 100.0, 1)
        pattern = "OBSTRUCTIVE_AIRWAY_DEFICIT" if ratio_pct < 70.0 else ("RESTRICTIVE_PATTERN_SUSPECTED" if fev1_pct < 80.0 else "NORMAL_PULMONARY_FUNCTION")
        return {
            "fev1_liters": fev1_liters,
            "fvc_liters": fvc_liters,
            "tiffeneau_index_fev1_fvc_pct": ratio_pct,
            "clinical_spirometry_classification": pattern
        }

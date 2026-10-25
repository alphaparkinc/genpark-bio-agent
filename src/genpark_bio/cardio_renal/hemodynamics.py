# -*- coding: utf-8 -*-
"""Hemodynamics & Cardiac Output Engine."""
from typing import Dict, Any

class HemodynamicsEngine:
    @staticmethod
    def compute_cardiac_output_tpr(heart_rate_bpm: float, systolic_bp: float, diastolic_bp: float, body_surface_area_m2: float = 1.9) -> Dict[str, Any]:
        map_mmhg = round(diastolic_bp + (systolic_bp - diastolic_bp) / 3.0, 1)
        pulse_pressure = round(systolic_bp - diastolic_bp, 1)
        stroke_volume_ml = round(max(35.0, min(140.0, pulse_pressure * 1.75)), 1)
        cardiac_output_l_min = round((stroke_volume_ml * heart_rate_bpm) / 1000.0, 2)
        cardiac_index = round(cardiac_output_l_min / max(1.0, body_surface_area_m2), 2)
        tpr_dynes = round((80.0 * (map_mmhg - 4.0)) / max(1.0, cardiac_output_l_min), 0)
        tier = "OPTIMAL_HEMODYNAMIC_EFFICIENCY" if 900 <= tpr_dynes <= 1400 and cardiac_index >= 2.5 else ("ELEVATED_VASCULAR_RESISTANCE" if tpr_dynes > 1400 else "HYPERDYNAMIC_STATE")
        return {
            "mean_arterial_pressure_map": map_mmhg,
            "estimated_stroke_volume_ml": stroke_volume_ml,
            "cardiac_output_l_min": cardiac_output_l_min,
            "cardiac_index_l_min_m2": cardiac_index,
            "total_peripheral_resistance_tpr": tpr_dynes,
            "hemodynamic_status": tier
        }

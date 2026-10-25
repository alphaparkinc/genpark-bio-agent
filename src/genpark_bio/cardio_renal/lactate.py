# -*- coding: utf-8 -*-
"""Continuous Lactate & Anaerobic Threshold Pacer."""
from typing import Dict, Any

class LactateThresholdEngine:
    @staticmethod
    def evaluate_lactate_dynamics(lactate_mmol_l: float, current_power_or_pace: float = 0.0) -> Dict[str, Any]:
        if lactate_mmol_l < 2.0:
            domain = "AEROBIC_LIPOLYTIC_BASE (LT1 / Zone 2)"
            fatigue_rate = "Negligible muscular acidosis; sustainable for multi-hour durations."
        elif lactate_mmol_l <= 4.0:
            domain = "MAXIMAL_LACTATE_STEADY_STATE (MLSS / Zone 3-4)"
            fatigue_rate = "Equilibrium between lactate production and oxidation; sustainable for 45-60 min."
        else:
            domain = "SEVERE_ANAEROBIC_GLYCOLYTIC (Above OBLA)"
            fatigue_rate = "Rapid proton (H+) accumulation and contractile failure within 2-10 minutes."
        return {
            "lactate_reading_mmol_l": lactate_mmol_l,
            "metabolic_intensity_domain": domain,
            "acidosis_projection": fatigue_rate,
            "governor_action": "THROTTLE_BACK_TO_LT1" if lactate_mmol_l > 4.0 else "SUSTAIN_TARGET_EFFORT"
        }

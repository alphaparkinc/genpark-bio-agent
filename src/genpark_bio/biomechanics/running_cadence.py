# -*- coding: utf-8 -*-
"""Biomechanical Running Cadence & Vertical Oscillation."""
from typing import Dict, Any

class RunningBiomechanicsEngine:
    @staticmethod
    def analyze_running_economy(step_cadence_spm: int, vertical_oscillation_cm: float, ground_contact_time_ms: int) -> Dict[str, Any]:
        estimated_stride_cm = max(50.0, (166.67 / max(100, step_cadence_spm)) * 100.0)
        vertical_ratio_pct = round((vertical_oscillation_cm / estimated_stride_cm) * 100.0, 1)
        tier = "ELITE_EFFICIENCY" if vertical_ratio_pct < 6.5 and step_cadence_spm >= 175 else ("GOOD_FORM" if vertical_ratio_pct < 8.5 else "EXCESSIVE_BOUNCE_BRAKING")
        return {
            "cadence_spm": step_cadence_spm,
            "vertical_oscillation_cm": vertical_oscillation_cm,
            "ground_contact_time_ms": ground_contact_time_ms,
            "vertical_ratio_pct": vertical_ratio_pct,
            "running_economy_tier": tier
        }

# -*- coding: utf-8 -*-
"""Circadian DLMO & Melatonin Dynamics."""
from typing import Dict, Any

class DLMOCircadianEngine:
    @staticmethod
    def predict_dim_light_melatonin_onset(wake_up_hour_decimal: float, evening_lux_average: float = 80.0) -> Dict[str, Any]:
        base_dlmo = (wake_up_hour_decimal + 14.0) % 24.0
        delay_minutes = min(120.0, (max(0.0, evening_lux_average - 30.0) / 10.0) * 15.0)
        adjusted_dlmo = (base_dlmo + (delay_minutes / 60.0)) % 24.0
        h = int(adjusted_dlmo)
        m = int((adjusted_dlmo - h) * 60)
        return {
            "wake_up_time": f"{int(wake_up_hour_decimal):02d}:{int((wake_up_hour_decimal%1)*60):02d}",
            "evening_lux": evening_lux_average,
            "estimated_dlmo": f"{h:02d}:{m:02d}",
            "biological_sleep_gate": f"{(h+2)%24:02d}:{m:02d}",
            "lighting_curfew": "Dim ambient lighting to < 10 lux 2 hours prior to DLMO."
        }

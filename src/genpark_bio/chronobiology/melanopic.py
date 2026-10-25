# -*- coding: utf-8 -*-
"""CIE S 026 Melanopic Lux & Circadian Entrainment."""
from typing import Dict, Any

class MelanopicLuxEngine:
    @staticmethod
    def calculate_equivalent_melanopic_lux(photopic_lux: float, light_source_type: str = "natural_daylight") -> Dict[str, Any]:
        mp_ratios = {"natural_daylight": 1.10, "cool_white_led_6500k": 0.92, "warm_incandescent_2700k": 0.45, "candlelight": 0.20}
        mp = mp_ratios.get(light_source_type, 0.70)
        eml = round(photopic_lux * mp * 1.218, 1)
        return {
            "light_source": light_source_type,
            "photopic_illuminance_lux": photopic_lux,
            "melanopic_photopic_ratio": mp,
            "equivalent_melanopic_lux_eml": eml,
            "iprgc_activation_tier": "HIGH_CIRCADIAN_STIMULATION" if eml >= 250 else ("LOW_CIRCADIAN_STIMULATION (Pre-sleep Safe)" if eml <= 50 else "MODERATE_AMBIENT")
        }

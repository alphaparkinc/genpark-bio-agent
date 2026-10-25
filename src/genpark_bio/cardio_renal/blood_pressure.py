# -*- coding: utf-8 -*-
"""Ambulatory Blood Pressure Dipping Sentinel."""
from typing import Dict, Any

class BloodPressureDippingEngine:
    @staticmethod
    def assess_nocturnal_dipping(daytime_mean_sbp: float, nighttime_mean_sbp: float, morning_surge_sbp: float = 0.0) -> Dict[str, Any]:
        dip_pct = round(((daytime_mean_sbp - nighttime_mean_sbp) / daytime_mean_sbp) * 100.0, 1)
        if dip_pct >= 20.0:
            category = "EXTREME_DIPPER"
            risk = "Elevated risk for anterior ischemic optic neuropathy and cerebral ischemic events."
        elif dip_pct >= 10.0:
            category = "NORMAL_DIPPER"
            risk = "Optimal physiological cardiovascular recovery profile."
        elif dip_pct >= 0.0:
            category = "NON_DIPPER"
            risk = "Elevated 24h cardiovascular burden and target organ damage risk."
        else:
            category = "REVERSE_DIPPER_RISER"
            risk = "Critical risk profile: severe nocturnal autonomic dysfunction and stroke risk."
        morning_surge_delta = round(max(0.0, morning_surge_sbp - nighttime_mean_sbp), 1) if morning_surge_sbp > 0 else 0.0
        return {
            "daytime_sbp": daytime_mean_sbp,
            "nighttime_sbp": nighttime_mean_sbp,
            "dipping_ratio_pct": dip_pct,
            "chronotype_classification": category,
            "morning_surge_mmhg": morning_surge_delta,
            "clinical_cardiovascular_assessment": risk
        }

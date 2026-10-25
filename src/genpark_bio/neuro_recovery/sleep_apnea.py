# -*- coding: utf-8 -*-
"""Nocturnal SpO2 Oxygen Desaturation & Sleep Apnea Screener."""
from typing import Dict, Any, List

class SleepApneaScreenerEngine:
    @staticmethod
    def calculate_odi3_index(spo2_readings: List[float], sleep_duration_hours: float) -> Dict[str, Any]:
        if not spo2_readings or sleep_duration_hours <= 0:
            return {"error": "Invalid readings or duration."}
        nadir = min(spo2_readings)
        mean_spo2 = round(sum(spo2_readings) / len(spo2_readings), 1)
        desat_events = 0
        baseline = spo2_readings[0]
        for val in spo2_readings:
            if baseline - val >= 3.0:
                desat_events += 1
                baseline = val
            elif val > baseline:
                baseline = val
        odi3 = round(desat_events / sleep_duration_hours, 1)
        tier = "SEVERE_SLEEP_APNEA_SUSPECTED" if odi3 >= 30.0 else ("MODERATE_OSA" if odi3 >= 15.0 else ("MILD_DESATURATION" if odi3 >= 5.0 else "NORMAL"))
        return {
            "mean_spo2_pct": mean_spo2,
            "nadir_spo2_pct": nadir,
            "odi3_events_per_hour": odi3,
            "clinical_tier": tier
        }

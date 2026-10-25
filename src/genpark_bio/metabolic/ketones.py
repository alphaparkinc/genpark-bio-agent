# -*- coding: utf-8 -*-
"""Blood Ketone & Glucose-Ketone Index (GKI) Calculator."""
from typing import Dict, Any

class KetoneMetabolicEngine:
    @staticmethod
    def calculate_gki_score(blood_glucose_mg_dl: float, blood_bhb_mmol_l: float) -> Dict[str, Any]:
        glucose_mmol = blood_glucose_mg_dl / 18.0182
        gki = round(glucose_mmol / max(0.05, blood_bhb_mmol_l), 2)
        if gki < 1.0: tier = "therapeutic_high"; status = "Highest Therapeutic Autophagy & Mitophagy"
        elif gki <= 3.0: tier = "moderate_autophagy"; status = "Robust Autophagy & Insulin Sensitivity"
        elif gki <= 9.0: tier = "mild_ketosis"; status = "Nutritional Ketosis Fat Adaptation"
        else: tier = "not_in_ketosis"; status = "Glycolytic Metabolism"
        return {"blood_glucose_mg_dl": blood_glucose_mg_dl, "blood_bhb_mmol_l": blood_bhb_mmol_l, "gki_score": gki, "metabolic_tier": tier, "clinical_state": status}

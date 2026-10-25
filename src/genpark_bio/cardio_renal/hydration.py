# -*- coding: utf-8 -*-
"""BUN & Creatinine Hydration Status Sentinel."""
from typing import Dict, Any

class HydrationRenalEngine:
    @staticmethod
    def calculate_bun_creatinine_ratio(bun_mg_dl: float, creatinine_mg_dl: float, egfr_ml_min: float = 90.0) -> Dict[str, Any]:
        ratio = round(bun_mg_dl / max(0.1, creatinine_mg_dl), 1)
        if ratio > 20.0:
            status = "PRERENAL_AZOTEMIA_DEHYDRATION"
            assessment = "Elevated ratio indicates significant intravascular volume contraction or high catabolic protein breakdown."
        elif ratio < 10.0:
            status = "LOW_RATIO_HEPATIC_OR_MALNUTRITION"
            assessment = "Low ratio suggests acute tubular necrosis, low protein intake, or overhydration."
        else:
            status = "PHYSIOLOGICAL_OPTIMAL"
            assessment = "Normal balanced renal perfusion and baseline hydration."
        return {
            "bun_mg_dl": bun_mg_dl,
            "creatinine_mg_dl": creatinine_mg_dl,
            "bun_creatinine_ratio": ratio,
            "egfr_ml_min": egfr_ml_min,
            "hydration_classification": status,
            "clinical_guidance": assessment
        }

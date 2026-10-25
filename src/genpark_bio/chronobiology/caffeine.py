# -*- coding: utf-8 -*-
"""Caffeine Adenosine Clearance & Half-life Pacer."""
from typing import Dict, Any

class CaffeineClearanceEngine:
    @staticmethod
    def calculate_caffeine_clearance(caffeine_doses_mg: list, elapsed_hours: float, cyp1a2_phenotype: str = "normal") -> Dict[str, Any]:
        # Half-life: Fast = 3.5h, Normal = 5.0h, Slow = 8.0h
        hl = 3.5 if cyp1a2_phenotype == "fast" else (8.0 if cyp1a2_phenotype == "slow" else 5.0)
        total_remaining = sum(dose * (0.5 ** (elapsed_hours / hl)) for dose in caffeine_doses_mg)
        total_remaining = round(total_remaining, 1)
        sleep_impact = "Significant Adenosine A2A Blockade (Sleep Disruption)" if total_remaining > 25.0 else "Minimal Sleep Architecture Impact"
        return {
            "cyp1a2_phenotype": cyp1a2_phenotype,
            "half_life_hours": hl,
            "residual_caffeine_mg": total_remaining,
            "bedtime_sleep_impact": sleep_impact
        }

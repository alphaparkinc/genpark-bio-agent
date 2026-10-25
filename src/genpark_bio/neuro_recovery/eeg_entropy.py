# -*- coding: utf-8 -*-
"""EEG Spectral Entropy & Neurocognitive Mental Fatigue Tracker."""
import math
from typing import Dict, Any

class EEGFatigueEngine:
    @staticmethod
    def calculate_theta_beta_and_entropy(theta_power_uv2: float, beta_power_uv2: float, alpha_power_uv2: float = 1.0) -> Dict[str, Any]:
        tbr = round(theta_power_uv2 / max(0.1, beta_power_uv2), 2)
        total_p = theta_power_uv2 + beta_power_uv2 + alpha_power_uv2
        p_theta = theta_power_uv2 / total_p
        p_beta = beta_power_uv2 / total_p
        p_alpha = alpha_power_uv2 / total_p
        entropy = - (p_theta * math.log(max(1e-6, p_theta)) + p_beta * math.log(max(1e-6, p_beta)) + p_alpha * math.log(max(1e-6, p_alpha)))
        entropy_normalized = round(min(1.0, max(0.0, entropy / math.log(3.0))), 2)
        fatigue_tier = "ACUTE_EXECUTIVE_EXHAUSTION" if tbr >= 4.0 else ("MODERATE_COGNITIVE_STRAIN" if tbr >= 2.5 else "OPTIMAL_ALERTNESS_FOCUS")
        return {
            "theta_beta_ratio_tbr": tbr,
            "normalized_spectral_entropy": entropy_normalized,
            "cognitive_fatigue_tier": fatigue_tier,
            "prefrontal_cortex_alertness": "HIGH" if tbr < 2.5 else "IMPAIRED"
        }

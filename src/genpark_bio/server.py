# -*- coding: utf-8 -*-
"""GenPark Bio-Agent Unified MCP JSON-RPC 2.0 Server (Zero External Dependencies)."""
import sys
import json
import logging
from typing import Dict, Any, List

from .metabolic import AutophagyFastingEngine, KetoneMetabolicEngine, GlycemicDynamicsEngine
from .cardio_renal import HydrationRenalEngine, HemodynamicsEngine, BloodPressureDippingEngine, LactateThresholdEngine
from .chronobiology import DLMOCircadianEngine, MelanopicLuxEngine, CaffeineClearanceEngine
from .neuro_recovery import EEGFatigueEngine, SleepApneaScreenerEngine, BinauralEntrainmentEngine, SaunaConditioningEngine
from .biomechanics import RunningBiomechanicsEngine, GripVitalityEngine, SpirometryPulmonaryEngine, PercussionTherapyEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

TOOLS = [
    {
        "name": "estimate_autophagy_index",
        "description": "Calculate cellular autophagy & mitophagy onset index from fasting duration and activity level.",
        "inputSchema": {
            "type": "object",
            "properties": {"fasting_duration_hours": {"type": "number"}, "baseline_ketone_mmol": {"type": "number"}, "activity_level": {"type": "string"}},
            "required": ["fasting_duration_hours"]
        }
    },
    {
        "name": "calculate_gki_score",
        "description": "Calculate Glucose-Ketone Index (GKI) cancer/longevity score from blood glucose (mg/dL) and BHB (mmol/L).",
        "inputSchema": {
            "type": "object",
            "properties": {"blood_glucose_mg_dl": {"type": "number"}, "blood_bhb_mmol_l": {"type": "number"}},
            "required": ["blood_glucose_mg_dl", "blood_bhb_mmol_l"]
        }
    },
    {
        "name": "calculate_mage_glucose_dynamics",
        "description": "Compute Mean Amplitude of Glycemic Excursions (MAGE) and coefficient of variation from CGM telemetry.",
        "inputSchema": {
            "type": "object",
            "properties": {"glucose_readings_mg_dl": {"type": "array", "items": {"type": "number"}}},
            "required": ["glucose_readings_mg_dl"]
        }
    },
    {
        "name": "calculate_bun_creatinine_ratio",
        "description": "Assess prerenal azotemia vs intrinsic renal strain from serum BUN and creatinine.",
        "inputSchema": {
            "type": "object",
            "properties": {"bun_mg_dl": {"type": "number"}, "creatinine_mg_dl": {"type": "number"}},
            "required": ["bun_mg_dl", "creatinine_mg_dl"]
        }
    },
    {
        "name": "compute_cardiac_output_tpr",
        "description": "Compute stroke volume (mL), cardiac output (L/min), and total peripheral resistance (TPR).",
        "inputSchema": {
            "type": "object",
            "properties": {"heart_rate_bpm": {"type": "number"}, "systolic_bp": {"type": "number"}, "diastolic_bp": {"type": "number"}},
            "required": ["heart_rate_bpm", "systolic_bp", "diastolic_bp"]
        }
    },
    {
        "name": "assess_nocturnal_dipping",
        "description": "Assess nocturnal blood pressure dipping percentage (Normal, Non-dipper, Reverse dipper).",
        "inputSchema": {
            "type": "object",
            "properties": {"daytime_mean_sbp": {"type": "number"}, "nighttime_mean_sbp": {"type": "number"}},
            "required": ["daytime_mean_sbp", "nighttime_mean_sbp"]
        }
    },
    {
        "name": "predict_dlmo_clock_time",
        "description": "Predict Dim Light Melatonin Onset (DLMO) clock time based on wake-up time and evening lux exposure.",
        "inputSchema": {
            "type": "object",
            "properties": {"wake_up_hour_decimal": {"type": "number"}, "evening_lux_average": {"type": "number"}},
            "required": ["wake_up_hour_decimal"]
        }
    },
    {
        "name": "calculate_equivalent_melanopic_lux",
        "description": "Calculate CIE S 026 Equivalent Melanopic Lux (EML) for circadian lighting entrainment.",
        "inputSchema": {
            "type": "object",
            "properties": {"photopic_lux": {"type": "number"}, "light_source_type": {"type": "string"}},
            "required": ["photopic_lux"]
        }
    },
    {
        "name": "calculate_caffeine_clearance",
        "description": "Model CYP1A2 pharmacokinetic caffeine clearance and bedtime adenosine receptor blockade.",
        "inputSchema": {
            "type": "object",
            "properties": {"caffeine_doses_mg": {"type": "array", "items": {"type": "number"}}, "elapsed_hours": {"type": "number"}, "cyp1a2_phenotype": {"type": "string"}},
            "required": ["caffeine_doses_mg", "elapsed_hours"]
        }
    },
    {
        "name": "compute_eeg_fatigue_entropy",
        "description": "Compute frontal Theta/Beta ratio (TBR) and Shannon spectral entropy for cognitive fatigue monitoring.",
        "inputSchema": {
            "type": "object",
            "properties": {"theta_power_uv2": {"type": "number"}, "beta_power_uv2": {"type": "number"}},
            "required": ["theta_power_uv2", "beta_power_uv2"]
        }
    },
    {
        "name": "assess_grip_vitality_age",
        "description": "Score isometric grip strength (kg) against normative cohorts to evaluate biological vitality age.",
        "inputSchema": {
            "type": "object",
            "properties": {"grip_dominant_kg": {"type": "number"}, "chronological_age": {"type": "integer"}, "gender": {"type": "string"}},
            "required": ["grip_dominant_kg", "chronological_age"]
        }
    }
]

DISPATCH = {
    "estimate_autophagy_index": (AutophagyFastingEngine, "estimate_autophagy_index"),
    "calculate_gki_score": (KetoneMetabolicEngine, "calculate_gki_score"),
    "calculate_mage_glucose_dynamics": (GlycemicDynamicsEngine, "calculate_mage_and_conga"),
    "calculate_bun_creatinine_ratio": (HydrationRenalEngine, "calculate_bun_creatinine_ratio"),
    "compute_cardiac_output_tpr": (HemodynamicsEngine, "compute_cardiac_output_tpr"),
    "assess_nocturnal_dipping": (BloodPressureDippingEngine, "assess_nocturnal_dipping"),
    "predict_dlmo_clock_time": (DLMOCircadianEngine, "predict_dim_light_melatonin_onset"),
    "calculate_equivalent_melanopic_lux": (MelanopicLuxEngine, "calculate_equivalent_melanopic_lux"),
    "calculate_caffeine_clearance": (CaffeineClearanceEngine, "calculate_caffeine_clearance"),
    "compute_eeg_fatigue_entropy": (EEGFatigueEngine, "calculate_theta_beta_and_entropy"),
    "assess_grip_vitality_age": (GripVitalityEngine, "assess_grip_strength_vitality")
}

def handle_rpc(line: str) -> str:
    try:
        req = json.loads(line)
        method = req.get("method")
        msg_id = req.get("id")

        if method == "initialize":
            res = {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-bio-agent", "version": "2.0.0"}
            }
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": res})
        elif method == "tools/list":
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}})
        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})
            if name not in DISPATCH:
                return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Method not found: {name}"}})
            cls_ref, fn_name = DISPATCH[name]
            result = getattr(cls_ref, fn_name)(**args)
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}})
        else:
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Unknown method: {method}"}})
    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}})

def run_test():
    init_res = json.loads(handle_rpc(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize"})))
    assert init_res["result"]["serverInfo"]["name"] == "genpark-bio-agent"
    list_res = json.loads(handle_rpc(json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})))
    assert len(list_res["result"]["tools"]) == len(TOOLS)
    call_res = json.loads(handle_rpc(json.dumps({
        "jsonrpc": "2.0", "id": 3, "method": "tools/call",
        "params": {"name": "estimate_autophagy_index", "arguments": {"fasting_duration_hours": 18.0}}
    })))
    assert "estimated_autophagy_index_pct" in call_res["result"]["content"][0]["text"]
    print("genpark-bio-agent: MCP self-test verified 100% PASS.")
    return True

if __name__ == "__main__":
    if "--test" in sys.argv:
        if run_test():
            sys.exit(0)
        sys.exit(1)
    for line in sys.stdin:
        if line.strip():
            out = handle_rpc(line)
            sys.stdout.write(out + "\n")
            sys.stdout.flush()

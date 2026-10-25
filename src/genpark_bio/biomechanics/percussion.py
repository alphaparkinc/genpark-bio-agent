# -*- coding: utf-8 -*-
"""Myofascial Trigger Point & Percussion Therapy Coach."""
from typing import Dict, Any

class PercussionTherapyEngine:
    @staticmethod
    def prescribe_percussion_therapy(target_muscle_group: str) -> Dict[str, Any]:
        muscle = target_muscle_group.lower()
        if any(k in muscle for k in ["quad", "glute", "hamstring"]):
            head = "Large Round Foam Ball"
            speed = "30 Hz (1800 RPM)"
            dur = 120
        elif any(k in muscle for k in ["neck", "trap"]):
            head = "Dampener Soft Head"
            speed = "20 Hz (1200 RPM)"
            dur = 60
        else:
            head = "Bullet or Flat Head"
            speed = "25 Hz (1500 RPM)"
            dur = 90
        return {"muscle": target_muscle_group, "attachment": head, "frequency": speed, "duration_seconds": dur}

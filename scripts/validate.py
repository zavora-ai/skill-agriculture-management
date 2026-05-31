#!/usr/bin/env python3
"""Estimate crop yield based on field conditions and NDVI readings."""
import json, sys

def estimate_yield(data):
    ndvi = data.get("ndvi", 0.5)
    rainfall_mm = data.get("rainfall_mm", 0)
    field_hectares = data.get("hectares", 1)
    crop = data.get("crop", "maize")

    base_yields = {"maize": 8, "wheat": 5, "rice": 6, "soybean": 3, "coffee": 2}
    base = base_yields.get(crop, 5)

    # NDVI health factor (0.2=stressed, 0.8=thriving)
    health = min(max((ndvi - 0.2) / 0.6, 0), 1)
    # Rainfall factor (optimal 400-800mm for most crops)
    rain_factor = min(max(rainfall_mm / 600, 0.3), 1.2)

    tonnes_per_ha = round(base * health * rain_factor, 2)
    total = round(tonnes_per_ha * field_hectares, 2)
    status = "healthy" if ndvi > 0.6 else "moderate" if ndvi > 0.4 else "stressed"

    return {
        "crop": crop,
        "ndvi_status": status,
        "yield_per_hectare_tonnes": tonnes_per_ha,
        "total_yield_tonnes": total,
        "recommendation": "Monitor closely" if status == "stressed" else "On track"
    }

if __name__ == "__main__":
    print(json.dumps(estimate_yield(json.loads(sys.argv[1])), indent=2))

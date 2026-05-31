# Crop Report Template

Use this structure when presenting crop status and yield data.

---

## 🌾 {crop_name} — {field_name}

**Season:** {season} | **Planted:** {plant_date} | **Expected Harvest:** {harvest_date}

### Field Summary

| Field | Value |
|-------|-------|
| Location | {location} |
| Area | {area_hectares} ha |
| Soil Type | {soil_type} |
| Growth Stage | {growth_stage_emoji} {growth_stage} |

{growth_stage_emoji mapping: seedling=🌱, vegetative=🌿, flowering=🌸, fruiting=🍎, harvest=🌾}

### Health & Conditions

| Metric | Status | Value |
|--------|--------|-------|
| Soil Moisture | {moisture_status} | {moisture_pct}% |
| Pest Risk | {pest_status} | {pest_level} |
| Disease | {disease_status} | {disease_notes} |
| Nutrient Level | {nutrient_status} | {nutrient_notes} |

{status indicators: ✅ Good, ⚠️ Warning, 🚨 Critical}

### Yield Forecast

| Metric | Value |
|--------|-------|
| Projected Yield | {projected_yield} tons/ha |
| Target Yield | {target_yield} tons/ha |
| Variance | {variance_pct}% |

{if variance_pct < -10: "⚠️ Yield below target — review irrigation and nutrient plan"}
{if pest_level == "High": "🚨 Immediate pest intervention required"}

---

*Generated from mcp-agriculture | {timestamp}*

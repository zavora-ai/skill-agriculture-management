# Agriculture Examples

## Example 1: "How are my crops doing?"
```
get_field_ndvi(field_id: "field_1") → {ndvi: 0.72, status: "healthy", zones: [{area: "north", ndvi: 0.45, alert: "stress"}]}
get_crop_health(field_id: "field_1") → {overall: "good", stressed_area: "12% in north zone"}
```
Response: "Field 1: Overall healthy (NDVI 0.72). ⚠️ North zone showing stress (0.45) — 12% of field. Check irrigation or pest damage."

## Example 2: "When should I sell my maize?"
```
get_commodity_price(commodity: "maize") → {price: 35, unit: "KES/kg", trend: "rising"}
get_best_sell_time(commodity: "maize", quantity: 5000) → {recommendation: "Hold 2 weeks", expected_price: 38}
```
Response: "Current: KES 35/kg (rising). Recommendation: Hold 2 weeks — expected KES 38/kg (+8.6%). Revenue: KES 190,000 vs 175,000 today."

## Example 3: "Is it safe to plant this week?"
```
get_forecast(location, days: 7) → {rain_days: [3, 5], temp_min: 18, frost_risk: false}
get_growing_degree_days(field_id) → {accumulated: 120, required: 100, ready: true}
```
Response: "✅ Safe to plant. No frost risk. Rain expected day 3 and 5 (good for germination). GDD accumulated: 120 (above 100 threshold)."

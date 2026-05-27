# Agriculture Tool Sequences (35 tools)

## Fields (5): list_fields, get_field, create_field, update_field, delete_field
## Crops (5): list_crops, get_crop, plant_crop, get_crop_calendar, log_harvest
## Activities (3): log_activity, list_activities, get_activity_summary
## Weather (4): get_forecast, get_historical_weather, get_weather_alerts, get_growing_degree_days
## Satellite (4): get_field_ndvi, get_crop_health, detect_anomalies, get_field_boundary
## Markets (5): get_commodity_price, get_price_history, get_market_trends, list_commodities, get_best_sell_time
## IoT (4): list_sensors, get_sensor_reading, get_soil_moisture, get_rainfall
## Yield (3): estimate_yield, get_harvest_history, compare_seasons
## Threats (2): get_pest_alerts, get_disease_risk

## Sequence: Morning Farm Check (4 calls)
```
1. get_forecast(location, days: 3) → weather outlook
2. get_weather_alerts(location) → any warnings
3. get_soil_moisture(field_id) → irrigation needed?
4. get_pest_alerts(region) → active threats
```

## Sequence: Harvest Decision (3 calls)
```
1. estimate_yield(field_id) → predicted quantity
2. get_commodity_price(crop) → current market price
3. get_best_sell_time(crop, quantity) → optimal timing
```

# Agriculture Cross-MCP Workflows

## Agriculture + Notifications: Weather Alerts
```
AGRI: get_weather_alerts(location) → frost tonight
NOTIFICATIONS: send_notification(recipient: farmer, title: "🥶 Frost Alert", priority: "critical")
```

## Agriculture + Finance: Harvest → Invoice
```
AGRI: log_harvest(field_id, crop: "maize", quantity: 5000)
AGRI: get_commodity_price("maize") → KES 35/kg
FINANCE: create_invoice(customer: "buyer", items: [{desc: "Maize 5t", price: 175000}])
```

## Agriculture + Analytics: Season Performance
```
AGRI: compare_seasons(field_id, years: [2024, 2025])
AGRI: get_harvest_history(field_id) → yields by year
ANALYTICS: query_metric(name: "farm_revenue", period: "12m")
```

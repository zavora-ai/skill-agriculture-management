# Agriculture Management Skill

> Farm operations for AI agents — field management, crop planning, weather intelligence, satellite monitoring (NDVI), commodity markets, IoT sensors, yield estimation, and pest/disease detection.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--agriculture-green)](https://github.com/zavora-ai/mcp-agriculture)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| Field Management | 1-3 | Track fields, crops, activities |
| Crop Planning | 3-4 | Optimal planting with weather window |
| Weather Intelligence | 2-4 | Forecasts, alerts, historical comparison |
| Satellite Health | 2-3 | NDVI, stress detection, anomalies |
| Market Intelligence | 2-4 | Prices, trends, optimal sell timing |
| IoT Monitoring | 2-3 | Soil moisture, rainfall, sensors |
| Yield Estimation | 2-3 | Predict harvest + compare seasons |
| Threat Detection | 2-3 | Pest alerts + disease risk |

### Revenue Impact
- **Market timing** — sell at optimal price (get_best_sell_time)
- **Yield optimization** — early stress detection via satellite
- **Loss prevention** — pest/disease/weather alerts before damage

## Installation

```bash
git clone https://github.com/zavora-ai/skill-agriculture-management.git \
  ~/.skills/skills/agriculture-management
```

## Requirements

**Required:** `mcp-agriculture` (35 tools)
**Cross-MCP:** `mcp-notifications` (weather alerts), `mcp-finance` (harvest invoicing), `mcp-analytics` (season performance)

## Success Criteria

| Metric | Target |
|--------|--------|
| Yield estimates | Within 15% of actual |
| Alert speed | Weather/pest alerts in 1 query |
| Market timing | Recommend optimal sell window |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)

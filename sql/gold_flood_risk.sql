CREATE OR REPLACE TABLE `capable-avatar-475900-j5.climate_gold.gold_flood_risk` AS

SELECT
    date,
    location,
    precipitation_mm,
    rainfall_3_day_total,
    rainfall_7_day_total,
    flood_risk,
    sustained_flood_risk,
    soil_saturation_risk,
    pond_overflow_risk

FROM `capable-avatar-475900-j5.climate_gold.weather_risk`;
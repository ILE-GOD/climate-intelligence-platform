CREATE OR REPLACE VIEW
`capable-avatar-475900-j5.climate_gold.gold_weather_summary`
AS

SELECT
    date,
    location,
    temperature_max,
    temperature_min,
    precipitation_mm,
    rainfall_3_day_total,
    rainfall_7_day_total,
    flood_risk,
    crop_stress,
    pond_overflow_risk,
    sustained_flood_risk,
    soil_saturation_risk
FROM
`capable-avatar-475900-j5.climate_gold.weather_risk`;
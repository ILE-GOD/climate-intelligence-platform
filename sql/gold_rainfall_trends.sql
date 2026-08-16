CREATE OR REPLACE VIEW
`capable-avatar-475900-j5.climate_gold.gold_rainfall_trends`
AS

SELECT
    date,
    location,
    precipitation_mm,
    rainfall_3_day_total,
    rainfall_7_day_total,
    flood_risk,
    sustained_flood_risk,
    soil_saturation_risk

FROM
`capable-avatar-475900-j5.climate_gold.weather_risk`;
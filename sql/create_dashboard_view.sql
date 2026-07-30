CREATE OR REPLACE VIEW
`capable-avatar-475900-j5.climate_gold.executive_dashboard`
AS

SELECT
    date,
    location,
    temperature_max,
    temperature_min,
    precipitation_mm,

    CAST(flood_risk AS STRING) AS flood_risk,
    CAST(crop_stress AS STRING) AS crop_stress,
    CAST(pond_overflow_risk AS STRING) AS pond_overflow_risk,
    CAST(sustained_flood_risk AS STRING) AS sustained_flood_risk,
    CAST(soil_saturation_risk AS STRING) AS soil_saturation_risk,

    rainfall_3_day_total,
    rainfall_7_day_total,
    temperature_change,
    latitude,
    longitude,
    extracted_at

FROM
`capable-avatar-475900-j5.climate_gold.weather_risk`;
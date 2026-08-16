CREATE OR REPLACE VIEW
`capable-avatar-475900-j5.climate_gold.gold_agriculture_advisory`
AS

SELECT
    date,
    location,
    temperature_max,
    temperature_min,
    precipitation_mm,
    rainfall_3_day_total,
    rainfall_7_day_total,
    crop_stress,

    CASE
        WHEN crop_stress = 'HIGH'
            THEN 'Provide shade and increase irrigation monitoring'

        WHEN crop_stress = 'MEDIUM'
            THEN 'Monitor crop water requirements'

        ELSE
            'Normal agricultural conditions'
    END AS agricultural_advisory

FROM
`capable-avatar-475900-j5.climate_gold.weather_risk`;
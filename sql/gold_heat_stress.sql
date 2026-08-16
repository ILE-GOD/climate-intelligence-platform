CREATE OR REPLACE VIEW
`capable-avatar-475900-j5.climate_gold.gold_heat_stress`
AS

SELECT
    date,
    location,
    temperature_max,
    temperature_min,
    temperature_change,

    crop_stress AS heat_stress_level,

    CASE
        WHEN temperature_max >= 35
            THEN 'Extreme heat stress risk'

        WHEN temperature_max >= 30
            THEN 'Moderate heat stress risk'

        ELSE
            'Low heat stress risk'
    END AS heat_stress_advisory

FROM
`capable-avatar-475900-j5.climate_gold.weather_risk`;
CREATE OR REPLACE VIEW
`capable-avatar-475900-j5.climate_gold.gold_aquaculture_advisory`
AS

SELECT
    date,
    location,
    precipitation_mm,
    rainfall_3_day_total,
    rainfall_7_day_total,
    pond_overflow_risk,

    CASE
        WHEN pond_overflow_risk = 'HIGH'
            THEN 'Inspect pond embankments and prepare overflow controls'

        WHEN pond_overflow_risk = 'MEDIUM'
            THEN 'Monitor pond water levels and drainage channels'

        ELSE
            'Normal pond conditions'
    END AS aquaculture_advisory

FROM
`capable-avatar-475900-j5.climate_gold.weather_risk`;
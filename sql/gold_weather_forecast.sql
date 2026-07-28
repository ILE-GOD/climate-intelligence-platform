CREATE OR REPLACE TABLE
`capable-avatar-475900-j5.climate_gold.gold_weather_forecast`
AS

SELECT
    date,
    location,
    temperature_max,
    temperature_min,
    precipitation_mm,
    temperature_change

FROM
`capable-avatar-475900-j5.climate_gold.weather_risk`

ORDER BY
    date;
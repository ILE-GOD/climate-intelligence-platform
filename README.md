# 🌍 Climate Intelligence & Flood Early Warning Platform

> A production-inspired Data Engineering platform that automates weather data ingestion, validation, transformation, climate risk assessment, and analytics using Apache Airflow, Docker, Google Cloud Storage, BigQuery, and Looker Studio.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Google Cloud Storage](https://img.shields.io/badge/Google%20Cloud-Storage-blue)
![BigQuery](https://img.shields.io/badge/Google-BigQuery-blue)
![Looker Studio](https://img.shields.io/badge/Looker-Studio-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Executive Summary

Climate-related disasters such as flooding, prolonged rainfall, and heat stress continue to threaten agriculture, aquaculture, infrastructure, food security, and public safety. Although weather information is publicly available, many organizations still lack automated systems that transform raw weather observations into actionable insights.

The **Climate Intelligence & Flood Early Warning Platform** is a production-inspired Data Engineering project that automates the complete weather analytics lifecycle from data extraction to decision-ready dashboards.

The project aims to:

- Build an end-to-end cloud-based ETL pipeline
- Implement a Medallion Architecture (Bronze, Silver, Gold)
- Automate weather data ingestion from the Open-Meteo API
- Validate and transform raw weather datasets
- Engineer climate and rainfall features
- Calculate flood and agricultural risk indicators
- Store analytics-ready datasets in BigQuery
- Build interactive dashboards in Looker Studio
- Demonstrate production-ready Data Engineering best practices

Instead of only reporting weather conditions, this platform provides actionable recommendations that support informed decision-making.

---

# 🌍 Business Problem

Flooding and changing weather patterns are becoming more frequent across many regions, particularly in developing countries.

These events affect multiple sectors, such as; Agriculture, Aquaculture, Food Production, Urban Planning, Disaster Management and Public Health.

Common challenges include: Crop losses, Fish pond overflow, Soil erosion, Heat stress, Waterlogging, Transportation disruption, Economic losses etc.

Although weather data is publicly available, organizations often struggle to:

- Collect it automatically
- Validate data quality
- Process large volumes consistently
- Generate meaningful risk indicators
- Deliver timely insights for decision-making

---

# 💡 Solution Overview

This project addresses these challenges by transforming raw weather observations into analytics-ready datasets and actionable climate intelligence. Unlike simple weather dashboards, this platform focuses on **decision support** by generating indicators such as:

- Flash Flood Risk
- Sustained Flood Risk
- Soil Saturation Risk
- Crop Heat Stress
- Pond Overflow Risk
- Rainfall Trends

---

# 🏗 Solution Architecture

<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/2531f028-634f-4d3d-a12c-57468d21fadb" />

---

# 🔄 End-to-End Pipeline Workflow

<img width="948" height="1659" alt="Image" src="https://github.com/user-attachments/assets/5e42ddf4-8761-4f4d-8e4f-ac29b804e4c6" />

---

# 🚀 Key Features

- ✅ Apache Airflow orchestration
- ✅ Dockerized deployment
- ✅ Incremental processing
- ✅ Timestamped datasets
- ✅ Configurable locations
- ✅ Automated validation
- ✅ Feature engineering
- ✅ Flood risk calculation
- ✅ Google Cloud Storage integration
- ✅ BigQuery data warehouse
- ✅ Looker Studio dashboards
- ✅ Production-inspired Medallion Architecture

---

# ⚙️ Technology Stack

| Category | Technology |
|------------|------------|
| Programming Language | Python 3.11 |
| Data Processing | Pandas |
| Workflow Orchestration | Apache Airflow |
| Containerization | Docker & Docker Compose |
| Cloud Storage | Google Cloud Storage (GCS) |
| Data Warehouse | Google BigQuery |
| Dashboard & BI | Looker Studio |
| Cloud SDK | Google Cloud SDK |
| Weather API | Open-Meteo API |
| Configuration | python-dotenv |
| File Format | JSON, Parquet |
| Version Control | Git & GitHub |

---

# 🌐 Data Sources

The platform currently consumes weather data from publicly available APIs and is designed to support multiple weather providers such as; Open-Meteo API, NASA POWER API, OpenWeather API, NiMet API | Nigerian Weather, NIHSA Flood Data.
Open-Meteo API used provides data such: Current Weather, Daily Forecast, Rainfall, Temperature, Humidity, Wind, Forecast Models

| Source | Purpose | Documentation |
|---------|----------|---------------|
| Open-Meteo API | Weather forecasts | https://open-meteo.com/en/docs |
| NASA POWER *(Future)* | Climate data | https://power.larc.nasa.gov |
| OpenWeather *(Future)* | Weather observations | https://openweathermap.org/api |
| NiMet *(Future)* | Nigerian weather | https://nimet.gov.ng |

---

# 📦 Data Model (Medallion Architecture)

| Layer | Purpose | Storage | Format | Key Outputs |
|--------|---------|---------|--------|-------------|
| 🥉 **Bronze** | Stores immutable raw weather API responses for auditing and historical tracking. | `data/raw/` | JSON | Timestamped raw weather data with metadata (location, coordinates, extraction time). |
| 🥈 **Silver** | Stores validated, cleaned, and feature-engineered datasets for downstream processing. | `data/processed/` | Parquet | Clean weather data, engineered features, flood risk indicators, and metadata. |
| 🥇 **Gold** | Stores analytics-ready datasets optimized for reporting and decision support. | Google BigQuery (`climate_gold.weather_risk`) | BigQuery Table | Business-ready datasets for SQL analytics, dashboards, reporting, and climate intelligence. |

---

# 📊 Dataset Schema

The final analytical dataset contains the following fields.

| Column | Type | Description |
|----------|----------|-------------|
| date | DATE | Forecast date |
| location | STRING | Selected location |
| latitude | FLOAT | Latitude |
| longitude | FLOAT | Longitude |
| extracted_at | TIMESTAMP | Extraction timestamp |
| temperature_max | FLOAT | Daily maximum temperature |
| temperature_min | FLOAT | Daily minimum temperature |
| precipitation_mm | FLOAT | Daily rainfall |
| rainfall_3_day_total | FLOAT | Rolling 3-day rainfall |
| rainfall_7_day_total | FLOAT | Rolling 7-day rainfall |
| temperature_change | FLOAT | Day-to-day temperature difference |
| flood_risk | STRING | Flash flood indicator |
| sustained_flood_risk | STRING | Long rainfall flood indicator |
| soil_saturation_risk | STRING | Soil saturation level |
| crop_stress | STRING | Heat stress indicator |
| pond_overflow_risk | STRING | Aquaculture flood risk |

---

# 🌧️ Risk Assessment Logic

Convertion of observations into actionable environmental indicators.

| Indicator | Threshold | Risk Level |
|-----------|-----------|------------|
| Flash Flood Risk | <40 mm | NORMAL |
| | 40–74 mm | WARNING |
| | ≥75 mm | CRITICAL |
| Sustained Flood Risk | <60 mm | NORMAL |
| | 60–99 mm | WARNING |
| | ≥100 mm | CRITICAL |
| Soil Saturation | <60 mm | LOW |
| | 60–99 mm | MEDIUM |
| | ≥100 mm | HIGH |
| Crop Heat Stress | <30°C | LOW |
| | 30–34°C | MEDIUM |
| | ≥35°C | HIGH |
| Pond Overflow | <40 mm | LOW |
| | 40–74 mm | MEDIUM |
| | ≥75 mm | HIGH |

---

# 💻 Installation Guide

### Prerequisites

- Python 3.11+
- Docker Desktop
- Git
- Google Cloud SDK

### Clone the Repository

```bash
git clone https://github.com/ILE-GOD/climate-intelligence-platform.git
cd climate-intelligence-platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file and add your Google Cloud credentials and project configuration.

### Start the Project

```bash
docker compose up -d
```

Open Apache Airflow:

```
http://localhost:8080
```

Trigger the **climate_intelligence_pipeline** DAG.

### Pipeline Output

- Raw JSON → `data/raw/`
- Processed Parquet → `data/processed/`
- Cloud Storage → Google Cloud Storage
- Data Warehouse → BigQuery (`climate_gold`)
- Dashboards → Looker Studio

---

# 📸 Screenshots

## Apache Airflow

> Added screenshot

<img width="1911" height="875" alt="Image" src="https://github.com/user-attachments/assets/83a1531b-1482-45f2-8681-d9b10905d14f" />

- Successful DAG Graph Run and Task Status

---

## Google Cloud Storage

> Added screenshot

<img width="1917" height="852" alt="Image" src="https://github.com/user-attachments/assets/5790fda1-ec32-4b9c-8d3a-4cba9af14ed5" />

- Bucket Showing successful Uploaded Parquet Files

---

## BigQuery Query Results

> Added screenshot

<img width="1920" height="872" alt="Image" src="https://github.com/user-attachments/assets/87583cdc-f1fe-48c8-a2e1-78a5f7b2fae3" />

- Climate Gold Table in Bigquery

---

## Looker Studio Dashboard

> Added screenshot

<img width="1178" height="692" alt="Image" src="https://github.com/user-attachments/assets/bf69c2f1-192f-41fd-830e-e2dae324fa18" />

Visuals showing: 

- Flood Risk by Date
- Rainfall Trend
- Temperature Trend
- Crop Stress
- Pond Overflow Risk

## 📊 Dashboard

[View the Live Climate Intelligence Dashboard](https://datastudio.google.com/reporting/f04d0d6e-329c-47d2-8ac8-60de333a968c)

---

# 🛣️ Project Roadmap

| Feature | Status |
|----------|--------|
| Project Setup | ✅ |
| Docker Environment | ✅ |
| Apache Airflow | ✅ |
| Weather API Integration | ✅ |
| Data Validation | ✅ |
| Feature Engineering | ✅ |
| Risk Calculation | ✅ |
| Incremental Processing | ✅ |
| Google Cloud Storage | ✅ |
| BigQuery Integration | ✅ |
| Looker Studio Dashboard | 🚧 |
| Data Quality Tests | 🚧 |
| GitHub Actions CI/CD | 🚧 |
| dbt Transformations | 🚧 |
| Great Expectations | 🚧 |
| Terraform Deployment | 🚧 |
| Kubernetes Deployment | 🚧 |
| Machine Learning Flood Prediction | 🚧 |
| Real-Time Streaming (Kafka) | 🚧 |

---

# 🚀 Future Enhancements

Planned improvements include:
- Apache Kafka
- dbt transformations
- Great Expectations validation
- Terraform Infrastructure as Code
- Kubernetes deployment
- Machine Learning flood prediction
- Rainfall anomaly detection
- WhatsApp flood alerts
- Email alert service
- Interactive GIS maps

---

# 💼 Skills Demonstrated

- Python
- Apache Airflow
- Docker
- Google Cloud Platform
- BigQuery
- Google Cloud Storage
- Pandas
- ETL/ELT Pipelines
- Medallion Architecture
- Data Warehousing
- Looker Studio
- Git & GitHub

---

# 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project with attribution.

---

# 👨‍💻 Author

## Daniel Okom

**Data Engineer | Cloud Data Engineer | Data Analyst**

📧 Email

```
okomilechukwudaniel@gmail.com
```

🔗 GitHub: https://github.com/ILE-GOD

🔗 LinkedIn: https://www.linkedin.com/in/daniel-okom-748798242

---

> **Demonstration of modern Data Engineering practices for climate intelligence and flood early warning.**
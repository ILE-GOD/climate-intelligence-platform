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

The platform:

- Automatically extracts weather data from public APIs
- Validates incoming data before processing
- Applies data cleaning and feature engineering
- Calculates climate and flood risk indicators
- Stores data using a Medallion Architecture
- Loads analytical datasets into Google BigQuery
- Supports interactive dashboards in Looker Studio
- Uses Apache Airflow for orchestration
- Runs entirely inside Docker containers

The project demonstrates modern cloud-based Data Engineering practices while producing practical insights that can support flood monitoring, agricultural planning, aquaculture management, and disaster preparedness.

---

# 🌍 Business Problem

Flooding and changing weather patterns are becoming more frequent across many regions, particularly in developing countries.

These events affect multiple sectors, including:

- 🌱 Agriculture
- 🐟 Aquaculture
- 🚜 Food Production
- 🏙 Urban Planning
- 🚧 Infrastructure
- 🚑 Disaster Management
- ❤️ Public Health

Common challenges include:

- Crop losses
- Fish pond overflow
- Soil erosion
- Heat stress
- Waterlogging
- Transportation disruption
- Economic losses

Although weather data is publicly available, organizations often struggle to:

- Collect it automatically
- Validate data quality
- Process large volumes consistently
- Generate meaningful risk indicators
- Deliver timely insights for decision-making

This project addresses these challenges by transforming raw weather observations into analytics-ready datasets and actionable climate intelligence.

---

# 🎯 Project Objectives

The objectives of this project are to:

- Build a complete end-to-end ETL/ELT pipeline
- Demonstrate production-inspired Data Engineering practices
- Implement a Medallion Data Architecture
- Automate weather data ingestion using Apache Airflow
- Perform automated data validation
- Engineer weather-based analytical features
- Calculate flood and climate risk indicators
- Publish analytical datasets to Google BigQuery
- Enable dashboard reporting using Looker Studio
- Demonstrate incremental data processing
- Showcase Docker-based deployment
- Follow cloud engineering best practices

---

# 💡 Solution Overview

The platform converts raw weather observations into meaningful business intelligence through a fully automated pipeline.

The pipeline performs the following tasks:

1. Extract weather forecasts from the Open-Meteo API.
2. Store timestamped raw JSON files in the Bronze layer.
3. Validate incoming datasets.
4. Transform raw data into clean Parquet files.
5. Engineer rainfall and temperature features.
6. Calculate environmental risk indicators.
7. Upload processed datasets to Google Cloud Storage.
8. Load analytics-ready data into Google BigQuery.
9. Remove duplicate records automatically.
10. Build dashboards in Looker Studio.

Unlike simple weather dashboards, this platform focuses on **decision support** by generating indicators such as:

- Flash Flood Risk
- Sustained Flood Risk
- Soil Saturation Risk
- Crop Heat Stress
- Pond Overflow Risk
- Rainfall Trends

---

# 🏗 Solution Architecture

```text
                    Weather API
                 (Open-Meteo API)
                         │
                         ▼
               Data Extraction Layer
                Python + Requests
                         │
                         ▼
             Apache Airflow Orchestration
                         │
                         ▼
                Data Validation Layer
      ┌──────────────────────────────────┐
      │ • Schema Validation              │
      │ • Missing Values                 │
      │ • Duplicate Checks               │
      │ • Data Quality Rules             │
      └──────────────────────────────────┘
                         │
                         ▼
               Transformation Layer
      ┌──────────────────────────────────┐
      │ • Data Cleaning                  │
      │ • Feature Engineering            │
      │ • Risk Calculations              │
      └──────────────────────────────────┘
                         │
                         ▼
             Bronze → Silver → Gold
                         │
                         ▼
             Google Cloud Storage (GCS)
                         │
                         ▼
                Google BigQuery
                         │
                         ▼
               Looker Studio Dashboard
                         │
                         ▼
             Climate Decision Support
```

---

# 🏛 Medallion Architecture

```text
                     Open-Meteo API
                            │
                            ▼
                    Bronze Layer
             Timestamped JSON Files
      lagos_20260728_144225.json

                            │
                            ▼
                    Silver Layer
      Timestamped Parquet Datasets

      lagos_20260728_144225.parquet
      lagos_20260728_144225_features.parquet
      lagos_20260728_144225_risk.parquet

                            │
                            ▼
               Google Cloud Storage

gs://climate-intel-raw-data-2026/
└── silver/
    └── 2026-07-28/
        └── lagos_20260728_144225_risk.parquet

                            │
                            ▼
                    Gold Layer

BigQuery
└── climate_gold
      └── weather_risk

                            │
                            ▼
                 Looker Studio Dashboards
```

---

# 🔄 End-to-End Pipeline Workflow

```text
Extract Weather Data
        │
        ▼
Validate Raw JSON
        │
        ▼
Transform Dataset
        │
        ▼
Feature Engineering
        │
        ▼
Risk Calculations
        │
        ▼
Upload Latest Dataset to GCS
        │
        ▼
Load Latest Dataset into BigQuery
        │
        ▼
Remove Duplicate Records
        │
        ▼
Build Dashboards
```

---

# 📂 Project Structure

```text
climate-intelligence-platform/

│
├── dags/
│     └── climate_pipeline_dag.py
│
├── scripts/
│     ├── extract.py
│     ├── validate.py
│     ├── transform.py
│     ├── feature_engineering.py
│     ├── calculate_risk.py
│     ├── load_to_gcs.py
│     ├── load_to_bigquery.py
│     └── run_pipeline.py
│
├── config/
│     ├── locations.json
│     └── gcp-service-account.json
│
├── data/
│     ├── raw/
│     └── processed/
│
├── logs/
│
├── plugins/
│
├── sql/
│
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

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

### API Documentation

Open-Meteo

https://open-meteo.com/

API Documentation

https://open-meteo.com/en/docs

Example Request

```text
https://api.open-meteo.com/v1/forecast
```

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

The platform converts rainfall observations into actionable environmental indicators.

## Flash Flood Risk

| Rainfall (3-Day) | Risk |
|------------------|------|
| ≥ 75 mm | CRITICAL |
| 40–74 mm | WARNING |
| < 40 mm | NORMAL |

---

## Sustained Flood Risk

| Rainfall (7-Day) | Risk |
|------------------|------|
| ≥ 100 mm | CRITICAL |
| 60–99 mm | WARNING |
| < 60 mm | NORMAL |

---

## Soil Saturation Risk

| Rainfall (7-Day) | Risk |
|------------------|------|
| ≥100 mm | HIGH |
| 60–99 mm | MEDIUM |
| <60 mm | LOW |

---

## Crop Heat Stress

| Maximum Temperature | Risk |
|----------------------|------|
| ≥35°C | HIGH |
| 30–34°C | MEDIUM |
| <30°C | LOW |

---

## Pond Overflow Risk

| Rainfall (3-Day) | Risk |
|------------------|------|
| ≥75 mm | HIGH |
| 40–74 mm | MEDIUM |
| <40 mm | LOW |

---

# 💻 Installation Guide

## Prerequisites

Install the following software before running the project.

| Software | Version |
|----------|----------|
| Python | 3.11+ |
| Docker Desktop | Latest |
| Docker Compose | Latest |
| Git | Latest |
| Google Cloud SDK | Latest |
| Visual Studio Code | Recommended |

---

# 📥 Clone the Repository

```bash
git clone https://github.com/ILE-GOD/climate-intelligence-platform.git

cd climate-intelligence-platform
```

---

# ⚙️ Project Setup

## Windows

### 1. Clone Repository

```powershell
git clone https://github.com/ILE-GOD/climate-intelligence-platform.git

cd climate-intelligence-platform
```

### 2. Create Virtual Environment

```powershell
python -m venv .venv
```

Activate

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment

Copy

```
.env.example
```

to

```
.env
```

Update the environment variables.

### 5. Start Docker

```powershell
docker compose up -d
```

### 6. Open Airflow

```
http://localhost:8080
```

---

## Linux

```bash
git clone https://github.com/ILE-GOD/climate-intelligence-platform.git

cd climate-intelligence-platform

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

docker compose up -d
```

---

## macOS

```bash
git clone https://github.com/ILE-GOD/climate-intelligence-platform.git

cd climate-intelligence-platform

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

docker compose up -d
```

---

# 🐳 Docker Services

The project runs inside Docker containers.

| Container | Purpose |
|------------|----------|
| airflow-webserver | Airflow UI |
| airflow-scheduler | DAG Scheduler |
| airflow-triggerer | Trigger Service |
| airflow-init | Initialization |
| postgres | Airflow Metadata Database |
| pgadmin | PostgreSQL Administration |

Start containers

```bash
docker compose up -d
```

Check status

```bash
docker ps
```

Stop containers

```bash
docker compose down
```

---

# ☁️ Google Cloud Setup

## Step 1

Create a Google Cloud Project.

Example

```
capable-avatar-475900-j5
```

---

## Step 2

Enable the following APIs

- BigQuery API
- Cloud Storage API
- IAM API

---

## Step 3

Create a Storage Bucket

Example

```
climate-intel-raw-data-2026
```

---

## Step 4

Create a Service Account

Grant

- Storage Admin
- BigQuery Admin

Download the JSON credentials.

Store it inside

```
config/
```

Example

```
config/gcp-service-account.json
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
#############################
# Google Cloud
#############################

BIGQUERY_PROJECT=capable-avatar-475900-j5

GCS_BUCKET_NAME=climate-intel-raw-data-2026

GOOGLE_APPLICATION_CREDENTIALS=/opt/airflow/config/gcp-service-account.json

#############################
# Weather Location
#############################

LOCATION=lagos

LATITUDE=6.4531

LONGITUDE=3.3958

LOCATION_NAME=lagos

#############################
# Data Directories
#############################

DATA_RAW_DIR=/opt/airflow/data/raw

DATA_PROCESSED_DIR=/opt/airflow/data/processed
```

---

# ▶️ Running the Pipeline

Start Docker

```bash
docker compose up -d
```

Open Airflow

```
http://localhost:8080
```

Default credentials

```
Username: airflow

Password: airflow
```

Enable

```
climate_intelligence_pipeline
```

Click

```
Trigger DAG
```

The pipeline executes the following tasks.

```text
Extract
      │
      ▼
Validate
      │
      ▼
Transform
      │
      ▼
Feature Engineering
      │
      ▼
Risk Calculation
      │
      ▼
Upload to GCS
      │
      ▼
Load to BigQuery
```

---

# 📂 Pipeline Outputs

## Bronze

```
data/raw/

lagos_20260728_144225.json
```

---

## Silver

```
data/processed/

lagos_20260728_144225.parquet

lagos_20260728_144225_features.parquet

lagos_20260728_144225_risk.parquet
```

---

## Google Cloud Storage

```
gs://climate-intel-raw-data-2026/

silver/

2026-07-28/

lagos_20260728_144225_risk.parquet
```

---

## BigQuery

```
Project

capable-avatar-475900-j5

Dataset

climate_gold

Table

weather_risk
```

---

# 📸 Screenshots

## Apache Airflow

> Add screenshot

```
images/airflow_dag.png
```

Suggested screenshot:

- DAG Graph
- Successful Run
- Task Status

---

## Airflow Task Graph

> Add screenshot

```
images/airflow_graph.png
```

---

## Google Cloud Storage

> Add screenshot

```
images/gcs_bucket.png
```

Show

- Bucket
- Uploaded Parquet Files

---

## BigQuery Dataset

> Add screenshot

```
images/bigquery_tables.png
```

Include

- Dataset
- Table
- Row Count

---

## BigQuery Query Results

> Add screenshot

```
images/bigquery_results.png
```

---

## Looker Studio Dashboard

> Add screenshot

```
images/dashboard.png
```

Recommended visuals

- Flood Risk by Date
- Rainfall Trend
- Temperature Trend
- Crop Stress
- Pond Overflow Risk

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

The platform is designed to evolve into a complete Climate Intelligence ecosystem.

Planned improvements include:

- Multiple weather APIs
- Real-time weather streaming
- Apache Kafka
- dbt transformations
- Great Expectations validation
- Cloud Composer deployment
- Terraform Infrastructure as Code
- Kubernetes deployment
- Machine Learning flood prediction
- Rainfall anomaly detection
- WhatsApp flood alerts
- SMS notifications
- Email alert service
- Interactive GIS maps
- Historical climate analytics
- Weather anomaly detection
- Automated data quality monitoring

---

# 💼 Skills Demonstrated

This project demonstrates practical experience with:

- Data Engineering
- ETL Pipeline Development
- ELT Architecture
- Apache Airflow
- Docker
- Google Cloud Platform
- Google Cloud Storage
- BigQuery
- Pandas
- REST APIs
- Data Validation
- Incremental Processing
- Feature Engineering
- Risk Modeling
- Medallion Architecture
- Data Warehousing
- Business Intelligence
- Looker Studio
- Git
- GitHub
- Cloud Automation

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/my-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature/my-feature
```

5. Open a Pull Request.

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

🔗 GitHub

```
https://github.com/ILE-GOD
```

🔗 LinkedIn

```
https://www.linkedin.com/in/daniel-okom-748798242
```

---

> **Demonstration of modern Data Engineering practices for climate intelligence and flood early warning.**
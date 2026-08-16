# 🌍 Climate Intelligence & Flood Early Warning Platform

> **Real-Time Weather Monitoring & Climate Risk Analytics for Abuja and Lagos**

A production-inspired Data Engineering platform that automates weather data ingestion, validation, transformation, climate risk assessment, and analytics using **Python, Apache Airflow, Docker, Google Cloud Storage, BigQuery, and Looker Studio**.

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

The **Climate Intelligence Platform** is a cloud-based Data Engineering solution that transforms raw weather data into actionable climate intelligence.

Its first implementation focuses on **Abuja and Lagos**, automatically collecting and processing weather information and converting it into climate risk indicators that support:

- 🌊 Flood preparedness
- 🌱 Agriculture
- 🐟 Aquaculture
- 🌡️ Heat-stress monitoring
- 🌧️ Rainfall analysis
- 🌍 Environmental monitoring

Unlike a basic weather dashboard, the platform transforms weather observations into **risk indicators and decision-support insights**.

---

## 🎯 Project Objectives

The project aims to:

- Build an end-to-end cloud-based ETL pipeline
- Implement a Medallion Architecture (Bronze, Silver, Gold)
- Automate weather data ingestion from the Open-Meteo API
- Validate incoming weather datasets
- Transform raw weather data into structured datasets
- Engineer climate and rainfall features
- Calculate climate and flood risk indicators
- Store analytics-ready datasets in BigQuery
- Build interactive dashboards in Looker Studio
- Demonstrate production-inspired Data Engineering practices

---

# 🌍 Business Problem

Nigeria experiences flooding, irregular rainfall, and rising temperatures that can affect:

- 🌱 Agriculture
- 🐟 Aquaculture
- 🏙️ Infrastructure
- 🍚 Food production
- 🚨 Disaster management
- 🌍 Environmental monitoring

Although weather information is publicly available, it is often not presented in a form that directly supports decision-making.

Organizations can struggle to:

- Collect weather data automatically
- Validate data quality
- Process weather data consistently
- Convert observations into meaningful risk indicators
- Deliver timely, understandable insights

The platform addresses this gap by transforming raw weather observations into **analytics-ready datasets and actionable climate intelligence**.

---

# 💡 Solution Overview

The platform automatically collects weather data from the **Open-Meteo API**, processes it through an end-to-end Data Engineering pipeline, calculates climate risk indicators, and presents the results through interactive Looker Studio dashboards.

The current implementation generates indicators including:

- 🌊 Flash Flood Risk
- 🌧️ Sustained Flood Risk
- 💧 Soil Saturation Risk
- 🌱 Crop Heat Stress
- 🐟 Pond Overflow Risk
- 📊 Rainfall Trends

The platform also provides sector-specific advisory information for **agriculture and aquaculture**.

---

# 🏗 Solution Architecture

<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/2531f028-634f-4d3d-a12c-57468d21fadb" />

---

# 🔄 End-to-End Pipeline Workflow

<img width="815" height="186" alt="Image" src="https://github.com/user-attachments/assets/1017d58e-4bb6-4975-93d1-9eb2c7ac9ee2" />

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

The platform currently consumes weather data from publicly available  Open-Meteo APIs https://open-meteo.com/en/docs

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

<img width="817" height="355" alt="Image" src="https://github.com/user-attachments/assets/a5534e38-deec-4bc9-a5ed-60f906f64eed" />

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

<img width="1376" height="754" alt="Image" src="https://github.com/user-attachments/assets/8e021137-500b-4b41-9a38-0a5a4582301f" />

Visuals showing: 

- Flood Risk by Date
- Rainfall Trend
- Temperature Trend
- Crop Stress
- Pond Overflow Risk

## 📊 Dashboard

[View the Live Climate Intelligence Dashboard](https://datastudio.google.com/reporting/f04d0d6e-329c-47d2-8ac8-60de333a968c)

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
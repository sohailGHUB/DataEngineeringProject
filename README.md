# 🚀 End-to-End Azure Data Engineering Project

### AdventureWorks Sales Analytics Pipeline

An end-to-end Azure Data Engineering solution that ingests raw data from GitHub, performs scalable data transformation using Azure Databricks, 
creates analytical datasets using Azure Synapse Serverless SQL, and visualizes business insights through Power BI.

# 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Solution Architecture](#-solution-architecture)
- [Architecture Diagram](#-architecture-diagram)
- [Technology Stack](#-technology-stack)
- [Azure Services Used](#-azure-services-used)
- [Project Workflow](#-project-workflow)
- [Repository Structure](#-repository-structure)
- [AdventureWorks Dataset](#-adventureworks-dataset)
- [Metadata-Driven Ingestion](#-metadata-driven-ingestion)
- [Azure Data Factory](#-azure-data-factory)
- [Azure Data Lake Storage Gen2](#-azure-data-lake-storage-gen2)
- [Azure Databricks](#-azure-databricks)
- [Azure Synapse Analytics](#-azure-synapse-analytics)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Business Insights](#-business-insights)
- [How to Run the Project](#-how-to-run-the-project)
- [Future Enhancements](#-future-enhancements)
- [Skills Demonstrated](#-skills-demonstrated)
- [Author](#-author)


# 📖 Project Overview

This project demonstrates the implementation of an **end-to-end Azure Data Engineering pipeline** using Microsoft's cloud ecosystem.

The pipeline follows the **Medallion Architecture (Bronze → Silver → Gold)** to ingest, transform, store, analyze, 
and visualize business data from the AdventureWorks dataset.

The solution begins by ingesting multiple CSV files from GitHub into Azure Data Lake Storage using a **metadata-driven Azure Data Factory pipeline**. 
The raw data is transformed using **Azure Databricks (PySpark)** and stored as optimized Parquet files in the Silver layer. 
Azure Synapse Serverless SQL is then used to create business-ready analytical datasets, which are finally visualized in Power BI.

This project demonstrates modern cloud-based data engineering practices, including:

- Metadata-driven ingestion
- Dynamic pipeline parameterization
- ETL/ELT processing
- Distributed data transformation
- Serverless SQL analytics
- Business Intelligence reporting

---

# 🎯 Business Problem

Organizations collect data from multiple operational systems, but raw data is often:

- Stored in different formats
- Difficult to analyze directly
- Not optimized for reporting
- Lacking business-ready aggregations

A scalable cloud-based data pipeline is required to:

- Automatically ingest data from source systems
- Store raw data securely
- Clean and transform datasets
- Build analytical models
- Generate business insights
- Support decision-making through dashboards

This project addresses these challenges by implementing an end-to-end Azure-based analytics pipeline.

---

# 🏗️ Solution Architecture

The project follows the Medallion Architecture consisting of three storage layers:

### 🥉 Bronze Layer

- Raw CSV files
- No transformations
- Source of truth
- Loaded using Azure Data Factory

### 🥈 Silver Layer

- Cleaned and transformed data
- PySpark transformations
- Fact and Dimension tables
- Stored as Parquet files

### 🥇 Gold Layer

- Business-ready analytical tables
- SQL aggregations
- Reporting datasets
- Power BI data source

---

# 🖼️ Architecture Diagram

<img width="1536" height="1024" alt="Architecture diagram" src="https://github.com/user-attachments/assets/5686638a-692f-46f0-9d33-086eda0c4c92" />


---

# 💻 Technology Stack

| Category | Technology |
|-----------|------------|
| Cloud Platform | Microsoft Azure |
| Data Ingestion | Azure Data Factory |
| Data Storage | Azure Data Lake Storage Gen2 |
| Data Processing | Azure Databricks |
| Programming Language | PySpark |
| Data Format | CSV, Parquet |
| Analytics | Azure Synapse Serverless SQL |
| Visualization | Microsoft Power BI |
| Source Control | GitHub |
| SQL | MySQL

---

# ☁️ Azure Services Used

| Azure Service | Purpose |
|---------------|---------|
| Azure Data Factory | Metadata-driven data ingestion |
| Azure Data Lake Storage Gen2 | Bronze, Silver and Gold storage |
| Azure Databricks | Data cleaning and transformation |
| Azure Synapse Analytics | Serverless SQL analytics |
| Power BI | Dashboard creation and visualization |

---

# 🔄 Project Workflow


                                      AdventureWorks Dataset
                                               │
                                               ▼
                                    metadata.json (Configuration)
                                               │
                                               ▼
                                  Azure Data Factory (Lookup)
                             Reads metadata.json configuration file
                                               │
                                               ▼
                                 Azure Data Factory (ForEach)
                      Iterates through each dataset defined in metadata.json
                                               │
                                               ▼
                                 Azure Data Factory (Copy Activity)
                  Dynamically copies files using @item().relativeURL,
                      @item().FolderName and @item().FileName
                                               │
                                               ▼
                           Azure Data Lake Storage Gen2 (Bronze Layer)
                          Stores raw CSV files without any transformation
                                               │
                                               ▼
                                  Azure Databricks (PySpark)
                    • Reads Bronze CSV files
                    • Cleans and transforms data
                    • Creates Fact and Dimension tables
                    • Writes optimized Parquet files
                                               │
                                               ▼
                           Azure Data Lake Storage Gen2 (Silver Layer)
                         Stores cleaned and transformed Parquet files
                                               │
                                               ▼
                           Azure Synapse Serverless SQL Pool
                    • Reads Silver Parquet files
                    • Performs SQL joins and aggregations
                    • Creates business-ready analytical datasets
                                               │
                                               ▼
                           CETAS (CREATE EXTERNAL TABLE AS SELECT)
                        Writes reporting tables to the Gold Layer
                                               │
                                               ▼
                            Azure Data Lake Storage Gen2 (Gold Layer)
                         Stores curated analytical Parquet datasets
                                               │
                                               ▼
                                 Microsoft Power BI Desktop
                         Connects using Synapse SQL Endpoint
                                               │
                                               ▼
                             Interactive AdventureWorks Dashboard
```

---

## 📌 Key Features

✅ End-to-End Azure Data Engineering Pipeline

✅ Metadata-Driven Azure Data Factory Pipeline

✅ Dynamic Dataset Parameterization

✅ Medallion Architecture (Bronze → Silver → Gold)

✅ PySpark Transformations in Azure Databricks

✅ Serverless SQL Analytics using Azure Synapse

✅ Business Intelligence Dashboard using Power BI

✅ Cloud-Native Data Lake Architecture

---

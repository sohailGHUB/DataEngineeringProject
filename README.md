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


---

# 📂 Repository Structure

Data-Engineering-Project/
│
├── AdventureWorks/
│   ├── metadata.json
│   ├── Customers.csv
│   ├── Products.csv
│   ├── ProductCategories.csv
│   ├── ProductSubcategories.csv
│   ├── Sales.csv
│   ├── Returns.csv
│   ├── Territories.csv
│   └── ...
│
├── Architecture/
│   └── Azure_Data_Engineering_Architecture.png
│
├── Azure-Data-Factory/
│   └── Screenshots/
│
├── Azure-Data-Lake/
│   └── Screenshots/
│
├── Azure-Databricks/
│   ├── SilverLayer.ipynb
│   ├── SilverLayer.py
│   └── Screenshots/
│
├── Azure-Synapse/
│   ├── SQL Scripts/
│   └── Screenshots/
│
├── Power-BI/
│   ├── AdventureWorksDashboard.pbix
│   └── Dashboard.png
│
├── Screenshots/
│
└── README.md
```

---

# 📊 AdventureWorks Dataset

The **AdventureWorks** dataset is a sample business dataset that represents a fictional retail company.

It contains information related to:

- Customers
- Products
- Product Categories
- Product Subcategories
- Sales
- Returns
- Sales Territories
- Calendar information

The dataset is stored as CSV files inside the **AdventureWorks** folder and acts as the source data for the pipeline.

---

# 📄 metadata.json

Instead of hardcoding every source file inside Azure Data Factory, this project uses a **metadata-driven approach**.

The `metadata.json` file contains configuration information required for data ingestion.

Typical metadata includes:

- Relative URL
- Destination Folder Name
- Destination File Name

Using metadata makes the pipeline reusable and scalable because adding a new dataset only requires updating the configuration file.

---

# 🔄 Metadata-Driven Ingestion

Traditional pipelines often require one Copy Activity for every dataset.

This project follows a metadata-driven design where a single pipeline dynamically ingests multiple datasets.

Advantages:

- No hardcoded file names
- Easy maintenance
- Easily scalable
- Reusable pipeline
- Minimal code changes when adding new datasets

---

# 🏭 Azure Data Factory

Azure Data Factory (ADF) is used to orchestrate the data ingestion process.

The pipeline dynamically reads dataset information from `metadata.json` and copies each source file into the Bronze layer of Azure Data Lake Storage Gen2.

---

## Pipeline Components

The pipeline consists of three major activities:

1. Lookup Activity
2. ForEach Activity
3. Copy Data Activity

---

## 🔍 Lookup Activity

The Lookup activity reads the configuration stored in `metadata.json`.

Instead of processing only a single record, it retrieves all configuration records required for ingestion.

### Purpose

- Read metadata configuration
- Return all dataset records
- Pass configuration to the ForEach activity

---

### Screenshot

<img width="1920" height="1080" alt="look-up activity config" src="https://github.com/user-attachments/assets/09df9432-d1a0-4a2e-bac9-77e3be5c858c" />

## 🔁 ForEach Activity

The ForEach activity iterates through every record returned by the Lookup activity.

The items property is configured using:

```text
@activity('Lookup1').output.value
```

This enables the pipeline to process multiple datasets using a single Copy Activity.

### Purpose

- Iterate over metadata records
- Execute one Copy Activity per dataset
- Support dynamic ingestion

---

### Screenshot

<img width="1920" height="1080" alt="look-up output to for-each" src="https://github.com/user-attachments/assets/4063234b-d242-4af6-910d-2699aad30ab0" />


## 📤 Copy Data Activity

The Copy Activity transfers each dataset from the HTTP source into Azure Data Lake Storage Gen2.

Instead of using fixed values, the pipeline dynamically reads values from the current metadata record.

---

## 🌐 Dynamic Source Parameterization

The HTTP source dataset is parameterized using:

```text
@item().relativeURL
```

This dynamically selects the source file during each iteration.

<img width="1920" height="1080" alt="source dataset parameterization (copy activity)" src="https://github.com/user-attachments/assets/f28f0158-1859-4840-9615-7b977a026ede" />

## 💾 Dynamic Sink Parameterization

The destination dataset is also parameterized.

Folder Name:

```text
@item().FolderName
```

File Name:

```text
@item().FileName
```

This ensures that each file is automatically stored in its correct location inside the Bronze layer.

<img width="1920" height="1080" alt="sink dataset parameterization (copy activity)" src="https://github.com/user-attachments/assets/d581a3cf-9bd7-4165-b5d9-caaa90f9d85d" />


## ⚙️ Pipeline Execution

The complete execution flow is:

Lookup Activity
        │
        ▼
Lookup Output
        │
        ▼
ForEach Activity
        │
        ▼
Copy Data Activity
        │
        ▼
Azure Data Lake Storage Gen2 (Bronze Layer)
```

---

## ✅ Azure Data Factory Highlights

✔ Metadata-driven ingestion

✔ Dynamic parameterization

✔ Lookup activity

✔ ForEach activity

✔ Copy Data activity

✔ HTTP source

✔ Azure Data Lake Storage Gen2 sink

✔ Scalable pipeline design


---

## 📷 Azure Data Factory Screenshots

The repository contains detailed implementation screenshots covering:

- Pipeline Overview
- Lookup Configuration Dataset
- Lookup Output to ForEach
- Dynamic Source Parameters
- Dynamic Sink Parameters
- Copy Activity
- Pipeline Validation
- Successful Pipeline Execution

These screenshots are available inside:

```text
Azure-Data-Factory/
    └── Screenshots/
```




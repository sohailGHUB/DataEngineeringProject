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
| SQL | T-SQL

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

```
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
```
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
```
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

# 🌊 Azure Data Lake Storage Gen2

Azure Data Lake Storage Gen2 (ADLS Gen2) serves as the centralized storage layer for this project.

The project follows the **Medallion Architecture**, organizing data into three logical layers:

- 🥉 Bronze Layer (Raw Data)
- 🥈 Silver Layer (Transformed Data)
- 🥇 Gold Layer (Business-Ready Data)

This architecture improves data quality, scalability, and maintainability while separating raw, processed, and analytical datasets.

---

## 🥉 Bronze Layer

The Bronze layer stores the raw data exactly as received from the source system.

### Characteristics

- Original CSV files
- No transformations
- Immutable raw data
- Source of truth
- Loaded by Azure Data Factory

### Purpose

- Preserve original datasets
- Support auditing
- Enable reprocessing if required

### Screenshot

<img width="1920" height="1080" alt="bronze container" src="https://github.com/user-attachments/assets/a1c205b2-4370-49e3-982b-be058589ee7f" />

## 🥈 Silver Layer

The Silver layer contains cleaned and transformed datasets generated by Azure Databricks.

Data is stored in **Apache Parquet** format for improved performance and compression.

### Characteristics

- Cleaned data
- Standardized columns
- Optimized Parquet files
- Dimension tables
- Fact tables

### Screenshot

<img width="1920" height="1080" alt="silver container" src="https://github.com/user-attachments/assets/21a8eb35-9fa2-4894-b632-3ae65d60e814" />


## 🥇 Gold Layer

The Gold layer contains business-ready analytical datasets.

These datasets are created using **Azure Synapse Serverless SQL** and stored back in ADLS Gen2 using **CETAS (CREATE EXTERNAL TABLE AS SELECT)**.

### Characteristics

- Aggregated data
- Reporting datasets
- Analytical tables
- Optimized for Power BI

### Screenshot

<img width="1920" height="1080" alt="gold container" src="https://github.com/user-attachments/assets/da92e329-5733-4fd8-8b00-1beb0d50585a" />


---

# 🏗️ Medallion Architecture
```
Source Data
     │
     ▼
Bronze Layer
(Raw CSV)
     │
     ▼
Silver Layer
(Cleaned Parquet)
     │
     ▼
Gold Layer
(Reporting Tables)
```

---

# 🔥 Azure Databricks

Azure Databricks is used to perform large-scale distributed data transformation using **PySpark**.

The notebook reads raw CSV files from the Bronze layer, performs data cleaning and transformation, creates analytical datasets, and writes optimized Parquet files into the Silver layer.

---

## Why Azure Databricks?

Azure Databricks provides:

- Distributed processing
- High-performance Spark engine
- PySpark programming
- Seamless integration with ADLS Gen2
- Scalable ETL processing

---

# 📒 Databricks Notebook

The notebook performs the following operations:

- Reads CSV files from Bronze
- Infers schemas
- Cleans missing values
- Removes unnecessary columns
- Converts data types
- Creates Fact tables
- Creates Dimension tables
- Writes Parquet files into Silver

---

## Screenshot

<img width="1920" height="1080" alt="databricks notebook UI" src="https://github.com/user-attachments/assets/46d58a90-81be-4489-aba2-c6d06d06ea46" />


---

# ⚙️ Data Transformation Process

The transformation pipeline follows these steps:
```
Bronze CSV Files
        │
        ▼
Read using PySpark
        │
        ▼
Schema Validation
        │
        ▼
Data Cleaning
        │
        ▼
Column Standardization
        │
        ▼
Fact & Dimension Table Creation
        │
        ▼
Write as Parquet
        │
        ▼
Silver Layer
```
---

# 🔄 PySpark Transformations

The notebook performs several transformations, including:

### ✔ Reading CSV Files

- Loads raw datasets from Bronze

### ✔ Schema Inference

- Automatically detects column data types

### ✔ Data Cleaning

- Handles null values
- Removes unnecessary columns
- Standardizes column names

### ✔ Type Conversion

Examples include:

- String → Integer
- String → Date
- String → Decimal

### ✔ Writing Parquet Files

The transformed datasets are stored in the Silver layer as Parquet files for optimized analytics.

---

# 📊 Dimension Tables

Dimension tables contain descriptive business information.

Examples include:

- Customer Dimension
- Product Dimension
- Product Category Dimension
- Product Subcategory Dimension
- Territory Dimension

These tables are optimized for analytical reporting.

---

# 📈 Fact Tables

Fact tables contain measurable business events.

Examples include:

- Sales Fact
- Returns Fact

These tables are later joined with Dimension tables in Azure Synapse Analytics.

---

# 💡 Why Parquet?

Instead of storing transformed data as CSV, the project uses **Apache Parquet** because it offers:

- Better compression
- Faster query performance
- Columnar storage
- Reduced storage cost
- Optimized analytics

---

# 📷 Azure Databricks Screenshots

The repository contains screenshots demonstrating:

- Workspace
- Cluster Configuration
- Notebook
- PySpark Transformations
- Data Preview
- Successful Execution

Location:
```
Azure-Databricks/
    └── Screenshots/
```
---

# ✅ Azure Databricks Highlights

✔ Distributed Data Processing

✔ PySpark Transformations

✔ Data Cleaning

✔ Schema Validation

✔ Fact Table Creation

✔ Dimension Table Creation

✔ Parquet Optimization

✔ Silver Layer Generation

✔ Medallion Architecture Implementation

---

# 🏛️ Azure Synapse Analytics

Azure Synapse Analytics is used as the **analytical serving layer** of the project.

Instead of loading data into a dedicated SQL database, this project uses **Serverless SQL Pool** to directly query Parquet files stored in Azure Data Lake Storage Gen2.

Business-ready analytical tables are then created using **CETAS (CREATE EXTERNAL TABLE AS SELECT)** and stored in the Gold layer.

---

# 🎯 Why Azure Synapse?

Azure Synapse provides:

- Serverless SQL querying
- High-performance analytics
- Direct querying of Data Lake
- No infrastructure management
- Integration with Power BI

It enables SQL analytics without moving data into a traditional database.

---

# ⚡ Serverless SQL Pool

The project uses **Azure Synapse Serverless SQL Pool**, which allows SQL queries to run directly against Parquet files stored in Azure Data Lake Storage Gen2.

### Benefits

- No database provisioning
- Pay only for data processed
- Direct access to ADLS Gen2
- Ideal for analytical workloads

---

# 🔗 External Data Source

Before querying files stored in ADLS Gen2, an **External Data Source** is created.

The External Data Source defines the connection between Synapse and Azure Data Lake Storage Gen2.

### Purpose

- Connect Synapse to ADLS Gen2
- Enable SQL queries on lake files
- Reuse the storage connection across multiple SQL scripts

---

# 📄 External File Format

An External File Format specifies the format of the data being queried.

Since the Silver layer stores data as **Apache Parquet**, an External File Format is created accordingly.

### Purpose

- Identify file type
- Improve query execution
- Enable Parquet support

---

# 📂 OPENROWSET

OPENROWSET is used to directly query Parquet files stored in the Silver layer.

Example use cases include:

- Preview transformed datasets
- Validate data
- Test SQL queries
- Explore lake data before creating reporting tables

---

# 📊 SQL Transformations

Azure Synapse SQL scripts perform several analytical operations, including:

- Table joins
- Aggregations
- Common Table Expressions (CTEs)
- GROUP BY
- ORDER BY
- Window Functions
- Business metrics

These transformations convert cleaned data into reporting-ready datasets.

---

# 🏆 Gold Layer using CETAS

The final analytical datasets are created using:

**CREATE EXTERNAL TABLE AS SELECT (CETAS)**

Instead of storing results inside Synapse, CETAS writes the output directly into the **Gold layer** of Azure Data Lake Storage Gen2.

### Advantages

- Faster reporting
- Reusable datasets
- Optimized Parquet storage
- Reduced query cost
- Easy integration with Power BI

---

# 📋 Gold Tables

The project creates multiple business-ready reporting tables.

These include:

### 📈 Sales Summary

Provides overall sales metrics including:

- Total Orders
- Total Quantity Sold
- Average Quantity per Order
- Monthly Sales Trend
- Unique Customers

---

### 🛍️ Product Performance

Analyzes product-level sales performance.

Business insights include:

- Best-selling products
- Product category analysis
- Quantity sold by product

---

### 👥 Customer Summary

Provides customer-level analytics.

Includes:

- Customer purchases
- Gender distribution
- Income band analysis

---

### 🌍 Territory Sales

Analyzes sales across different sales territories.

Helps identify:

- High-performing regions
- Regional sales distribution

---

### 🔄 Return Analysis

Provides insights into returned products.

Useful for:

- Product quality analysis
- Return trends
- Business decision making

---

### ⭐ Top Customers

Ranks customers based on purchasing behavior.

Business insights include:

- Highest purchasing customers
- Customer contribution analysis

---

# 📝 SQL Concepts Used

The SQL implementation demonstrates:

✔ CTE (Common Table Expressions)

✔ INNER JOIN

✔ LEFT JOIN

✔ GROUP BY

✔ ORDER BY

✔ Aggregate Functions

✔ Window Functions

✔ CASE Expressions

✔ Date Functions

✔ CREATE EXTERNAL TABLE

✔ OPENROWSET

✔ CETAS

---

# 📷 Azure Synapse Screenshots

The repository includes screenshots for:

- Synapse Workspace
- Serverless SQL Pool
- SQL Scripts
- Query Results
- External Tables
- Gold Layer
- Successful SQL Execution

Location:
```
Azure-Synapse/
    └── Screenshots/
```
---

# 📂 SQL Scripts

The repository contains SQL scripts used to generate the Gold layer.

These scripts demonstrate:

- External Data Source creation
- External File Format creation
- OPENROWSET queries
- Analytical SQL transformations
- CETAS implementation



---

# 🔄 Data Flow in Synapse
```
Silver Layer (Parquet Files)
            │
            ▼
External Data Source
            │
            ▼
External File Format
            │
            ▼
OPENROWSET
            │
            ▼
SQL Transformations
            │
            ▼
CETAS
            │
            ▼
Gold Layer (Parquet)
            │
            ▼
Power BI
```

---

# ✅ Azure Synapse Highlights

✔ Serverless SQL Pool

✔ External Data Source

✔ External File Format

✔ OPENROWSET

✔ SQL Analytics

✔ Aggregations

✔ CTE

✔ Window Functions

✔ CETAS

✔ Gold Layer Generation

✔ Business-Ready Reporting Tables

✔ Power BI Integration

---

# 📊 Power BI Dashboard

Microsoft Power BI is used as the final reporting and visualization layer of the project.

The dashboard connects directly to the **Azure Synapse Serverless SQL Endpoint**, allowing business users to interact with curated analytical datasets stored in the Gold layer.

The dashboard provides interactive visualizations that enable decision-makers to monitor sales performance, customer behavior, product trends, and territory-wise business insights.

---

# 🔗 Data Source Connection

Power BI connects to the Gold layer using the **Azure Synapse Serverless SQL Endpoint**.

Connection Type:

- Azure Synapse Analytics
- Serverless SQL Endpoint

This allows Power BI to retrieve business-ready datasets generated through Azure Synapse SQL scripts.

---

# 📷 Power BI Connection

<img width="1920" height="1080" alt="connect power BI via SQL endpoint" src="https://github.com/user-attachments/assets/d0cf8d1c-314e-4935-9115-4801d179f280" />

---

# 📈 Dashboard Overview

The dashboard consists of multiple business KPIs and visualizations designed to provide a comprehensive view of AdventureWorks sales performance.

It enables users to quickly identify:

- Sales trends
- Product performance
- Customer purchasing behavior
- Territory-wise sales
- Product category contribution
- Business growth

---

# 📌 Key Performance Indicators (KPIs)

The dashboard includes the following KPI cards:

| KPI | Description |
|------|-------------|
| 📦 Total Orders | Total number of customer orders |
| 🛒 Total Quantity Sold | Total products sold |
| 👥 Unique Customers | Number of unique customers |
| 📊 Average Quantity per Order | Average quantity sold per order |

These KPIs provide a quick summary of overall business performance.

---

# 📉 Dashboard Visualizations

The dashboard includes the following visualizations:

### 📈 Monthly Sales Trend

**Visual:** Line Chart

Displays monthly sales quantity trends over time.

Business Insight:

- Identify seasonal trends
- Monitor business growth
- Compare monthly performance

---

### 🏆 Top Selling Products

**Visual:** Clustered Bar Chart

Displays the highest-selling products based on total quantity sold.

Business Insight:

- Identify best-selling products
- Support inventory planning
- Improve marketing strategies

---

### 🛍️ Sales by Product Category

**Visual:** Clustered Column Chart

Displays product category performance.

Business Insight:

- Compare category sales
- Identify high-performing product segments

---

### 👥 Customer Purchases by Income Band

**Visual:** Stacked Bar Chart

Displays customer purchases grouped by income band and gender.

Business Insight:

- Understand customer demographics
- Analyze purchasing behavior

---

### 📊 Year-wise Sales Trend

**Visual:** Area Chart

Displays yearly sales quantity trends.

Business Insight:

- Monitor long-term business growth
- Compare yearly performance

---

### 🥧 Sales Distribution by Product Category

**Visual:** Pie Chart

Displays the contribution of each product category to overall sales.

Business Insight:

- Identify dominant product categories
- Analyze category contribution

---

# 📷 Dashboard Screenshot

<img width="1330" height="743" alt="dashboard_screenshot" src="https://github.com/user-attachments/assets/cc0e1f73-38a4-4e48-883b-3f8e2d058f93" />


---

# 📊 Business Insights

The dashboard provides several business insights, including:

### 📦 Sales Performance

- Monitor total sales volume
- Track monthly growth
- Measure yearly performance

---

### 🛒 Product Analysis

- Identify best-selling products
- Compare product categories
- Evaluate product demand

---

### 👥 Customer Analytics

- Understand customer purchasing patterns
- Analyze purchases across income bands
- Compare purchasing behavior by gender

---

### 🌍 Territory Performance

- Evaluate regional sales
- Compare territory performance
- Identify high-performing sales regions

---

# 💼 Business Value

The dashboard enables stakeholders to:

- Monitor business performance
- Identify sales trends
- Support inventory planning
- Improve customer targeting
- Make data-driven decisions

---

# 🚀 Project Outcome

This project successfully demonstrates an end-to-end cloud-based data engineering solution.

The implementation includes:

✔ Metadata-driven Data Ingestion

✔ Azure Data Factory Pipeline

✔ Azure Data Lake Gen2

✔ Azure Databricks (PySpark)

✔ Azure Synapse Serverless SQL

✔ Medallion Architecture

✔ CETAS Implementation

✔ Power BI Dashboard

✔ Business Analytics

---


# 🌟 Project Highlights

This project demonstrates practical implementation of:

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Azure Synapse Analytics
- Serverless SQL Pool
- OPENROWSET
- CETAS
- Power BI
- Medallion Architecture
- Metadata-Driven Pipeline
- Cloud Data Engineering

---

# 📈 End-to-End Pipeline Summary
```
GitHub (AdventureWorks Dataset)
            │
            ▼
Azure Data Factory
(Lookup → ForEach → Copy Activity)
            │
            ▼
Azure Data Lake Gen2
Bronze Layer (Raw CSV)
            │
            ▼
Azure Databricks
(PySpark Transformations)
            │
            ▼
Azure Data Lake Gen2
Silver Layer (Parquet)
            │
            ▼
Azure Synapse Serverless SQL
(OPENROWSET + SQL + CETAS)
            │
            ▼
Azure Data Lake Gen2
Gold Layer (Reporting Tables)
            │
            ▼
Power BI Dashboard
```

---

# 🚀 How to Run the Project

Follow the steps below to reproduce the project.

## Prerequisites

Before running this project, ensure you have access to:

- Microsoft Azure Subscription
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks Workspace
- Azure Synapse Analytics Workspace
- Microsoft Power BI Desktop
- GitHub

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/<your-github-username>/Data-Engineering-Project.git
```

---

## Step 2 — Upload the Dataset

Upload all AdventureWorks CSV files and `metadata.json` to your GitHub repository (or another supported source location).

---

## Step 3 — Configure Azure Data Factory

Create:

- Linked Services
- HTTP Dataset
- ADLS Dataset
- Configuration Dataset

Import or recreate the metadata-driven pipeline.

---

## Step 4 — Execute the Pipeline

Run the Azure Data Factory pipeline.

The pipeline will:

- Read metadata.json
- Iterate using ForEach
- Copy every dataset
- Store raw CSV files inside the Bronze layer

---

## Step 5 — Execute Databricks Notebook

Run the Databricks notebook.

The notebook will:

- Read Bronze CSV files
- Perform transformations
- Create Fact and Dimension tables
- Write Parquet files into the Silver layer

---

## Step 6 — Execute Synapse SQL Scripts

Run the SQL scripts in the following order:

1. Create External Data Source
2. Create External File Format
3. Sales Summary
4. Product Performance
5. Customer Summary
6. Territory Sales
7. Return Analysis
8. Top Customers

These scripts generate reporting datasets in the Gold layer.

---

## Step 7 — Open Power BI

Connect Power BI to:

Azure Synapse Serverless SQL Endpoint

Import the Gold tables and refresh the report.

---

# 📁 Folder Structure

Data-Engineering-Project/
│
├── AdventureWorks/
├── Architecture/
├── Azure-Data-Factory/
├── Azure-Data-Lake/
├── Azure-Databricks/
├── Azure-Synapse/
├── Power-BI/
├── Screenshots/
└── README.md
```

---

# 📚 Key Learnings

During this project, the following Azure Data Engineering concepts were implemented:

- Metadata-driven ingestion
- Dynamic parameterization
- Azure Data Factory orchestration
- Medallion Architecture
- Azure Data Lake Storage Gen2
- Distributed data processing with PySpark
- Data cleansing and transformation
- Fact and Dimension modeling
- Apache Parquet optimization
- Azure Synapse Serverless SQL
- OPENROWSET
- CETAS
- Analytical SQL queries
- Power BI dashboard development

---

# 🧠 Skills Demonstrated

## Azure

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- Azure Synapse Analytics

---

## Data Engineering

- ETL / ELT Pipelines
- Metadata-driven pipelines
- Medallion Architecture
- Data Lake Design
- Data Transformation
- Data Modeling

---

## Programming

- PySpark
- SQL
- JSON

---

## Analytics

- Business Intelligence
- Data Visualization
- Dashboard Design

---

## Cloud

- Microsoft Azure
- Cloud Storage
- Serverless Analytics

---

# 💼 Project Highlights

✅ End-to-End Azure Data Engineering Solution

✅ Metadata-Driven Pipeline

✅ Dynamic Dataset Parameterization

✅ Azure Data Factory

✅ Azure Data Lake Storage Gen2

✅ Azure Databricks

✅ PySpark Transformations

✅ Medallion Architecture

✅ Azure Synapse Serverless SQL

✅ OPENROWSET

✅ CETAS

✅ Power BI Dashboard

---

# 🔮 Future Enhancements

Potential improvements for future versions of this project include:

- Incremental Data Loading
- Change Data Capture (CDC)
- Delta Lake Implementation
- Slowly Changing Dimensions (SCD Type 2)
- Data Quality Validation
- Pipeline Scheduling
- Pipeline Monitoring
- Azure Key Vault Integration
- CI/CD using Azure DevOps or GitHub Actions
- Automated Data Validation
- Parameterized SQL Scripts

---

# ❓ Interview Highlights

This project demonstrates practical experience with:

- Building metadata-driven Azure Data Factory pipelines
- Designing Bronze, Silver and Gold layers
- Processing large datasets using PySpark
- Implementing Fact and Dimension tables
- Querying Data Lake using Serverless SQL
- Creating reporting datasets using CETAS
- Developing interactive Power BI dashboards
- Designing scalable cloud data engineering solutions

---

# 📸 Project Screenshots

Implementation screenshots are available inside the following folders:

- Azure-Data-Factory/
- Azure-Data-Lake/
- Azure-Databricks/
- Azure-Synapse/
- Power-BI/

Each folder contains screenshots demonstrating the implementation of the corresponding Azure service.

---

# 🙋 Author

**Sohail Akhter**

Information Technology Graduate | Azure Data Engineering Enthusiast

GitHub: https://github.com/sohailGHUB

LinkedIn: https://linkedin.com/in/sohail-akhter

---


# ⭐ Support

If you found this repository helpful:

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---


## Thank You for Visiting!

If you have any suggestions or feedback, feel free to connect with me.

Happy Learning! 🚀



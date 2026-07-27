# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Layer Script
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Access using Service Principal

# COMMAND ----------


spark.conf.set("fs.azure.account.auth.type.datalake001100.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.datalake001100.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.datalake001100.dfs.core.windows.net", <service-principal ID>)
spark.conf.set("fs.azure.account.oauth2.client.secret.datalake001100.dfs.core.windows.net", <client-secret>)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.datalake001100.dfs.core.windows.net", "https://login.microsoftonline.com/a53aec34-2b62-4f0a-b38b-8bc5cdd745cb/oauth2/token")

# COMMAND ----------

# MAGIC %md
# MAGIC read calender data 
# MAGIC

# COMMAND ----------

df_calendar = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Calendar",
    header=True,
    inferSchema=True
)

display(df_calendar)


# COMMAND ----------

# MAGIC %md
# MAGIC read customers

# COMMAND ----------

df_customers = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Customers",
    header=True,
    inferSchema=True
)

display(df_customers)

# COMMAND ----------

# MAGIC %md
# MAGIC read product categories
# MAGIC

# COMMAND ----------

df_product_categories = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Product_Categories",
    header=True,
    inferSchema=True
)

display(df_product_categories)

# COMMAND ----------

# MAGIC %md
# MAGIC product sub-categories

# COMMAND ----------

df_product_subcategories = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Product_Subcategories",
    header=True,
    inferSchema=True
)

display(df_product_subcategories)

# COMMAND ----------

# MAGIC %md
# MAGIC products

# COMMAND ----------

df_products = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Products",
    header=True,
    inferSchema=True
)

display(df_products)

# COMMAND ----------

# MAGIC %md
# MAGIC returns

# COMMAND ----------

df_returns = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Returns",
    header=True,
    inferSchema=True
)

display(df_returns)

# COMMAND ----------

# MAGIC %md
# MAGIC sales 2015

# COMMAND ----------

df_sales_2015 = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Sales_2015",
    header=True,
    inferSchema=True
)

display(df_sales_2015)

# COMMAND ----------

# MAGIC %md
# MAGIC sales 2016

# COMMAND ----------

df_sales_2016 = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Sales_2016",
    header=True,
    inferSchema=True
)

display(df_sales_2016)

# COMMAND ----------

# MAGIC %md
# MAGIC sales 2017

# COMMAND ----------

df_sales_2017 = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Sales_2017",
    header=True,
    inferSchema=True
)

display(df_sales_2017)

# COMMAND ----------

# MAGIC %md
# MAGIC territories

# COMMAND ----------

df_territories = spark.read.csv(
    "abfss://bronze@datalake001100.dfs.core.windows.net/AdventureWorks_Territories",
    header=True,
    inferSchema=True
)

display(df_territories)

# COMMAND ----------

# MAGIC %md
# MAGIC ##`TRANSFORMATIONS`

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformation 1: Calendar Dimension Enrichment**
# MAGIC Objective:
# MAGIC Transform the raw Calendar dataset into a reusable Date Dimension by:
# MAGIC
# MAGIC Converting the date column to DateType
# MAGIC Extracting Year, Month, Quarter, Week Number, Day Name
# MAGIC Creating Month-Year
# MAGIC Identifying weekends
# MAGIC
# MAGIC This dimension will be used throughout your Synapse views and Power BI reports.

# COMMAND ----------

# ==========================================
# Transformation 1 : Calendar Dimension
# ==========================================

from pyspark.sql.functions import *

# Convert Date column to DateType
df_calendar_silver = (
    df_calendar
    .withColumn("Date", to_date(col("Date")))
    .withColumn("Year", year(col("Date")))
    .withColumn("MonthNumber", month(col("Date")))
    .withColumn("MonthName", date_format(col("Date"), "MMMM"))
    .withColumn("Quarter", quarter(col("Date")))
    .withColumn("WeekNumber", weekofyear(col("Date")))
    .withColumn("DayName", date_format(col("Date"), "EEEE"))
    .withColumn(
        "WeekendFlag",
        when(dayofweek(col("Date")).isin(1,7), "Yes")
        .otherwise("No")
    )
    .withColumn("MonthYear", date_format(col("Date"), "MMM-yyyy"))
)

display(df_calendar_silver)

# COMMAND ----------

df_calendar_silver.write \
    .mode("overwrite") \
    .option("header", True) \
    .parquet(
        "abfss://silver@datalake001100.dfs.core.windows.net/Dim_Calendar/Dim_Calendar"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformation 2: Customer Dimension Enrichment**
# MAGIC Objective
# MAGIC
# MAGIC Transform the raw customer data into a business-friendly customer dimension by:
# MAGIC
# MAGIC Creating Full Name
# MAGIC Standardizing names using Proper Case
# MAGIC Creating Gender Description
# MAGIC Creating Home Owner Status
# MAGIC Creating Income Band
# MAGIC Creating Age Group
# MAGIC Removing duplicate customers
# MAGIC
# MAGIC This transformation will make customer segmentation in Power BI much easier.

# COMMAND ----------

# ==========================================
# Transformation 2 : Customer Dimension
# ==========================================

from pyspark.sql.functions import *

df_customers_silver = (
    df_customers

    # Remove duplicate customers
    .dropDuplicates(["CustomerKey"])

    # Convert BirthDate to Date
    .withColumn(
        "BirthDate",
        to_date(col("BirthDate"))
    )

    # Standardize Names
    .withColumn("Prefix", initcap(col("Prefix")))
    .withColumn("FirstName", initcap(col("FirstName")))
    .withColumn("LastName", initcap(col("LastName")))

    # Full Name
    .withColumn(
        "FullName",
        concat_ws(" ", col("FirstName"), col("LastName"))
    )

    # Calculate Age
    .withColumn(
        "Age",
        floor(datediff(current_date(), col("BirthDate")) / 365.25)
    )

    # Age Group
    .withColumn(
        "AgeGroup",
        when(col("Age") < 30, "Young Adults")
        .when((col("Age") >= 30) & (col("Age") < 45), "Adults")
        .when((col("Age") >= 45) & (col("Age") < 60), "Middle Age")
        .otherwise("Senior Citizens")
    )

    # Gender Description
    .withColumn(
        "GenderDescription",
        when(col("Gender") == "M", "Male")
        .when(col("Gender") == "F", "Female")
        .otherwise("Unknown")
    )

    # Home Owner Status
    .withColumn(
        "HomeOwnerStatus",
        when(col("HomeOwner") == "Y", "Home Owner")
        .when(col("HomeOwner") == "N", "Non Home Owner")
        .otherwise("Unknown")
    )

    # Convert Annual Income to Numeric
    .withColumn(
        "AnnualIncomeNumeric",
        regexp_replace(col("AnnualIncome"), "[$, ]", "").cast("int")
    )

    # Income Band
    .withColumn(
        "IncomeBand",
        when(col("AnnualIncomeNumeric") < 50000, "Low Income")
        .when(
            (col("AnnualIncomeNumeric") >= 50000) &
            (col("AnnualIncomeNumeric") < 80000),
            "Middle Income"
        )
        .when(
            (col("AnnualIncomeNumeric") >= 80000) &
            (col("AnnualIncomeNumeric") < 120000),
            "High Income"
        )
        .otherwise("Premium Income")
    )
)

display(df_customers_silver)

# COMMAND ----------

df_customers_silver.write \
    .mode("overwrite") \
    .parquet(
        "abfss://silver@datalake001100.dfs.core.windows.net/Dim_Customers/Dim_Customers"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformation 3: Product Categories & Product Subcategories Cleanup**
# MAGIC Objective
# MAGIC
# MAGIC Create clean dimension tables for:
# MAGIC
# MAGIC Product Categories
# MAGIC Product Subcategories
# MAGIC
# MAGIC These tables will later be joined with the Products table to build a complete Product Hierarchy.

# COMMAND ----------

# ==========================================
# Transformation 3A : Product Categories
# ==========================================

from pyspark.sql.functions import *

df_product_categories_silver = (
    df_product_categories

    # Remove duplicate categories
    .dropDuplicates(["ProductCategoryKey"])

    # Standardize Category Name
    .withColumn(
        "CategoryName",
        initcap(trim(col("CategoryName")))
    )
)

display(df_product_categories_silver)

# COMMAND ----------

df_product_categories_silver.write \
    .mode("overwrite") \
    .parquet(
        "abfss://silver@datalake001100.dfs.core.windows.net/Dim_Product_Categories/Dim_Product_Categories"
    )

# COMMAND ----------

# ==========================================
# Transformation 3B : Product Subcategories
# ==========================================

df_product_subcategories_silver = (
    df_product_subcategories

    # Remove duplicate subcategories
    .dropDuplicates(["ProductSubcategoryKey"])

    # Standardize Subcategory Name
    .withColumn(
        "SubcategoryName",
        initcap(trim(col("SubcategoryName")))
    )
)

display(df_product_subcategories_silver)

# COMMAND ----------

df_product_subcategories_silver.write \
    .mode("overwrite") \
    .parquet(
        "abfss://silver@datalake001100.dfs.core.windows.net/Dim_Product_Subcategories/Dim_Product_Subcategories"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformation 4: Product Dimension Enrichment**
# MAGIC Objective
# MAGIC
# MAGIC Transform the raw Products table into a business-friendly Product Dimension by:
# MAGIC
# MAGIC Removing duplicate products
# MAGIC Standardizing text columns
# MAGIC Handling missing values
# MAGIC Calculating Profit Per Unit
# MAGIC Calculating Profit Margin %
# MAGIC Creating Price Category
# MAGIC Creating Cost Category
# MAGIC
# MAGIC This dimension will be used heavily in Synapse and Power BI.

# COMMAND ----------

# ==========================================
# Transformation 4 : Product Dimension
# ==========================================

from pyspark.sql.functions import *

df_products_silver = (
    df_products

    # Remove duplicate products
    .dropDuplicates(["ProductKey"])

    # Standardize text columns
    .withColumn("ProductSKU", upper(trim(col("ProductSKU"))))
    .withColumn("ProductName", initcap(trim(col("ProductName"))))
    .withColumn("ModelName", initcap(trim(col("ModelName"))))
    .withColumn("ProductDescription", initcap(trim(col("ProductDescription"))))

    # Handle missing values
    .withColumn(
        "ProductColor",
        when(col("ProductColor").isNull(), "Unknown")
        .otherwise(initcap(trim(col("ProductColor"))))
    )

    .withColumn(
        "ProductSize",
        when(col("ProductSize").isNull(), "Unknown")
        .otherwise(trim(col("ProductSize")))
    )

    .withColumn(
        "ProductStyle",
        when(col("ProductStyle").isNull(), "Unknown")
        .otherwise(initcap(trim(col("ProductStyle"))))
    )

    # Profit Per Unit
    .withColumn(
        "ProfitPerUnit",
        round(col("ProductPrice") - col("ProductCost"), 2)
    )

    # Profit Margin %
    .withColumn(
        "ProfitMargin",
        round(
            ((col("ProductPrice") - col("ProductCost"))
            / col("ProductPrice")) * 100,
            2
        )
    )

    # Price Category
    .withColumn(
        "PriceCategory",
        when(col("ProductPrice") < 100, "Budget")
        .when(
            (col("ProductPrice") >= 100) &
            (col("ProductPrice") < 500),
            "Mid Range"
        )
        .otherwise("Premium")
    )

    # Cost Category
    .withColumn(
        "CostCategory",
        when(col("ProductCost") < 50, "Low Cost")
        .when(
            (col("ProductCost") >= 50) &
            (col("ProductCost") < 300),
            "Medium Cost"
        )
        .otherwise("High Cost")
    )
)

display(df_products_silver)

# COMMAND ----------

df_products_silver.write \
    .mode("overwrite") \
    .parquet(
        "abfss://silver@datalake001100.dfs.core.windows.net/Dim_Products/Dim_Products"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformation 5: Product Hierarchy Dimension**
# MAGIC Objective
# MAGIC
# MAGIC Create a single denormalized Product Hierarchy by joining:
# MAGIC
# MAGIC Dim_Products
# MAGIC Dim_Product_Subcategories
# MAGIC Dim_Product_Categories
# MAGIC
# MAGIC This avoids repeated joins in Synapse Serverless SQL and Power BI.

# COMMAND ----------

# ==========================================
# Transformation 5 : Product Hierarchy
# ==========================================

from pyspark.sql.functions import *

df_product_hierarchy = (
    df_products_silver.alias("p")

    .join(
        df_product_subcategories_silver.alias("ps"),
        col("p.ProductSubcategoryKey") == col("ps.ProductSubcategoryKey"),
        "left"
    )

    .join(
        df_product_categories_silver.alias("pc"),
        col("ps.ProductCategoryKey") == col("pc.ProductCategoryKey"),
        "left"
    )

    .select(
        col("p.ProductKey"),
        col("p.ProductSKU"),
        col("p.ProductName"),
        col("p.ModelName"),
        col("p.ProductDescription"),
        col("p.ProductColor"),
        col("p.ProductSize"),
        col("p.ProductStyle"),
        col("p.ProductCost"),
        col("p.ProductPrice"),
        col("p.ProfitPerUnit"),
        col("p.ProfitMargin"),
        col("p.PriceCategory"),
        col("p.CostCategory"),
        col("ps.ProductSubcategoryKey"),
        col("ps.SubcategoryName"),
        col("pc.ProductCategoryKey"),
        col("pc.CategoryName")
    )
)

display(df_product_hierarchy)

# COMMAND ----------

df_product_hierarchy.write \
    .mode("overwrite") \
    .parquet(
        "abfss://silver@datalake001100.dfs.core.windows.net/Dim_Product_Hierarchy/Dim_Product_Hierarchy"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformation 6: Create Fact_Sales**
# MAGIC Objective
# MAGIC
# MAGIC Create a single Sales Fact table by:
# MAGIC
# MAGIC Merging 2015, 2016, and 2017 sales
# MAGIC Removing duplicates
# MAGIC Converting date columns to DateType
# MAGIC Creating reporting columns:
# MAGIC SalesYear
# MAGIC SalesMonth
# MAGIC MonthName
# MAGIC Quarter
# MAGIC WeekNumber
# MAGIC DayName
# MAGIC
# MAGIC This table will later be joined with all the dimensions.

# COMMAND ----------

# ==========================================
# Transformation 6 : Fact Sales
# ==========================================

from pyspark.sql.functions import *

# Merge all sales data
df_sales = (
    df_sales_2015
    .unionByName(df_sales_2016)
    .unionByName(df_sales_2017)
)

# Create Fact Sales
df_fact_sales = (
    df_sales

    # Remove duplicate records
    .dropDuplicates()

    # Convert dates
    .withColumn(
        "OrderDate",
        to_date(col("OrderDate"))
    )

    .withColumn(
        "StockDate",
        to_date(col("StockDate"))
    )

    # Reporting Columns
    .withColumn(
        "SalesYear",
        year(col("OrderDate"))
    )

    .withColumn(
        "SalesMonth",
        month(col("OrderDate"))
    )

    .withColumn(
        "MonthName",
        date_format(col("OrderDate"), "MMMM")
    )

    .withColumn(
        "Quarter",
        quarter(col("OrderDate"))
    )

    .withColumn(
        "WeekNumber",
        weekofyear(col("OrderDate"))
    )

    .withColumn(
        "DayName",
        date_format(col("OrderDate"), "EEEE")
    )
)

display(df_fact_sales)

# COMMAND ----------

df_fact_sales.write \
    .mode("overwrite") \
    .parquet(
        "abfss://silver@datalake001100.dfs.core.windows.net/Fact_Sales/Fact_Sales"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformation 7: Create Fact_Returns**
# MAGIC Objective
# MAGIC
# MAGIC Transform the Returns dataset by:
# MAGIC
# MAGIC Removing duplicate records
# MAGIC Converting ReturnDate to DateType
# MAGIC Creating reporting columns:
# MAGIC ReturnYear
# MAGIC ReturnMonth
# MAGIC MonthName
# MAGIC Quarter
# MAGIC WeekNumber
# MAGIC DayName
# MAGIC
# MAGIC This table will later be joined with Product and Territory dimensions to analyze return trends.

# COMMAND ----------

# ==========================================
# Transformation 7 : Fact Returns
# ==========================================

from pyspark.sql.functions import *

df_fact_returns = (
    df_returns

    # Remove duplicate records
    .dropDuplicates()

    # Convert ReturnDate to Date
    .withColumn(
        "ReturnDate",
        to_date(col("ReturnDate"))
    )

    # Reporting Columns
    .withColumn(
        "ReturnYear",
        year(col("ReturnDate"))
    )

    .withColumn(
        "ReturnMonth",
        month(col("ReturnDate"))
    )

    .withColumn(
        "MonthName",
        date_format(col("ReturnDate"), "MMMM")
    )

    .withColumn(
        "Quarter",
        quarter(col("ReturnDate"))
    )

    .withColumn(
        "WeekNumber",
        weekofyear(col("ReturnDate"))
    )

    .withColumn(
        "DayName",
        date_format(col("ReturnDate"), "EEEE")
    )
)

display(df_fact_returns)

# COMMAND ----------

df_fact_returns.write \
    .mode("overwrite") \
    .parquet(
        "abfss://silver@datalake001100.dfs.core.windows.net/Fact_Returns/Fact_Returns"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformation 8: Territory Dimension**
# MAGIC Objective
# MAGIC
# MAGIC Clean and enrich the Territory dimension by:
# MAGIC
# MAGIC Removing duplicates
# MAGIC Trimming whitespace
# MAGIC Converting names to Proper Case
# MAGIC Creating a new RegionCountry column for easier reporting

# COMMAND ----------

# ==========================================
# Transformation 8 : Territory Dimension
# ==========================================

from pyspark.sql.functions import *

df_territories_silver = (
    df_territories

    # Remove duplicate territories
    .dropDuplicates(["SalesTerritoryKey"])

    # Clean text columns
    .withColumn(
        "Region",
        initcap(trim(col("Region")))
    )

    .withColumn(
        "Country",
        initcap(trim(col("Country")))
    )

    .withColumn(
        "Continent",
        initcap(trim(col("Continent")))
    )

    # Reporting column
    .withColumn(
        "RegionCountry",
        concat_ws(" - ", col("Region"), col("Country"))
    )
)

display(df_territories_silver)

# COMMAND ----------

df_territories_silver.write \
    .mode("overwrite") \
    .parquet(
        "abfss://silver@datalake001100.dfs.core.windows.net/Dim_Territories/Dim_Territories"
    )

# COMMAND ----------

# MAGIC %md
# MAGIC
CREATE MASTER KEY ENCRYPTION BY PASSWORD = <master-key-password>;

CREATE DATABASE SCOPED CREDENTIAL WorkspaceIdentity
WITH IDENTITY = 'Managed Identity';

CREATE EXTERNAL DATA SOURCE silver_ds
WITH (
    LOCATION = 'https://datalake001100.blob.core.windows.net/silver',
    CREDENTIAL = WorkspaceIdentity
);

CREATE EXTERNAL DATA SOURCE gold_ds
WITH (
    LOCATION = 'https://datalake001100.blob.core.windows.net/gold',
    CREDENTIAL = WorkspaceIdentity
);

CREATE EXTERNAL FILE FORMAT parquet_format
WITH (
    FORMAT_TYPE = PARQUET
);


--BUSINESS LOGIC SQL QUERIES
/*
This table will contain:

SalesYear
Quarter
SalesMonth
MonthName
Total Orders
Total Quantity Sold
Average Quantity Per Order
Unique Customers
Unique Products
Unique Territories
*/

CREATE EXTERNAL TABLE gold.sales_summary
WITH (
    LOCATION = 'sales_summary',
    DATA_SOURCE = gold_ds,
    FILE_FORMAT = parquet_format
)
AS

WITH Sales_CTE AS
(
    SELECT
        SalesYear,
        Quarter,
        SalesMonth,
        MonthName,
        OrderNumber,
        OrderQuantity,
        CustomerKey,
        ProductKey,
        TerritoryKey
    FROM OPENROWSET(
        BULK 'Fact_Sales/Fact_Sales/',
        DATA_SOURCE = 'silver_ds',
        FORMAT = 'PARQUET'
    ) AS sales
)

SELECT
    SalesYear,
    Quarter,
    SalesMonth,
    MonthName,

    COUNT(DISTINCT OrderNumber) AS TotalOrders,
    SUM(OrderQuantity) AS TotalQuantitySold,
    AVG(CAST(OrderQuantity AS FLOAT)) AS AvgQuantityPerOrder,

    COUNT(DISTINCT CustomerKey) AS UniqueCustomers,
    COUNT(DISTINCT ProductKey) AS UniqueProducts,
    COUNT(DISTINCT TerritoryKey) AS UniqueTerritories

FROM Sales_CTE

GROUP BY
    SalesYear,
    Quarter,
    SalesMonth,
    MonthName;

/*
    Gold Table 2: gold.product_performance
Business Objective

Answer questions like:

Which products sell the most?
Which products are top performers?
Which category contributes the most sales?
What is each product's sales rank?
*/

CREATE EXTERNAL TABLE gold.product_performance
WITH (
    LOCATION = 'product_performance',
    DATA_SOURCE = gold_ds,
    FILE_FORMAT = parquet_format
)
AS

WITH ProductSales AS
(
    SELECT
        p.ProductKey,
        p.ProductName,
        ph.CategoryName,
        ph.SubcategoryName,
        COUNT(DISTINCT s.OrderNumber) AS TotalOrders,
        SUM(s.OrderQuantity) AS TotalQuantitySold
    FROM OPENROWSET(
            BULK 'Fact_Sales/Fact_Sales/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS s

    INNER JOIN OPENROWSET(
            BULK 'Dim_Products/Dim_Products/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS p
        ON s.ProductKey = p.ProductKey

    INNER JOIN OPENROWSET(
            BULK 'Dim_Product_Hierarchy/Dim_Product_Hierarchy/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS ph
        ON p.ProductKey = ph.ProductKey

    GROUP BY
        p.ProductKey,
        p.ProductName,
        ph.CategoryName,
        ph.SubcategoryName
)

SELECT
    ProductKey,
    ProductName,
    CategoryName,
    SubcategoryName,
    TotalOrders,
    TotalQuantitySold,
    RANK() OVER (ORDER BY TotalQuantitySold DESC) AS ProductRank
FROM ProductSales;



/*
Gold Table 3: gold.customer_summary
Business Purpose

This table provides customer-level insights such as:

Number of orders placed
Total quantity purchased
Average quantity per order
Customer income and occupation
Customer rank based on quantity purchased
*/

CREATE EXTERNAL TABLE gold.customer_summary
WITH (
    LOCATION = 'customer_summary',
    DATA_SOURCE = gold_ds,
    FILE_FORMAT = parquet_format
)
AS

WITH CustomerSales AS
(
    SELECT
        c.CustomerKey,
        c.FullName,
        c.GenderDescription,
        c.Occupation,
        c.IncomeBand,

        COUNT(DISTINCT s.OrderNumber) AS TotalOrders,
        SUM(s.OrderQuantity) AS TotalQuantityPurchased,
        AVG(CAST(s.OrderQuantity AS FLOAT)) AS AvgQuantityPerOrder

    FROM OPENROWSET(
            BULK 'Fact_Sales/Fact_Sales/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS s

    INNER JOIN OPENROWSET(
            BULK 'Dim_Customers/Dim_Customers/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS c
        ON s.CustomerKey = c.CustomerKey

    GROUP BY
        c.CustomerKey,
        c.FullName,
        c.GenderDescription,
        c.Occupation,
        c.IncomeBand
)

SELECT
    CustomerKey,
    FullName,
    GenderDescription,
    Occupation,
    IncomeBand,
    TotalOrders,
    TotalQuantityPurchased,
    AvgQuantityPerOrder,
    DENSE_RANK() OVER (ORDER BY TotalQuantityPurchased DESC) AS CustomerRank
FROM CustomerSales;


/*
    Gold Table 4: gold.territory_sales
Business Purpose

This table answers:

Which continent has the highest sales?
Which country sells the most?
Which region performs best?
How many customers and products are involved in each territory?
*/

CREATE EXTERNAL TABLE gold.territory_sales
WITH (
    LOCATION = 'territory_sales',
    DATA_SOURCE = gold_ds,
    FILE_FORMAT = parquet_format
)
AS

WITH TerritorySales AS
(
    SELECT
        t.Continent,
        t.Country,
        t.Region,

        COUNT(DISTINCT s.OrderNumber) AS TotalOrders,
        SUM(s.OrderQuantity) AS TotalQuantitySold,
        COUNT(DISTINCT s.CustomerKey) AS UniqueCustomers,
        COUNT(DISTINCT s.ProductKey) AS UniqueProducts

    FROM OPENROWSET(
            BULK 'Fact_Sales/Fact_Sales/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS s

    INNER JOIN OPENROWSET(
            BULK 'Dim_Territories/Dim_Territories/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS t
        ON s.TerritoryKey = t.SalesTerritoryKey

    GROUP BY
        t.Continent,
        t.Country,
        t.Region
)

SELECT *
FROM TerritorySales;

/*
    Gold Table 5: gold.return_analysis
Business Purpose

This table answers:

Which products are returned the most?
What is the return rate for each product?
Which product categories have the highest returns?
*/

CREATE EXTERNAL TABLE gold.return_analysis
WITH (
    LOCATION = 'return_analysis',
    DATA_SOURCE = gold_ds,
    FILE_FORMAT = parquet_format
)
AS

WITH SalesSummary AS
(
    SELECT
        ProductKey,
        SUM(OrderQuantity) AS TotalSold
    FROM OPENROWSET(
            BULK 'Fact_Sales/Fact_Sales/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS sales
    GROUP BY ProductKey
),

ReturnSummary AS
(
    SELECT
        ProductKey,
        SUM(ReturnQuantity) AS TotalReturned
    FROM OPENROWSET(
            BULK 'Fact_Returns/Fact_Returns/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS returns
    GROUP BY ProductKey
)

SELECT
    p.ProductKey,
    p.ProductName,
    ph.CategoryName,
    ph.SubcategoryName,

    s.TotalSold,
    ISNULL(r.TotalReturned, 0) AS TotalReturned,

    ROUND(
        CAST(ISNULL(r.TotalReturned, 0) AS FLOAT)
        / NULLIF(s.TotalSold, 0) * 100,
        2
    ) AS ReturnRate

FROM SalesSummary s

LEFT JOIN ReturnSummary r
    ON s.ProductKey = r.ProductKey

INNER JOIN OPENROWSET(
        BULK 'Dim_Products/Dim_Products/',
        DATA_SOURCE = 'silver_ds',
        FORMAT = 'PARQUET'
    ) AS p
    ON s.ProductKey = p.ProductKey

INNER JOIN OPENROWSET(
        BULK 'Dim_Product_Hierarchy/Dim_Product_Hierarchy/',
        DATA_SOURCE = 'silver_ds',
        FORMAT = 'PARQUET'
    ) AS ph
    ON p.ProductKey = ph.ProductKey;


/*
    Gold Table 6: gold.top_customers
Business Purpose

This table answers:

Who are the top customers?
How do customers rank based on purchases?
Who are the Top 10 customers?
*/

CREATE EXTERNAL TABLE gold.top_customers
WITH (
    LOCATION = 'top_customers',
    DATA_SOURCE = gold_ds,
    FILE_FORMAT = parquet_format
)
AS

WITH CustomerSales AS
(
    SELECT
        c.CustomerKey,
        c.FullName,
        c.GenderDescription,
        c.Occupation,
        c.IncomeBand,

        COUNT(DISTINCT s.OrderNumber) AS TotalOrders,
        SUM(s.OrderQuantity) AS TotalQuantityPurchased

    FROM OPENROWSET(
            BULK 'Fact_Sales/Fact_Sales/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS s

    INNER JOIN OPENROWSET(
            BULK 'Dim_Customers/Dim_Customers/',
            DATA_SOURCE = 'silver_ds',
            FORMAT = 'PARQUET'
        ) AS c
        ON s.CustomerKey = c.CustomerKey

    GROUP BY
        c.CustomerKey,
        c.FullName,
        c.GenderDescription,
        c.Occupation,
        c.IncomeBand
)

SELECT
    CustomerKey,
    FullName,
    GenderDescription,
    Occupation,
    IncomeBand,
    TotalOrders,
    TotalQuantityPurchased,

    ROW_NUMBER() OVER (
        ORDER BY TotalQuantityPurchased DESC
    ) AS RowNum,

    RANK() OVER (
        ORDER BY TotalQuantityPurchased DESC
    ) AS CustomerRank,

    DENSE_RANK() OVER (
        ORDER BY TotalQuantityPurchased DESC
    ) AS DenseCustomerRank

FROM CustomerSales;

-- create views

CREATE VIEW gold.calendar
AS
SELECT *
FROM OPENROWSET(
    BULK 'https://datalake001100.blob.core.windows.net/silver/Dim_Calendar/Dim_Calendar/',
    FORMAT = 'PARQUET'
) AS query1;


CREATE VIEW gold.customers
AS
SELECT *
FROM OPENROWSET(
    BULK 'https://datalake001100.blob.core.windows.net/silver/Dim_Customers/Dim_Customers/',
    FORMAT = 'PARQUET'
) AS query1;

CREATE VIEW gold.products
AS
SELECT *
FROM OPENROWSET(
    BULK 'https://datalake001100.blob.core.windows.net/silver/Dim_Products/Dim_Products/',
    FORMAT = 'PARQUET'
) AS query1;

CREATE VIEW gold.product_categories
AS
SELECT *
FROM OPENROWSET(
    BULK 'https://datalake001100.blob.core.windows.net/silver/Dim_Product_Categories/Dim_Product_Categories/',
    FORMAT = 'PARQUET'
) AS query1;

CREATE VIEW gold.product_subcategories
AS
SELECT *
FROM OPENROWSET(
    BULK 'https://datalake001100.blob.core.windows.net/silver/Dim_Product_Subcategories/Dim_Product_Subcategories/',
    FORMAT = 'PARQUET'
) AS query1;

CREATE VIEW gold.product_hierarchy
AS
SELECT *
FROM OPENROWSET(
    BULK 'https://datalake001100.blob.core.windows.net/silver/Dim_Product_Hierarchy/Dim_Product_Hierarchy/',
    FORMAT = 'PARQUET'
) AS query1;

CREATE VIEW gold.territories
AS
SELECT *
FROM OPENROWSET(
    BULK 'https://datalake001100.blob.core.windows.net/silver/Dim_Territories/Dim_Territories/',
    FORMAT = 'PARQUET'
) AS query1;

CREATE VIEW gold.sales
AS
SELECT *
FROM OPENROWSET(
    BULK 'https://datalake001100.blob.core.windows.net/silver/Fact_Sales/Fact_Sales/',
    FORMAT = 'PARQUET'
) AS query1;

CREATE VIEW gold.returns
AS
SELECT *
FROM OPENROWSET(
    BULK 'https://datalake001100.blob.core.windows.net/silver/Fact_Returns/Fact_Returns/',
    FORMAT = 'PARQUET'
) AS query1;

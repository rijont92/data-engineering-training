# Pipeline Summary - Day 10

## Project Overview

This project implements a complete CSV data pipeline using Python.
The pipeline follows the Bronze -> Silver -> Gold architecture commonly used
in data engineering workflows.

The goal of the pipeline is to transform raw CSV files into clean,
validated datasets and create business-ready reports without using pandas.

---

## Pipeline Flow

### 1. Bronze Layer

The Bronze layer loads raw source data from CSV files:

- orders_raw.csv
- customers_raw.csv
- products_raw.csv

The raw data is kept unchanged to preserve the original source data and allow
future reprocessing or debugging.

The pipeline cleans only formatting issues such as extra spaces while loading
the data.

---

### 2. Silver Layer

The Silver layer is responsible for cleaning, validating, and enriching data.

Operations performed:

- Standardized order statuses.
- Standardized sales channels.
- Cleaned city names.
- Removed duplicate customers.
- Validated customer and product references.
- Checked order quantities and required fields.
- Detected invalid orders.
- Added calculated total order amounts.
- Joined order data with customer and product information.

Generated Silver files:

- customers_clean.csv
- products_clean.csv
- orders_clean.csv
- invalid_orders.csv

---

### 3. Gold Layer

The Gold layer creates analytics-ready reports for business use.

Generated reports:

- revenue_by_category.csv
- revenue_by_city.csv
- revenue_by_customer.csv
- top_products.csv
- executive_summary.txt

These reports provide insights about:

- Completed revenue performance.
- Best performing categories.
- Highest revenue cities.
- Top customers.
- Best selling products.
- Overall data quality.

---

## Data Quality

The pipeline includes validation checks to improve data reliability.

Examples of detected issues:

- Missing order IDs.
- Duplicate order IDs.
- Invalid customer IDs.
- Invalid product IDs.
- Missing dates.
- Invalid quantities.
- Invalid statuses.

Invalid records are separated from clean data and stored for investigation.

---

## Python Structure

The pipeline is organized using reusable functions instead of one long script.

Main responsibilities:

- Loading CSV files.
- Writing output files.
- Creating lookup dictionaries.
- Cleaning and validating data.
- Enriching orders.
- Creating business reports.
- Generating executive summaries.

The pipeline runs automatically from the `main()` function:

```python
if __name__ == "__main__":
    main()
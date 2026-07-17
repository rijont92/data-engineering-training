# Day 10 - Bronze / Silver / Gold Pipeline with Python

## Project goal

The goal of this project is to build a Python-based data engineering pipeline
using the Bronze → Silver → Gold architecture.

The pipeline simulates a Databricks-style medallion architecture by:

- Loading raw CSV data.
- Cleaning and validating records.
- Enriching datasets with customer and product information.
- Creating business-ready reports.

The project focuses on building a modular pipeline using Python functions
without using pandas.

---

# Bronze layer

## Overview

The Bronze layer stores the original raw source data.

Raw data is kept unchanged to preserve the original source of truth and allow
debugging, auditing, and future reprocessing.

## Files
data/bronze/
│
├── orders_raw.csv
├── customers_raw.csv
└── products_raw.csv


## Data issues identified

The raw datasets contained several quality problems:

- Inconsistent text formatting.
- Different status formats (`Completed`, `complete`, `done`).
- Different channel formats (`Online`, `online`, `web`).
- Missing values.
- Duplicate order IDs.
- Invalid quantities.
- Invalid product prices.
- Missing customer or product references.

---

# Silver layer

## Overview

The Silver layer contains cleaned, validated, and enriched data.

Only reliable records are allowed into Silver datasets.

## Cleaning and validation rules

The pipeline performs:

- Status normalization:
  - `completed`
  - `pending`
  - `cancelled`

- Channel normalization:
  - `online`
  - `store`
  - `unknown`

- City standardization.
- Duplicate customer removal.
- Product price validation.
- Quantity validation.
- Customer and product lookup validation.
- Duplicate order detection.

## Data enrichment

Additional columns added:

- `customer_name`
- `city`
- `product_name`
- `category`
- `price`
- `total_amount`

The `total_amount` value is calculated:
quantity * price

## Generated files
data/silver/

├── customers_clean.csv
├── products_clean.csv
├── orders_clean.csv
└── invalid_orders.csv
Invalid records are stored separately with validation failure reasons.

---

# Gold layer

## Overview

The Gold layer contains business-ready reports created from clean Silver data.

These outputs are designed for analytics and dashboard consumption.

## Generated reports
data/gold/

├── revenue_by_category.csv
├── revenue_by_city.csv
├── revenue_by_customer.csv
├── top_products.csv
└── executive_summary.txt


## Reports purpose

### revenue_by_category.csv

Answers:

- Which categories generate the highest revenue?
- How many completed orders does each category have?

### revenue_by_city.csv

Answers:

- Which cities generate the most revenue?
- Which locations have the most completed orders?

### revenue_by_customer.csv

Answers:

- Which customers generate the highest revenue?
- Who are the top customers?

### top_products.csv

Answers:

- Which products sell the most?
- Which products generate the highest revenue?

### executive_summary.txt

Provides:

- Pipeline statistics.
- Completed revenue.
- Top category.
- Top city.
- Top customer.
- Top product.
- Data quality summary.

---

# How to run the pipeline

Run:


python3 pipeline.py

The pipeline automatically:

Creates output folders.
Loads Bronze data.
Creates Silver datasets.
Generates Gold reports.


Files generated
After running the pipeline:
data/

├── silver/
│   ├── customers_clean.csv
│   ├── products_clean.csv
│   ├── orders_clean.csv
│   └── invalid_orders.csv
│
└── gold/
    ├── revenue_by_category.csv
    ├── revenue_by_city.csv
    ├── revenue_by_customer.csv
    ├── top_products.csv
    └── executive_summary.txt

Data quality checks

The pipeline validates:

Missing order IDs.
Duplicate order IDs.
Invalid customer IDs.
Invalid product IDs.
Missing order dates.
Invalid quantities.
Invalid statuses.
Invalid prices.

Invalid records are separated from clean data to prevent incorrect business
reports.

Business insights

The Gold reports can be used to analyze:

Revenue performance by category.
Revenue performance by city.
Customer purchasing behavior.
Product performance.
Overall completed revenue.

Example insights:

The highest revenue category can be identified.
The top-performing city can be discovered.
The best customers and products can be ranked.
Data quality problems can be monitored.
What I can explain and defend

I can explain:

Why Bronze keeps raw data unchanged.
Why Silver is responsible for cleaning and validation.
Why Gold contains business-level reports.
How lookup dictionaries connect datasets.
How invalid records are detected.
How revenue calculations are created.
Why dashboards should use Gold outputs instead of raw data.
What was difficult

The most challenging parts were:

Creating validation rules without pandas.
Handling inconsistent raw data values.
Designing reusable functions.
Managing invalid records separately.
Connecting customers, products, and orders correctly.
What I would improve next

Future improvements:

Add automated tests using pytest.
Add logging instead of only print statements.
Add configuration files for paths and rules.
Add date format validation.
Connect the pipeline to a database.
Run the pipeline using Apache Spark or Databricks for larger datasets.
Schedule automatic pipeline execution.
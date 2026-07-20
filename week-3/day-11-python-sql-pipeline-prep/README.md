# Day 11 - Python + SQL Pipeline Preparation

## Project Goal

Build a small data engineering pipeline that transforms raw CSV data into clean trusted data and business reports.

Workflow:
Bronze → Silver → Gold

---

# Bronze Data

Raw files:

- `orders_raw.csv`
- `customers_raw.csv`
- `products_raw.csv`

Location:
data/bronze/


Problems found:

- Missing quantities
- Invalid quantities
- Wrong status values
- Missing dates
- Invalid customer/product IDs
- Duplicate orders
- Different city formats

---

# Silver Data

The pipeline validates and cleans raw data.

Validation rules:

- Quantity must be positive
- Status must be valid
- Order date is required
- Customer and product IDs must exist
- Duplicate orders are rejected

Invalid records are saved in:
data/silver/invalid_orders.csv

Clean enriched orders are saved in:
data/silver/orders_clean.csv


Normalization:

- Status → completed, pending, cancelled
- Cities → consistent format
- Channels → online, store, web, bank, unknown

---

# Gold Reports

Generated business reports:
data/gold/


Files:

- `revenue_by_city.csv`
- `revenue_by_category.csv`
- `top_customers.csv`
- `executive_summary.txt`

Completed revenue only includes orders with:
status = completed


---

# Python vs SQL

## Python

Used for:

- Reading CSV files
- Validation
- Cleaning data
- Enrichment
- Creating Silver and Gold outputs

## SQL

Used for:

- Business reporting
- Revenue analysis
- Grouping and aggregation
- Finding top customers and cities

---

# Data Quality Notes

Invalid data is not deleted.

It is stored separately with an explanation of why it failed validation.

---

# Business Insights

The reports help understand:

- Revenue by city
- Revenue by category
- Top customers
- Completed sales performance

---

# What I Can Explain Live

- Bronze, Silver, Gold layers
- Data validation process
- Python pipeline logic
- SQL reporting logic
- Completed revenue calculation

---

# Future Improvements

- Add automated tests
- Add logging
- Move data storage to a database
- Run pipeline in Databricks

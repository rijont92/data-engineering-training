# Day 9 - CSV Data Pipeline: From Raw Data to Clean Reports

## Goal

The goal of this practice is to build a Python CSV data pipeline that loads raw data, cleans and validates records, enriches information, and creates trusted business reports.

---

## Bronze, Silver, Gold

### Bronze Layer
Contains raw source files without changes:

- orders_raw.csv
- customers_raw.csv
- products_raw.csv

### Silver Layer
Contains cleaned and validated data:

- orders_clean.csv
- invalid_orders.csv

Data is normalized, validated, and enriched with customer and product information.

### Gold Layer
Contains business reports created from Silver data:

- business_summary.txt
- revenue_by_city.txt
- revenue_by_category.txt
- top_customers.txt
- top_products.txt

---

## Project Structure
data/
├── orders_raw.csv
├── customers_raw.csv
└── products_raw.csv

output/
├── orders_clean.csv
├── invalid_orders.csv
└── reports

csv_pipeline.py
pipeline_explanation.md
daily_report.txt
README.md


---

## How To Run

Run:

```bash```
python csv_pipeline.py
The script will load CSV files, validate and clean data, create Silver outputs, and generate Gold reports.

Outputs

Generated files:

orders_clean.csv - validated clean orders
invalid_orders.csv - rejected records with reasons
data_quality_report.txt - data quality results
business_summary.txt - business analysis report
Additional revenue and ranking reports
Why No Pandas?

Pandas was not used because this practice focuses on understanding the core pipeline logic first.

Manual Python logic helps understand:

Data loading
Validation
Cleaning
Joins using dictionaries
Transformations

These concepts are the foundation for larger tools like Spark and Databricks.
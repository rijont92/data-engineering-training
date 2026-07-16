# Day 9 - Pipeline Explanation

## Source Data:
The source data consists of three raw CSV files:
- orders_raw.csv
- customers_raw.csv
- products_raw.csv

These files contain the original data exactly as received, including missing values, inconsistent formatting, and invalid records.

## Ingestion:
The ingestion step reads the raw CSV files into Python using `csv.DictReader`. The data is loaded into lists of dictionaries so it can be processed by the pipeline.

## Bronze layer:
The Bronze layer represents the raw input data. No changes are made to the data at this stage. The pipeline simply loads the CSV files and prepares them for processing.

## Cleaning rules:
The pipeline standardizes inconsistent values before they are used.
- Convert status values like "Completed", "complete", and "done" to "completed".
- Convert city names to a consistent format (for example, "prishtina" becomes "Prishtina").
- Convert channel values like "Online" and "web" to "online".
- Replace missing channels with "unknown".

## Validation rules:
Each order is checked before it becomes clean data.
- order_id must exist.
- customer_id must exist and match a customer.
- product_id must exist and match a product.
- order_date must not be empty.
- quantity must be a positive integer.
- status must be valid after normalization.
- channel must be valid after normalization.

Invalid records are saved separately with the reason they failed validation.

## Silver layer:
The Silver layer contains only valid, cleaned, and standardized records. Invalid records are excluded from the clean dataset and written to `invalid_orders.csv`.

## Transformation rules:
The pipeline enriches each valid order by joining customer and product information.
It adds:
- customer_name
- city
- product_name
- category
- price
- total_amount (quantity × price)

## Gold layer:
The Gold layer contains business-ready reports created from the cleaned data. These reports are used for business analysis and decision-making.

## Business Output:
The pipeline generates:
- orders_clean.csv
- invalid_orders.csv
- data_quality_report.txt
- business_summary.txt

These outputs provide trusted data and business metrics such as completed revenue, revenue by category, and top customers.

## What makes this data trusted:
The data is trusted because every record is validated, cleaned, and enriched before being used. Invalid records are separated instead of ignored, and all business calculations are based only on the verified clean data.
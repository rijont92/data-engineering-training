# Layer Explanation - Day 10

## Bronze layer

The Bronze layer stores the original raw CSV data received from the source system.

Files stored in Bronze:
- orders_raw.csv
- customers_raw.csv
- products_raw.csv

We keep raw data unchanged because Bronze acts as the original source of truth.
Keeping the raw files allows us to trace data problems, reprocess data if needed,
and compare the cleaned data with the original input.

Data problems noticed in Bronze:
- Extra spaces in column names and values.
- Different formats for status values (Completed, completed, done).
- Different formats for sales channels (Online, online, web).
- Invalid quantities such as negative or missing values.
- Duplicate order IDs.
- Missing customer or product references.
- Missing required fields.

---

## Silver layer

The Silver layer contains cleaned, validated, and enriched data.

Cleaning rules applied:
- Removed unnecessary spaces from values and column names.
- Standardized order statuses:
  - completed
  - pending
  - cancelled
  - unknown
- Standardized sales channels:
  - online
  - store
  - unknown
- Standardized city names.
- Removed duplicate customers.
- Removed products with invalid prices.
- Validated order IDs, customer IDs, product IDs, dates, quantities, statuses, and channels.

Records that became invalid:
- Orders with missing order IDs.
- Duplicate order IDs.
- Orders referencing customers that do not exist.
- Orders referencing products that do not exist.
- Orders with missing order dates.
- Orders with invalid or negative quantities.
- Orders with invalid statuses.

Invalid records were stored separately in:
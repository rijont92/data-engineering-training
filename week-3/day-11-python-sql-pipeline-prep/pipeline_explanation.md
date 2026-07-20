# Day 11 Practice - Python + SQL Pipeline Preparation

## Part 1 - Data Understanding

### Raw Orders Analysis

The raw orders dataset contains **24 orders**.

The main columns in orders_raw.csv are:
- order_id
- customer_id
- product_id
- quantity
- status
- order_date
- channel

### Joining Logic

Orders are connected with other datasets using:

- orders.customer_id = customers.customer_id

This join is used to get customer information such as:
- customer_name
- city
- segment

- orders.product_id = products.product_id

This join is used to get product information such as:
- product_name
- category
- price

### Inconsistent Values Found

The raw data contains several quality issues:

#### Status inconsistencies:
- "completed"
- "Completed"
- "done"
- "canceled"
- "cancelled"

These values should be normalized into a standard format.

#### Channel inconsistencies:
- "online"
- "Online"
- "store"
- "Store"
- "web"
- "bank"
- missing values

Channels should be cleaned and standardized.

#### Missing values:
- Order 3 has missing quantity.
- Order 8 has missing status.
- Order 9 has missing order_date.
- Order 18 has missing channel.

#### Invalid numeric values:
- Order 6 has quantity = -1.
- Order 7 has quantity = "abc".
- Order 22 has quantity = 0.

Quantity must be a positive integer.

#### Invalid references:
- Order 17 contains product_id P999 which does not exist in products_raw.csv.

### Records That Should Not Be Trusted For Revenue

The following orders should not be used for revenue calculation:

- Orders with missing required fields.
- Orders with invalid quantity values.
- Orders with non-existing customer_id or product_id.
- Orders with missing product price.
- Orders that cannot be successfully validated.

Examples:
- Order 3 (missing quantity)
- Order 6 (negative quantity)
- Order 7 (invalid quantity)
- Order 8 (missing status)
- Order 9 (missing date)
- Order 17 (invalid product_id)
- Order 22 (quantity is zero)

### Bronze, Silver, and Gold Layers

## Bronze Layer

Bronze contains raw unprocessed data.

Files:
- data/bronze/orders_raw.csv
- data/bronze/customers_raw.csv
- data/bronze/products_raw.csv

The Bronze layer keeps the original data without manual cleaning.

## Silver Layer

Silver contains cleaned and validated data.

The Silver process includes:
- cleaning inconsistent values
- validating records
- removing invalid records
- joining customers and products
- adding calculated fields like total_amount

Example output:
- data/silver/orders_clean.csv

## Gold Layer

Gold contains business-ready reports created from Silver data.

Examples:
- revenue_by_category.csv
- revenue_by_city.csv
- revenue_by_customer.csv
- top_products.csv
- executive_summary.txt

The Gold layer is used for reporting and business analysis.
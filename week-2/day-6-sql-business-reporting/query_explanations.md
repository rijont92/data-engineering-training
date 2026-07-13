# Query Explanations - Day 6 SQL Business Reporting Sprint


## Query title: Completed revenue by category

File:
join_reports.sql

Business question:
Which product category generated the most completed revenue?

Tables used:
orders and products

Why JOIN is needed:
The orders table contains product_id, but category and price information are stored in the products table.

Why WHERE is needed:
Only completed orders should be included because they represent real revenue.

Why GROUP BY is needed:
We need one result row for each category.

What I understood:
This report shows which categories contribute the most money to the business.


---

## Query title: Completed revenue by product

File:
join_reports.sql

Business question:
Which products generate the most completed revenue?

Tables used:
orders and products

Why JOIN is needed:
The product name and price are stored in the products table.

Why WHERE is needed:
Pending and cancelled orders should not be counted as revenue.

Why GROUP BY is needed:
We need to calculate revenue separately for each product.

What I understood:
This helps identify the best-performing products.


---

## Query title: Top 3 customers by completed revenue

File:
join_reports.sql

Business question:
Who are the most valuable customers?

Tables used:
orders, customers, products

Why JOIN is needed:
Customer names are stored in customers and product prices are stored in products.

Why WHERE is needed:
Only completed purchases should affect customer revenue.

Why GROUP BY is needed:
Revenue needs to be calculated for each customer.

What I understood:
This report helps identify customers who bring the most revenue.


---

## Query title: Customers with more than one order

File:
join_reports.sql

Business question:
Which customers purchased more than once?

Tables used:
orders and customers

Why JOIN is needed:
The customer name is stored separately from order transactions.

Why HAVING is needed:
HAVING filters grouped results after counting orders.

Why GROUP BY is needed:
Orders need to be counted for each customer.

What I understood:
This helps identify returning customers.


---

## Query title: Order count by city

File:
join_reports.sql

Business question:
Which cities generate the most orders?

Tables used:
orders and customers

Why JOIN is needed:
City information is stored in customers.

Why GROUP BY is needed:
Orders need to be counted separately for each city.

What I understood:
This report helps compare customer activity between locations.


---

## Query title: Complete order report

File:
join_reports.sql

Business question:
How can we create a readable business order report?

Tables used:
orders, customers, products

Why JOIN is needed:
Information is separated into different tables.

Why GROUP BY is not needed:
This report shows individual orders, not summarized data.

What I understood:
JOINs allow technical IDs to become understandable business information.


---

## Query title: Completed revenue calculation

File:
basic_aggregations.sql

Business question:
How much real revenue was generated?

Tables used:
orders and products

Why JOIN is needed:
Quantity comes from orders and price comes from products.

Why WHERE is needed:
Only completed transactions should count.

What I understood:
Revenue should only include successful transactions.


---

## Query title: Potential value from non-completed orders

File:
basic_aggregations.sql

Business question:
How much value is currently pending or cancelled?

Tables used:
orders and products

Why JOIN is needed:
Price information comes from products.

Why WHERE is needed:
Only pending and cancelled orders should be included.

What I understood:
This value is useful for understanding possible future revenue but should not be treated as actual revenue.
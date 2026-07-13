# Day 6 - SQL Business Reporting Sprint

## Goal

This project focuses on creating business reports using SQL.
The main topics practiced were COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING, and JOINs.

The goal was to transform raw data from multiple tables into meaningful business insights.

---

## Dataset

The project uses three related tables:

- orders - stores transaction information
- customers - stores customer details
- products - stores product information

The tables are connected using customer_id and product_id.

---

## Files Included

- setup.sql - Creates tables and inserts dataset
- basic_aggregations.sql - Calculates basic metrics using COUNT, SUM, AVG, MIN, and MAX
- group_by_reports.sql - Creates grouped business reports using GROUP BY and HAVING
- join_reports.sql - Combines tables to create readable business reports
- business_report.md - Contains business insights from SQL results
- query_explanations.md - Explains important SQL queries
- daily_report.txt - Summary of the work completed
- screenshots/ - Contains query result screenshots

---

## How to Run

Run the SQL files in this order:

1. setup.sql
2. basic_aggregations.sql
3. group_by_reports.sql
4. join_reports.sql

The project was tested using SQLiteOnline.com.

---

## SQL Concepts Practiced

### Basic Aggregations

Used:
- COUNT() to count records
- SUM() to calculate totals
- AVG() to calculate averages
- MIN() to find minimum values
- MAX() to find maximum values

### GROUP BY

Used to create reports by:
- status
- date
- customer
- product
- category
- city

### HAVING

Used to filter grouped results, for example:
- customers with more than one order
- products with completed quantity greater than 2

### JOIN

Used to combine related tables and create business-friendly reports.

Examples:
- orders with customer names
- orders with product details
- complete order reports using all three tables

---

## Important Business Insight

Completed revenue should only include orders with completed status.

Pending and cancelled orders represent potential or lost sales and should not be counted as actual revenue.

The analysis shows which products, categories, cities, and customers generate the highest value.

---

## Main Learning

This practice helped me understand how SQL is used not only to retrieve data, but also to create reports that support business decisions.
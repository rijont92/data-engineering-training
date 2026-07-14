# Day 7 - SQL Detective Day

## Goal

The goal of this practice was to debug broken SQL queries, validate business metrics, and create trusted business reports using SQL.

During this practice, I worked with the same business dataset from previous SQL sessions using three tables: orders, customers, and products. The main focus was understanding SQL errors, fixing incorrect queries, using JOIN correctly, and verifying that every business number is supported by a working SQL query.

## Files included

- setup.sql
- table_inspection.sql
- broken_queries.sql
- fixed_queries.sql
- validation_queries.sql
- verified_business_report.md
- query_explanations.md
- daily_report.txt
- screenshots/

## How to run the SQL files

Run the SQL files in this order:

1. setup.sql
2. table_inspection.sql
3. fixed_queries.sql
4. validation_queries.sql
5. Review verified_business_report.md

## What I learned about debugging SQL

I learned how to identify and fix common SQL problems such as missing JOIN conditions, incorrect table usage, missing filters, syntax mistakes, and incorrect query structure.

I also learned that a query running successfully does not always mean the result is correct. The business logic behind the query must also be checked.

## What I learned about verifying business reports

I learned that every reported business number should be backed by a validation query. Revenue calculations must use completed orders only, and additional information like customer names, cities, product names, categories, and prices must come from the correct tables using JOINs.

## Main SQL concepts practiced

- SELECT and filtering data
- COUNT and SUM calculations
- GROUP BY and HAVING
- JOIN between multiple tables
- Revenue calculations
- Business metric validation
- SQL debugging
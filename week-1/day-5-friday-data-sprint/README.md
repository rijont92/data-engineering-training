# Day 5 - Friday Data Sprint

## Business Scenario

In this project, we analyzed order data from a small electronics and office-supplies business.

The goal of this sprint was to use Python and SQL to analyze order data, calculate business metrics, and prepare useful insights for the business owner.

The same dataset was used in both Python and SQL to compare different approaches for analyzing data.

---

## Group Members

* Amar Fejzullahu
* Rijon Tahiri

---

## Project Structure

```
day-5-friday-data-sprint/

├── data/
│   └── orders.csv
│
├── python_analysis.py
├── setup.sql
├── sql_analysis.sql
├── business_insights.md
├── presentation_notes.md
├── README.md
│
├── screenshots/
│
└── individual_reflections/
    ├── student_1_name.txt
    └── student_2_name.txt
```

---

# Python Analysis

The Python script reads the order data from `orders.csv` and performs business analysis.

The script includes:

* Reading CSV data
* Counting total orders
* Displaying completed orders
* Displaying pending and cancelled orders
* Calculating `total_amount = quantity * price`
* Calculating completed revenue only
* Finding the most expensive single order
* Finding the highest total amount order
* Counting orders by status
* Counting orders by city
* Counting orders by category
* Printing a clean business report

## How to Run Python

Open the terminal inside the project folder and run:

```bash
python python_analysis.py
```

## Python Analysis Results

The analysis produced these results:

* Total Orders: 15
* Completed Orders: 9
* Pending Orders: 3
* Cancelled Orders: 3
* Completed Revenue: 3335.0

The highest total amount order was:

* Customer: Blerim Hoxha
* Product: Phone
* Total Amount: 1000.0

The most expensive single order by price was:

* Customer: Jonida Rama
* Product: Camera
* Price: 900.0

---

# SQL Analysis

SQL was used to analyze the same order dataset inside a database table.

The SQL analysis contains two files:

## setup.sql

This file:

* Removes the existing table if it exists
* Creates the `orders` table
* Inserts the same data from `orders.csv`
* Verifies the inserted data

## sql_analysis.sql

This file contains queries for:

* Showing all orders
* Showing completed orders
* Showing pending and cancelled orders
* Calculating `total_amount`
* Calculating completed revenue
* Counting orders by status
* Counting orders by city
* Counting orders by category
* Finding top valuable orders

SQL queries were tested using SQLiteOnline.com.

---

# Main Business Insight

The analysis showed that:

* The business has 15 total orders.
* Only completed orders generate revenue.
* Completed revenue is 3335.0.
* Prishtina has the highest number of orders with 3 orders.
* Electronics and Accessories are the strongest categories with 6 orders each.
* Some orders are pending or cancelled and do not contribute to revenue.

The business should focus on converting pending orders into completed sales and investigate the reasons behind cancelled orders.

---

# Tools Used

* Python
* SQL
* SQLiteOnline.com
* CSV data processing

---

# Team Contribution

## Rijon Tahiri

Responsibilities:

* Created Python analysis
* Loaded and processed CSV data
* Implemented calculations and filtering logic
* Generated terminal business report

## Amar Fejzullahu

Responsibilities:

* Created SQL database setup
* Prepared SQL analysis queries
* Worked on business insights and documentation

---

# Screenshots Included

The `screenshots/` folder contains:

* SQLiteOnline table creation and inserted data
* Completed orders query result
* Total amount calculation query
* Completed revenue query
* GROUP BY status or city query
* Python terminal business report

---

# Running Order

To reproduce the project:

1. Open the project folder.
2. Run `python_analysis.py` to see the Python business report.
3. Open SQLiteOnline.com.
4. Run `setup.sql` first to create and populate the database.
5. Run `sql_analysis.sql` to execute business analysis queries.
6. Review `business_insights.md` for the final conclusions.

---

# Conclusion

This project helped us practice how data engineers work with real business data.

We used Python for data processing and SQL for database analysis. By comparing both approaches, we learned how to transform raw order data into useful business insights.

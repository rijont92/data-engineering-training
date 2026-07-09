# Python vs SQL Comparison - Day 4

## Introduction

In this practice, I used the same orders dataset in two different ways:

* Python: using a list of dictionaries.
* SQL: using an orders table.

The goal was to understand that Python and SQL can solve the same data problems using different syntax.

Both approaches can:

* Filter records
* Calculate new values
* Sort data
* Limit results
* Create business summaries

---

# Task 1: Show completed orders

## Python approach:

In Python, I created a function called `filter_by_status()`.

Steps:

* Loop through the orders list.
* Check every order status.
* Compare `order["status"]` with `"completed"`.
* Add matching orders to a result list.
* Return and print the completed orders.

Example:

```python
def filter_by_status(orders, status):
    result = []

    for order in orders:
        if order["status"] == status:
            result.append(order)

    return result
```

Usage:

```python
filter_by_status(orders, "completed")
```

## SQL approach:

In SQL, the orders are stored in a table.

Steps:

* Select data from the orders table.
* Use WHERE to filter rows.
* Return only completed orders.

Example:

```sql
SELECT *
FROM orders
WHERE status = 'completed';
```

## What I understood:

Both Python and SQL filter data.

Python uses a loop and if condition to check every dictionary.

SQL uses the WHERE condition to filter rows directly from the table.

---

# Task 2: Show orders with price greater than 100

## Python approach:

In Python, I created a function called `filter_by_price()`.

Steps:

* Loop through every order.
* Check if the price is greater than the given value.
* Add matching orders to a new list.

Example:

```python
def filter_by_price(orders, price):

    result = []

    for order in orders:
        if order["price"] > price:
            result.append(order)

    return result
```

Usage:

```python
filter_by_price(orders, 100)
```

## SQL approach:

In SQL, I use WHERE with a price condition.

Example:

```sql
SELECT *
FROM orders
WHERE price > 100;
```

## What I understood:

Both approaches find orders that match a condition.

Python checks each dictionary one by one.

SQL filters records directly using the database query.

---

# Task 3: Calculate total_amount

## Python approach:

In Python, I created a function called `calculate_totals()`.

Steps:

* Loop through all orders.
* Multiply quantity by price.
* Create a new dictionary containing the calculated value.

Formula:

```
total_amount = quantity * price
```

Example:

```python
total_amount = order["quantity"] * order["price"]
```

The function returns:

* customer_name
* product
* quantity
* price
* total_amount

## SQL approach:

In SQL, I create a calculated column inside SELECT.

Example:

```sql
SELECT 
customer_name,
product,
quantity,
price,
quantity * price AS total_amount
FROM orders;
```

## What I understood:

Python calculates values while looping through data.

SQL creates a calculated column in the query result.

The calculation logic is the same:

quantity × price

---

# Task 4: Sort orders by price descending

## Python approach:

In Python, I used the `sorted()` function.

Steps:

* Use the orders list.
* Choose price as the sorting key.
* Use `reverse=True` to sort from highest to lowest.

Example:

```python
sorted_by_price = sorted(
    orders,
    key=lambda x: x["price"],
    reverse=True
)
```

## SQL approach:

In SQL, I use ORDER BY.

Example:

```sql
SELECT *
FROM orders
ORDER BY price DESC;
```

## What I understood:

Both methods organize data.

Python sorts a list in memory.

SQL sorts rows returned from the database.

---

# Task 5: Show top 3 orders by total_amount

## Python approach:

In Python, I first calculated totals using `calculate_totals()`.

Steps:

* Calculate total_amount for every order.
* Sort orders by total_amount.
* Use list slicing `[:3]` to return only three records.

Example:

```python
sorted_by_total = sorted(
    totals,
    key=lambda x: x["total_amount"],
    reverse=True
)

top_orders = sorted_by_total[:3]
```

## SQL approach:

In SQL, I combine calculated columns with ORDER BY and LIMIT.

Example:

```sql
SELECT 
customer_name,
product,
quantity,
price,
quantity * price AS total_amount
FROM orders
ORDER BY total_amount DESC
LIMIT 3;
```

## What I understood:

Python uses sorting and slicing.

SQL uses ORDER BY and LIMIT.

Both return the highest three orders based on total value.

---

# Task 6: Count orders by status

## Python approach:

In Python, I created a function called `status_summary()`.

Steps:

* Create an empty dictionary.
* Loop through orders.
* Check each status.
* Increase the counter.

Example:

```python
counts[status] += 1
```

Output example:

```
completed: 8
pending: 2
cancelled: 2
```

## SQL approach:

In SQL, I can use COUNT with GROUP BY.

Example:

```sql
SELECT 
status,
COUNT(*) AS number_of_orders
FROM orders
GROUP BY status;
```

## What I understood:

Python uses a dictionary to count values.

SQL uses GROUP BY to group rows and COUNT to count them.

---

# Task 7: Calculate completed revenue

## Python approach:

In Python, I created a function called `completed_revenue()`.

Steps:

* Start total revenue at 0.
* Loop through orders.
* Check if status is completed.
* Add quantity × price.

Example:

```python
if order["status"] == "completed":
    total += order["quantity"] * order["price"]
```

## SQL approach:

In SQL, I use SUM() with a WHERE condition.

Example:

```sql
SELECT 
SUM(quantity * price) AS completed_revenue
FROM orders
WHERE status = 'completed';
```

## What I understood:

Only completed orders should count as real revenue.

Pending and cancelled orders should not be included because they are not finished sales.

---

# Final Comparison

Python and SQL use different syntax, but the business logic is similar.

| Business Task           | Python                   | SQL                              |
| ----------------------- | ------------------------ | -------------------------------- |
| Filter completed orders | Loop + if condition      | WHERE status                     |
| Filter price values     | if price > value         | WHERE price > value              |
| Calculate total amount  | quantity * price in loop | quantity * price AS total_amount |
| Sort data               | sorted()                 | ORDER BY                         |
| Get top records         | [:3]                     | LIMIT 3                          |
| Count values            | Dictionary counter       | COUNT + GROUP BY                 |
| Calculate revenue       | Loop + sum               | SUM()                            |

## Final Understanding

Python works with lists and dictionaries and processes data step by step.

SQL works with tables and uses queries to retrieve and transform data.

The main idea I learned is that the same business question can be solved in both Python and SQL. The difference is only the way we write the instructions.

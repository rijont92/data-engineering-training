# Verified Business Report - Day 7 SQL Detective Day

## 1. Total order activity

Insight:
The dataset contains the total number of orders created.

Verified result:
Total orders: 14

SQL query used:
V1 - Count all orders

Business meaning:
Shows the total transaction activity in the system and gives an overview of the business workload.


## 2. Completed revenue

Insight:
Only completed orders are counted as real revenue.

Verified result:
Completed revenue: 1639

SQL query used:
V7 - Calculate completed revenue only

Business meaning:
Shows the actual earned revenue by excluding pending and cancelled orders.


## 3. Revenue by product

Insight:
Some products generate more revenue than others.

Verified result:
Laptop: 700
Monitor: 540
Headphones: 150
Desk Chair: 120
Mouse: 105
USB Cable: 24

SQL query used:
V8 - Calculate completed revenue by product_name

Business meaning:
Helps identify which products contribute the most revenue.


## 4. Revenue by category

Insight:
Some categories perform better than others.

Verified result:
Electronics: 1240
Accessories:279
Office:120

SQL query used:
V9 - Calculate completed revenue by category

Business meaning:
Shows the strongest product categories and helps with business decisions.


## 5. Orders by city

Insight:
Order activity differs between cities.

Verified result:
Prishtina: 5 orders
Vushtrri: 4 orders
Mitrovica: 2 orders
Peja: 1 orders
Prizren:1
Ferizaj:1

SQL query used:
V10 - Count orders by city

Business meaning:
Shows where customers are most active geographically.


## 6. Customers with more than one order

Insight:
Some customers are repeat buyers.

Verified result:
Arta: 2 orders
Blend: 2 orders
Dren: 2 orders
Elira: 2 orders

SQL query used:
V11 - Find customers with more than one order

Business meaning:
Helps identify loyal customers who may be valuable for retention strategies.


## 7. Orders not counted as revenue

Insight:
Pending and cancelled orders should not affect revenue calculations.

Verified result:
Order 1 - cancelled
Order 6 - pending
Order 11 - cancelled
Order 12 - pending

SQL query used:
V13 - Find orders that should not count as real revenue

Business meaning:
Prevents incorrect revenue reporting by excluding unfinished transactions.


## 8. Final recommendation

Based on the verified data, my recommendation is:
Focus on the highest-performing products and categories, while improving conversion of pending orders and reducing cancelled orders.
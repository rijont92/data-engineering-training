# Data Pipeline Thinking - Day 3

## Chosen business:
Restaurant

## Source Data:
The source data comes from customer orders, menu items, quantities, prices, and order statuses.
Customers create orders and the restaurant collects this information from the ordering system.

## Ingestion:
The order data is collected and entered into the database.
New customer orders are transferred from the restaurant system into SQL tables.

## Storage:
The data is stored in database tables.
For this project, the restaurant data is stored in the food_orders table.

## Cleaning:
Cleaning means improving the quality of the data.
Examples:
- Removing duplicate orders.
- Fixing incorrect prices.
- Checking missing customer names.
- Making sure order statuses are correct.

## Transformation:
The raw data is transformed into useful information.
Examples:
- Calculate total order value using quantity * price.
- Find the most popular food items.
- Calculate completed sales revenue.

## Business Output:
The final output can be used for business decisions.
Examples:
- Daily sales reports.
- Revenue dashboards.
- Popular food item reports.
- Completed and cancelled order analysis.

## Business questions we can answer:

1. Which food item generates the most revenue?
2. How many orders are completed or cancelled?
3. How much money did the restaurant earn from completed orders?

## Possible data problems:

1. Duplicate customer orders.
2. Incorrect prices or quantities.
3. Missing customer information.
-- Query 1: Show all orders
SELECT * FROM orders;

-- Query 2: Show only completed orders
SELECT * FROM orders WHERE status = 'completed';

-- Query 3: Show pending or cancelled orders.
SELECT * FROM orders WHERE status = 'pending' OR status = 'cancelled';

-- Query 4: Show total_amount as quantity * price.
SELECT , (quantity price) AS total_amount FROM orders;

-- Query 5: Show completed orders with total_amount.
SELECT , (quantity price) AS total_amount FROM orders WHERE status = 'completed';

-- Query 6: Calculate completed revenue using SUM(quantity * price)
SELECT SUM(quantity * price) AS completed_revenue FROM orders WHERE status = 'completed';

-- Query 7: Count orders by status using COUNT() and GROUP BY status.
SELECT status, COUNT() AS orders_count FROM orders GROUP BY status;

-- Query 8: Count orders by city using COUNT() and GROUP BY city.
SELECT city, COUNT() AS city_count FROM orders GROUP BY city;

-- Query 9: Count orders by category using COUNT() and GROUP BY category.
SELECT category, COUNT() AS category_count FROM orders GROUP BY category;

-- Query 10: Show top 3 orders by total_amount.
SELECT , (quantity price) AS total_amount FROM orders ORDER BY (quantity * price) DESC LIMIT 3;

-- Query 11: Find most valuable order.
SELECT , (quantity price) AS total_amount FROM orders ORDER BY (quantity * price) DESC LIMIT 1;
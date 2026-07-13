-- Join orders with customers
SELECT order_id, customer_name, city, order_date, status 
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;


-- Join orders with products
SELECT order_id, product_name, category, quantity, price,
quantity * price AS total_amount, status 
FROM orders
JOIN products ON orders.product_id = products.product_id;


-- Complete order report using all three tables
SELECT customer_name, city, product_name, category,
quantity, price, quantity * price AS total_amount, status, order_date 
FROM orders
JOIN products ON orders.product_id = products.product_id
JOIN customers ON orders.customer_id = customers.customer_id;


-- Revenue reports by product and category
SELECT product_name, SUM(quantity * price) AS completed_revenue 
FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY product_name
ORDER BY completed_revenue DESC;


SELECT category, SUM(quantity * price) AS completed_revenue 
FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY category
ORDER BY completed_revenue DESC;


-- Order and revenue reports by city
SELECT city, COUNT(*) AS order_count 
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY city
ORDER BY order_count DESC;


SELECT city, SUM(quantity * price) AS completed_revenue 
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY city
ORDER BY completed_revenue DESC;


-- Revenue report by customer
SELECT customer_name, SUM(quantity * price) AS completed_revenue 
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY customer_name
ORDER BY completed_revenue DESC;


-- Customers with multiple orders
SELECT customer_name, COUNT(*) AS order_count 
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customer_name
HAVING COUNT(*) > 1
ORDER BY order_count DESC;


-- Top 3 customers by completed revenue
SELECT customer_name, SUM(quantity * price) AS completed_revenue 
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY customer_name
ORDER BY completed_revenue DESC
LIMIT 3;


-- Top 3 products by completed revenue
SELECT product_name, SUM(quantity * price) AS completed_revenue 
FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY product_name
ORDER BY completed_revenue DESC
LIMIT 3;


-- Pending and cancelled orders potential value
SELECT customer_name, city, product_name,
quantity * price AS potential_amount 
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE status != 'completed';
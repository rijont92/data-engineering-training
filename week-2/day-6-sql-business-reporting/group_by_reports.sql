-- Count orders by status
SELECT status, COUNT(*) AS order_count 
FROM orders
GROUP BY status
ORDER BY order_count DESC;


-- Count orders by date
SELECT order_date, COUNT(*) AS order_count 
FROM orders
GROUP BY order_date
ORDER BY order_date ASC;


-- Count orders by customer
SELECT customer_id, COUNT(*) AS order_count 
FROM orders
GROUP BY customer_id
ORDER BY order_count DESC;


-- Count orders by product
SELECT product_id, COUNT(*) AS order_count 
FROM orders
GROUP BY product_id
ORDER BY order_count DESC;


-- Completed quantity by product
SELECT product_id, SUM(quantity) AS completed_quantity 
FROM orders
WHERE status = 'completed'
GROUP BY product_id
ORDER BY completed_quantity DESC;


-- Completed revenue by product
SELECT orders.product_id, SUM(quantity * price) AS completed_revenue 
FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY orders.product_id
ORDER BY completed_revenue DESC;


-- Value by order status
SELECT status, SUM(quantity * price) AS status_value 
FROM orders
JOIN products ON orders.product_id = products.product_id
GROUP BY status
ORDER BY status_value DESC;


-- Customers with more than one order
SELECT customer_id, COUNT(*) AS order_count 
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1
ORDER BY order_count DESC;


-- Products with completed quantity greater than 2
SELECT product_id, SUM(quantity) AS completed_quantity 
FROM orders
WHERE status = 'completed'
GROUP BY product_id
HAVING SUM(quantity) > 2
ORDER BY completed_quantity DESC;
-- Check how many order records exist in the orders table. 
SELECT COUNT(*) as total_orders FROM orders;

-- Count all completed orders in orders table
SELECT status,COUNT(*) as total_completed_orders FROM orders
WHERE status = 'completed';

-- Count all pending orders in orders table
SELECT status,COUNT(*) as total_pending_orders FROM orders
WHERE status = 'pending';

-- Count all cancelled orders in orders table
SELECT status,COUNT(*) as total_cancelled_orders FROM orders
WHERE status = 'cancelled';

-- Check how many customer records exist in the customers table. 
SELECT COUNT(*) as total_customers FROM customers;

-- Check how many product records exist in the products table. 
SELECT COUNT(*) as total_products FROM products;

-- Calculate completed revenue 
SELECT SUM(quantity * price) AS completed_revenue FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed';

-- Calculate completed revenue by product_name
SELECT product_name, SUM(quantity * price) AS revenue FROM orders 
JOIN products ON orders.product_id = products.product_id 
WHERE status = 'completed' 
GROUP BY product_name; 
-- Calculate completed revenue by category
SELECT category, SUM(quantity * price) AS revenue FROM orders 
JOIN products ON orders.product_id = products.product_id 
WHERE status = 'completed' 
GROUP BY category; 

-- Count orders by city
SELECT city, COUNT(*) AS order_count FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY city
ORDER BY order_count DESC;

-- Customers with more than 1 order
SELECT customer_name, COUNT(*) AS order_count 
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customer_name
HAVING COUNT(*) > 1
ORDER BY order_count DESC;


-- Find top 3 completed orders by total amount
SELECT orders.order_id,customers.customer_name,(orders.quantity * products.price) AS total_amount FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
ORDER BY total_amount DESC
LIMIT 3;

-- Find orders that should not count as real revenue
SELECT order_id,status,quantity,product_id FROM orders
WHERE status != 'completed';


-- Find category with the highest completed revenue
SELECT products.category,SUM(orders.quantity * products.price) AS completed_revenue FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.category
ORDER BY completed_revenue DESC
LIMIT 1;

-- Find city with the highest order activity
SELECT customers.city,COUNT(orders.order_id) AS order_count FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customers.city
ORDER BY order_count DESC
LIMIT 1;



-- BONUS

-- Show completed revenue by city
SELECT customers.city,SUM(orders.quantity * products.price) AS completed_revenue FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY customers.city
ORDER BY completed_revenue DESC;


-- Show average completed order value by category
SELECT products.category,AVG(orders.quantity * products.price) AS average_order_value FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.category;

-- Find products with completed revenue greater than 100
SELECT products.product_name,SUM(orders.quantity * products.price) AS completed_revenue FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY products.product_name
HAVING SUM(orders.quantity * products.price) > 100;


-- Compare completed, pending, and cancelled orders by city
SELECT customers.city,orders.status,COUNT(orders.order_id) AS order_count FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customers.city, orders.status
ORDER BY customers.city, order_count DESC;

-- Broken query:
SELECT city COUNT(*) AS order_count
FROM customers
GROUP BY city;

-- Fixed query:
SELECT city,COUNT(*) AS order_count
FROM customers
GROUP BY city;

--Explanation:The original query had a syntax error because SQL requires commas between selected columns.
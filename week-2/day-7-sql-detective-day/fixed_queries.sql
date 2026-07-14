-- Need to make join table customers to access column city
SELECT city, COUNT(*) AS order_count FROM orders 
JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY city; 

-- Fixed syntax error missing "," after product_name
SELECT product_name, SUM(quantity * price) AS revenue 
FROM orders 
JOIN products ON orders.product_id = products.product_id 
WHERE status = 'completed' 
GROUP BY product_name; 

-- Fixed syntax error removed ";" from "GROUP BY status;" and let it only at end of the query
SELECT status, COUNT(*) AS order_count 
FROM orders 
GROUP BY status
ORDER BY order_count DESC;

-- Need to make join table products to access column price
SELECT order_id, quantity, price, quantity * price AS total_amount FROM orders
JOIN products ON orders.product_id = products.product_id;


-- Need to make join table products to access column category
SELECT category, SUM(quantity) AS total_quantity FROM orders 
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed' 
GROUP BY category; 

-- Added WHERE status = 'completed' to calculate only completed revenue
SELECT SUM(quantity * price) AS total_revenue FROM orders 
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed'; 

-- Moved HAVING COUNT(*) > 1 after GROUP BY customer_id to fix syntax error
SELECT customer_id, COUNT(*) AS order_count 
FROM orders 
GROUP BY customer_id
HAVING COUNT(*) > 1; 


-- Added ON orders.customer_id = customers.customer_id to correctly match orders with customers.
SELECT orders.order_id, customers.customer_name 
FROM orders 
JOIN customers ON orders.customer_id = customers.customer_id;


-- Added the correct JOIN condition using product_id to connect orders with products.
SELECT orders.customer_id, orders.product_id, products.price FROM orders 
JOIN products ON orders.product_id = products.product_id;


-- Added ! before = to show only orders that are not completed
SELECT * FROM orders 
WHERE status != 'completed'; 

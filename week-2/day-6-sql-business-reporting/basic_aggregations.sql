-- Basic order counts
SELECT COUNT(*) AS order_count 
FROM orders;


SELECT COUNT(*) AS completed_orders 
FROM orders 
WHERE status = 'completed';

SELECT COUNT(*) AS pending_orders 
FROM orders 
WHERE status = 'pending';

SELECT COUNT(*) AS cancelled_orders 
FROM orders 
WHERE status = 'cancelled';


-- Quantity metrics
SELECT SUM(quantity) AS total_quantity 
FROM orders;

SELECT SUM(quantity) AS completed_quantity 
FROM orders 
WHERE status = 'completed';


-- Product price metrics
SELECT AVG(price) AS average_product_price 
FROM products;

SELECT MIN(price) AS cheapest_product_price 
FROM products;

SELECT MAX(price) AS most_expensive_product_price 
FROM products;


-- Revenue calculations
SELECT SUM(quantity * price) AS completed_revenue 
FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE status = 'completed';


-- Potential value from non-completed orders
SELECT SUM(quantity * price) AS potential_value 
FROM orders
JOIN products ON orders.product_id = products.product_id
WHERE status != 'completed';
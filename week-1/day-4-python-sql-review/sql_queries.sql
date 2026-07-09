-- Show all orders
SELECT * FROM orders;

-- Show customer name and product
SELECT customer_name, product FROM orders;

-- Show order details with customer, city, and status
SELECT order_id, customer_name, city, status FROM orders;

-- Show product details and pricing information
SELECT product, category, quantity, price FROM orders;


------------------------


-- Show completed orders
SELECT * FROM orders WHERE status = 'completed';

-- Show pending orders
SELECT * FROM orders WHERE status = 'pending';

-- Show cancelled orders
SELECT * FROM orders WHERE status = 'cancelled';

-- Show orders with price higher than 100
SELECT * FROM orders WHERE price > 100;

-- Show orders from Vushtrri
SELECT * FROM orders WHERE city = 'Vushtrri';

-- Show orders from Accessories category
SELECT * FROM orders WHERE category = 'Accessories';


------------------------


-- Show completed orders with price above 100
SELECT * FROM orders WHERE status = 'completed' AND price > 100;

-- Show completed orders from Prishtina
SELECT * FROM orders WHERE status = 'completed' AND city = 'Prishtina';

-- Show pending or cancelled orders
SELECT * FROM orders WHERE status = 'pending' OR status = 'cancelled';

-- Show cheap Accessories products
SELECT * FROM orders WHERE category = 'Accessories' AND price < 50;


------------------------


-- Sort orders by lowest price
SELECT * FROM orders ORDER BY price ASC;

-- Sort orders by highest price
SELECT * FROM orders ORDER BY price DESC;

-- Show top 3 most expensive orders
SELECT * FROM orders ORDER BY price DESC LIMIT 3;

-- Calculate and show top 3 orders by total amount
SELECT customer_name, product, quantity, price, quantity * price AS total_amount 
FROM orders 
ORDER BY total_amount DESC 
LIMIT 3;


------------------------


-- Calculate total amount for each order
SELECT customer_name, product, quantity, price, quantity * price AS total_amount 
FROM orders;

-- Calculate total amount only for completed orders
SELECT customer_name, product, status, quantity, price, quantity * price AS total_amount 
FROM orders 
WHERE status = 'completed';

-- Show completed orders sorted by total amount
SELECT customer_name, product, status, quantity, price, quantity * price AS total_amount 
FROM orders 
WHERE status = 'completed' 
ORDER BY total_amount DESC;


------------------------


-- Mini Business Challenge

-- Find the highest total amount order
SELECT customer_name, product, quantity, price, quantity * price AS total_amount 
FROM orders 
ORDER BY total_amount DESC 
LIMIT 1;

-- Find orders that are not real revenue
SELECT * FROM orders 
WHERE status IN ('cancelled','pending');

-- Calculate completed revenue only
SELECT SUM(quantity * price) AS completed_revenue 
FROM orders 
WHERE status = 'completed';


-- Add new orders
INSERT INTO orders VALUES
(13,'Blerina','Prishtina','Phone','Electronics',1,900,'completed','2026-07-07'),
(14,'Valon','Peja','Notebook','Office',5,10,'completed','2026-07-08');


-- Show all orders after inserting new data
SELECT * FROM orders;

-- Count total number of orders
SELECT COUNT(*) AS total_orders FROM orders;

-- Count orders by status
SELECT status, COUNT(*) AS number_of_orders 
FROM orders 
GROUP BY status;

-- Count orders by city
SELECT city, COUNT(*) AS number_of_orders 
FROM orders 
GROUP BY city;

-- Count orders by category
SELECT category, COUNT(*) AS number_of_orders 
FROM orders 
GROUP BY category;

-- Show completed orders sorted by total amount
SELECT customer_name, product, quantity, price, quantity * price AS total_amount 
FROM orders 
WHERE status = 'completed' 
ORDER BY total_amount DESC;
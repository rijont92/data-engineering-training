-- Level 1 - Basic SELECT and Relationship Checks

-- Show all customers. 
SELECT * FROM customers;

-- Show all products. 
SELECT * FROM products;

-- Show all orders.
SELECT * FROM orders;

-- Show all order_items
SELECT * FROM order_items;

-- Show only completed orders
SELECT * FROM orders WHERE status = "completed";

-- Show only pending or cancelled orders
SELECT * FROM orders WHERE status in ("cancelled","pending");


-- Level 2 - First INNER JOINS

-- Show each order with customer details
SELECT customer_name,city,order_date,status,channel FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;

-- Show each order_item with product details
SELECT
 order_items.order_item_id,
 products.product_name,
 products.category,
 products.price,
 order_items.quantity 
FROM order_items
INNER JOIN products ON order_items.product_id = products.product_id;

-- Show order_id, customer_name, product_name, quantity, price, and total_amount.
SELECT
    orders.order_id,
    customers.customer_name,
    products.product_name,
    order_items.quantity,
    products.price,
    (products.price * order_items.quantity) AS total_amount
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id
INNER JOIN order_items ON orders.order_id = order_items.order_id
INNER JOIN products ON order_items.product_id = products.product_id;

-- Show only completed orders with their customer and product details.
SELECT 
	orders.order_id,
    customers.customer_name,
    products.product_name,
    order_items.quantity,
    products.price,
    (products.price * order_items.quantity) AS total_amount,
    orders.order_date,
    orders.channel
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id
INNER JOIN order_items ON orders.order_id = order_items.order_id
INNER JOIN products ON order_items.product_id = products.product_id
WHERE status = "completed";



-- Join customers + orders + order_items + products in one query.
SELECT 
	customers.customer_name,
    customers.city,
    orders.order_id,
    orders.order_date,
    orders.status,
    orders.channel,
    products.product_name,
    products.category,
    products.price,
    order_items.quantity
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id
INNER JOIN order_items ON orders.order_id = order_items.order_id
INNER JOIN products ON order_items.product_id = products.product_id;


-- Show customer, order, product details with total amount
SELECT
    customers.customer_name,
    customers.city,
    orders.order_id,
    products.product_name,
    products.category,
    order_items.quantity,
    products.price,
    (order_items.quantity * products.price) AS total_amount
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
INNER JOIN order_items
    ON orders.order_id = order_items.order_id
INNER JOIN products
    ON order_items.product_id = products.product_id;


-- Sort result by order_id and product_name
SELECT
    customers.customer_name,
    customers.city,
    orders.order_id,
    products.product_name,
    products.category,
    order_items.quantity,
    products.price,
    (order_items.quantity * products.price) AS total_amount
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
INNER JOIN order_items
    ON orders.order_id = order_items.order_id
INNER JOIN products
    ON order_items.product_id = products.product_id
ORDER BY
    orders.order_id,
    products.product_name;


-- Show only completed orders from joined result
SELECT
    customers.customer_name,
    customers.city,
    orders.order_id,
    products.product_name,
    products.category,
    order_items.quantity,
    products.price,
    (order_items.quantity * products.price) AS total_amount
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
INNER JOIN order_items
    ON orders.order_id = order_items.order_id
INNER JOIN products
    ON order_items.product_id = products.product_id
WHERE orders.status = 'completed';


-- Level 4 - Business Reports with Relationships

-- Calculate completed revenue by city
SELECT
    customers.city,
    SUM(order_items.quantity * products.price) AS completed_revenue
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
INNER JOIN order_items
    ON orders.order_id = order_items.order_id
INNER JOIN products
    ON order_items.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY customers.city;


-- Calculate completed revenue by product category
SELECT
    products.category,
    SUM(order_items.quantity * products.price) AS completed_revenue
FROM products
INNER JOIN order_items
    ON products.product_id = order_items.product_id
INNER JOIN orders
    ON order_items.order_id = orders.order_id
WHERE orders.status = 'completed'
GROUP BY products.category;


-- Show top 5 customers by completed revenue
SELECT
    customers.customer_name,
    SUM(order_items.quantity * products.price) AS completed_revenue
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
INNER JOIN order_items
    ON orders.order_id = order_items.order_id
INNER JOIN products
    ON order_items.product_id = products.product_id
WHERE orders.status = 'completed'
GROUP BY customers.customer_name
ORDER BY completed_revenue DESC
LIMIT 5;


-- Show top 5 products by completed revenue
SELECT
    products.product_name,
    products.category,
    SUM(order_items.quantity * products.price) AS completed_revenue
FROM products
INNER JOIN order_items
    ON products.product_id = order_items.product_id
INNER JOIN orders
    ON order_items.order_id = orders.order_id
WHERE orders.status = 'completed'
GROUP BY products.product_name, products.category
ORDER BY completed_revenue DESC
LIMIT 5;


-- Count how many orders each customer has
SELECT
    customers.customer_name,
    COUNT(orders.order_id) AS total_orders
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_name;


-- Count how many items each order has

SELECT
    orders.order_id,
    COUNT(order_items.order_item_id) AS total_items
FROM orders
INNER JOIN order_items
    ON orders.order_id = order_items.order_id
GROUP BY orders.order_id;


-- Find customers who have more than one order
SELECT
    customers.customer_name,
    COUNT(orders.order_id) AS total_orders
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_name
HAVING COUNT(orders.order_id) > 1;


-- Find products that were sold more than once
SELECT
    products.product_name,
    COUNT(order_items.product_id) AS times_sold
FROM products
INNER JOIN order_items
    ON products.product_id = order_items.product_id
GROUP BY products.product_name
HAVING COUNT(order_items.product_id) > 1;

-- Level 5 - LEFT JOIN Thinking

-- Show all customers and their orders including customers without orders
SELECT
    customers.customer_name,
    customers.city,
    orders.order_id,
    orders.order_date,
    orders.status,
    orders.channel
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id;
    
    
-- Show all products and how many times they appear in order_items
SELECT
    products.product_name,
    products.category,
    COUNT(order_items.order_item_id) AS times_sold
FROM products
LEFT JOIN order_items
    ON products.product_id = order_items.product_id
GROUP BY products.product_name, products.category;
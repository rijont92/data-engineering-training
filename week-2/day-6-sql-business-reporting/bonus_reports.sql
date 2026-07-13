-- Completed revenue by order date
SELECT order_date,SUM(quantity * price) AS completed_revenue
FROM orders
JOIN products 
ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY order_date
ORDER BY order_date;


-- Average completed order value by category
SELECT category,AVG(quantity * price) AS average_order_value
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY category
ORDER BY average_order_value DESC;


-- Product completed orders report
SELECT product_name,COUNT(*) AS completed_orders,SUM(quantity) AS completed_quantity,SUM(quantity * price) AS completed_revenue
FROM orders
JOIN products
ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY product_name
ORDER BY completed_revenue DESC;


-- City completed revenue report
SELECT city,COUNT(*) AS completed_orders,SUM(quantity * price) AS completed_revenue
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN products
ON orders.product_id = products.product_id
WHERE status = 'completed'
GROUP BY city
ORDER BY completed_revenue DESC;
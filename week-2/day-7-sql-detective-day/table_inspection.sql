-- Fetches all columns and rows from the customer table.
SELECT * FROM customers;

-- Fetches all columns and rows from the products table.
SELECT * FROM products;

-- Fetches all columns and rows from the orders table.
SELECT * FROM orders;

-- Check how many order records exist in the customers table. 
SELECT COUNT(*) as total_customers FROM customers;

-- Check how many order records exist in the products table. 
SELECT COUNT(*) as total_products FROM products;

-- Check how many order records exist in the orders table. 
SELECT COUNT(*) as total_orders FROM orders;
-- Business: Restaurant

DROP TABLE IF EXISTS food_orders;

CREATE TABLE food_orders (
    order_id INTEGER,
    customer_name TEXT,
    item TEXT,
    quantity INTEGER,
    price INTEGER,
    status TEXT
);


INSERT INTO food_orders (order_id, customer_name, item, quantity, price, status)
VALUES
(1, 'Arta', 'Pizza', 2, 8, 'completed'),
(2, 'Dren', 'Burger', 1, 6, 'completed'),
(3, 'Elira', 'Pasta', 3, 7, 'pending'),
(4, 'Blend', 'Salad', 1, 4, 'completed'),
(5, 'Lira', 'Pizza', 1, 8, 'cancelled'),
(6, 'Arben', 'Burger', 2, 6, 'completed'),
(7, 'Sara', 'Pasta', 2, 7, 'pending'),
(8, 'Dion', 'Pizza', 3, 8, 'completed');


-- Show all rows from custom table
SELECT * FROM food_orders;

-- Show selected columns
SELECT customer_name, item, status FROM food_orders;

-- Filter rows by status
SELECT * FROM food_orders WHERE status = 'completed';

-- Filter rows by numeric value
SELECT * FROM food_orders WHERE quantity > 1;

-- Combine two conditions using AND
SELECT * FROM food_orders WHERE status = 'completed' AND item = 'Pizza';

-- Combine two conditions using OR
SELECT * FROM food_orders WHERE status = 'pending' OR status = 'cancelled';

-- Sort rows from highest to lowest price
SELECT * FROM food_orders ORDER BY price DESC;

-- Show top 3 rows
SELECT * FROM food_orders ORDER BY price DESC LIMIT 3;

-- Create calculated column
SELECT customer_name,item,quantity,price,quantity * price AS total_amount FROM food_orders;

-- Business-ready query
SELECT customer_name,item,quantity * price AS total_amount,status FROM food_orders WHERE status = 'completed' ORDER BY total_amount DESC;
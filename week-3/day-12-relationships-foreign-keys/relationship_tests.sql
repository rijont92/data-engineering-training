-- Trying to insert a product with negative price

INSERT INTO products
(product_name, category, price)
VALUES
('Charger', 'Accessories', -2);


-- Trying to insert a product with price 0

INSERT INTO products
(product_name, category, price)
VALUES
('Printer', 'Electronics', 0);



-- Trying to insert an order with customer_id that does not exist

INSERT INTO orders
(customer_id, order_date, status, channel)
VALUES
(99, '2026-07-10', 'completed', 'Online');



-- Trying to insert an order_item with order_id that does not exist

INSERT INTO order_items
(order_id, product_id, quantity)
VALUES
(99,1,1);



-- Trying to insert an order_item with product_id that does not exist

INSERT INTO order_items
(order_id, product_id, quantity)
VALUES
(1,99,1);



-- Trying to insert an order_item with quantity 0

INSERT INTO order_items
(order_id, product_id, quantity)
VALUES
(1,1,0);



-- Trying to insert an order with status done

INSERT INTO orders
(customer_id, order_date, status, channel)
VALUES
(2, '2026-07-08', 'done', 'Phone');
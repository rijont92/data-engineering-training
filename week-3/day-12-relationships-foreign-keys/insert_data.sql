-- Insert customers

INSERT INTO customers (customer_name, city, segment) VALUES
('Arta Krasniqi', 'Vushtrri', 'Business'),
('Blend Berisha', 'Prishtina', 'Individual'),
('Dren Gashi', 'Mitrovica', 'Business'),
('Elira Hoxha', 'Peja', 'Individual'),
('Leart Kelmendi', 'Ferizaj', 'Business'),
('Gresa Shala', 'Gjakova', 'Individual');


-- Insert products

INSERT INTO products (product_name, category, price) VALUES
('Laptop', 'Electronics', 950),
('Mouse', 'Electronics', 25),
('Monitor', 'Electronics', 220),
('Keyboard', 'Electronics', 45),
('Desk', 'Furniture', 180),
('Headphones', 'Accessories', 80);


-- Insert orders

INSERT INTO orders 
(customer_id, order_date, status, channel)
VALUES
(1, '2026-07-01', 'completed', 'Online'),
(2, '2026-07-02', 'completed', 'Store'),
(3, '2026-07-03', 'pending', 'Online'),
(4, '2026-07-04', 'completed', 'Phone'),
(5, '2026-07-05', 'cancelled', 'Store'),
(1, '2026-07-06', 'completed', 'Online'),
(6, '2026-07-07', 'completed', 'Store'),
(2, '2026-07-08', 'completed', 'Phone');


-- Insert order items

INSERT INTO order_items
(order_id, product_id, quantity)
VALUES

-- Order 1
(1,1,1),
(1,2,2),

-- Order 2
(2,3,1),

-- Order 3
(3,2,1),
(3,4,1),

-- Order 4
(4,5,1),
(4,6,2),

-- Order 5
(5,1,1),

-- Order 6
(6,3,2),
(6,4,1),

-- Order 7
(7,2,3),

-- Order 8
(8,1,1);
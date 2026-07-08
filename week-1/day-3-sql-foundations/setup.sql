DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
 order_id INTEGER,
 customer_name TEXT,
 product TEXT,
 quantity INTEGER,
 price INTEGER,
 status TEXT
);


INSERT INTO orders (order_id, customer_name, product, quantity, price, status) VALUES
(1,'Arta','Laptop',1,700,'completed'),
(2,'Blend','Mouse',2,15,'completed'),
(3,'Arta','Keyboard',1,40,'cancelled'),
(4,'Dren','Monitor',1,180,'completed'),
(5,'Elira','Mouse',1,15,'completed'),
(6,'Dren','Laptop',1,700,'pending');

SELECT * FROM orders;
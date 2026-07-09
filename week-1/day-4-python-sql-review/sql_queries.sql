SELECT * FROM orders;

SELECT customer_name,product FROM orders;

SELECT order_id,customer_name,city,status FROM orders;

SELECT product,category,quantity,price FROM orders;


------------------------



SELECT * FRom orders WHERE status = 'completed';
SELECT * FRom orders WHERE status = 'pending';
SELECT * FRom orders WHERE status = 'cancelled';
SELECT * FROM orders WHERE price > 100;
SELECT * FROM orders WHERE city = 'Vushtrri';
SELECT * FROM orders WHERE category = 'Accessories';


------------------------

SELECT * FROM orders WHERE status = 'completed' AND price > 100;
SELECT * FROM orders WHERE status = 'completed' AND city = 'Prishtina';
SELECT * FROM orders WHERE status = 'pending' OR status = 'cancelled';
SELECT * FROM orders WHERE category = 'Accessories' AND price < 50;

------------------------


SELECT * FROM orders ORDER BY price ASC;
SELECT * FROM orders ORDER BY price DESC;
SELECT * FROM orders ORDER BY price DESC LIMIT 3;
SELECT customer_name,product,quantity,price,quantity * price AS total_amount FROM orders ORDER BY total_amount DESC LIMIT 3;

------------------------


SELECT customer_name,product,quantity,price,quantity * price AS total_amount FROM orders;
SELECT customer_name,product,status,quantity,price,quantity * price AS total_amount FROM orders WHERE status = 'completed';
SELECT customer_name,product,status,quantity,price,quantity * price AS total_amount FROM orders WHERE status = 'completed' ORDER BY total_amount DESC;






------------------------



--Mini Business Challenge

SELECT customer_name,product,quantity,price,quantity * price AS total_amount FROM orders ORDER BY total_amount DESC LIMIT 1;

SELECT customer_name,product,quantity,price,quantity * price AS total_amount FROM orders ORDER BY total_amount DESC LIMIT 1;

SELECT * FROM orders WHERE status = 'pending' OR status = 'cancelled';

SELECT SUM(quantity * price) AS completed_revenue FROM orders WHERE status = 'completed';


INSERT INTO orders VALUES
(13,'Blerina','Prishtina','Phone','Electronics',1,900,'completed','2026-07-07'),
(14,'Valon','Peja','Notebook','Office',5,10,'completed','2026-07-08');



SELECT * FROM orders;

SELECT COUNT(*) AS total_orders FROM orders;

SELECT SUM(quantity * price) AS completed_revenue FROM orders WHERE status = 'completed';

SELECT status,COUNT(*) AS number_of_orders FROM orders GROUP BY status;


SELECT city,COUNT(*) AS number_of_orders FROM orders GROUP BY city;

SELECT category,COUNT(*) AS number_of_orders FROM orders GROUP BY category;

SELECT customer_name,product,quantity,price,quantity * price AS total_amount FROM orders ORDER BY total_amount DESC LIMIT 1;

SELECT customer_name,product,quantity,price,quantity * price AS total_amount FROM orders WHERE status = 'completed' ORDER BY total_amount DESC;

SELECT * FROM orders WHERE status IN ('cancelled','pending');


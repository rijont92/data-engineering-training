DROP TABLE IF EXISTS orders;
CREATE TABLE orders (order_id INT PRIMARY KEY, customer_name VARCHAR(100) NOT NULL, city VARCHAR(50) NOT NULL, product VARCHAR(100) NOT NULL, category VARCHAR(50) NOT NULL, quantity INT NOT NULL, price DECIMAL(10,2) NOT NULL, status VARCHAR(20) NOT NULL, order_date DATE NOT NULL);

INSERT INTO orders (order_id, customer_name, city, product, category, quantity, price, status, order_date) VALUES
(1, 'Arta Krasniqi', 'Prishtina', 'Laptop', 'Electronics', 1, 700.00, 'completed', '2026-07-01'),
(2, 'Blerim Hoxha', 'Vushtrri', 'Phone', 'Electronics', 2, 500.00, 'completed', '2026-07-02'),
(3, 'Era Berisha', 'Peja', 'Headphones', 'Accessories', 3, 80.00, 'pending', '2026-07-02'),
(4, 'Drilon Gashi', 'Prizren', 'Keyboard', 'Accessories', 1, 120.00, 'completed', '2026-07-03'),
(5, 'Learta Shala', 'Ferizaj', 'Monitor', 'Electronics', 2, 300.00, 'cancelled', '2026-07-03'),
(6, 'Arben Mustafa', 'Gjilan', 'Mouse', 'Accessories', 4, 40.00, 'completed', '2026-07-04'),
(7, 'Sara Aliu', 'Mitrovica', 'Tablet', 'Electronics', 1, 350.00, 'pending', '2026-07-04'),
(8, 'Endrit Rama', 'Prishtina', 'Printer', 'Office Equipment', 1, 250.00, 'completed', '2026-07-05'),
(9, 'Flora Kelmendi', 'Peja', 'Desk Chair', 'Furniture', 2, 180.00, 'completed', '2026-07-05'),
(10, 'Valon Krasniqi', 'Vushtrri', 'Webcam', 'Accessories', 2, 90.00, 'cancelled', '2026-07-06'),
(11, 'Rina Tahiri', 'Prizren', 'Smartwatch', 'Electronics', 1, 220.00, 'completed', '2026-07-06'),
(12, 'Luan Berisha', 'Ferizaj', 'USB Cable', 'Accessories', 5, 15.00, 'completed', '2026-07-07'),
(13, 'Melisa Gashi', 'Gjilan', 'Laptop Stand', 'Accessories', 2, 60.00, 'pending', '2026-07-08'),
(14, 'Ardit Hoxha', 'Mitrovica', 'Office Desk', 'Furniture', 1, 450.00, 'completed', '2026-07-08'),
(15, 'Jonida Rama', 'Prishtina', 'Camera', 'Electronics', 1, 900.00, 'cancelled', '2026-07-09');

SELECT * FROM orders;
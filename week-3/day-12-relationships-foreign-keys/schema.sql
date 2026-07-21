SET FOREIGN_KEY_CHECKS = 1;

-- Drop tables in correct order (child tables first)
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;


-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_name TEXT NOT NULL,
    city TEXT NOT NULL,
    segment TEXT
);


-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL CHECK(price > 0)
);


-- Orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL CHECK(
        status IN ('completed', 'pending', 'cancelled')
    ),
    channel TEXT NOT NULL,

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);


-- Order items bridge table
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),

    FOREIGN KEY (order_id)
    REFERENCES orders(order_id),

    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
);
# ERD Explanation - Day 12 Relationships, Foreign Keys, and JOINs

## Part 1 - Relationship Thinking Before Coding

### 1. What are the main entities in this project?

The main entities in this project are:

- Customers
- Products
- Orders
- Order Items

Each entity represents a different part of the business.

Customers store information about people or companies buying products.

Products store information about items that the company sells.

Orders store customer purchases and transaction information.

Order Items store the products included inside each order.


---

### 2. Which table should store customers?

The `customers` table should store customer information.

It contains:

- customer_id
- customer_name
- city
- segment

The customer_id is the primary key and uniquely identifies every customer.


---

### 3. Which table should store products?

The `products` table should store product information.

It contains:

- product_id
- product_name
- category
- price

The product_id is the primary key and uniquely identifies every product.


---

### 4. Which table should store orders?

The `orders` table should store customer order information.

It contains:

- order_id
- customer_id
- order_date
- status
- channel

The order_id is the primary key.

The customer_id is a foreign key that connects each order to a customer.


---

### 5. Why should orders not repeat all customer and product details directly?

Orders should not store repeated customer and product information because it creates duplicate data and makes the database harder to maintain.

For example, storing customer_name, city, and product_name inside every order would create:

- Duplicate information
- Larger tables
- Higher chance of inconsistent data

Instead, relationships are used with primary keys and foreign keys.


---

### 6. What is the relationship between customers and orders?

The relationship between customers and orders is:

**One-to-Many relationship**

One customer can create many orders.

Example:

A customer named Arta can have:

- Order 1
- Order 2
- Order 3

But each order belongs to only one customer.

Relationship:
customers
|
|
orders


---

### 7. What is the relationship between orders and products?

The relationship between orders and products is:

**Many-to-Many relationship**

One order can contain multiple products.

Example:

Order 1:

- Laptop
- Mouse
- Keyboard

Also, one product can appear in many different orders.

Example:

A Laptop can be included in:

- Order 1
- Order 5
- Order 8


---

### 8. Why do we need an order_items table?

The `order_items` table is needed because orders and products have a many-to-many relationship.

A normal table cannot directly store this relationship.

The `order_items` table works as a bridge table between orders and products.

It stores:

- order_item_id
- order_id
- product_id
- quantity

Example:
orders
|
order_items
|
products


This allows the database to know:

- Which products belong to each order
- How many products were purchased
- Which orders contain a specific product


---

# Database Model

## customers

Primary Key:

- customer_id (AUTOINCREMENT)

Columns:

- customer_name
- city
- segment


---

## products

Primary Key:

- product_id (AUTOINCREMENT)

Columns:

- product_name
- category
- price


---

## orders

Primary Key:

- order_id (AUTOINCREMENT)

Foreign Key:

- customer_id references customers.customer_id

Columns:

- order_date
- status
- channel


---

## order_items

Primary Key:

- order_item_id (AUTOINCREMENT)

Foreign Keys:

- order_id references orders.order_id
- product_id references products.product_id

Columns:

- quantity


---

# Relationship Summary

- One customer can have many orders.
- One order can contain many products.
- One product can appear in many different orders.
- The order_items table connects orders and products as a bridge table.

Using relationships makes the database cleaner, avoids duplicate data, and improves data quality.
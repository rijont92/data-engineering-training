# Mistakes and Fixes - Day 12: Relationships, Foreign Keys, and JOINs

## Mistake 1 - Using PRAGMA in MySQL instead of SQLite

**Problem:**

I tried to run:

```sql
PRAGMA foreign_keys = ON;
```

The database returned a syntax error:

```text
Error Code: 1064. You have an error in your SQL syntax
```

**Why it happened:**

`PRAGMA` is a SQLite command. I was running the query in MySQL, where this command does not exist.

**Fix:**

I used SQLiteOnline for this project because the task requires SQLite.

Correct command (run in SQLite):

```sql
PRAGMA foreign_keys = ON;
```

---

## Mistake 2 - Inserting an order with a customer_id that does not exist

**Problem:**

I tried to insert:

```sql
INSERT INTO orders
(customer_id, order_date, status, channel)
VALUES
(99, '2026-07-10', 'completed', 'Online');
```

**Error:**

```text
Cannot add or update a child row:
a foreign key constraint fails
```

**Why it happened:**

The `customer_id` column is a foreign key referencing `customers.customer_id`. Customer with ID 99 does not exist, so the database rejected the insert.

**Fix:**

Insert an existing `customer_id`:

```sql
INSERT INTO orders
(customer_id, order_date, status, channel)
VALUES
(1, '2026-07-10', 'completed', 'Online');
```

---

## Mistake 3 - Inserting order_items before creating valid orders

**Problem:**

I tried to insert `order_items`:

```sql
INSERT INTO order_items
(order_id, product_id, quantity)
VALUES
(1, 1, 1);
```

**Error:**

```text
Cannot add or update a child row:
a foreign key constraint fails
```

**Why it happened:**

`order_items.order_id` references `orders.order_id`. The `order_id` must already exist in the `orders` table before inserting `order_items`.

**Fix:**

Inserted data in the correct order:

1. `customers`
2. `products`
3. `orders`
4. `order_items`

---

## Mistake 4 - Trying to insert a product with an invalid price

**Problem:**

I tested the `CHECK` constraint:

```sql
INSERT INTO products
(product_name, category, price)
VALUES
('Charger', 'Accessories', -2);
```

**Result:**

Database rejected the insert.

**Why it happened:**

The `products` table has a CHECK constraint:

```sql
CHECK(price > 0)
```

Negative prices are not allowed.

**Correct insert:**

```sql
INSERT INTO products
(product_name, category, price)
VALUES
('Charger', 'Accessories', 20);
```

---

## Mistake 5 - Trying to insert an invalid status

**Problem:**

I tried:

```sql
INSERT INTO orders
(customer_id, order_date, status, channel)
VALUES
(2, '2026-07-08', 'done', 'Phone');
```

**Result:**

Database rejected the insert.

**Why it happened:**

The `status` column only allows:

- `completed`
- `pending`
- `cancelled`

The value `'done'` is not valid.

**Correct insert:**

```sql
INSERT INTO orders
(customer_id, order_date, status, channel)
VALUES
(2, '2026-07-08', 'completed', 'Phone');
```

---

## Mistake 6 - Wrong JOIN condition

**Problem:**

I wrote:

```sql
JOIN customers
ON orders.customer_id = customers.city
```

**Why it was wrong:**

`customer_id` is a number and `city` is text. They cannot be meaningfully connected.

**Fix:**

The correct relationship is:

```sql
JOIN customers
ON orders.customer_id = customers.customer_id
```

---

## Lessons Learned

Through these mistakes I learned:

- Foreign keys protect data consistency.
- Tables must be inserted in the correct order.
- Primary keys and foreign keys must match correctly.
- CHECK constraints prevent invalid business data.
- JOIN conditions must use related keys, not random columns.
- A relational database prevents bad data instead of fixing it later.

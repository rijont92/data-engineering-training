# Day 13 - Answers and Explanation

## What problem does a primary key solve?

A primary key gives every row a unique identity. It prevents duplicate records and allows other tables to reference a specific row.

Example:
student_id identifies each student uniquely.


## What problem does AUTOINCREMENT solve?

AUTOINCREMENT allows the database to create unique IDs automatically when a new row is inserted. It prevents manual ID mistakes and duplicate IDs.


## What problem does a foreign key solve?

A foreign key connects tables and protects data relationships. It prevents inserting data that does not exist in the parent table.

Example:
A course cannot have an instructor_id that does not exist in the instructors table.


## Why is enrollments a bridge table?

Enrollments is a bridge table because students and courses have a many-to-many relationship.

One student can join many courses, and one course can have many students.

The enrollments table connects these two tables and stores extra information like enrollment date and status.


## Why is submissions also a relationship table?

Submissions connects students and assignments.

A student submits work for an assignment, so the table stores the relationship between a student and an assignment.

It also stores extra data like score, submission date, and status.


## What is one-to-many in your project? Give two examples.

One-to-many means one record in one table can have many related records in another table.

Examples:

1. One instructor can teach many courses.
2. One course can have many assignments.


## What is many-to-many in your project? Give one example.

Many-to-many means both sides can have multiple relationships.

Example:

Students and courses.

A student can enroll in many courses, and a course can contain many students.

The enrollments table solves this relationship.


## Why should we not store instructor_name directly inside every course report table?

Because it creates duplicated data.

If an instructor changes their name, we would need to update many rows. Storing instructor_id and using JOIN keeps the data consistent.


## What is the difference between INNER JOIN and LEFT JOIN?

INNER JOIN returns only rows where both tables have matching data.

LEFT JOIN returns all rows from the left table, even if there is no matching record in the right table.


Example:

INNER JOIN shows students who have enrollments.

LEFT JOIN can show students who have no enrollments.


## Which constraint test was most important and why?

The foreign key test was the most important because it proves the database prevents invalid relationships.

For example, a course should not be created with an instructor that does not exist.


## How does this prepare you for Databricks tables and reporting?

This practice teaches how real data systems are structured.

Databricks also uses connected tables, relationships, and clean data models. Understanding keys, relationships, and joins helps create reliable analytics and reports.
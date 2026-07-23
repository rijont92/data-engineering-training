# Day 14 - Database Design Challenge

## Project Goal

The goal of this project is to design and build a relational database for a training center management system.

The database is designed to store and analyze information about students, programs, instructors, enrollments, attendance, and payments.

The main focus is:
- maintaining data consistency,
- creating relationships between entities,
- generating business reports,
- performing data quality checks.

---

## Business Scenario

Unity Tech Hub offers different training programs where students can enroll, attend sessions, and make payments.

Management needs a database system that can answer business questions such as:

- Which programs have the most students?
- Which programs generate the highest revenue?
- Which students have attendance problems?
- Which payments are missing or incomplete?
- Which instructors manage the most active students?

The database supports operational tracking and business decision-making.

---

## Database Design

The database contains the following tables:

### Students
Stores information about registered students.

Columns include:
- student_id
- full_name
- email
- phone
- city
- registration_date

### Programs
Stores available training programs.

Columns include:
- program_id
- program_name
- category
- duration_months
- monthly_fee

### Instructors
Stores instructor information.

Columns include:
- instructor_id
- full_name
- email
- specialization

### Enrollments
Connects students, programs, and instructors.

Stores:
- enrollment date
- enrollment status

### Attendance
Tracks student attendance for each session.

Stores:
- session date
- attendance status

### Payments
Tracks financial information.

Stores:
- payment month
- amount
- payment status

---

## Primary Keys and Foreign Keys

### Primary Keys

Each table has a unique identifier:

- students.student_id
- programs.program_id
- instructors.instructor_id
- enrollments.enrollment_id
- attendance.attendance_id
- payments.payment_id

Primary keys guarantee that every record is unique.

---

### Foreign Keys

Foreign keys create relationships between tables:

- enrollments.student_id → students.student_id
- enrollments.program_id → programs.program_id
- enrollments.instructor_id → instructors.instructor_id
- attendance.enrollment_id → enrollments.enrollment_id
- payments.enrollment_id → enrollments.enrollment_id

Foreign keys prevent invalid data from entering the database.

---

## Relationships

The database uses the following relationships:

### Students - Enrollments
One student can have multiple enrollments.

### Programs - Enrollments
One program can have many students.

### Instructors - Enrollments
One instructor can manage multiple students.

### Enrollments - Attendance
One enrollment can have multiple attendance records.

### Enrollments - Payments
One enrollment can have multiple payment records.

The enrollments table acts as the connection between students, programs, and instructors.

---

## Constraints

The database uses constraints to protect data quality.

Examples:

### NOT NULL
Ensures required information exists.

Example:
- student name
- email
- program name

### UNIQUE
Prevents duplicate values.

Example:
- student email
- instructor email

### PRIMARY KEY
Ensures every record has a unique identifier.

### FOREIGN KEY
Maintains valid relationships between tables.

### CHECK
Validates allowed values.

Examples:

Enrollment status:
- active
- completed
- dropped

Payment status:
- paid
- partial
- unpaid

Attendance:
- 0 = absent
- 1 = attended

Duration and payment amounts must be positive values.

---

## How to Run

Run the SQL files in this order:

1. database_schema.sql  
Creates all tables and relationships.

2. insert_data.sql  
Adds realistic test data.

3. relationship_tests.sql  
Tests foreign keys and constraints using invalid examples.

4. join_reports.sql  
Creates reports using JOIN operations.

5. aggregation_reports.sql  
Creates reports using COUNT, SUM, AVG.

6. having_reports.sql  
Creates filtered business reports using HAVING.

7. data_quality_checks.sql  
Finds missing or risky data.

---

## Most Important Reports

Important reports created:

- Students with their programs and instructors.
- Active, completed, and dropped enrollments.
- Attendance analysis by student and program.
- Revenue collected by program and city.
- Top performing programs.
- Instructor workload analysis.
- Students with financial or attendance risks.

---

## Data Quality Checks Discovered

The database checks for:

- Students without enrollments.
- Programs without students.
- Enrollments without payments.
- Enrollments without attendance records.
- Active students with unpaid payments.
- Students with low attendance.
- Dropped students with payments.
- Instructors without active students.
- Invalid or incomplete records.

These checks help ensure the data is complete and trustworthy.

---

## Business Insights

The database can help management understand:

- Which programs are most popular.
- Which programs generate the most revenue.
- Where students are located.
- Which students need support.
- Which instructors have high workloads.
- Where operational improvements are needed.

---

## What I Can Explain Live

I can explain:

- How primary keys and foreign keys work.
- Why relationships are needed in relational databases.
- How JOINs combine information from different tables.
- Difference between WHERE and HAVING.
- How aggregation functions like COUNT, SUM, and AVG work.
- How constraints protect data quality.
- How the database supports business reporting.
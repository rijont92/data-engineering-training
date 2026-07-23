# Database Design Plan
## Day 14 - Database Design Challenge


# Project Goal

The goal of this database is to manage a training center system where students can enroll in different programs, attend classes, work with instructors, and make payments.

The database solves the problem of organizing student information, program management, attendance tracking, and financial records in one structured system.

The design allows management to:
- track student enrollments,
- monitor attendance performance,
- analyze payments and revenue,
- evaluate instructor workload,
- identify students who need support.


# Tables

## Students Table

The students table stores information about all registered students.

It keeps basic student information such as:
- name,
- email,
- phone number,
- city,
- registration date.

This table is needed because students are the main users of the training programs.


## Programs Table

The programs table stores all available training programs.

It contains:
- program name,
- category,
- duration,
- monthly fee.

This table allows management to track different courses and analyze which programs are more popular or profitable.


## Instructors Table

The instructors table stores information about teachers responsible for programs.

It contains:
- instructor name,
- email,
- specialization.

This table helps track instructor responsibilities and workload.


## Enrollments Table

The enrollments table connects students, programs, and instructors.

It stores:
- which student joined which program,
- which instructor is responsible,
- enrollment date,
- enrollment status.

This table is the main relationship table because one student can join multiple programs and one program can have many students.


## Attendance Table

The attendance table stores student attendance records for each session.

It contains:
- enrollment reference,
- session date,
- attendance value.

This table allows analysis of student performance and attendance rates.


## Payments Table

The payments table stores financial transactions.

It contains:
- enrollment reference,
- payment month,
- payment amount,
- payment status.

This allows management to track collected revenue and students with payment problems.


# Primary Keys

Each table has a primary key that uniquely identifies every record.

Primary keys:

- Students:
  - student_id

- Programs:
  - program_id

- Instructors:
  - instructor_id

- Enrollments:
  - enrollment_id

- Attendance:
  - attendance_id

- Payments:
  - payment_id


Primary keys prevent duplicate records and allow tables to connect correctly.


# Foreign Keys

Foreign keys create relationships between tables.

Relationships:

## Enrollments → Students

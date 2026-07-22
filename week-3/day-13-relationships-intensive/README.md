# Day 13 - Intensive Relationships and Foreign Keys

## Project Goal

The goal of this project was to design a relational database for Unity Tech Hub training management.

The database tracks students, instructors, courses, enrollments, attendance, assignments, and submissions.

The main focus was understanding primary keys, foreign keys, relationships, constraints, and creating reports using SQL JOINs.


## Database Design

The database was designed by separating information into different tables instead of storing everything in one large table.

This avoids duplicated data and makes the database easier to maintain.

The main entities are:

- Students
- Instructors
- Courses
- Enrollments
- Attendance
- Assignments
- Submissions


## Tables and Relationships

### Students

Stores information about students.

Relationship:
- One student can have many enrollments.
- One student can have many submissions.


### Instructors

Stores information about instructors.

Relationship:
- One instructor can teach many courses.


### Courses

Stores training courses.

Relationship:
- Each course belongs to one instructor.
- One course can have many enrollments.
- One course can have many assignments.


### Enrollments

This is a bridge table between students and courses.

Relationship:
- Many students can join many courses.

It also stores enrollment date and status.


### Attendance

Stores attendance records for enrollments.

Relationship:
- One enrollment can have many attendance records.


### Assignments

Stores assignments created for courses.

Relationship:
- One course can have many assignments.


### Submissions

Stores student assignment submissions.

Relationship:
- One student can submit many assignments.
- One assignment can have many submissions.


## Primary Keys, Foreign Keys, and Constraints

Primary keys were used to uniquely identify every row.

Examples:
- student_id
- instructor_id
- course_id

Foreign keys were used to connect tables.

Examples:
- courses.instructor_id references instructors
- enrollments.student_id references students
- enrollments.course_id references courses

Constraints were added to protect data quality:

- PRIMARY KEY for unique IDs
- AUTOINCREMENT for automatic ID generation
- FOREIGN KEY for relationships
- UNIQUE for preventing duplicate emails and enrollments
- NOT NULL for required fields
- CHECK for valid values like status and levels


## Seed Data

Realistic sample data was inserted into all tables.

Inserted data includes:

- 8 students
- 3 instructors
- 5 courses
- 12 enrollments
- 18 attendance records
- 6 assignments
- 12 submissions

The data was created to make JOIN reports and manager reports meaningful.


## Constraint Tests

Constraint tests were created to verify database protection.

Tests included:

- Invalid instructor ID
- Invalid student ID
- Invalid course ID
- Duplicate enrollment
- Invalid attendance minutes
- Invalid course level
- Invalid submission assignment
- Duplicate student email

The failed inserts prove that the database prevents incorrect data.


## JOIN Reports

JOIN queries were created to combine information from multiple tables.

Reports include:

- Students with their courses
- Courses with instructors
- Assignments with courses
- Attendance reports
- Submission reports
- Students enrolled in multiple courses
- Students without enrollments using LEFT JOIN


## Manager Report

A business-focused report was created for Unity Tech Hub management.

The report answers questions like:

- Which courses have the most enrollments?
- Which students are active in multiple courses?
- Which course has the strongest attendance?
- Which students need attention because of missing submissions?
- Which instructor has the highest active enrollments?

A final combined report includes:

- Student name
- Course name
- Instructor name
- Enrollment status
- Total sessions
- Attended sessions
- Total minutes
- Average score


## Screenshots

Screenshots included:

- Successful schema execution
- Tables after seed inserts
- Failed foreign key tests
- Failed constraint tests
- Enrollment JOIN report
- Submission JOIN report
- LEFT JOIN reports
- Final manager report


## What I Can Explain Live

I can explain:

- Why databases use multiple tables instead of one large table
- Primary keys and foreign keys
- One-to-many relationships
- Many-to-many relationships
- Why enrollments is a bridge table
- How JOINs combine data
- How constraints protect data quality
- How reports are created from relational data


## What I Would Improve Next

Next improvements could include:

- Adding more detailed attendance tracking
- Adding user roles and permissions
- Creating more automated data validation
- Building dashboards from SQL reports
- Connecting the database with Python or Databricks pipelines
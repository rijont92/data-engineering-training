# Day 13 - Database Design Before SQL

## Database Model Explanation

The purpose of this database is to manage Unity Tech Hub training data.

Instead of storing all information in one large table, the data is separated into different tables based on real-world entities. This design reduces duplicate data, keeps information consistent, and makes reporting easier.

The main entities are:

- Students
- Instructors
- Courses
- Enrollments
- Attendance
- Assignments
- Submissions

## Tables and Relationship Logic

### Students

Represents people attending training.

**Primary Key:** `student_id`

**Relationships:**
- One student can have many enrollments.
- One student can have many submissions.

### Instructors

Represents people teaching courses.

**Primary Key:** `instructor_id`

**Relationships:**
- One instructor can teach many courses.

### Courses

Represents training courses or modules.

**Primary Key:** `course_id`

**Foreign Key:** `instructor_id` references `instructors(instructor_id)`

**Relationships:**
- One course belongs to one instructor.
- One course can have many enrollments.
- One course can have many assignments.

### Enrollments

Represents the relationship between students and courses.

**Primary Key:** `enrollment_id`

**Foreign Keys:**
- `student_id` references `students(student_id)`
- `course_id` references `courses(course_id)`

**Relationships:**
- Connects students and courses.
- Stores information like enrollment date and status.

Enrollments is a bridge table because students and courses have a many-to-many relationship.

### Attendance

Represents attendance records for each enrollment session.

**Primary Key:** `attendance_id`

**Foreign Key:** `enrollment_id` references `enrollments(enrollment_id)`

**Relationship:**
- One enrollment can have many attendance records.

### Assignments

Represents tasks created for courses.

**Primary Key:** `assignment_id`

**Foreign Key:** `course_id` references `courses(course_id)`

**Relationship:**
- One course can have many assignments.

### Submissions

Represents student assignment work.

**Primary Key:** `submission_id`

**Foreign Keys:**
- `assignment_id` references `assignments(assignment_id)`
- `student_id` references `students(student_id)`

**Relationship:**
- Connects students with assignments.
- Stores score and submission status.

## One-to-Many Relationships

Examples of one-to-many relationships in this database:

**1. One instructor can teach many courses.**
```
instructors
    |
    | 1:N
    |
 courses
```

**2. One course can have many assignments.**
```
courses
    |
    | 1:N
    |
 assignments
```

**3. One student can have many submissions.**
```
students
    |
    | 1:N
    |
 submissions
```

## Many-to-Many Relationship

Students and courses have a many-to-many relationship.

A student can join multiple courses, and a course can contain multiple students.

This relationship is solved using the `enrollments` bridge table.

```
students
    |
    |
enrollments
    |
    |
 courses
```

## Why course_name Should Not Be Stored Repeatedly Inside Students

The course name should not be stored inside the students table because it creates duplicated data.

A student can join multiple courses, and storing course names there would create repeated values. If a course name changes, many student records would need to be updated.

Instead, we store `course_id` in enrollments and use JOINs to get the course name when needed.

## Database Relationship Diagram

Since several entities connect to more than one other table, it's clearer to show each relationship chain separately rather than as one long line.

**Instructors → Courses → Assignments → Submissions**
```
instructors
    |
    | 1:N
    |
 courses
    |
    | 1:N
    |
 assignments
    |
    | 1:N
    |
 submissions
    |
    | N:1
    |
 students
```

**Students → Enrollments → Courses**
```
students
    |
    | 1:N
    |
enrollments
    |
    | N:1
    |
 courses
```

**Enrollments → Attendance**
```
enrollments
    |
    | 1:N
    |
attendance
```

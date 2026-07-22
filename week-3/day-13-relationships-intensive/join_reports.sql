-- 1. Show all students with city and email
SELECT
    student_id,
    full_name,
    city,
    email
FROM students;


-- 2. Show all courses with instructor name and specialization
SELECT
    courses.course_name,
    courses.level,
    instructors.full_name AS instructor_name,
    instructors.specialization
FROM courses
JOIN instructors
ON courses.instructor_id = instructors.instructor_id;


-- 3. Show all assignments with course name and due date
SELECT
    assignments.title AS assignment_title,
    courses.course_name,
    assignments.due_date
FROM assignments
JOIN courses
ON assignments.course_id = courses.course_id;


-- 4. Show all enrollments with student and course information
SELECT
    students.full_name AS student_name,
    courses.course_name,
    enrollments.enrollment_date,
    enrollments.status
FROM enrollments
JOIN students
ON enrollments.student_id = students.student_id
JOIN courses
ON enrollments.course_id = courses.course_id;


-- 5. Show only active enrollments
SELECT
    students.full_name AS student_name,
    courses.course_name,
    enrollments.enrollment_date,
    enrollments.status
FROM enrollments
JOIN students
ON enrollments.student_id = students.student_id
JOIN courses
ON enrollments.course_id = courses.course_id
WHERE enrollments.status = 'active';


-- 6. Show attendance records
SELECT
    students.full_name AS student_name,
    courses.course_name,
    attendance.session_date,
    attendance.attended,
    attendance.minutes_attended
FROM attendance
JOIN enrollments
ON attendance.enrollment_id = enrollments.enrollment_id
JOIN students
ON enrollments.student_id = students.student_id
JOIN courses
ON enrollments.course_id = courses.course_id;


-- 7. Show submissions with student, assignment, course
SELECT
    students.full_name AS student_name,
    assignments.title AS assignment_title,
    courses.course_name,
    submissions.score,
    submissions.status
FROM submissions
JOIN students
ON submissions.student_id = students.student_id
JOIN assignments
ON submissions.assignment_id = assignments.assignment_id
JOIN courses
ON assignments.course_id = courses.course_id;


-- 8. Count students enrolled in each course
SELECT
    courses.course_name,
    COUNT(enrollments.student_id) AS total_students
FROM courses
LEFT JOIN enrollments
ON courses.course_id = enrollments.course_id
GROUP BY courses.course_id, courses.course_name;


-- 9. Students enrolled in more than one course
SELECT
    students.full_name,
    COUNT(enrollments.course_id) AS course_count
FROM students
JOIN enrollments
ON students.student_id = enrollments.student_id
GROUP BY students.student_id, students.full_name
HAVING COUNT(enrollments.course_id) > 1;


-- 10. Average attendance minutes by course
SELECT
    courses.course_name,
    AVG(attendance.minutes_attended) AS average_minutes
FROM attendance
JOIN enrollments
ON attendance.enrollment_id = enrollments.enrollment_id
JOIN courses
ON enrollments.course_id = courses.course_id
GROUP BY courses.course_id, courses.course_name;


-- 11. Average score by course
SELECT
    courses.course_name,
    AVG(submissions.score) AS average_score
FROM submissions
JOIN assignments
ON submissions.assignment_id = assignments.assignment_id
JOIN courses
ON assignments.course_id = courses.course_id
GROUP BY courses.course_id, courses.course_name;


-- 12. Missing or late submissions
SELECT
    students.full_name AS student_name,
    courses.course_name,
    assignments.title AS assignment_title,
    submissions.status
FROM submissions
JOIN students
ON submissions.student_id = students.student_id
JOIN assignments
ON submissions.assignment_id = assignments.assignment_id
JOIN courses
ON assignments.course_id = courses.course_id
WHERE submissions.status IN ('missing','late');


-- 13. Students with no enrollments
SELECT
    students.full_name,
    students.city,
    students.email
FROM students
LEFT JOIN enrollments
ON students.student_id = enrollments.student_id
WHERE enrollments.enrollment_id IS NULL;


-- 14. Assignments with no submissions
SELECT
    assignments.title AS assignment_title,
    courses.course_name
FROM assignments
LEFT JOIN submissions
ON assignments.assignment_id = submissions.assignment_id
JOIN courses
ON assignments.course_id = courses.course_id
WHERE submissions.submission_id IS NULL;
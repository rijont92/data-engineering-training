-- 1. Courses with the most enrollments
SELECT
    courses.course_name,
    COUNT(enrollments.enrollment_id) AS total_enrollments
FROM courses
JOIN enrollments
ON courses.course_id = enrollments.course_id
GROUP BY courses.course_name
ORDER BY total_enrollments DESC;


-- 2. Students active in more than one course
SELECT
    students.full_name,
    COUNT(enrollments.course_id) AS total_courses
FROM students
JOIN enrollments
ON students.student_id = enrollments.student_id
WHERE enrollments.status = 'active'
GROUP BY students.full_name
HAVING COUNT(enrollments.course_id) > 1;


-- 3. Strongest average attendance by course
SELECT
    courses.course_name,
    AVG(attendance.minutes_attended) AS average_minutes
FROM courses
JOIN enrollments
ON courses.course_id = enrollments.course_id
JOIN attendance
ON enrollments.enrollment_id = attendance.enrollment_id
GROUP BY courses.course_name
ORDER BY average_minutes DESC;


-- 4. Weakest assignment completion
SELECT
    courses.course_name,
    COUNT(submissions.submission_id) AS total_submissions
FROM courses
JOIN assignments
ON courses.course_id = assignments.course_id
LEFT JOIN submissions
ON assignments.assignment_id = submissions.assignment_id
GROUP BY courses.course_name
ORDER BY total_submissions ASC;


-- 5. Students with missing or late submissions
SELECT
    students.full_name,
    courses.course_name,
    assignments.title,
    submissions.status
FROM students
JOIN submissions
ON students.student_id = submissions.student_id
JOIN assignments
ON submissions.assignment_id = assignments.assignment_id
JOIN courses
ON assignments.course_id = courses.course_id
WHERE submissions.status = 'missing'
OR submissions.status = 'late';


-- 6. Instructor with most active enrollments
SELECT
    instructors.full_name,
    COUNT(enrollments.enrollment_id) AS active_students
FROM instructors
JOIN courses
ON instructors.instructor_id = courses.instructor_id
JOIN enrollments
ON courses.course_id = enrollments.course_id
WHERE enrollments.status = 'active'
GROUP BY instructors.full_name
ORDER BY active_students DESC
LIMIT 1;


-- 7. Final manager report
SELECT
    students.full_name AS student_name,
    courses.course_name,
    instructors.full_name AS instructor_name,
    enrollments.status,
    COUNT(attendance.attendance_id) AS total_sessions,
    SUM(attendance.attended) AS attended_sessions,
    SUM(attendance.minutes_attended) AS total_minutes,
    AVG(submissions.score) AS average_score
FROM students
JOIN enrollments
ON students.student_id = enrollments.student_id
JOIN courses
ON enrollments.course_id = courses.course_id
JOIN instructors
ON courses.instructor_id = instructors.instructor_id
LEFT JOIN attendance
ON enrollments.enrollment_id = attendance.enrollment_id
LEFT JOIN submissions
ON students.student_id = submissions.student_id
GROUP BY
    students.full_name,
    courses.course_name,
    instructors.full_name,
    enrollments.status;
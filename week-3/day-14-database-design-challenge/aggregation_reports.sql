-- Count students by city
SELECT city,COUNT(*) AS city_count FROM students
GROUP BY CITY;

-- Count enrollments by status
SELECT 
	enrollments.status,
    COUNT(*) AS status_count
FROM enrollments
GROUP BY enrollments.status;


-- Count enrollments by program
SELECT 
	programs.program_name AS program_name,
    COUNT(enrollments.enrollment_id) AS enrollments_count
FROM programs
LEFT JOIN enrollments
	ON programs.program_id = enrollments.program_id
GROUP BY programs.program_id, programs.program_name;


-- Count active enrollments by program
SELECT
    programs.program_name AS program_name,
    COUNT(enrollments.enrollment_id) AS active_enrollments_count
FROM programs
JOIN enrollments
    ON programs.program_id = enrollments.program_id
WHERE enrollments.status = 'active'
GROUP BY programs.program_id, programs.program_name;


-- Calculate total paid amount by program.
SELECT
    programs.program_name AS program_name,
    SUM(payments.amount) AS total_paid_amount
FROM programs
JOIN enrollments
    ON programs.program_id = enrollments.program_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE payments.payment_status = 'paid'
GROUP BY programs.program_id, programs.program_name;


-- Calculate unpaid or partial amount by program.
SELECT
    programs.program_name AS program_name,
    SUM(payments.amount) AS unpaid_partial_amount
FROM programs
JOIN enrollments
    ON programs.program_id = enrollments.program_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE payments.payment_status IN ('unpaid', 'partial')
GROUP BY programs.program_id, programs.program_name;


-- Calculate collected revenue by city
SELECT
    students.city AS city,
    SUM(payments.amount) AS collected_revenue
FROM students
JOIN enrollments
    ON students.student_id = enrollments.student_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE payments.payment_status = 'paid'
GROUP BY students.city;


-- Calculate average attendance rate by student.
SELECT
    students.full_name AS student_name,
    ROUND(AVG(attendance.attended) * 100, 2) AS attendance_rate
FROM students
JOIN enrollments
    ON students.student_id = enrollments.student_id
JOIN attendance
    ON enrollments.enrollment_id = attendance.enrollment_id
GROUP BY students.student_id, students.full_name;

-- Calculate average attendance rate by program.
SELECT
    programs.program_name AS program_name,
    ROUND(AVG(attendance.attended) * 100, 2) AS attendance_rate
FROM programs
JOIN enrollments
    ON programs.program_id = enrollments.program_id
JOIN attendance
    ON enrollments.enrollment_id = attendance.enrollment_id
GROUP BY programs.program_id, programs.program_name;


-- Show top 5 students by attendance rate
SELECT
    students.full_name AS student_name,
    ROUND(AVG(attendance.attended) * 100, 2) AS attendance_rate
FROM students
JOIN enrollments
    ON students.student_id = enrollments.student_id
JOIN attendance
    ON enrollments.enrollment_id = attendance.enrollment_id
GROUP BY students.student_id, students.full_name
ORDER BY attendance_rate DESC
LIMIT 5;


-- Show top 5 programs by collected revenue.
SELECT
    programs.program_name AS program_name,
    SUM(payments.amount) AS collected_revenue
FROM programs
JOIN enrollments
    ON programs.program_id = enrollments.program_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE payments.payment_status = 'paid'
GROUP BY programs.program_id, programs.program_name
ORDER BY collected_revenue DESC
LIMIT 5;


-- Show instructors ranked by number of active students.
SELECT
    instructors.full_name AS instructor_name,
    COUNT(enrollments.student_id) AS active_students_count
FROM instructors
JOIN enrollments
    ON instructors.instructor_id = enrollments.instructor_id
WHERE enrollments.status = 'active'
GROUP BY instructors.instructor_id, instructors.full_name
ORDER BY active_students_count DESC;




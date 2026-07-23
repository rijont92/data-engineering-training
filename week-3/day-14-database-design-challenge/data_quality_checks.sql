-- Find students with no enrollments
SELECT
    students.full_name AS student_name
FROM students
LEFT JOIN enrollments
    ON students.student_id = enrollments.student_id
WHERE enrollments.enrollment_id IS NULL;


-- Find programs with no enrollments
SELECT
    programs.program_name AS program_name
FROM programs
LEFT JOIN enrollments
    ON programs.program_id = enrollments.program_id
WHERE enrollments.enrollment_id IS NULL;


-- Find enrollments with no payment record
SELECT
    enrollments.enrollment_id,
    students.full_name AS student_name,
    programs.program_name AS program_name
FROM enrollments
JOIN students
    ON enrollments.student_id = students.student_id
JOIN programs
    ON enrollments.program_id = programs.program_id
LEFT JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE payments.payment_id IS NULL;


-- Find enrollments with no attendance records
SELECT
    enrollments.enrollment_id,
    students.full_name AS student_name,
    programs.program_name AS program_name
FROM enrollments
JOIN students
    ON enrollments.student_id = students.student_id
JOIN programs
    ON enrollments.program_id = programs.program_id
LEFT JOIN attendance
    ON enrollments.enrollment_id = attendance.enrollment_id
WHERE attendance.attendance_id IS NULL;


-- Find active students with unpaid or partial payments
SELECT
    students.full_name AS student_name,
    programs.program_name AS program_name,
    payments.payment_status AS payment_status,
    payments.amount AS amount
FROM enrollments
JOIN students
    ON enrollments.student_id = students.student_id
JOIN programs
    ON enrollments.program_id = programs.program_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE enrollments.status = 'active'
AND payments.payment_status IN ('unpaid', 'partial');


-- Find students with low attendance but paid payment
SELECT
    students.full_name AS student_name,
    ROUND(AVG(attendance.attended) * 100, 2) AS attendance_rate,
    payments.payment_status
FROM students
JOIN enrollments
    ON students.student_id = enrollments.student_id
JOIN attendance
    ON enrollments.enrollment_id = attendance.enrollment_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE payments.payment_status = 'paid'
GROUP BY students.student_id, students.full_name, payments.payment_status
HAVING AVG(attendance.attended) * 100 < 70;


-- Find students with high attendance but unpaid or partial payment
SELECT
    students.full_name AS student_name,
    ROUND(AVG(attendance.attended) * 100, 2) AS attendance_rate,
    payments.payment_status
FROM students
JOIN enrollments
    ON students.student_id = enrollments.student_id
JOIN attendance
    ON enrollments.enrollment_id = attendance.enrollment_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE payments.payment_status IN ('unpaid', 'partial')
GROUP BY students.student_id, students.full_name, payments.payment_status
HAVING AVG(attendance.attended) * 100 > 80;


-- Find dropped students who still have paid or partial payment records
SELECT
    students.full_name AS student_name,
    programs.program_name AS program_name,
    payments.payment_status AS payment_status,
    payments.amount AS amount
FROM enrollments
JOIN students
    ON enrollments.student_id = students.student_id
JOIN programs
    ON enrollments.program_id = programs.program_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE enrollments.status = 'dropped'
AND payments.payment_status IN ('paid', 'partial');


-- Find instructors with no active students
SELECT
    instructors.full_name AS instructor_name
FROM instructors
LEFT JOIN enrollments
    ON instructors.instructor_id = enrollments.instructor_id
    AND enrollments.status = 'active'
WHERE enrollments.enrollment_id IS NULL;


-- Find risky, inconsistent, or incomplete records
SELECT
    payment_id,
    enrollment_id,
    amount,
    payment_status
FROM payments
WHERE amount < 0
OR payment_status NOT IN ('paid', 'partial', 'unpaid');


SELECT
    enrollment_id,
    student_id,
    program_id,
    instructor_id
FROM enrollments
WHERE student_id IS NULL
OR program_id IS NULL
OR instructor_id IS NULL;

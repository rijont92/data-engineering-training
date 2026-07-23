-- BONUS CHALLENGES
-- Day 14 - Database Design Challenge


-- 1. View for active student enrollments
-- Shows students who are currently active,
-- their programs and instructors.

CREATE VIEW active_student_enrollments AS
SELECT
    students.full_name AS student_name,
    students.city,
    programs.program_name,
    instructors.full_name AS instructor_name,
    enrollments.enrollment_date,
    enrollments.status
FROM enrollments
JOIN students
    ON enrollments.student_id = students.student_id
JOIN programs
    ON enrollments.program_id = programs.program_id
JOIN instructors
    ON enrollments.instructor_id = instructors.instructor_id
WHERE enrollments.status = 'active';



-- 2. View for program revenue
-- Shows collected revenue by program.

CREATE VIEW program_revenue AS
SELECT
    programs.program_name,
    SUM(payments.amount) AS total_revenue
FROM programs
JOIN enrollments
    ON programs.program_id = enrollments.program_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id
WHERE payments.payment_status = 'paid'
GROUP BY programs.program_id, programs.program_name;



-- 3. View for student risk summary
-- Combines attendance and payment risk.

CREATE VIEW student_risk_summary AS
SELECT
    students.full_name AS student_name,

    ROUND(AVG(attendance.attended) * 100, 2) 
        AS attendance_rate,

    CASE
        WHEN AVG(attendance.attended) * 100 < 70
        THEN 'High Academic Risk'
        ELSE 'Normal'
    END AS academic_risk,

    CASE
        WHEN payments.payment_status IN ('unpaid','partial')
        THEN 'Financial Risk'
        ELSE 'Normal'
    END AS financial_risk

FROM students
JOIN enrollments
    ON students.student_id = enrollments.student_id
JOIN attendance
    ON enrollments.enrollment_id = attendance.enrollment_id
JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id

GROUP BY
    students.student_id,
    students.full_name,
    payments.payment_status;



-- 4. Scholarship / Discount Concept
-- Adds discounts for students.

CREATE TABLE scholarships(
    scholarship_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INTEGER NOT NULL,
    discount_percentage INTEGER 
        CHECK(discount_percentage BETWEEN 0 AND 100),
    reason TEXT NOT NULL,

    FOREIGN KEY (enrollment_id)
        REFERENCES enrollments(enrollment_id)
);



-- Example scholarship data

INSERT INTO scholarships
(
    enrollment_id,
    discount_percentage,
    reason
)
VALUES
(1, 50, 'High academic performance'),
(3, 25, 'Financial support');



-- 5. Certificate Concept
-- Stores certificates for completed students.

CREATE TABLE certificates(
    certificate_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INTEGER NOT NULL,
    issue_date DATE NOT NULL,
    certificate_code VARCHAR(50) UNIQUE,

    FOREIGN KEY (enrollment_id)
        REFERENCES enrollments(enrollment_id)
);



-- Example certificates

INSERT INTO certificates
(
    enrollment_id,
    issue_date,
    certificate_code
)
VALUES
(2, '2026-07-20', 'CERT-001'),
(5, '2026-07-21', 'CERT-002');



-- 6. Combined academic and financial risk report
-- Finds students with low attendance
-- and payment problems.

SELECT
    students.full_name AS student_name,

    ROUND(AVG(attendance.attended) * 100,2)
        AS attendance_rate,

    payments.payment_status

FROM students

JOIN enrollments
    ON students.student_id = enrollments.student_id

JOIN attendance
    ON enrollments.enrollment_id = attendance.enrollment_id

JOIN payments
    ON enrollments.enrollment_id = payments.enrollment_id

WHERE payments.payment_status IN ('unpaid','partial')

GROUP BY
    students.student_id,
    students.full_name,
    payments.payment_status

HAVING AVG(attendance.attended) * 100 < 70;



-- 7. Student readiness report
-- Useful for Agilyti or partners.
-- Shows completed students with strong attendance.

SELECT
    students.full_name AS student_name,
    programs.program_name,
    ROUND(AVG(attendance.attended) * 100,2)
        AS attendance_rate,
    enrollments.status

FROM students

JOIN enrollments
    ON students.student_id = enrollments.student_id

JOIN programs
    ON enrollments.program_id = programs.program_id

JOIN attendance
    ON enrollments.enrollment_id = attendance.enrollment_id

WHERE enrollments.status = 'completed'

GROUP BY
    students.student_id,
    students.full_name,
    programs.program_name,
    enrollments.status

HAVING AVG(attendance.attended) * 100 >= 80;
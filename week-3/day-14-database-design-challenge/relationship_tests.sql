-- ==========================================
-- TEST 1: Enrollment with non-existing student_id
-- Expected: FAIL
-- Reason: Foreign key prevents enrollment for a student that does not exist.
-- ==========================================

-- INSERT INTO enrollments
-- (student_id, program_id, instructor_id, enrollment_date, status)
-- VALUES
-- (999, 1, 1, '2026-05-01', 'active');


-- ==========================================
-- TEST 2: Enrollment with non-existing program_id
-- Expected: FAIL
-- Reason: Foreign key prevents enrollment for a program that does not exist.
-- ==========================================

-- INSERT INTO enrollments
-- (student_id, program_id, instructor_id, enrollment_date, status)
-- VALUES
-- (1, 999, 1, '2026-05-01', 'active');


-- ==========================================
-- TEST 3: Attendance with non-existing enrollment_id
-- Expected: FAIL
-- Reason: Attendance must belong to an existing enrollment.
-- ==========================================

-- INSERT INTO attendance
-- (enrollment_id, session_date, attended)
-- VALUES
-- (999, '2026-05-01', 1);


-- ==========================================
-- TEST 4: Payment with non-existing enrollment_id
-- Expected: FAIL
-- Reason: Payment must belong to an existing enrollment.
-- ==========================================

-- INSERT INTO payments
-- (enrollment_id, payment_month, amount, payment_status)
-- VALUES
-- (999, 'May', 200, 'paid');


-- ==========================================
-- TEST 5: Duplicate student email
-- Expected: FAIL
-- Reason: Email column has UNIQUE constraint.
-- ==========================================

-- INSERT INTO students
-- (full_name, email, phone, city, registration_date)
-- VALUES
-- ('Test Student', 'rijon@gmail.com', '049000000', 'Prishtina', '2026-05-01');


-- ==========================================
-- TEST 6: Negative payment amount
-- Expected: FAIL
-- Reason: CHECK constraint prevents negative payments.
-- ==========================================

-- INSERT INTO payments
-- (enrollment_id, payment_month, amount, payment_status)
-- VALUES
-- (1, 'May', -50, 'paid');


-- ==========================================
-- TEST 7: Invalid enrollment status
-- Expected: FAIL
-- Reason: CHECK constraint only allows:
-- active, completed, dropped
-- ==========================================

-- INSERT INTO enrollments
-- (student_id, program_id, instructor_id, enrollment_date, status)
-- VALUES
-- (1, 1, 1, '2026-05-01', 'pending');


-- ==========================================
-- TEST 8: Invalid attendance value
-- Expected: FAIL
-- Reason: attended only accepts 0 or 1.
-- ==========================================

-- INSERT INTO attendance
-- (enrollment_id, session_date, attended)
-- VALUES
-- (1, '2026-05-01', 5);

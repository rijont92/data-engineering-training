 -- Invalid course instructor
-- FOREIGN KEY error: instructor does not exist
INSERT INTO courses(course_name, level, instructor_id)
VALUES ('Machine Learning', 'Advanced', 999);


-- Invalid enrollment student
-- FOREIGN KEY error: student does not exist
INSERT INTO enrollments(student_id, course_id, enrollment_date, status)
VALUES (999, 1, '2026-07-20', 'active');


-- Invalid enrollment course
-- FOREIGN KEY error: course does not exist
INSERT INTO enrollments(student_id, course_id, enrollment_date, status)
VALUES (1, 999, '2026-07-20', 'active');


-- Duplicate enrollment
-- UNIQUE(student_id, course_id) error
INSERT INTO enrollments(student_id, course_id, enrollment_date, status)
VALUES (1, 1, '2026-07-25', 'active');


-- Invalid attendance enrollment
-- FOREIGN KEY error
INSERT INTO attendance(enrollment_id, session_date, attended, minutes_attended)
VALUES (999, '2026-07-20', 1, 120);


-- Invalid attendance minutes
-- CHECK error
INSERT INTO attendance(enrollment_id, session_date, attended, minutes_attended)
VALUES (1, '2026-07-20', 1, -10);


-- Invalid course level
-- CHECK error
INSERT INTO courses(course_name, level, instructor_id)
VALUES ('AI Course', 'Expert', 1);


-- Invalid submission assignment
-- FOREIGN KEY error
INSERT INTO submissions(assignment_id, student_id, submitted_at, score, status)
VALUES (999, 1, '2026-07-20', 90, 'submitted');


-- Invalid submission score
-- CHECK error (negative score)
INSERT INTO submissions(assignment_id, student_id, submitted_at, score, status)
VALUES (1, 1, '2026-07-20', -10, 'submitted');


-- Duplicate email
-- UNIQUE error
INSERT INTO students(full_name, city, email, created_at)
VALUES ('Test User', 'Prishtina', 'rijon@gmail.com', '2026-07-20');
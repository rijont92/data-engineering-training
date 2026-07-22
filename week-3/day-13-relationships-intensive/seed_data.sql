INSERT INTO students (full_name, city, email, created_at)
VALUES
('Rijon Tahiri', 'Vushtrri', 'rijon@gmail.com', '2026-07-01'),
('Ardit Krasniqi', 'Prishtina', 'ardit@gmail.com', '2026-07-02'),
('Elira Berisha', 'Peja', 'elira@gmail.com', '2026-07-03'),
('Dren Gashi', 'Prizren', 'dren@gmail.com', '2026-07-04'),
('Sara Hoxha', 'Ferizaj', 'sara@gmail.com', '2026-07-05'),
('Luan Mustafa', 'Gjilan', 'luan@gmail.com', '2026-07-06'),
('Era Shala', 'Mitrovica', 'era@gmail.com', '2026-07-07'),
('Blerim Rexha', 'Gjakova', 'blerim@gmail.com', '2026-07-08');

SELECT * FROM students;



INSERT INTO instructors (full_name, specialization)
VALUES
('Arben Krasniqi', 'SQL Database Engineering'),
('Mentor Hoxha', 'Python Development'),
('Flora Berisha', 'Data Engineering');

SELECT * FROM instructors;


INSERT INTO courses (course_name, level, instructor_id)
VALUES
('SQL Fundamentals', 'Beginner', 1),
('Python Programming', 'Intermediate', 2),
('Databricks Data Engineering', 'Advanced', 3),
('PySpark Processing', 'Advanced', 3),
('Data Modeling', 'Intermediate', 1);

SELECT * FROM courses;


INSERT INTO enrollments
(student_id, course_id, enrollment_date, status)
VALUES
(1,1,'2026-07-01','active'),
(1,2,'2026-07-02','active'),
(1,3,'2026-07-03','active'),

(2,1,'2026-07-01','completed'),
(2,5,'2026-07-03','active'),

(3,2,'2026-07-02','active'),
(3,4,'2026-07-05','active'),

(4,3,'2026-07-04','active'),

(5,1,'2026-07-01','completed'),
(5,5,'2026-07-06','active'),

(6,2,'2026-07-03','active'),

(7,4,'2026-07-05','dropped');

-- Student 8 intentionally has no enrollment

SELECT * FROM enrollments;


INSERT INTO attendance
(enrollment_id, session_date, attended, minutes_attended)
VALUES
(1,'2026-07-10',1,120),
(1,'2026-07-11',1,115),
(2,'2026-07-10',1,130),
(2,'2026-07-12',0,0),
(3,'2026-07-10',1,150),
(4,'2026-07-11',1,110),
(5,'2026-07-12',1,100),
(6,'2026-07-10',1,120),
(7,'2026-07-12',0,0),
(8,'2026-07-11',1,140),
(9,'2026-07-13',1,125),
(10,'2026-07-13',1,130),
(11,'2026-07-14',0,0),
(12,'2026-07-14',1,90),
(3,'2026-07-15',1,145),
(5,'2026-07-15',1,105),
(6,'2026-07-15',1,115),
(8,'2026-07-15',0,0);

SELECT * FROM attendance;


INSERT INTO assignments
(course_id, title, max_score, due_date)
VALUES
(1,'SQL Queries Practice',100,'2026-07-20'),
(1,'Database Joins Task',100,'2026-07-25'),
(2,'Python Data Pipeline',100,'2026-07-22'),
(3,'Databricks ETL Project',100,'2026-07-30'),
(4,'PySpark Transformation Task',100,'2026-08-01'),
(5,'Design Star Schema',100,'2026-08-05');

SELECT * FROM assignments;


INSERT INTO submissions
(assignment_id, student_id, submitted_at, score, status)
VALUES
(1,1,'2026-07-18',95,'submitted'),
(2,1,'2026-07-23',85,'late'),

(1,2,'2026-07-19',90,'submitted'),
(6,2,'2026-07-28',75,'late'),

(3,3,'2026-07-20',88,'submitted'),
(5,3,NULL,NULL,'missing'),

(4,4,'2026-07-25',92,'submitted'),

(1,5,NULL,NULL,'missing'),
(6,5,'2026-08-02',80,'submitted'),

(3,6,'2026-07-21',70,'late'),

(5,7,NULL,NULL,'missing'),

(4,1,'2026-07-29',98,'submitted');

SELECT * FROM submissions;
-- INSERT STUDENTS

INSERT INTO students (full_name, email, phone, city, registration_date)
VALUES
('Rijon Tahiri', 'rijon@gmail.com', '049111111', 'Vushtrri', '2026-01-10'),
('Ardit Krasniqi', 'ardit@gmail.com', '049222222', 'Prishtina', '2026-01-12'),
('Elira Berisha', 'elira@gmail.com', '049333333', 'Peja', '2026-01-15'),
('Dren Gashi', 'dren@gmail.com', '049444444', 'Prizren', '2026-01-18'),
('Sara Hoxha', 'sara@gmail.com', '049555555', 'Ferizaj', '2026-02-01'),
('Luan Shala', 'luan@gmail.com', '049666666', 'Gjilan', '2026-02-05'),
('Era Mustafa', 'era@gmail.com', '049777777', 'Mitrovica', '2026-02-10'),
('Blerim Rexha', 'blerim@gmail.com', '049888888', 'Prishtina', '2026-02-15'),
('Drin Zenjullahu', 'drin@gmail.com', '049288188', 'Prishtina', '2026-02-18'),
('Anisa Krasniqi', 'anisa@gmail.com', '049999999', 'Peja', '2026-02-20'),
('Valon Berisha', 'valon@gmail.com', '048111111', 'Prizren', '2026-02-25');



-- INSERT PROGRAMS

INSERT INTO programs 
(program_name, category, duration_months, monthly_fee)
VALUES
('Data Engineering', 'Technology', 6, 200),
('Python Programming', 'Technology', 4, 150),
('Web Development', 'Technology', 5, 180),
('Digital Marketing', 'Business', 3, 120);



-- INSERT INSTRUCTORS

INSERT INTO instructors
(full_name, email, specialization)
VALUES
('Arben Krasniqi', 'arben@gmail.com', 'Python and Data'),
('Mira Berisha', 'mira@gmail.com', 'Web Development'),
('Gent Shala', 'gent@gmail.com', 'Marketing');


-- INSERT ENROLLMENTS

INSERT INTO enrollments
(student_id, program_id, instructor_id, enrollment_date, status)
VALUES
-- Data Engineering (many enrollments)
(1,1,1,'2026-03-01','active'),
(2,1,1,'2026-03-02','active'),
(3,1,1,'2026-03-03','completed'),
(4,1,1,'2026-03-05','dropped'),
(5,1,1,'2026-03-06','active'),

-- Python Programming
(1,2,1,'2026-03-10','completed'),
(6,2,1,'2026-03-12','active'),
(7,2,1,'2026-03-15','dropped'),

-- Web Development
(8,3,2,'2026-03-20','active'),
(9,3,2,'2026-03-22','completed'),
(10,3,2,'2026-03-25','active'),

-- Digital Marketing
(2,4,3,'2026-04-01','active'),
(4,4,3,'2026-04-02','completed'),

-- Extra enrollment
(5,3,2,'2026-04-05','active');


-- INSERT ATTENDANCE
-- 30+ records

INSERT INTO attendance
(enrollment_id, session_date, attended)
VALUES

(1,'2026-03-10',1),
(1,'2026-03-17',1),
(1,'2026-03-24',1),

(2,'2026-03-10',1),
(2,'2026-03-17',0),
(2,'2026-03-24',1),

(3,'2026-03-10',1),
(3,'2026-03-17',1),
(3,'2026-03-24',1),

(4,'2026-03-10',0),
(4,'2026-03-17',0),
(4,'2026-03-24',1),

(5,'2026-03-10',1),
(5,'2026-03-17',1),

(6,'2026-03-15',1),
(6,'2026-03-22',1),

(7,'2026-03-15',1),
(7,'2026-03-22',0),

(8,'2026-03-20',0),
(8,'2026-03-27',1),

(9,'2026-03-20',1),
(9,'2026-03-27',1),

(10,'2026-03-20',1),
(10,'2026-03-27',1),

(11,'2026-03-20',0),
(11,'2026-03-27',1),

(12,'2026-04-05',1),
(12,'2026-04-12',1),

(13,'2026-04-05',1),
(14,'2026-04-12',0);



-- INSERT PAYMENTS
-- 14 records
-- One enrollment intentionally has no payment

INSERT INTO payments
(enrollment_id, payment_month, amount, payment_status)
VALUES

(1,'March',200,'paid'),
(2,'March',200,'paid'),
(3,'March',200,'paid'),
(4,'March',100,'partial'),
(5,'March',0,'unpaid'),

(6,'March',150,'paid'),
(7,'March',150,'partial'),
(8,'March',0,'unpaid'),

(9,'March',180,'paid'),
(10,'March',180,'paid'),
(11,'April',180,'partial'),

(12,'April',120,'paid'),
(13,'April',120,'unpaid'),

(14,'April',180,'paid');
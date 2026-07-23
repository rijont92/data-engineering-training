SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS programs;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS students;

SET FOREIGN_KEY_CHECKS = 1;


CREATE TABLE students(
    student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    city VARCHAR(50) NOT NULL,
    registration_date DATE NOT NULL
);


CREATE TABLE programs(
    program_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    program_name VARCHAR(255) NOT NULL UNIQUE,
    category VARCHAR(100) NOT NULL,
    duration_months INTEGER NOT NULL CHECK(duration_months > 0),
    monthly_fee DECIMAL(10,2) NOT NULL CHECK(monthly_fee > 0)
);


CREATE TABLE instructors(
    instructor_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    specialization VARCHAR(100) NOT NULL
);


CREATE TABLE enrollments(
    enrollment_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    student_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL 
        CHECK(status IN ('active','completed','dropped')),

    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (program_id) REFERENCES programs(program_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);


CREATE TABLE attendance(
    attendance_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INTEGER NOT NULL,
    session_date DATE NOT NULL,
    attended INTEGER NOT NULL CHECK(attended IN (0,1)),

    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);


CREATE TABLE payments(
    payment_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INTEGER NOT NULL,
    payment_month VARCHAR(20) NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK(amount >= 0),
    payment_status VARCHAR(20) NOT NULL
        CHECK(payment_status IN ('paid','partial','unpaid')),

    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);
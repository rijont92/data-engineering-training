students = [
    {
        "student_id": 1,
        "name": "Arta",
        "city": "Vushtrri",
        "course": "Python",
        "age": 17,
        "attendance": 90,
        "homework_score": 85
    },
    {
        "student_id": 2,
        "name": "Blend",
        "city": "Prishtina",
        "course": "React",
        "age": 18,
        "attendance": 60,
        "homework_score": 70
    },
    {
        "student_id": 3,
        "name": "Dion",
        "city": "Vushtrri",
        "course": "Python",
        "age": 16,
        "attendance": 75,
        "homework_score": 95
    },
    {
        "student_id": 4,
        "name": "Elira",
        "city": "Mitrovica",
        "course": "React",
        "age": 17,
        "attendance": 80,
        "homework_score": 60
    },
    {
        "student_id": 5,
        "name": "Faton",
        "city": "Vushtrri",
        "course": "Data Engineering",
        "age": 19,
        "attendance": 100,
        "homework_score": 90
    },
    {
        "student_id": 6,
        "name": "Gresa",
        "city": "Prishtina",
        "course": "Python",
        "age": 18,
        "attendance": 55,
        "homework_score": 88
    }
]

# Task 1
print("Total students:", len(students))
print("Student names:")
for student in students:
    print(student["name"])

print("\nStudent details:")
for student in students:
    print(f"{student['name']} is from {student['city']} and is learning {student['course']}.")

# Task 2
print("\nStudents from Vushtrri:")
for student in students:
    if student["city"] == "Vushtrri":
        print(student["name"])

print("\nStudents with low attendance:")
for student in students:
    if student["attendance"] < 70:
        print(student["name"])

print("\nStudents with homework score above 85:")
for student in students:
    if student["homework_score"] > 85:
        print(student["name"])

# Task 3
total_attendance = 0
total_homework = 0
for student in students:
    total_attendance += student["attendance"]
    total_homework += student["homework_score"]

avg_attendance = total_attendance / len(students)
avg_homework = total_homework / len(students)

print(f"\nAverage attendance: {avg_attendance:.2f}")
print(f"Average homework score: {avg_homework:.2f}")

city_count = {}
for student in students:
    city = student["city"]
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("\nStudents by city:")
for city, count in city_count.items():
    print(f"{city}: {count}")

course_count = {}
for student in students:
    course = student["course"]
    if course in course_count:
        course_count[course] += 1
    else:
        course_count[course] = 1

print("\nStudents by course:")
for course, count in course_count.items():
    print(f"{course}: {count}")

# Task 4
print("\nPerformance status:")
for student in students:
    attendance = student["attendance"]
    homework = student["homework_score"]
    if attendance >= 80 and homework >= 80:
        status = "Strong"
    elif attendance >= 60 and homework >= 60:
        status = "Average"
    else:
        status = "Needs Support"
    print(f"{student['name']}: {status}")

# Task 5
clean_records = []
for student in students:
    attendance = student["attendance"]
    homework = student["homework_score"]
    if attendance >= 80 and homework >= 80:
        status = "Strong"
    elif attendance >= 60 and homework >= 60:
        status = "Average"
    else:
        status = "Needs Support"
    
    clean_record = {
        "student_id": student["student_id"],
        "name": student["name"],
        "course": student["course"],
        "performance_status": status
    }
    clean_records.append(clean_record)

print("\nClean report records:")
for record in clean_records:
    print(f"{record['student_id']} - {record['name']} - {record['course']} - {record['performance_status']}")

def get_performance_status(student):
    attendance = student.get("attendance", 0)
    homework = student.get("homework_score", 0)
    if attendance >= 80 and homework >= 80:
        return "Strong"
    elif attendance >= 60 and homework >= 60:
        return "Average"
    else:
        return "Needs Support"

def calculate_average_attendance(student_list):
    if not student_list:
        return 0.0
    total = 0
    for student in student_list:
        total += student.get("attendance", 0)
    return total / len(student_list)

def calculate_average_homework(student_list):
    if not student_list:
        return 0.0
    total = 0
    for student in student_list:
        total += student.get("homework_score", 0)
    return total / len(student_list)

def count_by_city(student_list):
    counts = {}
    for student in student_list:
        city = student.get("city")
        if city:
            if city in counts:
                counts[city] += 1
            else:
                counts[city] = 1
    return counts

def count_by_course(student_list):
    counts = {}
    for student in student_list:
        course = student.get("course")
        if course:
            if course in counts:
                counts[course] += 1
            else:
                counts[course] = 1
    return counts

def get_low_attendance(student_list):
    names = []
    for student in student_list:
        if student.get("attendance", 0) < 70:
            names.append(student.get("name"))
    return names

def get_strong_students(student_list):
    names = []
    for student in student_list:
        if get_performance_status(student) == "Strong":
            names.append(student.get("name"))
    return names

def get_needs_support(student_list):
    names = []
    for student in student_list:
        if get_performance_status(student) == "Needs Support":
            names.append(student.get("name"))
    return names

def generate_report(student_list):
    print("Student Report:")
    if not student_list:
        print("No student data available.")
        return


    print("\nTotal students:", len(student_list))
    print(f"Average attendance: {calculate_average_attendance(student_list):.2f}")
    print(f"Average homework score: {calculate_average_homework(student_list):.2f}")
    
    print("\nStudents by city:")
    cities = count_by_city(student_list)
    for city, count in cities.items():
        print(f"{city}: {count}")
        
    print("\nStudents by course:")
    courses = count_by_course(student_list)
    for course, count in courses.items():
        print(f"{course}: {count}")
        
    print("\nStudents with low attendance:")
    for name in get_low_attendance(student_list):
        print(name)
        
    print("\nStrong students:")
    for name in get_strong_students(student_list):
        print(name)
        
    print("\nStudents that need support:")
    for name in get_needs_support(student_list):
        print(name)

def add_student(student_list, student):
    student_list.append(student)

def sort_students_by_homework(student_list):
    if not student_list:
        return []
    def get_score(s):
        return s.get("homework_score", 0)
    return sorted(student_list, key=get_score, reverse=True)

def get_top_three_students(student_list):
    if not student_list:
        return []
    def get_combined(s):
        return s.get("attendance", 0) + s.get("homework_score", 0)
    sorted_list = sorted(student_list, key=get_combined, reverse=True)
    return sorted_list[:3]

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

generate_report(students)

print("\nStudents sorted by homework score:")
sorted_students = sort_students_by_homework(students)
for s in sorted_students:
    print(f"{s['name']}: {s['homework_score']}")

print("\nTop 3 students by combined score:")
top_three = get_top_three_students(students)
for s in top_three:
    print(f"{s['name']}: {s['attendance'] + s['homework_score']}")

new_student = {
    "student_id": 7,
    "name": "Valon",
    "city": "Prishtina",
    "course": "Python",
    "age": 20,
    "attendance": 95,
    "homework_score": 92
}
add_student(students, new_student)

print("\nUpdated student report after adding Valon:")
generate_report(students)

print("\nReport with empty student list:")
generate_report([])

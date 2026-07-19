import csv
import os
# Reads CSV data from a file
def read_csv_file(file_path):
    records = []
    with open(file_path,"r",newline="",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            records.append(row)
        
        return records
    


# Inspects records by printing counts and column names
def inspect_records(records):
    print("Total raw records:",len(records))
    
    
    print("\nColumns:")
    for column in records[0].keys():
        print(column)
        
        
        
    print("\nFirst 3 records:") 
    for record in records[:3]:
        print(f"{record['student_id']} - {record['name']} - {record['city']} - {record['course']}")




# Checks if the provided value can be converted to an integer
def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    

# Identifies data quality issues in the records
def find_data_quality_issues(records):
    issues = []
    for student in records:
        student_id = student["student_id"]
        
        
        for column in ["name","city","course","age","attendance","homework_score","registered_date"]:
            if student[column].strip() == "":
                issues.append(f"student_id={student_id}, column={column}")
                
        for column in ["age","attendance","homework_score"]:
            value = student[column]
            
            if value != "" and not is_number(value):
                issues.append(f"student_id={student_id},column={column},value={value}")
                
        
        if student["city"] in ["VUSHTRRI","prishtina"]:
            issues.append(f"student_id={student_id}, column=city, value={student['city']}")
            
        if student["course"] in ["Data engineering"]:
            issues.append(f"student_id={student_id}, column=course, value={student['course']}")
            
            
    return issues



# Saves a text report to a file with a given title and lines
def save_text_report(file_path, title, lines):
    with open(file_path,"w",encoding="utf-8") as file:
        file.write(title + "\n\n")
        
        for line in lines:
            file.write(line + "\n")



# Cleans and standardizes a single student record
def clean_student_record(student):
    clean = student.copy()
    
    if clean["city"].strip() == "":
        clean["city"] = "Unknown"
    elif clean["city"].strip() == "VUSHTRRI":
        clean["city"] = "Vushtrri"
    elif clean["city"].strip() == "prishtina":
        clean["city"] = "Prishtina"
        

    if clean["course"].strip() == "":
        clean["course"] = "Not Assigned"
    elif clean["course"].strip() == "Data engineering":
        clean["course"] = "Data Engineering"
        
    if clean["age"].strip() == "":
        clean["age"] = 0
        
    if clean["attendance"].strip() == "":
        clean["attendance"] = 0
    elif not is_number(clean["attendance"]):
        clean["attendance"] = 0
        
    if clean["homework_score"].strip() == "":
        clean["homework_score"] = 0
    elif not is_number(clean["homework_score"]):
        clean["homework_score"] = 0

    if clean["registered_date"].strip() == "":
        clean["registered_date"] = "Unknown Date"
        
    clean["student_id"] = int(clean["student_id"])
    clean["age"] = int(clean["age"])
    clean["attendance"] = int(clean["attendance"])
    clean["homework_score"] = int(clean["homework_score"])
    
    clean["total_score"] = clean["attendance"] + clean["homework_score"]
    
    clean["performance_status"] = get_performance_status(
        clean["attendance"],
        clean["homework_score"]
    )
        
    if (clean["attendance"] < 60 or clean["homework_score"] < 60):
        clean["risk_flag"] = "At Risk"
    else:
        clean["risk_flag"] = "OK"
        
    if clean["attendance"] >= 80:
        clean["attendance_level"] = "High"
    elif clean["attendance"] >= 60:
        clean["attendance_level"] = "Medium"
    else:
        clean["attendance_level"] = "Low"
        
    return clean
        
        
    
# Returns performance status based on attendance and homework scores
def get_performance_status(attendance,homework_score):
        if attendance >= 80 and homework_score >= 80:
            return "Strong"
        elif attendance >= 60 and homework_score >= 60:
            return "Average"
        else:
            return "Needs Support"
            
        
            

# Cleans all student records in the list
def clean_all_records(records):
    cleaned = []

    for student in records:
        cleaned.append(clean_student_record(student))

    return cleaned

# Counts occurrences of values in a specific field
def count_by_field(records, field):

    result = {}

    for record in records:
        value = record[field]

        if value in result:
            result[value] += 1
        else:
            result[value] = 1

    return result

# Calculates the average value of a numeric field
def calculate_average(records, field):

    total = 0

    for record in records:
        total += record[field]

    return round(total / len(records),2)

# Gets names of students matching a performance status
def get_students_by_status(records, status):

    students = []

    for record in records:
        if record["performance_status"] == status:
            students.append(record["name"])

    return students

# Gets top students sorted by their total score
def get_top_students(records):

    sorted_students = sorted(
        records,
        key=lambda x:x["total_score"],
        reverse=True
    )

    return sorted_students[:3]


# Generates a text summary report of the student data analysis
def generate_summary_report(raw, clean, issues):

    report = []

    report.append("Final Student Data Report")
    report.append("------------------------")

    report.append(f"Total raw records: {len(raw)}")
    report.append(f"Total cleaned records: {len(clean)}")
    report.append(f"Total data quality issues found: {len(issues)}")

    report.append(
        f"Average attendance: {calculate_average(clean,'attendance')}"
    )

    report.append(
        f"Average homework score: {calculate_average(clean,'homework_score')}"
    )


    report.append("\nStudents by city:")

    for city,count in count_by_field(clean,"city").items():
        report.append(f"{city}: {count}")


    report.append("\nStudents by course:")

    for course,count in count_by_field(clean,"course").items():
        report.append(f"{course}: {count}")


    report.append("\nStrong students:")

    for name in get_students_by_status(clean,"Strong"):
        report.append(name)


    report.append("\nStudents that need support:")

    for name in get_students_by_status(clean,"Needs Support"):
        report.append(name)


    report.append("\nAt Risk students:")

    for student in clean:

        if student["risk_flag"] == "At Risk":
            report.append(student["name"])


    report.append("\nTop 3 students by total score:")

    for student in get_top_students(clean):

        report.append(
            f"{student['name']}: {student['total_score']}"
        )

    report.append("\nAverage attendance by course:")

    attendance_by_course = calculate_average_by_field(
        clean,
        "course",
        "attendance"
    )

    for course, avg in attendance_by_course.items():
        report.append(f"{course}: {avg}")
        
    report.append("\nAverage homework score by city:")

    homework_by_city = calculate_average_by_field(
        clean,
        "city",
        "homework_score"
    )

    for city, avg in homework_by_city.items():
        report.append(f"{city}: {avg}")

    return "\n".join(report)


# Saves the cleaned records into a CSV file
def save_clean_csv(file_path, records):

    fieldnames = [
        "student_id",
        "name",
        "city",
        "course",
        "age",
        "attendance",
        "homework_score",
        "registered_date",
        "total_score",
        "performance_status",
        "risk_flag",
        "attendance_level"
    ]

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for record in records:
            writer.writerow(record)



# Calculates the average of a value field grouped by a field
def calculate_average_by_field(records, group_field, value_field):
    result = {}

    for record in records:
        key = record[group_field]

        if key not in result:
            result[key] = []

        result[key].append(record[value_field])


    averages = {}

    for key, values in result.items():
        averages[key] = round(sum(values) / len(values), 2)

    return averages



# Finds duplicate student IDs in the list of records
def find_duplicate_ids(records):

    seen = set()
    duplicates = []

    for student in records:
        student_id = student["student_id"]

        if student_id in seen:
            duplicates.append(student_id)

        seen.add(student_id)

    return duplicates



# Runs the main data processing and reporting pipeline
def main():

    os.makedirs("output", exist_ok=True)
    input_file = "data/students_raw.csv"
    try:
        students = read_csv_file(input_file)

    except FileNotFoundError:
        print("Error: students_raw.csv not found")
        return
    duplicates = find_duplicate_ids(students)

    if duplicates:
        print("Duplicate student IDs:", duplicates)

    inspect_records(students)

    issues = find_data_quality_issues(students)
    print("\n")
    for issue in issues:
        print(issue)
        
        
        
    save_text_report(
        "output/data_quality_report.txt",
        "Data Quality Report",
        [f"Total issues found: {len(issues)}"] + issues
    )
    
    clean_students = clean_all_records(students)
    save_clean_csv(
    "output/students_clean.csv",
    clean_students
    )
    
    summary = generate_summary_report(
    students,
    clean_students,
    issues
)


    print("\n")
    print(summary)


    save_text_report(
        "output/summary_report.txt",
        "Final Student Data Report",
        summary.split("\n")
    )



if __name__ == "__main__":
    main()
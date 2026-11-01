# STUDENT PERFORMANCE ANALYTICS TOOLKIT

students = {}
def add_student(student_id, name, marks):
    if student_id in students:
        return "Student ID already exists!"

    if not name.strip():
        return "Student name cannot be empty!"

    if not marks:
        return "Marks list cannot be empty!"

    for mark in marks:
        if not isinstance(mark, (int, float)) or mark < 0 or mark > 100:
            return "Invalid marks! Enter marks between 0 and 100."

    student = {
        "name": name,
        "marks": marks
    }

    students[student_id] = student
    return "Student added successfully!"

def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return calculate_total(marks) / len(marks)

def get_grade(average):
    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Division"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"

def build_report(student):
    marks = student["marks"]

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)

    return {
        "name": student["name"],
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

def get_top_students(records):
    return list(filter(
        lambda item: calculate_average(item[1]["marks"]) >= 75,
        records.items()
    ))

def flexible_average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

def class_summary(**kwargs):
    print("===== CLASS SUMMARY OPTIONS =====\n")

    for key, value in kwargs.items():
        print(key, ":", value)

def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

def scope_demo():
    message = "This is a local variable."
    print("Scope Demonstration:\n")
    print(message)

def display_reports(records):

    print("===== STUDENT PERFORMANCE REPORT =====\n")

    for student_id, student in records.items():

        report = build_report(student)

        print("Student ID:\n", student_id)
        print("Name:", report["name"])
        print("Marks:", report["marks"])
        print("Total:", report["total"])
        print("Average: {:.2f}".format(report["average"]))
        print("Grade:", report["grade"])

def main():

    print("Adding Student Records...")

    print(add_student("S101", "Aman", [78, 65, 88]))
    print(add_student("S102", "Riya", [35, 72, 61]))
    print(add_student("S103", "Rahul", [90, 85, 95]))
    print(add_student("S104", "Priya", [55, 60, 65]))

    display_reports(students)
    top_students = get_top_students(students)

    top_names = list(map(
        lambda item: item[1]["name"],
        top_students
    ))

    print("High Performers (Average >= 75):\n")
    print(top_names)

    all_averages = list(map(
        lambda student: calculate_average(student["marks"]),
        students.values()
    ))

    class_average = sum(all_averages) / len(all_averages)

    print("Class Average: {:.2f}\n".format(class_average))
    print("Flexible Average:\n",
          flexible_average(80, 70, 90, 60))

    class_summary(
        title="Class Report",
        passing_mark=40,
        total_students=len(students)
    )

    print("===== RECURSION TEST =====\n")

    print("Sum from 1 to 5:", recursive_sum(5))
    print("Sum from 1 to 7:", recursive_sum(7))
    print("Sum from 1 to 10:", recursive_sum(10))

    scope_demo()

if __name__ == "__main__":
    main()
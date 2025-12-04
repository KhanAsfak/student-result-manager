# Student Result Manager
# Mini Project (B.Tech CSE) - Python

students = []  # list to store all student records


def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    print("Enter marks out of 100:")
    try:
        m1 = float(input("Subject 1: "))
        m2 = float(input("Subject 2: "))
        m3 = float(input("Subject 3: "))
    except ValueError:
        print("Invalid input! Marks should be numbers.")
        return

    marks = [m1, m2, m3]
    total, percentage, grade = calculate_result(marks)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
    }

    students.append(student)
    print(f"\nStudent {name} added successfully!")


def view_students():
    if not students:
        print("\nNo student records found.")
        return

    print("\n--- All Student Results ---")
    print(
        f"{'Roll':<10}{'Name':<20}{'Sub1':<8}{'Sub2':<8}{'Sub3':<8}{'Total':<8}{'%':<8}{'Grade':<8}"
    )
    print("-" * 80)

    for s in students:
        print(
            f"{s['roll']:<10}{s['name']:<20}"
            f"{s['marks'][0]:<8}{s['marks'][1]:<8}{s['marks'][2]:<8}"
            f"{s['total']:<8}{s['percentage']:<8.2f}{s['grade']:<8}"
        )


def search_student():
    if not students:
        print("\nNo student records found.")
        return

    roll_to_search = input("\nEnter roll number to search: ")

    for s in students:
        if s["roll"] == roll_to_search:
            print("\n--- Student Found ---")
            print(f"Name       : {s['name']}")
            print(f"Roll No.   : {s['roll']}")
            print(f"Marks      : {s['marks']}")
            print(f"Total      : {s['total']}")
            print(f"Percentage : {s['percentage']:.2f}")
            print(f"Grade      : {s['grade']}")
            break
    else:
        print("No student found with that roll number.")


def main_menu():
    while True:
        print("\n====== Student Result Manager ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll No.")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter between 1–4.")


if __name__ == "__main__":
    main_menu()

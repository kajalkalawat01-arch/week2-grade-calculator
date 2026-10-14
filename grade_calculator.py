students = []

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    marks = []

    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i} (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / len(marks)
    grade = get_grade(percentage)

    if percentage >= 90:
        comment = "Excellent work!"
    elif percentage >= 70:
        comment = "Very good! Keep it up."
    elif percentage >= 40:
        comment = "Good effort. Keep improving."
    else:
        comment = "Work harder next time."

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "comment": comment
    }

    students.append(student)
    print("Student result added successfully!")


def display_results():
    if not students:
        print("No student records available.")
        return

    print("\n" + "-" * 78)
    print(f"{'Name':<18}{'Total':<10}{'Percentage':<15}{'Grade':<10}{'Comment'}")
    print("-" * 78)

    for student in students:
        print(
            f"{student['name']:<18}"
            f"{student['total']:<10.1f}"
            f"{student['percentage']:<15.2f}"
            f"{student['grade']:<10}"
            f"{student['comment']}"
        )

    percentages = [s["percentage"] for s in students]

    print("-" * 78)
    print(f"Class average: {sum(percentages) / len(percentages):.2f}%")
    print(f"Highest percentage: {max(percentages):.2f}%")
    print(f"Lowest percentage: {min(percentages):.2f}%")


def search_student():
    name = input("Enter student name to search: ").strip().lower()

    for student in students:
        if student["name"].lower() == name:
            print("\nStudent found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print("Percentage:", f"{student['percentage']:.2f}%")
            print("Grade:", student["grade"])
            print("Comment:", student["comment"])
            return

    print("Student not found.")


def save_results():
    try:
        with open("results_sample.txt", "w") as file:
            for student in students:
                file.write(f"Name: {student['name']}\n")
                file.write(f"Marks: {student['marks']}\n")
                file.write(f"Total: {student['total']}\n")
                file.write(
                    f"Percentage: {student['percentage']:.2f}%\n"
                )
                file.write(f"Grade: {student['grade']}\n")
                file.write(f"Comment: {student['comment']}\n")
                file.write("-" * 30 + "\n")

        print("Results saved to results_sample.txt")

    except OSError as error:
        print("Could not save results:", error)


def main():
    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Add student")
        print("2. Display results and statistics")
        print("3. Search student")
        print("4. Save results")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_results()
        elif choice == "3":
            search_student()
        elif choice == "4":
            save_results()
        elif choice == "5":
            print("Thank you for using Student Grade Calculator!")
            break
        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()

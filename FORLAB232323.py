def get_equivalent_grade(final_grade):
    if 98 <= final_grade <= 100:
        return 4.00
    elif 95 <= final_grade <= 97:
        return 3.75
    elif 92 <= final_grade <= 94:
        return 3.50
    elif 89 <= final_grade <= 91:
        return 3.25
    elif 86 <= final_grade <= 88:
        return 3.00
    elif 83 <= final_grade <= 85:
        return 2.75
    elif 80 <= final_grade <= 82:
        return 2.50
    elif 77 <= final_grade <= 79:
        return 2.25
    elif 74 <= final_grade <= 76:
        return 2.00
    elif 71 <= final_grade <= 73:
        return 1.75
    elif 68 <= final_grade <= 70:
        return 1.50
    elif 64 <= final_grade <= 67:
        return 1.25
    elif 60 <= final_grade <= 63:
        return 1.00
    else:
        return 0.00


def calculate_final_grade(quizzes, research_assignment, project, exam):
    # Applying the formula
    final_grade = (0.30 * quizzes) + (0.10 * research_assignment) + (0.40 * exam) + (0.20 * project)
    return final_grade


def main():
    # Input student data
    student_name = input("Enter student's name: ")

    # Input and validation for grades not exceeding 100
    quizzes = float(input("Enter final quizzes score (0-100): "))
    if quizzes > 100:
        print("Error: The final quizzes score cannot exceed 100.")
        return

    research_assignment = float(input("Enter final research/assignment score (0-100): "))
    if research_assignment > 100:
        print("Error: The final research/assignment score cannot exceed 100.")
        return

    project = float(input("Enter final project score (0-100): "))
    if project > 100:
        print("Error: The final project score cannot exceed 100.")
        return

    exam = float(input("Enter final exam score (0-100): "))
    if exam > 100:
        print("Error: The final exam score cannot exceed 100.")
        return

    # Calculate the final grade
    final_grade = calculate_final_grade(quizzes, research_assignment, project, exam)

    # Cap the final grade to 100 if it exceeds
    if final_grade > 100:
        final_grade = 100

    # Get the equivalent grade
    equivalent_grade = get_equivalent_grade(final_grade)

    # Display the results
    print(f"\nStudent Name: {student_name}")
    print(f"Final Quizzes: {quizzes:.2f}")
    print(f"Final Research/Assignment: {research_assignment:.2f}")
    print(f"Final Project: {project:.2f}")
    print(f"Final Exam: {exam:.2f}")
    print(f"Final Grade: {final_grade:.2f}")
    print(f"Equivalent Grade: {equivalent_grade:.2f}")

if __name__=="__main__":
    main()
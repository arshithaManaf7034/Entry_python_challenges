

"""
Student Grade Management System

This program:
1. Accepts marks for 5 subjects (0–100).
2. Validates numeric input and range.
3. Calculates the average.
4. Determines the grade using defined criteria.
5. Displays the results.
"""


def calculate_average(marks):
    """
    Calculate and return the average of a list of numeric marks.

    :param marks: List of 5 numeric marks (0-100)
    :return: Float average of marks
    """
    return sum(marks) / len(marks)


def get_grade(average):
    """
    Determine grade based on average score.

    :param average: Float average mark
    :return: Grade as string
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_valid_mark(subject_number):
    """
    Prompt user until a valid mark (0-100) is entered.

    :param subject_number: Subject index for display
    :return: Validated float mark
    """
    while True:
        try:
            mark = float(input(f"Enter mark for subject {subject_number}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Mark must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """Main execution function."""
    marks = []

    print("Enter marks for 5 subjects:")
    for i in range(1, 6):
        mark = get_valid_mark(i)
        marks.append(mark)

    average = calculate_average(marks)
    grade = get_grade(average)

    print(f"\nAverage Marks: {average:.1f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
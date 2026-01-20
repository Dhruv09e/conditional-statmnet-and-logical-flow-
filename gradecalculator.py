def calculate_grade(marks):
    """
    Determine grade based on marks.
    Applies business rules using nested conditions.
    """

    # Handle invalid marks
    if marks < 0 or marks > 100:
        return "❌ Invalid marks! Please enter marks between 0 and 100."

    # Business rule: Fail if marks < 40
    if marks < 40:
        return "Grade: F | Status: Fail"

    # Nested conditions for passing grades
    if marks >= 40 and marks < 50:
        return "Grade: D | Status: Pass"
    elif marks >= 50 and marks < 60:
        return "Grade: C | Status: Pass"
    elif marks >= 60 and marks < 75:
        return "Grade: B | Status: Good"
    elif marks >= 75 and marks < 90:
        return "Grade: A | Status: Very Good"
    else:  # marks >= 90
        return "Grade: A+ | Status: Excellent"


def main():
    try:
        marks = float(input("Enter your marks (0–100): "))
        result = calculate_grade(marks)
        print(result)

    except ValueError:
        print("❌ Invalid input! Please enter numeric marks.")


# Run the program
if __name__ == "__main__":
    main()

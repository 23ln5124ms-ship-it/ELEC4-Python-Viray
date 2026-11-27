# Name: Mariel Viray
# Section: IV-BSIT B
# Activity: P1 - Student Grade Calculator
# Date: November 2026

def compute_average(grades):
    return sum(grades) / len(grades)

def get_highest(grades):
    return max(grades)

def get_lowest(grades):
    return min(grades)

def get_status(average):
    if average >= 75:
        return "Passed"
    return "Failed"

def get_highest(grades):
    return max(grades)

def get_lowest(grades):
    return min(grades)

def get_status(average):
    if average >= 75:
        return "Passed"
    return "Failed"

def get_valid_grade():
    while True:
        try:
            grade = float(input("Enter a grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be from 0 to 100.")
        except ValueError:
            print("Please enter a number only.")

grades = []

def main():
    while True:
        print("\n=== Student Grade Calculator - Mariel Viray ===")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            grades.clear()
            count = int(input("How many grades? "))
            for i in range(count):
                grades.append(get_valid_grade())
            print("Grades saved:", grades)
        
        if choice == "3":
            print("Goodbye!")
            break
        else:
            print("Not ready yet.")

main()
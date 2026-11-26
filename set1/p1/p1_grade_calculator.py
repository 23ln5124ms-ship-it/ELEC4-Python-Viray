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


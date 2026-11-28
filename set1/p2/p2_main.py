# Name: Mariel Viray
# Section: IV-BSIT B
# Activity: P2 - Main program
# Date: November 27, 2026

import student_utils
from student_utils import get_status
from datetime import datetime

grades = []
count = int(input("How many grades? "))

for i in range(count):
    while True:
        try:
            grade = float(input("Enter grade " + str(i + 1) + ": "))
            if 0 <= grade <= 100:
                break
            print("Grade must be from 0 to 100.")
        except ValueError:
            print("Please enter a number only.")
    grades.append(grade)

    average = student_utils.compute_average(grades)
highest = student_utils.get_highest(grades)
lowest = student_utils.get_lowest(grades)
status = get_status(average)

print("\n=== Grade Report - Mariel Viray ===")
print("Grades:", grades)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Status:", status)
print("Report :", datetime.now())
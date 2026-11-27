# Name: Mariel Viray
# Section: IV-BSIT B
# Activity: P2 - Main program
# Date: November 2026

import student_utils
from student_utils import get_status
from datetime import datetime

grades = []
count = int(input("How many grades? "))

for i in range(count):
    grade = float(input("Enter grade " + str(i + 1) + ": "))
    grades.append(grade)
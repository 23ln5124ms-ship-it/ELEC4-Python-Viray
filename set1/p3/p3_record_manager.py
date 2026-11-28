# Name: Mariel Viray
# Section: IV-BSIT B
# Activity: P3 - Student Record Manager
# Date: November 2026

students = set()   # a set: no duplicates allowed

def add_student():
    name = input("Enter student name: ").strip().lower()
    if name in students:
        print("That student is already in the list.")
    else:
        students.add(name)
        print("Student added.")

add_student()
add_student()
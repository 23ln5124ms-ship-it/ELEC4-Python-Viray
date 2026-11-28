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

def display_students():
    if len(students) == 0:
        print("No students yet.")
    else:
        print("\n--- Student List ---")
        number = 1
        for name in sorted(students):
            print(number, ".", name.title())
            number += 1
        print("Total:", len(students))

def search_student():
    keyword = input("Search name: ").strip().lower()
    found = False
    for name in sorted(students):
        if keyword in name:
            print("Found:", name.title())
            found = True
    if not found:
        print("No student found.")

def remove_student():
    name = input("Enter name to remove: ").strip().lower()
    if name in students:
        students.remove(name)
        print("Student removed.")
    else:
        print("That student is not in the list.")
        
add_student()
add_student()
display_students()
search_student()
remove_student()
display_students()
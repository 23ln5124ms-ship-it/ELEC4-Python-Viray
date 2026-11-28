# Name: Mariel Viray
# Section: IV-BSIT B
# Activity: P3 - Student Record Manager
# Date: November 2026

from pdb import main


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
        print("\n=== Student List ===")
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
            print("\nFound:", name.title())
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

def main():
    while True:
        print("\n=== Student Record Manager - Mariel Viray ===")
        print("1. Add student")
        print("2. Remove student")
        print("3. Search student")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1 to 5.")

main()

# A list keeps its items in order and can have the same item more than once.
# A set does not allow duplicates and has no fixed order.
# I used a set for students, so the same name can't be added twice.
# I used sorted(students) when displaying, which gives a list in alphabetical order.
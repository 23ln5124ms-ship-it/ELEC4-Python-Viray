# Name: Mariel Viray
# Section: IV-BSIT B
# Activity: P1 - Student Grade Calculator
# Date: November 26, 2026

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
        print("\n=== Student Grade Calculator ===")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            grades.clear()
            count = int(input("How many grades? "))
            for i in range(count):
                grades.append(get_valid_grade())
            print("\n Grades saved:", grades)

        elif choice == "2":
            if len(grades) == 0:
                print("\n No grades yet. Choose option 1 first.")
            else:
                average = compute_average(grades)
                print("Average:", average)
                print("Highest:", get_highest(grades))
                print("Lowest:", get_lowest(grades))
                print("Status:", get_status(average))

        elif choice == "3":
            print("Thank You for using the Student Grade Calculator, Goodbye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2, or 3.")

main()

# Explanation of global and local variables:
# A global variable is a variable I made outside of the functions, so any part of my program can use it.
# In my program, grades = [] is global, that's why main() can add grades and read them later.
# A local variable is made inside a function, so it only works inside that function.
# Like for example, average is local to main(), and grade is local to get_valid_grade().
# If I try to print average outside main(), it gives a NameError because it doesn't exist there.

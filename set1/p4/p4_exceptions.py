# Name: Mariel Viray
# Section: IV-BSIT B
# Activity: P4 - Safe Menu Program
# Date: November 2026

def divide_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a / b
    except ValueError:
        print("Error: please enter numbers only.")
    except ZeroDivisionError:
        print("Error: you cannot divide by zero.")
    else:
        print("Result:", result)
    finally:
        print("Division finished.")

def open_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: that file does not exist.")
    else:
        print("\n--- File contents ---")
        print(content)

divide_numbers()
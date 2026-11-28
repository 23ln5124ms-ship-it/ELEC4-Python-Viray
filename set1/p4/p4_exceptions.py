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

divide_numbers()
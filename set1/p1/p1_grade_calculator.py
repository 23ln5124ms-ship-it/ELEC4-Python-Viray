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

sample = [80, 90, 70]
print(compute_average(sample))
print(get_highest(sample))
print(get_lowest(sample))
print(get_status(compute_average(sample)))
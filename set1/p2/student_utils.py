# Name: Mariel Viray
# Section: IV-BSIT B
# Activity: P2 - student_utils module
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
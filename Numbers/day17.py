# Day 17: Average
# Write a python program that calculates the average for the marks of students in a list 
# Input: [90, 98, 92, 85]
# Output: 91.25
# Average = sum of subjects / occurance of subjects
# Avg = (90 + 98 + 92 + 85) / 4

def average_of_marks_of_students(marks):
    s = 0
    for mark in marks:
        s+=mark
    return f"Average Marks of Student: {(s / len(marks))}"

print(average_of_marks_of_students([90, 98, 92, 85]))
print(average_of_marks_of_students([90, 98, 92, 85, 42, 47]))
print(average_of_marks_of_students([90, 90, 90]))


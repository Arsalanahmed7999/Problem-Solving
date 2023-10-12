# Given the dictionary grades = {"Math": 85, "Science": 92, "History": 78}, remove the "History" key-value pair.

# Use the pop() method to remove the value associated with the "Math" key from the grades dictionary.

grades = {"Math": 85, "Science": 92, "History": 78}
print(grades)

if "History" in grades:
    del grades["History"]

grades['Math'] = None

print(grades)
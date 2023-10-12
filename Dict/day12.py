# You are given a nested dictionary students representing student information. Each student has a name, age, and a list of subjects they're studying. Write a function that takes a student's name as input and returns a formatted string with their information. If the student is not found, return "Student not found."

students = {
    "Alice": {
        "name": "Alice",
        "age": 18,
        "subjects": ["Math", "Science"]
    },
    "Bob": {
        "name": "Bob",
        "age": 17,
        "subjects": ["History", "English"]
    }
}
def func(name):
    for student_name, value in students.items():
        if(name.lower() == student_name.lower()):
            return (f"The name of the student is {value['name']}, age is {value['age']} and subjects are: {value['subjects']}")
    return 'Student not found'

arsalan = func('arsalan')
alice = func('alice')
print(arsalan)
print(alice)
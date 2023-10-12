# Create a nested dictionary named school with student information. Each student should have a name, age, and a list of subjects they're studying.

# Print the subjects of a specific student from the school dictionary.

school = {
    'student_information' : {
        'student1' : {
            'name': 'arsalan',
            'age': 16,
            'subjects': ['Hindi', 'English', 'Maths']
        },
        'student2':{
            'name':'ahmed',
            'age':16,
            'subjects': ['French', 'English', 'Science']
        }
    }
}

student_info = school['student_information']

for key, value in student_info.items():
    print(f"{value['name']}: {value['subjects']}")
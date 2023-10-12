# Create a dictionary named phonebook with at least three entries. Each entry should have a person's name as the key and their phone number as the value. Write a function that takes a name as input and returns the corresponding phone number from the phonebook dictionary. If the name is not found in the dictionary, return "Contact not found."

phonebook = {
    'entry1' : {'name': 'Arsalan', 'phone_number': 9454243221},
    'entry2' : {'name': 'Ahmed', 'phone_number': 9454243221},
    'entry3' : {'name': 'Danish', 'phone_number': 6078607890},
}

def func(username):
    for entry, value in phonebook.items():
        if(value['name'].lower() == username.lower()):
            return(f"Phone Number associated with {value['name']} : {value['phone_number']}")
    return(f'Contact not found of user: {username}')
    
a = func('arsalan')
print(a)
a = func('juhi')
print(a)


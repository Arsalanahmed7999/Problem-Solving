# Use the get() method to retrieve the value associated with the key "salary" from a dictionary employee without raising an error.

# Create a dictionary inventory with items and quantities. Use the update() method to add new items and quantities to the dictionary.


employee = {
    'salary' : 2000
}

print(employee.get('salary', 0))

invertory = {
        "name": "Widget",
        "quantity": 100,
        "price": 10.99
}

employee.update(invertory)

print(employee)
# Day 2: Accessing and Modifying Dictionary Values
# Given the dictionary person = {"name": "John", "age": 30, "city": "New York"}, print the value associated with the key "age".
# Update the value of the "city" key in the person dictionary to "Los Angeles".
# Add a new key-value pair "job": "Engineer" to the person dictionary.

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)
print(person["age"])
person['city'] = 'Los Angeles'
print(person)
person.update({"job":"Engineer"})
print(person)

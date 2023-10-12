# Day 3: Iterating dictionary
# Create a dictionary named fruits with the keys "apple", "banana", and "orange", each associated with their respective quantities.

# Use the keys() method to print all the keys in the fruits dictionary.

# Use the values() method to print all the values in the fruits dictionary.

# Use the items() method to print all key-value pairs in the fruits dictionary.


fruits = {
    'apple': 10,
    'banana':12,
    'orange': 20
}

# print(fruits.keys())
# print(fruits.values())
# print(fruits.items())

for k, v in fruits.items():
    print(f'{k}:{v}')
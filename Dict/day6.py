# Create two dictionaries: dict1 = {"a": 1, "b": 2} and dict2 = {"b": 3, "c": 4}. Merge these dictionaries into a new dictionary.

# Create a new dictionary by combining the keys from dict1 and dict2 with their corresponding values added.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict3 = {**dict1, **dict2}
print(set(dict1) | set(dict2))
print(dict3.get('b', 0))
combined_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

print(dict3)
print(combined_dict)
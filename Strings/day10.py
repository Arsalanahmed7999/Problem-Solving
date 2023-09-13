# Day 10: 
# Check if One String is a Rotation of Another
# Create a Python function that checks if one string is a rotation of another. For example, "waterbottle" is a rotation of "erbottlewat."
# Input: "waterbottle", "erbottlewat"
# Output: True

# "waterbottle" -> "erbottlewat", So this the rotation
# "bottle" -> "totlbe", So this will not be a rotation
# str1 = "waterbottle"
# str2 = "erbottlewat"
# str3 = "waterbottle" + "waterbottle"
# str3 = "waterbottlewaterbottle"
def rotation(str1, str2):
    concatenated_string = str1 + str1 #waterbottlewaterbottle
    return str2 in concatenated_string


print(rotation('waterbottle', 'erbottlewat'))
print(rotation('waterbottle', 'erbbottlewat'))
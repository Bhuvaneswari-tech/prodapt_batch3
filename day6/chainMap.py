#ChainMap is used to combine multiple dictionaries into a single view 
# without actually merging them.

from collections import ChainMap

student = {
    "Name": "Alice",
    "Age": 20
}

course = {
    "Course": "Python",
    "Duration": "3 Months"
}

combined = ChainMap(student, course)

print(combined)
print(combined["Name"])
print(combined["Course"])
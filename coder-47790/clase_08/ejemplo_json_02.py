import json

# Reading the data from a JSON file
with open("students.json", "r") as file:
    loaded_data = json.load(file)

# Printing the loaded data
print(loaded_data)

# Accessing specific parts of the loaded data
for student in loaded_data["students"]:
    print(f"{student['name']} is studying {', '.join(student['subjects'])}.")

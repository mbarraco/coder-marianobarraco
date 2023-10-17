import json

# Sample data in Python dictionary format
data = {
    "students": [
        {
            "name": "Alice",
            "age": 20,
            "subjects": ["Math", "Science"]
        },
        {
            "name": "Bob",
            "age": 22,
            "subjects": ["English", "History"]
        }
    ]
}

# Saving the data to a JSON file
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)  # `indent=4` makes the output more readable

import json

# Open the JSON file


def get_db_json(path):
    with open(path, 'r') as file:
        # Load the contents of the file as a Python object
        data = json.load(file)
        # Use the data variable as needed
        print(data)


path = '../database.json'

get_db_json(path)

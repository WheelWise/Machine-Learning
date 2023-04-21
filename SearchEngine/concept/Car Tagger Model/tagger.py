import json
from car_descriptor import CarDescriptor
# Open the JSON file


def get_db_json(path):
    with open(path, 'r') as file:
        # Load the contents of the file as a Python object
        data = json.load(file)
        # Use the data variable as needed
        return data


# Creates dictionary from json database with only key info
def translate_to_descriptor(db_json):
    new_dict = {}

    for obj in db_json:
        model = obj['model']

        description = obj['description']

        new_dict[model] = description

    return new_dict


def main():
    path = './TestFiles/database.json'
    db_json = get_db_json(path)
    descriptions_dict = translate_to_descriptor(db_json)
    car_descriptor = CarDescriptor(descriptions_dict)


main()

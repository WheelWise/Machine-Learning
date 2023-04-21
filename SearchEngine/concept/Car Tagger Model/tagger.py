import json
from car_descriptor import CarDescriptor
# Open the JSON file


def get_json(path):
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


# helps user to enrich the descriptions
def add_decription(path):
    pool_json = get_json(path)
    descriptions = []

    choices = []
    print("Introuce los indices que describan a tu auto")
    print("-1 para dejar de ingresar datos")
    for key in pool_json:
        temp = []
        print("Categoría: ", key)
        print("Opciones: ")
        for idx, val in enumerate(pool_json[key]):
            print(idx + 1, val)
        counter = 0
        while (counter <= len(pool_json[key])):
            key_input = int(input())

            if key_input == -1:
                break
            else:
                if key_input > 0 and key_input <= len(pool_json[key]):
                    temp.append(key_input)
                    print("Added")
                    print(temp)
                else:
                    print("Fuera del rango, intenta otra vez")
                    continue
            counter += 1
        choices.append(temp)
    for i in choices:
        for j in i:
            print(j)


def main():
    db_path = './TestFiles/database.json'
    db_json = get_json(db_path)
    descriptions_dict = translate_to_descriptor(db_json)
    car_descriptor = CarDescriptor(descriptions_dict)

    # print(car_descriptor.get_description("Camry"))
    pool_path = './TestFiles/pool.json'
    new_descriptions = add_decription(pool_path)
    # car_descriptor.update_car("Camry", ["
    # "])Q


main()

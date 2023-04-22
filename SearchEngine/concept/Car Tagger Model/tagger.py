import json
from car_descriptor import CarDescriptor
# Open the JSON file


class Tagger:
    def __init__(self, db_path, pool_path):
        self.db_path = db_path
        self.pool_path = pool_path
        self.db_json = self.get_json(db_path)
        self.pool_json = self.get_json(pool_path)

    # Open the JSON file
    def get_json(self, path):
        with open(path, 'r') as file:
            # Load the contents of the file as a Python object
            data = json.load(file)
            return data

    # Creates dictionary from json database with only key info
    def translate_to_descriptor(self):
        new_dict = {}

        for obj in self.db_json:
            model = obj['model']
            description = obj['description']
            new_dict[model] = description

        return new_dict

    # Helps user to enrich the descriptions
    def add_description(self):
        descriptions = []

        choices = []
        print("Introduce los índices que describan a tu auto")
        print("-1 para dejar de ingresar datos")
        for key in self.pool_json:
            temp = []
            print("Categoría: ", key)
            print("Opciones: ")
            for values in (self.pool_json[key]):
                for idx, val in enumerate(values):
                    print(idx+1, val)
            counter = 0
            while (counter <= len(self.pool_json[key][0])):
                key_input = int(input())

                if key_input == -1:
                    break
                else:

                    for idx2, (keyy, item) in enumerate(self.pool_json[key][0].items()):
                        if key_input > 0 and key_input <= len(self.pool_json[key][0]):
                            if idx2 == key_input - 1:
                                for i in item:
                                    temp.append(i)

                        else:
                            print("Fuera del rango, intenta otra vez")

                counter += 1
            choices.append(temp)
        desc_list = []

        return choices

    def write_changes(self, new_dict, car_name):
        for dict in self.db_json:
            if dict["model"] == car_name:
                dict["description"] = new_dict[car_name]
                # Open file for writing
        with open(self.db_path, "w") as f:
            # Write data to file
            json.dump(self.db_json, f)

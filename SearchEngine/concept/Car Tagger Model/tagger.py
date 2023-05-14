import json
import pymongo
from car_descriptor import CarDescriptor

from config import DB_HOST, DB_NAME, DB_COLLECTION
# Open the JSON file


class Tagger:
    def __init__(self, db_path, pool_path):
        self.db_path = db_path
        self.pool_path = pool_path
        self.db_json = self.get_json(db_path)
        self.pool_json = self.get_pool_from_db()

    # Open the JSON file
    def get_json(self, path):
        with open(path, 'r') as file:
            # Load the contents of the file as a Python object
            data = json.load(file)
            return data

    def get_pool_from_db(self):
    
        # establecer la conexión con el servidor MongoDB
        client = pymongo.MongoClient(DB_HOST)

        # acceder a una base de datos específica en MongoDB
        db = client[DB_NAME]

        # acceder a una colección específica en la base de datos
        collection = db[DB_COLLECTION]
        cursor = collection.find({})
        result = next(cursor)

        #Remove id from dict
        new_dict = {key: value for key, value in result.items() if key != "_id"}
        
        return new_dict
        

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
        print("Introduce el índice que mejor describa a tu auto")
        print("Si en  una categoria ninguna opción describe tu auto, no hace falta agregarla")
     
        for key in self.pool_json:
            temp = []
            print("Categoría: ", key)
            print("Opciones: ")
            for values in (self.pool_json[key]):
                for idx, val in enumerate(values):
                    print(idx+1, val)
            counter = 0
            while (counter <= len(self.pool_json[key][0])):
                key_input = input()

                if key_input == "":

                    break
                else:
                    key_input = int(key_input)
                    for idx2, (keyy, item) in enumerate(self.pool_json[key][0].items()):
                        if key_input > 0 and key_input <= len(self.pool_json[key][0]):
                            if idx2 == key_input - 1:
                                for i in item:
                                    temp.append(i)
                                
                        else:
                            print("Fuera del rango, intenta otra vez")
                    break
                counter += 1
            choices.append(temp)
        desc_list = []

        #Allow user to describe vehicle
        print("Want to describe vehicle with another words? Y/N")
        key_input = input()
        if key_input == "Y":
            print("Introduce words to describe the vehicle and press enter: Up to 15 words (in spanish and -1 to stop adding words)")
            i = 0
            temp2 = []
            while i < 15:
                key_input = input()
                if key_input == "-1":
                    break
                temp2.append(key_input)
            choices.append(temp2)

        return choices

    def write_changes(self, new_dict, car_name):
        for dict in self.db_json:
            if dict["model"] == car_name:
                dict["description"] = new_dict[car_name]
                # Open file for writing
        with open(self.db_path, "w") as f:
            # Write data to file
            json.dump(self.db_json, f)

        print(car_name + "description" + "updated")

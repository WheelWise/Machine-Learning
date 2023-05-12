"""
Alvaro Garcia
Functions to hide basic methods's complexity"""

from tagger import Tagger
from car_descriptor import CarDescriptor
DB_PATH = './TestFiles/database.json'
POOL_PATH = './TestFiles/pool.json'


def update_car(car_name):

    tagger = Tagger(DB_PATH, POOL_PATH)
    tagger.get_pool_from_db()
    translated_dict = tagger.translate_to_descriptor()
    print(translated_dict)
    description_list = tagger.add_description()
    car_descriptor = CarDescriptor(translated_dict)

    print(car_descriptor.get_description(car_name))
    car_descriptor.update_car(car_name, description_list)
    print(car_descriptor.get_description(car_name))
    new_dict = car_descriptor.get_cars_dict()
    tagger.write_changes(new_dict, car_name)
    


def get_description(car_name):
    tagger = Tagger(DB_PATH, POOL_PATH)
    translated_dict = tagger.translate_to_descriptor()
    car_descriptor = CarDescriptor(translated_dict)
    return car_descriptor.get_description(car_name)

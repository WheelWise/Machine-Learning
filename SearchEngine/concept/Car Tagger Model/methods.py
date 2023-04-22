"""
Alvaro Garcia
Functions to hide basic methods's complexity"""

from tagger import Tagger
from car_descriptor import CarDescriptor


def update_car(car_name):

    db_path = './TestFiles/database.json'
    pool_path = './TestFiles/pool.json'

    tagger = Tagger(db_path, pool_path)
    translated_dict = tagger.translate_to_descriptor()
    print(translated_dict)
    description_list = tagger.add_description()
    car_descriptor = CarDescriptor(translated_dict)

    print(car_descriptor.get_description(car_name))
    car_descriptor.update_car(car_name, description_list)
    print(car_descriptor.get_description(car_name))
    new_dict = car_descriptor.get_cars_dict()
    tagger.write_changes(new_dict, car_name)


update_car("Camry")

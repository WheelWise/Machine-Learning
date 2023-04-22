"""Alvaro Garcia 
    Car's dictionary and methods
"""
from typing import List


class CarDescriptor:
    def __init__(self, descriptions_dict):
        self.cars_dict = descriptions_dict

    def get_description(self, name):
        return self.cars_dict[name]

    def update_car(self, name, new_vals: List):
        if name not in self.cars_dict:
            return
        if len(self.cars_dict[name]) == 0:
            for new_val in new_vals:
                self.cars_dict[name].extend(new_val)
            print("Car was updated")
        else:
            print("Car description complete")

    def remove_car(self, name):
        if name in self.cars_dict:
            self.cars_dict.pop(name)
            print("Car was removed")

    def get_cars_dict(self):
        return self.cars_dict

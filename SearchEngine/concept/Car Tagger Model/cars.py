"""Alvaro Garcia 
    Car's dictionary and methods
"""

from typing import List

cars = {}


def add_car(name):
    if name in cars:
        return
    else:
        cars[name] = []
    print("Car was added")


def get_description(name):
    return cars[name]


def update_car(name, new_vals: List):
    if name not in cars:
        return
    if len(cars[name]) < 3:
        cars[name].extend(new_vals)
    print("Car was updated")


def remove_car(name):
    if name in cars:
        cars.pop(name)
        print("Car was removed")


# Testing methods
    # print(cars)
    # add_car("Honda City MT")
    # add_car("Honda City SPORT CVT")
    # get_description("Honda City MT")
    # update_car("Honda City MT", [
    #            "Familiar, Sedán, Seguro, Cómodo, Eficiente, Automatico "])
    # remove_car("Honda City MT")
    # print(cars)

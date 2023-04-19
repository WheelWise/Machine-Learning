"""
Tool for creating a random Car database in mongodb, 
for testing and development purposes.
By : Sebastian Mora (@Bastian1110)
"""

import sys
import random
from pymongo import MongoClient


makes = [
    "Toyota",
    "Ford",
    "Honda",
    "Chevrolet",
    "Nissan",
    "BMW",
    "Mercedes-Benz",
    "Audi",
    "Tesla",
]

models = {
    "Toyota": ["Camry", "Corolla", "RAV4", "Highlander", "Tacoma"],
    "Ford": ["Mustang", "F-150", "Explorer", "Escape", "Focus"],
    "Honda": ["Civic", "Accord", "CR-V", "Pilot", "Odyssey"],
    "Chevrolet": ["Corvette", "Silverado", "Equinox", "Malibu", "Camaro"],
    "Nissan": ["Altima", "Rogue", "Sentra", "Pathfinder", "Frontier"],
    "BMW": ["X5", "3 Series", "5 Series", "7 Series", "i8"],
    "Mercedes-Benz": ["C-Class", "E-Class", "S-Class", "GLA", "GLC"],
    "Audi": ["A3", "A4", "Q5", "Q7", "R8"],
    "Tesla": ["Model S", "Model 3", "Model X", "Model Y"],
}
colors = ["rojo", "azul", "verde", "negro", "plata", "blanco"]
transmissions = ["manual", "automatico", "estandar"]
years = [2020, 2021, 2022, 2023, 2024]
prices = range(150000, 1000000)


def generateCars(num: int):
    cars = []
    for i in range(num):
        make = random.choice(makes)
        model = random.choice(models[make])
        color = random.choice(colors)
        transmission = random.choice(transmissions)
        year = random.choice(years)
        price = random.choice(prices)
        car = {
            "_id": i + 1,
            "marca": make,
            "modelo": model,
            "precio": price,
            "color": color,
            "transmision": transmission,
            "año": year,
        }

        if make == "Toyota":
            car["asientos"] = random.randint(2, 5)
            car["combustible"] = random.choice(["gasolina", "hibrido", "electrico"])
        elif make == "Ford":
            car["puertas"] = random.randint(2, 4)
            car["motor"] = random.randint(1, 8)
        elif make == "Honda":
            car["años_garantia"] = random.choice([2, 3, 5])
            car["bolsas_de_aire"] = random.randint(1, 8)
        elif make == "Chevrolet":
            car["tamaño_llantas"] = random.choice(["pequeño", "mediano", "grande"])
            car["sonido"] = random.choice(["basico", "premium"])
        elif make == "Nissan":
            car["quemacocos"] = random.choice([True, False])
            car["eficicencia"] = random.randint(10, 30)
        elif make == "BMW":
            car["velocidad"] = random.randint(100, 200)
            car["gps"] = random.choice([True, False])
        elif make == "Mercedes-Benz":
            car["piloto_automatico"] = random.choice([True, False])
            car["caballos_de_fuerza"] = random.randint(100, 400)
        elif make == "Audi":
            car["asistente_de_manejo"] = random.choice([True, False])
            car["tanque"] = random.randint(10, 100)
        elif make == "Tesla":
            car["rango"] = random.randint(100, 500)
            car["piloto_automatico"] = random.choice([True, False])
        cars.append(car)
    return cars


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage : python3 <MONGO_URL> <DB_NAME> <COLLECTION> <N_CARS>")
        quit()
    if len(sys.argv) != 5:
        print("Oops ... You are missing one or more arguments.")
        quit()
    client = MongoClient(sys.argv[1])
    db = client[sys.argv[2]]
    col = db[sys.argv[3]]
    if int(sys.argv[4]) <= 0:
        print("NCARS should be greater than 0")
    col.insert_many(generateCars(int(sys.argv[4])))
    print("Fake Database Created!")

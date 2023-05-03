import random
import csv
import sys

agencies = {
    "Ford": {
        "Modelo": ["Fiesta", "Focus", "Mustang", "Explorer"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": [2017, 2018, 2019, 2020, 2021],
        "Precio": [
            35000,
            40000,
            45000,
            50000,
            55000,
        ],
        "Potencia": [100, 150, 200, 250],
        "Tracción": ["Delantera", "Trasera", "4x4"],
    },
    "Nissan": {
        "Modelo": ["Sentra", "Altima", "Maxima", "Rogue"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": [2017, 2018, 2019, 2020, 2021],
        "Precio": [
            35000,
            40000,
            45000,
            50000,
            55000,
        ],
        "Altura": [150, 160, 170, 180],
        "Peso": [1000, 1200, 1400, 1600],
    },
    "Toyota": {
        "Modelo": ["Corolla", "Camry", "RAV4", "Highlander"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": [2017, 2018, 2019, 2020, 2021],
        "Precio": [
            35000,
            40000,
            45000,
            50000,
            55000,
        ],
        "Tamaño": ["Compacto", "Mediano", "Grande"],
        "Consumo": [20, 25, 30, 35],
        "Motor": ["Gasolina", "Híbrido", "Eléctrico"],
    },
    "Chevrolet": {
        "Modelo": ["Spark", "Cruze", "Malibu", "Tahoe"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": [2017, 2018, 2019, 2020, 2021],
        "Precio": [
            35000,
            40000,
            45000,
            50000,
            55000,
        ],
        "Potencia": [100, 150, 200, 250],
        "Tamaño": ["Compacto", "Mediano", "Grande"],
        "Tracción": ["Delantera", "Trasera", "4x4"],
    },
    "Honda": {
        "Modelo": ["Civic", "Accord", "CR-V", "Pilot"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": [2017, 2018, 2019, 2020, 2021],
        "Precio": [
            35000,
            40000,
            45000,
            50000,
            55000,
        ],
        "Potencia": [120, 140, 160, 180, 200],
        "Tracción": ["Delantera", "Trasera", "4x4"],
    },
    "Mazda": {
        "Modelo": ["Mazda3", "Mazda6", "CX-5", "CX-9"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": [2017, 2018, 2019, 2020, 2021],
        "Precio": [
            35000,
            40000,
            45000,
            50000,
            55000,
        ],
        "Potencia": [120, 140, 160, 180, 200],
        "Tamaño": ["Compacto", "Mediano", "Grande"],
        "Motor": ["Gasolina", "Híbrido"],
    },
    "Volkswagen": {
        "Modelo": ["Jetta", "Passat", "Tiguan", "Atlas"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": [2017, 2018, 2019, 2020, 2021],
        "Precio": [
            35000,
            40000,
            45000,
            50000,
            55000,
        ],
        "Potencia": [100, 120, 140, 160],
        "Tamaño": ["Compacto", "Mediano", "Grande"],
        "Tracción": ["Delantera", "Trasera", "4x4"],
    },
    "BMW": {
        "Modelo": ["Serie 3", "Serie 5", "X3", "X5"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": [2017, 2018, 2019, 2020, 2021],
        "Precio": [
            35000,
            40000,
            45000,
            50000,
            55000,
        ],
        "Potencia": [200, 250, 300, 350],
        "Tracción": ["Trasera", "4x4"],
    },
}


def create_csv(n_cars, age):
    if age not in agencies.keys():
        return f"Error : {age} i not a supported agency"
    agency = agencies[age]
    columns = list(agency.keys())
    with open(
        f"{age.lower()}_catalogo.csv", mode="w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(columns)

        for i in range(n_cars):
            row = []
            for col in columns:
                value = random.choice(agency[col])
                row.append(value)
            writer.writerow(row)
        return f"CSV with {n_cars} created!"


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("For ceating a fake csv based on a real agency")
        print("python3 csv_faker.py <AGENCY> <N_CARS>")
        print("Actual Agancies supported : ")
        for a in agencies.keys():
            print(a)
        quit()
    elif len(sys.argv) == 3:
        print(create_csv(int(sys.argv[2]), sys.argv[1]))
        quit()
    else:
        print("Oops ... You are missing one or more arguments.")
        quit()

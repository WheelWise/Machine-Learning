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
        "Imagen": {
            "Fiesta": "https://images.carexpert.com.au/crop/1200/630/app/uploads/2020/04/2020-ford-fiesta-st-review-4.jpg",
            "Focus": "https://media.whatcar.com/wc-image/2019-05/ford-focus-st-4303e.jpg",
            "Mustang": "https://i2.wp.com/www.keywestford.com/wp-content/uploads/sites/563/2020/07/2020-ford-mustang-ecoboost-coupe-hpp-102-1568989846.jpg",
            "Explorer": "https://www.thedrive.com/content/2021/05/New-2021-Ford-Explorer-Timberline_03.jpg?quality=85&width=1440&quality=70",
        },
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
        "Imagen": {
            "Sentra": "https://www.kbb.com/wp-content/uploads/2020/11/2021-nissan-sentra-grey-front-3qtr.jpg",
            "Altima": "https://9kuyruk.com/upload/9-kuyruk-2023-nissan-altima-ozellikleri.jpeg",
            "Maxima": "https://i2.wp.com/gtautoperformance.com/wp-content/uploads/2016/01/Nissan-Maxima-SR-2016.jpg",
            "Rogue": "https://i0.wp.com/nissanmodel.com/wp-content/uploads/2021/02/2023-Nissan-Rogue-Platinum.jpg?w=1200&ssl=1",
        },
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
        "Imagen": {
            "Corolla": "https://www.ihwanburhan.com/wp-content/uploads/2021/04/2023-Toyota-Corolla-Exterior.png",
            "Camry": "https://www.toyota-2023.com/wp-content/uploads/2021/06/2023-Toyota-Camry-Exterior.png",
            "RAV4": "https://cdn.motor1.com/images/mgl/WOKBO/s1/2021-toyota-rav4-hybrid-front-3-4.jpg",
            "Highlander": "https://www.carglancer.com/wp-content/uploads/2021/01/Toyota-Highlander-2020-e1609941440584.jpg",
        },
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
        "Imagen": {
            "Spark": "https://2023chevrolet.com/wp-content/uploads/2021/04/2022-Chevrolet-Spark-Exterior.jpg",
            "Cruze": "https://www.chevy-2023.com/wp-content/uploads/2021/08/2023-Chevy-Cruze-Exterior.png",
            "Malibu": "https://www.chevy-2023.com/wp-content/uploads/2021/08/2023-Chevrolet-Malibu-Exterior.png",
            "Tahoe": "https://www.chevy-2023.com/wp-content/uploads/2021/09/2023-Chevrolet-Tahoe-RST-Exterior.png",
        },
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
        "Imagen": {
            "Civic": "https://hosteriadeinumeriprimi.com/wp-content/uploads/2021/10/2023-Honda-Civic-Si-specs-price-mpg-pictures.jpg",
            "Accord": "https://www.ihwanburhan.com/wp-content/uploads/2021/03/2023-Honda-Accord-Exterior-1.png",
            "CR-V": "https://www.cnet.com/a/img/resize/b9b708600a8a549feff5ccf073411ee903b9a852/hub/2022/07/12/76f438ac-9244-4cb6-9f73-2e633077f684/2023-honda-cr-v-001.jpg?auto=webp&fit=crop&height=675&width=1200",
            "Pilot": "https://www.kbb.com/wp-content/uploads/2023/01/2023-honda-pilot-elite-driving-front-3qtr.jpg?w=757",
        },
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
        "Imagen": {
            "Mazda3": "https://www.ihwanburhan.com/wp-content/uploads/2021/03/Mazda-3-2023-Exterior.png",
            "Mazda6": "https://www.ihwanburhan.com/wp-content/uploads/2021/04/2023-Mazda-6-Exterior-1-768x448.png",
            "CX-5": "https://d1hv7ee95zft1i.cloudfront.net/custom/car-model-photo/original/2022-mazda-cx-5-62aaedb09e913.jpg",
            "CX-9": "https://mazdaredesign.com/wp-content/uploads/2021/06/2023-Mazda-CX-9-Exterior-2.jpg",
        },
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
            modelo = ""
            for col in columns:
                if col != "Imagen":
                    value = random.choice(agency[col])
                if col == "Modelo":
                    modelo = value
                if col == "Imagen":
                    value = agency["Imagen"][modelo]
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

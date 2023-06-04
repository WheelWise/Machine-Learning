import random
import csv
import sys

agencies = {
    "Ford": {
        "Modelo": ["Fiesta", "Focus", "Mustang", "Explorer", "Escape", "Bronco"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": ["2020", "2021", "2022", "2023"],
        "Precio": [
            "350000",
            "400000",
            "450000",
            "500000",
            "550000",
        ],
        "Potencia": ["100 hp", "150 hp", "200 hp", "250 hp"],
        "Tracción": ["Delantera", "Trasera", "4x4"],
        "Imagen": {
            "Fiesta": "https://images.carexpert.com.au/crop/1200/630/app/uploads/2020/04/2020-ford-fiesta-st-review-4.jpg",
            "Focus": "https://media.whatcar.com/wc-image/2019-05/ford-focus-st-4303e.jpg",
            "Mustang": "https://i2.wp.com/www.keywestford.com/wp-content/uploads/sites/563/2020/07/2020-ford-mustang-ecoboost-coupe-hpp-102-1568989846.jpg",
            "Explorer": "https://www.thedrive.com/content/2021/05/New-2021-Ford-Explorer-Timberline_03.jpg?quality=85&width=1440&quality=70",
            "Escape": "https://acnews.blob.core.windows.net/imgnews/medium/NAZ_fc3d72c64c2d4f238b569f3b84707794.jpg",
            "Bronco": "https://img.remediosdigitales.com/b7d391/2560_3000/840_560.jpeg",
        },
    },
    "Nissan": {
        "Modelo": [
            "Sentra",
            "Altima",
            "Maxima",
            "Rogue",
            "Pathfinder",
            "Kicks",
            "Armada",
        ],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": ["2020", "2021", "2022", "2023"],
        "Precio": [
            "350000",
            "400000",
            "450000",
            "500000",
            "550000",
        ],
        "Altura": ["150 cm.", "160 cm.", "170 cm.", "180 cm."],
        "Peso": ["1000 k.", "1200 k.", "1400 k.", "1600 k."],
        "Imagen": {
            "Sentra": "https://www.kbb.com/wp-content/uploads/2020/11/2021-nissan-sentra-grey-front-3qtr.jpg",
            "Altima": "https://9kuyruk.com/upload/9-kuyruk-2023-nissan-altima-ozellikleri.jpeg",
            "Maxima": "https://i2.wp.com/gtautoperformance.com/wp-content/uploads/2016/01/Nissan-Maxima-SR-2016.jpg",
            "Rogue": "https://i0.wp.com/nissanmodel.com/wp-content/uploads/2021/02/2023-Nissan-Rogue-Platinum.jpg?w=1200&ssl=1",
            "Pathfinder": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiWAXHyltVskUowwlraW6bcyFc6IDzyQrDZw&usqp=CAU",
            "Kicks": "https://www.elcarrocolombiano.com/wp-content/uploads/2021/02/20210211-NISSAN-KICKS-2022-PORTADA.jpg",
            "Armada": "https://geeksroom.com/wp-content/uploads/2022/06/2022-Nissan-Armada-SL-4WD-27.jpg",
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
        "Modelo": ["MX-5", "CX-30", "CX-5", "CX-9", "Mazda3"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": ["2019", "2020", "2021", "2022", "2023"],
        "Precio": [
            "350000",
            "400000",
            "450000",
            "500000",
            "550000",
        ],
        "Potencia": ["100 hp", "155 hp", "220 hp", "150 hp"],
        "Tamaño": ["Compacto", "Mediano", "Grande"],
        "Motor": ["Gasolina", "Híbrido"],
        "Imagen": {
            "MX-5": "https://img.remediosdigitales.com/bdd3f6/mazda-mx-5_club-2016-1600-02/1366_2000.jpg",
            "Mazda3": "https://www.ihwanburhan.com/wp-content/uploads/2021/03/Mazda-3-2023-Exterior.png",
            "CX-5": "https://d1hv7ee95zft1i.cloudfront.net/custom/car-model-photo/original/2022-mazda-cx-5-62aaedb09e913.jpg",
            "CX-9": "https://mazdaredesign.com/wp-content/uploads/2021/06/2023-Mazda-CX-9-Exterior-2.jpg",
            "CX-30": "https://img.remediosdigitales.com/84ddfe/mazda-cx-30-2022-precio-mexico-/1366_2000.jpeg",
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
        "Modelo": ["Serie 3", "Serie 5", "X3", "X5", "Serie 8", "Serie 4", "Z4"],
        "Color": ["Rojo", "Azul", "Negro", "Blanco", "Gris"],
        "Año": ["2020", "2021", "2022", "2023"],
        "Precio": [
            "350000",
            "400000",
            "450000",
            "500000",
            "550000",
        ],
        "Motor": ["Gasolina", "Híbrido"],
        "Potencia": ["200 hp", "250 hp", "300 hp", "350 hp"],
        "Tracción": ["Trasera", "4x4"],
        "Imagen": {
            "Serie 3": "https://www.autobild.es/sites/autobild.es/public/dc/fotos/BMW_Serie_3_Berlina_03_0.jpg",
            "Serie 5": "https://img.automexico.com/2020/08/13/0M2xJlFh/p90389016-highres-the-new-bmw-530e-xdr-9856-1-d818.jpg",
            "X3": "https://www.elcarrocolombiano.com/wp-content/uploads/2021/06/Diseno-sin-titulo-17-9.jpg",
            "X5": "https://hips.hearstapps.com/hmg-prod/images/2020-bmw-x5-m-140-1582911136.jpg?crop=0.784xw:0.882xh;0.0721xw,0.118xh&resize=640:*",
            "Serie 8": "https://img.automexico.com/2021/07/23/rkwP8Fam/bmw-serie-8-2-0952.jpg",
            "Serie 4": "https://noticias.coches.com/wp-content/uploads/2021/06/BMW-Serie-4-Gran-Coupe-2022-4.jpg",
            "Z4": "https://cdn.motor1.com/images/mgl/VzX8RL/s3/bmw-z4-2023.jpg",
        },
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

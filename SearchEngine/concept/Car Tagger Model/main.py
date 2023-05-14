"""
Alvaro Garcia
Car tagger main menu"""
import methods


def main():
    car_name = "Camry"
    
    #Obtener coches que todavía no tienen una descripción
    methods.cars_missing_description()

    #Actualizar la descripción de un carro sin descripción
    methods.update_car(car_name)

    #Obtener la description de un carro
    description = methods.get_description(car_name)
    print(description)

    


main()

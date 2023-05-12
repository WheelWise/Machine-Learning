"""
Alvaro Garcia
Car tagger main menu"""
import methods


def main():
    car_name = "Camry"
    # description = methods.get_description(car_name)
    # print(description)
    methods.update_car(car_name)
    description = methods.get_description(car_name)
    print(description)


main()

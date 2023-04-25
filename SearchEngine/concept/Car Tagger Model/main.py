"""
Alvaro Garcia
Car tagger main menu"""
import methods


def main():
    while True:
        x = input("New query ? (Y/n): ")
        if x.lower() == "n":
            break
        string = input("Carro : ")
        methods.update_car(string)
        description = methods.get_description(string)


main()

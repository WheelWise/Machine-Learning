import json

# load database of known car models and tags
with open("tags.json") as f:
    car_models = json.load(f)


def tag_car_model(car_model):
    # check if car model is in database
    if car_model in car_models:
        return car_models[car_model]
    else:
        # prompt user for tags
        print("Can you describe the car model in a few words?")
        tags = input("Tags (separated by commas): ").split(",")
        # store new car model and tags in database
        car_models[car_model] = [tag.strip() for tag in tags]
        with open("tags.json", "w", encoding="utf-8") as f:
            json.dump(car_models, f, ensure_ascii=False, indent=4)
        return tags


while True:
    answer = input("New Query ? (Y/n) ")
    if answer.lower() == "n":
        break
    test = input("Car : ")
    print(tag_car_model(test))

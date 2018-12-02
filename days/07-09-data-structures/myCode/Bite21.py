import re #Import regex for case insenstive search

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


# Testing things
# for models in cars.values():
#     for model in models:
#         print(model)

def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    carString = ""
    jeepList = cars['Jeep']
    for jeep in jeepList:
        carString+=jeep+", "
    return carString[:-2]

# print(get_all_jeeps())

# Testing
# for models in cars.values():
#     print(models)

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    firstModels=[]
    for models in cars.values():
        firstModels.append(models[0])
    return firstModels

# print(get_first_model_each_manufacturer())

def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matchList = []
    for models in cars.values():
        for model in models:
            if re.search(grep,model,re.IGNORECASE):
                matchList.append(model)
    return matchList

print(get_all_matching_models())


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    pass

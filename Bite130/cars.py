import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    cars = {}
    for car in data:
        if car['year'] == year:
            if not car['automaker'] in cars:
                cars[car['automaker']] = 1
            else:
                cars[car['automaker']] += 1
    return max(cars, key=cars.get)        


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return set(car["model"] for car in data if car['automaker'] == automaker and car['year'] == year)


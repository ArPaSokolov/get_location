import json
import random
from datetime import timedelta, datetime


# генерация времени остановок
def generate_time():
    # начало остановки
    start_month = random.randint(1, 5)
    start_day = random.randint(1, 28)
    start_hour = random.randint(0, 23)
    start_minute = random.randint(0, 59)
    start_second = random.randint(0, 59)

    start = datetime(2024, start_month, start_day, start_hour, start_minute, start_second)

    # длительность остановки
    duration_days = random.randint(0, 3)
    duration_hours = random.randint(0, 1)
    duration_minutes = random.randint(0, 59)
    duration_seconds = random.randint(0, 59)

    # конец остановки = начало + длительность
    end = start + timedelta(days=duration_days, hours=duration_hours, minutes=duration_minutes, seconds=duration_seconds)

    # формат времени
    start_str = start.isoformat() + "Z"
    end_str = end.isoformat() + "Z"

    return start_str, end_str


# генерация остановок
def generate_stops(addresses):
    stops = []
    for _ in range(10):
        start, end = generate_time()
        stop = {
            "address": random.choice(addresses),
            "eventId": random.randint(1, 100),
            "eventName": "string",
            "start": start,
            "end": end,
            "duration": 0
        }
        stops.append(stop)
    return stops


def generate_data(vehicleIds, addresses):
    data = []
    # данные
    for vehicleId in vehicleIds:
        vehicle = {
            "vehicleId": vehicleId,
            "vehicleName": "Контейнер",
            "receiverEmail": "demid.working@gmail.com",
            "receiverPhone": "89110234562",

            "stops": generate_stops(addresses)
        }
        data.append(vehicle)

    return data


# список адресов
addresses = ["Россия, Ленинградская область, Санкт-Петербург, ул. Ленина, 10",
             "Россия, Ленинградская область, Санкт-Петербург, ул. Советская, 20",
             "Россия, Ленинградская область, Санкт-Петербург, ул. Желябова, 8",
             "Россия, Калининградская область, Калининград, ул. Пролетарская, 10",
             "Россия, Калининградская область, Балтийск, улица Красной Армии, 11",
             "Швеция, Стокгольмская область, Стокгольм, ул. Гамла Стана, 10",
             "Финляндия, Уусимаа, Хельсинки, ул. Эспланади, 1",
             "Литва, Клайпедская область, Клайпеда, ул. Таурагес, 5",
             "Латвия, Рига, ул. Андрейостас, 15",
             "Эстония, Харьюмаа, Таллинн, ул. Вабадус, 7",
             "Германия, Мекленбург-Передняя Померания, Росток, ул. Ленштрассе, 10",
             "Польша, Поморское воеводство, Гданьск, ул. Тарнавска, 2",
             "Литва, Клайпедская область, Паланга, ул. Базницию, 3"]

# список id
vehicleIds = ["84350",
              "12774",
              "38618",
              "42131"]

# запись
with open("data.json", "w") as file:
    data = generate_data(vehicleIds, addresses)
    json.dump(data, file)

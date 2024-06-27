import json
import datetime


with open("data.json", "r") as file:
    data = json.load(file)  # читаем полученные данные

    receiver = data.get('receiverEmail', '-')  # почта получателя

    vehicleId = data.get('vehicleId', '-')  # id груза
    vehicleName = data.get('vehicleName', '-')  # название груза
    stops = data.get('stops', '-')  # остановки для данного груза

    if stops != '-':  # если остановки были
        stop = stops[-1]  # берем последнюю

        address = stop.get('address', '-')  # адрес

        start_time = stop.get('start', '-')  # время начала остановки
        start_time = datetime.datetime.fromisoformat(start_time[:-1])

        end_time = stop.get('end', '-')  # время окончания остановки
        end_time = datetime.datetime.fromisoformat(end_time[:-1])
        print(f"Последнее местоположение груза {vehicleName} (#{vehicleId}):\
              \nПункт: {address}\
              \nПрибыл: {start_time.strftime('%H:%M %d-%m-%Y')}\
              \nПокинул: {end_time.strftime('%H:%M %d-%m-%Y')}\
              \nПолучатель: {receiver}")
    else:
        print(f"Местоположение груза {vehicleId} неизвестно.")

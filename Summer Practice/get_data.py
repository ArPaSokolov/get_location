import json
import datetime


def get_data(desired_client):
    answers_id = []
    answers_full = {}
    with open("data.json", "r") as file:
        data = json.load(file)  # читаем полученные данные
        for item in data:
            if item.get("receiverEmail") == desired_client:
                receiver = item.get('receiverEmail', '-')  # почта получателя

                vehicleId = item.get('vehicleId', '-')  # id груза
                vehicleName = item.get('vehicleName', '-')  # название груза
                stops = item.get('stops', '-')  # остановки для данного груза

                if stops != '-':  # если остановки были
                    stop = stops[-1]  # берем последнюю

                    address = stop.get('address', '-')  # адрес

                    start_time = stop.get('start', '-')  # время начала остановки
                    start_time = datetime.datetime.fromisoformat(start_time[:-1])

                    end_time = stop.get('end', '-')  # время окончания остановки
                    end_time = datetime.datetime.fromisoformat(end_time[:-1])
                    answer_id = (vehicleId)
                    answer_full = (f"Последнее местоположение груза {vehicleName} (#{vehicleId}):\
                                \nПункт: {address}\
                                \nПрибыл: {start_time.strftime('%H:%M %d-%m-%Y')}\
                                \nПокинул: {end_time.strftime('%H:%M %d-%m-%Y')}")
                else:
                    answer_full = (f"Местоположение груза {vehicleId} неизвестно.")
                answers_id.append(answer_id)
                answers_full[vehicleId] = answer_full

    if not answers_id:
        return "Пользователя не существует", ""
    if answers_id and answers_full:
        return answers_id, answers_full

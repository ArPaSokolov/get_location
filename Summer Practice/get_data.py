import json
import datetime


def get_data():
    answers = []
    desired_client = "demid.working@gmail.com"  # почта, по которой получаем данные
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
                    answer = (f"Последнее местоположение груза {vehicleName} (#{vehicleId}):\
                                \nПункт: {address}\
                                \nПрибыл: {start_time.strftime('%H:%M %d-%m-%Y')}\
                                \nПокинул: {end_time.strftime('%H:%M %d-%m-%Y')}\
                                \nПолучатель: {receiver}")
                else:
                    print(f"Местоположение груза {vehicleId} неизвестно.")

            answers.append(answer)

        return answers


print(*get_data())

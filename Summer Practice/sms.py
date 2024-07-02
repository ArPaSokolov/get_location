import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sms(body, receiver_email):
    # Параметры подключения к почтовому серверу
    smtp_server = 'smtp.mail.ru' # тип почты
    smtp_port = 587 # порт
    username = 'gvozdenko.demid@mail.ru'  # адрес электронной почты
    password = 'fwEbj0igMBmDviirUGsf'  # пароль

    # Создание сообщения
    subject = 'Местоположение Вашего груза' # заголовок
    sender_email = username # адрес отправителя

    message = MIMEMultipart()
    message['From'] = sender_email # установка адреса отправителя
    message['To'] = receiver_email # установка адреса получателя
    message['Subject'] = subject # установка заголовка
    message.attach(MIMEText(body, 'plain')) # установка основной части сообщения

    server = smtplib.SMTP(smtp_server, smtp_port) # подключение к серверу
    server.starttls() # шифрование
    server.login(username, password) # залогиниться

    # Отправка сообщения
    try:
        server.sendmail(sender_email, receiver_email, message.as_string()) # отправка сообщения
        return 'Сообщение успешно отправлено'
    except smtplib.SMTPConnectError as e:
        return 'Ошибка подключения к почтовому серверу:', str(e)
    except Exception as e:
        return 'Ошибка при отправке сообщения:', str(e)
    finally:
        server.quit() # отправка порта
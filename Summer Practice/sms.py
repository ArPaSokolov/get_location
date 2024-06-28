import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Параметры подключения к почтовому серверу
smtp_server = 'smtp.mail.ru' # тип почты
smtp_port = 587 # порт
username = 'gvozdenko.demid@mail.ru'  # адрес электронной почты
password = 'fwEbj0igMBmDviirUGsf'  # пароль

# Создание сообщения
subject = 'Проверка работы через Python' # заголовок
body = 'Привет, это тело письма!' # основная часть сообщения
sender_email = username # адрес отправителя
receiver_email = 'demid.working@gmail.com'  # адрес получателя

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
    print('Сообщение успешно отправлено')
except smtplib.SMTPConnectError as e:
    print('Ошибка подключения к почтовому серверу:', str(e))
except Exception as e:
    print('Ошибка при отправке сообщения:', str(e))
finally:
    server.quit() # отправка порта
import telebot

bot = telebot.TeleBot('7405204357:AAFb858hrwmJkzj8TgM7JlOFZwy4gCxRwuc')

from telebot import types
from get_data import get_data
from sms import sms


@bot.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"Здравствуйте, <b>{message.from_user.first_name}</b>!\n Хотите найти груз?"  # Первое сообщение
    markup = types.InlineKeyboardMarkup()  # Создание кнопки как переменной
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # Текст кнопки и значение, которое принимает
    markup.add(button_yes)  # Добавление кнопки
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)  # Вывод всего что выше


@bot.message_handler(commands=['help'])  # Команда хелп
def helpBot(message):
    help_mess = f"Вот команды, которые я умею:\n/start\nТакже в мои возможности входит получение последних данных о передвижении груза.\nЧтобы получить местоположение груза напишите Ваш адрес электронной почты"
    bot.send_message(message.chat.id, help_mess)


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        global count
        if function_call.data == "yes":  # Если нажали кнопку "Да"
            second_mess = "Напишите адрес своей электронной почты"  # Второе сообщение, после "Да"
            bot.send_message(function_call.message.chat.id, second_mess)  # Показать второе сообщение
            bot.answer_callback_query(function_call.id)  # Обработка команды закончена
        elif function_call.data == "mail":
            id, full = get_data(mail)
            mail_mess = sms(full[id[count]], mail)
            bot.send_message(function_call.message.chat.id, mail_mess)
            bot.answer_callback_query(function_call.id)
        else:
            count = 0
            id, full = get_data(mail)
            while count < len(id):
                if function_call.data == id[count]:
                    markup = types.InlineKeyboardMarkup()
                    button_mail = types.InlineKeyboardButton(text='Отправить на почту', callback_data='mail')
                    markup.add(button_mail)
                    bot.send_message(function_call.message.chat.id, full[id[count]], reply_markup=markup)
                    break
                count += 1


@bot.message_handler(content_types=['text'])
def get_answer(message):
    global mail
    if "@" in message.text:
        mail = message.text
        id, full = get_data(mail)
        if type(id) != str:
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            for item in id:
                button = types.InlineKeyboardButton(text=item, callback_data=item)
                keyboard.add(button)
            bot.send_message(message.chat.id, 'Выберите ID груза, который Вам нужен:', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, 'Груза привязанного к данной электронной почте нет, напишите другую почту')
    else:
        third_mess = 'Введите название своей электронной почты'
        bot.send_message(message.chat.id, third_mess)


bot.infinity_polling()
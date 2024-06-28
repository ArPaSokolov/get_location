import telebot

bot = telebot.TeleBot('7405204357:AAFb858hrwmJkzj8TgM7JlOFZwy4gCxRwuc')

from telebot import types


@bot.message_handler(commands=['start'])  # Начало работы
def startBot(message):
    first_mess = f"Здравствуйте, <b>{message.from_user.first_name}</b>!\n Хотите найти груз?"  # Первое сообщение
    markup = types.InlineKeyboardMarkup()  # Создание кнопки как переменной
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # Текст кнопки и значение, которое принимает
    markup.add(button_yes)  # Добавление кнопки
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)  # Вывод всего что выше


@bot.message_handler(commands=['help'])  # Команда хелп
def helpBot(message):
    help_mess = f"Вот команды, которые я умею:\n/start (Начало работы)\n/stop (Конец работы)\nТакже в мои возможности входит получение последних данных о передвижении груза.\nЧтобы получить местоположение груза напишите его ID"
    bot.send_message(message.chat.id, help_mess)


@bot.message_handler(commands=['stop'])  # Команда стоп
def stopBot(message):
    stop_mess = f"Уже закончили?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='end')
    button_no = types.InlineKeyboardButton(text='Нет', callback_data='yes')
    markup.add(button_yes, button_no)
    bot.send_message(message.chat.id, stop_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":  # Если нажали кнопку "Да"
            second_mess = "Напиши ID груза, который хотите найти"  # Второе сообщение, после "Да"
            bot.send_message(function_call.message.chat.id, second_mess)  # Показать второе сообщение
            bot.answer_callback_query(function_call.id)  # Обработка команды закончена
        elif function_call.data == "end":
            end_mess = "До свидания!"
            bot.send_message(function_call.message.chat.id, end_mess)
            bot.answer_callback_query(function_call.id)


bot.infinity_polling()
# Установка необходимых библиотек
import telebot
from settings import TG_TOKEN
# Подключение API ключа
bot = telebot.TeleBot(TG_TOKEN)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Что будем делать? Путешествовать или изучать историю?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
# Покупка билетов
    if message.text =="Путешествовать":
        bot.reply_to(message, "Самолёт или Поезд?")
    elif message.text == "Самолёт":
        bot.reply_to(message,"Неземное путешествие по земным ценам: https://www.aeroflot.ru/ru-ru")
    elif message.text == "Поезд":
        bot.reply_to(message, "Лучшие железнодорожные путешествия только здесь: https://www.rzd.ru/")
# Бронирование отеля
    elif message.text == "Хочу забронировать отель":
        bot.reply_to(message, "Лучшие отели только здесь: https://ostrovok.ru/")
    elif message.text == "Изучать историю":
        bot.reply_to(message, "Историю какого города желаете изучить?")
# Список городов
    elif message.text == "Москва":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0")
    elif message.text == "Санкт-Петербург":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3")
    elif message.text == "Нижний Новгород":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4")
    elif message.text == "Сергиев Посад":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%80%D0%B3%D0%B8%D0%B5%D0%B2_%D0%9F%D0%BE%D1%81%D0%B0%D0%B4")
    elif message.text == "Переславль":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D1%81%D0%BB%D0%B0%D0%B2%D0%BB%D1%8C-%D0%97%D0%B0%D0%BB%D0%B5%D1%81%D1%81%D0%BA%D0%B8%D0%B9")
    elif message.text == "Ростов":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2")
    elif message.text == "Кострома":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%BC%D0%B0")
    elif message.text == "Иваново":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE")
    elif message.text == "Суздаль":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%A1%D1%83%D0%B7%D0%B4%D0%B0%D0%BB%D1%8C")
    elif message.text == "Владимир":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_(%D0%B3%D0%BE%D1%80%D0%BE%D0%B4,_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F")
        bot.infinity_polling()

bot.infinity_polling()
import telebot
from settings import TG_TOKEN
bot = telebot.TeleBot(TG_TOKEN)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Что будем делать? Путешествовать или изучать историю?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text =="Путешествовать":
        bot.reply_to(message, "Самолёт или Поезд?")
    elif message.text == "Самолёт":
        bot.reply_to(message,"Неземное путешествие по земным ценам: https://www.aeroflot.ru/ru-ru")
    elif message.text == "Поезд":
        bot.reply_to(message, "Лучшие железнодорожные путешествия только здесь:https://www.rzd.ru/")
    elif message.text == "Хочу забронировать отель":
        bot.reply_to(message, "Лучшие отели только здесь: https://ostrovok.ru/")
    elif message.text == "Изучать историю":
        bot.reply_to(message, "Историю какого города желаете изучить?")
    elif message.text == "Москва":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0")
    elif message.text == "Санкт-Петербург":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3")
    elif message.text == "Нижний Новгород":
        bot.reply_to(message, "https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4")





bot.infinity_polling()

#Библиотека/bible

import telebot

#Token

TOKEN = 'Токен телеграм бота/Token Telegram Bot'

bot = telebot.TeleBot(TOKEN)

#Messages

@bot.message_handler(content_types=['text'])

def text(message):

	if message.text.lower() == "Ваше сообщение/Your message":		bot.send_message(message.chat.id, 'Сообщение которое ответит бот/The message that the bot will reply to')

#So that the bot does not stop

bot.polling(none_stop = True, interval = 0)

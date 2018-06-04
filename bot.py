# -*- coding: utf-8 -*-


import telebot

from telebot import apihelper

apihelper.proxy = {'https':'socks5://:@37.59.8.29:38335'} 



TOKEN = '478813577:AAGaLfIGJG38ApCNbTOsichGxj8vEzyKL4g' 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])

def repeat_all_messages(message): 
	bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
	bot.polling(none_stop=True)




#   1. pip install pysocks
#   2. pip install request[socks]
#   3. pip unistall requests
#   4. pip install requests==2.10.0
#
from config import TOKEN
import telebot
from random import choice


#print(config.TOKEN)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Здраствуйте, я Бот о многом.
Пока что я нахожусь в стадии раработки, но вы иожете поддержать моего автора, подписавшись на ютуб канал Dethtorkk. Спасибо >;)\
""")

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

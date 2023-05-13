import telebot
import json
from telebot import apihelper

def get_config():
    with open("config.json", "r") as f:
        return json.loads(f.read())


config = get_config()
token = config["token"]

telebot.apihelper.proxy = {
    "https": "socks5://ksfzxrkb:onzpkvfn45py@45.94.47.66:8110"
}
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['ping'])
def handle_ping_message(message):
    bot.send_message(message.chat.id,'Bot is active.')


@bot.message_handler(commands=['start'])
def handle_start_message(message):
    bot.send_message(message.chat.id,'welcome message')


















print(bot.get_me())
bot.infinity_polling()

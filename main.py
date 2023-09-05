import os
import telebot
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hello_vagrant'])

def hello(message):
    bot.reply_to(message, "Hi, I'am Server Monitoring Bot")

@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.chat.id, "The server is alive")
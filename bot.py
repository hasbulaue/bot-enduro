import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

API_TOKEN = "8166774313:AAEsNleY3OGFMK4EFMB0aJKbFdwtmvvgKg4"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(
        "Магазин",
        web_app=WebAppInfo(url="https://hasbulaue.github.io/Enduro-Sochi-/")
    ))
    bot.send_message(
        message.chat.id,
        "Добро пожаловать!",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def echo_msg(message):
    bot.send_message(message.chat.id, f"Вы написали: {message.text}")

if __name__ == "__main__":
    bot.infinity_polling()
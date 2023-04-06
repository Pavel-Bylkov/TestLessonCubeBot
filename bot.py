import telebot
from telebot import types
from secret import TOKEN

bot = telebot.TeleBot(TOKEN)

user = {}

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(m):
    bot.reply_to(m, "Привет!")
    user[m.chat.id] = {"id": m.from_user.id,
            "first_name": m.from_user.first_name,
            "last_name": m.from_user.last_name,
            "username": m.from_user.username}
    text = f"{m.from_user.first_name}! Твой бот готов поработать."
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    list_b = [types.KeyboardButton(btn) for btn in ("#photo", "#audio")]
    markup.add(*list_b)
    bot.send_message(chat_id=m.chat.id, text=text, reply_markup=markup)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def handler_message(message):
    if message.text == "#photo":
        url = "https://pytba.readthedocs.io/en/latest/_static/logo.png"
        bot.send_photo(chat_id=message.chat.id, photo=url)
        photo = open("Павлин.png", "rb")
        bot.send_photo(chat_id=message.chat.id, photo=photo)
        photo.close()
    elif message.text == "#audio":
        audio = open("1918.mp3", "rb")
        bot.send_audio(chat_id=message.chat.id, audio=audio)
        audio.close()
    else:
        bot.reply_to(message, message.text)

bot.infinity_polling()
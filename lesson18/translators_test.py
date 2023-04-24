import telebot
import translators as ts
from Tests.translater import remove_keyword

API_KEY = 'add_api'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start_message(message: telebot.types.Message):
    log(message)
    to_send = 'Этот бот поможет вам перевести текст c английского на русский. '\
              'Введите фразу на английском'
    bot.send_message(chat_id=message.chat.id, text=to_send, reply_markup=remove_keyword)


@bot.message_handler(content_types=['text'])
def on_message_recieved(message: telebot.types.Message):
    log(message)
    q_text = message.text
    to_send_en = ts.translate_text(q_text, from_language='en', to_language='ru')
    bot.send_message(chat_id=message.chat.id, text=to_send_en)


def log(message: telebot.types.Message):
    print(f'from user {message.from_user.username} {message.text}')


bot.polling(none_stop=True)
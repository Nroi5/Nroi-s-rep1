# pip install pyTelegramBotAPI
import telebot # в терминале -> pip install pyTelegramBotAPI
import random


token = '5609613153:AAEGalfvUDlUmbhg8nz1wjsTaKYBKow3jIA'#свой токет от botfather
bot = telebot.TeleBot(token)#

# декоратор - функция обертка (улучшение функции без изменения кода)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message): #словарь с данными о сообщениями
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """

    #создаю клавиатуру
    keyboard= telebot.types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True, one_time_keyboard=False)

    btn1 = telebot.types.KeyboardButton('/poem')

    keyboard.add(btn1)

    bot.send_message(message.chat.id,  welcome_text, reply_markup=keyboard)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)

    keyboard= telebot.types.InlineKeyboardMarkup(row_width=2)
    btn_url= telebot.types.InlineKeyboardButton('Перейти', url='https://ru.pinterest.com/pin/22518066878597198/sent/?invite_code=94b3d590e5744b5f87f482c55a1ab397&sender=642748315477400914&sfo=1')
    keyboard.add(btn_url)

    bot.send_message(message.chat.id,'dada', reply_markup=keyboard)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1,10))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=['sticker'])
def send_sticker(message):

    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHR7NjxVAEa8uWSUgJbp_x6zjwDLmk2QACeyYAAjfqKUrynLJ4ah7GMS0E")

# @bot.message_handler(commands=["game"])
# def game_choose(message):



@bot.message_handler(content_types=["text"])
def text_user(message):
    if message.text == "Поэма":
        send_poem(message)
    elif message.text == "Стикер":
        send_sticker(message)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю")




bot.polling()

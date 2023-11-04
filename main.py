import telebot
from telebot import types

bot = telebot.TeleBot('6445313495:AAESDAgHITm0kcMUyHNjvd2qLphaFSi2hSI')



# Словарь для отслеживания состояний пользователя
user_states = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('EN music')
    item2 = types.KeyboardButton('KG music')
    item3 = types.KeyboardButton('RU music')
    item4 = types.KeyboardButton('KZ music')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'ПРИВЕТСТВУЕМ ВАС НА НАШ БОТ: "Musics_1_tele_bot" 🫶🏻❤️)', reply_markup=markup)
    bot.send_message(message.chat.id, 'Выбирайте в каком языке вы хотели бы послушать музыку🥳🎼🎧)', reply_markup=markup)



    user_states[message.chat.id] = "start"




    @bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "start" and message.text == 'EN music')
    def choose_movie_genre(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('№1: https://t.me/enlishmusic')
        item2 = types.KeyboardButton('№2: https://t.me/Inglizcha_qoshiqlar_va_kliplar')
        item3 = types.KeyboardButton('№3: https://t.me/englishmusicwithtexts')
        item4 = types.KeyboardButton('№4: https://t.me/Trend_English_Musics')
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, 'Выбирайте каналы:', reply_markup=markup)
        # user_states[message.chat.id] = "en musics"



    @bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "start" and message.text == 'KG music')
    def choose_movie_genre(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('№1: https://t.me/musica_2001')
        item2 = types.KeyboardButton('№2: https://t.me/trekiamiro')
        item3 = types.KeyboardButton('№3: https://t.me/kyrgyzmusicborosh')
        item4 = types.KeyboardButton('№4: https://t.me/kyrgyz_music')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Выбирайте каналы:', reply_markup=markup)



    @bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "start" and message.text == 'RU music')
    def choose_movie_genre(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('№1: https://t.me/russian_music_group')
        item2 = types.KeyboardButton('№2: https://t.me/russian_movies_musics')
        item3 = types.KeyboardButton('№3: https://t.me/russiantalks')
        item4 = types.KeyboardButton('№4: https://t.me/+mQcnVYpbVEwzOThi')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Выбирайте каналы:', reply_markup=markup)




    @bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "start" and message.text == 'KZ music')
    def choose_movie_genre(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('№1: https://t.me/kz_fm')
        item2 = types.KeyboardButton('№2: https://t.me/muzz_kz5')
        item3 = types.KeyboardButton('№3: https://t.me/kazakmusic36')
        item4 = types.KeyboardButton('№4: https://t.me/kznewsongs')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Выбирайте каналы:', reply_markup=markup)





bot.polling()



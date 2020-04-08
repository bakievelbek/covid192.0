import telebot
import random
import http.client

from telebot import types

bot = telebot.TeleBot('874581229:AAEMadVLv4alttxTI8P8By0Tyme8J1gOLjc')
conn = http.client.HTTPSConnection("coronavirus-monitor.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "89bc88b7c4msh2ca111ae12e23b5p162dd0jsn6c43fd7ca82b"
    }


@bot.message_handler(commands=['start'])
def welcome(message):
     sti = open('img/sticker.webp', 'rb')
     bot.send_sticker(message.chat.id, sti)
     
     #keyboard
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     item1 = types.KeyboardButton("Uzbekistan🇺🇿")
     item2 = types.KeyboardButton("Italy🇮🇹")
     item3 = types.KeyboardButton("Spain🇪🇸")
     item4 = types.KeyboardButton("France🇫🇷")
     item5 = types.KeyboardButton("Germany🇩🇪")
     item6 = types.KeyboardButton("UK🇬🇧")
     item7 = types.KeyboardButton("Iran🇮🇷")
     item8 = types.KeyboardButton("China🇨🇳")
     item9 = types.KeyboardButton("Russia🇷🇺")
     item10 = types.KeyboardButton("Turkey🇹🇷")
     item11 = types.KeyboardButton("USA🇺🇸")
     item12 = types.KeyboardButton("World🌎")
     
     markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
     
     bot.send_message(message.chat.id, "Welcome, {0.first_name}!\nЯ - <em>{1.first_name}</em>, введите страну:".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)
     print("<")
     print(message.chat.username) 
     print(message.chat.first_name)  
     print(message.chat.last_name)
     print(">")
     
     
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == "World🌎":
        conn.request("GET", "/coronavirus/worldstat.php", headers=headers)
        k = conn.getresponse().read().decode("utf-8")
        a = k.replace('\"',' ')
        c = a.replace(',','')
        res = [int(i) for i in c.split() if i.isdigit()]
        final_message = f"<u>Данные по миру:</u>\nВсего случаев : {res[0]}\nНовых случаев : +{res[3]}\nАктивных случаев : {res[0] - res[1] - res[2]}\nНовых смертей : +{res[4]}\nВсего смертей : {res[1]}\nВыздоровело : {res[2]}"
        message.text = ''
        bot.send_message(message.chat.id, final_message, parse_mode='html')
        
    conn.request("GET", "/coronavirus/latest_stat_by_country.php?country="+ message.text[:-2], headers=headers)
    k = conn.getresponse().read().decode("utf-8")
    a = k.replace('\"',' ')
    c = a.replace(',','')
    res = [int(i) for i in c.split() if i.isdigit()]
    if len(res) == 9:
        final_message = f"<u>Данные по стране:</u>\nВсего случаев : {res[1]}\nНовых случаев : +{res[2]}\nАктивных случаев : {res[3]}\nНовых смертей : +{res[5]}\nВсего смертей : {res[4]}\nВыздоровело : {res[6]}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif len(res) == 8:
            final_message = f"<u>Данные по стране:</u>\nВсего случаев : {res[1]}\nНовых случаев : +{res[2]}\nАктивных случаев : {res[3]}\nВсего смертей : {res[4]}\nВыздоровело : {res[5]}"
            bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif len(res) == 7:
                final_message = f"<u>Данные по стране:</u>\nВсего случаев : {res[1]}\nАктивных случаев : {res[2]}\nВсего смертей : {res[3]}\nВыздоровело : {res[4]}"
                bot.send_message(message.chat.id, final_message, parse_mode='html')
        
bot.polling(none_stop=True)
        
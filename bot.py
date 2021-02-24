import telebot
from telebot import types


bot = telebot.TeleBot('1615883583:AAHnp6cw_3Gw_Bd0ur_wwqOGSzhQFWLaV1o')

@bot.message_handler(commands = ['start'])
def list(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    bt1 = types.KeyboardButton('Вода')
    bt2 = types.KeyboardButton('Постройки')
    bt3 = types.KeyboardButton('Работа')
    bt4 = types.KeyboardButton('Отмена')
    markup.add(bt1, bt2, bt3, bt4)
    msg = bot.send_message(message.chat.id, 'Выберите кнопку',
        reply_markup=markup)
    bot.register_next_step_handler(msg, switch)
def switch(message):
    try:
        chat_id = message.chat.id

        if message.text == 'Вода':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            bt1 = types.KeyboardButton('/start - чтобы вернуться в начало')
            markup.add(bt1)
            msg = bot.send_message(chat_id, f'Введите координаты нарушения',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, water_pr)

        elif message.text == 'Постройки':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            bt1 = types.KeyboardButton('/start - чтобы вернуться в начало')
            markup.add(bt1)
            msg = bot.send_message(chat_id, f'Введите координаты нарушения',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, build_pr)

        elif message.text == 'Робота':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            bt1 = types.KeyboardButton('/start - чтобы вернуться в начало')
            markup.add(bt1)
            msg = bot.send_message(chat_id, f'Опишите проблему',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, work_pr)
        else:
            markup = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(chat_id, 'Отмена!', reply_markup=markup)
    except Exception as e:
        print(str(e))

def water_pr(message):
    try:
        chat_id = message.chat.id
        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text != 'Отмена':
            file = open("water.txt", "a", encoding='utf-8')
            file.write(str(message.text) + '\n')
        else:
            bot.send_message(chat_id, 'Отмена!', reply_markup=markup)
    except Exception as e:
        print(str(e))
def build_pr(message):
    try:
        chat_id = message.chat.id
        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text != 'Отмена':
            file = open("build.txt", "a", encoding='utf-8')
            file.write(str(message.text) + '\n')
        else:
            bot.send_message(chat_id, 'Отмена!', reply_markup=markup)
    except Exception as e:
        print(str(e))
def work_pr(message):
    try:
        chat_id = message.chat.id
        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text != 'Отмена':
            file = open("work.txt", "a", encoding='utf-8')
            file.write(str(message.text) + '\n')
        else:
            bot.send_message(chat_id, 'Отмена!', reply_markup=markup)
    except Exception as e:
        print(str(e))
bot.polling(none_stop=True, interval=0)




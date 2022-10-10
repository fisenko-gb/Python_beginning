import datetime
import requests
import telebot
from telebot import types
from telebot.types import Message
from config import TOKEN, ADMIN_ID
import json_worker as jw

bot = telebot.TeleBot(token=TOKEN)
menu_level = 0
last_name, first_name, patronymic, telef, comment = '', '', '', '', ''


def menu(n_menu: int):
    global menu_level
    if n_menu == 1: # Главное меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1.Добавить")
        btn2 = types.KeyboardButton("2.Поиск")
        btn3 = types.KeyboardButton("3.Показать все")
        btn4 = types.KeyboardButton("4.Экспорт")
        btn5 = types.KeyboardButton("5.Импорт")
        btn6 = types.KeyboardButton("Выход")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        menu_level = 1
        return markup
    elif n_menu == 2: # Редактирование записи
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("2.1 Фамилия")
        btn2 = types.KeyboardButton("2.2 Имя")
        btn3 = types.KeyboardButton("2.3 Отчество")
        btn4 = types.KeyboardButton("2.4 Телефон")
        btn5 = types.KeyboardButton("2.5 Комментарий")
        btn6 = types.KeyboardButton("2.6 Сохранить")
        btn7 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        menu_level = 2
        return markup
    elif n_menu == 3: # Поиск
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("3.1 Найти")
        btn2 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2)
        menu_level = 3
        return markup
    elif n_menu == 4: # Назад
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад")
        markup.add(btn1)
        menu_level = 4
        return markup
    elif n_menu == 5: # Сохранить
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сохранить")
        btn2 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2)
        menu_level = 5
        return markup


@bot.message_handler(commands=['start'])
def start(mesage: Message):
    markup = menu(1)
    bot.send_message(mesage.chat.id,
                     text="Добро пожаловать в телефонную книгу.\nВыберите кнопку с желаемым действием...".format(
                         mesage.from_user), reply_markup=markup)


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    pass

# Добавление нового элемента
def save_lastname(mesage: Message):
    global last_name
    last_name = mesage.text
    bot.send_message(mesage.chat.id, text="Введите имя")
    bot.register_next_step_handler(mesage, save_firstname)

def save_firstname(mesage: Message):
    global first_name
    first_name = mesage.text
    bot.send_message(mesage.chat.id, text="Введите отчество")
    bot.register_next_step_handler(mesage, save_patronymic)

def save_patronymic(mesage: Message):
    global patronymic
    patronymic = mesage.text
    bot.send_message(mesage.chat.id, text="Введите телефон")
    bot.register_next_step_handler(mesage, save_telefon)

def save_telefon(mesage: Message):
    global telef
    telef = mesage.text
    bot.send_message(mesage.chat.id, text="Введите комментарий")
    bot.register_next_step_handler(mesage, save_comment)

def save_comment(mesage: Message):
    global comment
    comment = mesage.text
    markup = menu(5)
    bot.send_message(mesage.chat.id, text="Вы закончили ввод данных, хотите их сохранить?", reply_markup=markup)
# Конец Добавление нового элемента


@bot.message_handler(content_types=['text'])
def func(message):
    global last_name, first_name, patronymic, telef, comment

    if (message.text == "1.Добавить"):
        markup = menu(4)
        bot.send_message(message.chat.id, text="Введите фамилию", reply_markup=markup)
        bot.register_next_step_handler(message, save_lastname)
    elif (message.text == '2.1 Фамилия'):
        bot.send_message(message.chat.id, text="Введите фамилию")

    elif (message.text == "2.2 Имя"):
        pass
    elif (message.text == "2.3 Отчество"):
        pass
    elif (message.text == "2.4 Телефон"):
        pass
    elif (message.text == "2.5 Комментарий"):
        pass
    elif (message.text == "2.6 Сохранить"):
        pass
    elif (message.text == "2.Поиск"):
        markup = menu(3)
        bot.send_message(message.chat.id, text="Введите строку поиска", reply_markup=markup)

    elif message.text == "3.Показать все":
        database = jw.read_base()
        database_srt = jw.show_tuple_string(database)
        markup = menu(4)
        bot.send_message(message.chat.id, text=database_srt, reply_markup=markup)
    elif (message.text == "Назад"):
        markup = menu(1)
        if menu_level == 2 or menu_level == 3:
            markup = menu(1)
        bot.send_message(message.chat.id, text="Выберите нужный пункт меню", reply_markup=markup)
    elif (message.text == "Сохранить"):
        if first_name != '' or last_name != '' or patronymic != '':
            jw.add_base(last_name, first_name, patronymic, telef, comment)
            markup = menu(1)
            bot.send_message(message.chat.id, text="Данные успешно сохранены\nВыберите нужный пункт меню",
                             reply_markup=markup)
        else:
            markup = menu(1)
            bot.send_message(message.chat.id, text="Вы не заполнили ни одного поля имени, данные не сохранены\nВыберите нужный пункт меню",
                             reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

while True:
    try:
        bot.polling()
    except Exception as err:
        '''
        Добавляем прямой запрос в телеграмм для отправки сообщения админу
        '''
        requests.post(f'https://api.telegram.org/bot{TOKEN}'
                      f'/sendMessage?chat_id={ADMIN_ID}&'
                      f'text={datetime.datetime.now().__format__("%d/%m/%y, %H:%M:%S")} ___ ERROR ___ {err.__class__} ___ {err}')
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
str_find = []
str_choice = {}


def menu(n_menu: int):
    global menu_level
    if n_menu == 1: # Главное меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Добавить")
        btn2 = types.KeyboardButton("Поиск")
        btn3 = types.KeyboardButton("Показать все")
        btn4 = types.KeyboardButton("Экспорт")
        btn5 = types.KeyboardButton("Импорт")
        btn6 = types.KeyboardButton("Выход")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        menu_level = 1
        return markup
    elif n_menu == 2: # Редактирование записи
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Фамилия")
        btn2 = types.KeyboardButton("Имя")
        btn3 = types.KeyboardButton("Отчество")
        btn4 = types.KeyboardButton("Телефон")
        btn5 = types.KeyboardButton("Комментарий")
        btn6 = types.KeyboardButton("Сохранить.")
        btn7 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        menu_level = 2
        return markup
    elif n_menu == 3: # Поиск
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад")
        markup.add(btn1)
        menu_level = 3
        return markup
    elif n_menu == 4: # Назад
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад")
        markup.add(btn1)
        menu_level = 4
        return markup
    elif n_menu == 5: # Сохранить отменить
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сохранить")
        btn2 = types.KeyboardButton("Отменить")
        markup.add(btn1, btn2)
        menu_level = 5
        return markup
    elif n_menu == 6: # Отменить
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отменить")
        markup.add(btn1)
        menu_level = 6
        return markup
    elif n_menu == 7: # Выбрать
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Выбрать")
        btn2 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2)
        menu_level = 7
        return markup
    elif n_menu == 8: # Выбрать
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Редактировать")
        btn2 = types.KeyboardButton("Удалить")
        btn3 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3)
        menu_level = 8
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
    if mesage.text == 'Отменить':
        func(mesage)
        return
    last_name = mesage.text
    bot.send_message(mesage.chat.id, text="Введите имя")
    bot.register_next_step_handler(mesage, save_firstname)

def save_firstname(mesage: Message):
    global first_name
    if mesage.text == 'Отменить':
        func(mesage)
        return
    first_name = mesage.text
    bot.send_message(mesage.chat.id, text="Введите отчество")
    bot.register_next_step_handler(mesage, save_patronymic)

def save_patronymic(mesage: Message):
    global patronymic
    if mesage.text == 'Отменить':
        func(mesage)
        return
    patronymic = mesage.text
    bot.send_message(mesage.chat.id, text="Введите телефон")
    bot.register_next_step_handler(mesage, save_telefon)

def save_telefon(mesage: Message):
    global telef
    if mesage.text == 'Отменить':
        func(mesage)
        return
    telef = mesage.text
    bot.send_message(mesage.chat.id, text="Введите комментарий")
    bot.register_next_step_handler(mesage, save_comment)

def save_comment(mesage: Message):
    global comment
    if mesage.text == 'Отменить':
        func(mesage)
        return
    comment = mesage.text
    markup = menu(5)
    bot.send_message(mesage.chat.id, text="Вы закончили ввод данных, хотите их сохранить?", reply_markup=markup)
# Конец Добавление нового элемента

# Редактирование элемента
def correct_lastname(mesage: Message):
    global str_choice
    if mesage.text == 'Отменить':
        func(mesage)
        return
    str_choice['last_name'] = mesage.text
    markup = menu(2)
    bot.send_message(mesage.chat.id, text="Что именно будем редактировать?", reply_markup=markup)

def correct_firstname(mesage: Message):
    global str_choice
    if mesage.text == 'Отменить':
        func(mesage)
        return
    str_choice['first_name'] = mesage.text
    markup = menu(2)
    bot.send_message(mesage.chat.id, text="Что именно будем редактировать?", reply_markup=markup)

def correct_patronymic(mesage: Message):
    global str_choice
    if mesage.text == 'Отменить':
        func(mesage)
        return
    str_choice['patronymic'] = mesage.text
    markup = menu(2)
    bot.send_message(mesage.chat.id, text="Что именно будем редактировать?", reply_markup=markup)

def correct_telefon(mesage: Message):
    global str_choice
    if mesage.text == 'Отменить':
        func(mesage)
        return
    str_choice['telefon'] = mesage.text
    markup = menu(2)
    bot.send_message(mesage.chat.id, text="Что именно будем редактировать?", reply_markup=markup)

def correct_comment(mesage: Message):
    global str_choice
    if mesage.text == 'Отменить':
        func(mesage)
        return
    str_choice['comment'] = mesage.text
    markup = menu(2)
    bot.send_message(mesage.chat.id, text="Что именно будем редактировать?", reply_markup=markup)
# Конец редактирования



def find_base(mesage: Message):
    global str_find
    if mesage.text == 'Назад':
        func(mesage)
        return
    str_find = jw.search_base(mesage.text)

    if len(str_find) > 0:
        markup = menu(3)
        rez = jw.show_tuple_string(str_find)
        rez += '\n\n Введите порядковый номер записи для дальнейших действий с ней'
        bot.send_message(mesage.chat.id, text=rez, reply_markup=markup)
        bot.register_next_step_handler(mesage, choice_str)
    else:
        markup = menu(3)
        bot.send_message(mesage.chat.id, text="Ничего не найдено, по-пробуйте еще раз", reply_markup=markup)
        bot.register_next_step_handler(mesage, find_base)

def choice_str(mesage: Message):
    global str_find, str_choice
    if len(str_find) > 0:
        for i in str_find:
            if str(i['id']) == mesage.text:
                str_choice = i
                markup = menu(8)
                bot.send_message(mesage.chat.id, text="Что Вы хотите сделать с выбранной строкой?", reply_markup=markup)
                return
    str_find = []
    str_choice = {}
    markup = menu(1)
    bot.send_message(mesage.chat.id, text="Введенный порядковый номер не найден\nВыберите нужный пункт меню", reply_markup=markup)





@bot.message_handler(content_types=['text'])
def func(message):
    global last_name, first_name, patronymic, telef, comment

    if (message.text == "Добавить"):
        markup = menu(6)
        bot.send_message(message.chat.id, text="Введите фамилию", reply_markup=markup)
        bot.register_next_step_handler(message, save_lastname)
    elif (message.text == 'Фамилия'):
        bot.send_message(message.chat.id, text="Введите фамилию")
        bot.register_next_step_handler(message, correct_lastname)
    elif (message.text == "Имя"):
        bot.send_message(message.chat.id, text="Введите Имя")
        bot.register_next_step_handler(message, correct_firstname)
    elif (message.text == "Отчество"):
        bot.send_message(message.chat.id, text="Введите Отчество")
        bot.register_next_step_handler(message, correct_patronymic)
    elif (message.text == "Телефон"):
        bot.send_message(message.chat.id, text="Введите Телефон")
        bot.register_next_step_handler(message, correct_telefon)
    elif (message.text == "Комментарий"):
        bot.send_message(message.chat.id, text="Введите Комментарий")
        bot.register_next_step_handler(message, correct_comment())
    elif (message.text == "Сохранить."):
        jw.update_str_base(str_choice)
        markup = menu(1)
        bot.send_message(message.chat.id, text="Выбранная успешно отредактирована\nВыберете нужный пункт меню",
                         reply_markup=markup)
    elif (message.text == "Поиск"):
        markup = menu(3)
        bot.send_message(message.chat.id, text="Введите строку поиска", reply_markup=markup)
        bot.register_next_step_handler(message, find_base)
    elif (message.text == "Удалить"):
        jw.delete_str_base(str_choice['id'])
        markup = menu(1)
        bot.send_message(message.chat.id, text="Выбранная строка удалена\nВыберете нужный пункт меню", reply_markup=markup)
    elif (message.text == "Редактировать"):
        markup = menu(2)
        bot.send_message(message.chat.id, text="Что именно будем редактировать?", reply_markup=markup)
    elif message.text == "Показать все":
        database = jw.read_base()
        database_srt = jw.show_tuple_string(database)
        markup = menu(4)
        bot.send_message(message.chat.id, text=database_srt, reply_markup=markup)
    elif message.text == "Назад" or message.text == "Отменить":
        markup = menu(1)
        if menu_level == 2 or menu_level == 3:
            markup = menu(1)
        bot.send_message(message.chat.id, text="Выберите нужный пункт меню", reply_markup=markup)
    elif message.text == "Экспорт":
        jw.export_csv()
        markup = menu(1)
        bot.send_message(message.chat.id, text='Операция экспорта завершена\nВыберете нужный пункт меню', reply_markup=markup)
    elif message.text == "Импорт":
        jw.import_csv()
        markup = menu(1)
        bot.send_message(message.chat.id, text='Операция импорта завершена\nВыберете нужный пункт меню',
                         reply_markup=markup)

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
        markup = menu(1)
        bot.send_message(message.chat.id, text="Выберите нужный пункт меню", reply_markup=markup)

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
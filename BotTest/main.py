import datetime
import requests
import telebot
from telebot.types import Message
from config import TOKEN, ADMIN_ID
import json

bot_client = telebot.TeleBot(token=TOKEN)


@bot_client.message_handler(commands=['start'])
def start(mesage: Message):
    user = mesage.from_user

    with open('users.json', 'r', encoding='UTF-8') as f_o:
        data_from_json = json.load(f_o)

    if str(user.id) not in data_from_json:
        user_id = user.id
        user_name = user.username
        last_name = user.last_name
        first_name = user.first_name

        data_from_json[user_id] = {'user_name': user_name, 'last_name': last_name, 'first_name': first_name}

        with open('users.json', 'w', encoding='UTF-8') as f_o:
            json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)

        bot_client.reply_to(message=mesage, text=str(f'Вы зарегистрированы {user_name}.\n'
                                                     f'Ваш id: {user_id}'))
    else:
        bot_client.reply_to(message=mesage, text=str(f'{user.username}, Вы уже зарегистрировались ранее'))

@bot_client.message_handler(commands=['help'])
def help(mesage: Message):
    bot_client.reply_to(message=mesage, text='Поддерживаемые команды:\n'
                                             '/start\n'
                                             '/say_standup_speech\n'
                                             '/help')


def handle_standup_speech(mesage: Message):
    '''
    функция используется для колбека
    '''
    bot_client.reply_to(mesage, 'Спасибо большое. Желаю успехов!')
    print(mesage)


@bot_client.message_handler(commands=['say_standup_speech'])
def say_standup_speech(mesage: Message):
    bot_client.reply_to(mesage, text='Чем занимался вчера?\n'
                                      'Что будешь делать сегодня?\n'
                                      'Что будешь делать завтра?')
    bot_client.register_next_step_handler(mesage, handle_standup_speech)


while True:
    try:
        bot_client.polling()
    except Exception as err:
        '''
        Добавляем прямой запрос в телеграмм для отправки сообщения админу
        '''
        requests.post(f'https://api.telegram.org/bot{TOKEN}'
                      f'/sendMessage?chat_id={ADMIN_ID}&'
                      f'text={datetime.datetime.now().__format__("%d/%m/%y, %H:%M:%S")} ___ ERROR ___ {err.__class__} ___ {err}')

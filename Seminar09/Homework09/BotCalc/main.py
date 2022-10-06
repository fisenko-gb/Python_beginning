import telebot, datetime, time, math, re
from telebot import types
from config import TOKEN
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y/%m/%d, %H:%M:%S", encoding='UTF-8')

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TOKEN)

TIME_SLEEP = 5  # Таймаут переподключения

MES_START = """Приветствую Вас!!!\n/help - список поддерживаемых операций"""
MES_HELP = """Введите выражение и отправьте мне, можно использовать:

***Операторы***:
    + - сложение;
    - - вычитание;
    \* - умножение;
    / - деление;
    \*\* - возведение в степнь.

***Функции***:
    sin(x) - синус x;
    cos(x) - косинус x;   
    tg(x) - тангенс x;
    fact(x) - факториал x;
    sqrt(x) - квадратный корень х;
    sqr(x) - х в квадрате.
    lg(х) - десятичный логарифм х;
    ln(x) - натуральный логарифм x;
    log(b, х) - логарифм х по основанию b;
    log2(x) - логарифм х по основанию 2;
    
***Перевод систем исчеслений***:
    0bx - перевести двоичное число х в десятичное;
    0ox - перевести восьмиричное число х в десятичное;
    0xx - перевести шестнадцатиричное число х в десятичное;"""

def fact(float_):
    return math.factorial(float_)

def cos(float_):
    return math.cos(float_)

def sin(float_):
    return math.sin(float_)

def tg(float_):
    return math.tan(float_)

def tan(float_):
    return math.tan(float_)

def ln(float_):
    return math.log(float_)

def log(base, float_):
    return math.log(float_, base)

def lg(float_):
    return math.log10(float_)

def log2(float_):
    return math.log2(float_)

def exp(float_):
    return math.exp(float_)

@bot.message_handler(commands=['start', 'help'])
def send_start(update):
    logging.info('%s (%s): %s' % (update.chat.first_name, update.chat.username, update.text))
    msg = None

    if update.text.lower() == '/start':
        msg = bot.send_message(update.chat.id, MES_START, parse_mode='markdown')

    elif update.text.lower() == '/help':
        msg = bot.send_message(update.chat.id, MES_HELP, parse_mode='markdown')


@bot.message_handler(func=lambda update: True)
def answer_to_user(update):
    logging.info('%s (%s): %s' % (update.chat.first_name, update.chat.username, update.text))
    msg = None
    user_message = update.text.lower()
    user_message = (user_message.lstrip()).rstrip()

    if user_message == 'привет':
        msg = bot.send_message(update.chat.id, '*Привет, %s*' % (update.chat.first_name), parse_mode='markdown')

    elif user_message == 'помощь':
        msg = bot.send_message(update.chat.id, MES_HELP, parse_mode='markdown')

    else:
        try:
            answer = str(eval(user_message.replace(' ', '')))
            msg = bot.send_message(update.chat.id, user_message.replace(' ', '') + ' = ' + answer)
            logging.info(f'Результат выражения {answer}')
        except:
            msg = bot.send_message(update.chat.id, 'Введенные данные не корректны, повторите снова')

    if (msg):
        logging.info('Ответ: %s' % msg.text)

if (__name__ == '__main__'):
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            logging.ERROR('Ошибка подключения. Попытка подключения через %s сек.' % TIME_SLEEP)
            time.sleep(TIME_SLEEP)

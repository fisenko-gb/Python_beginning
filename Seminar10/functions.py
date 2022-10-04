import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    ConversationHandler,
)
# Включим ведение журнала
#import check
import json

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def read_bd(name_path_file):
    try:
        with open(name_path_file, "r", encoding='utf-8') as read_file:
            data = read_file.read()
            if not data:
                del data
                return {}

            data_from_file = json.loads(data)
            return data_from_file
    except FileNotFoundError:
        with open("data.json", "w") as read_file:
            return {}


def parsing_bd():
    bd_full = read_bd('our_bd.json')
    rez = ''
    for stroka in bd_full:
        for key, val in stroka.items():
            rez += str(val) + '\n'

        rez += '\n'

    return rez


# print(parsing_bd())

# читаем БД


def show_contact(update, context):
    update.message.reply_text(parsing_bd())


    # Определяем константы этапов разговора
GENDER, PHOTO, LOCATION, BIO = range(4)

RAZIO = 'Рациональные'
COMPLEX = 'Комплексные'
WAY, ENTER_FLOAT, ENTER_COMPLEX, OPERATION = range(4)

# функция обратного вызова точки входа в разговор


def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [[RAZIO, COMPLEX]]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Меня зовут профессор Калькулятор. Выберите, с какими числами вы будете работать?',
        reply_markup=markup_key,)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список
    # обработчиков, определенных в виде значения ключа `GENDER`
    return WAY


def choose_path_to_work(update, _):
    way = update.message.text
    if way == RAZIO:
        update.message.reply_text('Вы выбрали режим рациональных чисел')
        update.message.reply_text('Введите первое число: ')
        return ENTER_FLOAT
    elif way == COMPLEX:
        update.message.reply_text('Вы выбрали режим комплексных чисел чисел')
        update.message.reply_text('Введите первое число вида ...+ ...j : ')
        return ENTER_COMPLEX
    update.message.reply_text('Вы выбрали несуществующий режим')


def get_float_number(update, context):
    num = update.message.text
    if not check.check_realnumber(update, num):
        return ENTER_FLOAT
    update.message.reply_text(f'Вы ввели число {num}')
    which = 'num1' if 'num1' not in context.user_data else 'num2'
    context.user_data[which] = int(num)
    if 'num2' not in context.user_data:
        update.message.reply_text('Теперь введи второе число')
        return ENTER_FLOAT
    update.message.reply_text('Теперь введите операцию: +, -, * или /')
    return OPERATION


def get_operation(update, context):
    oper = update.message.text
    if not check.check_operation(update, oper):
        return OPERATION
    context.user_data['oper'] = oper
    num1 = context.user_data.get('num1')
    num2 = context.user_data.get('num2')
    expression = f'{num1} {oper} {num2}'
    update.message.reply_text(f'{expression} = {eval(expression)}')
    context.user_data.clear()
    return ConversationHandler.END


# Обрабатываем пол пользователя
def gender(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info("Пол %s: %s", user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Хорошо. Пришли мне свою фотографию, чтоб я знал как ты '
        'выглядишь, или отправь /skip, если стесняешься.',
        reply_markup=ReplyKeyboardRemove(),
    )
    # переходим к этапу `PHOTO`
    return PHOTO

# Обрабатываем фотографию пользователя


def photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем фото
    photo_file = update.message.photo[-1].get_file()
    # скачиваем фото
    photo_file.download(f'{user.first_name}_photo.jpg')
    # Пишем в журнал сведения о фото
    logger.info("Фотография %s: %s", user.first_name,
                f'{user.first_name}_photo.jpg')
    # Отвечаем на сообщение с фото
    update.message.reply_text(
        'Великолепно! А теперь пришли мне свое'
        ' местоположение, или /skip если параноик..'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем команду /skip для фото


def skip_photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        'Держу пари, ты выглядишь великолепно! А теперь пришлите мне'
        ' свое местоположение, или /skip если параноик.'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем местоположение пользователя


def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем местоположение пользователя
    user_location = update.message.location
    # Пишем в журнал сведения о местоположении
    logger.info(
        "Местоположение %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'Может быть, я смогу как-нибудь навестить тебя!'
        ' Расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу `BIO`
    return BIO

# Обрабатываем команду /skip для местоположения


def skip_location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о местоположении
    logger.info("User %s did not send a location.", user.first_name)
    # Отвечаем на сообщение с пропущенным местоположением
    update.message.reply_text(
        'Точно параноик! Ну ладно, тогда расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу `BIO`
    return BIO

# Обрабатываем сообщение с рассказом/биографией пользователя


def bio(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s",
                user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    update.message.reply_text(
        'Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
    # Заканчиваем разговор.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил разговор


def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.',
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END

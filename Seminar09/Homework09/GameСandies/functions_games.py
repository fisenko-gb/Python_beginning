import logging  # Включим ведение журнала
from random import randint

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    ConversationHandler,
)

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y/%m/%d, %H:%M:%S", encoding='UTF-8')
logger = logging.getLogger(__name__)

INPUT_CANDY, MOTION_HUMAN = range(2)

count_candy = 0
min_candy = 1
max_candy = 28
human = ''
bot = 'Умник'

count_pl1 = 0
count_pl2 = 0


def messeng_set(name: str, t_kol: int, count_pl: int, count_can: int):
    '''
    Функция формирует строку сообщения о текущем состоянии игры
    '''

    return (f'Игрок {name}, взял {t_kol}, итого у него {count_pl}. На столе осталось {count_can} конфет.')


# функция обратного вызова точки входа в разговор


def start(update, _):
    user = update.message.from_user
    logging.info(f'Бот запущен {user.username} id {user.id}')
    # Начинаем разговор с вопроса
    update.message.reply_text(
        f'Добро пожаловать на Игру, {user.username}!!!\n\nПравила:\nна столе лежит ограниченное количество конфет, кто забирает последнюю конфету, тот выигрывает!\nУдачи!!!')
    update.message.reply_text('Введите общее количество конфет: ')
    return INPUT_CANDY

def input_cout_candy(update, _):
    global count_candy
    number = update.message.text
    logging.info(f'Человек ввел количество конфет всего {number}')
    try:
        count_candy = int(number)
        if count_candy <= max_candy:
            t_text = f'Количество конфет не может быть меньше {max_candy}'
            update.message.reply_text(t_text)
            logging.error(t_text)
        else:
            rez = randint(0, 2)
            if rez:
                logging.info('Первым ходит человек')
                update.message.reply_text('Сколько конфет Вы возьмете?')
            else:
                logging.info('Первым ходит бот')
                game(update)
            return MOTION_HUMAN

    except:
        logging.error(f"Не удалось привести к числу {number}. Вызвано исключение.")
        update.message.reply_text('Введенные данные не корректны... ')


def motion_human(update, _):
    global count_pl1, count_candy
    user = update.message.from_user
    number = update.message.text
    logging.info(f'Человек ввел {number}')
    try:
        k = int(number)
        if k < min_candy or k > max_candy or k > count_candy:
            t_text = 'Вводить можно числа от 1 до 28 и не больше остатка конфет'
            update.message.reply_text(t_text)
            logging.ERROR(t_text)
        else:
            count_pl1 += k
            count_candy -= k
            update.message.reply_text(messeng_set(user.username, k, count_pl1, count_candy))
            if count_candy == 0:
                update.message.reply_text('Поздравляю Вас с победой!!!')
                logging.info('Выиграл человек')
                reset()
                return ConversationHandler.END
            elif count_candy <= max_candy:
                update.message.reply_text('На этот раз победил Умник!!!')
                logging.info('Выиграл бот')
                reset()
                return ConversationHandler.END
            else:
                game(update)
                if count_candy == 0:
                    update.message.reply_text('На этот раз победил Умник!!!')
                    logging.info('Выиграл бот')
                    reset()
                    return ConversationHandler.END
                elif count_candy <= max_candy:
                    update.message.reply_text('Поздравляю Вас с победой!!!')
                    logging.info('Выиграл человек')
                    reset()
                    return ConversationHandler.END
                else:
                    logging.info(f'Человек взял {k} конфет')
                    return MOTION_HUMAN
    except:
        update.message.reply_text('Введенные данные не корректны... ')
        logging.ERROR(f'Введены не корректные данные {number}. Вызвано исключение')


def game(update):
    global count_pl2, count_candy

    if count_candy == max_candy:
        k = max_candy
    elif count_candy < max_candy:
        k = count_candy
    elif (count_candy > max_candy * 2) or (count_candy == max_candy + 1):
        k = randint(min_candy, max_candy)
    else:
        k = count_candy - max_candy - 1

    count_pl2 += k
    count_candy -= k

    update.message.reply_text(messeng_set(bot, k, count_pl2, count_candy))
    logging.info(f'Бот взял {k}')
    if count_candy != 0:
        update.message.reply_text('Сколько конфет Вы возьмете?')

def reset():
    count_candy = 0
    min_candy = 1
    max_candy = 28
    count_pl1 = 0
    count_pl2 = 0
    logging.info('Обнуление переменных')
    logging.info('==============================================================================================')


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

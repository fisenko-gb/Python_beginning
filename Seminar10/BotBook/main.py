import functions as fun
import time
from config import TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

sleep_time = 5

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', fun.start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            fun.INPUT_CANDY: [MessageHandler(Filters.text & ~Filters.command, fun.input_cout_candy)],
            fun.MOTION_HUMAN: [MessageHandler(Filters.text & ~Filters.command, fun.motion_human)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', fun.cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    if (__name__ == '__main__'):
        while True:
            try:
                updater.start_polling()
                updater.idle()
            except Exception as e:
                print('Ошибка подключения. Попытка подключения через %s сек.' % 5)
                time.sleep(sleep_time)
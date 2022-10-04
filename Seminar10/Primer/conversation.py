from functions import *
from config import TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)




if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            WAY: [MessageHandler(Filters.regex('^(Рациональные|Комплексные)$'), choose_path_to_work)],
            ENTER_FLOAT: [MessageHandler(Filters.text & ~Filters.command, get_float_number)],
            ENTER_COMPLEX: [
                MessageHandler(Filters.text & ~Filters.command, get_float_number)
            ],
            OPERATION: [MessageHandler(Filters.text & ~Filters.command, get_operation)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
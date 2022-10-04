import functions as fun
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

    show_handler = CommandHandler('show', fun.show_contact)

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', fun.start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            fun.WAY: [MessageHandler(Filters.regex('^(Рациональные|Комплексные)$'), fun.choose_path_to_work)],
            fun.ENTER_FLOAT: [MessageHandler(Filters.text & ~Filters.command, fun.get_float_number)],
            fun.ENTER_COMPLEX: [
                MessageHandler(Filters.text & ~Filters.command,
                               fun.get_float_number)
            ],
            fun.OPERATION: [MessageHandler(Filters.text & ~Filters.command, fun.get_operation)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', fun.cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(show_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

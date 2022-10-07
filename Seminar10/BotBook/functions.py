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
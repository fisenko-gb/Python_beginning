from random import randint
a = 2
print('Hello')

###########################################################################################
### Функции если есть return, то вернет значение, иначе возврат NotType или типо того ###


def is_number_power(x, y):
    if y == x**2 or x == y**2:
        print('да')
    else:
        print('нет')

###########################################################################################
### Форматированная строка ###
# f перед строкой и переменные в {}


print(f'{numbers} -> {max}')

###########################################################################################
### Приведение типов ###

number = int(input('Введите число: '))
a = list(range(-number, number+1))

###########################################################################################
### Попытка ###

try:
    x = int(x)
    if x < 1 or x > 7:
        print('Ошибка!!! Введенное Вами число не соответствует указанному диапазону')
    elif x == 6 or x == 7:
        print(f'{x} -> да')
    elif x < 6:
        print(f'{x} -> нет')
except ValueError:
    print('Вводить можно только числа от 1 до 7, по-пробуйте еще раз.')

###########################################################################################
### Генерация листа и заполнение случайными числами ###


# Создаем лист из 5 элементов и заполняем случайными числами от 1 до 100
numbers = [randint(1, 100) for i in range(5)]

###########################################################################################
### Проверка что ввели число ###

# Преобразование текста в число, с проверкой что это число, в противном случаи возвращает строку 'ошибка'


def checking_number(x):

    if x.lower() == 'стоп':
        exit()

    try:
        x = float(x)
    except ValueError:
        print('Вы ввели не число, по-пробуйте еще раз или напишите "стоп" для отмены')
        x = 'ошибка'

    return x


x = ''

while x == '' or x == 'ошибка':
    x = input('Введите число: ')
    x = checking_number(x)

###########################################################################################
### Оставить только числа ###

# Принимает строку, возвращает строку, но оставляю только цифры от входящей строки


def leave_only_numbers(st):
    rezult = ''

    for i in st:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            rezult += i

    return rezult

###########################################################################################
### Оставить только буквы ###

# Принимает строку, возвращает строку, но оставляя только буквы от входящей строки


def leave_only_char(st):
    rezult = ''

    for i in st:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 1040 and ord(i) <= 1103):
            rezult += i

    return rezult

###########################################################################################
### Перевернуть список, сделать копию списка с обратным порядком элементов ###
x = list(range(5))
reverse_x = x[::-1]

###########################################################################################
### Запись списка в файл ###
with open(file_name, 'w', encoding='utf-8') as file:
    print(*data_file, file=file, sep="\n")

###########################################################################################
import logging  # Включим ведение журнала логирование
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y/%m/%d, %H:%M:%S", encoding='UTF-8')
logger = logging.getLogger(__name__)

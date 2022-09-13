from random import randint
import time

def random_list(min: int, max: int, list_len: int) -> list:
    """
    Функция принимает на вход три параметра и возвращает список случайных числе
    """
    return [randint(min, max) for i in range(list_len)]

def leave_only_numbers(st: str) -> str:
    """
    Функция принимает строку и возвращает строку только из цифр переданной строки
    """
    rezult = ''

    for i in st:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            rezult += i

    if st[0] == '-' and len(rezult) > 0:
        rezult = '-' + rezult

    return rezult

def leave_only_char(st: str) -> str:
    """
    Функция принимает строку и возвращает строку БЕЗ цифр переданной строки
    """
    rezult = ''

    for i in st:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 1040 and ord(i) <= 1103):
            rezult += i

    return rezult

def random_my(min_number: int, max_number: int) -> int:
    """
    Функция принимает диапазон. в котором необходимо сгенирировать случайное число, на основании time, и возращает случайное число
    """

    t_data = '%.9f' % time.time()
    time.sleep(0.00001)
    interval = max_number - min_number
    razrad = len(str(interval)) * -1
    smech = int(t_data[razrad:])

    while smech > interval:
        smech = int(smech / 2)

    rnd = min_number + smech
    return rnd

def list_revers(x: list) -> list:
    """
    Функция принимает список и возращает его в перевернутом виде
    """
    return x[::-1]

def input_testing_number(t_str: str = 'Введите число: '):
    """
    Функция возращает число, если оно корректно, введенное пользователем
    """

    while type:
        input_x = input(t_str)
        try:
            x = int(input_x)
        except ValueError:
            print('"' + input_x + '"' + ' - данные введены не корректно...')
            continue
        else:
            break

    return x

def convert(number: int, osn: int = 2, t_srt: str = '') -> str:
    """
    Функция переводит десятичное число в систему исчесления переданой вторым параметром рекурсией
    """
    if number != 0:
        t_srt += convert(number // osn,
                         osn, t_srt) + str(number % osn)
    return t_srt
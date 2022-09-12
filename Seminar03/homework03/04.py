# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

from asyncio.windows_events import NULL


def convert(number: int, osn: int = 2, t_srt: str = '') -> str:
    '''
    Функция переводит десятичное число в систему исчесления переданой вторым параметром рекурсией
    '''
    if number != 0:
        t_srt += convert(number // osn,
                         osn, t_srt) + str(number % osn)
    return t_srt


def input_testing_number(t_str: str = 'Введите число: '):
    '''
    Функция возращает число, если оно корректно, введенное пользователем
    '''

    while type:
        input_x = input(t_str)
        try:
            x = int(input_x)
        except ValueError:
            print('"' + input_x + '"' + ' - не является числом')
            continue
        else:
            break

    return x


num = input_testing_number()

print(convert(num))

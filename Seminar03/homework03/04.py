# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

def binary_from_decimal(number: int, t_srt: str = '') -> str:
    '''
    Функция переводит десятичное число в двоичное представление рекурсией
    '''
    if number != 0:
        t_srt += binary_from_decimal(number // 2, t_srt) + str(number % 2)
    return t_srt


num = int(input('Введите десятичное число: '))

print(binary_from_decimal(num))

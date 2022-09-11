# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] = > [12, 15, 16]
# [2, 3, 5, 6] = > [12, 15]
from random import randint


def return_random_list(min: int, max: int, list_len: int) -> list:
    '''
    Фкнкция принимает на вход три параметра и возвращает список случайных числе
    '''
    return [randint(min, max) for i in range(list_len)]


def multiplication_pairs(t_list: list) -> list:
    '''
    Функция возвращает произведение пар чисел списка
    '''
    i = 0
    rezult = []
    while i < len(t_list) / 2:
        rezult.append(t_list[i] * t_list[len(t_list) - (i + 1)])
        i += 1
    return rezult


numbers = return_random_list(-10, 10, randint(3, 10))
rez = multiplication_pairs(numbers)

print(f'{numbers} -> {rez}')

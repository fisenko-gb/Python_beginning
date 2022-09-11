# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] = > 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
import random


def return_random_list(min: int, max: int, list_len: int) -> list:
    '''
    Фкнкция принимает на вход три параметра и возвращает список случайных чисел
    '''

    numbers = [random.uniform(min, max) for i in range(list_len)]
    i = 0
    while i < len(numbers):
        okr = random.randint(1, 5)
        numbers[i] = round(numbers[i], okr)
        i += 1
    return numbers


def return_raz(t_list: list) -> dict:
    '''
    Функция возращает разницу между максимальным и минимальным значениями дробных частей переданного на вход списка чисел
    '''
    min = t_list[0] - int(t_list[0])
    max = t_list[0] - int(t_list[0])
    for i in t_list:
        tek = i - int(i)
        if tek > max:
            max = tek
        if tek < min:
            min = tek

    return max - min


numbers = return_random_list(1, 10, random.randint(3, 10))

print(f'{numbers}= > {round(return_raz(numbers), 5)}')

# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def random_list(min: int, max: int, list_len: int) -> list:
    '''
    Фкнкция принимает на вход три параметра и возвращает список случайных числе
    '''
    return [randint(min, max) for i in range(list_len)]


def sum_odd_index(t_list: list) -> int:
    '''
    Функция возращает словарь - sum - сумма чисел на не четных позициях, numbers - список значений элементов на не четных позициях
    '''
    slovar = {}
    numbers = []
    sum = 0
    j = 0
    while j <= len(t_list):
        if j % 2 != 0:
            sum += t_list[j]
            numbers.append(t_list[j])
        j += 1

    slovar = slovar | {
        "sum": sum,
        "numbers": numbers
    }
    return slovar


list_numbers = random_list(-10, 10, 10)
rezult = sum_odd_index(list_numbers)
print(
    f'{list_numbers} -> на нечетных позициях элементы {rezult["numbers"]}, ответ: {rezult["sum"]}')

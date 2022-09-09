# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['апап4', 'fdgg3', 'fgdf', '6', 'fg24'] - ищем 24 - найдено на 4 индексе


def leave_only_numbers(st):
    rezult = ''

    for i in st:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            rezult += i

    return rezult


number = input('Введите число: ')

n_list = ['апап4', 'fdgg3', 'fdgf', '6', '3fg24']

ind = 0
for i in n_list:
    t_el = leave_only_numbers(i)
    if number in t_el:
        print(f'{n_list} - ищем {number} - найдено на {ind} индексе')
    ind += 1

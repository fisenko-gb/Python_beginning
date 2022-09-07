# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений(набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

# Принимает строку, возвращает строку, но оставляя только цифры от входящей строки
def leave_only_numbers(st):
    rezult = ''

    for i in st:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            rezult += i

    return rezult


def multiplication_numbers(x):
    rezult = []
    n_list = list(range(1, x+1))
    pred = 1

    for i in n_list:
        tek = pred * i
        rezult.append(tek)
        pred = tek

    return rezult


x = ''

while x == '' or x == 'ошибка':
    input_x = input('Введите число: ')

    if input_x.lower() == 'стоп':
        exit()

    x = leave_only_numbers(input_x)

    if len(x) == 0:
        print('Вы ввели не число, по-пробуйте еще раз или напишите "стоп" для отмены')
        x = 'ошибка'
    else:
        x = int(x)

rezult = multiplication_numbers(x)


print(f'{input_x} -> {rezult}')

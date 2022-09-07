# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

# Принимает строку, возвращает строку, но оставляя только цифры от входящей строки
def leave_only_numbers(st):
    rezult = ''

    for i in st:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            rezult += i

    return rezult


def sum_numbers(a):
    result = 0
    while a > 0:
        result += a % 10
        a //= 10
    return result


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

rezult = sum_numbers(x)

if input_x[0] == "-":
    rezult *= -1

print(f'{input_x} -> {rezult}')

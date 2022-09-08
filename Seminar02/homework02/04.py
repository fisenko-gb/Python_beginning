# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime(миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до(максимальное)
import time


def leave_only_numbers(st):
    rezult = ''

    for i in st:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            rezult += i

    return rezult


def random(max_number, min_number):

    t_data = '%.9f' % time.time()
    time.sleep(0.00001)
    interval = max_number - min_number
    razrad = len(str(interval)) * -1
    smech = int(t_data[razrad:])

    while smech > interval:
        smech = int(smech / 2)

    rnd = min_number + smech
    return rnd


min_number = ''
max_number = ''

while min_number == '' or min_number == 'ошибка':
    input_x = input('Введите минимальное число диапазона: ')

    if input_x.lower() == 'стоп':
        exit()

    min_number = leave_only_numbers(input_x)

    if len(min_number) == 0:
        print('Вы ввели не число, по-пробуйте еще раз или напишите "стоп" для отмены')
        min_number = 'ошибка'
    else:
        min_number = int(min_number)

if input_x[0] == '-':
    min_number *= -1

while max_number == '' or max_number == 'ошибка':
    input_x = input('Введите максимальное число диапазона: ')

    if input_x.lower() == 'стоп':
        exit()

    max_number = leave_only_numbers(input_x)

    if len(max_number) == 0:
        print('Вы ввели не число, по-пробуйте еще раз или напишите "стоп" для отмены')
        max_number = 'ошибка'
    else:
        max_number = int(max_number)

if input_x[0] == '-':
    max_number *= -1

if max_number <= min_number:
    print("Максимальное число не может быть больше или равно минимальномо числу...")
    exit()

i = 10
while i > 0:
    print(f'Случайное число: {random(max_number, min_number)}')
    i -= 1

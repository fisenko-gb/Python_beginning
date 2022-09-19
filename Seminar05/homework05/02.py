# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
from random import randint

def input_kol(name: str) -> int:
    '''
    Функция спрашивает у игрока, и возвращает то количество которое он выбрал
    '''
    global min_candy, max_candy
    x = 0
    while x < min_candy or x > max_candy:
        try:
            x = int(input(f'{name}, можно брать только от {min_candy} до {max_candy} конфет, сколько конфет Вы возьмете: '))
        except ValueError:
            x = 0
            print('Вводить можно только числа...')
            continue
    return x

def messeng(name: str, t_kol: int, count_pl: int, count_can: int):
    '''
    Функция формирует строку сообщения о текущем состоянии игры
    '''
    print(f'Игрок {name}, взял {t_kol}, итого у него {count_pl}. На столе осталось {count_can} конфет.')

print('Добро пожаловать на Игру, на столе лежит ограниченное количество конфет, кто забирает последнюю конфету, тот выигрывает! Удачи!!!')

min_candy = 1
max_candy = 28

human = input('Введите имя первого игрока: ')
bot = 'Умник'
count_candy = int(input('Всего на столе лежит конфет: '))
motion_human = randint(0, 2)
if motion_human:
    print(f'Первый ходит {human}')
else:
    print(f'Первый ходит {bot}')

count_pl1 = 0
count_pl2 = 0

while count_candy > max_candy:
    if motion_human:
        k = input_kol(human)
        count_pl1 += k
        count_candy -= k
        motion_human = False
        messeng(human, k, count_pl1, count_candy)
    else:
        if (count_candy > max_candy) * 2 or (count_candy == max_candy + 1):
            k = randint(min_candy, max_candy)
        else:
            k = count_candy - max_candy - 1

        count_pl2 += k
        count_candy -= k
        motion_human = True
        messeng(bot, k, count_pl2, count_candy)

if motion_human:
    print(f'{human}, Вы снова победили, как у Вас это получается?!')
else:
    print(f'И снова победил {bot}!!!')
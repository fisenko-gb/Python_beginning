from random import randint


def messeng(name: str, t_kol: int, count_pl: int, count_can: int):
    '''
    Функция формирует строку сообщения о текущем состоянии игры
    '''
    print(f'Игрок {name}, взял {t_kol}, теперь у него {count_pl}. Осталось на столе {count_can} конфет.')


min_candy = 1
max_candy = 28

count_candy = 2021

human = 'Глуповастик'
bot = 'Умник'

#motion_human = randint(0, 1)

count_pl1 = 0
count_pl2 = 0
i = 1
v_h = 0
v_b = 0

while i <= 10000:

    motion_human = randint(0, 1)

    while count_candy > max_candy:

        if motion_human:
            # k = input_kol(human)
            k = randint(min_candy, max_candy)
            count_pl1 += k
            count_candy -= k
            motion_human = False
            #messeng(human, k, count_pl1, count_candy)
        else:
            koef = randint(1, 3)
            if (count_candy > max_candy * 2) or (count_candy == max_candy + 1):
                k = randint(min_candy, max_candy)
           #elif count_candy < max_candy * 2:
            else:
                k = count_candy - max_candy - 1
            #else:
            #   k = max_candy - 1

            count_pl2 += k
            count_candy -= k
            motion_human = True
            #messeng(bot, k, count_pl2, count_candy)

    if motion_human:
        v_h += 1
        #print(f'{human}, Вы снова победили, как у Вас это получается?!')
    else:
        v_b += 1
       # print(f'И снова победил {bot}!!!')

    i += 1

print(f'Человек победил {v_h} раз, комп {v_b} раз')


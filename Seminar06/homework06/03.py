# Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math

while True:
    try:
        numbers = list(map(float, input("Введите числа через пробел:\n").split(' ')))
        break
    except:
        continue

pif = lambda k2, k1: (k2 - k1) ** 2
print(round(math.sqrt((pif(numbers[3], numbers[0]) + pif(numbers[4], numbers[1]) + pif(numbers[5], numbers[2]))), 2))
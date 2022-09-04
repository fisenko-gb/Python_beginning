# 02. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

from random import randint

numbers = [randint(1, 100) for i in range(5)]
max = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i

print(f'{numbers} -> {max}')

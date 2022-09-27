# Найти сумму чисел списка стоящих на нечетной позиции
from functools import reduce
numbers = [4, 3, 7, 3, 0, 1, -9]
sum = 0

for i in numbers[::2]:
    sum += i

print(sum)

# Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами

from random import randint

numbers = [randint(1, 10) for i in range(5)]
max_index = numbers.index(max(numbers))
min_index = numbers.index(min(numbers))

sum = 0
if max_index > min_index:
    for i in numbers[min_index+1:max_index]:
        sum += i
else:
    for i in numbers[max_index+1:min_index]:
        sum += i


print(numbers)
print(f'max_index {max_index} -> min_index {min_index}')
print(sum)

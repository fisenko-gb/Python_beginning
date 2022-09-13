# 3 - Задать список из N элементов, заполненных числами из[-N, N]. Найти произведение элементов на указанных позициях.
# Число N вводится пользователем.
# Позиции хранятся в файле file.txt в одной строке одно число
# Позиции в файл вам нужно программно положить в файл в зависимости от выбранного N: если пользователь введет двойку,
# то в файле вряд ли будут индексы 5 или 16.
# В решении должны быть и запись в файл, и чтение из файла.
import random
import f_function as f

number = f.input_testing_number()

list_number = f.random_list(number * -1, number, random.randint(5, 15))

index1 = random.randint(0, len(list_number)-1)
index2 = random.randint(0, len(list_number)-1)

while index1 == index2:
    index2 = random.randint(0, len(list_number)-1)

with open('file.txt', 'w') as file:
    file.write(str(index1) + '\n')
    file.write(str(index2) + '\n')

with open('file.txt', 'r') as file:
    data_file = file.read().split('\n')

rezult = list_number[int(data_file[0])] * list_number[int(data_file[1])]

print(list_number)
print(data_file)
print(rezult)

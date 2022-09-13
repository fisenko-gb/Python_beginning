# 1 - Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

line = '1, 2, 3, 4, 5'
list = []

for i in range(len(line)):
    if line[i] != ',' and line[i] != ' ':
        list.append(int(line[i]))

print(*list)
print(f'Min: {min(list)}')
print(f'Max: {max(list)}')

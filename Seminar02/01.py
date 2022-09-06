# s1 = list(range(5))

# s2 = list(s1)

# s2.append('a')

# print(s1)
# print(s2)


# . Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов в виде списка

# *Пример: *

# - Для N = 5: 1, -3, 9, -27, 81

def sequence(num):
    string = ''
    s = 1
    for i in list(range(num)):
        string = string + str(s) + ' '
        s *= -3
    return string


x = int(input('Введите число: '))

print(f'Для N = {x}: {sequence(x)}')

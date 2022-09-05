# 06. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

x = input('Введите число от 1 до 7: ')

try:    
    x = int(x)
    if x < 1 or x > 7:
        print('Ошибка!!! Введенное Вами число не соответствует указанному диапазону')
    elif x == 6 or x == 7:
        print(f'{x} -> да')
    elif x < 6:
        print(f'{x} -> нет')
except ValueError:
    print('Вводить можно только числа от 1 до 7, по-пробуйте еще раз.')
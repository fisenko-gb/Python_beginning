# 2 - Задайте два числа. Напишите программу, которая найдет НОК(наименьшее общее кратное) этих двух чисел. НОК - наименьшее общее кратное, которое делится и на первое, и на второе число.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())

print(a*b//gcd(a, b))

# == == == == == == =


# def lcm(a, b):
#     lcm.multiple = lcm.multiple + b
#     if (lcm.multiple % a == 0) and (lcm.multiple % b == 0):
#         return lcm.multiple
#     else:
#         lcm(a, b)
#     return lcm.multiple


# lcm.multiple = 0
# a = int(input("Ввендите первое чило: "))
# b = int(input("Введите второе число: "))
# if (a > b):
#     LCM = lcm(b, a)

# else:
#     LCM = lcm(a, b)

# print(f'НОК {LCM}')

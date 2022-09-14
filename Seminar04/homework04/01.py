# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import f_function as f


def prime_factors(n: int) -> list:
    '''
    Функция возвращает список простых множителей числа переданного параметром
    '''
    i = 2
    list_rezult = []

    while i <= n:
        if n % i == 0:
            list_rezult.append(i)
            n //= i

        i += 1

    return list_rezult


num = f.input_testing_number()

print(f"N = {num} -> {prime_factors(num)}")

# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def input_testing_number(t_str: str = 'Введите число: '):
    """
    Функция возращает число, если оно корректно, введенное пользователем
    """

    while type:
        input_x = input(t_str)
        try:
            x = int(input_x)
        except ValueError:
            print('"' + input_x + '"' + ' - не является числом')
            continue
        else:
            break

    return x

def negafibon(n:int) -> list:
    """
    Функция возращает список с рядом фибоначи для переданного числа
    """
    f_numbers = []
    a, b = 1, 1

    for i in range(n):
        f_numbers.append(a)
        a, b = b, a + b

    a, b = 0, 1

    for i in range (n + 1):
        f_numbers.insert(0, a)
        a, b = b, a - b
    return f_numbers

number = input_testing_number()

print(f'Для k = {number} список будет выглядеть так: {negafibon(number)}')

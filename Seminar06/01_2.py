expression = '-22+2'


def get_numbers(expression):
    numbers = []
    temp = ''
    expression += '='
    minus = -1 if expression[0]=='-' else 1
    expression = expression[1:] if expression[0]=='-' else expression
    for char in expression:
        if char.isdigit():
            temp += char
        else:
            numbers.append(temp)
            temp = ''
    numbers = list(filter(lambda char: char.isdigit(), numbers))
    numbers[0] = f'-{numbers[0]}'
    return numbers


def get_operators(expression):
    return list(filter(lambda char: char in '+-*/', expression))


def check_alpha(expression):
    return not any(filter(lambda char: char.isalpha(), expression))


def check_expression(numbers: list, opers: list):
    return True if len(numbers) > len(opers)  else False


if check_alpha(expression):
    numbers = get_numbers(expression)
    list_operators = get_operators(expression)
    if check_expression(numbers, list_operators):
        print(numbers, list_operators)
    else:
        print('Выражение неполное', numbers, list_operators)
else:
    print('Вы ввели буквы')

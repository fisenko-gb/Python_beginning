import random

def input_testing_number(t_str: str = 'Введите число: '):
    """
    Функция возращает число, если оно корректно, введенное пользователем
    """

    while type:
        input_x = input(t_str)
        try:
            x = int(input_x)
        except ValueError:
            print('"' + input_x + '"' + ' - данные введены не корректно...')
            continue
        else:
            break

    return x

def random_list(min: int, max: int, list_len: int = 0) -> list:
    """
    Функция принимает на вход три параметра и возвращает список случайных числе
    """
    if list_len == 0:
        list_len = random.randint(10, 50)

    if min <= max:
        return [random.randint(min, max) for i in range(list_len)]
    else:
        return [random.randint(max, min) for i in range(list_len)]


n = input_testing_number("Введите число целое: ")

list_of_coef = random_list(0, 100, n)
list_of_coef.append(random_list(1, 100, 1).pop())

print(list_of_coef)
str = f"{list_of_coef[n]}*x^{n}"
i = n-1
while i > 0:
    if list_of_coef[i] == 0:
        continue
    elif i == 1:
        str += f" + {list_of_coef[i]}*x"
    else:
        str += f" + {list_of_coef[i]}*x^{i}"
    i -= 1
else:
    str += f" + {list_of_coef[0]}"
print(str)

with open("Our_polynom.txt", 'w', encoding='utf-8') as file:
        print(str, file=file)

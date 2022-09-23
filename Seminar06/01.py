# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
#
# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2

def str_to_list(t_str: str) -> list:
    t_str = t_str.replace(' ', '')
    new_list = []
    temp_str = ''
    for i, element in enumerate(t_str):

        if element.isdigit() or element == '.' or (
                element == '-' and i != 0 and t_str[i - 1] != '' and not t_str[i - 1].isdigit()):

            if temp_str == '':
                temp_str = element
            else:
                temp_str += element
        else:
            if element == '':
                continue
            else:
                if temp_str != '':
                    new_list.append(temp_str)
                new_list.append(element)
                temp_str = ''
    if temp_str != '':
        new_list.append(temp_str)
        temp_str = ''
    return new_list

def get_prioritet(oper:str)  -> int:
    if oper == '^':
        return 3
    elif oper == '*' or oper == '/':
        return 2
    elif oper == '+' or oper == '-':
        return 1
    return 0

def reverse_natation(t_list: list) -> list:
    rezult = 0
    out_list = []
    stek = []

    for i, element in enumerate(t_list):
        if element.isdigit():
            out_list.append(element)
        elif (len(element) > 1 and element[0] == '-'): # отрицательное число
            out_list.append('0' + element)
        elif element == ')':
            dl = len(stek) - 1
            t_ves = get_prioritet(stek[len(stek) - 1])
            while dl > 0:
                if stek[dl] != '(':
                    n_prioritet = get_prioritet(stek[dl])
                    if n_prioritet >= t_ves:
                        out_list.append(stek.pop())
                else:
                    stek.pop()
                    #break
                    continue
                dl -= 1

        else:
            stek.append(element)
    for i in stek:
        if i != '(':
            out_list.append(i)
    print(stek)
    print(out_list)
    return out_list

def calc(t_list: list, oper: str) -> float:
    rez = float(t_list[0])
    if oper == '+':
        for i in t_list[1:]:
            rez = rez + float(i)

    elif oper == '-':
        for i in t_list[1:]:
            rez = rez - float(i)

    elif oper == '*':
        for i in t_list[1:]:
            rez = rez * float(i)

    elif oper == '/':
        for i in t_list[1:]:
            rez = rez / float(i)

    return rez

def counting(t_list: list) -> float:
    rez = 0
    temp_list = []
    calc_list = []
    temp_rez = 0

    for i, element in enumerate(t_list):
        if element.isdigit():
            temp_list.append(element)
        else:

            calc_list.append(temp_list.pop())
            calc_list.append(temp_list.pop())
            temp_rez = calc(calc_list, element)
            temp_list.append(temp_rez)
            calc_list.clear()

    return temp_rez


t_str = '2*(16-14)+2'

new_list = str_to_list(t_str)
natation_list = reverse_natation(new_list)
rez = counting(natation_list)

print(f'Ввели строку: {t_str}')
print(f'Получился список: {natation_list}')
print(f'Мой расчет: {rez}')

otvet = eval(t_str)
print(f'Правильный ответ: {otvet}')

# print(f'Подсчет правильный {}')
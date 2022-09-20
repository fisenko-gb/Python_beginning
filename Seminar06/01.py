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



def leave_only_numbers(st):
    rezult = ''

    for i in st:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            rezult += i

    return rezult

t_str = '20+23+3'
new_list = []

t_str += ' '
temp_str = ''
for i, element in enumerate(t_str):
    if element.isdigit():
        temp_str += element
    else:
        new_list.append(temp_str)
        new_list.append(element)
        temp_str = ''

#for i, element in enumerate(t_str):

new_list = new_list[:-1]
print(new_list)
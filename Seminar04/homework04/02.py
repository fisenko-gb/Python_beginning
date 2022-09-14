# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def choose_different(t_list:list) -> list:
    returt_list = []

    for i in t_list:
        if i not in returt_list:
            returt_list.append(i)

    return returt_list

n_list = [1,1,1,1,2,2,2,3,3,3,4]
print(f'{n_list} -> {choose_different(n_list)}')



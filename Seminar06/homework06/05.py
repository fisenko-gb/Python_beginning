# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
t_list = [3, 3, 5, 2, 4, 8, 5]

print(list(map(lambda i: t_list[i] * t_list[len(t_list) - i - 1], range(len(t_list) // 2 + len(t_list) % 2))))
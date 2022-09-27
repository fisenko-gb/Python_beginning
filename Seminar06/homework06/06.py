# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

while True:
    try:
        number = int(input("Введите число: "))
        break
    except:
        continue

print(list(map(lambda x: (-3)**x, range(number))))
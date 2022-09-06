# slovo = 30011981
# key = 11122013

# encrypt = slovo ^ key

# print(encrypt)

# discrypt = encrypt ^ key

# print(discrypt)

# обмен значений переменных
""" x = 2
y = 5
print(f'x = {x}, y = {y}')
x = x ^ y
y = x ^ y
print(f'x = {x}, y = {y}')
x = x ^ y
print(f'x = {x}, y = {y}') """

# Таблица умножения
i = 1
j = 1

while i < 13:
    while j < 13:
        print(i * j, end = "\t")
        j += 1
    print('\n')
    j = 1
    i += 1



# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def compress(t_str: str) -> str:
    '''
        Функция сворачивает текст подсчетом количества одинаковых символов подряд
    '''
    count = 1
    result = ''
    for i in range(len(t_str) - 1):
        if t_str[i] == t_str[i + 1]:
            count += 1
        else:
            if t_str[i] == ' ':
                result += ' '
            else:
                result = result + str(count) + t_str[i]
                count = 1
    if count > 1 or (t_str[len(t_str) - 2] != t_str[-1]):
        result = result + str(count) + t_str[-1]
    return result

def decompress(t_str: str) -> str:
    '''
        Функция разворачивает свернутую строку
    '''
    number = ''
    result = ''

    for i in range(len(t_str)):
        if t_str[i] == ' ':
            result += ' '
            continue
        elif not t_str[i].isalpha():
            number += t_str[i]
        else:
            result = result + t_str[i] * int(number)
            number = ''
    return result


input_str = input("Введите текст для сжатия: ")
print(f"Текст после сжатия: {compress(input_str)}")
print(f"Текст после разворота: {decompress(compress(input_str))}")
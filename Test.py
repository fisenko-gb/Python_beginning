
def getNumber01():  # Первый вариант
    while type:
        getNumber = input('Введите число: ')                 # Ввод числа
        try:                                    # Проверка что getTempNumber преобразуется в число без ошибки
            getTempNumber = int(getNumber)
        # Проверка на ошибку неверного формата (введены буквы)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
            continue
        else:                                   # Если getTempNumber преобразован в число без ошибки, выход из цикла while
            break
    # возвращает модуль getTempNumber (для искл. отрицат. чисел)
    return getTempNumber


print(getNumber01())

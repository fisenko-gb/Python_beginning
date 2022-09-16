# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

# c = (x + n)
def encrypt_decrypt(t_string: str, t_key: int, encrypt: bool = True) -> str:
    '''
    Функция зашифровывает или расшивровывает(определяется последним параметром) принимаемый текст
    '''
    rezult = ''
    for i in range(len(t_string)):
        if encrypt:
            rezult += chr((ord(t_string[i]) + t_key))
        else:
            rezult += chr((ord(t_string[i]) - t_key))

    return rezult

def read_file(file_name: str, enc: str = 'utf-8') -> list:
    '''
       Функция читает файл и возращает список строк переданного файла
    '''
    with open(file_name, 'r', encoding=enc) as file:
        text_file = file.read().split('\n')
    return text_file

def write_file(t_list: list, file_name: str, enc: str = 'utf-8'):
    '''
       Функция записываеи в файл данные из переданного списка
    '''
    with open(file_name, 'w', encoding=enc) as file:
        print(*t_list, file=file, sep="\n")

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

shift = 3

file_name_original = 'Text_Original.txt'
file_name_encrypted = 'Text_Encrypted.txt'
file_name_decryption = 'Text_Decryption.txt'

# Читаем файл
text_file_original = read_file(file_name_original)

# Шифруем
temp_list = []
for i in text_file_original:
    temp_str = encrypt_decrypt(i, shift)
    temp_list.append(temp_str)

# Записываем зашифрованные данные в файл
write_file(temp_list, file_name_encrypted)

shift = input_testing_number()

# Читаем зашифрованный файл
text_file_encrypted = read_file(file_name_encrypted)

# Расшифровываем данные
temp_list.clear()
for i in text_file_encrypted:
    temp_str = encrypt_decrypt(i, shift, False)
    temp_list.append(temp_str)

# Пишем расшифрованные данные в файл
write_file(temp_list, file_name_decryption)


print('Работы программы завершена')


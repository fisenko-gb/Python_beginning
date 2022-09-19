# -Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

def set_tuple(list1:list, list2:list) -> tuple:

    for i in range(len(list1)):
        list1[i] = list1[i].upper()


    return dict(zip(list2, list1))

def filter_elements(t_tuple:tuple):
    new_tuple = {}
    for key, value in t_tuple.items():
        t_sum_kod = 0
        for i in value:
            t_sum_kod += ord(i)

        proverka = t_sum_kod / key == int(t_sum_kod / key)
        if proverka:
            new_tuple[t_sum_kod] = value

    return new_tuple


language_list = ['Action Script', 'C++/CLI', 'C#', 'ColdFusion', 'Dart', 'Object Pascal', 'Dylan', 'Eiffel', 'Game Maker Language (GML)', 'Groovy', 'Haxe', 'Io', 'Java', 'JavaScript', 'MC#', 'Object Pascal']
numbers_list = range(1, len(language_list) + 1)

rez = (set_tuple(language_list, numbers_list))
print(rez)
print(filter_elements(rez))


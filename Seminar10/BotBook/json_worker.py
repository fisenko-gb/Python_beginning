import json
from config import BASE_FILE

data_from_json = []

def read_base():
    global data_from_json
    try:
        with open(BASE_FILE, 'r', encoding='UTF-8') as f_o:
            data_from_json = json.load(f_o)
            return data_from_json
    except Exception as err:
        print(f'Ошибка {err.__class__} {err}')
        data_from_json = []
        write_base()
        return data_from_json


def write_base():
    global data_from_json
    string_json = json.dumps(data_from_json, indent=4, ensure_ascii=False)
    with open(BASE_FILE, 'w', encoding='UTF-8') as f_o:
        f_o.write(string_json)


def show_tuple_string(t_tuple):
    rez_string = ''
    for i in t_tuple:
        for key, value in i.items():
            rez_string += str(value) + '\n'
        rez_string += '\n'
    return rez_string


def search_base(str_searh: str) -> list:
    global data_from_json
    rez = []
    data_from_json = read_base()
    for i in data_from_json:
        for val in i.values():
            if type(val) == int:
                continue
            if str_searh.lower() in val.lower():
                rez.append(i)
                break

    return rez


def add_base(last_name: str, first_name: str, patronymic: str, telefon: str, comment: str):
    global data_from_json
    data_from_json = read_base()
    try:
        last_index = data_from_json[len(data_from_json) - 1]
        id = int(last_index['id']) + 1
    except:
        id = 1
    data_from_json.append({'id': id, 'last_name': last_name, 'first_name': first_name, 'patronymic': patronymic, 'telefon': telefon, 'comment': comment})
    write_base()

##################################################################################################
##################################################################################################

def test_read_and_write():
    data_from_json = read_base()
    print(data_from_json)
    print(show_tuple_string(data_from_json))
    add_base('Тестовый', 'Тест', 'Тестович', '123456789', 'рабочий')
    print(data_from_json)
    print(show_tuple_string(data_from_json))

def test_sear(t_str: str):
    rez_searh = search_base(t_str)
    print(show_tuple_string(rez_searh))


# test_read_and_write()
test_sear('ива')



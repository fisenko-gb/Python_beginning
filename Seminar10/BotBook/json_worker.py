import json
import csv
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

def delete_str_base(t_id: int):
    global data_from_json
    data_from_json = read_base()
    for i, j in enumerate(data_from_json):
        if j['id'] == t_id:
            del data_from_json[i]
            break
    write_base()

def update_str_base(new_str):
    global data_from_json
    data_from_json = read_base()
    for i in data_from_json:
        if i['id'] == new_str['id']:
            i['last_name'] = new_str['last_name']
            i['first_name'] = new_str['first_name']
            i['patronymic'] = new_str['patronymic']
            i['telefon'] = new_str['telefon']
            i['comment'] = new_str['comment']
            break
    write_base()

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

def export_csv():

    with open(BASE_FILE, "r", encoding="UTF-8") as my_file:    # читаем из файла
            string_json = my_file.read()
    t_list = json.loads(string_json)


    with open('export.csv', mode="w", encoding='utf-8') as w_file:
        names = ['id',
                 'last_name',
                 'first_name',
                 'patronymic',
                 'telefon',
                 'comment']
        file_writer = csv.DictWriter(w_file, delimiter=";",
                                     lineterminator="\r", fieldnames=names)
        file_writer.writerows(t_list)

def import_csv(file_name: str = 'test.csv') -> list:
    global data_from_json
    data_from_json = read_base()
    result = []
    try:
        with open(file_name, 'r', encoding='utf-8') as csv_file:
            file_read = csv.reader(csv_file, delimiter=';')
            count = 0
            for row in file_read:
                if count == 0:
                    count += 1
                    continue
                else:
                    temp_dict ={}
                    temp_dict['id'] = int(row[0])
                    temp_dict['surname'] = row[1]
                    temp_dict['name'] = row[2]
                    temp_dict['fathername'] = row[3]
                    temp_dict['telefon'] = int(row[4])
                    temp_dict['comment'] = row[5]
                result.append(temp_dict)
                count += 1
        for i in result:
            data_from_json.append(i)
        write_base()
    except:
        return -1

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
#test_sear('ива')



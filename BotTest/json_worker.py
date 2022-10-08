import json

with open('users.json', 'r', encoding='UTF-8') as f_o:
    data_from_json = json.load(f_o)

user_id = 12345
user_name = 'Леха'
last_name = 'Иванов'

if str(user_id) not in data_from_json:
    data_from_json[user_id] = {'user_name': user_name, 'last_name': last_name}

with open('users.json', 'w', encoding='UTF-8') as f_o:
    json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)

# print(data_from_json)


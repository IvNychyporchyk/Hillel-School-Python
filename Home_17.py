# Прочитать сохранённый json-файл из задания №16 и записать данные
# на диск в csv-файл, первой строкой которого озаглавив каждый
# столбец и добавив новый столбец “телефон”.

import json

with open("home16.json", "r") as my_file:
    data_json = my_file.read()
capitals = list(json.loads(data_json).values())
capitals[0].append(4357687)
capitals[1].append(4363756)
capitals[2].append(3457354)
capitals[3].append(3248755)
capitals[4].append(5738457)
# header_data = ["Name", "Age", "Telefone"]
# capitals.insert(0, header_data)
# print(capitals)

import csv

with open('home17.csv', 'w', newline='') as new_file:
    writer = csv.writer(new_file, delimiter=',')
    writer.writerow(['Name', 'Age', 'Telefone'])
    for item in capitals:
        writer.writerow(item)

# with open('home17.csv', mode='w', encoding='utf-8') as f:
#     file_writer = csv.writer(f)
#     for item in capitals:
#         file_writer.writerow(item)

with open('home17.csv', encoding='utf-8') as f:
    file_read = csv.reader(f)
    count = 0
    for row in file_read:
        print(f'{row[0]} | {row[1]} | {row[2]}')
    if count == 0:
        print('-' * 20)
    count += 1

# Записать в CSV-файл нижеприведённые данные.
# После этого прочитать этот файл и вывести данные в виде таблицы


# import csv
#
# name_of_filds = ['Name', 'Grade', 'Age']
# field_01 = ['Jack', '3', '10']
# field_02 = ['Tom', '5', '12']
# field_03 = ['Sam', '11', '18']
#
#
# with open('task_02.csv', mode='w', encoding='utf-8') as f:
#     file_writer = csv.writer(f)
#     for item in (name_of_filds, field_01, field_02, field_03):
#         file_writer.writerow(item)
#
# print('-' * 50)
#
# with open('task_02.csv', encoding='utf-8') as f:
#     file_reader = csv.reader(f)
#     count = 0
#     for row in file_reader:
#         print(f'{row[0]} | {row[1]} | {row[2]}')
#         if count == 0:
#             print('-' * 20)
#         count += 1

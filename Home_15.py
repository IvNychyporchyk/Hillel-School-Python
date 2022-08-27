# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.


str_1 = input("Введіть вашу першу строку:\n")
str_2 = input("Введіть вашу другу строку:\n")
str_3 = input("Введіть вашу третю строку:\n")
str_4 = input("Введіть вашу четверту строку:\n")

with open('file_test.txt', 'w') as file:
    file.write(f"{str_1}\n{str_2}\n")

file = open('file_test.txt', 'a')
try:
    file.write(f"{str_3}\n{str_4}\n")
finally:
    file.close()












# f = open('test.txt')
#
# data_a = f.readline()
# print(f'first line: {data_a}')
# f.close()
#
# f = open('test.txt')
# for index, item in enumerate(f):
#     if index == 4:
#         print(f'fives line: {item}')
# f.close()
#
# f = open('test.txt')
# for index, item in enumerate(f):
#     if index <= 4:
#         print('lines:', item, end='')
# f.close()
#
# print('-' * 50)
#
# with open('test.txt') as f:
#     a = f.readlines()
#     for item in a:
#         print(item, end='')

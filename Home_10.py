# Дан список состоящий из данных разного типа.
# Вернуть новый список, где при помощи функции map() каждый элемент типа int
# первоначального списка приведён к типу str, элементы всех остальных типов
# передаются в новый список без изменения их типа.
# В качестве функции в map использовать lambda.


values_ = [1, 2, '3', 'forth', 'end', 99, True, None]
new_list = list(map(lambda x: str(x) if type(x) == int else x, values_))
print(new_list)















# def intersection(values):
#     out = list(map(lambda it: int(it) in values))
#     return out
#
# print("Отфильтрованный список:", intersection())


# print(type(values))
# values_list = list(values)
# print(values_list)
# print(type(values_list))
# for el in values:
#     print(type(el), el)
#     int(el) == str(el)
#     print(int(el) == str(el))



 # for elem_list in values:
#     if elem_list == int(elem_list):
#         continue
#         new_elem_list == str(elem_list)
#     print(new_elem_list)
    # old_value = values[elem_list]
    # new_value = str(old_value)
    # values[elem_list] = new_value



# new_list = list(map(lambda x: str(x) if type(x) == int()))
# print(new_list())

# Дан список чисел.
# Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь (ключ - само число,
# а значение - сколько раз оно встречается). Для проверки нахождения элемента
# в словаре использовать метод get(), либо оператор in.


def counting_fun():
    input_list = list(input("Enter a list of numbers: "))
    generated_dict = {key: list(input_list).count(key) for key in input_list}
    print(generated_dict)
    print(generated_dict.get(str(input("Enter the dictionary key: "))))


counting_fun()





# generated_dict = dict(zip(list(input_list), [list(input_list).count(key) for key in list(input_list)]))
# print("Dictionary : ", generated_dict)
# print("count : ", len(generated_dict))

# Написать лямбда-функцию определяющую чётное/нечётное.
# Функция принимает параметр (число) и если чётное,
# то выдаёт слово “чётное”, если нет - то “не чётное”.

my_int = int(input("Enter your integer: "))
checked_int = lambda x: print("Парне") if x % 2 == 0 or print("Не парне") else x % 2 == 1
# checked_int = lambda x: print(f"Парне: {x}") if x % 2 == 0 or print(f"Не парне: {x}") else x % 2 == 1
checked_int(my_int)














# even_int = lambda x: (x % 2 == 0), my_int
# odd_int = lambda x: (x % 2 == 1), my_int
# print(f"Парне: {even_int}")
# print(f"Не парне: {odd_int}


# def area(b, h):
#     return 0.5 * b * h
#
#
# area_lambda = lambda b, h: 0.5 * b * h
#
#
# print(area(2, 4))
# print(area_lambda(2, 4))
#
#
# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# print(new_list)
#
#
#
# tables = [lambda x = x: x*10 for x in range(1, 11)]
# for table in tables:
#     print(table())
#
#
# max_number = lambda a, b: a if a > b else b
# print(max_number(3, 5))
#
#
# current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
# sorted_list = lambda x: (sorted(i) for i in x)
# second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
# result = second_largest(current_list, sorted_list)
# print(result)

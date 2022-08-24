# Написать декоратор к 2-м любым функциям, который бы считал и
# выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()

import time


def decorator_of_time(function):
    def wrapped(*args, **kwargs):
        start_time = time.perf_counter_ns()
        new_fun = function(*args, **kwargs)
        print("Time function: ", time.perf_counter_ns() - start_time)
        # pref_counter_ns(): завжди дає ціле значення часу в наносекундах
        return new_fun

    return wrapped


@decorator_of_time
def func_1():
    name_ = str(input("Введіть ваше ім'я: "))
    age_ = int(input("Введіть ваш рік народження: "))
    return f"Hello {name_}! Вам дійсно {age_} років."


print("-" * 50)
print(func_1())
print("-" * 50)


@decorator_of_time
def func_2(arg1, arg2):
    return int(arg1 * (arg1 + arg2))


print("-" * 50)
print("Result func_2: ", func_2(25, 25))
print("-" * 50)



















# def wrapper(*args, **kwargs):
#     t = time.clock()
#     res = func(*args, **kwargs)
#     print
#     func.__name__, time.clock() - t
#     return res
#
#
# return wrapper












# def my_decorator(a_func):
#     def the_wrapper():
#         print("Before")
#         a_func()
#         print("After")
#
#     return the_wrapper
#
#
# def my_decorator_2(a_func):
#     def the_wrapper():
#         print("Before 2")
#         a_func()
#         print("After 2")
#
#     return the_wrapper
#
#
# @my_decorator
# @my_decorator_2
# def alone_func():
#     print("I am alone function")


# alone_func()
#
# print("-" * 50)
#
# alone_func = my_decorator(alone_func)

# alone_func()

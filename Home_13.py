# Написать программу, которая состоит из вечного цикла ожидающего ввод числа
# или одно из значений: "выход", "exit", "quit", "e" или "q" в любом регистре.
# При вводе одного из этих значений происходит выход из вечного цикла.
# При любом другом вводе вызывается отдельная функция которая умеет распознавать
# введённые числа. Сама функция ничего не распечатывает, она возвращает строку,
# типа: "Вы ввели отрицательное дробное число: -6.7" или "Вы ввели не корректное
# число: Erdf". Затем в цикле выводится это сообщение и цикл начинается заново
# ожидая следующего ввода. Функция на вход принимает строку из ввода из вечного
# цикла. Анализирует её исключительно методом .isdigit() и другими методами
# строк, без доп.библиотек и переводит строку в число, если это возможно.
# Функция умеет распознавать отрицательные числа и десятичные дроби, а так же
# распознаёт десятичные дроби как с точкой, так и с запятой.
# Функция возвращает строку в которой описывается какое число введено -
# отрицательное или положительно, целое или дробное и выводит его или же
# сообщает, что введено не корректное число.
# *Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля
#
# Примеры:
# -6,7 → Вы ввели отрицательное дробное число: -6.7
# 5 → Вы ввели положительное целое число: 5
# 5.4r → Вы ввели не корректное число: 5.4r
# -.777 → Вы ввели отрицательное дробное число: -0.777

def check_float(str_):
    f = float(str_)
    if f > 0:
        return f"Вы ввели положительное дробное число: {float(str_)}"
    return f"Вы ввели отрицательное дробное число: {float(str_)}"


def check_int(str_):
    f = int(str_)
    if f < 0:
        return f"Вы ввели отрицательное число: {int(str_)}"
    return f"Вы ввели положительное число: {int(str_)}"


while True:
    input_st = input("Введіть значення: ")
    input_str = input_st.replace(',', '.')
    if not input_str.lstrip('-').replace('.', '').isdigit():
        print(f"Вы ввели не корректное число: {input_str}")

    elif input_str.lstrip('-').find('.') == 1:
        print(check_float(input_str))
    else:
        print(check_int(input_str))
    answer = input("Do you want to go out? ( Выход / Exit / Quit / E / Q ): ")
    if answer.lower() in ('выход', 'exit', 'quit', 'e', 'q'):
        break

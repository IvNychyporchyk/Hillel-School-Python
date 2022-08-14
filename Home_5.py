# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for


while True:
    input_str = input("Enter an integer n: ")
    if not input_str.isdigit() or int(input_str) == 0:
        print("Error, try again!")
        continue
    input_n = int(input_str)
    step = 0
    sum_cubes = 0
    while input_n > step:
        step += 1
        if step % 3 == 0:
            continue

        sum_cubes += int(step) ** 3
        print("Step: ", step)
        print("Result cubes: ", sum_cubes)
    print("The result is as follows", sum_cubes)

    answer = input("Do you want to go out? (Y/D): ")
    if answer.upper() in ('Y', 'D'):
        break

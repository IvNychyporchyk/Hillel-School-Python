sum_cubes = 0
while True:
    input_str = input("Enter an integer n: ")
    if not input_str.isdigit() or int(input_str) == 0:
        print("Error, try again!")
        continue
    for index in range(1, int(input_str) + 1):
        if index % 3 == 0:
            continue
        print("Index: ", index)
        sum_cubes += int(index) ** 3
        print("Result cubes: ", sum_cubes)
    print("The result is as follows", sum_cubes)

    answer = input("Do you want to go out? (Y/D): ")
    if answer.upper() in ('Y', 'D'):
        break


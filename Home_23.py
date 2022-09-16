# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень
# и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких
# исключений, как минимум деление на 0.
#
# Создать своё исключение, к примеру возведение в отрицательную степень.


class MyException(Exception):
    def __init__(self, message="Raising to a negative power!"):
        super().__init__(message)


class calculator():

    def __init__(self, in_1=None, in_2=None):
        self.a = in_1
        self.b = in_2

    def add_vals(self):
        result = None
        try:
            result = int(self.a) + int(self.b)
        except ValueError:
            result = float(self.a) + float(self.b)
        return result

    def mul_vals(self):
        result = None
        try:
            result = int(self.a) * int(self.b)
        except ValueError:
            result = float(self.a) * float(self.b)
        return result

    def div_vals(self):
        result = None
        try:
            result = int(self.a) / int(self.b)
        except ValueError:
            result = float(self.a) / float(self.b)
        return result

    def sub_vals(self):
        result = None
        try:
            result = int(self.a) - int(self.b)
        except ValueError:
            result = float(self.a) - float(self.b)
        return result

    def elevation_to_a_degree(self):
        if int(self.b) < 0:
            raise MyException()
        result = None
        try:
            result = int(self.a) ** int(self.b)
        except ValueError:
            result = float(self.a) ** float(self.b)

        return result

    def square_root(self):
        try:
            if int(self.a) < 0:
                square_ = abs(int(self.a)) ** (1 / int(self.b)) * (-1)
            elif float(self.a) < 0:
                square_ = abs(float(self.a)) ** (1 / float(self.b)) * (-1)
            elif int(self.a) > 0:
                square_ = abs(int(self.a)) ** (1 / int(self.b))
            elif float(self.a) > 0:
                square_ = abs(float(self.a)) ** (1 / float(self.b))
        except ValueError:
            if type(self.a) == int():
                square_ = abs(int(self.a)) ** (1 / 2)
            else:
                square_ = abs(float(self.a)) ** (1 / 2)
        return square_


input_1 = input("Enter the first number: ").replace(",", ".")
input_2 = input("Enter the second number: ").replace(",", ".")
my_instance = calculator(input_1, input_2)

choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Div")
    print("3. Mul")
    print("4. Sub")
    print("5. Elevation to a degree")
    print("6. Square root")
    choice = int(input("Enter your choice... "))
    if choice == 1:
        print("The computed addition result is : ", my_instance.add_vals())
    elif choice == 2:
        print("The computed subtraction result is : ", my_instance.sub_vals())
    elif choice == 3:
        print("The computed product result is : ", my_instance.mul_vals())
    elif choice == 4:
        print("The computed division result is : ", my_instance.div_vals())
    elif choice == 5:
        print("The computed division result is : ", round(my_instance.elevation_to_a_degree(), 4))
    elif choice == 6:
        print("The computed division result is : ", round(my_instance.square_root(), 4))
    elif choice == 0:
        print("Exit")
    else:
        print("Sorry, invalid choice!")
print()

# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение
# обязательного атрибута max_load.
# Создать по 2 объекта для каждого из классов truck и car,
# проверить все их методы и атрибуты.
import time


class Auto(object):
    brand = None
    age = 0
    mark = None
    weight = None
    color = None

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        """ Метод руху """
        print("Move!")

    def birthday(self):
        """ Метод роста """
        self.age += 1
        print(self.age)

    def stop(self):
        """ Метод зупинки """
        print("Stop!")


class Truck(Auto):
    max_load = None

    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print("Attention!")
        super().move()

    def load(self):
        time.sleep(1)
        print('Load!!!')
        time.sleep(1)


class Car(Auto):
    max_speed = None

    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        super().move()
        print(f"«Max speed is <{self.max_load}> »")


truck_1 = Truck("oak", 24, "werwre", 98787)
truck_1.move()
truck_1.birthday()
truck_1.stop()
truck_1.load()
print("--" * 50)
car_1 = Car("bmw", 24, "dere", 987)
car_1.move()
car_1.birthday()
car_1.stop()
print("--" * 50)
truck_2 = Truck("ww", 24, "fgkjd", 967)
truck_2.move()
truck_2.birthday()
truck_2.stop()
truck_2.load()
print("--" * 50)
car_2 = Car("dfjd", 24, "fkgg", 899)
car_2.move()
car_2.birthday()
car_2.stop()

# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto(object):
    brand = None
    age = 0
    color = None
    mark = None
    weight = None

    def __init__(self, brand, mark, age=0):
        self.brand = brand
        self.age = 0
        self.mark = mark


def move(self):
    """ Метод руху """
    print("Move!")


def birthday(self):
    """ Метод роста """
    self.age += 1


def stop(self):
    """ Метод зупинки """
    print("Stop!")

















# class Animal(object):
#     viviparous = True
#     number_of_foot = 4
#     tail = True
#     name = None
#
#     def __init__(self, name, number_of_foot=4, tail=True):
#         self.name = name
#         self.number_of_foot = number_of_foot
#         self.tail = tail
#
#     def go(self):
#         for item in range(1, self.number_of_foot + 1):
#             print(f'Step on {item} foot', end='-')
#         print()
#
#
# class Dog(Animal):
#     _weight_1 = 10
#     __weight_2 = 20
#
#     def __str__(self):
#         return f"Это класс собака, у него есть хвост и лапы"
#
#     def say(self):
#         print('Woof, woof')
#
#
# class Cat(Animal):
#
#     def say(self):
#         print('Miay')
#
#
# class Dolphin(Animal):
#     fin = True
#     number_of_foot = None
#
#     def __init__(self, name='Noname', number_of_foot=3, tail=True, fin=True):
#         super().__init__(name, number_of_foot, tail)
#         self.fin = fin
#
#     def say(self):
#         print('Ultrasound')
#
#     def go(self):
#         print('Swim')
#         super().go()
#         print('Swim')
#
#     def not_breath(self):
#         print('No breath around 60 min')
#
#
# dog_1 = Dog('Jack', tail=False)
# dog_1.say()
# dog_1.go()
# print(dog_1)
# print(dog_1.name)
# print(dog_1.tail)
# print(dog_1._weight_1)
# print(dog_1._Dog__weight_2)
#
# print('-' * 30)
#
# dog_2 = Dog('Bob')
# print(dog_2.name)
# print(dog_2.tail)
#
# print('-' * 30)
#
# cat_1 = Cat('Sisy')
# print(cat_1.name)
# print(cat_1.tail)
# cat_1.say()
# cat_1.go()
#
# print('-' * 30)
#
# d_1 = Dolphin('Noname')
# d_1.go()
# print(d_1.name)

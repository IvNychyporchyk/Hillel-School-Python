# Создайте свой произвольный класс и в нём помимо обычных методов и
# атрибутов создайте несколько статических методов и методов класса.
# Продемонстрируйте их работу.

import datetime


class Person:
    num_telefone = None
    _type = "Person"
    number_of_person = 0

    def __init__(self, name=None, age=None, year=None, num_telefone=None):
        self.name = name
        self.age = age
        self.year = year
        self.num_telefone = num_telefone
        Person.number_of_person += 1

    def getAge(self):
        return self.age

    @staticmethod
    def greeting_h():
        print("Hello human being")

    # метод класу для створення об’єктa Person за роком народження

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, datetime.date.today().year - year)

    @staticmethod
    def print_type():
        print(Person._type)

    @classmethod
    def Num_person(cls):
        print("Number of person:", cls.number_of_person)

    @staticmethod
    def is_Adult(name, age):
        if age > 18:
            print(f"{name}you are an adult")
        else:
            print(f"{name} you have to grow up a little, up to {18 - age} years!")

    def number_tel(self):
        print(f" {self.name}, your phone number {self.num_telefone}")


Person.greeting_h()

person1 = Person('Mak', 17, 5767463487)
person2 = Person.fromBirthYear('Yank', 1996)

print(person1.age)
print(person2.age)
Person.is_Adult('Mak', 17)
Person.number_tel(person1)
Person.Num_person()

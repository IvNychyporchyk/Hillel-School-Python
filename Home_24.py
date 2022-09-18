# Создать генератор геометрической прогрессии

class Counter(object):

    def __init__(self, member, high, step):
        self.member = member
        self.high = high
        self.step = step
        self.i = 0

    def __next__(self):
        while self.member != 0 and self.high >= 1:
            if self.i < self.step:
                self.i += 1
                return self.member * self.high ** (self.i - 1)
        raise StopIteration

    def __iter__(self):
        return self


a = Counter(2, 3, 3)

for item in a:
    print(item)


#
# def simple_generator(member, high, step):
#     while member != 0 and high >= 1:
#         for i in range(1, step + 1):
#             if i <= step:
#                 yield member * high ** (i - 1)
#         break
#
#
# for item in simple_generator(5, 6, 7):
#     print(item)

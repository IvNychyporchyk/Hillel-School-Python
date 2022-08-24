# При помощи функции filter() из котрежа слов отфильтровать только те,
# которые являются полиндромами (читаются одинаково в обе стороны),
# регистр букв не учитывать.

indata = ('Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык')

palindromes = list(filter(lambda x: x.casefold() == x[::-1].casefold(), indata))
print("Слова поліндроми: ", list(palindromes))

















# inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
# def intersection(arr1, arr2):
#    out = list(map(lambda it: int(it) in arr1, arr2))
#    return out
# out = intersection(arr1, arr2)
# print("Отфильтрованный список:", out)








# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 75, 99, 12]
#
#
# def is_A(score):
#     return score >= 75
#
#
# over_75 = list(filter(is_A, scores))
# print(over_75)
#
# over2_75 = list(filter(lambda x: x >= 75, scores))
# print(over2_75)
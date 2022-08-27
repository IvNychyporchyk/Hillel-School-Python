# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’
# И на конец результат снова декодировать в строку
# (результаты всех преобразований выводить на экран).

string_bytes = b'r\xc3\xa9sum\xc3\xa9'
str_decode = string_bytes.decode()
print(string_bytes)
print(str_decode)

string_latin1 = str_decode.encode('Latin1')
print(string_latin1)
str_dec_latin1 = string_latin1.decode('Latin1')
print(str_dec_latin1)

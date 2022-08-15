# Дан словарь, создать новый словарь при помощи конструкции
# генератор словаря, поменяв местами ключ и значение.

just_phrase = "Hello, Yevhen Arefa!"
given_dict = {sym_p: sym_p * 4 for sym_p in just_phrase}
print(given_dict)
new_dict = {value: key for key, value in given_dict.items()}
print("New dictionary:\n", new_dict)
print("-" * 50)

# second_dict = {val: val**2 + 1 for val in range(8)}
# print(second_dict)
# new_dict_2 = second_dict | given_dict
# print(new_dict_2)





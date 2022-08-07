# ---------------------------------------------------------------------------------
# First point of homework

tuple_1 = (12, 12, 33, 34)
tuple_2 = (12, 12, 33, 34)
tuple_3 = (12, 12, 33, 34)
print(id(tuple_1))
print(id(tuple_2))
print(id(tuple_3))
print(tuple_1 == tuple_2 == tuple_3)
print(tuple_1 is tuple_2 is tuple_3)
# ---------------------------------------------------------------------------------
# Second point of homework

set_11 = {23, 34, 44, 55}
set_21 = {23, 34, 44, 55}
print(id(set_11))
print(id(set_21))
print(set_11 == set_21)
print(set_11 is set_21)
# -----------------------------------------------------------------------------------
# Third point of homework

set_1 = set(tuple_1)
set_2 = set(tuple_2)
set_3 = set(tuple_3)
print(id(set_1))
print(id(set_2))
print(id(set_3))
print(set_1 == set_2 == set_3)
print(set_1 is set_2 is set_3)
# --------------------------------------------------------------------
string_1 = str(set_11)
string_2 = str(set_21)
print(id(string_1))
print(id(string_2))
print(string_1 == string_1)
print(string_1 is string_1)
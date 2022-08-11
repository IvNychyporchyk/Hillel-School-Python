Str_0, Str_1 = input("Enter a two-word sentence: ").split(" ")
Str_3: str = f"{Str_0}  {Str_1}"
print(Str_3)
print(Str_0)
print(Str_1)
nwst_0 = Str_3[::-1]
print(nwst_0)
nwst_1: str = f"{Str_0.upper()[::-1]} {Str_1.title()[::-1]}"
print(nwst_1)
nwst_2 = f"!{nwst_1}?"
print(nwst_2)
New_string_0 = nwst_1[::-1]
print(New_string_0)
print(Str_3, nwst_0, nwst_1, nwst_2, New_string_0, sep="<<<>>>")















# print(       ,sep="<<<>>>")

# str_0: str = input("Type the first word: ")
# str_1: str = input("Enter the second word: ")
# str_3 = f"{str_0}  {str_1}"
# print(str_3)


# str_1 = str_0[1::2]
# print(str_1)
# str_2 = str_0[::-1]
# print(str_2.upper())

# file_0 = open("pythonfile.txt", "w")
# print(str_4, file=file_0)
# file_0.close()

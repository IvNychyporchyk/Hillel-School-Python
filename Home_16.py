import json

input_dic = {
    678945: ("Dan", 23),
    457328: ("Sara", 22),
    897678: ("Alex", 26),
    978575: ("Olena", 24),
    788765: ("Victoria", 27)
}

with open("home16.json", "w") as f:
    json.dump(input_dic, f)

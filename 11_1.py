"""

1. WAP to create a Dictionary of  with their position as their values.

Example:    Dict_Alpha = {"A":1 , "B":2 , "C":3 , .... , "Z":26}

"""

dict_d = {}
values_d = 0

for i in range(65, 91):
    keys_d = chr(i)
    values_d += 1
    dict_d[keys_d] = values_d

print(dict_d)
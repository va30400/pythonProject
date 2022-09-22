"""

WAP to input 2 List from user, One is the key List and the other one is the Value list
and then Create a Dictionary using the Keys and Values
"""

key_list = eval(input("enter key list "))
value_list = eval(input("enter value list"))
user_dict = {}

for i in range(0, len(key_list)):
    key_d = key_list[i]
    value_d = value_list[i]
    user_dict[key_d] = value_d

print(user_dict)
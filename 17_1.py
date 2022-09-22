
# list, replace odd numbers with "odd" and even ...


def conv(user_num):
    if user_num % 2 == 0 :
        return "Even"
    else :
        return "Odd"

userRange = eval(input("enter your list "))

l2 = []

l2 = list(map(conv , userRange))

print(l2)

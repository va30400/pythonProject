T = int(input())

a =  b = 0

for i in range(T):
    input_string = input()
    a, b = input_string.split()
    a = int(a)
    b = int(b)
    if (a > b):
        print (b)
    else:
        print (a)
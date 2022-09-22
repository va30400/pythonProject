# cook your dish here
T = int(input())

a = b = c = d = 0

for i in range(T):
    input_string = input()
    # convert each item to int type
    a, b, c, d = input_string.split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    print(max(a, b) + max(c, d))

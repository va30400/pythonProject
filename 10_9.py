# cook your dish here
# cook your dish here
T = int(input())

a = b = 0

for i in range(T):
    input_string = input()
    # convert each item to int type
    a, b = input_string.split()
    a = int(a)
    b = int(b)
    c = abs(a-int(((a+b)/2)))
    d = abs((b-int(((a+b)/2))))
    print(max(c,d))

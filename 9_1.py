# 1 to 100, including both, create a list which are mutilples of 2 & 3

l = [i for i in range(1,101) if ( i%2==0 and i%3==0 ) ]
print (l)

# input list from user, convert list [23,45,7,89] --> 2345789

ll = eval(input("input your list "))

num = ""

for i in range(0,len(ll)):
    num += str(ll[i])

num = int(num)
print(num, type(num))
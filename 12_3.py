
# input set from user and find min max

set_s = eval(input("enter your set : "))
max = -999
min = 999

for i in set_s:
    if i > max :
        max = i
    if i < min :
        min = i

print(min, max)
# take tuple from user, largest number index

tt = eval(input("input your tuple "))

largest = tt[0]
ind = 1

for i in range(1,len(tt)):
    if tt[i] >= largest:
        largest = tt[i]
        ind = i

print(largest, ind)

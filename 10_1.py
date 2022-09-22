# take a list with minimum 2 elements from user, find the elements with highest product

ll = eval(input("input your list "))

prod = highProd = 0
x = y = 0
# [1 , 23, 78 , 45, 5]

for i in range(len(ll)):
    for j in range(i, len(ll)):
        prod = ll[i] * ll[j]
        if (prod > highProd and i != j):
            highProd = prod
            x = ll[i]
            y = ll[j]

print(x,y)




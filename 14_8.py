# print first n natural numbers
"""
def natural_n(i, j=1):
    if i > j:
        print (j)
        natural_n(i, j+1)
    else:
        print (i)


u_num = int(input("enter a number "))

natural_n(u_num)
"""

"""
def natural_n(i, j=1):
    if i != j:
        return j, natural_n(i, j + 1)
    else:
        return i

"""


def natural_n(i, j = 1):
    if i > j :
        return natural_n(i, j+1)
    else :
        return j


u_num = int(input("enter a number "))

for k in range(1, u_num+1):
    result = natural_n(k)
    print(result)


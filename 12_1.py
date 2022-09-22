
"""

num_n = int(input("how many numbers : "))

set_s = set()

for i in range(num_n):
    n = eval(input("enter the set element "))
    set_s.add(n)

print(set_s)
"""

s_1 = {1,3,5,4}
s_2 = {1,3,5}

print(s_2.issuperset(s_1))
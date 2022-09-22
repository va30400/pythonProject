# take n and r from user, use recursion to find nCr

def ncr(n, r):
    return int(fact(n) / (fact(r) * fact(n - r)))


def fact(n2):
    if n2 == 1 or n2 == 0:
        return 1
    else:
        return n2 * fact(n2 - 1)


u_num1 = int(input("enter your N number "))
u_num2 = int(input("enter your R number "))

result = ncr(u_num1, u_num2)

print(result)

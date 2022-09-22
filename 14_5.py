# take number from user and sum of even numbers series from 0 and odd numbers


def even_sum(n):
    if n == 0 :
        return 0
    if n % 2 != 0 :
        return even_sum(n-1)
    else :
        return n + even_sum(n-1)

def odd_sum(n):
    if n == 1 :
        return 1
    if n % 2 != 0 :
        return n + odd_sum(n-1)
    else :
        return odd_sum(n-1)

u_num = int(input("enter a number "))

result = even_sum(u_num)
result2 = odd_sum(u_num)
print(result, result2)


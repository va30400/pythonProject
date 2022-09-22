# GCD of 2 numbers
# take a number from user and print  n terms of fibonaci
# 0 1 1 2 3 5

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

u_num = int(input("enter a number "))

for i in range(1, u_num+1):
    result = fibo(i)
    print(result)
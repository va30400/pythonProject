# GCD of 2 numbers from user

def gcd(i,j):
    if j == 0 :
        return i
    else:
        return gcd(j, i%j)


u_num1 = int(input("enter number 1 "))
u_num2 = int(input("enter number 2 "))

result = gcd(u_num1, u_num2)

print(result)
# prime number by recursion

def prime_n(i, j = 2):
    if i == 2 :         # base case
        return True
    if i != j :
        if i % j == 0:
            return False
        else :
            return True
    else :
        prime_n(i, j+1)         # increment j until it reaches user num


u_num = int(input("enter a number "))

result = prime_n(u_num)

if result:
    print(" Your number is prime")
else:
    print(" Your number is not prime")
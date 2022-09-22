
# list out odd and even numbers

def check_even(num1):
    if num1%2 == 0 :
        return True

def check_odd(num2):
    if num2%2 != 0 :
        return True

l = [1,2,3,4,5,6,7,8,9,10]

l2 = list(filter(check_even, l))
l3 = list(filter(check_odd, l))

print(l2, l3)
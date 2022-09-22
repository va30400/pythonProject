# a list , find cube of numbers, filter the cubes multiples of 3

# function for cube
def cubed(num1):
    return num1 ** 3
# function to filter multiples of 3
def three_mult(num2):
    if num2 % 3 == 0 :
        return True

l = [20,21,23,1,7,4,6,9]

l2 = list(filter(three_mult, list(map(cubed, l))))

print (l2)


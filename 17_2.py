# take 2 lists from user of equal lenght, first list is integers and second list is integers to be treated as power

def pow_comp(num1, num2):
    return num1 ** num2

l1 = [3,6,7,9,1,2,5]
l2 = [2,3,2,1,0,9,7]

l3 = list(map(pow_comp, l1 , l2))

print (l3)
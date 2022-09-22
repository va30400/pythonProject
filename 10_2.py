totalNum = int(input("how many numbers will you input "))

for i in range(0,totalNum):
    userNum: int = int(input("enter a number : "))
    if i == 0 :
        large = userNum

    elif i == 1 :
        if userNum > large :
            secondLarge = large
            large = userNum
        else:
            secondLarge = userNum
    else :
        if userNum > large :
            secondLarge = large
            large = userNum
        elif (userNum < large) and (userNum > secondLarge):
            secondLarge = userNum
print(secondLarge)

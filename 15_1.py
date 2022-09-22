# guess the number game
import random as ra

# python generates a random number

pNum = ra.randint(10,100)

# user gets 5 chances to guess, and is given hint if number is lower or smaller

# name, rules

for i in range (0,5) :
    uNum = int(input("enter your guess "))
    if uNum not in range(10, 101):
        print("You must input between 10 and 100")
    elif uNum == pNum :
        print(" You have won ")
        break
    elif uNum < pNum :
        print("Your number is too low ")
    elif uNum > pNum :
        print ("Your number is too high")
else:
    print("The number was ", pNum)


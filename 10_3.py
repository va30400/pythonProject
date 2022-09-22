
t = (23, 45, 1, 231, 98, 231, 300, 42, 23)
# userNum = int(input("enter a number "))
#print(t[userNum])
#print(t.index(300))

# take 2 numbers from user, and print tuple elements between them, conditions for start_t & end_t

num1 = int(input("number 1 is "))
num2 = int(input("number 2 is "))

start_t = t.index(num1)
end_t = t.index(num2)

for i in range(start_t , end_t+1):
    print(t[i])
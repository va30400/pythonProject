'''

Sam likes to climb the steps either one at a time, two at a time or three at a time.
He wants to find the total number of ways in which he can climb n steps,
assuming that the order of his individual steps matters.

WAP to help Sam compute this number.

For example, if he wishes to climb three steps, the case of n = 3,
 he could do it in four different ways: (1, 1, 1)(1,1,1): do it in three moves, one step at a time (1, 2)(1,2):
 do it in two moves, first take a single step, then a double step (2, 1)(2,1):
 do it in two moves, first take a double step, then a single step (3)(3):
  do it in just one move, directly leaping to the third step To take another example,
'''


# cook your dish here
# cook your dish here
def multo(num1, num2):
    if num1 == num2:
        return True
    elif num2 % 2 == 0 and num2 // 2 > 1:
        num2 = num2 // 2
        """print (num2,type(num2))"""
        return multo(num1, num2)
    else:
        return False


T = int(input())
for i in range(T):
    a = list(map(int, (input().split())))
    c = multo(a[0], a[1])
    if c:
        print("YES")
    else:
        print("NO")

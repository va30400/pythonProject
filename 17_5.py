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


def calcn(num1):
  """  if num1 == 1:
        return 1
    if num1 == 2:
        return 2
    if num1 == 3:
        return 4
    if num1 < 1:
        return 0"""
    if num1 < 4 :
        l = [1,2,4]
        return (l[num1-1])
    else:
        return calcn(num1 - 1) + calcn(num1 - 2) + calcn(num1 - 3)


steps = int(input())
result = calcn(steps)
print(result)

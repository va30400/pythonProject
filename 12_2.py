
# take 3 lists from user and return intersecting elements

list_1 = set(eval(input("list 1 ")))
list_2 = set(eval(input("list 2 ")))
list_3 = set(eval(input("list 3 ")))

list_1.intersection_update(list_2)
list_1.intersection_update(list_3)

print(list_1)

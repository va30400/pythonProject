

def binary_search(list_l, u_num):
    start_index = 0
    end_index = len(list_l) - 1

    while (start_index < end_index):
        mid_index = ( start_index + end_index ) // 2
        if u_num == list_l[mid_index] :
            return True
        elif u_num < list_l[mid_index] :
            end_index = mid_index - 1
        elif u_num > list_l[mid_index]:
            start_index = mid_index + 1
        else :
            return False

userRange = eval(input("enter your list "))
userNum = int(input("number to find ? "))

userRange.sort()

result = binary_search(userRange, userNum)

if result:
    print(" Number was found ")
else:
    print(" Number was not found ")

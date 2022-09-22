# binary search with recursion and otherwise, input from user list and element to check

def binary_search(user_list, starting_num, ending_num, user_int):
    if ( user_int <= user_list[ending_num] ) and ( user_int >= user_list[starting_num] ) :
        mid_num = (starting_num + ending_num) // 2
        if user_list[mid_num] == user_int:
            return True
        elif user_list[mid_num] > user_int:
            return binary_search(user_list, starting_num, mid_num-1, user_int)
        elif user_list[mid_num] < user_int:
            return binary_search(user_list, mid_num+1, ending_num, user_int)
    else:
        return False


userRange = eval(input("enter your list "))
userNum = int(input("number to find ? "))

userRange.sort()

result = binary_search(userRange, 0, len(userRange)-1, userNum)

if result:
    print(" Number was found ")
else:
    print(" Number was not found ")

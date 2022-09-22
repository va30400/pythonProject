# cook your dish here
N = int(input())

initial = final = []

for i in range(N):
    stat = True
    buttons = int(input())
    initial = input()
    final = input()
    for k in range(buttons):
        if initial[k] != final[k]:
            stat = not stat
    if stat:
        print(1)
    else:
        print(0)


# why is true / false or 1 / 0 not working
# cook your dish here
T = int(input())

for i in range(T):
    N = int(input())
    counter = 0
    k = 1
    while (k <= N):
        j = 1
        while (j <= N):
            if (k + j) % 2 != 0: counter += 1
            j += 1
        k += 1
    print(counter)


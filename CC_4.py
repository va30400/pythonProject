# cook your dish here
T = int(input())

for i in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_new = []
    A_new[0] = X
    for j in range(1, len(A)):
        A_new[j] = A_new[j - 1] + A[j - 1]
    print(max(A_new))


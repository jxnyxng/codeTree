n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def sol():
    for i in range(len(A)):
        if A[i]!=B[i]:
            return print('No')
    return print('Yes')

sol()



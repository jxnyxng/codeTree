A, B = map(int, input().split())
temp = B
B = max(A, B)
A = min(A, temp)

for i in range(B, A-1, -1):
    print(i, end=' ')
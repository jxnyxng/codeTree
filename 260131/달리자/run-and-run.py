n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

P = []
for i in range(n):
    P.append(A[i] - B[i])

cost = 0
current_balance = 0

for val in P:
    current_balance += val
    cost += abs(current_balance)

print(cost)
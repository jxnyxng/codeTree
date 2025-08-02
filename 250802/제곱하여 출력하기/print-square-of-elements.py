num = int(input())
j = list(map(int, input().split()))

for i in range(num):
    print(j[i]**2, end=" ")

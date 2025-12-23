arr = [[0] * 4 for _ in range(2)]

for i in range(2):
    line = list(map(int, input().split()))
    arr[i] = line

for i in range(2):
    print(f"{sum(arr[i])/4:.1f}", end=' ')
print()

for j in range(4):
    avg = arr[0][j] + arr[1][j] 
    print(f"{avg/2:.1f}", end=' ')
print()

total_sum = sum(sum(row) for row in arr)
print(f"{total_sum/8:.1f}")
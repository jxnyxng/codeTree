n = int(input())
numbers = list(map(int, input().split()))

# 배열에서 인접 안하는 수 두개 고르고 합
# 최댓값만 가져가기
ans = 0

for i in range(n-2):
    temp = 0
    for j in range(i+2, n):
        temp = numbers[i]+numbers[j]
        ans = max(ans,temp)

print(ans)

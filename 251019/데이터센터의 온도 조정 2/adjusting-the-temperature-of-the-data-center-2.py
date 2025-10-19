N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

end=0
for i in ranges:
    end = max(end, i[1]) 
# 각 범위의 작업량 더하기
arr = [0] * (end+5)
# 최댓값출력
for i in range(N):
    for j in range(0, ranges[i][0]):
        arr[j] += C
    for j in range(ranges[i][0], ranges[i][1]+1):
        arr[j] += G
    for j in range(ranges[i][1]+1, end):
        arr[j] += H

ans=0
ans = max(arr[:])
print(ans)
n = int(input())
a = [int(input()) for _ in range(n)]

# 시작 위치 모두 탐색
# 시작 인덱스와 현재 인덱스 사이 거리 곱하기 인원수를 모두 더한게 이동거리
ans=float('inf')
for i in range(n): #시작인덱스
    dist = 0
    # 배열 끝까지 탐색
    for j in range(i, n):
        dist += (j-i) * a[j]
    # 배열 넘어서 탐색    
    for k in range(0, i):
        dist += (n-i+k) * a[k]
    
    ans = min(ans, dist)

print(ans)
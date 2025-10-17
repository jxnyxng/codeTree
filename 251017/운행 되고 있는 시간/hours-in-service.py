n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# 해고할 개발자 선택 후 운행시간 계산 -> 최댓값만 저장
ans=0
for i in range(n):
    cnt=0
    t = [0] * 1005
    for j in range(n):
        if i==j:
            continue
        for k in range(a[j], b[j]):
            t[k] = 1

    for j in t:
        if j==1:
            cnt+=1
    
    ans = max(ans, cnt)

print(ans)

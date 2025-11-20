N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
 
ans=0
# 쿠폰 적용할 선물 고르기
for i in range(N): 
    p = []
    for j in range(N):
        if i==j:
            p.append((gifts[j][0]//2) + gifts[j][1])
        else:
            p.append(gifts[j][0] + gifts[j][1])
    p.sort()
    count=0
    total=0
    for cost in p:
        if total + cost <= B:
            total += cost
            count += 1
        else:
            break
    ans = max(ans, count)

print(ans)
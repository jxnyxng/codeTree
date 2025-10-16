ability = list(map(int, input().split()))

# 여섯명을 각각 묶어서 세팀을 만드는 모든 결과 탐색
# 네명의 팀 골라주면 나머지는 알아서

# 생성된 팀 능력 최고 - 최저를 구해 최솟값만 저장

ans = float('inf')
for i in range(6):
    for j in range(6):
        for l in range(6):
            for k in range(6):
                if i==j or i==l or i==k or j==l or j==k or l==k:
                    continue
                    
                a = ability[i] + ability[j]
                b = ability[l] + ability[k]
                c = sum(ability) - (a+b) #남은 능력합

                ans = min(ans, max(a,b,c)-min(a,b,c))

print(ans)





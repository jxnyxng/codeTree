abilities = list(map(int, input().split()))

# 6명중 세명 골라서
# 더한 값과 전체에서 그걸 뺀 값 사이의 최솟값을 저장

ans=float('inf')

for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1, 6):
            s = (abilities[i]+abilities[j]+abilities[k])
            l = sum(abilities)-s
            ans =min(ans, abs(s-l))

print(ans)
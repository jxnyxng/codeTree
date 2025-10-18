N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# 할인할 물건 하나씩 골라 놓고 더해보고
# 최대 명수만 저장  
ans = 0

for i in range(N):
    np = P.copy()
    np[i] = np[i] // 2
    np.sort()

    price = 0
    cnt = 0

    for j in np:
        if price+j <= B:
            price += j
            cnt += 1
        else:
            break
            
    ans = max(ans, cnt)

print(ans)
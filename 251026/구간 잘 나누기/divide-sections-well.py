n, m = tuple(map(int, input().split()))
a = list(map(int, input().split())) 


MAX_A = 10000 
ans = MAX_A


for i in range(1, MAX_A+1): 
    possible = True
    section = 1

    cnt = 0
    for j in range(n): 
        if a[j] > i:
            possible = False
            break
         
        if cnt + a[j] > i:
            cnt = 0
            section += 1
        cnt += a[j]

    if possible and section <= m:
        ans = min(ans, i)

print(ans)

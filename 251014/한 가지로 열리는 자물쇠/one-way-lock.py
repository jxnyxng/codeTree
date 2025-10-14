N = int(input())
a, b, c = map(int, input().split())

cnt=0
# 안열리는경우가 더 적음
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            # a b c +- 2 모두 범위 밖에 수인 경우
            check = (i>a+2 or i<a-2) and (j>b+2 or j<b-2) and(k>c+2 or k<c-2)
            if check:
                cnt+=1

print((N**3) - cnt)
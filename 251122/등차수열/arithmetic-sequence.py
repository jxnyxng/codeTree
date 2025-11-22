n = int(input())
a = list(map(int, input().split()))

# 리스트의 원소들 두개를 잡아서 뺀 값이 짝수이면 카운트 
max_num = max(a)
ans = 0
for K in range(1, max_num+1):
    cnt=0
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(K-a[i]) == abs(K-a[j]):
                cnt+=1
    ans = max(ans, cnt)

print(ans)
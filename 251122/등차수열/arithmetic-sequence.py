n = int(input())
a = list(map(int, input().split()))

# 리스트의 원소들 두개를 잡아서 뺀 값이 짝수이면 카운트
cnt=0
for i in range(n-1):
    for j in range(i+1, n):
        check=abs(a[i]-a[j])
        if check!=0 and (check%2) == 0:
            cnt+=1

print(cnt)
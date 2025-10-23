n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# 숫자를 두배 했을 때 범위내에 없으면 트루반환하는 함수
def check(a, b, nnum):
    if a<= (2*nnum) <= b:
        return False
    else:
        return True


ans=0
for i in range(a[0]//2, (b[0]//2)+1):
    nnum = i
    for j in range(n):
        # 범위 내에 존재하지 않으면 트루반환 후 반복문 종료
        if check(a[j], b[j], nnum):
            break
        else:
            nnum *= 2
        if j==n-1:
            ans = i
    if ans != 0:
        break
print(ans)


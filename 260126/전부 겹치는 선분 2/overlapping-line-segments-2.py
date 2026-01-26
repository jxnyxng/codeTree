# 좌표압축 필요없음
# 카운팅 어레이 적용
# 겹치는 부분이 n-1 이상이면 yes 아니면 no

n = int(input())
arr = [0] * 105
for _ in range(n):
    st, ed = map(int, input().split())

    for idx in range(st, ed+1):
        arr[idx] += 1
        if arr[idx]>=(n-1):
            print('Yes')
            exit()

print('No')

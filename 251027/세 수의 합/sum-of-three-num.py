n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 각 숫자가 몇번씩 나왓는지 기록
d = dict()
for a in arr:
    if a in d:
        d[a] += 1
    else:
        d[a]=1

ans=0


for i in range(n):
    # 고른 거는 빼주기
    d[arr[i]] -= 1

    # 찾을 숫자 지정
    for j in range(i):
        c = k - arr[i] - arr[j]

        # 찾을 숫자가 딕셔너리에 잇으면 정답 + 1
        if c in d:
            # d[c] 는 c라는 숫자가 arr에 몇개가 잇는지 - 고른 거 제외하고
            ans += d[c]

print(ans)

N, K = map(int, input().split())
candy = []
pos = []
end = (2*K)+1
for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# 각 배열의 알맞은 위치에 사탕 개수 저장
# c-k c+K 구간에서 최대사탕 개수 찾기
# 시작은 0부터, c-K <= ?? <= c+K 틀의 길이는 (2K + 1)
arr = [0] * 10005

for i in range(N):
    arr[pos[i]] += candy[i]

ans = 0
for i in range(10005-end):
    ans = max(ans, sum(arr[i:i+end]))

print(ans)



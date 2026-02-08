n, d, k, c = map(int, input().split())
rail = []
for i in range(n):
    rail.append(int(input()))
for i in range(k):
    rail.append(rail[i])

l = [0] * (d+1)
l[c] += 1
cnt = 1

for i in range(k):
    if l[rail[i]] == 0:
        cnt += 1
    l[rail[i]] += 1

max_cnt = cnt

for i in range(n-1):
    start = rail[i]
    l[start] -= 1
    if l[start] == 0:
        cnt -= 1

    end = rail[i+k]
    if l[end] == 0:
        cnt += 1
    l[end] += 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)
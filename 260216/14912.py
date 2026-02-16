# 백준 14912번
n, d = map(int, input().split())
ans = 0

for now_num in range(1, n + 1):
    now_num_str = str(now_num)
    for each in now_num_str:
        if int(each) == d:
            ans += 1

print(ans)
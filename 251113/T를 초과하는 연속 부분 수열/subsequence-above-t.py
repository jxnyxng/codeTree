n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

stack = []

for i in range(n):
    now_num = arr[i]
    if now_num>t:
        stack.append(now_num)
    else:
        ans = max(ans, len(stack))
        while len(stack)>0: stack.pop()

print(ans)
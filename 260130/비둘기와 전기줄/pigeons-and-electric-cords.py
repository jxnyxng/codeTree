n = int(input())
arr = [[0] * 2 for _ in range(11)]
s = set()
cnt = 0

for i in range(n):
    a, b = map(int, input().split())

    if not a in s:
        arr[a] = b
        s.add(a)
    elif arr[a] != b:
        cnt+=1
        arr[a] = b

print(cnt)
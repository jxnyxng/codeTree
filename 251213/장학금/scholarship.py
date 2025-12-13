mid, fin = map(int, input().split())
ans = 0
if mid>=90:
    if fin >= 95:
        ans+=100000
    elif fin>=90:
        ans+=50000

print(ans)
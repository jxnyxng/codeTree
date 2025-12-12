l = list(map(int, input().split()))

print(1 if min(l) == l[0] else 0, 1 if l[0]==l[1]==l[2] else 0)

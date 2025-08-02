a, b = map(int, input().split())

l = [a, b]
for i in range(2,10):
    t = (l[i-1] + l[i-2])%10
    l.append(t)

for i in l:
    print(i, end=" ")
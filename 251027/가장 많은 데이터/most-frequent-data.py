n = int(input())
words = [input() for _ in range(n)]

d = dict()

for i in range(n):
    if words[i] in d:
        d[words[i]] += 1
    else:
        d[words[i]] = 1

print(max(*d.values()))
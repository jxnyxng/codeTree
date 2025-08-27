m1, d1, m2, d2 = map(int, input().split())

d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a = d1
b = d2

for i in range(m1):
    a += d[i]
for i in range(m2):
    b += d[i]

print(b-a)
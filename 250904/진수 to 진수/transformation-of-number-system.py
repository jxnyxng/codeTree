a, b = map(int, input().split())
n = input()
# a 진수인 n
# 을 b 진수로
temp = 0
for i in range(len(n)-1, -1, -1):
    temp += (int(n[i]) * (a**i))
ans = []

while temp>=b:
    ans.append(temp%b)
    temp//=b

ans.append(temp%b)
for i in ans[::-1]:
    print(i, end='')


binary = input()

ans = 0
m=2
length = len(binary)

for i in range(length-1, -1, -1):
    ans += int(binary[length-i-1]) * (m**i)

print(ans)

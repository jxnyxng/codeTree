a, b = map(int, input().split()) 

ans = str(a//b)+'.'
temp = a%b
for i in range(20):
    ans += str(temp*10//b)
    temp = temp*10%b

print(ans)

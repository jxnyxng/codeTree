X, Y = map(int, input().split())

ans=0
def dsum(i):
    t = str(i)
    t2=0
    for j in range(len(t)):
        t2+=int(t[j])
    return t2

for i in range(X, Y+1):
    t = dsum(i)
    ans = max(ans, t)

print(ans)

        

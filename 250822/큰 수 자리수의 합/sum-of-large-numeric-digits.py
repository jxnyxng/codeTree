a, b, c = map(int, input().split())

num = a*b*c

def sol(num):
    sn = str(num)
    ans = 0
    for i in sn: 
        ans += int(i)
    
    return ans

print(sol(num))

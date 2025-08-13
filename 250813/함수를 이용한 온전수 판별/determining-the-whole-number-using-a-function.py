a, b = map(int, input().split())

def sol(num):
    if num%2==0:
        return False
    elif num%10==5:
        return False
    elif num%3==0 and num%9!=0:
        return False
    else:
        return True

cnt = 0

for i in range(a, b+1):
    if sol(i):
        cnt+=1

print(cnt)


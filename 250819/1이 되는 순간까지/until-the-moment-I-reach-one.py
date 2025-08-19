N = int(input())
cnt = 0

def sol(n):
    global cnt
    if n==1:
        return
    elif n%2==0:
        cnt+=1
        return sol(n//2)
    else:
        cnt+=1
        return sol(n//3)

sol(N)
print(cnt)
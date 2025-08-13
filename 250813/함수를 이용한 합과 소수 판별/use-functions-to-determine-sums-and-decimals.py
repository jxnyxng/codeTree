a, b = map(int, input().split())

def sol(num):
    check=0
    s = str(num)
    for i in range(len(s)):
        check += int(s[i])

    if num==2:
        return True
    elif check%2==0 :
        for i in range(2, num):
            if num%i==0:
                return False
            if i==num-1:
                return True
cnt = 0

for i in range(a, b+1):
    if sol(i):
        cnt+=1

print(cnt)
        
n = int(input())

def rep(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            print(cnt, end=' ')
            if cnt==9:
                cnt=1
            else:
                cnt+=1
        print()

rep(n)
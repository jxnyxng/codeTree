a, b = map(int, input().split())
cnt = a
while cnt<=b:
    print(cnt, end=' ')
    if cnt%2!=0:
        cnt*=2
    else:
        cnt+=3
    

        
N, B = map(int, input().split())

ans = []
while True:
    if N==0:
        break
    
    ans.append(N%B)
    N//=B

for i in ans[::-1]:
    print(i,end='')



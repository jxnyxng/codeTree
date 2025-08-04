N = int(input())
cnt=0
for i in range(N):
    now = i+1
    if now%2==0 or now%3==0 or now%5==0:
        cnt+=1

print(N-cnt)    

word, a = input().split()

ans = 'No'
cnt=0

for w in word:
    if w==a:
        ans = cnt
        break
    
    cnt+=1

print(ans)
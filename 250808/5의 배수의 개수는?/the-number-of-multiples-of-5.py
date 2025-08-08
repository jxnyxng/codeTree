sum=0
for _ in range(4):
    l = list(map(int, input().split()))
    for i in range(4):
        if l[i]%5==0 :
            sum+=1
print(sum)

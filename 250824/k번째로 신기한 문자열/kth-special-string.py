n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

sorted_str = sorted(str)
cnt=0

for i in range(len(str)):
    for j in range(len(t)):
        if sorted_str[i][j]!=t[j]:
            break
        
        if j==len(t)-1:
            cnt+=1

    if cnt==k:
        print(sorted_str[i])
        break
        
        
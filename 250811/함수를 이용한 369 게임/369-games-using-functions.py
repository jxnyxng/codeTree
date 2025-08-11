a, b = map(int, input().split())

def sol(a,b):
    cnt=0
    for i  in range(a, b+1):
        if i%3==0:
            cnt+=1
            continue
        else:
            l = str(i)
            for j in range(len(l)): 
                if l[j]=='3' or l[j]=='6' or l[j]=='9':
                    cnt+=1
                    break 
    return cnt

print(sol(a,b))
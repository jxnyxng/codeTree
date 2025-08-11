a, b = map(int, input().split())

def sol(a,b):
    s=0
    for i in range(a,b+1):
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
                s+=i
                        
    return s

print(sol(a,b))
            
            
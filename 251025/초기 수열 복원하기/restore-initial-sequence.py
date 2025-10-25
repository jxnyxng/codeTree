n = int(input())
adjacent = list(map(int, input().split()))

# 1~더한 값 사이

def dupl(clist): 
    for i in range(n):
        cnum = clist[i]

        for j in range(n):
            if i == j: 
                continue 
            if clist[j] == cnum: 
                return True
     
    return False
 
def plus(clist): 
    for num in clist: 
        if num <= 0: 
            return False 
    return True
  
 
for i in range(n): 
    clist = [0] * n
    clist[0] = i + 1
     
    for j in range(1, n):
        clist[j] = adjacent[j-1] - clist[j-1]
 
    if not dupl(clist) and plus(clist):
        for num in clist:
            print(num, end=' ')
num = int(input())
cnt = 1

def check(num):
    if num%3==0:
        return True

    num = list(str(num))
    for i in num:
        if i=='3' or i=='6' or i=='9':
            return True
    
    return False

for i in range(num):
    if check(cnt):
        print(0, end=' ')
    else:
        print(cnt, end=' ')
    cnt+=1
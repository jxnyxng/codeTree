n=int(input())
num=0
temp=0

while(True):
    temp += 1
    
    if temp==100:
        break

    if num+temp >= n:
        print(temp)
        break
    else:
        num += temp
 
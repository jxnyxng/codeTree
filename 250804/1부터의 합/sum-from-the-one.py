n=int(input())
num=0
temp=0

while(True):
    if temp==100:
        break
        
    if n == num+temp:
        print(num)
        break
    else:
        temp += 1
        num += temp

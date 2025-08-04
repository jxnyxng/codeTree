t=0
f=0

for i in range(10):
    num = int(input())
    if num%3==0:
        t+=1
    
    if num%5==0:
        f+=1

print(f"{t} {f}")

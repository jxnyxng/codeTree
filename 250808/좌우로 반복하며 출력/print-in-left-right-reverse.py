num = int(input())

for i in range(num):
    if i%2==0:
        for j in range(num):
            print(j+1, end='')
    else:
        for j in range(num,0,-1):
            print(j, end='')
    print()

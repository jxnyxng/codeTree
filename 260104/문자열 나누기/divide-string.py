n = int(input())

number = ''.join(input().split())

for i in range(1, len(number)+1):
    print(number[i-1], end='')
    if i%5==0:
        print()
        
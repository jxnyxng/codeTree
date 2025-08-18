n = int(input())

def up(i):
    if i!=0:
        print(n-i+1, end=' ')
        up(i-1)

def down(i):
    if i!=0:
        print(i, end=' ')
        down(i-1)

up(n)
print()
down(n)
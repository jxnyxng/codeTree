n = int(input())
length = 0
sta = 0

for i in range(n):
    l = input()
    length+=len(l)
    if l[0]=='a':
        sta+=1

print(length, sta)
    
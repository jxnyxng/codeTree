l = []

for i in range(10):
    l.append(input())

key = input()
cnt = 0
for i in l:
    if i[-1] == key:
        cnt+=1
        print(i)
if cnt==0:
    print('None')
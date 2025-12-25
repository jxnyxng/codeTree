l = ['apple', 'banana', 'grape', 'blueberry','orange']
f = input()
cnt=0

for i in l:
    if i[2]==f or i[3]==f:
        cnt+=1
        print(i)
    

print(cnt)



a = input()
l = ['apple', 'banana', 'grape', 'blueberry', 'orange']
cnt=0

for i in range(5):
    now = l[i]
    if now[2]==a or now[3]==a:
        print(now,end='\n')
        cnt+=1
print(cnt)


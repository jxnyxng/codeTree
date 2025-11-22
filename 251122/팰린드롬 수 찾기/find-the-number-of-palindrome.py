X, Y = map(int, input().split())

cnt=0
for number in range(X, Y+1):
    new_num = str(number)[::-1]
    if str(number) == new_num:
        cnt+=1
        # print(new_num)

print(cnt)
    
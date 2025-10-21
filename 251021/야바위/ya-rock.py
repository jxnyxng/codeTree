n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

#   1 2 3 각 종이컵에 돌멩이 잇을 때 점수 확인 후 높은 거 ㄱ
def simul(select):
    p=0
    cup1, cup2, cup3 = 0, 0, 0

    if select==1: 
        cup1=1
    elif select==2:
        cup2=1
    else:
        cup3=1

    for i in range(n): 
        # 1 2 선택
        if a[i]+b[i]==3:
            temp = cup1
            cup1 = cup2
            cup2 = temp
        # 1 3 선택
        elif a[i]+b[i]==4:
            temp = cup1
            cup1 = cup3
            cup3 = temp 
        # 2 3 선택
        else:
            temp = cup3
            cup3 = cup2
            cup2 = temp

        if c[i]==1 and cup1==1:
            p+=1
        elif c[i]==2 and cup2==1:
            p+=1
        elif c[i]==3 and cup3==1:
            p+=1
    return p


ans=0
# 넣을 컵 선택
for i in range(3):
    ans = max(ans, simul(i+1))

print(ans)


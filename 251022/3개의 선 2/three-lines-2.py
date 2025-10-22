n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# 가능한 숫자 모두 변수에 저장후
# 평행한 경우 나눠서 탐색
# 하나라도 지나가면 계속 진행

answer=0
run = True
for i in range(0, 11):
    for j in range(0, 11):
        for k in range(0, 11):
            check = True 
            # x평행 3 y평행 0
            for l in range(n):
                if x[l]==i or x[l]==j or x[l]==k:
                    continue
                check=False
            if check:
                answer=1
                run = False
                break 

            check = True 
            # x평행 2 y평행 1
            for l in range(n):
                if x[l]==i or x[l]==j or y[l]==k:
                    continue
                check=False
            if check:
                answer=1
                run = False
                break 


            check = True 
            # x평행 1 y평행 2
            for l in range(n):
                if x[l]==i or y[l]==j or y[l]==k:
                    continue
                check=False
            if check:
                answer=1
                run = False
                break 


            check = True 
            # x평행 0 y평행 3
            for l in range(n):
                if y[l]==i or y[l]==j or y[l]==k:
                    continue
                check=False
            if check:
                answer=1
                run = False
                break 

        if not run:
            break
    if not run:
        break

print(answer)
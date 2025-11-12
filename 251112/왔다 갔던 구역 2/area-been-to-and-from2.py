n = int(input())
x = [] #거리
dir = [] #방향
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)
# 최대거리 10으로 100번 움직인게 최대 -> 배열 크기 2005

# 정답 배열에 +1로 방문 횟수 체크
# 영역이니까 끝점 포함 X 

arr = [0] * 2001
now = 1000 
 
for i in range(n):
    now_x = x[i]
    now_dir = dir[i]

    if now_dir == 'L':
        for j in range(now - 1, now - now_x - 1, -1):
            arr[j] += 1
        now -= now_x
    
    else:
        for j in range(now, now + now_x):
            arr[j] += 1
        now += now_x

ans = 0
for i in arr:
    if i>1:
        ans+=1

print(ans)


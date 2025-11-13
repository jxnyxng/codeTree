n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))


# 오른쪽으로 이동시키고 더이상 오른쪽에 숫자 없으면 아래칸 왼쪽
# 우하단 숫자가 템프 -> 좌상단으로 이동시키면 1초

# 각 숫자가 이동하는 함수
def shift():
    global u, d
    temp1 = u[n-1] #위
    temp2 = d[n-1] #아래

    for i in range(n):
        d[n-i-1] = d[n-i-2]
        u[n-i-1] = u[n-i-2] 
    
    d[0] = temp1 
    u[0] = temp2
         
# 템프 지정하고 함수호출
# t초동안 쉬픝
for i in range(t):
    shift()

print(*u)
print(*d)

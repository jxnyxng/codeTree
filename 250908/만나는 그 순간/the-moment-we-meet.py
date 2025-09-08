n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))
 

a_move = []
# A의 움직임
for i in range(n):
    for j in range(t[i]):
        if d[i] == 'L':
            a_move.append(-1)
        else:
            a_move.append(1)

b_move = []
# B의 움직임
for i in range(m):
    for j in range(t2[i]):
        if d2[i] == 'L':
            b_move.append(-1)
        else:
            b_move.append(1)

a_pos=0
b_pos=0
# a의 움직임과 b의 움직임 중 최소 시간만큼 시간의 흐름 제어
for t in range(min(len(a_move), len(b_move))):
    a_pos += a_move[t]
    b_pos += b_move[t]
    if a_pos == b_pos:
        print(t+1)
        break

# 시간 흐름 끝낫는데 a,b위치가 다르면 못만난것
if a_pos != b_pos:
    print(-1)
    


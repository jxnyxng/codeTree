n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# 시간 흐름에 따른 각 로봇의 위치를 각각 기록
# 위치 정보를 시간에 따라 탐색해 같은 위치인 시점 체크
# 해당 시점이 직전의 위치가 달라야 카운트, 아니면 패스

# 다른 위치에 있다가 만나야 카운트
# 만나고 같은 방향으로 가는건 카운트 노노
# 다른 방향에서 만나는 경우만 카운트
a_time = [0] * 1000005
b_time = [0] * 1000005

aidx=0
cnt=1
for i in range(n):
    nt = t[i]
    nd = d[i]
    if nd=='L': 
        for j in range(aidx-1, aidx-nt-1, -1):
            a_time[cnt] = j
            cnt+=1
        aidx = aidx - nt
    else:
        for j in range(aidx+1, aidx+nt+1):
            a_time[cnt] = j
            cnt+=1
        aidx = aidx + nt 
        
# A의 총 이동 시간 마지막 위치
total_time_a = cnt - 1
final_pos_a = aidx


# b로봇
bidx=0
cnt=1 
for i in range(m):
    nt = t_b[i]
    nd = d_b[i]
    if nd=='L': 
        for j in range(bidx-1, bidx-nt-1, -1):
            b_time[cnt] = j
            cnt+=1
        bidx = bidx - nt
    else:
        for j in range(bidx+1, bidx+nt+1):
            b_time[cnt] = j
            cnt+=1
        bidx = bidx + nt

# B의 총 이동 시간, 마지막 위치
total_time_b = cnt - 1
final_pos_b = bidx

max_time = max(total_time_a, total_time_b)

# A가 먼저 멈춤 -> B가 끝날 때까지 A는 마지막 위치
for i in range(total_time_a + 1, max_time + 1):
    a_time[i] = final_pos_a

# B가 먼저 멈춤 -> A가 끝날 때까지 B는 마지막 위치에
for i in range(total_time_b + 1, max_time + 1):
    b_time[i] = final_pos_b 
  
ans=0 
for i in range(1, max_time + 1): 
    if a_time[i] == b_time[i] and a_time[i-1] != b_time[i-1]:
        ans+=1

print(ans)
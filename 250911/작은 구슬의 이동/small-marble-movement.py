n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 상하좌우
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

# 방향 인덱스
if d == 'U':
    dir_idx = 0
elif d == 'D':
    dir_idx = 1
elif d == 'L':
    dir_idx = 2
else:
    dir_idx = 3

# 벽에 부딪혔을 때의 반대 방향 인덱스
reverse_dir = {0: 1, 1: 0, 2: 3, 3: 2}

def in_range(x, y):
    global n
    return 1 <= x <= n and 1 <= y <= n

# t초 동안 진행
for _ in range(t):
    next_r = r + dys[dir_idx]
    next_c = c + dxs[dir_idx]

    # 다음 위치 범위 확인
    if in_range(next_r, next_c):
        r, c = next_r, next_c
    else:  # 벗어나면
        dir_idx = reverse_dir[dir_idx]  # 방향변경

print(r, c)
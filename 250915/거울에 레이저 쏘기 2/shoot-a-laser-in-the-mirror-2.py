n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# 다음 이동 방향
# / : 하 -> 좌, 우 -> 상, 상 -> 우, 좌 -> 하
# \ : 하 -> 우, 좌 -> 상, 상 -> 좌, 우 -> 하
dis = [-1, 0, 1, 0] 
djs = [0, -1, 0, 1]

# 거울, 진입에 따른 방향
def reflect(mirror_type, in_dir):
    # 0:상, 1:좌, 2:하, 3:우
    if mirror_type == '/':
        # / : 상->우, 좌->하, 하->좌, 우->상 
        if in_dir == 0: return 3
        if in_dir == 1: return 2
        if in_dir == 2: return 1
        if in_dir == 3: return 0
    elif mirror_type == '\\': 
        # \ : 상->좌, 좌->상, 하->우, 우->하
        if in_dir == 0: return 1
        if in_dir == 1: return 0
        if in_dir == 2: return 3
        if in_dir == 3: return 2

# k번째 레이저
def start(k, n):
    if 1 <= k <= n:
        # 1. 위쪽 진입
        return 0, k - 1, 2
    elif n + 1 <= k <= 2 * n:
        # 2. 오른쪽 진입
        return (k - n - 1), n - 1, 1
    elif 2 * n + 1 <= k <= 3 * n:
        # 3. 아래쪽 진입
        return n - 1, n - 1 - (k - 2 * n - 1), 0
    else:
        # 4. 왼쪽 진입
        return n - 1 - (k - 3 * n - 1), 0, 3

# 그리드 범위 체크
def is_in_range(r, c, n):
    return 0 <= r < n and 0 <= c < n
  
r, c, d = start(k, n)
cnt=0
 
# 나갈때까지
while is_in_range(r, c, n): 
    cnt += 1 
    mirror = grid[r][c] 
    # 반사
    d = reflect(mirror, d)
     
    r += dis[d]
    c += djs[d]
 
print(cnt)
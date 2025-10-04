n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 첫 번째 블록 회전시 다음 위치
# -> 1. 하우  2. 하좌  3. 우하  4. 좌하 
dx = [0, 1, 0, -1, 1, 0, -1, 0] #열
dy = [1, 0, 1, 0, 0, 1, 0, 1] #행

# 두번째 블록 회전시 다음 위치
# -> 1. 우우우  2. 하하하
dx2 = [1, 1, 0, 0]#열
dy2 = [0, 0, 1, 1]#행

# 레인지체크
def in_range(i, j):
    return 0<=i<n and 0<=j<m

# 특정 시작지점에 대해 블록의 모든 경우를 적용한 뒤 나올 수 잇는 최댓값을 반환하는 함수
# 시작위치의 숫자가 기본값, 이동한 곳의 숫자를 더해주며 계산
def max_result(i, j):
    renum=0
    # 첫번째 블록
    for a in range(0, 8, 2):
        cnt=grid[i][j]
        ni, nj = i, j
        is_ended=True
        for b in range(a, a+2): 
            ni += dy[b]
            nj += dx[b]
            if not(in_range(ni,nj)):
                is_ended=False
                break
            cnt+=grid[ni][nj]
        if is_ended:    
            renum = max(renum, cnt)
    
    # 두번째블록
    for a in range(0, 4, 2):
        cnt=grid[i][j]
        ni, nj = i, j
        is_ended=True
        for b in range(a, a+2): 
            ni += dy2[b]
            nj += dx2[b]
            if not(in_range(ni,nj)):
                is_ended=False
                break
            cnt+=grid[ni][nj]
        if is_ended:
            renum = max(renum, cnt)
    
    return renum
ans=0
# 모든 숫자를 시작지점으로 설정해서 dx dy 두개씩 끊어 (해당 시작점에서의 4개의 경우) 최댓값만 저장 
# 같은 방식으로 dx2 dy2를 세개씩 끊어 당 시작점에서의 케이스 2개를 탐색하고 최댓값잇으면 변경 
for i in range(n):
    for j in range(m):
        # 첫번째 블록을 지정했을 때 구할 수 있는 모든 케이스 중 최댓값 저장
        ans = max(ans, max_result(i,j)) 
        
print(ans)
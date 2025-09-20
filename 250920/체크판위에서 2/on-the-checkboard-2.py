R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# 출발자와 도착지 색깔이 같으면 0
# 출발지의 행과 열 다음에서 출발지와 다른 색깔 찾기
# 다음 행과 열에서 도착지와 다른 색깔 찾기

def find_next(i, j):
    cnt = 0
    for a in range(i+1, R-1):
        for b in range(j+1, C-1):
            if grid[a][b] != end:
                cnt+=1
    return cnt

start = grid[0][0]
end = grid[R-1][C-1]

if start==end:
    print(0)
else:
    ans = 0
    for i in range(1, R-1):
        for  j in range(1, C-1):
            # 주어진 위치가 start와 다른지 확인
            if grid[i][j] != start:
                # 해당 위치와 엔드 사이에서 엔드와 다른 지점 개수를 반환
                ans += find_next(i, j)

    print(ans)

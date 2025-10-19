k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# 가능한 a, b를 모두 탐색
# 탐색 중 모순 발견하면 다음 조합으로 

# 순위 확인해서 앞에 있으면 트루 반환하는 함수
def check_l(i, a, b):
    for j in range(n):
        if arr[i][j] == a:
            pos = j
        elif arr[i][j] == b:
            pos2 = j
    
    if pos>pos2:
        return True
    else:
        return False
    
ans = 0
# 가능한 a b 
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            continue 

        # 주어진 모든 순위를 검사
        for i in range(k):
            if not check_l(i, a, b):
                break
                
            if i==k-1:
                ans+=1
    
print(ans)
                
            
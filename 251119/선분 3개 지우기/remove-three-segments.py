n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

ans=0
# 완탐
# 선분 세개 고르는 경우
# 선분 1
for i in range(n):
# 선분 2
    for j in range(i+1, n):
# 선분 3
        for k in range(j+1, n):
            arr = [0] * 105
# 탐색
            for idx in range(n):
                if idx==i or idx==j or idx==k:
                    continue
                else:
                    for idx2 in range(l[idx], r[idx]+1):
                        arr[idx2] += 1
            t = True
            for point in arr:
                if point>1:
                    t =False
                    break
            if t:
                ans+=1
                
print(ans)
                    
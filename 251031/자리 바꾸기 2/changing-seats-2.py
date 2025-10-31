n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

# 1부터 n까지 숫자들 자리 바꾸기
# 방문한 자리의 개수를 출력

# 현재 위치를 기록할 딕셔너리
# 1 2 3 4 5
# 1 2 3 4 5
d1 = dict()
for i in range(1, n+1):
    d1[i] = i
# 방문햇던 위치들을 세트로 저장하는 딕셔너리
# 1  2  3  4  5
# [1]  [2]  [3]  4  5
d2 = dict()
for i in range(1, n+1):
    d2[i] = set([i])

for _ in range(3):
    for idx1, idx2 in edges:
        # 현재 위치에 잇는 숫자가 옮길 위치를 방문한 적잇는지
        d2[d1[idx1]].add(idx2)
        d2[d1[idx2]].add(idx1)
        
        d1[idx2], d1[idx1] = d1[idx1], d1[idx2]

for key in d2: 
    print(len(d2[key]))
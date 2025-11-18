n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# 탐색 중 주어진 구간에서는 temp에 저장하지 맣고 패스
# 탐색 1회 진행하는 함수
def sol(st, ed):
    global blocks
    temp = []
    for i in range(len(blocks)):
        if not(i>=st and i<ed):
            temp.append(blocks[i])

    blocks[:] = temp
    
sol(s1-1,e1)
sol(s2-1,e2)
print(len(blocks))
for i in range(len(blocks)):
    print(blocks[i])
from itertools import permutations
    
N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

ans = 0

# 쿠폰 적용할 선물 고르기
for i in range(N):
    nprice = P[:]
    nprice[i] //= 2
    price = 0
    # 가능한 선물 조합
    for j in range(1, N+1):
        for newP in permutations(nprice, j):
            if sum(newP)<=B:
                ans = j
                break

print(ans)
# 백준 1166번

N, L, W, H = map(int, input().split())
S, E = 0, max(L, W, H)

for idx in range(10000):
    M = (S+E) / 2
    count = (L//M) * (W//M) * (H//M)
    
    if count >= N:
        S = M
    else:
        E = M

print("%.10f" %(E))
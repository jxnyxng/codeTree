S, Q = map(str, input().split())
Q = int(Q)
for _ in range(Q):
    qu, idx1, idx2 = map(str, input().split())
    
    if int(qu) == 1:
        idx1 = int(idx1) - 1
        idx2 = int(idx2) - 1
        S = S[:idx1] + S[idx2] + S[idx1+1:idx2] + S[idx1] + S[idx2+1:]
        print(S)
    else:
        x = idx1
        y = idx2
        S = S.replace(x, y)
        print(S)
    
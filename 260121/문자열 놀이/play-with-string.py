S, Q = map(str, input().split())
Q = int(Q)
for _ in range(Q):
    qu, idx1, idx2 = map(str, input().split())
    
    if int(qu) == 1:
        S = list(S)  
        temp = S[int(idx1) - 1]
        S[int(idx1) - 1] = S[int(idx2) - 1]
        S[int(idx2) - 1] = temp
        S = ''.join(S)
        print(S)
    else:
        x = idx1
        y = idx2
        S = S.replace(x, y)
        print(S)
    
N = int(input())
V = list(map(int, input().split()))

def solve(arr):
    n = len(arr)
    S = [0] * (n + 1)
    
    for i in range(n): 
        S[i+1] = S[i] + arr[i]
    
    dp = [[0]*n for _ in range(n)]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if i == j:
                dp[i][j] = arr[i]
                continue
            
            tot = S[j+1] - S[i]
            min_val = float('inf')
            
            for k in range(i, j + 1):
                left = dp[i][k-1] if k > i else 0
                right = dp[k+1][j] if k < j else 0
                min_val = min(min_val, left + right)
            
            dp[i][j] = tot - min_val
            
    return dp[0][n-1]

ans = 0
for i in range(N):
    rem = V[i+1:] + V[:i]
    opp = solve(rem)
    ans = max(ans, V[i] + sum(rem) - opp)

print(ans)
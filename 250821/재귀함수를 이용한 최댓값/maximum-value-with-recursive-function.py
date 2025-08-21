n = int(input())
arr = list(map(int, input().split()))

def sol(num, ans):
    if num==n:
        return ans
    else:
        return sol(num+1, max(arr[num], ans))

print(sol(1, arr[0]))

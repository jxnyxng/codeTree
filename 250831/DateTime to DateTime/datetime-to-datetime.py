a, b, c = map(int, input().split())

day_to_m = 60*24
hour_to_m = 60

ori = 11*day_to_m + 11*hour_to_m + 11
ttt = a*day_to_m + b*hour_to_m + c

ans = (ttt - ori)
if ans<0:
    ans = -1
        
print(ans)

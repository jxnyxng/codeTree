n, m, d, s = map(int, input().split()) 
eat_log = [tuple(map(int, input().split())) for _ in range(d)]
sick_log = [tuple(map(int, input().split())) for _ in range(s)]

ans = 0

for i in range(1, m + 1): 
    eat_time = [0] * (n + 1)
    for p, cheese, t in eat_log:
        if cheese == i:
            if eat_time[p] == 0 or t < eat_time[p]:
                eat_time[p] = t

    possible = True
    for p, sick_t in sick_log: 
        if eat_time[p] == 0 or eat_time[p] >= sick_t:
            possible = False
            break 

    if possible:
        pill_count = 0
        for t in eat_time: 
            if t > 0:
                pill_count += 1
        ans = max(ans, pill_count)

print(ans)
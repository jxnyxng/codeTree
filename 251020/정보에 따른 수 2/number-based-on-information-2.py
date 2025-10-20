T, a, b = map(int, input().split())
line = [''] * 1001
for _ in range(T):
    char, pos = input().split()
    line[int(pos)] = char

s_pos = []
n_pos = []
for i, char in enumerate(line):
    if char == 'S':
        s_pos.append(i)
    elif char == 'N':
        n_pos.append(i)

def find_dist(p, positions):
    min_d = float('inf')
    for pos in positions:
        min_d = min(min_d, abs(p - pos))
    return min_d

ans = 0
for i in range(a, b + 1):
    dist_s = find_dist(i, s_pos)
    dist_n = find_dist(i, n_pos)
    
    if dist_s <= dist_n:
        ans += 1

print(ans)
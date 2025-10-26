N = int(input())
h = [int(input()) for _ in range(N)]

if N == 0:
    print(0)
    exit()

mn, mx = min(h), max(h)

if mx - mn <= 17:
    print(0)
    exit()

def calc_cost(add, sub):
    new_min = mn + add
    new_max = mx - sub
    cost = 0
    for val in h:
        if val < new_min:
            cost += (new_min - val) ** 2
        elif val > new_max:
            cost += (val - new_max) ** 2
    return cost

adj = mx-mn-17 
min_cost = float('inf') 

for i in range(adj + 1):
    min_cost = min(min_cost, calc_cost(i, adj - i))

print(min_cost)
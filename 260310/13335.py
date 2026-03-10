# 백준 13335번

n, w, l = map(int, input().split())
q = list(map(int, input().split()))
bridge = [0] * w
time = 0

while bridge:
	time += 1
	bridge.pop(0)
    
	if q:
		if sum(bridge) + q[0] <= l:
			bridge.append(q.pop(0))
		else:
			bridge.append(0)
			
print(time)
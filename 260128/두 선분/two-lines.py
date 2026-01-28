x1, x2, x3, x4 = map(int, input().split())

arr = [0] * 105

for i in range(x1, x2+1):
    arr[i] += 1

for i in range(x3, x4+1):
    arr[i] += 1

for now in arr:
    if now==2:
        print("intersecting")
        exit()

print("nonintersecting")

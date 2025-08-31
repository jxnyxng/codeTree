n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

class S:
    def __init__(self, h, w, idx):
        self.h = h
        self.w = w
        self.idx = idx

arr = []
for i in range(n):
    arr.append(S(students[i][0], students[i][1], students[i][2]))

arr.sort(key=lambda x:(x.h -x.w))

for i in arr:
    print(i.h, i.w, i.idx)

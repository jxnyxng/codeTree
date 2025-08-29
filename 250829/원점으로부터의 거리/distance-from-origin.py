n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]


class A:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.pita = (abs(x) + abs(y))

answer = []
for i in range(n):
    answer.append(A(points[i][1][0], points[i][1][1], points[i][0]+1))

answer.sort(key=lambda x:(x.pita, x.idx))
for i in answer:
    print(i.idx)
 

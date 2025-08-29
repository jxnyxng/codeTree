n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))


class A:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
answer = []

for i in range(n):
    answer.append(A(name[i], height[i], weight[i]))

answer.sort(key=lambda x:(x.height, -x.weight))

for i in answer:
    print(i.name, i.height, i.weight)
    
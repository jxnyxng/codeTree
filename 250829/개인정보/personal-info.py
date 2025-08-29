n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))


class S:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

answer_n = []
answer_h = []

for i in range(len(name)):
    answer_n.append(S(name[i], height[i], weight[i]))
    answer_h.append(S(name[i], height[i], weight[i]))

answer_n.sort(key=lambda x:x.name)
answer_h.sort(key=lambda x:-x.height)

print('name')
for i in answer_n:
    print(i.name, i.height, i.weight)
print()
print('height') 
for i in answer_h:
    print(i.name, i.height, i.weight)


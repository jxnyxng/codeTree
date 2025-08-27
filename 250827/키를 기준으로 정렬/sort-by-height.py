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
        self.name=name
        self.height=height
        self.weight=weight

students = []
for i in range(n): 
    students.append(A(name[i], height[i], weight[i]))

students.sort(key=lambda x:x.height)

for st in students: 
    print(st.name, st.height, st.weight)
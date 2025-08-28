n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

class S:
    def __init__(self, idx, h, w):
        self.idx = idx
        self.h = h
        self.w = w

st = []
for i in range(n):
    h = students[i][0]
    w = students[i][1]
    st.append(S(i+1, h, w))

st.sort(key=lambda x:(-x.h, -x.w, x.idx))

for i in st:
    print(i.h, i.w, i.idx)
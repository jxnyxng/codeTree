n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

class Rank:
    def __init__(self, n, s1, s2, s3):
        self.n = n
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

st = []

for i in range(n):
    r = Rank(name[i], score1[i], score2[i], score3[i])
    st.append(r)

st.sort(key=lambda x:x.s1 + x.s2 + x.s3)
for i in st:
    print(i.n, i.s1, i.s2, i.s3)
    
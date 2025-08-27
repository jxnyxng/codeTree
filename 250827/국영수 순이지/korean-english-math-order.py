n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

class A:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

students = []
for i in range(n):
    students.append(A(name[i], korean[i], english[i], math[i]))

students.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for i in students:
    print(i.name, i.kor, i.eng, i.math)


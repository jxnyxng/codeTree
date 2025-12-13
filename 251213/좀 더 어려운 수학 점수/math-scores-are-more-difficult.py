A_math, A_eng = map(int, input().split())
B_math, B_eng = map(int, input().split())

student = [('A', A_math, A_eng), ('B', B_math, B_eng)]
student.sort(key = lambda x : (-x[1], -x[2]))
print(student[0][0])
grade = ["A", "B", "C", "D", "F", "A"]
p = int(input())
idx = 9 - (p//10)
if idx>4:
    idx = 4

print(grade[idx])
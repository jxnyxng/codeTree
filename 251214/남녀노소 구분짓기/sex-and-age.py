li = ['BOY', 'GIRL', 'MAN', 'WOMAN']

gender_idx = int(input())
age = int(input())

if age>=19:
    gender_idx+=2

print(li[gender_idx])

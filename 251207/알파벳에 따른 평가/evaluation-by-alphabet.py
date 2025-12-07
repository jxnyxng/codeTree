d = {'S' : 'Superior', 'A' : 'Excellent', 'B' : 'Good', 'C' : 'Usually', 'D' : 'Effort'}

i = input()
if i in d:
    print(d[i])
else:
    print('Failure')

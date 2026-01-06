a = input()
ee_res = 'No'
ab_res = 'No'

for i in range(1, len(a)):
    if a[i-1]+a[i] == 'ee':
        ee_res = 'Yes'
    elif a[i-1]+a[i] == 'ab':
        ab_res = 'Yes'


print(ee_res, ab_res)
    
    
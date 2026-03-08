# 백준 1918번

inl = input()
keep = []
op1 = ['+', '-']
op2 = ['*', '/']
ans = ''

for now in inl:
    if now == '(':
        keep.append('(')
    elif now == ')':
        while keep and keep[-1] != '(':
            ans += keep.pop()
        keep.pop()
    elif now in op2:
        while keep and (1 if keep[-1] in op2 else 0):
            ans += keep.pop()
        keep.append(now)
    elif now in op1:
        while keep and keep[-1] != '(':
            ans+= keep.pop()
        keep.append(now)
    else:
        ans += now

while keep:
    ans += keep.pop()

print(ans)    
        
        
    
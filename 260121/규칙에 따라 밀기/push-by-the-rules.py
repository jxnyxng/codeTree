word = input()
commands = list(input())

def SL(word):
    return word[1:] + word[0]

def SR(word):
    return word[-1] + word[:-1]

ans=word
for now_c in commands:
    if now_c == 'L':
        ans = SL(ans)
    else:
        ans = SR(ans)

print(ans)
        
    


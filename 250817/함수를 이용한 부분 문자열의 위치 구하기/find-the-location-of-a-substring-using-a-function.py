text = input()
pattern = input()

def sol():
    for i in range(len(text)-len(pattern)+1):
        if text[i]==pattern[0]:
            if check(i):
                ans = i
                return i
    return -1 

def check(i):
    for j in range(i,i+len(pattern)):
        if text[j]!=pattern[j-i]:
            return False
    return True

answer = sol()

print(answer)
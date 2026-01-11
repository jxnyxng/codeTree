line = input()

ans = line[:1] + 'a' + line[2:len(line)-2] + 'a' + line[len(line)-1:]
print(ans)
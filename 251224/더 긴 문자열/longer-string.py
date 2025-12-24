a, b = input().split(" ")

print(f"{a} {len(a)}" if len(a)>len(b) else f"{b} {len(b)}" if len(b)>len(a) else 'same')
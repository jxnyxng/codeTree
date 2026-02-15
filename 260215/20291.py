# 백준 20291번
n = int(input())
file_types = {}

for _ in range(n):
    file_name = input().strip()
    ext = file_name.split('.')[-1]
    
    if ext in file_types:
        file_types[ext] += 1
    else:
        file_types[ext] = 1

for ext, count in sorted(file_types.items()):
    print(f"{ext} {count}")
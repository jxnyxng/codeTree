# 백준 1747
import math

N = int(input())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

while True:
    if is_prime(N) and is_palindrome(N):
        print(N)
        break
    N += 1

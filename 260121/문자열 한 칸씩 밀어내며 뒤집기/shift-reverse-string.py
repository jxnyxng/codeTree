word, q = input().split()
now_word = word


def shift_to_L(word):
    return word[1:] + word[0]

def shift_to_R(word):
    return word[-1] + word[:-1]

def reverse(word):
    return word[::-1]

for i in range(int(q)):
    command = int(input())
    if command == 1:
        now_word = shift_to_L(now_word)
    elif command == 2:
        now_word = shift_to_R(now_word)
    else:
        now_word = reverse(now_word)
    print(now_word)
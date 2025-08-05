while(True):
    guess = int(input())
    if guess==25:
        print('Good')
        break
    elif guess>25:
        print('Lower')
    else:
        print('Higher')
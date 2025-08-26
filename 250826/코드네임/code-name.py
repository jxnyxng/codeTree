MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class L:
    def __init__(self, codenames, scores):
        self.codenames = codenames
        self.scores = scores

        m=101
        mn=''

        for i in self.scores:
            m = min(m, i)
        
        for j in range(5):
            if m == self.scores[j]:
                mn = self.codenames[j]
        print(mn, m)

finder = L(codenames, scores)
            


import random

char1 = ["F", "R", "U"]
char2 = ["B", "L", "D"]
suffix = ["'", "2", ""]

def getScramble(length):
    combined = []
    old = ""
    new = ""
    for _ in range(length):
        i = _ % 2
        if i:
            while old == new: new = random.randint(0, 2)
            combined.append(char1[new] + random.choice(suffix))
            old = new
        else:
            while old == new: new = random.randint(0, 2)
            combined.append(char2[new] + random.choice(suffix))
            old = new
    return(' '.join(combined))

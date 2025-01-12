import random

numStreaks = 0

for experiment in range(10000):
    endList = []
    streak = 0
    for flips in range(100):
        endList.append(random.randint(0, 1))
    #print(endList)
    for i in range(1, len(endList)):
        streakPresent = False 
        if endList[i] == endList[i-1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numStreaks += 1
            break
    endList = []
print("Chance of streak [SIMULATION]: %s%%" % (numStreaks / 100))
print("Chance of streak [MATH] %s%%" % ((1/2)**6 * 100))
    
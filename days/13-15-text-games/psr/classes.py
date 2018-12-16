from collections import defaultdict

# This is the most basic version
winData = {
    "paper" : ["rock"],
    "rock" : ["scissors"],
    "scissors" : ["paper"],
}

winData = defaultdict(list,winData)
loseData = defaultdict(list)

for key1 in winData.keys():
    for key2 in winData.keys():
        if key1 == key2:
            pass
        else:
            if key1 in winData[key2]:
                loseData[key1].append(key2)

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0

class Roll():
    def __init__(self, name):
        self.name = name
        self.winAgainst = winData[name]
        self.loseAgainst = loseData[name]
    def winsTo(self, roll):
        return roll.name in self.winAgainst
    def losesTo(self, roll):
        return roll.name in self.loseAgainst

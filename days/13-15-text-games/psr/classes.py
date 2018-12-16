from collections import defaultdict

# This is the most basic version
winData = {
    "paper" : ["rock"],
    "rock" : ["scissors"],
    "scissors" : ["paper"],
}

loseData = {
    "scissors" : ["rock"],
    "paper" : ["scissors"],
    "rock" : ["paper"],
}


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

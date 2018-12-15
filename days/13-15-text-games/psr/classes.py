from collections import defaultdict

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

class Roll():
    def __init__(self, name):
        self.name = name
        self.winsAgainst = winData[name]
        self.loseAgainst = loseData[name]

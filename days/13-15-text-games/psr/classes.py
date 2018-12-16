import csv
from collections import defaultdict
winData = defaultdict(list) 

with open('../data/battle-table.csv') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        for key in row.keys():
            if row[key]=='win':
                winData[row['Attacker']].append(key)


# This is the most basic version
# winData = {
#     "paper" : ["rock"],
#     "rock" : ["scissors"],
#     "scissors" : ["paper"],
# }

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0

class Roll():
    def __init__(self, name):
        self.name = name
        self.winAgainst = winData[name]
    def winsTo(self, roll):
        return roll.name in self.winAgainst
    def losesTo(self, roll):
        return not ((roll.name in self.winAgainst) or self.name == roll.name)

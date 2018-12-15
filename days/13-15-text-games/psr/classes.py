class Player():
    def __init__(self, name):
        self.name = name

class Hand():
    def __init__(self, handName):
        self.handName = handName
    def handCompare(self, hand):
        if self.handName == "rock" and hand.handName == "rock":
            return "Draw"
        if self.handName == "rock" and hand.handName == "paper":
            return "Lose"
        if self.handName == "rock" and hand.handName == "scissors":
            return "Win"
        if self.handName == "paper" and hand.handName == "rock":
            return "Win"
        if self.handName == "paper" and hand.handName == "paper":
            return "Draw"
        if self.handName == "paper" and hand.handName == "scissors":
            return "Lose"
        if self.handName == "scissors" and hand.handName == "rock":
            return "Lose"
        if self.handName == "scissors" and hand.handName == "paper":
            return "Win"
        if self.handName == "scissors" and hand.handName == "scissors":
            return "Draw"

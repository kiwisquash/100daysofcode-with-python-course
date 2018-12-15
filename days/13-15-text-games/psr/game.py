from classes import Player, Hand
import random

dataSet = [
    "rock",
    "paper",
    "scissors",
]

def getPlayerName():
    return input("Hi, what is your name? ")

def gameBanner():
    lines = 20*"-"
    message = "Welcome to Paper, Scissors, Rock."
    print(lines)
    print(message)
    print(lines)

def pickPlayerHand():
    return input("Pick your hand: rock, paper, or scissors: ")

def main():
    gameBanner()
    playerName = getPlayerName()
    you = Player(playerName)
    enemy = Player("Computer")
    i = 0
    while (i < 3):
        yourHand = Hand(pickPlayerHand())
        computerHand = Hand(random.choice(dataSet))
        print(f"You played {yourHand.handName}.",end=" ")
        print(f"The {enemy.name} played {computerHand.handName}.")
        print(f"You {yourHand.handCompare(computerHand).lower()}")
        i += 1

if __name__ == "__main__":
    main()
    print("Good game!")

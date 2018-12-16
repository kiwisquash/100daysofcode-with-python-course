from classes import Player, Roll
import random

def getPlayerName():
    return input("Hi, what is your name? ")

def gameBanner():
    lines = 40*"-"
    message = "Welcome to Ki's Paper, Scissors, Rock."
    print(lines)
    print(message)
    print(lines)

def buildRolls():
    return [
        Roll("paper"),
        Roll("rock"),
        Roll("scissors"),
    ]

def pickPlayerHand():
    return input("Pick your hand: rock, paper, or scissors: ")

def gameLoop(player1, player2, rolls):
    i = 0
    while (i < 3):
        p1_roll = Roll(pickPlayerHand())
        p2_roll = random.choice(rolls)
        if p1_roll.winsTo(p2_roll):
            player1.score +=1
            print(f"Your {p1_roll.name} beats {player2.name}'s {p2_roll.name}.")
        elif p1_roll.losesTo(p2_roll):
            player2.score +=1
            print(f"Your {p1_roll.name} loses to {player2.name}'s {p2_roll.name}.")
        else:
            if p1_roll.name == p2_roll.name:
                print(f"You both played {p1_roll.name}. No points awared!")
        i += 1
    if player1.score > player2.score:
        print(f"The winner is {player1.name}!")
    elif player1.score < player2.score:
        print(f"The winner is {player2.name}!")
    else:
        print(f"""Both {player1.name} and {player2.name} have {player1.score}
              wins""")

def main():
    gameBanner()

    rolls = buildRolls()
    playerName = getPlayerName()

    player1 = Player(playerName)
    player2 = Player("the computer")

    gameLoop(player1, player2, rolls)

if __name__ == "__main__":
    while True:
        main()
        print("Good game!")
        replay = input("Do you want to play again? ")
        if replay == "no":
            print("Have a nice day!")
            break

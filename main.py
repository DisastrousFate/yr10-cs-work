import random

playerName1 = input("Enter player 1 name")
playerName2 = input("Enter player 2 name")

playerScore1 = 0
playerScore2 = 0

def game():
    playerScore1 = 0
    playerScore2 = 0

    print("It's player 1's turn! ")
    print(rollDice(playerName1))

def isEven(num):
    if(num % 2 ) == 0:
        return True
    else:
        return False


def rollDice(plrName):
    input("Press Enter to roll first dice...")

    roll1 = random.choice([1,2,3,4,5,6])
    print("You rolled a " + str(roll1))
    
    input("Press Enter to roll second dice...")
    
    roll2 = random.choice([1,2,3,4,5,6])
    print("You rolled a " + str(roll2))
    
    return roll1, roll2


game()
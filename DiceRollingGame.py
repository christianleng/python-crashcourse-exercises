import random

# range (start, stop, step)


def GenerateRandomNumber():
    print(f"({random.randint(1, 6)}, {random.randint(1, 6)})")


def DiceRollingGame():
    while True:
        GenerateRandomNumber()
        ShouldRollAgain = input("Roll the dice? (y/n): ")
        if ShouldRollAgain.lower() == "y":
            DiceRollingGame()
        else:
            break
        break


DiceRollingGame()

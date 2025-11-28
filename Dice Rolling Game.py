import random

# range (start, stop, step)


def GenerateRandomNumber():
    for x in range(1):
        print(f"({random.randint(1, 6)}, {random.randint(1, 6)})")


def DiceRollingGame(offset):
    while offset != 0:
        GenerateRandomNumber()
        ShouldRollAgain = input("Roll the dice? (y/n): ")
        if ShouldRollAgain.lower() == "y":
            DiceRollingGame()
        else:
            break


DiceRollingGame(2)

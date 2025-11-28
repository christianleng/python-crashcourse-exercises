import random


def GenerateRandomNumber():
    return random.randint(1, 100)


def NumberGuessingGame():
    countAttempts = 1
    correctNumber = GenerateRandomNumber()
    attemptNumber = 0
    print(f"correctNumber ::=> {correctNumber}")

    while correctNumber != attemptNumber:
        attemptNumber = input("Guess the number (between 1 and 100): ")
        print(f"attemptNumber {attemptNumber}")
        if int(attemptNumber) < correctNumber:
            print("Too low! Try again.")
        elif int(attemptNumber) > correctNumber:
            print("Too high! Try again.")
        elif int(attemptNumber) == correctNumber:
            break

        countAttempts += 1

    print(
        f"Congratulations! You guessed the number in {countAttempts} attempts.")


NumberGuessingGame()

import random
from typing import Literal

ROOK_PAPER_SCISSORS = Literal["rock", "paper", "scissors"]

ICON_ROOK_PAPER_SCISSORS = {
    "rock": "🪨",
    "paper": "📝",
    "scissors": "✂️",
}

INPUT_MAP = {
    "r": "rock",
    "p": "paper",
    "s": "scissors",
}


def generateRandomIconGame() -> str:
    return random.choice(["rock", "paper", "scissors"])


def userChoice() -> ROOK_PAPER_SCISSORS:
    choice = input("Rock, paper, or scissors? (r/p/s):").lower()

    if choice not in INPUT_MAP:
        print("choice the correct answer")
        return userChoice()

    return INPUT_MAP[choice]


def getIcon(props) -> str:
    return ICON_ROOK_PAPER_SCISSORS[props]


def defineWinnerOrLoser(computer: str, user: str) -> str:
    if computer == user:
        return "Draw"

    winners = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if winners[user] == computer:
        return "win"
    else:
        return "lose"


def playRookPaperScissors() -> str:
    answer = userChoice()
    computer_move = generateRandomIconGame()

    iconComputer = getIcon(computer_move)
    iconUser = ICON_ROOK_PAPER_SCISSORS[answer]

    result = defineWinnerOrLoser(computer_move, answer)

    print(f"You chose {iconUser}")
    print(f"Computer chose {iconComputer}")
    print(f"You {result}")

    playGain = input("Continue? (y/n):").lower()
    return playGain == 'y'


def main() -> None:
    while playRookPaperScissors():
        pass


main()

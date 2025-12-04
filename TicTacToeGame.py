boards = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


def print_board(rows: list[list[str]]) -> None:
    horizontal = "---+---+---"
    for i in range(3):
        print(horizontal)
        line = ""
        for j in range(3):
            line += " " + rows[i][j] + " "
            if j != 2:
                line += "|"
        print(line)
    print(horizontal)


def check_winner(boards: list[list[str]]) -> None | bool:
    for i in range(3):
        if boards[i][0] == boards[i][1] == boards[i][2] != " ":
            return True

    for j in range(3):
        if boards[0][j] == boards[1][j] == boards[2][j] != " ":
            return True

    for k in range(3):
        if boards[0][0] == boards[1][1] == boards[2][2] != " ":
            return True

    for d in range(3):
        if boards[0][2] == boards[1][1] == boards[2][0] != " ":
            return True

    return None


current_player = "X"


def check_draw(boards: list[list[str]]) -> bool:
    for i in range(3):
        for j in range(3):
            if boards[i][j] == " ":
                return False
    return True


while True:
    print(f"Player {current_player}'s turn")
    row = int(input("Enter row (0-2): "))
    column = int(input("Enter column (0-2): "))

    if boards[row][column] != " ":
        print("Already take")
        continue

    boards[row][column] = current_player

    print_board(boards)

    has_winner = check_winner(boards)
    has_no_winner = check_draw(boards)

    if has_winner != None:
        print(f"WINNER : {current_player}")
        break

    if has_no_winner:
        print(f"DRAW !")
        break

    current_player = "O" if current_player == "X" else "X"

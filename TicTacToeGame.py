board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


def print_board(rows: list[list[str]]):
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


current_player = "X"


def check_winner():
    global current_player

    print(f"Player {current_player}'s turn")
    row = int(input("Enter row (0-2): "))
    column = int(input("Enter column (0-2): "))

    if board[row][column] != " ":
        print("Already")
        return

    board[row][column] = current_player

    print_board(board)


check_winner()

from termcolor import colored

PLAYER_X = "X"
PLAYER_O = "O"


def create_empty_board():
    return [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]


def display_current_player(current_player):
    print(f"Player {current_player}'s turn")


def switch_player(current_player):
    return PLAYER_O if current_player == PLAYER_X else PLAYER_X


def is_board_full(game_board):
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if game_board[row][col] == "":
                return False

    return True


def cell(mark):
    if mark == "":
        return " "

    color = "red" if mark == PLAYER_X else "green"
    return colored(mark, color)


def print_board(game_board):
    line = "---+---+---"
    print(line)
    for row in game_board:
        print(f" {cell(row[0])} | {cell(row[1])} | {cell(row[2])} ")
        print(line)


def insert(coordinate_name):
    while True:
        try:
            coordinate = int(input(f"Enter {coordinate_name} (0-2): "))

            if 0 <= coordinate <= 2:
                return coordinate
            else:
                print("Invalid input!")

        except ValueError:
            print("Invalid input!")


def update_board(game_board, row, col, current_player):
    game_board[row][col] = current_player


def check_winner(game_board):
    # Check rows
    for row in game_board:
        if row[0] == row[1] == row[2] != "":
            return True

    # Check columns
    for column in range(3):
        if game_board[0][column] == game_board[1][column] == game_board[2][column] != "":
            return True

    # Check diagonals
    if (
        game_board[0][0] == game_board[1][1] == game_board[2][2] != ""
        or
        game_board[0][2] == game_board[1][1] == game_board[2][0] != ""
    ):
        return True

    return False


def get_move():
    row = insert("row")
    col = insert("col")
    return row, col


def announce_turn(game_board, current_player):
    print_board(game_board)
    display_current_player(current_player)


def handle_taken_spot(game_board):
    print("This spot is already taken")
    print_board(game_board)


def process_game_end(game_board, current_player):
    """Check for a win or draw after a move. Returns True if the game is over."""
    if check_winner(game_board):
        print_board(game_board)
        print(f"Player {current_player} wins!")
        return True

    if is_board_full(game_board):
        print_board(game_board)
        print("The board is full!")
        return True

    return False


def main():
    game_board = create_empty_board()
    current_player = PLAYER_X

    announce_turn(game_board, current_player)

    while True:
        # 1. Input
        row, col = get_move()

        # 2. Validate move
        if game_board[row][col] != "":
            handle_taken_spot(game_board)
            continue

        # 3. Place move
        update_board(game_board, row, col, current_player)

        # 4. Check winner / draw
        if process_game_end(game_board, current_player):
            break

        # 5. Switch player and show next turn
        current_player = switch_player(current_player)
        announce_turn(game_board, current_player)


if __name__ == "__main__":
    main()

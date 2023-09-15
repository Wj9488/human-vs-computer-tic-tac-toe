def print_board(board):
    for row in board:
        print(" | ".join(row))


def check_winner(board, symbol):
    for row in board:
        if all([s == symbol for s in row]):
            return True
    for col in range(3):
        if all([board[row][col] == symbol for row in range(3)]):
            return True
    if all([board[i][i] == symbol for i in range(3)]) or \
            all([board[i][2 - i] == symbol for i in range(3)]):
        return True
    return False


def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells


def minimax(board, depth, maximizing):
    if check_winner(board, "X"):
        return -10 + depth
    if check_winner(board, "O"):
        return 10 - depth
    if not get_empty_cells(board):
        return 0

    if maximizing:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, False)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, True)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
        return min_eval


def find_best_move(board):
    best_value = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = "O"
        move_value = minimax(board, 0, False)
        board[i][j] = " "
        if move_value > best_value:
            best_move = (i, j)
            best_value = move_value

    return best_move


def main():
    player_name = input("Enter your name: ")
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("")
    print(f"Welcome to Tic-Tac-Toe, {player_name}.")
    print("")
    while True:
        print_board(board)
        print("")
        row = input("Enter the row (0, 1, 2) or 'q' to quit or 'r' to restart: ")

        if row == 'q':
            print("Thanks for playing.")
            break
        if row == 'r':
            print("Game restarted.")
            print("")
            board = [[" " for _ in range(3)] for _ in range(3)]
            continue

        row = int(row)
        print("")
        col = int(input("Enter the column (0, 1, 2): "))
        print("")

        if board[row][col] != " ":
            print("")
            print("Cell occupied. Choose another.")
            continue

        board[row][col] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("")
            print(f"{player_name} wins.")
            break

        if not get_empty_cells(board):
            print_board(board)
            print("")
            print("It's a draw.")
            break

        row, col = find_best_move(board)
        board[row][col] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("")
            print("Computer wins.")
            break

        if not get_empty_cells(board):
            print("")
            print_board(board)
            print("It's a draw.")
            break


if __name__ == "__main__":
    main()

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def get_move(board, player):
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if move >= 0 and move <= 8 and board[move] == " ":
            board[move] = player
            return
        print("Invalid move, try again.")

def has_winner(board):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for win in wins:
        if all(board[pos] == "X" for pos in win):
            return "X"
        if all(board[pos] == "O" for pos in win):
            return "O"
    return None

board = [" " for _ in range(9)]
display_board(board)

while True:
    get_move(board, "O")
    display_board(board)
    winner = has_winner(board)
    if winner:
        print(f"{winner} wins!")
        break

    get_move(board, "X")
    display_board(board)
    winner = has_winner(board)
    if winner:
        print(f"{winner} wins!")
        break

# tictactoe.py
def create_board():
    return [" " for _ in range(9)]

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i+1] + "|" + board[i+2])
    print()

def is_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in cond) for cond in win_conditions)

def is_draw(board):
    return " " not in board and not is_winner(board, "X") and not is_winner(board, "O")

def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]

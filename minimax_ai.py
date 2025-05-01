# minimax_ai.py
from tictactoe import is_winner, is_draw, get_available_moves

def minimax(board, is_maximizing):
    if is_winner(board, "O"): return 1
    if is_winner(board, "X"): return -1
    if is_draw(board): return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -float("inf")
    best_move = None
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

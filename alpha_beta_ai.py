from tictactoe import is_winner, is_draw, get_available_moves

def alpha_beta(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, "O"): return 1
    if is_winner(board, "X"): return -1
    if is_draw(board): return 0

    if is_maximizing:
        max_eval = -float("inf")
        for move in get_available_moves(board):
            board[move] = "O"
            eval = alpha_beta(board, depth + 1, alpha, beta, False)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in get_available_moves(board):
            board[move] = "X"
            eval = alpha_beta(board, depth + 1, alpha, beta, True)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_score = -float("inf")
    best_move = None
    for move in get_available_moves(board):
        board[move] = "O"
        score = alpha_beta(board, 0, -float("inf"), float("inf"), False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

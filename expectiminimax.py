from tictactoe import is_winner, is_draw, get_available_moves

def expectiminimax(board, is_maximizing, max_player):
    opponent = "X" if max_player == "O" else "O"

    if is_winner(board, "X"):
        return -1
    elif is_winner(board, "O"):
        return 1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for move in get_available_moves(board):
            # Simulate chance node after the move
            board_success = board[:]
            board_fail = board[:]

            board_success[move] = max_player
            score_success = expectiminimax(board_success, False, max_player)

            board_fail[move] = " "  # move gets canceled
            score_fail = expectiminimax(board_fail, False, max_player)

            expected_score = 0.7 * score_success + 0.3 * score_fail

            best_score = max(best_score, expected_score)

        return best_score

    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move] = opponent
            score = expectiminimax(board, True, max_player)
            board[move] = " "
            best_score = min(best_score, score)

        return best_score


def get_best_move(board):
    best_score = float("-inf")
    best_move = None
    for move in get_available_moves(board):
        board_success = board[:]
        board_fail = board[:]

        board_success[move] = "O"
        score_success = expectiminimax(board_success, False, "O")

        board_fail[move] = " "
        score_fail = expectiminimax(board_fail, False, "O")

        expected_score = 0.7 * score_success + 0.3 * score_fail

        if expected_score > best_score:
            best_score = expected_score
            best_move = move
        print(f"AI evaluating move {move} → Expected Score: {expected_score:.2f}")

    return best_move

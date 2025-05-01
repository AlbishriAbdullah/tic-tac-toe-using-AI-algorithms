# main.py

from tictactoe import create_board, print_board, is_winner, is_draw, get_available_moves
from minimax_ai import get_best_move as minimax_move
from alpha_beta_ai import get_best_move as alpha_beta_move
import random

def random_ai_move(board):
    return random.choice(get_available_moves(board))

def get_ai_move(board, strategy):
    if strategy == "easy":
        return random_ai_move(board)
    elif strategy == "medium":
        return minimax_move(board)
    elif strategy == "hard":
        return alpha_beta_move(board)

def main():
    print("Welcome to Tic-Tac-Toe! (You are X, AI is O)")
    print("Choose difficulty:")
    print("1 - Easy (Random)")
    print("2 - Medium (Minimax)")
    print("3 - Hard (Alpha-Beta Pruning)")

    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        strategy = "easy"
    elif choice == "2":
        strategy = "medium"
    elif choice == "3":
        strategy = "hard"
    else:
        print("Invalid input. Defaulting to Medium.")
        strategy = "medium"

    board = create_board()

    while True:
        print_board(board)
        move = int(input("Your move (0-8): "))
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"

        if is_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = get_ai_move(board, strategy)
        board[ai_move] = "O"
        print(f"AI chooses position {ai_move}")

        if is_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()


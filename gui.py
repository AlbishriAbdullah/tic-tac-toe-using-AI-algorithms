import pygame
import sys
from minimax_ai import get_best_move as minimax_move

pygame.init()

# screen borders
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe AI")

# draw background
screen.fill(BG_COLOR)

def draw_lines():
    # horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # vertical lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

draw_lines()
def draw_symbol(row, col, player):
    centerX = col * 200 + 100
    centerY = row * 200 + 100

    if player == "X":
        # draw X
        offset = 50
        pygame.draw.line(screen, (84, 84, 84), (centerX - offset, centerY - offset),
                         (centerX + offset, centerY + offset), 15)
        pygame.draw.line(screen, (84, 84, 84), (centerX - offset, centerY + offset),
                         (centerX + offset, centerY - offset), 15)
    elif player == "O":
        # draw O
        pygame.draw.circle(screen, (242, 235, 211), (centerX, centerY), 60, 15)

pygame.display.update()

# game board state (3x3 grid)
board = [["" for _ in range(3)] for _ in range(3)]

# Player turns:
# "X" = Human
# "O" = AI
current_player = "X"


def flatten_board(board_2d):
    flat = []
    for row in board_2d:
        for cell in row:
            flat.append(cell if cell != "" else " ")
    return flat

def check_win(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_draw():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def show_message(text):
    font = pygame.font.SysFont(None, 72)
    text_surface = font.render(text, True, (255, 255, 255))
    rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text_surface, rect)
    pygame.display.update()
    pygame.time.delay(2000)  # wait 2 seconds

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = mouseY // 200
            clicked_col = mouseX // 200

            if board[clicked_row][clicked_col] == "" and current_player == "X":
                board[clicked_row][clicked_col] = "X"
                draw_symbol(clicked_row, clicked_col, "X")
                pygame.display.update()

                # let AI respond as "O"
                current_player = "O"
                pygame.time.delay(500)  # delay to mimic the real world game

                # check for draw before AI moves ( always check before moves)
                if is_draw():
                    show_message("Draw!")
                    pygame.quit()
                    sys.exit()

                flat_board = flatten_board(board)
                ai_move = minimax_move(flat_board)

                if ai_move is not None:
                    ai_row = ai_move // 3
                    ai_col = ai_move % 3

                    if board[ai_row][ai_col] == "":
                        board[ai_row][ai_col] = "O"
                        draw_symbol(ai_row, ai_col, "O")
                        pygame.display.update()

                    if check_win("O"):
                        show_message("AI Wins!")
                        pygame.quit()
                        sys.exit()
                    elif is_draw():
                        show_message("Draw!")
                        pygame.quit()
                        sys.exit()

                    current_player = "X"

            # after player move (X)
            if check_win("X"):
                show_message("You Win!")
                pygame.quit()
                sys.exit()
            elif is_draw():
                show_message("Draw!")
                pygame.quit()
                sys.exit()

            # after AI move (O)
            if check_win("O"):
                show_message("AI Wins!")
                pygame.quit()
                sys.exit()
            elif is_draw():
                show_message("Draw!")
                pygame.quit()
                sys.exit()






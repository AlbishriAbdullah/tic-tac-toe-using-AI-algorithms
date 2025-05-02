import pygame
import sys
import random
from minimax_ai import get_best_move as minimax_move
from alpha_beta_ai import get_best_move as alpha_beta_move
from expectiminimax import get_best_move as expectiminimax_move
from tictactoe import get_available_moves

pygame.mixer.init()

click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
ai_sound = pygame.mixer.Sound("assets/sounds/pop.wav")
win_sound = pygame.mixer.Sound("assets/sounds/win.wav")

pygame.init()

# screen borders
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe With AI Algorithms")

difficulty = None

def draw_lines():
    # horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # vertical lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

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

def draw_difficulty_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None,45)
    title = font.render("Choose Difficulty", True, (255, 255, 255))
    easy = font.render("1 - Easy (Random)", True, (0, 255, 0))
    medium = font.render("2 - Medium (Minimax)", True, (255, 255, 0))
    hard = font.render("3 - Hard (Alpha-Beta)", True, (255, 0, 0))
    expectiminimax = small_font.render("4 - Expectiminimax (Chance-Based)", True, (0, 200, 255))


    screen.blit(title, (WIDTH//2 - title.get_width()//2, 80))
    screen.blit(easy, (WIDTH//2 - easy.get_width()//2, 200))
    screen.blit(medium, (WIDTH//2 - medium.get_width()//2, 300))
    screen.blit(hard, (WIDTH//2 - hard.get_width()//2, 400))
    screen.blit(expectiminimax, (WIDTH // 2 - expectiminimax.get_width() // 2, 480))
    pygame.display.update()

def get_ai_move(flat_board, mode):
    if mode == "easy":
        return random.choice(get_available_moves(flat_board))
    elif mode == "medium":
        return minimax_move(flat_board)
    elif mode == "hard":
        return alpha_beta_move(flat_board)
    elif mode == "expectiminimax":
        return expectiminimax_move(flat_board)

# difficulty selection
draw_difficulty_menu()
selecting = True
while selecting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                difficulty = "easy"
                selecting = False
            elif event.key == pygame.K_2:
                difficulty = "medium"
                selecting = False
            elif event.key == pygame.K_3:
                difficulty = "hard"
                selecting = False
            elif event.key == pygame.K_4:
                difficulty = "expectiminimax"
                selecting = False

# initialize the game
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
screen.fill(BG_COLOR)
draw_lines()
pygame.display.update()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            row = mouseY // 200
            col = mouseX // 200

            if board[row][col] == "" and current_player == "X":
                board[row][col] = "X"
                click_sound.play()
                draw_symbol(row, col, "X")
                pygame.display.update()

                if check_win("X"):
                    win_sound.play()
                    show_message("You Win!")
                    pygame.quit()
                    sys.exit()
                elif is_draw():
                    show_message("Draw!")
                    pygame.quit()
                    sys.exit()

                current_player = "O"
                pygame.time.delay(300)

                if is_draw():
                    show_message("Draw!")
                    pygame.quit()
                    sys.exit()

                flat_board = flatten_board(board)
                ai_move = get_ai_move(flat_board, difficulty)

                if ai_move is not None:
                    ai_row = ai_move // 3
                    ai_col = ai_move % 3
                    if board[ai_row][ai_col] == "":
                        board[ai_row][ai_col] = "O"
                        ai_sound.play()
                        draw_symbol(ai_row, ai_col, "O")
                        pygame.display.update()

                if check_win("O"):
                    win_sound.play()
                    show_message("AI Wins!")
                    pygame.quit()
                    sys.exit()
                elif is_draw():
                    show_message("Draw!")
                    pygame.quit()
                    sys.exit()

                current_player = "X"






import numpy as np
import pygame
import sys

# Screen dimensions
WIDTH, HEIGHT = 700, 600
ROWS, COLS = 6, 7
SQUARE_SIZE = 100

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")

# Create the board
def create_board():
    return np.zeros((ROWS, COLS))

# Drop a piece in the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check if a column is valid for placing a piece
def is_valid_location(board, col):
    return board[ROWS - 1][col] == 0

# Get the next open row in the column
def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

# Print the board (for debugging purposes)
def print_board(board):
    print(np.flip(board, 0))

# Check for a winning move
def winning_move(board, piece):
    # Check horizontal
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

# Draw the board
def draw_board(board):
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (c * SQUARE_SIZE + SQUARE_SIZE // 2, r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

    for c in range(COLS):
        for r in range(ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - (r * SQUARE_SIZE + SQUARE_SIZE // 2)), SQUARE_SIZE // 2 - 5)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - (r * SQUARE_SIZE + SQUARE_SIZE // 2)), SQUARE_SIZE // 2 - 5)
    pygame.display.update()

# Main game loop
def main():
    board = create_board()
    game_over = False
    turn = 0

    draw_board(board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))

                # Player 1 input
                if turn == 0:
                    posx = event.pos[0]
                    col = posx // SQUARE_SIZE

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            print("Player 1 wins!")
                            game_over = True

                # Player 2 input
                else:
                    posx = event.pos[0]
                    col = posx // SQUARE_SIZE

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            print("Player 2 wins!")
                            game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn %= 2

                if game_over:
                    pygame.time.wait(3000)

if __name__ == "__main__":
    main()
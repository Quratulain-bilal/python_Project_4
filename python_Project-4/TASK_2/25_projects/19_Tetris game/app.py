import pygame
import random

# Screen dimensions and block size
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30

# Colors
BLACK = (0, 0, 0)
COLORS = [(0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0), (128, 0, 128)]

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Clock and grid setup
clock = pygame.time.Clock()
grid = [[BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]

def create_block():
    return {"shape": random.choice(SHAPES), "color": random.choice(COLORS), "x": 5, "y": 0}

def draw_grid_and_block(block):
    screen.fill(BLACK)
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for y, row in enumerate(block["shape"]):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, block["color"], ((block["x"] + x) * BLOCK_SIZE, (block["y"] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

def check_collision(block):
    for y, row in enumerate(block["shape"]):
        for x, cell in enumerate(row):
            if cell:
                if block["y"] + y >= len(grid) or block["x"] + x < 0 or block["x"] + x >= len(grid[0]) or grid[block["y"] + y][block["x"] + x] != BLACK:
                    return True
    return False

def place_block(block):
    for y, row in enumerate(block["shape"]):
        for x, cell in enumerate(row):
            if cell:
                grid[block["y"] + y][block["x"] + x] = block["color"]

def clear_lines():
    global grid
    new_grid = [row for row in grid if BLACK in row]
    lines_cleared = len(grid) - len(new_grid)
    grid = [[BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(lines_cleared)] + new_grid
    return lines_cleared

# Main game loop
def main():
    current_block = create_block()
    fall_time = 0
    fall_speed = 500  # Milliseconds
    score = 0
    running = True

    while running:
        fall_time += clock.get_rawtime()
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_block["x"] -= 1
                    if check_collision(current_block):
                        current_block["x"] += 1
                if event.key == pygame.K_RIGHT:
                    current_block["x"] += 1
                    if check_collision(current_block):
                        current_block["x"] -= 1
                if event.key == pygame.K_DOWN:
                    current_block["y"] += 1
                    if check_collision(current_block):
                        current_block["y"] -= 1
                if event.key == pygame.K_UP:
                    rotated = list(zip(*current_block["shape"][::-1]))
                    old_shape = current_block["shape"]
                    current_block["shape"] = rotated
                    if check_collision(current_block):
                        current_block["shape"] = old_shape

        if fall_time > fall_speed:
            fall_time = 0
            current_block["y"] += 1
            if check_collision(current_block):
                current_block["y"] -= 1
                place_block(current_block)
                score += clear_lines()
                current_block = create_block()
                if check_collision(current_block):
                    running = False

        draw_grid_and_block(current_block)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Snake block size and speed
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# Font for displaying score
font = pygame.font.SysFont(None, 35)

def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

def draw_snake(block_size, snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

def game_loop():
    # Initial position of the snake
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

    # Snake body and food
    snake_body = []
    snake_length = 1
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx != BLOCK_SIZE:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx != -BLOCK_SIZE:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy != BLOCK_SIZE:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy != -BLOCK_SIZE:
                    dx, dy = 0, BLOCK_SIZE

        # Update snake position
        x += dx
        y += dy

        # Check boundaries
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            running = False

        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Update snake body
        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check for collision with itself
        for block in snake_body[:-1]:
            if block == snake_head:
                running = False

        # Draw snake
        draw_snake(BLOCK_SIZE, snake_body)

        # Display score
        display_score(snake_length - 1)

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        # Update the display
        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
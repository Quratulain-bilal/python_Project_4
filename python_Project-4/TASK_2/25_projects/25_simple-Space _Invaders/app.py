import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5

# Enemy
enemy_size = 40
enemies = []
for i in range(5):
    enemies.append([
        random.randint(0, WIDTH - enemy_size),
        random.randint(50, 200),
        2  # Speed
    ])

# Bullet
bullet_size = 5
bullet_speed = 7
bullet_state = "ready"  # "ready" or "fired"
bullet_x, bullet_y = 0, 0

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_state = "fired"
                bullet_x = player_x + player_size // 2
                bullet_y = player_y
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    # Enemy movement
    for enemy in enemies[:]:
        enemy[0] += enemy[2]
        
        # Enemy boundaries
        if enemy[0] <= 0 or enemy[0] >= WIDTH - enemy_size:
            enemy[2] *= -1
            enemy[1] += 20
        
        # Draw enemy
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))
        
        # Collision detection
        if (bullet_state == "fired" and
            enemy[0] < bullet_x < enemy[0] + enemy_size and
            enemy[1] < bullet_y < enemy[1] + enemy_size):
            bullet_state = "ready"
            enemies.remove(enemy)
            score += 10
            # Add new enemy
            enemies.append([
                random.randint(0, WIDTH - enemy_size),
                random.randint(50, 200),
                2
            ])
    
    # Bullet movement
    if bullet_state == "fired":
        pygame.draw.rect(screen, GREEN, (bullet_x, bullet_y, bullet_size, bullet_size))
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"
    
    # Draw player
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
import pygame
import socket
import threading

# Screen dimensions
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Game")

# Player positions
my_pos = [100, 300]
other_pos = [600, 300]

# Network setup
HOST = '127.0.0.1'  # Server IP
PORT = 5555         # Server port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
try:
    client.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")
except Exception as e:
    print(f"Failed to connect: {e}")
    exit()

# Receive data from the server
def receive_data():
    global other_pos
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if not data:
                break
            x, y = map(int, data.split(','))
            other_pos = [x, y]
        except:
            print("Disconnected from server")
            break

# Start receiving data in a separate thread
thread = threading.Thread(target=receive_data)
thread.start()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        my_pos[0] += 5
    if keys[pygame.K_UP]:
        my_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        my_pos[1] += 5

    # Send player position to the server
    client.send(f"{my_pos[0]},{my_pos[1]}".encode('utf-8'))

    # Draw players
    pygame.draw.rect(screen, RED, (*my_pos, PLAYER_SIZE, PLAYER_SIZE))       # My player
    pygame.draw.rect(screen, BLUE, (*other_pos, PLAYER_SIZE, PLAYER_SIZE))   # Other player

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

client.close()
pygame.quit()
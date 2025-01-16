import pygame
import sys

WIDTH, HEIGHT = 600, 600
TILE_SIZE = 30
FPS = 60

# Renlar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Labirint (1 - diywal, 0 - jol)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Oyinshinin baslangish pozitsiyasi
player_pos = [1, 1]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirint Topish O'yini")
clock = pygame.time.Clock()

def draw_maze():
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

def draw_player():
    rect = pygame.Rect(player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, GREEN, rect)

# Oyin loopi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and maze[player_pos[1] - 1][player_pos[0]] == 0:
        player_pos[1] -= 1
    if keys[pygame.K_DOWN] and maze[player_pos[1] + 1][player_pos[0]] == 0:
        player_pos[1] += 1
    if keys[pygame.K_LEFT] and maze[player_pos[1]][player_pos[0] - 1] == 0:
        player_pos[0] -= 1
    if keys[pygame.K_RIGHT] and maze[player_pos[1]][player_pos[0] + 1] == 0:
        player_pos[0] += 1

    screen.fill(WHITE)
    draw_maze()
    draw_player()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()


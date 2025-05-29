import pygame
import sys

# === COSTANTI ===
WIDTH, HEIGHT = 800, 600
RECT_WIDTH, RECT_HEIGHT = 200, 150
PLATFORM_WIDTH = 300
PLATFORM_HEIGHT = 30
PLATFORM_X = 300
PLATFORM_Y = HEIGHT - PLATFORM_HEIGHT
GRAVITY = 0.2
FRICTION = 0.99
BOUNCE = 0.7
FPS = 50

# COLORI
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# === INIZIALIZZAZIONE ===
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Demo Pygame")
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

# === STATO INIZIALE ===
x, y = 100, 100
vx, vy = 1, 2
message = ""

# === FUNZIONI ===

def landed():
    return y >= HEIGHT - RECT_HEIGHT

def within_platform():
    return x > PLATFORM_X and x + RECT_WIDTH < PLATFORM_X + PLATFORM_WIDTH

def update_physics():
    global x, y, vx, vy, message

    x += vx
    y += vy

    # Rimbalzi laterali
    if x > WIDTH - RECT_WIDTH:
        vx = -vx * BOUNCE
        x = WIDTH - RECT_WIDTH
    if x < 0:
        vx = -vx * BOUNCE
        x = 0

    # Rimbalzo a terra
    if y > HEIGHT - RECT_HEIGHT:
        vy = -vy * BOUNCE
        y = HEIGHT - RECT_HEIGHT
        if within_platform():
            message = "Well done!"
        else:
            message = "Oh no!"
    
    # Rimbalzo in alto
    if y < 0:
        vy = -vy * BOUNCE
        y = 0

    # Gravità e attriti
    vy += GRAVITY
    vx *= FRICTION
    vy *= FRICTION

def draw_scene():
    screen.fill(WHITE)

    # Disegna rettangolo
    rect = pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT)
    pygame.draw.rect(screen, BLUE, rect)

    # Disegna piattaforma
    pygame.draw.rect(screen, RED, (PLATFORM_X, PLATFORM_Y, PLATFORM_WIDTH, PLATFORM_HEIGHT))

    # Disegna messaggio se presente
    if message:
        text_surface = font.render(message, True, BLACK)
        screen.blit(text_surface, (20, 20))

    pygame.display.flip()

# === LOOP PRINCIPALE ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        vx += 0.1
    if keys[pygame.K_LEFT]:
        vx -= 0.1
    if keys[pygame.K_DOWN]:
        vy += 0.1
    if keys[pygame.K_UP]:
        vy -= 0.9

    update_physics()
    draw_scene()
    clock.tick(FPS)

pygame.quit()
sys.exit()
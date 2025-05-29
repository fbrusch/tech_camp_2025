import pygame
import sys
import time

# Inizializza Pygame
pygame.init()

# Imposta dimensioni e crea la finestra
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Demo Pygame")

# Definisci un colore (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Let's introduce a variable that represents the x coordinate del rettangolo

x = 100
y = 100


# also the speed is a variable now!
vx = 20
vy = 20


# Loop principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    # Disegna il rettangolo
    pygame.draw.rect(screen, BLUE, (x, y, 200, 150))

    # Aggiorna il display
    pygame.display.flip()

    # Move the rectangle a little bit on the right
    x += vx
    y += vy

    # if we reach the end of the screen, let's bounce!

    if x > 640:
        vx = -vx

    if x < 0:
        vx = -vx

    if y > 480:
        vy = -vy

    if y < 0:
        vy = -vy
    


    # wait for a bit (let's aim at 50 fps)
    time.sleep(0.02)

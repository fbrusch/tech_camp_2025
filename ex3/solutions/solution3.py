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
vx = 1
vy = 2

e = 0.95

# Loop principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Riempi lo sfondo
    screen.fill(WHITE)

    # Now the rectangle has a "variable" x!

    rect = pygame.Rect(x, y, 200, 150)

    # Disegna il rettangolo
    pygame.draw.rect(screen, BLUE, rect)

    # Aggiorna il display
    pygame.display.flip()

    # Move the rectangle a little bit on the right
    x += vx
    y += vy

    # if we reach the end of the screen, let's bounce!
    # but with anaelastic collisions!

    if x > 640:
        vx = -vx*e

    if x < 0:
        vx = -vx*e

    if y > 480:
        vy = -vy*e

    if y < 0:
        vy = -vy*e
    
    # Gravity

    vy += 0.2

    



    # wait for a bit (let's aim at 50 fps)
    time.sleep(0.02)


    

# Chiudi Pygame
pygame.quit()
sys.exit()